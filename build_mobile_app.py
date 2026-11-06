import json

with open("items_data.json", "r", encoding="utf-8") as f:
    items = json.load(f)

items_json_str = json.dumps(items)

html_code = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
  <title>Diwali Crackers Scanner • Fastest Box Verifier</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;700;800&display=swap" rel="stylesheet">
  <style>
    /* =========================================================================
       LUXURY MINIMALIST TOKENS (Inspired by exp / haoqi / why-zero)
       Matte Obsidian (#0a0c0e), Frosted Glass HUD, Electric Lime (#c0fe04)
       ========================================================================= */
    :root {{
      --bg-deep: #090b0e;
      --bg-surface: #12151b;
      --bg-elevated: #181d26;
      --bg-card: rgba(24, 29, 38, 0.7);
      --border-subtle: rgba(255, 255, 255, 0.07);
      --border-focus: rgba(192, 254, 4, 0.45);
      
      --accent-lime: #c0fe04;
      --accent-lime-dim: rgba(192, 254, 4, 0.15);
      --accent-gold: #fbbf24;
      --accent-pink: #f43f5e;
      --accent-green: #10b981;
      
      --text-1: #ffffff;
      --text-2: #94a3b8;
      --text-3: #64748b;
      
      --font-sans: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;
      --font-mono: 'JetBrains Mono', ui-monospace, monospace;
      
      --ease-snap: cubic-bezier(0.16, 1, 0.3, 1);
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      -webkit-tap-highlight-color: transparent;
      user-select: none;
    }}

    input, textarea {{
      user-select: text;
    }}

    html, body {{
      height: 100%;
      height: 100dvh;
      overflow: hidden;
      background-color: var(--bg-deep);
      color: var(--text-1);
      font-family: var(--font-sans);
      -webkit-font-smoothing: antialiased;
    }}

    /* Fullscreen App Shell */
    .app-shell {{
      height: 100%;
      height: 100dvh;
      display: flex;
      flex-direction: column;
      max-width: 480px;
      margin: 0 auto;
      position: relative;
      background: radial-gradient(circle at 50% 0%, #151b24 0%, var(--bg-deep) 75%);
    }}

    /* Top Glass Navigation Bar */
    .top-hud {{
      padding: 10px 14px 6px 14px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 10px;
      z-index: 20;
    }}

    .brand-pill {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 6px 12px;
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid var(--border-subtle);
      border-radius: 999px;
      backdrop-filter: blur(12px);
    }}

    .brand-pill .spark {{
      color: var(--accent-gold);
      font-size: 14px;
      animation: pulse 1.5s infinite alternate;
    }}

    @keyframes pulse {{
      from {{ opacity: 0.6; transform: scale(0.9); }}
      to {{ opacity: 1; transform: scale(1.1); }}
    }}

    .brand-pill span {{
      font-size: 12px;
      font-weight: 700;
      letter-spacing: 0.04em;
      text-transform: uppercase;
      color: var(--text-2);
    }}

    .hud-right-actions {{
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    .hud-btn {{
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid var(--border-subtle);
      color: var(--text-2);
      border-radius: 999px;
      padding: 6px 12px;
      font-size: 12px;
      font-weight: 600;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      backdrop-filter: blur(12px);
      transition: all 0.2s;
    }}

    .hud-btn.active {{
      background: var(--accent-lime-dim);
      border-color: var(--accent-lime);
      color: var(--accent-lime);
    }}

    /* Progress Micro Bar */
    .progress-strip {{
      padding: 0 14px 4px 14px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-size: 11px;
      font-family: var(--font-mono);
      color: var(--text-3);
    }}

    .progress-bar-wrap {{
      flex: 1;
      height: 4px;
      background: rgba(255, 255, 255, 0.05);
      border-radius: 99px;
      margin: 0 10px;
      overflow: hidden;
    }}

    .progress-bar-fill {{
      height: 100%;
      background: var(--accent-lime);
      width: 0%;
      transition: width 0.3s var(--ease-snap);
      box-shadow: 0 0 8px var(--accent-lime);
    }}

    /* Main Deck: Middle Viewport */
    .deck-viewport {{
      flex: 1;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      padding: 4px 14px 10px 14px;
      overflow: hidden;
    }}

    /* Active Item Card */
    .item-card {{
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: 20px;
      padding: 14px 16px;
      backdrop-filter: blur(20px);
      box-shadow: 0 12px 30px rgba(0,0,0,0.5);
      transition: all 0.2s var(--ease-snap);
      position: relative;
    }}

    .item-card.is-verified {{
      border-color: rgba(16, 185, 129, 0.5);
      background: linear-gradient(180deg, rgba(16, 185, 129, 0.08) 0%, rgba(18, 21, 27, 0.85) 100%);
    }}

    /* Card Top Meta */
    .card-top {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 8px;
    }}

    .sticker-tag {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: #000;
      border: 1px solid rgba(255, 255, 255, 0.15);
      padding: 4px 12px;
      border-radius: 10px;
    }}

    .sticker-tag .num {{
      font-size: 1.35rem;
      font-weight: 800;
      font-family: var(--font-mono);
      color: #fff;
    }}

    .sticker-tag.pink-tag .num {{
      color: #fb7185;
    }}

    .sticker-tag .bill-name {{
      font-size: 10px;
      color: var(--text-3);
      text-transform: uppercase;
      font-weight: 700;
    }}

    .status-badge {{
      display: inline-flex;
      align-items: center;
      gap: 5px;
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      padding: 4px 10px;
      border-radius: 999px;
      background: rgba(255, 255, 255, 0.04);
      color: var(--text-3);
      border: 1px solid var(--border-subtle);
    }}

    .status-badge.verified {{
      background: rgba(16, 185, 129, 0.15);
      border-color: rgba(16, 185, 129, 0.4);
      color: #34d399;
    }}

    /* Product Title */
    .product-title {{
      font-size: 1.45rem;
      font-weight: 800;
      color: #fff;
      line-height: 1.15;
      margin-bottom: 4px;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      letter-spacing: -0.01em;
    }}

    .product-sub {{
      font-size: 12px;
      font-weight: 600;
      color: var(--text-2);
      display: flex;
      gap: 12px;
      margin-bottom: 12px;
    }}

    .product-sub strong {{
      color: var(--accent-gold);
    }}

    /* Compact Costing Bar */
    .cost-strip {{
      display: grid;
      grid-template-columns: 1fr 1fr 1fr;
      gap: 8px;
      background: rgba(0, 0, 0, 0.35);
      border: 1px solid var(--border-subtle);
      border-radius: 12px;
      padding: 8px 12px;
      margin-bottom: 12px;
      text-align: center;
    }}

    .cost-strip-cell .label {{
      font-size: 9px;
      text-transform: uppercase;
      font-weight: 700;
      color: var(--text-3);
      margin-bottom: 2px;
    }}

    .cost-strip-cell .val {{
      font-size: 14px;
      font-weight: 700;
      font-family: var(--font-mono);
      color: var(--text-2);
    }}

    .cost-strip-cell.highlight .val {{
      color: #fff;
    }}

    .cost-strip-cell.box-total .val {{
      color: var(--accent-gold);
    }}

    /* SELLING PRICE HERO SECTION */
    .price-hero {{
      background: linear-gradient(135deg, rgba(192, 254, 4, 0.08) 0%, rgba(0, 0, 0, 0.5) 100%);
      border: 1.5px solid var(--accent-lime);
      border-radius: 14px;
      padding: 10px 14px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      position: relative;
    }}

    .price-hero-label {{
      font-size: 10px;
      font-weight: 800;
      text-transform: uppercase;
      color: var(--accent-lime);
      letter-spacing: 0.06em;
      margin-bottom: 2px;
    }}

    .price-hero-profit {{
      font-size: 11px;
      font-family: var(--font-mono);
      font-weight: 600;
      color: #34d399;
    }}

    .price-hero-val-wrap {{
      display: flex;
      align-items: baseline;
      gap: 4px;
    }}

    .price-hero-symbol {{
      font-size: 1.5rem;
      font-weight: 800;
      color: var(--accent-lime);
      font-family: var(--font-mono);
    }}

    .price-hero-input {{
      width: 110px;
      background: transparent;
      border: none;
      color: #ffffff;
      font-size: 2.2rem;
      font-weight: 800;
      font-family: var(--font-mono);
      text-align: right;
      outline: none;
    }}

    /* Quick Margin Pills */
    .margin-pills {{
      display: flex;
      gap: 6px;
      margin-top: 8px;
    }}

    .m-pill {{
      flex: 1;
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid var(--border-subtle);
      color: var(--text-2);
      font-size: 11px;
      font-family: var(--font-mono);
      font-weight: 700;
      padding: 6px 0;
      border-radius: 8px;
      cursor: pointer;
      text-align: center;
      transition: all 0.15s;
    }}

    .m-pill:active {{
      background: var(--accent-lime);
      color: #000;
      border-color: var(--accent-lime);
      transform: scale(0.96);
    }}

    /* BIG ONE-TAP ACTION BUTTON */
    .action-row {{
      margin-top: 8px;
      display: flex;
      gap: 8px;
    }}

    .btn-verify-huge {{
      flex: 1;
      height: 52px;
      border-radius: 14px;
      border: none;
      background: var(--accent-lime);
      color: #000000;
      font-family: var(--font-sans);
      font-size: 1rem;
      font-weight: 800;
      letter-spacing: -0.01em;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      box-shadow: 0 4px 18px rgba(192, 254, 4, 0.35);
      transition: all 0.15s var(--ease-snap);
      touch-action: manipulation;
    }}

    .btn-verify-huge:active {{
      transform: scale(0.97);
      background: #a3dc00;
    }}

    .btn-verify-huge.is-verified {{
      background: rgba(255, 255, 255, 0.08);
      color: var(--text-2);
      box-shadow: none;
      border: 1px solid var(--border-subtle);
    }}

    .btn-nav {{
      width: 48px;
      height: 52px;
      border-radius: 14px;
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid var(--border-subtle);
      color: #fff;
      font-size: 1.2rem;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      touch-action: manipulation;
    }}

    .btn-nav:active {{
      background: rgba(255, 255, 255, 0.12);
      transform: scale(0.94);
    }}

    /* ERGONOMIC THUMB NUMPAD (Bottom Fixed Area) */
    .numpad-grid {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 6px;
      margin-top: 6px;
    }}

    .key {{
      height: 48px;
      background: rgba(255, 255, 255, 0.035);
      border: 1px solid rgba(255, 255, 255, 0.06);
      border-radius: 12px;
      color: #ffffff;
      font-size: 1.35rem;
      font-weight: 700;
      font-family: var(--font-mono);
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      touch-action: manipulation;
      transition: all 0.1s ease;
    }}

    .key:active {{
      background: var(--accent-lime);
      color: #000;
      transform: scale(0.94);
      border-color: var(--accent-lime);
    }}

    .key.key-p {{
      color: var(--accent-pink);
      font-size: 1.15rem;
      font-weight: 800;
    }}

    .key.key-del {{
      color: var(--text-3);
      font-size: 1.1rem;
    }}

    .key-sub {{
      font-size: 7px;
      font-family: var(--font-sans);
      text-transform: uppercase;
      color: var(--text-3);
      line-height: 1;
      margin-top: 1px;
    }}

    .key:active .key-sub {{
      color: #000;
    }}

    /* SEARCH OVERLAY / BOTTOM DRAWER */
    .drawer-overlay {{
      display: none;
      position: fixed;
      inset: 0;
      background: rgba(0, 0, 0, 0.7);
      backdrop-filter: blur(10px);
      z-index: 50;
      flex-direction: column;
      justify-content: flex-end;
    }}

    .drawer-overlay.open {{
      display: flex;
    }}

    .drawer-sheet {{
      background: #10141b;
      border-top: 1px solid var(--border-subtle);
      border-radius: 24px 24px 0 0;
      max-height: 85vh;
      display: flex;
      flex-direction: column;
      padding: 18px 16px;
      animation: slideUp 0.25s var(--ease-snap);
    }}

    @keyframes slideUp {{
      from {{ transform: translateY(100%); }}
      to {{ transform: translateY(0); }}
    }}

    .drawer-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 12px;
    }}

    .drawer-header h3 {{
      font-size: 1rem;
      font-weight: 700;
    }}

    .drawer-close {{
      background: rgba(255,255,255,0.06);
      border: none;
      color: #fff;
      width: 32px;
      height: 32px;
      border-radius: 50%;
      cursor: pointer;
      font-weight: 800;
    }}

    .drawer-search {{
      background: rgba(0,0,0,0.4);
      border: 1px solid var(--border-subtle);
      border-radius: 12px;
      padding: 10px 14px;
      color: #fff;
      font-size: 14px;
      margin-bottom: 12px;
      outline: none;
      width: 100%;
    }}

    .drawer-list {{
      overflow-y: auto;
      flex: 1;
      display: flex;
      flex-direction: column;
      gap: 6px;
      max-height: 60vh;
    }}

    .drawer-item-row {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: rgba(255,255,255,0.02);
      border: 1px solid var(--border-subtle);
      padding: 10px 12px;
      border-radius: 10px;
      cursor: pointer;
    }}

    .drawer-item-row:hover {{
      background: rgba(192, 254, 4, 0.05);
      border-color: var(--accent-lime);
    }}

    .drawer-item-row.verified {{
      border-left: 3px solid var(--accent-green);
    }}

    /* Financials Sheet */
    .fin-row {{
      display: flex;
      justify-content: space-between;
      padding: 8px 0;
      border-bottom: 1px dashed rgba(255,255,255,0.07);
      font-size: 13px;
    }}

    .fin-row.total {{
      font-weight: 800;
      font-size: 15px;
      color: var(--accent-lime);
      border-top: 1px solid var(--border-subtle);
      border-bottom: none;
      padding-top: 12px;
      margin-top: 4px;
    }}

    /* Desktop View Enhancement */
    @media (min-width: 768px) {{
      .app-shell {{
        max-width: 440px;
        height: 94vh;
        border-radius: 32px;
        border: 1px solid var(--border-subtle);
        box-shadow: 0 25px 60px rgba(0, 0, 0, 0.8), 0 0 40px rgba(192, 254, 4, 0.1);
        margin: 3vh auto;
      }}
    }}
  </style>
</head>
<body>

  <div class="app-shell">
    
    <!-- Top Minimal HUD -->
    <header class="top-hud">
      <div class="brand-pill">
        <span class="spark">⚡</span>
        <span id="bill-category-label">White Bill #1–74</span>
      </div>

      <div class="hud-right-actions">
        <button class="hud-btn" id="btn-voice-toggle" onclick="toggleVoice()">
          <span id="voice-icon">🔈</span> Voice
        </button>
        <button class="hud-btn" onclick="openDrawer('list')">
          📋 All (94)
        </button>
        <button class="hud-btn" onclick="openDrawer('fin')">
          💰 Stats
        </button>
      </div>
    </header>

    <!-- Progress Strip -->
    <div class="progress-strip">
      <span id="hud-verified-text">0 / 94 Tagged</span>
      <div class="progress-bar-wrap">
        <div class="progress-bar-fill" id="hud-progress-fill"></div>
      </div>
      <span id="hud-verified-pct" style="color: var(--accent-lime)">0%</span>
    </div>

    <!-- Center Deck (No Scrolling Required) -->
    <main class="deck-viewport">
      
      <!-- Current Item Card -->
      <div class="item-card" id="main-item-card">
        
        <div class="card-top">
          <div class="sticker-tag" id="main-sticker-tag">
            <span class="num" id="card-sticker-num">#1</span>
            <span class="bill-name" id="card-bill-source">WHITE</span>
          </div>

          <div class="status-badge" id="card-status-badge">
            <span id="status-icon">⚪</span>
            <span id="status-text">Pending</span>
          </div>
        </div>

        <h2 class="product-title" id="card-title">3 1/2 Lakshmi (15P)</h2>
        
        <div class="product-sub">
          <span>📦 In Stock: <strong id="card-units">20 Units</strong></span>
          <span id="card-pack" style="color: var(--text-3)">Pack: 20</span>
        </div>

        <!-- Costs Bar -->
        <div class="cost-strip">
          <div class="cost-strip-cell">
            <div class="label">Wholesale</div>
            <div class="val" id="card-base-rate">₹150</div>
          </div>
          <div class="cost-strip-cell highlight">
            <div class="label">Cost + 10%</div>
            <div class="val" style="color: var(--accent-gold);" id="card-cost-10">₹165</div>
          </div>
          <div class="cost-strip-cell box-total">
            <div class="label">Box Total (+10%)</div>
            <div class="val" id="card-box-cost">₹3,300</div>
          </div>
        </div>

        <!-- Retail Selling Price Hero Input -->
        <div class="price-hero">
          <div>
            <div class="price-hero-label">Target Selling Price (Write on Box)</div>
            <div class="price-hero-profit" id="card-profit-preview">+₹85 profit / unit (+52%)</div>
          </div>
          <div class="price-hero-val-wrap">
            <span class="price-hero-symbol">₹</span>
            <input type="number" class="price-hero-input" id="card-sp-input" value="250" oninput="onPriceEdit(this.value)">
          </div>
        </div>

        <!-- Quick 1-Tap Margin Pills -->
        <div class="margin-pills">
          <button class="m-pill" onclick="quickMargin(0.30)">+30%</button>
          <button class="m-pill" onclick="quickMargin(0.40)">+40%</button>
          <button class="m-pill" onclick="quickMargin(0.50)">+50%</button>
          <button class="m-pill" onclick="quickMargin(0.75)">+75%</button>
          <button class="m-pill" onclick="quickMargin(1.00)">2x</button>
        </div>

      </div>

      <!-- Giant One-Thumb Action Row -->
      <div class="action-row">
        <button class="btn-nav" onclick="stepItem(-1)" title="Previous Box">◀</button>
        
        <button class="btn-verify-huge" id="btn-verify-main" onclick="toggleVerified()">
          <span id="btn-verify-icon">✓</span>
          <span id="btn-verify-text">MARK TAGGED & NEXT</span>
        </button>

        <button class="btn-nav" onclick="stepItem(1)" title="Next Box">▶</button>
      </div>

      <!-- Ergonomic Thumb Numpad -->
      <div class="numpad-grid">
        <button class="key" onclick="tapKey('1')">1</button>
        <button class="key" onclick="tapKey('2')">2</button>
        <button class="key" onclick="tapKey('3')">3</button>
        <button class="key" onclick="tapKey('4')">4</button>
        <button class="key" onclick="tapKey('5')">5</button>
        <button class="key" onclick="tapKey('6')">6</button>
        <button class="key" onclick="tapKey('7')">7</button>
        <button class="key" onclick="tapKey('8')">8</button>
        <button class="key" onclick="tapKey('9')">9</button>
        <button class="key key-p" onclick="tapKey('P')">P<span class="key-sub">Pink</span></button>
        <button class="key" onclick="tapKey('0')">0</button>
        <button class="key key-del" onclick="tapKey('DEL')">⌫<span class="key-sub">Clear</span></button>
      </div>

    </main>

  </div>

  <!-- DRAWER: ALL ITEMS SEARCH LIST -->
  <div class="drawer-overlay" id="drawer-list" onclick="closeDrawer('list')">
    <div class="drawer-sheet" onclick="event.stopPropagation()">
      <div class="drawer-header">
        <h3>Master Inventory (94 Items)</h3>
        <button class="drawer-close" onclick="closeDrawer('list')">✕</button>
      </div>
      <input type="text" class="drawer-search" id="drawer-search-input" placeholder="Search by name, sticker #, rate..." oninput="filterDrawerList(this.value)">
      <div class="drawer-list" id="drawer-list-items">
        <!-- Rendered by JS -->
      </div>
    </div>
  </div>

  <!-- DRAWER: FINANCIAL STATS -->
  <div class="drawer-overlay" id="drawer-fin" onclick="closeDrawer('fin')">
    <div class="drawer-sheet" onclick="event.stopPropagation()">
      <div class="drawer-header">
        <h3>Financial Snapshot</h3>
        <button class="drawer-close" onclick="closeDrawer('fin')">✕</button>
      </div>
      
      <div style="padding: 10px 0;">
        <div class="fin-row">
          <span style="color: var(--text-2)">Stock Purchase (94 items)</span>
          <span style="font-family: var(--font-mono)">₹3,32,518</span>
        </div>
        <div class="fin-row">
          <span style="color: var(--text-2)">Stock Cost (+10% Overhead)</span>
          <span style="font-family: var(--font-mono); color: var(--accent-gold)">₹3,65,770</span>
        </div>
        <div class="fin-row">
          <span style="color: var(--text-2)">Shed & Permissions Expense</span>
          <span style="font-family: var(--font-mono)">₹74,700</span>
        </div>
        <div class="fin-row">
          <span style="color: var(--text-2)">Total Project Investment</span>
          <span style="font-family: var(--font-mono); color: #f87171">₹4,07,218</span>
        </div>
        <div class="fin-row total">
          <span>Projected Sales Revenue</span>
          <span id="fin-total-sales">₹0</span>
        </div>
        <div class="fin-row" style="font-weight: 800; font-size: 16px; color: var(--accent-lime); padding-top: 8px;">
          <span>Projected Net Profit</span>
          <span id="fin-net-profit">₹0</span>
        </div>
        <div class="fin-row" style="border: none; padding-top: 14px; font-size: 11px; color: var(--text-3)">
          <span>Paid so far: ₹2,20,000 | Pending: ₹1,12,518</span>
        </div>
      </div>
    </div>
  </div>

  <script>
    const MASTER_ITEMS = {items_json_str};

    let items = [];
    let currentIndex = 0;
    let typedBuffer = "";
    let bufferTimer = null;
    let voiceActive = false;

    // Web Audio Click & Chime Feedback
    const ctx = new (window.AudioContext || window.webkitAudioContext)();
    function clickSound(freq = 550, dur = 0.04) {{
      try {{
        if (ctx.state === 'suspended') ctx.resume();
        const osc = ctx.createOscillator();
        const g = ctx.createGain();
        osc.frequency.value = freq;
        osc.connect(g);
        g.connect(ctx.destination);
        g.gain.setValueAtTime(0.08, ctx.currentTime);
        g.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + dur);
        osc.start();
        osc.stop(ctx.currentTime + dur);
      }} catch(e) {{}}
    }}

    function successChime() {{
      clickSound(523.25, 0.08);
      setTimeout(() => clickSound(659.25, 0.08), 80);
      setTimeout(() => clickSound(783.99, 0.15), 160);
    }}

    // App Initialization
    function init() {{
      const saved = localStorage.getItem('diwali_cracker_items_v2');
      if (saved) {{
        try {{
          items = JSON.parse(saved);
        }} catch(e) {{
          items = JSON.parse(JSON.stringify(MASTER_ITEMS));
        }}
      }} else {{
        items = JSON.parse(JSON.stringify(MASTER_ITEMS));
      }}

      const lastIdx = localStorage.getItem('diwali_last_idx_v2');
      if (lastIdx !== null && items[lastIdx]) {{
        currentIndex = parseInt(lastIdx);
      }}

      render();
      updateMetrics();
      renderDrawerList();

      // Keyboard physical support
      window.addEventListener('keydown', (e) => {{
        if (e.target.tagName === 'INPUT') return;
        if (e.key >= '0' && e.key <= '9') tapKey(e.key);
        else if (e.key === 'p' || e.key === 'P') tapKey('P');
        else if (e.key === 'Backspace') tapKey('DEL');
        else if (e.key === 'Enter' || e.key === ' ') {{
          e.preventDefault();
          toggleVerified();
        }}
        else if (e.key === 'ArrowRight') stepItem(1);
        else if (e.key === 'ArrowLeft') stepItem(-1);
      }});
    }}

    function save() {{
      localStorage.setItem('diwali_cracker_items_v2', JSON.stringify(items));
      localStorage.setItem('diwali_last_idx_v2', currentIndex.toString());
      updateMetrics();
    }}

    // Numpad Tap
    function tapKey(key) {{
      clickSound(600, 0.03);
      if (navigator.vibrate) navigator.vibrate(15);

      if (key === 'DEL') {{
        typedBuffer = "";
        return;
      }}

      typedBuffer += key;
      clearTimeout(bufferTimer);

      // Search immediately for match
      const query = typedBuffer.toLowerCase();
      const matchIdx = items.findIndex(i => i.sticker_no.toLowerCase() === query);

      if (matchIdx !== -1) {{
        currentIndex = matchIdx;
        render();
        // Reset buffer after 1.2s of inactivity
        bufferTimer = setTimeout(() => {{ typedBuffer = ""; }}, 1200);
      }} else {{
        // Buffer timeout
        bufferTimer = setTimeout(() => {{ typedBuffer = ""; }}, 1800);
      }}
    }}

    // Render Current Card
    function render() {{
      const item = items[currentIndex];
      if (!item) return;

      const numEl = document.getElementById('card-sticker-num');
      const tagEl = document.getElementById('main-sticker-tag');
      const sourceEl = document.getElementById('card-bill-source');
      const catEl = document.getElementById('bill-category-label');

      numEl.textContent = '#' + item.sticker_no;
      if (item.bill_type === 'pink') {{
        tagEl.classList.add('pink-tag');
        sourceEl.textContent = 'PINK SLIP';
        catEl.textContent = 'Pink Bill (Chinna Pasumarru)';
      }} else {{
        tagEl.classList.remove('pink-tag');
        sourceEl.textContent = 'WHITE BILL';
        catEl.textContent = 'White Bill #1–74 (Nandigama)';
      }}

      document.getElementById('card-title').textContent = item.name;
      document.getElementById('card-units').textContent = item.units + ' Units';
      document.getElementById('card-pack').textContent = 'Pack: ' + item.pack_details;

      document.getElementById('card-base-rate').textContent = '₹' + item.rate;
      document.getElementById('card-cost-10').textContent = '₹' + Math.round(item.rate_plus_10);
      document.getElementById('card-box-cost').textContent = '₹' + Math.round(item.units * item.rate_plus_10).toLocaleString('en-IN');

      const spInput = document.getElementById('card-sp-input');
      spInput.value = item.selling_price;
      updateProfitPreview();

      // Verified styling
      const card = document.getElementById('main-item-card');
      const badge = document.getElementById('card-status-badge');
      const statusIcon = document.getElementById('status-icon');
      const statusText = document.getElementById('status-text');
      const verifyBtn = document.getElementById('btn-verify-main');
      const verifyText = document.getElementById('btn-verify-text');

      if (item.verified) {{
        card.classList.add('is-verified');
        badge.className = 'status-badge verified';
        statusIcon.textContent = '✓';
        statusText.textContent = 'Tagged';
        verifyBtn.className = 'btn-verify-huge is-verified';
        verifyText.textContent = 'TAGGED (TAP TO UNMARK)';
      }} else {{
        card.classList.remove('is-verified');
        badge.className = 'status-badge';
        statusIcon.textContent = '⚪';
        statusText.textContent = 'Pending';
        verifyBtn.className = 'btn-verify-huge';
        verifyText.textContent = 'MARK TAGGED & NEXT';
      }}

      if (voiceActive) {{
        announceVoice(item);
      }}
    }}

    function updateProfitPreview() {{
      const item = items[currentIndex];
      const sp = parseFloat(document.getElementById('card-sp-input').value) || 0;
      item.selling_price = sp;
      const profitPerUnit = sp - item.rate_plus_10;
      const marginPct = item.rate_plus_10 > 0 ? ((profitPerUnit / item.rate_plus_10) * 100).toFixed(0) : 0;
      const totalBoxProfit = profitPerUnit * item.units;

      const previewEl = document.getElementById('card-profit-preview');
      previewEl.textContent = `+₹${{Math.round(profitPerUnit)}} / unit (+${{marginPct}}%) • Box: +₹${{Math.round(totalBoxProfit).toLocaleString('en-IN')}}`;
      previewEl.style.color = profitPerUnit >= 0 ? '#34d399' : '#f87171';
    }}

    function onPriceEdit(val) {{
      items[currentIndex].selling_price = parseFloat(val) || 0;
      updateProfitPreview();
      save();
    }}

    function quickMargin(multiplier) {{
      clickSound(700, 0.04);
      const item = items[currentIndex];
      const raw = item.rate_plus_10 * (1 + multiplier);
      let rounded = Math.ceil(raw / 10) * 10;
      if (raw <= 30) rounded = Math.ceil(raw / 5) * 5;
      item.selling_price = rounded;
      document.getElementById('card-sp-input').value = rounded;
      updateProfitPreview();
      save();
    }}

    // Toggle Verified Button
    function toggleVerified() {{
      const item = items[currentIndex];
      item.verified = !item.verified;

      if (item.verified) {{
        successChime();
        if (navigator.vibrate) navigator.vibrate([30, 50, 70]);
      }} else {{
        clickSound(300, 0.08);
      }}

      save();
      render();
      renderDrawerList();

      // Auto-advance to next box
      if (item.verified) {{
        setTimeout(() => {{
          typedBuffer = "";
          stepItem(1);
        }}, 450);
      }}
    }}

    function stepItem(dir) {{
      clickSound(500, 0.03);
      typedBuffer = "";
      let next = currentIndex + dir;
      if (next < 0) next = items.length - 1;
      if (next >= items.length) next = 0;
      currentIndex = next;
      render();
    }}

    // Metrics & Financials
    function updateMetrics() {{
      const verified = items.filter(i => i.verified).length;
      const total = items.length;
      const pct = Math.round((verified / total) * 100);

      document.getElementById('hud-verified-text').textContent = `${{verified}} / ${{total}} Tagged`;
      document.getElementById('hud-progress-fill').style.width = pct + '%';
      document.getElementById('hud-verified-pct').textContent = pct + '%';

      let totalSales = 0;
      items.forEach(i => {{
        totalSales += (i.selling_price || 0) * i.units;
      }});
      const totalInv = 407218;
      const netProfit = totalSales - totalInv;

      document.getElementById('fin-total-sales').textContent = '₹' + Math.round(totalSales).toLocaleString('en-IN');
      document.getElementById('fin-net-profit').textContent = '₹' + Math.round(netProfit).toLocaleString('en-IN');
    }}

    // Voice Readout
    function toggleVoice() {{
      voiceActive = !voiceActive;
      const btn = document.getElementById('btn-voice-toggle');
      const icon = document.getElementById('voice-icon');
      if (voiceActive) {{
        btn.classList.add('active');
        icon.textContent = '🔊';
        successChime();
        speak('Voice activated');
      }} else {{
        btn.classList.remove('active');
        icon.textContent = '🔈';
        clickSound(350, 0.08);
      }}
    }}

    function announceVoice(item) {{
      const text = `Box ${{item.sticker_no}}, ${{item.name}}, Cost ${{Math.round(item.rate_plus_10)}}, Sell ${{item.selling_price}}`;
      speak(text);
    }}

    function speak(text) {{
      if (!('speechSynthesis' in window)) return;
      window.speechSynthesis.cancel();
      const u = new SpeechSynthesisUtterance(text);
      u.rate = 1.1;
      window.speechSynthesis.speak(u);
    }}

    // Drawers
    function openDrawer(id) {{
      clickSound(600, 0.04);
      document.getElementById('drawer-' + id).classList.add('open');
      if (id === 'list') {{
        setTimeout(() => document.getElementById('drawer-search-input').focus(), 150);
      }}
    }}

    function closeDrawer(id) {{
      document.getElementById('drawer-' + id).classList.remove('open');
    }}

    function renderDrawerList(filter = "") {{
      const container = document.getElementById('drawer-list-items');
      container.innerHTML = "";
      const term = filter.toLowerCase();

      items.forEach((item, idx) => {{
        if (term && !item.name.toLowerCase().includes(term) && !item.sticker_no.toLowerCase().includes(term)) {{
          return;
        }}

        const row = document.createElement('div');
        row.className = `drawer-item-row ${{item.verified ? 'verified' : ''}}`;
        row.innerHTML = `
          <div>
            <div style="font-weight: 700; font-size: 13px;">
              <span style="color: ${{item.bill_type==='pink'?'#f43f5e':'#fbbf24'}}; font-family: var(--font-mono); font-weight: 800;">#${{item.sticker_no}}</span>
              ${{item.name}}
            </div>
            <div style="font-size: 11px; color: var(--text-3); font-family: var(--font-mono)">
              ${{item.units}} Units • Cost ₹${{Math.round(item.rate_plus_10)}}
            </div>
          </div>
          <div style="text-align: right;">
            <div style="font-family: var(--font-mono); font-weight: 800; color: var(--accent-lime); font-size: 15px;">
              ₹${{item.selling_price}}
            </div>
            <div style="font-size: 10px; color: ${{item.verified ? '#34d399' : 'var(--text-3)'}}">
              ${{item.verified ? 'Tagged ✓' : 'Pending'}}
            </div>
          </div>
        `;
        row.onclick = () => {{
          currentIndex = idx;
          render();
          closeDrawer('list');
        }};
        container.appendChild(row);
      }});
    }}

    function filterDrawerList(val) {{
      renderDrawerList(val);
    }}

    window.addEventListener('DOMContentLoaded', init);
  </script>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_code)

print("Ultra-minimalist mobile-first index.html built successfully!")
