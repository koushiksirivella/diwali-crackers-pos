const http = require('http');
const fs = require('fs');
const path = require('path');
const { exec } = require('child_process');

const PORT = process.env.PORT || 3000;
const BASE_DIR = __dirname;
const SPREADSHEET_ID = '1swTMlDSVKEHMPwIriVmvAsmaWXIO_DxwEzQ6vI9ZFQw';

const MIME_TYPES = {
  '.html': 'text/html',
  '.css': 'text/css',
  '.js': 'application/javascript',
  '.json': 'application/json',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.svg': 'image/svg+xml',
  '.ico': 'image/x-icon',
  '.csv': 'text/csv'
};

function writeInventoryCsv(items) {
  const csvRows = [
    ['Box #', 'Bill S.No', 'Item Name', 'Bill Source', 'Pack Details', 'Total Units', 'Units Sold', 'Units In Stock', 'Wholesale Rate (₹)', 'Landed Cost (+20%) (₹)', 'Final Selling Price (3x) (₹)', 'Total Inventory Value (₹)', 'Cash Collected (₹)', 'Status']
  ];
  items.forEach((it, idx) => {
    const box = it.box_no || (idx + 1);
    const billSno = it.bill_item_no || (idx + 1);
    const name = it.name || '';
    const bill = it.bill_type === 'pink' ? 'Pink Bill (Chilakaluripet)' : 'White Bill (Nandigama)';
    const pack = it.pack_details || '1';
    const u = parseInt(it.total_units || 0);
    const s = parseInt(it.units_sold || 0);
    const left = Math.max(0, u - s);
    const rate = parseFloat(it.rate || 0);
    const c20 = parseFloat(it.rate_plus_20) || Math.round(rate * 1.20 * 100) / 100;
    const sp = parseFloat(it.selling_price) || Math.round(c20 * 3);
    const tot_val = Math.round(u * sp);
    const collected = Math.round(s * sp);
    const status = (u > 0 && left === 0) ? 'SOLD OUT' : (s === 0 ? 'IN STOCK' : `${s}/${u} SOLD`);
    csvRows.push([box, billSno, `"${name.replace(/"/g, '""')}"`, `"${bill}"`, `"${pack}"`, u, s, left, rate, c20, sp, tot_val, collected, status]);
  });
  const csvContent = csvRows.map(r => r.join(',')).join('\n');
  fs.writeFileSync(path.join(BASE_DIR, 'diwali_inventory.csv'), csvContent, 'utf8');
}

const server = http.createServer((req, res) => {
  const url = new URL(req.url, `http://${req.headers.host}`);
  const pathname = url.pathname;

  // CORS headers
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') {
    res.writeHead(204);
    return res.end();
  }

  // API: Get latest data
  if (pathname === '/api/data' && req.method === 'GET') {
    try {
      const data = fs.readFileSync(path.join(BASE_DIR, 'items_data.json'), 'utf8');
      res.writeHead(200, { 'Content-Type': 'application/json' });
      return res.end(data);
    } catch (e) {
      res.writeHead(500, { 'Content-Type': 'application/json' });
      return res.end(JSON.stringify({ error: e.message }));
    }
  }

  // API: Save and push to Google Sheets & GitHub
  if (pathname === '/api/save' && req.method === 'POST') {
    let body = '';
    req.on('data', chunk => { body += chunk; });
    req.on('end', () => {
      try {
        const parsed = JSON.parse(body);
        const itemsArray = Array.isArray(parsed) ? parsed : (Array.isArray(parsed.items) ? parsed.items : []);
        fs.writeFileSync(path.join(BASE_DIR, 'items_data.json'), JSON.stringify(itemsArray, null, 2), 'utf8');
        
        // Write CSV and sync to Google Sheets
        writeInventoryCsv(itemsArray);
        exec(`gsheets mutate import-csv ${SPREADSHEET_ID} diwali_inventory.csv && git add items_data.json diwali_inventory.csv && git commit -m "Auto-sync inventory data & Google Sheets [skip ci]" && git push origin master`, (err, stdout, stderr) => {
          if (err) {
            console.warn('Sync warning:', err.message);
          } else {
            console.log('Successfully synced to Google Sheets & pushed to GitHub!');
          }
        });

        res.writeHead(200, { 'Content-Type': 'application/json' });
        return res.end(JSON.stringify({
          success: true,
          sheet_id: SPREADSHEET_ID,
          sheet_url: `https://docs.google.com/spreadsheets/d/${SPREADSHEET_ID}/edit`,
          message: 'Saved to disk, synced to Google Sheets, and pushing to GitHub!'
        }));
      } catch (e) {
        res.writeHead(400, { 'Content-Type': 'application/json' });
        return res.end(JSON.stringify({ error: e.message }));
      }
    });
    return;
  }

  // Static File Serving
  let filePath = path.join(BASE_DIR, pathname === '/' ? 'index.html' : pathname);
  
  // URL decode path for filenames with spaces like "WhatsApp Image..."
  try {
    filePath = decodeURIComponent(filePath);
  } catch(e) {}

  fs.stat(filePath, (err, stats) => {
    if (err || !stats.isFile()) {
      res.writeHead(404, { 'Content-Type': 'text/plain' });
      return res.end('404 Not Found');
    }

    const ext = path.extname(filePath).toLowerCase();
    const contentType = MIME_TYPES[ext] || 'application/octet-stream';

    res.writeHead(200, {
      'Content-Type': contentType,
      'Access-Control-Allow-Origin': '*'
    });
    fs.createReadStream(filePath).pipe(res);
  });
});

server.listen(PORT, () => {
  console.log(`Diwali Crackers Server running on http://localhost:${PORT}`);
});
