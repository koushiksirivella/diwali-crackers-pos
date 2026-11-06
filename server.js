const http = require('http');
const fs = require('fs');
const path = require('path');
const { exec } = require('child_process');

const PORT = process.env.PORT || 3000;
const BASE_DIR = __dirname;

const MIME_TYPES = {
  '.html': 'text/html',
  '.css': 'text/css',
  '.js': 'application/javascript',
  '.json': 'application/json',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.svg': 'image/svg+xml',
  '.ico': 'image/x-icon'
};

const server = http.createServer((req, res) => {
  const url = new URL(req.url, `http://${req.headers.host}`);
  const pathname = url.pathname;

  // API: Get latest data
  if (pathname === '/api/data' && req.method === 'GET') {
    try {
      const data = fs.readFileSync(path.join(BASE_DIR, 'items_data.json'), 'utf8');
      res.writeHead(200, { 'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*' });
      return res.end(data);
    } catch (e) {
      res.writeHead(500, { 'Content-Type': 'application/json' });
      return res.end(JSON.stringify({ error: e.message }));
    }
  }

  // API: Save and push to GitHub
  if (pathname === '/api/save' && req.method === 'POST') {
    let body = '';
    req.on('data', chunk => { body += chunk; });
    req.on('end', () => {
      try {
        const parsed = JSON.parse(body);
        fs.writeFileSync(path.join(BASE_DIR, 'items_data.json'), JSON.stringify(parsed, null, 2), 'utf8');
        
        // Auto Git commit & push in background
        exec('git add items_data.json && git commit -m "Auto-sync inventory data [skip ci]" && git push origin master', (err, stdout, stderr) => {
          if (err) {
            console.warn('Git sync warning (local saved successfully):', err.message);
          } else {
            console.log('Successfully pushed updated data to GitHub!');
          }
        });

        res.writeHead(200, { 'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*' });
        return res.end(JSON.stringify({ success: true, message: 'Saved to disk and syncing to GitHub!' }));
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
