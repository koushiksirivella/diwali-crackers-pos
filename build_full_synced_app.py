import json

with open("items_data.json", "r", encoding="utf-8") as f:
    items = json.load(f)

items_json_str = json.dumps(items)

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>Diwali Crackers Checklist, Box Finder & Sales Sync</title>
  <link rel="manifest" href="manifest.json">
  <meta name="theme-color" content="#0b0f17">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;600;700;800&display=swap" rel="stylesheet">
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
      padding: 10px 10px 50px 10px;
    }}

    .app-container {{
      width: 100%;
      max-width: 620px;
      display: flex;
      flex-direction: column;
      gap: 12px;
    }}

    /* STICKY TOP HEADER */
    .top-header {{
      background: #111827;
      border: 1px solid #1f293d;
      border-radius: 16px;
      padding: 12px 14px;
      display: flex;
      flex-direction: column;
      gap: 10px;
      position: sticky;
      top: 8px;
      z-index: 50;
      box-shadow: 0 10px 25px rgba(0,0,0,0.5);
    }}

    .header-title-row {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 8px;
    }}

    .header-title-row h1 {{
      font-size: 1.1rem;
      font-weight: 800;
      color: #fff;
      display: flex;
      align-items: center;
      gap: 6px;
      white-space: nowrap;
    }}

    .header-btn-group {{
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    .header-pill-btn {{
      background: #1e293b;
      border: 1px solid #334155;
      color: #f1f5f9;
      font-size: 0.75rem;
      font-weight: 700;
      padding: 5px 10px;
      border-radius: 8px;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 5px;
      transition: all 0.15s;
    }}

    .header-pill-btn:hover {{
      border-color: #fbbf24;
      color: #fbbf24;
    }}

    .header-pill-btn.sync-active {{
      background: #064e3b;
      border-color: #10b981;
      color: #34d399;
    }}

    /* Search & Voice Bar */
    .search-bar-wrap {{
      display: flex;
      align-items: center;
      background: #090d14;
      border: 2px solid #243048;
      border-radius: 12px;
      padding: 6px 10px;
      gap: 8px;
      position: relative;
    }}

    .search-bar-wrap:focus-within {{
      border-color: #fbbf24;
    }}

    .search-bar-wrap input {{
      width: 100%;
      background: transparent;
      border: none;
      color: #fff;
      font-size: 1.05rem;
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

    .btn-voice-mic {{
      background: linear-gradient(135deg, #1e293b 0%, #334155 100%);
      border: 1.5px solid #475569;
      color: #f1f5f9;
      border-radius: 8px;
      padding: 5px 10px;
      font-size: 0.8rem;
      font-weight: 700;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 5px;
      white-space: nowrap;
      flex-shrink: 0;
      transition: all 0.2s ease;
    }}

    .btn-voice-mic.listening {{
      background: linear-gradient(135deg, #dc2626 0%, #ef4444 100%);
      border-color: #f87171;
      color: #fff;
      animation: pulseMic 1.2s infinite alternate;
      box-shadow: 0 0 14px rgba(239, 68, 68, 0.6);
    }}

    @keyframes pulseMic {{
      from {{ transform: scale(1); }}
      to {{ transform: scale(1.05); }}
    }}

    .clear-search-btn {{
      background: #1e293b;
      border: none;
      color: #94a3b8;
      width: 24px;
      height: 24px;
      border-radius: 50%;
      cursor: pointer;
      font-size: 0.8rem;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
    }}

    /* Voice Status Banner */
    .voice-status-banner {{
      display: none;
      background: rgba(239, 68, 68, 0.15);
      border: 1px solid rgba(239, 68, 68, 0.4);
      color: #fca5a5;
      font-size: 0.75rem;
      font-weight: 600;
      padding: 6px 10px;
      border-radius: 8px;
      align-items: center;
      justify-content: space-between;
    }}

    .voice-status-banner.active {{
      display: flex;
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
      padding: 4px 10px;
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
      padding: 8px 10px;
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
      gap: 8px;
      transition: all 0.2s ease;
      position: relative;
    }}

    .item-card.is-ticked {{
      background: #0d1724;
      border-color: #10b981;
    }}

    .item-card.voice-matched {{
      border-color: #fbbf24;
      box-shadow: 0 0 20px rgba(251, 191, 36, 0.4);
    }}

    /* Header Row: Checkbox + Number + Name */
    .item-header-row {{
      display: flex;
      align-items: center;
      gap: 10px;
    }}

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

    /* Sticker Number Badge (Directly Editable on tap) */
    .box-badge {{
      background: #fbbf24;
      color: #000;
      font-family: 'JetBrains Mono', monospace;
      font-weight: 900;
      font-size: 0.95rem;
      padding: 2px 8px;
      border-radius: 6px;
      letter-spacing: -0.02em;
      flex-shrink: 0;
      cursor: pointer;
      border: 1px solid rgba(0,0,0,0.2);
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

    /* 4 Core Columns Grid */
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

    /* MODAL: DATA EXTRACTION & BACKUP */
    .modal-scrim {{
      display: none;
      position: fixed;
      inset: 0;
      background: rgba(0,0,0,0.8);
      backdrop-filter: blur(8px);
      z-index: 100;
      align-items: center;
      justify-content: center;
      padding: 16px;
    }}

    .modal-scrim.open {{
      display: flex;
    }}

    .modal-box {{
      background: #111827;
      border: 1px solid #1f293d;
      border-radius: 18px;
      max-width: 440px;
      width: 100%;
      padding: 18px;
      display: flex;
      flex-direction: column;
      gap: 12px;
    }}

    .modal-top {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid #1f293d;
      padding-bottom: 10px;
    }}

    .modal-top h3 {{
      font-size: 1.1rem;
      font-weight: 800;
    }}

    .btn-close-modal {{
      background: #1e293b;
      border: none;
      color: #fff;
      width: 28px;
      height: 28px;
      border-radius: 50%;
      cursor: pointer;
      font-weight: 800;
    }}

    .export-action-card {{
      background: #090d14;
      border: 1px solid #1e293b;
      border-radius: 12px;
      padding: 12px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 10px;
      cursor: pointer;
      transition: all 0.15s;
    }}

    .export-action-card:hover {{
      border-color: #fbbf24;
      background: #131b28;
    }}

    .export-info h4 {{
      font-size: 0.95rem;
      font-weight: 700;
      color: #fff;
    }}

    .export-info p {{
      font-size: 0.75rem;
      color: #94a3b8;
    }}

    .btn-export-download {{
      background: #fbbf24;
      color: #000;
      border: none;
      padding: 6px 14px;
      border-radius: 8px;
      font-weight: 800;
      font-size: 0.8rem;
      cursor: pointer;
      white-space: nowrap;
    }}
  </style>
</head>
<body>

  <div class="app-container">
    
    <!-- STICKY TOP CONTROLS -->
    <header class="top-header">
      <div class="header-title-row">
        <h1><span>🪔</span> Diwali Box Checklist</h1>
        <div class="header-btn-group">
          <button class="header-pill-btn" id="btn-sync-cloud" onclick="syncDataToServer()" title="Save & Push to GitHub">
            <span id="sync-icon">☁️</span> <span id="sync-text">Save / Sync</span>
          </button>
          <button class="header-pill-btn" onclick="openExtractModal()" title="Extract / Download Data">
            <span>📥</span> Extract
          </button>
        </div>
      </div>

      <!-- Search & Voice Bar -->
      <div class="search-bar-wrap">
        <span style="color: #fbbf24; font-size: 1rem;">🔍</span>
        <input type="text" id="box-search" placeholder="Search # (e.g. 46, 1294, P1) or Name..." autocomplete="off">
        
        <button class="btn-voice-mic" id="btn-voice-search" onclick="toggleVoiceSearch()" title="Say a box number (e.g. '46' or '1294') or item name">
          <span id="mic-icon">🎙️</span>
          <span id="mic-label">Voice</span>
        </button>

        <button class="clear-search-btn" onclick="clearSearch()">✕</button>
      </div>

      <!-- Live Voice Status Banner -->
      <div class="voice-status-banner" id="voice-banner">
        <span id="voice-status-text">🔴 Listening... Say number (e.g. "46" or "1294") or item name</span>
        <button class="clear-search-btn" style="width: 20px; height: 20px; font-size: 0.7rem;" onclick="stopVoiceSearch()">✕</button>
      </div>

      <!-- Quick Filter Pills -->
      <div class="filter-pills-row">
        <button class="f-pill active" onclick="setFilter('all')">All (94)</button>
        <button class="f-pill" onclick="setFilter('pending')">Pending Boxes</button>
        <button class="f-pill" onclick="setFilter('done')">Ticked (Done)</button>
        <button class="f-pill" onclick="setFilter('white')">White Bill (1–74)</button>
        <button class="f-pill" onclick="setFilter('pink')">Pink Bill 1294 (20)</button>
      </div>
    </header>

    <!-- LIVE SUMMARY METRICS -->
    <section class="summary-strip">
      <div class="sum-cell">
        <div class="lbl">Ticked Boxes</div>
        <div class="val" id="sum-ticked-boxes">0 / 94</div>
      </div>
      <div class="sum-cell">
        <div class="lbl">Total Units</div>
        <div class="val" id="sum-total-units">3,925</div>
      </div>
      <div class="sum-cell">
        <div class="lbl">Units Sold</div>
        <div class="val" id="sum-units-sold">0</div>
      </div>
      <div class="sum-cell highlight">
        <div class="lbl">Total Revenue</div>
        <div class="val" id="sum-total-sales">₹0</div>
      </div>
    </section>

    <!-- CHECKLIST LIST (All 94 items rendered here) -->
    <main class="checklist-container" id="checklist-items-wrap">
      <!-- Generated by JavaScript -->
    </main>

  </div>

  <!-- MODAL: DATA EXTRACTION & GITHUB SYNC -->
  <div class="modal-scrim" id="extract-modal" onclick="closeExtractModal()">
    <div class="modal-box" onclick="event.stopPropagation()">
      <div class="modal-top">
        <h3>📥 Data Extraction & Cloud Backup</h3>
        <button class="btn-close-modal" onclick="closeExtractModal()">✕</button>
      </div>

      <div class="export-action-card" onclick="exportToCSV()">
        <div class="export-info">
          <h4>📊 Download Excel / CSV</h4>
          <p>Complete spreadsheet with units sold, rates, selling prices, profit & status.</p>
        </div>
        <button class="btn-export-download">CSV</button>
      </div>

      <div class="export-action-card" onclick="exportToJSON()">
        <div class="export-info">
          <h4>📦 Download Full JSON Backup</h4>
          <p>Export raw verified dataset file to save on phone or PC.</p>
        </div>
        <button class="btn-export-download">JSON</button>
      </div>

      <div class="export-action-card" onclick="syncDataToServer(true)">
        <div class="export-info">
          <h4>☁️ Push to GitHub Repository</h4>
          <p>Commit latest verified numbers and sales directly to GitHub.</p>
        </div>
        <button class="btn-export-download" style="background:#10b981; color:#000;">Sync</button>
      </div>

      <div style="border-top: 1px solid #1e293b; padding-top: 8px; font-size: 0.75rem; color: #64748b; text-align: center;">
        GitHub Repo: <a href="https://github.com/koushiksirivella/diwali-crackers-scanner" target="_blank" style="color: #fbbf24; text-decoration: none;">koushiksirivella/diwali-crackers-scanner</a>
      </div>
    </div>
  </div>

  <script>
    const RAW_ITEMS = {items_json_str};

    let items = [];
    let currentFilter = 'all';

    const NUMBER_WORDS = {{
      'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
      'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10,
      'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15,
      'sixteen': 16, 'seventeen': 17, 'eighteen': 18, 'nineteen': 19, 'twenty': 20,
      'thirty': 30, 'forty': 40, 'fifty': 50, 'sixty': 60, 'seventy': 70,
      'eighty': 80, 'ninety': 90, 'hundred': 100, 'thousand': 1000
    }};

    function parseSpokenWords(str) {{
      let clean = str.toLowerCase()
        .replace(/box\\s*number/g, '')
        .replace(/box/g, '')
        .replace(/number/g, '')
        .replace(/item/g, '')
        .trim();

      // Check pink prefix or 1294
      let hasPink = false;
      if (clean.includes('pink') || clean.startsWith('p ') || clean.startsWith('p-') || clean.includes('1294')) {{
        hasPink = true;
      }}

      // Direct digits match
      const digitMatch = clean.match(/\\d+/);
      if (digitMatch) {{
        return digitMatch[0];
      }}

      // Composite spoken numbers (e.g. "forty six" -> 46)
      const words = clean.split(/[\\s-]+/);
      let total = 0;
      let isNumber = false;

      for (let w of words) {{
        if (NUMBER_WORDS[w] !== undefined) {{
          isNumber = true;
          total += NUMBER_WORDS[w];
        }}
      }}

      if (isNumber && total > 0) {{
        return total.toString();
      }}

      return clean;
    }}

    // Init App State (Load from Server or LocalStorage)
    async function init() {{
      let loaded = null;

      // 1. Try fetching latest synced data from server API
      try {{
        const resp = await fetch('/api/data');
        if (resp.ok) {{
          loaded = await resp.json();
        }}
      }} catch(e) {{}}

      // 2. If server not reachable, use LocalStorage
      if (!loaded) {{
        const saved = localStorage.getItem('diwali_items_v5');
        if (saved) {{
          try {{ loaded = JSON.parse(saved); }} catch(e) {{}}
        }}
      }}

      // 3. Fallback to embedded data
      items = loaded || JSON.parse(JSON.stringify(RAW_ITEMS));

      // Search Listener
      const searchInput = document.getElementById('box-search');
      searchInput.addEventListener('input', (e) => {{
        renderList(e.target.value.trim());
      }});

      renderList();
      updateGlobalSummary();
    }}

    function saveStateLocal() {{
      localStorage.setItem('diwali_items_v5', JSON.stringify(items));
      updateGlobalSummary();
    }}

    // Push / Sync to Server & GitHub
    async function syncDataToServer(showAlert = false) {{
      saveStateLocal();
      const syncBtn = document.getElementById('btn-sync-cloud');
      const syncText = document.getElementById('sync-text');
      syncText.textContent = "Syncing...";

      try {{
        const res = await fetch('/api/save', {{
          method: 'POST',
          headers: {{ 'Content-Type': 'application/json' }},
          body: JSON.stringify(items)
        }});

        if (res.ok) {{
          syncBtn.classList.add('sync-active');
          syncText.textContent = "Synced ✓";
          if (showAlert) alert("Successfully synced and pushed to GitHub repository!");
          setTimeout(() => {{ syncText.textContent = "Save / Sync"; }}, 3000);
          return;
        }}
      }} catch(e) {{
        console.warn("Server offline, saved locally to device storage.");
      }}

      syncText.textContent = "Saved Local ✓";
      if (showAlert) alert("Saved to local device storage! (Run local server or use Export CSV/JSON for extraction).");
      setTimeout(() => {{ syncText.textContent = "Save / Sync"; }}, 2500);
    }}

    // Render Checklist Items
    function renderList(query = '') {{
      const container = document.getElementById('checklist-items-wrap');
      container.innerHTML = '';
      const q = query.toLowerCase();

      let visibleCount = 0;
      let matchedIndex = -1;

      items.forEach((item, index) => {{
        if (currentFilter === 'pending' && item.verified) return;
        if (currentFilter === 'done' && !item.verified) return;
        if (currentFilter === 'white' && item.bill_type !== 'white') return;
        if (currentFilter === 'pink' && item.bill_type !== 'pink') return;

        if (q) {{
          const matchNo = item.sticker_no.toLowerCase().includes(q) || 
                          (item.search_keys && item.search_keys.some(k => k.toLowerCase().includes(q)));
          const matchName = item.name.toLowerCase().includes(q);
          if (!matchNo && !matchName) return;
          if (matchedIndex === -1) matchedIndex = index;
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
          <!-- Header Row: Tickbox + Number + Name -->
          <div class="item-header-row">
            <div class="tick-box-wrap" onclick="toggleTick(${{index}})">
              <div class="custom-tick">${{item.verified ? '✓' : ''}}</div>
            </div>

            <!-- Sticker Number Badge: Tap to customize sticker # on box -->
            <div class="box-badge ${{isPink ? 'pink' : ''}}" onclick="editStickerNumber(${{index}})" title="Tap to edit sticker number on box">
              #${{item.sticker_no}}
            </div>

            <div class="item-title-wrap">
              <div class="name">${{item.name}}</div>
              <div class="sub">${{item.bill_name}} • Pack: ${{item.pack_details}}</div>
            </div>
          </div>

          <!-- 4 Core Columns -->
          <div class="item-stats-grid">
            <div class="stat-col">
              <span class="lbl">Total Units</span>
              <input type="number" class="stat-input" value="${{item.total_units}}" 
                onchange="updateTotalUnits(${{index}}, this.value)">
            </div>

            <div class="stat-col">
              <span class="lbl">Sold Units</span>
              <div class="sold-counter-wrap">
                <button class="btn-step" onclick="stepSold(${{index}}, -1)">-</button>
                <input type="number" class="stat-input sold-input" value="${{item.units_sold || 0}}" 
                  onchange="updateSoldUnits(${{index}}, this.value)">
                <button class="btn-step" onclick="stepSold(${{index}}, 1)">+</button>
              </div>
            </div>

            <div class="stat-col">
              <span class="lbl">Wholesale</span>
              <div style="font-family: 'JetBrains Mono', monospace; font-weight: 800; font-size: 0.95rem; text-align: center; color: #cbd5e1; padding-top: 4px;">
                ₹${{item.rate}}
              </div>
              <span style="font-size: 0.65rem; color: #fbbf24; text-align: center;">+10%: ₹${{Math.round(costPlus10)}}</span>
            </div>

            <div class="stat-col sell-col">
              <span class="lbl" style="color: #34d399;">Sell Price (₹)</span>
              <input type="number" class="stat-input sp-input" value="${{item.selling_price || 0}}" 
                onchange="updateSellingPrice(${{index}}, this.value)">
            </div>
          </div>

          <!-- Profit & Stock Remaining -->
          <div class="item-footer-row">
            <span>Remaining: <strong>${{item.total_units - (item.units_sold || 0)}}</strong></span>
            <span class="profit-text ${{profitPerUnit < 0 ? 'negative' : ''}}">
              Profit: ${{profitPerUnit >= 0 ? '+' : ''}}₹${{Math.round(profitPerUnit)}}/pc (Box: ${{totalProfit >= 0 ? '+' : ''}}₹${{totalProfit.toLocaleString('en-IN')}})
            </span>
          </div>
        `;

        container.appendChild(card);
      }});

      if (visibleCount === 0) {{
        container.innerHTML = `
          <div style="text-align: center; padding: 40px 10px; color: #64748b; font-size: 0.95rem;">
            No box found matching "<strong>${{query}}</strong>".<br>
            Try searching a number like <strong>46</strong>, <strong>1294</strong>, or name like <strong>7 shot</strong>, <strong>GLC</strong>.
          </div>
        `;
      }}

      return matchedIndex;
    }}

    // Checkbox Toggle
    function toggleTick(index) {{
      items[index].verified = !items[index].verified;
      items[index].verified_at = items[index].verified ? new Date().toISOString() : null;
      saveStateLocal();
      
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
      updateGlobalSummary();
    }}

    // Customize Sticker Number on tap
    function editStickerNumber(index) {{
      const current = items[index].sticker_no;
      const updated = prompt("Enter specific sticker/box number printed on this carton:", current);
      if (updated && updated.trim()) {{
        items[index].sticker_no = updated.trim();
        if (!items[index].search_keys) items[index].search_keys = [];
        items[index].search_keys.push(updated.trim());
        saveStateLocal();
        renderList(document.getElementById('box-search').value.trim());
      }}
    }}

    function updateTotalUnits(index, val) {{
      items[index].total_units = parseInt(val) || 0;
      saveStateLocal();
      renderCardFooter(index);
    }}

    function updateSoldUnits(index, val) {{
      items[index].units_sold = parseInt(val) || 0;
      saveStateLocal();
      renderCardFooter(index);
    }}

    function stepSold(index, delta) {{
      let current = items[index].units_sold || 0;
      current += delta;
      if (current < 0) current = 0;
      if (current > items[index].total_units) current = items[index].total_units;
      items[index].units_sold = current;
      saveStateLocal();

      const card = document.getElementById(`card-idx-${{index}}`);
      if (card) {{
        card.querySelector('.sold-input').value = current;
      }}
      renderCardFooter(index);
    }}

    function updateSellingPrice(index, val) {{
      items[index].selling_price = parseFloat(val) || 0;
      saveStateLocal();
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
        <span>Remaining: <strong>${{remaining}}</strong></span>
        <span class="profit-text ${{profitPerUnit < 0 ? 'negative' : ''}}">
          Profit: ${{profitPerUnit >= 0 ? '+' : ''}}₹${{Math.round(profitPerUnit)}}/pc (Box: ${{totalProfit >= 0 ? '+' : ''}}₹${{totalProfit.toLocaleString('en-IN')}})
        </span>
      `;
    }}

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

    function updateGlobalSummary() {{
      const ticked = items.filter(i => i.verified).length;
      document.getElementById('sum-ticked-boxes').textContent = `${{ticked}} / ${{items.length}}`;

      let totalUnits = 0;
      let totalSold = 0;
      let totalSales = 0;

      items.forEach(i => {{
        totalUnits += (i.total_units || 0);
        totalSold += (i.units_sold || 0);
        totalSales += (i.selling_price || 0) * (i.units_sold || 0);
      }});

      document.getElementById('sum-total-units').textContent = totalUnits.toLocaleString('en-IN');
      document.getElementById('sum-units-sold').textContent = totalSold.toLocaleString('en-IN');
      document.getElementById('sum-total-sales').textContent = '₹' + Math.round(totalSales).toLocaleString('en-IN');
    }}

    // =========================================================================
    // VOICE SEARCH (Number or Name)
    // =========================================================================
    let recognition = null;
    let isListening = false;

    if ('webkitSpeechRecognition' in window || 'SpeechRecognition' in window) {{
      const SpeechClass = window.SpeechRecognition || window.webkitSpeechRecognition;
      recognition = new SpeechClass();
      recognition.continuous = false;
      recognition.interimResults = false;
      recognition.lang = 'en-IN';

      recognition.onstart = function() {{
        isListening = true;
        document.getElementById('btn-voice-search').classList.add('listening');
        document.getElementById('mic-label').textContent = 'Listening';
        const banner = document.getElementById('voice-banner');
        banner.classList.add('active');
        document.getElementById('voice-status-text').textContent = '🔴 Listening... Say number (e.g. "46", "1294") or item name';
      }};

      recognition.onresult = function(event) {{
        const transcript = event.results[0][0].transcript;
        const parsed = parseSpokenWords(transcript);
        
        document.getElementById('box-search').value = parsed;
        const matchedIdx = renderList(parsed);

        stopVoiceSearch();

        if (matchedIdx !== -1) {{
          const matchedItem = items[matchedIdx];
          const card = document.getElementById(`card-idx-${{matchedIdx}}`);
          if (card) {{
            card.classList.add('voice-matched');
            card.scrollIntoView({{ behavior: 'smooth', block: 'center' }});
          }}
          speakVoiceResult(matchedItem);
        }}
      }};

      recognition.onerror = function() {{ stopVoiceSearch(); }};
      recognition.onend = function() {{ stopVoiceSearch(); }};
    }}

    function toggleVoiceSearch() {{
      if (!recognition) {{
        alert("Voice recognition supported in Chrome/Safari on mobile and desktop!");
        return;
      }}
      if (isListening) stopVoiceSearch();
      else recognition.start();
    }}

    function stopVoiceSearch() {{
      isListening = false;
      const btn = document.getElementById('btn-voice-search');
      if (btn) btn.classList.remove('listening');
      const label = document.getElementById('mic-label');
      if (label) label.textContent = 'Voice';
      const banner = document.getElementById('voice-banner');
      if (banner) banner.classList.remove('active');
      if (recognition) {{ try {{ recognition.stop(); }} catch(e) {{}} }}
    }}

    function speakVoiceResult(item) {{
      if (!('speechSynthesis' in window)) return;
      window.speechSynthesis.cancel();
      const text = `${{item.name}}, Box ${{item.sticker_no}}, ${{item.total_units}} units, wholesale rate ₹${{item.rate}}, selling at ₹${{item.selling_price}}`;
      const utterance = new SpeechSynthesisUtterance(text);
      utterance.rate = 1.05;
      window.speechSynthesis.speak(utterance);
    }}

    // =========================================================================
    // DATA EXTRACTION & EXPORT ENGINE
    // =========================================================================
    function openExtractModal() {{
      document.getElementById('extract-modal').classList.add('open');
    }}

    function closeExtractModal() {{
      document.getElementById('extract-modal').classList.remove('open');
    }}

    // Export to Excel / CSV
    function exportToCSV() {{
      let csv = "Box / Sticker No,Lot / Origin,Product Name,Pack Info,Total Units Received,Units Sold,Units Remaining,Wholesale Rate (Rs),Cost with 10pct (Rs),Selling Price (Rs),Revenue Collected (Rs),Net Profit (Rs),Verified Status,Verified Date\\n";

      items.forEach(it => {{
        const sold = it.units_sold || 0;
        const rem = it.total_units - sold;
        const rev = sold * (it.selling_price || 0);
        const profit = Math.round(((it.selling_price || 0) - it.rate_plus_10) * sold);
        const status = it.verified ? "VERIFIED" : "PENDING";
        const vDate = it.verified_at || "";

        csv += `"${{it.sticker_no}}","${{it.bill_name}}","${{it.name}}","${{it.pack_details}}",${{it.total_units}},${{sold}},${{rem}},${{it.rate}},${{it.rate_plus_10}},${{it.selling_price}},${{rev}},${{profit}},"${{status}}","${{vDate}}"\\n`;
      }});

      const blob = new Blob([csv], {{ type: 'text/csv;charset=utf-8;' }});
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = `Diwali_Crackers_Sales_Data_${{new Date().toISOString().slice(0,10)}}.csv`;
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
    }}

    // Export Full JSON Backup
    function exportToJSON() {{
      const jsonStr = JSON.stringify(items, null, 2);
      const blob = new Blob([jsonStr], {{ type: 'application/json' }});
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = `diwali_inventory_backup_${{new Date().toISOString().slice(0,10)}}.json`;
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
    }}

    window.addEventListener('DOMContentLoaded', init);
  </script>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Full synced index.html written successfully!")
