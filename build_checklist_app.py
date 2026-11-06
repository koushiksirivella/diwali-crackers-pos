import json

with open("items_data.json", "r", encoding="utf-8") as f:
    items = json.load(f)

# Sort: White 1-74, then Pink 1-20
white_items = [i for i in items if i["bill_type"] == "white"]
white_items.sort(key=lambda x: x["bill_item_no"])
pink_items = [i for i in items if i["bill_type"] == "pink"]
pink_items.sort(key=lambda x: x["bill_item_no"])
all_sorted = white_items + pink_items

# Ensure fields: total_units, units_sold, rate, rate_plus_10, selling_price, verified
for it in all_sorted:
    it["total_units"] = it["units"]
    it["units_sold"] = it.get("units_sold", 0)

items_json_str = json.dumps(all_sorted)

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>Diwali Crackers Checklist & Pricing Tracker</title>
  <link rel="manifest" href="manifest.json">
  <meta name="theme-color" content="#0b0f17">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;600;700;800&display=swap" rel="stylesheet">
  <style>
    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      font-family: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;
      -webkit-tap-highlight-color: transparent;
    }}

    body {{
      background: #0b0f17;
      color: #f1f5f9;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      padding: 12px 10px 40px 10px;
    }}

    .app-container {{
      width: 100%;
      max-width: 600px;
      display: flex;
      flex-direction: column;
      gap: 12px;
    }}

    /* Top Sticky Header */
    .top-header {{
      background: #111827;
      border: 1px solid #1f293d;
      border-radius: 16px;
      padding: 14px 16px;
      display: flex;
      flex-direction: column;
      gap: 10px;
      position: sticky;
      top: 10px;
      z-index: 50;
      box-shadow: 0 10px 25px rgba(0,0,0,0.5);
    }}

    .header-title-row {{
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}

    .header-title-row h1 {{
      font-size: 1.15rem;
      font-weight: 800;
      color: #fff;
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    .progress-pill {{
      background: #064e3b;
      border: 1px solid #10b981;
      color: #34d399;
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.8rem;
      font-weight: 700;
      padding: 4px 10px;
      border-radius: 999px;
    }}

    /* Search Box */
    .search-bar-wrap {{
      display: flex;
      align-items: center;
      background: #090d14;
      border: 2px solid #243048;
      border-radius: 12px;
      padding: 8px 12px;
      gap: 8px;
    }}

    .search-bar-wrap:focus-within {{
      border-color: #fbbf24;
    }}

    .search-bar-wrap input {{
      width: 100%;
      background: transparent;
      border: none;
      color: #fff;
      font-size: 1.1rem;
      font-weight: 700;
      outline: none;
      font-family: 'JetBrains Mono', monospace;
    }}

    .search-bar-wrap input::placeholder {{
      font-size: 0.85rem;
      color: #64748b;
      font-family: 'Plus Jakarta Sans', sans-serif;
      font-weight: 500;
    }}

    .clear-search-btn {{
      background: #1e293b;
      border: none;
      color: #94a3b8;
      width: 26px;
      height: 26px;
      border-radius: 50%;
      cursor: pointer;
      font-size: 0.85rem;
      display: flex;
      align-items: center;
      justify-content: center;
    }}

    /* Filter Pills */
    .filter-pills-row {{
      display: flex;
      gap: 6px;
      overflow-x: auto;
      scrollbar-width: none;
    }}
    .filter-pills-row::-webkit-scrollbar {{ display: none; }}

    .f-pill {{
      background: #182234;
      border: 1px solid #27354f;
      color: #94a3b8;
      font-size: 0.75rem;
      font-weight: 700;
      padding: 5px 10px;
      border-radius: 8px;
      cursor: pointer;
      white-space: nowrap;
      transition: all 0.15s;
    }}

    .f-pill.active {{
      background: #fbbf24;
      color: #000;
      border-color: #fbbf24;
    }}

    /* Summary Bar */
    .summary-strip {{
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 6px;
      background: #111827;
      border: 1px solid #1f293d;
      border-radius: 12px;
      padding: 10px;
      text-align: center;
    }}

    .sum-cell .lbl {{
      font-size: 0.65rem;
      text-transform: uppercase;
      font-weight: 700;
      color: #64748b;
      margin-bottom: 2px;
    }}

    .sum-cell .val {{
      font-size: 0.95rem;
      font-weight: 800;
      font-family: 'JetBrains Mono', monospace;
      color: #fff;
    }}

    .sum-cell.highlight .val {{
      color: #34d399;
    }}

    /* CHECKLIST ITEMS CONTAINER */
    .checklist-container {{
      display: flex;
      flex-direction: column;
      gap: 10px;
    }}

    /* INDIVIDUAL ITEM CARD */
    .item-card {{
      background: #111827;
      border: 1.5px solid #1f293d;
      border-radius: 14px;
      padding: 12px 14px;
      display: flex;
      flex-direction: column;
      gap: 10px;
      transition: all 0.2s ease;
      position: relative;
    }}

    .item-card.is-ticked {{
      background: #0d1724;
      border-color: #10b981;
    }}

    /* Top Row: Checkbox + Number + Name */
    .item-header-row {{
      display: flex;
      align-items: center;
      gap: 10px;
    }}

    /* Custom Checkbox */
    .tick-box-wrap {{
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
    }}

    .custom-tick {{
      width: 26px;
      height: 26px;
      border-radius: 8px;
      border: 2px solid #475569;
      background: #090d14;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1rem;
      font-weight: 900;
      color: transparent;
      transition: all 0.15s;
    }}

    .item-card.is-ticked .custom-tick {{
      background: #10b981;
      border-color: #10b981;
      color: #000;
    }}

    .box-badge {{
      background: #fbbf24;
      color: #000;
      font-family: 'JetBrains Mono', monospace;
      font-weight: 900;
      font-size: 1rem;
      padding: 3px 8px;
      border-radius: 6px;
      letter-spacing: -0.02em;
      flex-shrink: 0;
    }}

    .box-badge.pink {{
      background: #f43f5e;
      color: #fff;
    }}

    .item-title-wrap {{
      flex: 1;
      min-width: 0;
    }}

    .item-title-wrap .name {{
      font-size: 1.05rem;
      font-weight: 800;
      color: #fff;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }}

    .item-title-wrap .sub {{
      font-size: 0.72rem;
      color: #64748b;
    }}

    /* The 4 Core Editable Columns Grid */
    .item-stats-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr 1fr 1.25fr;
      gap: 6px;
      background: #090d14;
      border: 1px solid #1e293b;
      border-radius: 10px;
      padding: 8px;
    }}

    .stat-col {{
      display: flex;
      flex-direction: column;
      justify-content: center;
    }}

    .stat-col .lbl {{
      font-size: 0.65rem;
      text-transform: uppercase;
      font-weight: 700;
      color: #64748b;
      margin-bottom: 3px;
    }}

    /* Editable Input Fields */
    .stat-input {{
      width: 100%;
      background: #162032;
      border: 1px solid #27354f;
      border-radius: 6px;
      color: #fff;
      font-size: 0.95rem;
      font-weight: 700;
      font-family: 'JetBrains Mono', monospace;
      padding: 4px 6px;
      outline: none;
      text-align: center;
    }}

    .stat-input:focus {{
      border-color: #fbbf24;
      background: #1c283e;
    }}

    /* Units Sold Counter (+ / -) */
    .sold-counter-wrap {{
      display: flex;
      align-items: center;
      gap: 2px;
    }}

    .btn-step {{
      width: 22px;
      height: 28px;
      background: #1e293b;
      border: 1px solid #334155;
      color: #cbd5e1;
      border-radius: 4px;
      font-size: 0.85rem;
      font-weight: 800;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
    }}

    .btn-step:active {{
      background: #fbbf24;
      color: #000;
    }}

    .stat-input.sold-input {{
      width: 36px;
      padding: 4px 2px;
    }}

    /* Selling Price Column Highlight */
    .stat-col.sell-col {{
      border-left: 1px dashed #243048;
      padding-left: 6px;
    }}

    .stat-input.sp-input {{
      background: #064e3b;
      border-color: #059669;
      color: #34d399;
      font-size: 1.05rem;
      font-weight: 800;
    }}

    .stat-input.sp-input:focus {{
      border-color: #34d399;
      box-shadow: 0 0 8px rgba(52, 211, 153, 0.4);
    }}

    /* Profit Footer Row */
    .item-footer-row {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 0.75rem;
      font-family: 'JetBrains Mono', monospace;
      color: #94a3b8;
      padding-top: 2px;
    }}

    .profit-text {{
      color: #34d399;
      font-weight: 700;
    }}

    .profit-text.negative {{
      color: #f87171;
    }}

    /* Empty state */
    .empty-state {{
      text-align: center;
      padding: 40px 10px;
      color: #64748b;
      font-size: 0.95rem;
    }}
  </style>
</head>
<body>

  <div class="app-container">
    
    <!-- STICKY TOP CONTROLS -->
    <header class="top-header">
      <div class="header-title-row">
        <h1><span>🪔</span> Diwali Box Checklist</h1>
        <div class="progress-pill" id="header-progress">0 / 94 Ticked</div>
      </div>

      <!-- Search Box: e.g. type '46' or 'GLC' -->
      <div class="search-bar-wrap">
        <span style="color: #fbbf24; font-size: 1rem;">🔍</span>
        <input type="text" id="box-search" placeholder="Search Box # (e.g. 46, 33, P5) or Name..." autocomplete="off">
        <button class="clear-search-btn" onclick="clearSearch()">✕</button>
      </div>

      <!-- Quick Filter Pills -->
      <div class="filter-pills-row">
        <button class="f-pill active" onclick="setFilter('all')">All (94)</button>
        <button class="f-pill" onclick="setFilter('pending')">Pending Boxes</button>
        <button class="f-pill" onclick="setFilter('done')">Ticked (Done)</button>
        <button class="f-pill" onclick="setFilter('white')">White Bill (1–74)</button>
        <button class="f-pill" onclick="setFilter('pink')">Pink Bill (P1–P20)</button>
      </div>
    </header>

    <!-- LIVE SUMMARY METRICS -->
    <section class="summary-strip">
      <div class="sum-cell">
        <div class="lbl">Total Units</div>
        <div class="val" id="sum-total-units">3,925</div>
      </div>
      <div class="sum-cell">
        <div class="lbl">Units Sold</div>
        <div class="val" id="sum-units-sold">0</div>
      </div>
      <div class="sum-cell">
        <div class="lbl">Stock Cost</div>
        <div class="val">₹3.32L</div>
      </div>
      <div class="sum-cell highlight">
        <div class="lbl">Total Sales</div>
        <div class="val" id="sum-total-sales">₹0</div>
      </div>
    </section>

    <!-- CHECKLIST LIST (All 94 items rendered here) -->
    <main class="checklist-container" id="checklist-items-wrap">
      <!-- Generated by JavaScript -->
    </main>

  </div>

  <script>
    const RAW_ITEMS = {items_json_str};

    let items = [];
    let currentFilter = 'all';

    // Initialize from LocalStorage or Default
    function init() {{
      const saved = localStorage.getItem('diwali_checklist_items_v4');
      if (saved) {{
        try {{
          items = JSON.parse(saved);
        }} catch(e) {{
          items = JSON.parse(JSON.stringify(RAW_ITEMS));
        }}
      }} else {{
        items = JSON.parse(JSON.stringify(RAW_ITEMS));
      }}

      // Setup Search Listener
      const searchInput = document.getElementById('box-search');
      searchInput.addEventListener('input', (e) => {{
        renderList(e.target.value.trim());
      }});

      renderList();
      updateGlobalSummary();
    }}

    function saveState() {{
      localStorage.setItem('diwali_checklist_items_v4', JSON.stringify(items));
      updateGlobalSummary();
    }}

    // Render Checklist Items
    function renderList(query = '') {{
      const container = document.getElementById('checklist-items-wrap');
      container.innerHTML = '';
      const q = query.toLowerCase();

      let visibleCount = 0;

      items.forEach((item, index) => {{
        // Filter by Tab
        if (currentFilter === 'pending' && item.verified) return;
        if (currentFilter === 'done' && !item.verified) return;
        if (currentFilter === 'white' && item.bill_type !== 'white') return;
        if (currentFilter === 'pink' && item.bill_type !== 'pink') return;

        // Filter by Search Query
        if (q) {{
          const matchNo = item.sticker_no.toLowerCase() === q || item.sticker_no.toLowerCase().includes(q);
          const matchName = item.name.toLowerCase().includes(q);
          if (!matchNo && !matchName) return;
        }}

        visibleCount++;

        const isPink = item.bill_type === 'pink';
        const costPlus10 = item.rate_plus_10;
        const profitPerUnit = (item.selling_price || 0) - costPlus10;
        const totalProfit = Math.round(profitPerUnit * item.total_units);

        const card = document.createElement('div');
        card.className = `item-card ${{item.verified ? 'is-ticked' : ''}}`;
        card.id = `card-idx-${{index}}`;

        card.innerHTML = `
          <!-- Header Row: Tickbox + Box # + Name -->
          <div class="item-header-row">
            <div class="tick-box-wrap" onclick="toggleTick(${{index}})">
              <div class="custom-tick">${{item.verified ? '✓' : ''}}</div>
            </div>

            <div class="box-badge ${{isPink ? 'pink' : ''}}">
              #${{item.sticker_no}}
            </div>

            <div class="item-title-wrap">
              <div class="name">${{item.name}}</div>
              <div class="sub">${{item.bill_name}} • Pack: ${{item.pack_details}}</div>
            </div>
          </div>

          <!-- 4 Editable Columns Specified by You -->
          <div class="item-stats-grid">
            
            <!-- 1. Total Units (How many you have) -->
            <div class="stat-col">
              <span class="lbl">Total Units</span>
              <input type="number" class="stat-input" value="${{item.total_units}}" 
                onchange="updateTotalUnits(${{index}}, this.value)">
            </div>

            <!-- 2. Units Sold (How many you sell) -->
            <div class="stat-col">
              <span class="lbl">Sold Units</span>
              <div class="sold-counter-wrap">
                <button class="btn-step" onclick="stepSold(${{index}}, -1)">-</button>
                <input type="number" class="stat-input sold-input" value="${{item.units_sold || 0}}" 
                  onchange="updateSoldUnits(${{index}}, this.value)">
                <button class="btn-step" onclick="stepSold(${{index}}, 1)">+</button>
              </div>
            </div>

            <!-- 3. Wholesale Rate (How much rate you got) -->
            <div class="stat-col">
              <span class="lbl">Wholesale Rate</span>
              <div style="font-family: 'JetBrains Mono', monospace; font-weight: 800; font-size: 0.95rem; text-align: center; color: #cbd5e1; padding-top: 4px;">
                ₹${{item.rate}}
              </div>
              <span style="font-size: 0.65rem; color: #fbbf24; text-align: center;">+10%: ₹${{Math.round(costPlus10)}}</span>
            </div>

            <!-- 4. Selling Price (How much you are going to sell) -->
            <div class="stat-col sell-col">
              <span class="lbl" style="color: #34d399;">Sell Price (₹)</span>
              <input type="number" class="stat-input sp-input" value="${{item.selling_price || 0}}" 
                onchange="updateSellingPrice(${{index}}, this.value)">
            </div>

          </div>

          <!-- Live Profit & Stock Left Bar -->
          <div class="item-footer-row">
            <span>Left in Stock: <strong>${{item.total_units - (item.units_sold || 0)}}</strong></span>
            <span class="profit-text ${{profitPerUnit < 0 ? 'negative' : ''}}">
              Profit: ${{profitPerUnit >= 0 ? '+' : ''}}₹${{Math.round(profitPerUnit)}}/pc (Box: ${{totalProfit >= 0 ? '+' : ''}}₹${{totalProfit.toLocaleString('en-IN')}})
            </span>
          </div>
        `;

        container.appendChild(card);
      }});

      if (visibleCount === 0) {{
        container.innerHTML = `
          <div class="empty-state">
            No box found matching "<strong>${{query}}</strong>".<br>
            Try searching a number like <strong>46</strong>, <strong>33</strong>, or <strong>P5</strong>.
          </div>
        `;
      }}
    }}

    // Checkbox Toggle
    function toggleTick(index) {{
      items[index].verified = !items[index].verified;
      saveState();
      
      const card = document.getElementById(`card-idx-${{index}}`);
      if (card) {{
        if (items[index].verified) {{
          card.classList.add('is-ticked');
          card.querySelector('.custom-tick').textContent = '✓';
        }} else {{
          card.classList.remove('is-ticked');
          card.querySelector('.custom-tick').textContent = '';
        }}
      }}
      updateHeaderProgress();
    }}

    // Editable Inputs Handlers
    function updateTotalUnits(index, val) {{
      items[index].total_units = parseInt(val) || 0;
      saveState();
      renderCardFooter(index);
    }}

    function updateSoldUnits(index, val) {{
      items[index].units_sold = parseInt(val) || 0;
      saveState();
      renderCardFooter(index);
    }}

    function stepSold(index, delta) {{
      let current = items[index].units_sold || 0;
      current += delta;
      if (current < 0) current = 0;
      if (current > items[index].total_units) current = items[index].total_units;
      items[index].units_sold = current;
      saveState();

      const card = document.getElementById(`card-idx-${{index}}`);
      if (card) {{
        card.querySelector('.sold-input').value = current;
      }}
      renderCardFooter(index);
    }}

    function updateSellingPrice(index, val) {{
      items[index].selling_price = parseFloat(val) || 0;
      saveState();
      renderCardFooter(index);
    }}

    function renderCardFooter(index) {{
      const item = items[index];
      const card = document.getElementById(`card-idx-${{index}}`);
      if (!card) return;

      const profitPerUnit = (item.selling_price || 0) - item.rate_plus_10;
      const totalProfit = Math.round(profitPerUnit * item.total_units);
      const remaining = item.total_units - (item.units_sold || 0);

      const footer = card.querySelector('.item-footer-row');
      footer.innerHTML = `
        <span>Left in Stock: <strong>${{remaining}}</strong></span>
        <span class="profit-text ${{profitPerUnit < 0 ? 'negative' : ''}}">
          Profit: ${{profitPerUnit >= 0 ? '+' : ''}}₹${{Math.round(profitPerUnit)}}/pc (Box: ${{totalProfit >= 0 ? '+' : ''}}₹${{totalProfit.toLocaleString('en-IN')}})
        </span>
      `;
    }}

    // Filter Buttons
    function setFilter(filterType) {{
      currentFilter = filterType;
      document.querySelectorAll('.f-pill').forEach(btn => btn.classList.remove('active'));
      event.target.classList.add('active');
      const q = document.getElementById('box-search').value.trim();
      renderList(q);
    }}

    function clearSearch() {{
      const input = document.getElementById('box-search');
      input.value = '';
      input.focus();
      renderList('');
    }}

    // Header & Summary Metrics
    function updateHeaderProgress() {{
      const tickedCount = items.filter(i => i.verified).length;
      document.getElementById('header-progress').textContent = `${{tickedCount}} / ${{items.length}} Ticked`;
    }}

    function updateGlobalSummary() {{
      updateHeaderProgress();

      let totalUnits = 0;
      let totalSold = 0;
      let totalSales = 0;

      items.forEach(i => {{
        totalUnits += (i.total_units || 0);
        totalSold += (i.units_sold || 0);
        totalSales += (i.selling_price || 0) * (i.total_units || 0);
      }});

      document.getElementById('sum-total-units').textContent = totalUnits.toLocaleString('en-IN');
      document.getElementById('sum-units-sold').textContent = totalSold.toLocaleString('en-IN');
      document.getElementById('sum-total-sales').textContent = '₹' + Math.round(totalSales).toLocaleString('en-IN');
    }}

    window.addEventListener('DOMContentLoaded', init);
  </script>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Checklist index.html built successfully!")
