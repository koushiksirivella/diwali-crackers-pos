import json

with open("items_data.json", "r", encoding="utf-8") as f:
    items = json.load(f)

# Sort items: White 1-74 first, then Pink P1-P20
white_items = [i for i in items if i["bill_type"] == "white"]
white_items.sort(key=lambda x: x["bill_item_no"])
pink_items = [i for i in items if i["bill_type"] == "pink"]
pink_items.sort(key=lambda x: x["bill_item_no"])
sorted_items = white_items + pink_items

items_json = json.dumps(sorted_items)

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>Diwali Crackers Price Finder</title>
  <link rel="manifest" href="manifest.json">
  <meta name="theme-color" content="#0a0a0a">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@600;700;800&display=swap" rel="stylesheet">
  <style>
    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
      -webkit-tap-highlight-color: transparent;
    }}

    body {{
      background: #0d0f12;
      color: #ffffff;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      padding: 16px 14px;
    }}

    .container {{
      width: 100%;
      max-width: 440px;
      display: flex;
      flex-direction: column;
      gap: 14px;
    }}

    /* Clean Simple Header */
    .header {{
      text-align: center;
      padding: 10px 0 4px 0;
    }}

    .header h1 {{
      font-size: 1.35rem;
      font-weight: 800;
      letter-spacing: -0.02em;
      color: #ffffff;
    }}

    .header p {{
      font-size: 0.85rem;
      color: #94a3b8;
      margin-top: 2px;
    }}

    /* Big Search Input */
    .search-section {{
      background: #161a22;
      border: 2px solid #2d3748;
      border-radius: 16px;
      padding: 12px 14px;
      display: flex;
      align-items: center;
      gap: 10px;
      transition: border-color 0.2s;
    }}

    .search-section:focus-within {{
      border-color: #fbbf24;
      box-shadow: 0 0 16px rgba(251, 191, 36, 0.2);
    }}

    .search-icon {{
      font-size: 1.2rem;
      color: #fbbf24;
    }}

    .search-input {{
      width: 100%;
      background: transparent;
      border: none;
      color: #ffffff;
      font-size: 1.3rem;
      font-weight: 700;
      outline: none;
      font-family: 'JetBrains Mono', monospace;
    }}

    .search-input::placeholder {{
      color: #4b5563;
      font-size: 0.95rem;
      font-family: 'Inter', sans-serif;
      font-weight: 500;
    }}

    .btn-clear {{
      background: #242b38;
      border: none;
      color: #9ca3af;
      width: 28px;
      height: 28px;
      border-radius: 50%;
      font-size: 0.9rem;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
    }}

    /* MAIN RESULT CARD */
    .result-card {{
      background: #161b24;
      border: 2px solid #232c3d;
      border-radius: 20px;
      padding: 20px;
      box-shadow: 0 10px 25px rgba(0,0,0,0.4);
      display: flex;
      flex-direction: column;
      gap: 14px;
      position: relative;
    }}

    .card-top {{
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}

    .sticker-pill {{
      background: #fbbf24;
      color: #000000;
      font-weight: 900;
      font-size: 1.25rem;
      font-family: 'JetBrains Mono', monospace;
      padding: 4px 14px;
      border-radius: 10px;
      letter-spacing: -0.02em;
    }}

    .sticker-pill.pink {{
      background: #f43f5e;
      color: #ffffff;
    }}

    .bill-source-text {{
      font-size: 0.75rem;
      font-weight: 700;
      text-transform: uppercase;
      color: #64748b;
      letter-spacing: 0.05em;
    }}

    .product-name {{
      font-size: 1.6rem;
      font-weight: 800;
      color: #ffffff;
      line-height: 1.2;
    }}

    .units-row {{
      display: flex;
      gap: 12px;
      font-size: 0.95rem;
      color: #cbd5e1;
    }}

    .units-row strong {{
      color: #fbbf24;
      font-family: 'JetBrains Mono', monospace;
    }}

    /* The Cost Box */
    .costs-box {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 10px;
      background: #0e1218;
      border: 1px solid #242c3b;
      border-radius: 12px;
      padding: 12px;
    }}

    .cost-item .lbl {{
      font-size: 0.72rem;
      text-transform: uppercase;
      color: #64748b;
      font-weight: 700;
      margin-bottom: 2px;
    }}

    .cost-item .val {{
      font-size: 1.35rem;
      font-weight: 800;
      font-family: 'JetBrains Mono', monospace;
      color: #ffffff;
    }}

    .cost-item.highlight .val {{
      color: #fbbf24;
    }}

    /* SELLING PRICE BANNER */
    .sell-banner {{
      background: linear-gradient(135deg, #064e3b 0%, #065f46 100%);
      border: 2px solid #10b981;
      border-radius: 14px;
      padding: 14px;
      text-align: center;
      display: flex;
      flex-direction: column;
      gap: 4px;
    }}

    .sell-banner .lbl {{
      font-size: 0.75rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      color: #a7f3d0;
    }}

    .sell-banner .price {{
      font-size: 2.8rem;
      font-weight: 900;
      color: #ffffff;
      font-family: 'JetBrains Mono', monospace;
      line-height: 1;
      margin: 4px 0;
    }}

    .sell-banner .profit {{
      font-size: 0.85rem;
      color: #d1fae5;
      font-weight: 600;
    }}

    /* Change Price Toggle (Optional) */
    .edit-price-btn {{
      background: transparent;
      border: 1px dashed rgba(255,255,255,0.2);
      color: #94a3b8;
      border-radius: 8px;
      padding: 6px;
      font-size: 0.78rem;
      cursor: pointer;
      text-align: center;
    }}

    .custom-price-input-wrap {{
      display: none;
      margin-top: 6px;
      gap: 8px;
    }}

    .custom-price-input-wrap.open {{
      display: flex;
    }}

    .custom-price-input {{
      flex: 1;
      background: #000;
      border: 1px solid #10b981;
      border-radius: 8px;
      padding: 8px 12px;
      color: #fff;
      font-size: 1.2rem;
      font-weight: 800;
      font-family: 'JetBrains Mono', monospace;
      outline: none;
    }}

    .btn-save-price {{
      background: #10b981;
      color: #000;
      border: none;
      border-radius: 8px;
      padding: 0 16px;
      font-weight: 800;
      cursor: pointer;
    }}

    /* FAST NUMPAD */
    .numpad {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 8px;
      margin-top: 4px;
    }}

    .btn-num {{
      height: 52px;
      background: #181d26;
      border: 1px solid #283243;
      border-radius: 12px;
      color: #ffffff;
      font-size: 1.5rem;
      font-weight: 700;
      font-family: 'JetBrains Mono', monospace;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      user-select: none;
      touch-action: manipulation;
    }}

    .btn-num:active {{
      background: #fbbf24;
      color: #000000;
      transform: scale(0.95);
    }}

    .btn-num.pink-key {{
      color: #f43f5e;
      font-weight: 800;
      font-size: 1.2rem;
    }}

    .btn-num.del-key {{
      color: #94a3b8;
      font-size: 1.1rem;
    }}

    /* BOTTOM CHEATSHEET BUTTON */
    .btn-sheet-toggle {{
      width: 100%;
      background: #161b24;
      border: 1px solid #283243;
      color: #e2e8f0;
      border-radius: 12px;
      padding: 12px;
      font-size: 0.9rem;
      font-weight: 700;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      margin-top: 4px;
    }}

    .btn-sheet-toggle:hover {{
      border-color: #fbbf24;
    }}

    /* FULL TABLE MODAL / CHEATSHEET */
    .table-sheet {{
      display: none;
      position: fixed;
      inset: 0;
      background: #0d0f12;
      z-index: 100;
      flex-direction: column;
      padding: 16px;
      overflow-y: auto;
    }}

    .table-sheet.open {{
      display: flex;
    }}

    .table-header-row {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 14px;
    }}

    .table-header-row h2 {{
      font-size: 1.2rem;
      font-weight: 800;
    }}

    .btn-close-sheet {{
      background: #242c3b;
      border: none;
      color: #fff;
      padding: 6px 14px;
      border-radius: 8px;
      font-weight: 700;
      cursor: pointer;
    }}

    .sheet-search {{
      background: #181d26;
      border: 1px solid #283243;
      border-radius: 10px;
      padding: 10px 14px;
      color: #fff;
      font-size: 1rem;
      margin-bottom: 12px;
      outline: none;
      width: 100%;
    }}

    .simple-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.88rem;
    }}

    .simple-table th {{
      background: #161b24;
      color: #94a3b8;
      text-align: left;
      padding: 10px 8px;
      font-size: 0.75rem;
      text-transform: uppercase;
      border-bottom: 2px solid #283243;
    }}

    .simple-table td {{
      padding: 10px 8px;
      border-bottom: 1px solid #1f2735;
      font-family: 'JetBrains Mono', monospace;
    }}

    .simple-table tr:hover {{
      background: rgba(251, 191, 36, 0.05);
    }}

    .td-name {{
      font-family: 'Inter', sans-serif !important;
      font-weight: 600;
      color: #fff;
    }}

    .td-num {{
      font-weight: 800;
      color: #fbbf24;
    }}

    .td-num.pink {{
      color: #f43f5e;
    }}

    .td-price {{
      font-weight: 800;
      color: #34d399;
      font-size: 1rem;
    }}
  </style>
</head>
<body>

  <div class="container">
    
    <!-- Clean Header -->
    <div class="header">
      <h1>Diwali Crackers Price Finder</h1>
      <p>Look at box sticker ➔ Type number below ➔ Write price</p>
    </div>

    <!-- Search Input Bar -->
    <div class="search-section">
      <span class="search-icon">🔍</span>
      <input type="text" id="main-input" class="search-input" placeholder="Enter sticker # (e.g. 33, 1, P5)..." autocomplete="off" autofocus>
      <button class="btn-clear" onclick="clearInput()">✕</button>
    </div>

    <!-- THE SINGLE CARD (Clean, Instant, Uncluttered) -->
    <div class="result-card" id="card">
      <div class="card-top">
        <div class="sticker-pill" id="sticker-pill">#1</div>
        <div class="bill-source-text" id="bill-source">White Bill</div>
      </div>

      <div class="product-name" id="product-name">3 1/2 Lakshmi (15P)</div>

      <div class="units-row">
        <span>Units in Box: <strong id="box-units">20</strong></span>
        <span style="color: #64748b;">•</span>
        <span id="pack-info" style="color: #94a3b8;">Pack: 20</span>
      </div>

      <!-- Cost You Paid vs Cost + 10% Overhead -->
      <div class="costs-box">
        <div class="cost-item">
          <div class="lbl">Wholesale Cost</div>
          <div class="val" id="wholesale-val">₹150</div>
        </div>
        <div class="cost-item highlight">
          <div class="lbl">Cost + 10% Overhead</div>
          <div class="val" id="cost10-val">₹165</div>
        </div>
      </div>

      <!-- THE SELLING PRICE (The ONLY thing to write on the box) -->
      <div class="sell-banner">
        <div class="lbl">Write This Price on Box:</div>
        <div class="price" id="selling-price-val">₹250</div>
        <div class="profit" id="profit-val">Your Profit: +₹85 / piece (+₹1,700 on box)</div>
      </div>

      <!-- Optional Custom Price Editor -->
      <button class="edit-price-btn" onclick="toggleEditPrice()">✏️ Change Selling Price for this item</button>
      <div class="custom-price-input-wrap" id="custom-price-wrap">
        <input type="number" id="custom-price-input" class="custom-price-input" placeholder="New price">
        <button class="btn-save-price" onclick="saveCustomPrice()">Save</button>
      </div>

    </div>

    <!-- TOUCH NUMPAD FOR FAST 1-HAND PHONE USE -->
    <div class="numpad">
      <button class="btn-num" onclick="tap('1')">1</button>
      <button class="btn-num" onclick="tap('2')">2</button>
      <button class="btn-num" onclick="tap('3')">3</button>
      <button class="btn-num" onclick="tap('4')">4</button>
      <button class="btn-num" onclick="tap('5')">5</button>
      <button class="btn-num" onclick="tap('6')">6</button>
      <button class="btn-num" onclick="tap('7')">7</button>
      <button class="btn-num" onclick="tap('8')">8</button>
      <button class="btn-num" onclick="tap('9')">9</button>
      <button class="btn-num pink-key" onclick="tap('P')">P</button>
      <button class="btn-num" onclick="tap('0')">0</button>
      <button class="btn-num del-key" onclick="tap('DEL')">⌫</button>
    </div>

    <!-- CHEATSHEET BUTTON -->
    <button class="btn-sheet-toggle" onclick="openTableSheet()">
      <span>📋</span> View Complete Cheatsheet (All 94 Items)
    </button>

  </div>

  <!-- COMPLETE CHEATSHEET MODAL -->
  <div class="table-sheet" id="table-sheet">
    <div class="table-header-row">
      <h2>Complete Price Cheatsheet (94 Items)</h2>
      <button class="btn-close-sheet" onclick="closeTableSheet()">✕ Close</button>
    </div>
    <input type="text" class="sheet-search" id="sheet-search" placeholder="Filter by name or number..." oninput="filterSheet(this.value)">
    <table class="simple-table">
      <thead>
        <tr>
          <th>Sticker #</th>
          <th>Item Name</th>
          <th>Units</th>
          <th>Wholesale</th>
          <th>Cost + 10%</th>
          <th>Sell Price</th>
        </tr>
      </thead>
      <tbody id="sheet-tbody">
        <!-- Rendered by JS -->
      </tbody>
    </table>
  </div>

  <script>
    const ITEMS = {items_json};
    let currentItem = ITEMS[0];

    // Load saved prices if user edited any
    const savedCustomPrices = JSON.parse(localStorage.getItem('diwali_custom_prices') || '{{}}');
    ITEMS.forEach(it => {{
      if (savedCustomPrices[it.id] !== undefined) {{
        it.selling_price = savedCustomPrices[it.id];
      }}
    }});

    const input = document.getElementById('main-input');

    input.addEventListener('input', (e) => {{
      lookup(e.target.value.trim());
    }});

    function tap(val) {{
      if (val === 'DEL') {{
        input.value = input.value.slice(0, -1);
      }} else {{
        input.value += val;
      }}
      lookup(input.value.trim());
    }}

    function clearInput() {{
      input.value = '';
      input.focus();
    }}

    function lookup(term) {{
      if (!term) return;
      const q = term.toLowerCase();

      // 1. Exact sticker match
      let match = ITEMS.find(it => it.sticker_no.toLowerCase() === q);

      // 2. Exact match without 'p'
      if (!match) {{
        match = ITEMS.find(it => it.search_keys && it.search_keys.includes(q));
      }}

      // 3. Name contains
      if (!match) {{
        match = ITEMS.find(it => it.name.toLowerCase().includes(q));
      }}

      if (match) {{
        renderCard(match);
      }}
    }}

    function renderCard(item) {{
      currentItem = item;
      const pill = document.getElementById('sticker-pill');
      pill.textContent = '#' + item.sticker_no;
      if (item.bill_type === 'pink') {{
        pill.className = 'sticker-pill pink';
        document.getElementById('bill-source').textContent = 'Pink Bill (Chinna Pasumarru)';
      }} else {{
        pill.className = 'sticker-pill';
        document.getElementById('bill-source').textContent = 'White Bill (Nandigama)';
      }}

      document.getElementById('product-name').textContent = item.name;
      document.getElementById('box-units').textContent = item.units;
      document.getElementById('pack-info').textContent = 'Pack: ' + item.pack_details;
      document.getElementById('wholesale-val').textContent = '₹' + item.rate;
      document.getElementById('cost10-val').textContent = '₹' + Math.round(item.rate_plus_10);
      document.getElementById('selling-price-val').textContent = '₹' + item.selling_price;

      const profitPerUnit = item.selling_price - item.rate_plus_10;
      const totalBoxProfit = Math.round(profitPerUnit * item.units);
      document.getElementById('profit-val').textContent = 
        `Your Profit: +₹${{Math.round(profitPerUnit)}} / piece (+₹${{totalBoxProfit.toLocaleString('en-IN')}} on box)`;
    }}

    function toggleEditPrice() {{
      const wrap = document.getElementById('custom-price-wrap');
      wrap.classList.toggle('open');
      if (wrap.classList.contains('open')) {{
        const pInput = document.getElementById('custom-price-input');
        pInput.value = currentItem.selling_price;
        pInput.focus();
      }}
    }}

    function saveCustomPrice() {{
      const newP = parseFloat(document.getElementById('custom-price-input').value);
      if (newP && newP > 0) {{
        currentItem.selling_price = newP;
        savedCustomPrices[currentItem.id] = newP;
        localStorage.setItem('diwali_custom_prices', JSON.stringify(savedCustomPrices));
        renderCard(currentItem);
        renderSheetTable();
        document.getElementById('custom-price-wrap').classList.remove('open');
      }}
    }}

    // Cheatsheet modal
    function openTableSheet() {{
      renderSheetTable();
      document.getElementById('table-sheet').classList.add('open');
    }}

    function closeTableSheet() {{
      document.getElementById('table-sheet').classList.remove('open');
    }}

    function renderSheetTable(filter = '') {{
      const tbody = document.getElementById('sheet-tbody');
      tbody.innerHTML = '';
      const f = filter.toLowerCase();

      ITEMS.forEach(it => {{
        if (f && !it.name.toLowerCase().includes(f) && !it.sticker_no.toLowerCase().includes(f)) {{
          return;
        }}
        const tr = document.createElement('tr');
        tr.innerHTML = `
          <td class="td-num ${{it.bill_type==='pink'?'pink':''}}">#${{it.sticker_no}}</td>
          <td class="td-name">${{it.name}}</td>
          <td>${{it.units}}</td>
          <td>₹${{it.rate}}</td>
          <td style="color:#fbbf24">₹${{Math.round(it.rate_plus_10)}}</td>
          <td class="td-price">₹${{it.selling_price}}</td>
        `;
        tr.onclick = () => {{
          renderCard(it);
          input.value = it.sticker_no;
          closeTableSheet();
        }};
        tbody.appendChild(tr);
      }});
    }}

    function filterSheet(val) {{
      renderSheetTable(val);
    }}

    // Initial render
    renderCard(ITEMS[0]);
  </script>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Radically simple index.html built successfully!")
