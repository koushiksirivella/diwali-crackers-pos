import json

with open("items_data.json", "r", encoding="utf-8") as f:
    items = json.load(f)

# Add remaining_units default equal to initial units
for it in items:
    it["remaining_units"] = it["units"]
    it["sold_units"] = 0

items_json_str = json.dumps(items)

html_code = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
  <title>Diwali Crackers Scanner & POS • Nandigama</title>
  <link rel="manifest" href="manifest.json">
  <meta name="theme-color" content="#090b0e">
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;700;800&display=swap" rel="stylesheet">
  <style>
    /* =========================================================================
       LUXURY MINIMALIST TOKENS (Haoqi / Why-Zero aesthetic from exp)
       Matte Obsidian (#090b0e), Frosted Glass HUD, Electric Lime (#c0fe04), Gold (#fbbf24)
       ========================================================================= */
    :root {{
      --bg-deep: #090b0e;
      --bg-surface: #12151b;
      --bg-card: rgba(22, 27, 36, 0.72);
      --border-subtle: rgba(255, 255, 255, 0.08);
      --border-active: rgba(192, 254, 4, 0.5);
      
      --accent-lime: #c0fe04;
      --accent-lime-dim: rgba(192, 254, 4, 0.15);
      --accent-gold: #fbbf24;
      --accent-pink: #f43f5e;
      --accent-green: #10b981;
      --accent-cyan: #06b6d4;
      
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

    /* Fullscreen Mobile Viewport Shell */
    .app-shell {{
      height: 100%;
      height: 100dvh;
      display: flex;
      flex-direction: column;
      max-width: 480px;
      margin: 0 auto;
      position: relative;
      background: radial-gradient(circle at 50% 0%, #151c27 0%, var(--bg-deep) 80%);
    }}

    /* Top Glass Navigation HUD */
    .top-hud {{
      padding: 8px 12px 4px 12px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 8px;
      z-index: 20;
    }}

    .brand-pill {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 6px 10px;
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid var(--border-subtle);
      border-radius: 999px;
      backdrop-filter: blur(12px);
      cursor: pointer;
    }}

    .brand-pill .spark {{
      color: var(--accent-gold);
      font-size: 13px;
    }}

    .brand-pill span {{
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.03em;
      text-transform: uppercase;
      color: var(--text-2);
    }}

    .hud-actions {{
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    .hud-pill {{
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid var(--border-subtle);
      color: var(--text-2);
      border-radius: 999px;
      padding: 6px 10px;
      font-size: 11px;
      font-weight: 700;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 4px;
      backdrop-filter: blur(12px);
      transition: all 0.15s;
    }}

    .hud-pill.active {{
      background: var(--accent-lime-dim);
      border-color: var(--accent-lime);
      color: var(--accent-lime);
    }}

    .hud-pill.cart-badge {{
      border-color: var(--accent-cyan);
      color: var(--accent-cyan);
    }}

    /* Progress Tracker Strip */
    .progress-strip {{
      padding: 2px 14px 4px 14px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-size: 10px;
      font-family: var(--font-mono);
      color: var(--text-3);
    }}

    .progress-track {{
      flex: 1;
      height: 4px;
      background: rgba(255, 255, 255, 0.05);
      border-radius: 99px;
      margin: 0 10px;
      overflow: hidden;
    }}

    .progress-bar {{
      height: 100%;
      background: var(--accent-lime);
      width: 0%;
      transition: width 0.3s var(--ease-snap);
      box-shadow: 0 0 8px var(--accent-lime);
    }}

    /* Mode Navigation Tabs (Scanner vs POS Cart vs Stock) */
    .view-switcher {{
      display: flex;
      padding: 2px 12px 6px 12px;
      gap: 6px;
    }}

    .tab-switch-btn {{
      flex: 1;
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid var(--border-subtle);
      color: var(--text-2);
      border-radius: 10px;
      padding: 6px 0;
      font-size: 11px;
      font-weight: 700;
      cursor: pointer;
      text-align: center;
      transition: all 0.15s;
    }}

    .tab-switch-btn.active {{
      background: var(--bg-card);
      border-color: var(--accent-lime);
      color: #fff;
    }}

    /* Center Viewport (Single Screen, No Scroll) */
    .deck-content {{
      flex: 1;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      padding: 2px 12px 8px 12px;
      overflow: hidden;
    }}

    /* Item Card */
    .scanner-card {{
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: 18px;
      padding: 12px 14px;
      backdrop-filter: blur(20px);
      box-shadow: 0 10px 25px rgba(0,0,0,0.4);
      position: relative;
      transition: all 0.2s var(--ease-snap);
    }}

    .scanner-card.is-verified {{
      border-color: rgba(16, 185, 129, 0.45);
      background: linear-gradient(180deg, rgba(16, 185, 129, 0.07) 0%, rgba(22, 27, 36, 0.85) 100%);
    }}

    .card-meta-row {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 6px;
    }}

    .tag-badge {{
      display: inline-flex;
      align-items: center;
      gap: 5px;
      background: #000;
      border: 1px solid rgba(255, 255, 255, 0.15);
      padding: 3px 10px;
      border-radius: 8px;
    }}

    .tag-badge .num {{
      font-size: 1.25rem;
      font-weight: 800;
      font-family: var(--font-mono);
      color: #fff;
    }}

    .tag-badge.pink-tag .num {{
      color: #fb7185;
    }}

    .tag-badge .src {{
      font-size: 9px;
      color: var(--text-3);
      text-transform: uppercase;
      font-weight: 700;
    }}

    .status-pill {{
      display: inline-flex;
      align-items: center;
      gap: 4px;
      font-size: 10px;
      font-weight: 700;
      text-transform: uppercase;
      padding: 3px 8px;
      border-radius: 999px;
      background: rgba(255, 255, 255, 0.04);
      color: var(--text-3);
      border: 1px solid var(--border-subtle);
    }}

    .status-pill.verified {{
      background: rgba(16, 185, 129, 0.15);
      border-color: rgba(16, 185, 129, 0.4);
      color: #34d399;
    }}

    .item-name-text {{
      font-size: 1.35rem;
      font-weight: 800;
      color: #fff;
      line-height: 1.15;
      margin-bottom: 4px;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      letter-spacing: -0.01em;
    }}

    .item-stock-sub {{
      font-size: 11px;
      font-weight: 600;
      color: var(--text-2);
      display: flex;
      justify-content: space-between;
      margin-bottom: 8px;
    }}

    .item-stock-sub strong {{
      color: var(--accent-gold);
      font-family: var(--font-mono);
    }}

    /* Compact Cost Strip */
    .mini-cost-strip {{
      display: grid;
      grid-template-columns: 1fr 1fr 1fr;
      gap: 6px;
      background: rgba(0, 0, 0, 0.35);
      border: 1px solid var(--border-subtle);
      border-radius: 10px;
      padding: 6px 10px;
      margin-bottom: 8px;
      text-align: center;
    }}

    .mini-cell .lbl {{
      font-size: 8.5px;
      text-transform: uppercase;
      font-weight: 700;
      color: var(--text-3);
    }}

    .mini-cell .val {{
      font-size: 13px;
      font-weight: 700;
      font-family: var(--font-mono);
      color: var(--text-2);
    }}

    .mini-cell.highlight .val {{
      color: var(--accent-gold);
    }}

    .mini-cell.box-cost .val {{
      color: #fff;
    }}

    /* Selling Price Hero */
    .price-action-box {{
      background: linear-gradient(135deg, rgba(192, 254, 4, 0.08) 0%, rgba(0, 0, 0, 0.45) 100%);
      border: 1.5px solid var(--accent-lime);
      border-radius: 12px;
      padding: 8px 12px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}

    .price-action-left .title {{
      font-size: 9.5px;
      font-weight: 800;
      text-transform: uppercase;
      color: var(--accent-lime);
      letter-spacing: 0.05em;
    }}

    .price-action-left .profit-badge {{
      font-size: 10.5px;
      font-family: var(--font-mono);
      font-weight: 700;
      color: #34d399;
      margin-top: 1px;
    }}

    .price-action-right {{
      display: flex;
      align-items: baseline;
      gap: 3px;
    }}

    .price-action-right .sym {{
      font-size: 1.4rem;
      font-weight: 800;
      color: var(--accent-lime);
      font-family: var(--font-mono);
    }}

    .price-action-right input {{
      width: 100px;
      background: transparent;
      border: none;
      color: #fff;
      font-size: 2rem;
      font-weight: 800;
      font-family: var(--font-mono);
      text-align: right;
      outline: none;
    }}

    /* Margin Pills */
    .margin-strip {{
      display: flex;
      gap: 5px;
      margin-top: 6px;
    }}

    .m-btn {{
      flex: 1;
      background: rgba(255, 255, 255, 0.035);
      border: 1px solid var(--border-subtle);
      color: var(--text-2);
      font-size: 10.5px;
      font-family: var(--font-mono);
      font-weight: 700;
      padding: 5px 0;
      border-radius: 7px;
      cursor: pointer;
      text-align: center;
      transition: all 0.15s;
    }}

    .m-btn:active {{
      background: var(--accent-lime);
      color: #000;
      border-color: var(--accent-lime);
      transform: scale(0.96);
    }}

    /* Action Row (Tag & Next + Cart Add) */
    .cta-row {{
      margin-top: 6px;
      display: flex;
      gap: 6px;
    }}

    .btn-step-nav {{
      width: 44px;
      height: 48px;
      border-radius: 12px;
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid var(--border-subtle);
      color: #fff;
      font-size: 1.1rem;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      touch-action: manipulation;
    }}

    .btn-step-nav:active {{
      background: rgba(255, 255, 255, 0.12);
      transform: scale(0.94);
    }}

    .btn-tag-main {{
      flex: 1;
      height: 48px;
      border-radius: 12px;
      border: none;
      background: var(--accent-lime);
      color: #000000;
      font-family: var(--font-sans);
      font-size: 0.95rem;
      font-weight: 800;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      box-shadow: 0 4px 14px rgba(192, 254, 4, 0.3);
      transition: all 0.15s var(--ease-snap);
      touch-action: manipulation;
    }}

    .btn-tag-main:active {{
      transform: scale(0.97);
      background: #a3dc00;
    }}

    .btn-tag-main.is-verified {{
      background: rgba(255, 255, 255, 0.08);
      color: var(--text-2);
      box-shadow: none;
      border: 1px solid var(--border-subtle);
    }}

    .btn-add-cart {{
      width: 48px;
      height: 48px;
      border-radius: 12px;
      background: rgba(6, 182, 212, 0.15);
      border: 1px solid var(--accent-cyan);
      color: var(--accent-cyan);
      font-size: 1.15rem;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      touch-action: manipulation;
    }}

    .btn-add-cart:active {{
      background: var(--accent-cyan);
      color: #000;
      transform: scale(0.94);
    }}

    /* Fixed Thumb Numpad */
    .numpad-grid {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 5px;
      margin-top: 4px;
    }}

    .key-btn {{
      height: 44px;
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid rgba(255, 255, 255, 0.06);
      border-radius: 10px;
      color: #ffffff;
      font-size: 1.25rem;
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

    .key-btn:active {{
      background: var(--accent-lime);
      color: #000;
      transform: scale(0.94);
      border-color: var(--accent-lime);
    }}

    .key-btn.key-p {{
      color: var(--accent-pink);
      font-size: 1.1rem;
      font-weight: 800;
    }}

    .key-btn.key-del {{
      color: var(--text-3);
      font-size: 1rem;
    }}

    .key-btn-sub {{
      font-size: 6.5px;
      font-family: var(--font-sans);
      text-transform: uppercase;
      color: var(--text-3);
      line-height: 1;
    }}

    .key-btn:active .key-btn-sub {{
      color: #000;
    }}

    /* POS BILLING VIEW */
    #view-pos {{
      display: none;
      flex: 1;
      flex-direction: column;
      justify-content: space-between;
      overflow: hidden;
    }}

    .pos-cart-list {{
      flex: 1;
      overflow-y: auto;
      display: flex;
      flex-direction: column;
      gap: 6px;
      padding: 4px 0;
      margin-bottom: 8px;
    }}

    .pos-cart-item {{
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: 12px;
      padding: 8px 10px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}

    .pos-item-info strong {{
      font-size: 13px;
      color: #fff;
    }}

    .pos-item-info span {{
      font-size: 11px;
      color: var(--text-3);
      font-family: var(--font-mono);
    }}

    .pos-qty-controls {{
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    .qty-btn {{
      width: 28px;
      height: 28px;
      border-radius: 8px;
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid var(--border-subtle);
      color: #fff;
      font-size: 14px;
      font-weight: 800;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
    }}

    .qty-val {{
      font-family: var(--font-mono);
      font-weight: 800;
      font-size: 14px;
      width: 24px;
      text-align: center;
    }}

    .pos-checkout-panel {{
      background: #11151d;
      border: 1px solid var(--border-subtle);
      border-radius: 14px;
      padding: 10px 12px;
    }}

    .pos-summary-row {{
      display: flex;
      justify-content: space-between;
      font-size: 12px;
      color: var(--text-2);
      margin-bottom: 4px;
      font-family: var(--font-mono);
    }}

    .pos-summary-row.total {{
      font-size: 1.25rem;
      font-weight: 800;
      color: var(--accent-lime);
      border-top: 1px solid var(--border-subtle);
      padding-top: 6px;
      margin-top: 4px;
    }}

    .pos-btn-row {{
      display: flex;
      gap: 8px;
      margin-top: 8px;
    }}

    .btn-pos-wa {{
      flex: 2;
      background: #25d366;
      color: #000;
      font-weight: 800;
      font-size: 13px;
      border: none;
      border-radius: 10px;
      padding: 10px;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      cursor: pointer;
    }}

    .btn-pos-clear {{
      flex: 1;
      background: rgba(239, 68, 68, 0.15);
      border: 1px solid rgba(239, 68, 68, 0.4);
      color: #fca5a5;
      font-weight: 700;
      font-size: 12px;
      border-radius: 10px;
      cursor: pointer;
    }}

    /* BOTTOM SHEETS / DRAWERS */
    .drawer-scrim {{
      display: none;
      position: fixed;
      inset: 0;
      background: rgba(0, 0, 0, 0.75);
      backdrop-filter: blur(12px);
      z-index: 50;
      flex-direction: column;
      justify-content: flex-end;
    }}

    .drawer-scrim.open {{
      display: flex;
    }}

    .drawer-box {{
      background: #0f131a;
      border-top: 1px solid var(--border-subtle);
      border-radius: 20px 20px 0 0;
      max-height: 85vh;
      display: flex;
      flex-direction: column;
      padding: 16px 14px;
      animation: sheetUp 0.2s var(--ease-snap);
    }}

    @keyframes sheetUp {{
      from {{ transform: translateY(100%); }}
      to {{ transform: translateY(0); }}
    }}

    .drawer-top-bar {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 10px;
    }}

    .drawer-top-bar h3 {{
      font-size: 15px;
      font-weight: 800;
    }}

    .btn-drawer-x {{
      background: rgba(255,255,255,0.06);
      border: none;
      color: #fff;
      width: 28px;
      height: 28px;
      border-radius: 50%;
      cursor: pointer;
      font-weight: 800;
    }}

    .drawer-search-bar {{
      background: rgba(0,0,0,0.5);
      border: 1px solid var(--border-subtle);
      border-radius: 10px;
      padding: 8px 12px;
      color: #fff;
      font-size: 13px;
      margin-bottom: 10px;
      outline: none;
      width: 100%;
    }}

    .drawer-scroll-list {{
      overflow-y: auto;
      flex: 1;
      display: flex;
      flex-direction: column;
      gap: 5px;
      max-height: 55vh;
    }}

    .drawer-list-item {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: rgba(255,255,255,0.02);
      border: 1px solid var(--border-subtle);
      padding: 8px 10px;
      border-radius: 8px;
      cursor: pointer;
    }}

    .drawer-list-item:hover {{
      background: rgba(192, 254, 4, 0.05);
      border-color: var(--accent-lime);
    }}

    .drawer-list-item.is-verified {{
      border-left: 3px solid var(--accent-green);
    }}

    /* CAMERA SCANNER MODAL */
    .cam-modal {{
      display: none;
      position: fixed;
      inset: 0;
      background: #000;
      z-index: 60;
      flex-direction: column;
    }}

    .cam-modal.open {{
      display: flex;
    }}

    .cam-header {{
      padding: 12px 16px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: rgba(0,0,0,0.7);
      backdrop-filter: blur(10px);
      z-index: 2;
    }}

    .cam-video-wrap {{
      flex: 1;
      position: relative;
      display: flex;
      align-items: center;
      justify-content: center;
      overflow: hidden;
    }}

    #cam-stream {{
      width: 100%;
      height: 100%;
      object-fit: cover;
    }}

    .cam-reticle {{
      position: absolute;
      width: 240px;
      height: 140px;
      border: 2px dashed var(--accent-lime);
      border-radius: 16px;
      box-shadow: 0 0 0 4000px rgba(0, 0, 0, 0.55);
      pointer-events: none;
      display: flex;
      align-items: center;
      justify-content: center;
      color: var(--accent-lime);
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }}

    /* CREDITS MODAL */
    .credits-card {{
      background: #11151c;
      border: 1px solid var(--border-subtle);
      border-radius: 14px;
      padding: 12px;
      margin-bottom: 12px;
    }}

    .credits-card h4 {{
      font-size: 12px;
      text-transform: uppercase;
      color: var(--accent-gold);
      margin-bottom: 4px;
    }}

    .credits-card p {{
      font-size: 12px;
      color: var(--text-2);
      line-height: 1.4;
    }}

    /* Desktop View Optimization */
    @media (min-width: 768px) {{
      .app-shell {{
        max-width: 440px;
        height: 94vh;
        border-radius: 28px;
        border: 1px solid var(--border-subtle);
        box-shadow: 0 25px 60px rgba(0, 0, 0, 0.8), 0 0 40px rgba(192, 254, 4, 0.1);
        margin: 3vh auto;
      }}
    }}
  </style>
</head>
<body>

  <div class="app-shell">
    
    <!-- Top Glass HUD -->
    <header class="top-hud">
      <div class="brand-pill" onclick="openSheet('credits')">
        <span class="spark">🪔</span>
        <span id="active-source-badge">Nandigama Stall</span>
      </div>

      <div class="hud-actions">
        <button class="hud-pill" id="btn-cam" onclick="openCameraScanner()" title="Scan Box Sticker with Camera">
          📷 Cam
        </button>
        <button class="hud-pill" id="btn-voice-pill" onclick="toggleVoice()">
          <span id="voice-icon">🔈</span> En
        </button>
        <button class="hud-pill cart-badge" id="btn-cart-toggle" onclick="switchMainView('pos')">
          🛒 <span id="cart-item-count">0</span>
        </button>
      </div>
    </header>

    <!-- Progress Strip -->
    <div class="progress-strip">
      <span id="progress-text">0 / 94 Tagged</span>
      <div class="progress-track">
        <div class="progress-bar" id="progress-fill"></div>
      </div>
      <span id="progress-pct" style="color: var(--accent-lime)">0%</span>
    </div>

    <!-- Mode Switcher Tabs -->
    <nav class="view-switcher">
      <button class="tab-switch-btn active" id="tab-nav-scan" onclick="switchMainView('scanner')">⚡ Box Scanner</button>
      <button class="tab-switch-btn" id="tab-nav-pos" onclick="switchMainView('pos')">🛒 POS Bill</button>
      <button class="tab-switch-btn" id="tab-nav-all" onclick="openSheet('inventory')">📦 All (94)</button>
      <button class="tab-switch-btn" id="tab-nav-stats" onclick="openSheet('stats')">💰 P&L Stats</button>
    </nav>

    <!-- Content Deck -->
    <div class="deck-content">

      <!-- VIEW 1: BOX SCANNER HERO -->
      <section id="view-scanner">
        
        <div class="scanner-card" id="scanner-box-card">
          <div class="card-meta-row">
            <div class="tag-badge" id="card-tag-badge">
              <span class="num" id="card-num">#1</span>
              <span class="src" id="card-src">WHITE BILL</span>
            </div>
            <div class="status-pill" id="card-status-pill">
              <span id="status-symbol">⚪</span>
              <span id="status-title">Pending</span>
            </div>
          </div>

          <h2 class="item-name-text" id="card-name">3 1/2 Lakshmi (15P)</h2>

          <div class="item-stock-sub">
            <span>📦 Total Stock: <strong id="card-qty">20 Units</strong></span>
            <span>Rem: <strong id="card-rem" style="color: var(--accent-lime)">20</strong></span>
            <span id="card-pack" style="color: var(--text-3)">Pack: 20</span>
          </div>

          <!-- Cost Bar -->
          <div class="mini-cost-strip">
            <div class="mini-cell">
              <div class="lbl">Wholesale</div>
              <div class="val" id="card-rate">₹150</div>
            </div>
            <div class="mini-cell highlight">
              <div class="lbl">Cost + 10%</div>
              <div class="val" id="card-cost10">₹165</div>
            </div>
            <div class="mini-cell box-cost">
              <div class="lbl">Box Total (+10%)</div>
              <div class="val" id="card-total-box">₹3,300</div>
            </div>
          </div>

          <!-- Retail Price Tag -->
          <div class="price-action-box">
            <div class="price-action-left">
              <div class="title">Retail Selling Price (Write on Box)</div>
              <div class="profit-badge" id="card-profit-lbl">+₹85 profit / unit (+52%)</div>
            </div>
            <div class="price-action-right">
              <span class="sym">₹</span>
              <input type="number" id="card-sp" value="250" oninput="onPriceChange(this.value)">
            </div>
          </div>

          <!-- Margin Pills -->
          <div class="margin-strip">
            <button class="m-btn" onclick="applyMargin(0.30)">+30%</button>
            <button class="m-btn" onclick="applyMargin(0.40)">+40%</button>
            <button class="m-btn" onclick="applyMargin(0.50)">+50%</button>
            <button class="m-btn" onclick="applyMargin(0.75)">+75%</button>
            <button class="m-btn" onclick="applyMargin(1.00)">2x</button>
          </div>
        </div>

        <!-- Single-Thumb Action Row -->
        <div class="cta-row">
          <button class="btn-step-nav" onclick="stepItem(-1)" title="Previous">◀</button>
          
          <button class="btn-tag-main" id="btn-tag-action" onclick="toggleTagItem()">
            <span id="btn-tag-icon">✓</span>
            <span id="btn-tag-text">MARK TAGGED & NEXT</span>
          </button>

          <button class="btn-add-cart" onclick="addToCartCurrent()" title="Add 1 to Customer Bill">
            +🛒
          </button>

          <button class="btn-step-nav" onclick="stepItem(1)" title="Next">▶</button>
        </div>

        <!-- Ergonomic Numpad -->
        <div class="numpad-grid">
          <button class="key-btn" onclick="pressKey('1')">1</button>
          <button class="key-btn" onclick="pressKey('2')">2</button>
          <button class="key-btn" onclick="pressKey('3')">3</button>
          <button class="key-btn" onclick="pressKey('4')">4</button>
          <button class="key-btn" onclick="pressKey('5')">5</button>
          <button class="key-btn" onclick="pressKey('6')">6</button>
          <button class="key-btn" onclick="pressKey('7')">7</button>
          <button class="key-btn" onclick="pressKey('8')">8</button>
          <button class="key-btn" onclick="pressKey('9')">9</button>
          <button class="key-btn key-p" onclick="pressKey('P')">P<span class="key-btn-sub">Pink</span></button>
          <button class="key-btn" onclick="pressKey('0')">0</button>
          <button class="key-btn key-del" onclick="pressKey('DEL')">⌫<span class="key-btn-sub">Clear</span></button>
        </div>

      </section>

      <!-- VIEW 2: POS CUSTOMER BILLING -->
      <section id="view-pos">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
          <h3 style="font-size: 14px; font-weight: 800; color: var(--accent-cyan);">🛒 Active Customer Cart</h3>
          <span style="font-size: 11px; color: var(--text-3);" id="pos-items-label">0 items</span>
        </div>

        <div class="pos-cart-list" id="pos-cart-items-container">
          <div style="text-align: center; color: var(--text-3); font-size: 13px; margin-top: 40px;">
            Cart is empty.<br>Tap <span style="color: var(--accent-cyan); font-weight: 700;">+🛒</span> on any box in Scanner or search to add!
          </div>
        </div>

        <div class="pos-checkout-panel">
          <div class="pos-summary-row">
            <span>Subtotal</span>
            <span id="pos-subtotal">₹0</span>
          </div>
          <div class="pos-summary-row" style="align-items: center;">
            <span>Festival Discount</span>
            <div style="display: flex; align-items: center; gap: 4px;">
              <input type="number" id="pos-discount-pct" value="0" style="width: 44px; background: rgba(0,0,0,0.4); border: 1px solid var(--border-subtle); color: #fff; font-family: var(--font-mono); font-size: 12px; text-align: center; border-radius: 4px;" oninput="updatePOSCalculations()">
              <span style="font-size: 11px;">%</span>
            </div>
          </div>
          <div class="pos-summary-row total">
            <span>Customer Total</span>
            <span id="pos-final-total">₹0</span>
          </div>

          <div class="pos-btn-row">
            <button class="btn-pos-wa" onclick="sendWhatsAppReceipt()">
              <span>💬</span> Send WhatsApp Bill
            </button>
            <button class="btn-pos-clear" onclick="clearCart()">
              Clear Cart
            </button>
          </div>
        </div>
      </section>

    </div>

  </div>

  <!-- DRAWER: ALL 94 ITEMS INVENTORY -->
  <div class="drawer-scrim" id="sheet-inventory" onclick="closeSheet('inventory')">
    <div class="drawer-box" onclick="event.stopPropagation()">
      <div class="drawer-top-bar">
        <h3>Master Inventory (94 Items)</h3>
        <button class="btn-drawer-x" onclick="closeSheet('inventory')">✕</button>
      </div>
      <input type="text" class="drawer-search-bar" id="inventory-search" placeholder="Search by name, sticker #..." oninput="filterInventory(this.value)">
      <div class="drawer-scroll-list" id="inventory-list-container">
        <!-- JS rendered -->
      </div>
    </div>
  </div>

  <!-- DRAWER: FINANCIAL STATS -->
  <div class="drawer-scrim" id="sheet-stats" onclick="closeSheet('stats')">
    <div class="drawer-box" onclick="event.stopPropagation()">
      <div class="drawer-top-bar">
        <h3>Diwali Consignment P&L</h3>
        <button class="btn-drawer-x" onclick="closeSheet('stats')">✕</button>
      </div>
      
      <div style="padding: 6px 0; font-size: 13px;">
        <div style="display: flex; justify-content: space-between; padding: 6px 0; border-bottom: 1px dashed var(--border-subtle)">
          <span style="color: var(--text-2)">Stock Bill (94 items)</span>
          <span style="font-family: var(--font-mono)">₹3,32,518</span>
        </div>
        <div style="display: flex; justify-content: space-between; padding: 6px 0; border-bottom: 1px dashed var(--border-subtle)">
          <span style="color: var(--text-2)">Stock with +10% Buffer</span>
          <span style="font-family: var(--font-mono); color: var(--accent-gold)">₹3,65,770</span>
        </div>
        <div style="display: flex; justify-content: space-between; padding: 6px 0; border-bottom: 1px dashed var(--border-subtle)">
          <span style="color: var(--text-2)">Shed, Auto, Labour & Permissions</span>
          <span style="font-family: var(--font-mono)">₹74,700</span>
        </div>
        <div style="display: flex; justify-content: space-between; padding: 8px 0; font-weight: 800; color: #f87171">
          <span>Total Project Capital</span>
          <span style="font-family: var(--font-mono)">₹4,07,218</span>
        </div>
        <div style="display: flex; justify-content: space-between; padding: 8px 0; border-top: 1px solid var(--border-subtle); font-size: 16px; font-weight: 800; color: #fff">
          <span>Projected Retail Sales</span>
          <span style="font-family: var(--font-mono)" id="stats-total-sales">₹0</span>
        </div>
        <div style="display: flex; justify-content: space-between; padding: 8px 0; font-size: 18px; font-weight: 900; color: var(--accent-lime)">
          <span>Expected Net Profit</span>
          <span style="font-family: var(--font-mono)" id="stats-net-profit">₹0</span>
        </div>
        <div style="margin-top: 10px; font-size: 11px; color: var(--text-3); text-align: center;">
          Wholesaler Paid: ₹2,20,000 • Pending Balance: ₹1,12,518
        </div>
      </div>
    </div>
  </div>

  <!-- DRAWER: CREDITS & CREATORS -->
  <div class="drawer-scrim" id="sheet-credits" onclick="closeSheet('credits')">
    <div class="drawer-box" onclick="event.stopPropagation()">
      <div class="drawer-top-bar">
        <h3>About & Creators</h3>
        <button class="btn-drawer-x" onclick="closeSheet('credits')">✕</button>
      </div>
      
      <div class="credits-card">
        <h4>🚀 Created For</h4>
        <p><strong>Koushik AI Automation</strong><br>Automating retail & seasonal inventory workflows with precision.</p>
      </div>

      <div class="credits-card">
        <h4>📦 Consignment Origin</h4>
        <p><strong>Lakshmi Vasavi Crackers</strong><br>Chinna Pasumarru, Chilakaluripet - 522616<br>Consignment for Nandigama Stall • 94 SKUs (₹3,32,518)</p>
      </div>

      <div class="credits-card">
        <h4>✨ 1-Click Vercel Deploy</h4>
        <p>Configured with <code>vercel.json</code>, PWA <code>manifest.json</code>, and offline Service Worker. Runs anywhere on phone, tablet, and PC.</p>
      </div>
    </div>
  </div>

  <!-- CAMERA SCANNER MODAL -->
  <div class="cam-modal" id="camera-modal">
    <div class="cam-header">
      <span style="font-weight: 800; font-size: 14px; color: var(--accent-lime)">📷 Sticker Camera Scanner</span>
      <button class="btn-drawer-x" onclick="closeCameraScanner()">✕</button>
    </div>
    <div class="cam-video-wrap">
      <video id="cam-stream" autoplay playsinline></video>
      <div class="cam-reticle">
        <span>Align Sticker # Here</span>
      </div>
    </div>
    <div style="padding: 16px; background: rgba(0,0,0,0.85); text-align: center;">
      <p style="font-size: 12px; color: var(--text-2); margin-bottom: 8px;">Point camera at box sticker number or tap number on keypad.</p>
      <button class="btn-tag-main" style="height: 42px;" onclick="closeCameraScanner()">Done / Return to Keypad</button>
    </div>
  </div>

  <script>
    const MASTER_ITEMS = {items_json_str};

    let items = [];
    let currentIndex = 0;
    let typedBuffer = "";
    let bufferTimer = null;
    let voiceMode = 'none'; // 'none', 'en', 'te'
    let cart = []; // POS Customer Cart

    // Web Audio Synthesizer
    const audioCtx = new (window.AudioContext || window.webkitAudioContext)();
    function beep(freq = 600, dur = 0.04) {{
      try {{
        if (audioCtx.state === 'suspended') audioCtx.resume();
        const osc = audioCtx.createOscillator();
        const g = audioCtx.createGain();
        osc.frequency.value = freq;
        osc.connect(g);
        g.connect(audioCtx.destination);
        g.gain.setValueAtTime(0.08, audioCtx.currentTime);
        g.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + dur);
        osc.start();
        osc.stop(audioCtx.currentTime + dur);
      }} catch(e) {{}}
    }}

    function chime() {{
      beep(523.25, 0.08);
      setTimeout(() => beep(659.25, 0.08), 80);
      setTimeout(() => beep(783.99, 0.15), 160);
    }}

    // Init App State
    function init() {{
      const saved = localStorage.getItem('diwali_cracker_items_v3');
      if (saved) {{
        try {{
          items = JSON.parse(saved);
        }} catch(e) {{
          items = JSON.parse(JSON.stringify(MASTER_ITEMS));
        }}
      }} else {{
        items = JSON.parse(JSON.stringify(MASTER_ITEMS));
      }}

      const savedCart = localStorage.getItem('diwali_cart_v3');
      if (savedCart) {{
        try {{ cart = JSON.parse(savedCart); }} catch(e) {{}}
      }}

      const lastIdx = localStorage.getItem('diwali_last_idx_v3');
      if (lastIdx !== null && items[lastIdx]) {{
        currentIndex = parseInt(lastIdx);
      }}

      render();
      updateMetrics();
      renderInventoryList();
      renderPOSCart();

      // Register Service Worker for offline PWA
      if ('serviceWorker' in navigator) {{
        navigator.serviceWorker.register('./sw.js').catch(() => {{}});
      }}

      // Keyboard support
      window.addEventListener('keydown', (e) => {{
        if (e.target.tagName === 'INPUT') return;
        if (e.key >= '0' && e.key <= '9') pressKey(e.key);
        else if (e.key === 'p' || e.key === 'P') pressKey('P');
        else if (e.key === 'Backspace') pressKey('DEL');
        else if (e.key === 'Enter') toggleTagItem();
        else if (e.key === 'ArrowRight') stepItem(1);
        else if (e.key === 'ArrowLeft') stepItem(-1);
      }});
    }}

    function save() {{
      localStorage.setItem('diwali_cracker_items_v3', JSON.stringify(items));
      localStorage.setItem('diwali_last_idx_v3', currentIndex.toString());
      localStorage.setItem('diwali_cart_v3', JSON.stringify(cart));
      updateMetrics();
    }}

    // Numpad Touch Input
    function pressKey(k) {{
      beep(620, 0.03);
      if (navigator.vibrate) navigator.vibrate(15);

      if (k === 'DEL') {{
        typedBuffer = "";
        return;
      }}

      typedBuffer += k;
      clearTimeout(bufferTimer);

      const q = typedBuffer.toLowerCase();
      const matchIdx = items.findIndex(i => i.sticker_no.toLowerCase() === q);

      if (matchIdx !== -1) {{
        currentIndex = matchIdx;
        render();
        bufferTimer = setTimeout(() => {{ typedBuffer = ""; }}, 1200);
      }} else {{
        bufferTimer = setTimeout(() => {{ typedBuffer = ""; }}, 1800);
      }}
    }}

    // Render Active Card
    function render() {{
      const item = items[currentIndex];
      if (!item) return;

      const numEl = document.getElementById('card-num');
      const tagEl = document.getElementById('card-tag-badge');
      const srcEl = document.getElementById('card-src');
      const sourceBadge = document.getElementById('active-source-badge');

      numEl.textContent = '#' + item.sticker_no;
      if (item.bill_type === 'pink') {{
        tagEl.classList.add('pink-tag');
        srcEl.textContent = 'PINK SLIP';
        sourceBadge.textContent = 'Pink Bill (Chinna Pasumarru)';
      }} else {{
        tagEl.classList.remove('pink-tag');
        srcEl.textContent = 'WHITE BILL';
        sourceBadge.textContent = 'White Bill #1–74 (Nandigama)';
      }}

      document.getElementById('card-name').textContent = item.name;
      document.getElementById('card-qty').textContent = item.units + ' Units';
      document.getElementById('card-rem').textContent = (item.remaining_units !== undefined ? item.remaining_units : item.units);
      document.getElementById('card-pack').textContent = 'Pack: ' + item.pack_details;

      document.getElementById('card-rate').textContent = '₹' + item.rate;
      document.getElementById('card-cost10').textContent = '₹' + Math.round(item.rate_plus_10);
      document.getElementById('card-total-box').textContent = '₹' + Math.round(item.units * item.rate_plus_10).toLocaleString('en-IN');

      const spInput = document.getElementById('card-sp');
      spInput.value = item.selling_price;
      updateProfitBadge();

      // Verification Status
      const card = document.getElementById('scanner-box-card');
      const pill = document.getElementById('card-status-pill');
      const symbol = document.getElementById('status-symbol');
      const title = document.getElementById('status-title');
      const tagBtn = document.getElementById('btn-tag-action');
      const tagText = document.getElementById('btn-tag-text');

      if (item.verified) {{
        card.classList.add('is-verified');
        pill.className = 'status-pill verified';
        symbol.textContent = '✓';
        title.textContent = 'Tagged';
        tagBtn.className = 'btn-tag-main is-verified';
        tagText.textContent = 'TAGGED (TAP TO UNMARK)';
      }} else {{
        card.classList.remove('is-verified');
        pill.className = 'status-pill';
        symbol.textContent = '⚪';
        title.textContent = 'Pending';
        tagBtn.className = 'btn-tag-main';
        tagText.textContent = 'MARK TAGGED & NEXT';
      }}

      if (voiceMode !== 'none') {{
        speakItem(item);
      }}
    }}

    function updateProfitBadge() {{
      const item = items[currentIndex];
      const sp = parseFloat(document.getElementById('card-sp').value) || 0;
      item.selling_price = sp;
      const profit = sp - item.rate_plus_10;
      const margin = item.rate_plus_10 > 0 ? ((profit / item.rate_plus_10) * 100).toFixed(0) : 0;
      const boxProfit = profit * item.units;

      const badge = document.getElementById('card-profit-lbl');
      badge.textContent = `+₹${{Math.round(profit)}} / unit (+${{margin}}%) • Box: +₹${{Math.round(boxProfit).toLocaleString('en-IN')}}`;
      badge.style.color = profit >= 0 ? '#34d399' : '#f87171';
    }}

    function onPriceChange(val) {{
      items[currentIndex].selling_price = parseFloat(val) || 0;
      updateProfitBadge();
      save();
    }}

    function applyMargin(m) {{
      beep(700, 0.04);
      const item = items[currentIndex];
      const raw = item.rate_plus_10 * (1 + m);
      let rounded = Math.ceil(raw / 10) * 10;
      if (raw <= 35) rounded = Math.ceil(raw / 5) * 5;
      item.selling_price = rounded;
      document.getElementById('card-sp').value = rounded;
      updateProfitBadge();
      save();
    }}

    // Tag Box Toggle
    function toggleTagItem() {{
      const item = items[currentIndex];
      item.verified = !item.verified;

      if (item.verified) {{
        chime();
        if (navigator.vibrate) navigator.vibrate([25, 45, 65]);
      }} else {{
        beep(350, 0.08);
      }}

      save();
      render();
      renderInventoryList();

      if (item.verified) {{
        setTimeout(() => {{
          typedBuffer = "";
          stepItem(1);
        }}, 400);
      }}
    }}

    function stepItem(dir) {{
      beep(500, 0.03);
      typedBuffer = "";
      let next = currentIndex + dir;
      if (next < 0) next = items.length - 1;
      if (next >= items.length) next = 0;
      currentIndex = next;
      render();
    }}

    // Global Metrics Calculation
    function updateMetrics() {{
      const tagged = items.filter(i => i.verified).length;
      const total = items.length;
      const pct = Math.round((tagged / total) * 100);

      document.getElementById('progress-text').textContent = `${{tagged}} / ${{total}} Tagged`;
      document.getElementById('progress-fill').style.width = pct + '%';
      document.getElementById('progress-pct').textContent = pct + '%';

      let totalSales = 0;
      items.forEach(i => {{
        totalSales += (i.selling_price || 0) * i.units;
      }});
      const netProfit = totalSales - 407218;

      document.getElementById('stats-total-sales').textContent = '₹' + Math.round(totalSales).toLocaleString('en-IN');
      document.getElementById('stats-net-profit').textContent = '₹' + Math.round(netProfit).toLocaleString('en-IN');

      // Update cart count
      const cartCount = cart.reduce((acc, c) => acc + c.qty, 0);
      document.getElementById('cart-item-count').textContent = cartCount;
    }}

    // View Switching (Scanner vs POS)
    function switchMainView(view) {{
      beep(550, 0.03);
      const vScan = document.getElementById('view-scanner');
      const vPOS = document.getElementById('view-pos');
      const tabScan = document.getElementById('tab-nav-scan');
      const tabPOS = document.getElementById('tab-nav-pos');

      if (view === 'scanner') {{
        vScan.style.display = 'flex';
        vPOS.style.display = 'none';
        tabScan.classList.add('active');
        tabPOS.classList.remove('active');
      }} else {{
        vScan.style.display = 'none';
        vPOS.style.display = 'flex';
        tabScan.classList.remove('active');
        tabPOS.classList.add('active');
        renderPOSCart();
      }}
    }}

    // POS CART & BILLING ENGINE
    function addToCartCurrent() {{
      const item = items[currentIndex];
      addToCart(item);
    }}

    function addToCart(item) {{
      chime();
      const existing = cart.find(c => c.id === item.id);
      if (existing) {{
        existing.qty += 1;
      }} else {{
        cart.push({{
          id: item.id,
          sticker_no: item.sticker_no,
          name: item.name,
          price: item.selling_price,
          qty: 1
        }});
      }}
      save();
      updateMetrics();
      renderPOSCart();
    }}

    function updateCartQty(idx, delta) {{
      beep(500, 0.03);
      cart[idx].qty += delta;
      if (cart[idx].qty <= 0) {{
        cart.splice(idx, 1);
      }}
      save();
      updateMetrics();
      renderPOSCart();
    }}

    function clearCart() {{
      if (cart.length === 0) return;
      if (confirm("Clear customer cart?")) {{
        cart = [];
        save();
        updateMetrics();
        renderPOSCart();
      }}
    }}

    function renderPOSCart() {{
      const container = document.getElementById('pos-cart-items-container');
      const countLabel = document.getElementById('pos-items-label');

      if (cart.length === 0) {{
        container.innerHTML = `
          <div style="text-align: center; color: var(--text-3); font-size: 13px; margin-top: 40px;">
            Cart is empty.<br>Tap <span style="color: var(--accent-cyan); font-weight: 700;">+🛒</span> on any box in Scanner to add!
          </div>
        `;
        countLabel.textContent = "0 items";
        document.getElementById('pos-subtotal').textContent = "₹0";
        document.getElementById('pos-final-total').textContent = "₹0";
        return;
      }}

      countLabel.textContent = `${{cart.length}} line items`;
      container.innerHTML = "";

      cart.forEach((c, idx) => {{
        const row = document.createElement('div');
        row.className = 'pos-cart-item';
        row.innerHTML = `
          <div class="pos-item-info">
            <div><strong>#${{c.sticker_no}} ${{c.name}}</strong></div>
            <span>₹${{c.price}} each</span>
          </div>
          <div class="pos-qty-controls">
            <button class="qty-btn" onclick="updateCartQty(${{idx}}, -1)">-</button>
            <span class="qty-val">${{c.qty}}</span>
            <button class="qty-btn" onclick="updateCartQty(${{idx}}, 1)">+</button>
            <span style="font-family: var(--font-mono); font-weight: 800; margin-left: 6px; width: 60px; text-align: right;">
              ₹${{c.price * c.qty}}
            </span>
          </div>
        `;
        container.appendChild(row);
      }});

      updatePOSCalculations();
    }}

    function updatePOSCalculations() {{
      const subtotal = cart.reduce((acc, c) => acc + (c.price * c.qty), 0);
      const discountPct = parseFloat(document.getElementById('pos-discount-pct').value) || 0;
      const discountAmt = Math.round(subtotal * (discountPct / 100));
      const finalTotal = subtotal - discountAmt;

      document.getElementById('pos-subtotal').textContent = '₹' + subtotal.toLocaleString('en-IN');
      document.getElementById('pos-final-total').textContent = '₹' + finalTotal.toLocaleString('en-IN');
    }}

    function sendWhatsAppReceipt() {{
      if (cart.length === 0) {{
        alert("Cart is empty! Add items first.");
        return;
      }}

      const subtotal = cart.reduce((acc, c) => acc + (c.price * c.qty), 0);
      const discountPct = parseFloat(document.getElementById('pos-discount-pct').value) || 0;
      const discountAmt = Math.round(subtotal * (discountPct / 100));
      const finalTotal = subtotal - discountAmt;

      let msg = "🎆 *DIWALI CRACKERS BILL*\\n";
      msg += "📍 Nandigama Fireworks Stall\\n";
      msg += "-------------------------------\\n";
      cart.forEach((c, i) => {{
        msg += `${{i+1}}. *${{c.name}}* x ${{c.qty}} = ₹${{c.price * c.qty}}\\n`;
      }});
      msg += "-------------------------------\\n";
      msg += `Subtotal: ₹${{subtotal}}\\n`;
      if (discountPct > 0) {{
        msg += `Discount (${{discountPct}}%): -₹${{discountAmt}}\\n`;
      }}
      msg += `*FINAL AMOUNT: ₹${{finalTotal}}*\\n`;
      msg += "-------------------------------\\n";
      msg += "Wishing you a Happy & Safe Diwali! 🪔✨";

      const waUrl = "https://api.whatsapp.com/send?text=" + encodeURIComponent(msg);
      window.open(waUrl, '_blank');
    }}

    // Bilingual Voice Engine
    function toggleVoice() {{
      const pill = document.getElementById('btn-voice-pill');
      if (voiceMode === 'none') {{
        voiceMode = 'en';
        pill.classList.add('active');
        pill.innerHTML = '<span id="voice-icon">🔊</span> En';
        speak('Voice English active');
      }} else if (voiceMode === 'en') {{
        voiceMode = 'te';
        pill.classList.add('active');
        pill.innerHTML = '<span id="voice-icon">🔊</span> Te';
        speak('బాక్స్ వాయిస్ ఆన్ చేయబడింది');
      }} else {{
        voiceMode = 'none';
        pill.classList.remove('active');
        pill.innerHTML = '<span id="voice-icon">🔈</span> Off';
      }}
      chime();
    }}

    function speakItem(item) {{
      if (voiceMode === 'en') {{
        speak(`Box ${{item.sticker_no}}, ${{item.name}}, Cost ${{Math.round(item.rate_plus_10)}}, Sell ${{item.selling_price}}`);
      }} else if (voiceMode === 'te') {{
        speak(`బాక్స్ ${{item.sticker_no}}, ${{item.name}}, రేటు ${{item.selling_price}} రూపాయలు`);
      }}
    }}

    function speak(text) {{
      if (!('speechSynthesis' in window)) return;
      window.speechSynthesis.cancel();
      const u = new SpeechSynthesisUtterance(text);
      u.rate = 1.1;
      window.speechSynthesis.speak(u);
    }}

    // Camera Scanner
    let streamRef = null;
    function openCameraScanner() {{
      const modal = document.getElementById('camera-modal');
      modal.classList.add('open');
      navigator.mediaDevices.getUserMedia({{ video: {{ facingMode: 'environment' }} }})
        .then(stream => {{
          streamRef = stream;
          document.getElementById('cam-stream').srcObject = stream;
        }})
        .catch(err => {{
          alert("Camera access unavailable. Use the on-screen keypad!");
          closeCameraScanner();
        }});
    }}

    function closeCameraScanner() {{
      document.getElementById('camera-modal').classList.remove('open');
      if (streamRef) {{
        streamRef.getTracks().forEach(t => t.stop());
        streamRef = null;
      }}
    }}

    // Sheets / Drawers
    function openSheet(id) {{
      beep(600, 0.03);
      document.getElementById('sheet-' + id).classList.add('open');
    }}

    function closeSheet(id) {{
      document.getElementById('sheet-' + id).classList.remove('open');
    }}

    function renderInventoryList(filter = "") {{
      const container = document.getElementById('inventory-list-container');
      container.innerHTML = "";
      const term = filter.toLowerCase();

      items.forEach((item, idx) => {{
        if (term && !item.name.toLowerCase().includes(term) && !item.sticker_no.toLowerCase().includes(term)) {{
          return;
        }}

        const row = document.createElement('div');
        row.className = `drawer-list-item ${{item.verified ? 'is-verified' : ''}}`;
        row.innerHTML = `
          <div>
            <div style="font-weight: 700; font-size: 13px;">
              <span style="color: ${{item.bill_type==='pink'?'#fb7185':'#fbbf24'}}; font-family: var(--font-mono); font-weight: 800;">#${{item.sticker_no}}</span>
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
          closeSheet('inventory');
          switchMainView('scanner');
        }};
        container.appendChild(row);
      }});
    }}

    function filterInventory(val) {{
      renderInventoryList(val);
    }}

    window.addEventListener('DOMContentLoaded', init);
  </script>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_code)

print("Comprehensive Vercel-ready mobile app index.html built successfully!")
