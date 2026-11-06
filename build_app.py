import json

with open("items_data.json", "r", encoding="utf-8") as f:
    items = json.load(f)

items_json_str = json.dumps(items)

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>Diwali Crackers Smart Pricing & Box Verifier</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;600;700&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg-primary: #0a0e17;
      --bg-secondary: #121826;
      --bg-card: #182234;
      --bg-card-hover: #1f2b42;
      --border-color: #27354f;
      --accent-gold: #f59e0b;
      --accent-gold-light: #fbbf24;
      --accent-fire: #ef4444;
      --accent-orange: #f97316;
      --accent-green: #10b981;
      --accent-blue: #3b82f6;
      --accent-purple: #8b5cf6;
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
      --text-dim: #64748b;
      --radius-sm: 8px;
      --radius-md: 12px;
      --radius-lg: 18px;
      --radius-xl: 24px;
      --shadow-sm: 0 2px 8px rgba(0,0,0,0.3);
      --shadow-md: 0 6px 20px rgba(0,0,0,0.4);
      --shadow-glow: 0 0 25px rgba(245, 158, 11, 0.25);
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      -webkit-tap-highlight-color: transparent;
    }

    body {
      font-family: 'Outfit', sans-serif;
      background-color: var(--bg-primary);
      color: var(--text-main);
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      overflow-x: hidden;
      line-height: 1.5;
    }

    /* Header & Navigation */
    header {
      background: linear-gradient(135deg, #101624 0%, #172033 100%);
      border-bottom: 1px solid var(--border-color);
      position: sticky;
      top: 0;
      z-index: 50;
      backdrop-filter: blur(12px);
    }

    .header-top {
      max-width: 1400px;
      margin: 0 auto;
      padding: 12px 18px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 16px;
    }

    .brand-wrap {
      display: flex;
      align-items: center;
      gap: 12px;
    }

    .brand-icon {
      font-size: 28px;
      background: linear-gradient(135deg, #f59e0b, #ef4444);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      animation: pulseGlow 2s infinite alternate;
    }

    @keyframes pulseGlow {
      from { transform: scale(1); filter: drop-shadow(0 0 4px rgba(245, 158, 11, 0.4)); }
      to { transform: scale(1.08); filter: drop-shadow(0 0 10px rgba(239, 68, 68, 0.7)); }
    }

    .brand-text h1 {
      font-size: 1.25rem;
      font-weight: 800;
      letter-spacing: -0.02em;
      background: linear-gradient(to right, #ffffff, #fef08a);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    .brand-text p {
      font-size: 0.75rem;
      color: var(--accent-gold);
      font-weight: 600;
      letter-spacing: 0.04em;
      text-transform: uppercase;
    }

    /* Live Summary Badges in Header */
    .header-metrics {
      display: flex;
      align-items: center;
      gap: 10px;
      flex-wrap: wrap;
    }

    .metric-pill {
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      padding: 5px 12px;
      border-radius: var(--radius-md);
      font-size: 0.78rem;
      display: flex;
      flex-direction: column;
      align-items: flex-end;
    }

    .metric-pill .label {
      color: var(--text-dim);
      font-size: 0.68rem;
      text-transform: uppercase;
      font-weight: 600;
    }

    .metric-pill .value {
      color: var(--text-main);
      font-weight: 700;
      font-family: 'JetBrains Mono', monospace;
    }

    .metric-pill.highlight {
      border-color: var(--accent-gold);
      background: rgba(245, 158, 11, 0.08);
    }
    .metric-pill.highlight .value {
      color: var(--accent-gold-light);
    }

    .metric-pill.green {
      border-color: var(--accent-green);
      background: rgba(16, 185, 129, 0.08);
    }
    .metric-pill.green .value {
      color: var(--accent-green);
    }

    /* Tabs Bar */
    .tabs-bar {
      max-width: 1400px;
      margin: 0 auto;
      padding: 0 18px;
      display: flex;
      gap: 6px;
      overflow-x: auto;
      scrollbar-width: none;
    }
    .tabs-bar::-webkit-scrollbar {
      display: none;
    }

    .nav-tab {
      padding: 10px 18px;
      background: transparent;
      border: none;
      border-bottom: 3px solid transparent;
      color: var(--text-muted);
      font-size: 0.88rem;
      font-weight: 600;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 8px;
      white-space: nowrap;
      transition: all 0.2s ease;
    }

    .nav-tab:hover {
      color: var(--text-main);
    }

    .nav-tab.active {
      color: var(--accent-gold);
      border-bottom-color: var(--accent-gold);
      background: rgba(245, 158, 11, 0.05);
    }

    /* Main Container */
    main {
      flex: 1;
      max-width: 1400px;
      width: 100%;
      margin: 0 auto;
      padding: 20px 18px;
    }

    .tab-content {
      display: none;
      animation: fadeIn 0.25s ease;
    }

    .tab-content.active {
      display: block;
    }

    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(6px); }
      to { opacity: 1; transform: translateY(0); }
    }

    /* FAST VERIFIER HERO LAYOUT */
    .verifier-grid {
      display: grid;
      grid-template-columns: 360px 1fr;
      gap: 24px;
      align-items: start;
    }

    @media (max-width: 900px) {
      .verifier-grid {
        grid-template-columns: 1fr;
      }
    }

    /* Search & Keypad Panel */
    .keypad-panel {
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-xl);
      padding: 20px;
      box-shadow: var(--shadow-md);
    }

    .search-box-wrap {
      margin-bottom: 16px;
      position: relative;
    }

    .search-box-wrap label {
      display: block;
      font-size: 0.78rem;
      text-transform: uppercase;
      font-weight: 700;
      color: var(--accent-gold);
      margin-bottom: 6px;
      letter-spacing: 0.05em;
    }

    .search-input-wrap {
      display: flex;
      align-items: center;
      background: var(--bg-secondary);
      border: 2px solid var(--border-color);
      border-radius: var(--radius-lg);
      padding: 6px 14px;
      transition: border-color 0.2s;
    }

    .search-input-wrap:focus-within {
      border-color: var(--accent-gold);
      box-shadow: var(--shadow-glow);
    }

    .search-input-wrap input {
      width: 100%;
      background: transparent;
      border: none;
      color: #fff;
      font-size: 1.5rem;
      font-weight: 700;
      font-family: 'JetBrains Mono', monospace;
      outline: none;
    }

    .search-input-wrap input::placeholder {
      font-size: 1rem;
      color: var(--text-dim);
      font-weight: 400;
      font-family: 'Outfit', sans-serif;
    }

    .clear-btn {
      background: transparent;
      border: none;
      color: var(--text-dim);
      font-size: 1.2rem;
      cursor: pointer;
      padding: 4px 8px;
    }
    .clear-btn:hover {
      color: var(--text-main);
    }

    /* Touch Numpad */
    .numpad {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 10px;
      margin-top: 14px;
    }

    .num-key {
      background: var(--bg-secondary);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-md);
      color: var(--text-main);
      font-size: 1.5rem;
      font-weight: 700;
      font-family: 'JetBrains Mono', monospace;
      padding: 14px 0;
      cursor: pointer;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      user-select: none;
      transition: all 0.15s ease;
      touch-action: manipulation;
    }

    .num-key:active {
      transform: scale(0.95);
      background: var(--accent-gold);
      color: #000;
    }

    .num-key.p-key {
      color: #ec4899;
      font-size: 1.15rem;
      font-weight: 800;
    }

    .num-key.action-key {
      color: var(--accent-orange);
      font-size: 1.1rem;
    }

    .num-key.zero-key {
      font-size: 1.5rem;
    }

    .key-hint {
      font-size: 0.65rem;
      color: var(--text-dim);
      font-family: 'Outfit', sans-serif;
      font-weight: 500;
    }

    /* Quick Shortcuts below Keypad */
    .quick-list-section {
      margin-top: 18px;
      border-top: 1px solid var(--border-color);
      padding-top: 14px;
    }

    .quick-title {
      font-size: 0.75rem;
      font-weight: 700;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.04em;
      margin-bottom: 8px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    .recent-chips {
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
      max-height: 120px;
      overflow-y: auto;
    }

    .recent-chip {
      background: var(--bg-secondary);
      border: 1px solid var(--border-color);
      padding: 5px 10px;
      border-radius: var(--radius-sm);
      font-size: 0.78rem;
      font-family: 'JetBrains Mono', monospace;
      cursor: pointer;
      color: var(--text-muted);
      display: flex;
      align-items: center;
      gap: 5px;
    }
    .recent-chip:hover {
      border-color: var(--accent-gold);
      color: var(--text-main);
    }
    .recent-chip.verified {
      border-color: var(--accent-green);
      color: var(--accent-green);
    }

    /* Item Card Details (Right Column) */
    .card-display-panel {
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-xl);
      padding: 24px;
      box-shadow: var(--shadow-md);
      position: relative;
      overflow: hidden;
    }

    .card-display-panel.verified-glow {
      border-color: var(--accent-green);
      box-shadow: 0 0 30px rgba(16, 185, 129, 0.2);
    }

    .card-header-bar {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      gap: 16px;
      border-bottom: 1px solid var(--border-color);
      padding-bottom: 18px;
      margin-bottom: 20px;
      flex-wrap: wrap;
    }

    .badge-group {
      display: flex;
      align-items: center;
      gap: 8px;
      flex-wrap: wrap;
    }

    .sticker-badge {
      background: linear-gradient(135deg, #f59e0b, #d97706);
      color: #000;
      font-weight: 900;
      font-size: 1.4rem;
      font-family: 'JetBrains Mono', monospace;
      padding: 6px 18px;
      border-radius: var(--radius-md);
      box-shadow: 0 4px 12px rgba(245, 158, 11, 0.35);
      letter-spacing: -0.02em;
    }

    .sticker-badge.pink-badge {
      background: linear-gradient(135deg, #ec4899, #be185d);
      color: #fff;
      box-shadow: 0 4px 12px rgba(236, 72, 153, 0.35);
    }

    .source-tag {
      background: var(--bg-secondary);
      border: 1px solid var(--border-color);
      padding: 4px 10px;
      border-radius: var(--radius-sm);
      font-size: 0.75rem;
      color: var(--text-muted);
      font-weight: 600;
    }

    .verification-status-pill {
      display: flex;
      align-items: center;
      gap: 6px;
      padding: 6px 14px;
      border-radius: var(--radius-lg);
      font-size: 0.82rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    .verification-status-pill.unverified {
      background: rgba(239, 68, 68, 0.12);
      border: 1px solid rgba(239, 68, 68, 0.4);
      color: #fca5a5;
    }

    .verification-status-pill.verified {
      background: rgba(16, 185, 129, 0.15);
      border: 1px solid rgba(16, 185, 129, 0.5);
      color: #6ee7b7;
    }

    .item-title-section {
      margin-bottom: 22px;
    }

    .item-title-section h2 {
      font-size: 2.2rem;
      font-weight: 800;
      color: #ffffff;
      line-height: 1.2;
      margin-bottom: 6px;
      letter-spacing: -0.01em;
    }

    .item-pack-info {
      font-size: 1rem;
      color: var(--accent-gold);
      font-weight: 600;
      display: flex;
      align-items: center;
      gap: 8px;
    }

    /* Price Comparison Stats Grid */
    .rates-overview-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
      gap: 14px;
      margin-bottom: 24px;
    }

    .rate-stat-card {
      background: var(--bg-secondary);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-lg);
      padding: 16px;
      position: relative;
      transition: all 0.2s ease;
    }

    .rate-stat-card .stat-label {
      font-size: 0.75rem;
      font-weight: 600;
      color: var(--text-dim);
      text-transform: uppercase;
      letter-spacing: 0.04em;
      margin-bottom: 6px;
    }

    .rate-stat-card .stat-val {
      font-size: 1.6rem;
      font-weight: 800;
      font-family: 'JetBrains Mono', monospace;
      color: var(--text-main);
    }

    .rate-stat-card.wholesale-card .stat-val {
      color: #93c5fd;
    }

    .rate-stat-card.overhead-card {
      border-color: rgba(245, 158, 11, 0.4);
      background: linear-gradient(135deg, rgba(245, 158, 11, 0.05) 0%, rgba(24, 34, 52, 0.9) 100%);
    }

    .rate-stat-card.overhead-card .stat-val {
      color: var(--accent-gold-light);
    }

    .rate-stat-card.units-card .stat-val {
      color: #a78bfa;
    }

    .rate-stat-card .stat-sub {
      font-size: 0.72rem;
      color: var(--text-dim);
      margin-top: 4px;
    }

    /* SELLING PRICE INTERACTIVE CONTROLS */
    .selling-control-section {
      background: linear-gradient(135deg, #19273c 0%, #152033 100%);
      border: 2px solid var(--accent-gold);
      border-radius: var(--radius-xl);
      padding: 22px;
      margin-bottom: 24px;
      box-shadow: 0 8px 30px rgba(0, 0, 0, 0.35);
    }

    .selling-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 14px;
      flex-wrap: wrap;
      gap: 10px;
    }

    .selling-header h3 {
      font-size: 1.1rem;
      font-weight: 800;
      color: var(--accent-gold-light);
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .margin-badge {
      background: var(--accent-green);
      color: #064e3b;
      font-weight: 800;
      font-size: 0.82rem;
      padding: 3px 10px;
      border-radius: var(--radius-sm);
      font-family: 'JetBrains Mono', monospace;
    }

    .selling-input-row {
      display: flex;
      gap: 14px;
      align-items: center;
      flex-wrap: wrap;
    }

    .sp-input-wrap {
      flex: 1;
      min-width: 220px;
      display: flex;
      align-items: center;
      background: #0d1523;
      border: 2px solid #334b74;
      border-radius: var(--radius-lg);
      padding: 8px 16px;
    }

    .sp-input-wrap:focus-within {
      border-color: var(--accent-gold-light);
      box-shadow: var(--shadow-glow);
    }

    .currency-symbol {
      font-size: 1.8rem;
      font-weight: 800;
      color: var(--accent-gold);
      margin-right: 8px;
    }

    .sp-input-wrap input {
      width: 100%;
      background: transparent;
      border: none;
      color: #fff;
      font-size: 2.2rem;
      font-weight: 800;
      font-family: 'JetBrains Mono', monospace;
      outline: none;
    }

    .margin-buttons-row {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin-top: 14px;
      align-items: center;
    }

    .margin-btn-label {
      font-size: 0.72rem;
      text-transform: uppercase;
      font-weight: 700;
      color: var(--text-dim);
    }

    .margin-btn {
      background: var(--bg-secondary);
      border: 1px solid var(--border-color);
      color: var(--text-main);
      padding: 6px 12px;
      border-radius: var(--radius-md);
      font-size: 0.8rem;
      font-weight: 700;
      font-family: 'JetBrains Mono', monospace;
      cursor: pointer;
      transition: all 0.15s ease;
    }

    .margin-btn:hover {
      border-color: var(--accent-gold);
      background: var(--bg-card-hover);
    }

    .margin-btn.active {
      background: var(--accent-gold);
      color: #000;
      border-color: var(--accent-gold);
    }

    /* Profit calculations bar */
    .profit-metrics-bar {
      margin-top: 16px;
      padding-top: 14px;
      border-top: 1px solid rgba(255,255,255,0.1);
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
      gap: 12px;
    }

    .profit-sub-item .title {
      font-size: 0.68rem;
      text-transform: uppercase;
      font-weight: 600;
      color: var(--text-dim);
    }

    .profit-sub-item .val {
      font-size: 1.15rem;
      font-weight: 700;
      font-family: 'JetBrains Mono', monospace;
      color: #fff;
    }

    .profit-sub-item .val.green {
      color: #34d399;
    }

    /* Big Action Buttons Row */
    .action-cta-row {
      display: flex;
      gap: 12px;
      margin-top: 24px;
      flex-wrap: wrap;
    }

    .btn-verify-main {
      flex: 2;
      min-width: 240px;
      background: linear-gradient(135deg, #059669 0%, #10b981 100%);
      border: none;
      color: #ffffff;
      padding: 16px 24px;
      border-radius: var(--radius-xl);
      font-size: 1.15rem;
      font-weight: 800;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 10px;
      box-shadow: 0 8px 24px rgba(16, 185, 129, 0.35);
      transition: all 0.2s ease;
    }

    .btn-verify-main:hover {
      transform: translateY(-2px);
      box-shadow: 0 12px 28px rgba(16, 185, 129, 0.45);
    }

    .btn-verify-main:active {
      transform: translateY(1px);
    }

    .btn-verify-main.is-verified {
      background: linear-gradient(135deg, #1e293b 0%, #334155 100%);
      border: 1px solid #475569;
      color: #94a3b8;
      box-shadow: none;
    }

    .btn-nav-step {
      flex: 1;
      min-width: 100px;
      background: var(--bg-secondary);
      border: 1px solid var(--border-color);
      color: var(--text-main);
      padding: 14px 18px;
      border-radius: var(--radius-xl);
      font-size: 0.95rem;
      font-weight: 700;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      transition: all 0.15s ease;
    }

    .btn-nav-step:hover {
      border-color: var(--accent-gold);
      background: var(--bg-card-hover);
    }

    .btn-voice-toggle {
      background: var(--bg-secondary);
      border: 1px solid var(--border-color);
      color: var(--text-muted);
      padding: 14px;
      border-radius: var(--radius-xl);
      font-size: 1.2rem;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: all 0.2s;
    }

    .btn-voice-toggle.voice-active {
      background: rgba(245, 158, 11, 0.15);
      border-color: var(--accent-gold);
      color: var(--accent-gold);
    }

    /* MASTER TABLE STYLES */
    .table-controls-bar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 14px;
      margin-bottom: 16px;
      flex-wrap: wrap;
    }

    .table-filter-group {
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
    }

    .filter-btn {
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      color: var(--text-muted);
      padding: 7px 14px;
      border-radius: var(--radius-md);
      font-size: 0.82rem;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.15s;
    }

    .filter-btn.active {
      background: var(--accent-gold);
      color: #000;
      border-color: var(--accent-gold);
      font-weight: 700;
    }

    .table-search-input {
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-md);
      padding: 8px 14px;
      color: #fff;
      font-size: 0.9rem;
      outline: none;
      min-width: 250px;
    }

    .table-search-input:focus {
      border-color: var(--accent-gold);
    }

    .bulk-tools-panel {
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-lg);
      padding: 14px 18px;
      margin-bottom: 18px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 14px;
      flex-wrap: wrap;
    }

    .bulk-tools-left {
      display: flex;
      align-items: center;
      gap: 10px;
      flex-wrap: wrap;
    }

    .bulk-label {
      font-size: 0.8rem;
      font-weight: 700;
      color: var(--accent-gold);
      text-transform: uppercase;
    }

    .btn-bulk-action {
      background: var(--bg-secondary);
      border: 1px solid var(--border-color);
      color: var(--text-main);
      padding: 6px 12px;
      border-radius: var(--radius-sm);
      font-size: 0.78rem;
      font-weight: 600;
      cursor: pointer;
    }

    .btn-bulk-action:hover {
      border-color: var(--accent-gold);
      background: var(--bg-card-hover);
    }

    .table-responsive {
      overflow-x: auto;
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-lg);
      box-shadow: var(--shadow-sm);
    }

    table.master-table {
      width: 100%;
      border-collapse: collapse;
      font-size: 0.85rem;
      text-align: left;
      white-space: nowrap;
    }

    table.master-table th {
      background: #111827;
      color: var(--text-muted);
      font-weight: 700;
      text-transform: uppercase;
      font-size: 0.72rem;
      letter-spacing: 0.04em;
      padding: 12px 14px;
      border-bottom: 2px solid var(--border-color);
      position: sticky;
      top: 0;
      z-index: 10;
    }

    table.master-table td {
      padding: 10px 14px;
      border-bottom: 1px solid #1f293d;
      color: var(--text-main);
    }

    table.master-table tr:hover {
      background: rgba(245, 158, 11, 0.04);
    }

    table.master-table tr.row-verified {
      background: rgba(16, 185, 129, 0.03);
    }

    .table-sticker-badge {
      display: inline-block;
      font-weight: 800;
      font-family: 'JetBrains Mono', monospace;
      padding: 3px 8px;
      border-radius: 6px;
      font-size: 0.8rem;
    }

    .badge-w {
      background: rgba(245, 158, 11, 0.15);
      color: #fbbf24;
      border: 1px solid rgba(245, 158, 11, 0.3);
    }

    .badge-p {
      background: rgba(236, 72, 153, 0.15);
      color: #f472b6;
      border: 1px solid rgba(236, 72, 153, 0.3);
    }

    .table-sp-input {
      width: 90px;
      background: #0d1523;
      border: 1px solid var(--border-color);
      border-radius: 6px;
      padding: 4px 8px;
      color: #fff;
      font-weight: 700;
      font-family: 'JetBrains Mono', monospace;
      text-align: right;
    }

    .table-sp-input:focus {
      border-color: var(--accent-gold);
      outline: none;
    }

    /* ANALYTICS TAB STYLES */
    .analytics-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
      gap: 20px;
      margin-bottom: 24px;
    }

    .analytics-card {
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-xl);
      padding: 22px;
      box-shadow: var(--shadow-sm);
    }

    .analytics-card h3 {
      font-size: 1.1rem;
      font-weight: 700;
      color: var(--text-main);
      margin-bottom: 16px;
      display: flex;
      align-items: center;
      gap: 8px;
      border-bottom: 1px solid var(--border-color);
      padding-bottom: 12px;
    }

    .expense-list {
      display: flex;
      flex-direction: column;
      gap: 10px;
    }

    .expense-row {
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 0.88rem;
      padding: 6px 0;
      border-bottom: 1px dashed rgba(255,255,255,0.06);
    }

    .expense-row.total-row {
      border-top: 2px solid var(--border-color);
      border-bottom: none;
      padding-top: 10px;
      font-weight: 800;
      font-size: 1rem;
      color: var(--accent-gold-light);
    }

    .mono-amount {
      font-family: 'JetBrains Mono', monospace;
      font-weight: 700;
    }

    /* PRINTABLE LABELS VIEW */
    .printable-sheet {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
      gap: 14px;
      margin-top: 16px;
    }

    .print-label-card {
      background: #ffffff;
      color: #000000;
      border: 2px solid #000000;
      border-radius: 8px;
      padding: 12px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      min-height: 140px;
      position: relative;
    }

    .label-card-top {
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 2px solid #000;
      padding-bottom: 4px;
      margin-bottom: 6px;
    }

    .label-sticker-num {
      font-size: 1.6rem;
      font-weight: 900;
      font-family: 'JetBrains Mono', monospace;
    }

    .label-units {
      font-size: 0.75rem;
      font-weight: 700;
      text-transform: uppercase;
    }

    .label-product-name {
      font-size: 1rem;
      font-weight: 800;
      line-height: 1.2;
      margin-bottom: 8px;
    }

    .label-price-block {
      background: #000;
      color: #fff;
      padding: 6px 8px;
      border-radius: 4px;
      text-align: center;
      font-weight: 900;
      font-size: 1.3rem;
      font-family: 'JetBrains Mono', monospace;
    }

    /* BILLS GALLERY */
    .gallery-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
      gap: 20px;
    }

    .bill-card {
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-lg);
      overflow: hidden;
      display: flex;
      flex-direction: column;
    }

    .bill-card-img-wrap {
      height: 380px;
      background: #0d121c;
      overflow: hidden;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: zoom-in;
    }

    .bill-card-img-wrap img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: transform 0.3s;
    }

    .bill-card-img-wrap:hover img {
      transform: scale(1.05);
    }

    .bill-card-info {
      padding: 14px 16px;
    }

    .bill-card-info h4 {
      font-size: 1rem;
      font-weight: 700;
      margin-bottom: 4px;
    }

    .bill-card-info p {
      font-size: 0.8rem;
      color: var(--text-muted);
    }

    /* Modal for Bill Zoom */
    .modal-overlay {
      display: none;
      position: fixed;
      inset: 0;
      background: rgba(0,0,0,0.85);
      z-index: 100;
      align-items: center;
      justify-content: center;
      padding: 20px;
    }

    .modal-overlay.active {
      display: flex;
    }

    .modal-content {
      max-width: 90vw;
      max-height: 90vh;
      position: relative;
    }

    .modal-content img {
      max-width: 100%;
      max-height: 90vh;
      border-radius: 8px;
      box-shadow: 0 0 40px rgba(0,0,0,0.8);
      object-fit: contain;
    }

    .modal-close-btn {
      position: absolute;
      top: -15px;
      right: -15px;
      background: #ef4444;
      color: white;
      border: none;
      width: 36px;
      height: 36px;
      border-radius: 50%;
      font-size: 1.2rem;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 800;
    }

    /* Print media styling */
    @media print {
      header, .tabs-bar, .table-controls-bar, .bulk-tools-panel, .action-cta-row, .keypad-panel, .no-print {
        display: none !important;
      }
      body, main {
        background: #fff !important;
        color: #000 !important;
        padding: 0 !important;
        margin: 0 !important;
      }
      .tab-content {
        display: none !important;
      }
      #tab-labels {
        display: block !important;
      }
      .print-label-card {
        page-break-inside: avoid;
        break-inside: avoid;
      }
    }
  </style>
</head>
<body>

  <!-- Top App Header -->
  <header>
    <div class="header-top">
      <div class="brand-wrap">
        <div class="brand-icon">🎆</div>
        <div class="brand-text">
          <h1>Diwali Crackers Smart Pricing & Box Verifier</h1>
          <p>Nandigama Sales Godown • Lakshmi Vasavi Consignment</p>
        </div>
      </div>

      <!-- Live Financial & Progress Badges -->
      <div class="header-metrics">
        <div class="metric-pill highlight">
          <span class="label">Verified Boxes</span>
          <span class="value" id="header-verified-count">0 / 94 (0%)</span>
        </div>
        <div class="metric-pill">
          <span class="label">Stock Cost (+10%)</span>
          <span class="value">₹3,65,770</span>
        </div>
        <div class="metric-pill">
          <span class="label">Total Investment</span>
          <span class="value">₹4,07,218</span>
        </div>
        <div class="metric-pill green">
          <span class="label">Total Sales Value</span>
          <span class="value" id="header-total-revenue">₹0</span>
        </div>
      </div>
    </div>

    <!-- Navigation Tabs Bar -->
    <div class="tabs-bar">
      <button class="nav-tab active" onclick="switchTab('verifier')">
        <span>⚡</span> Fast Box Verifier (Sticker Numpad)
      </button>
      <button class="nav-tab" onclick="switchTab('catalog')">
        <span>📋</span> Master Price & Inventory Table (94 Items)
      </button>
      <button class="nav-tab" onclick="switchTab('analytics')">
        <span>📊</span> Total Expense & Profit Analytics
      </button>
      <button class="nav-tab" onclick="switchTab('labels')">
        <span>🏷️</span> Print Price Stickers / Box Labels
      </button>
      <button class="nav-tab" onclick="switchTab('bills')">
        <span>🧾</span> Original Bills & Gallery
      </button>
    </div>
  </header>

  <!-- Main Application Body -->
  <main>

    <!-- TAB 1: FAST BOX VERIFIER (NUMPAD HERO) -->
    <section id="tab-verifier" class="tab-content active">
      <div class="verifier-grid">
        
        <!-- Left Column: Fast Numpad & Box Search -->
        <div class="keypad-panel">
          <div class="search-box-wrap">
            <label>⚡ Instant Box / Sticker Lookup</label>
            <div class="search-input-wrap">
              <input type="text" id="sticker-input" placeholder="Type sticker # (e.g. 33, P1)..." autocomplete="off" autofocus>
              <button class="clear-btn" onclick="clearStickerInput()">✕</button>
            </div>
          </div>

          <!-- Rapid Touch Keypad for phone / standing operation -->
          <div class="numpad">
            <button class="num-key" onclick="pressKey('1')">1</button>
            <button class="num-key" onclick="pressKey('2')">2</button>
            <button class="num-key" onclick="pressKey('3')">3</button>
            <button class="num-key" onclick="pressKey('4')">4</button>
            <button class="num-key" onclick="pressKey('5')">5</button>
            <button class="num-key" onclick="pressKey('6')">6</button>
            <button class="num-key" onclick="pressKey('7')">7</button>
            <button class="num-key" onclick="pressKey('8')">8</button>
            <button class="num-key" onclick="pressKey('9')">9</button>
            <button class="num-key p-key" onclick="pressKey('P')">P<span class="key-hint">Pink Slip</span></button>
            <button class="num-key zero-key" onclick="pressKey('0')">0</button>
            <button class="num-key action-key" onclick="pressKey('BACK')">⌫<span class="key-hint">Del</span></button>
          </div>

          <!-- Quick Verified Tracker -->
          <div class="quick-list-section">
            <div class="quick-title">
              <span>Recently Verified Boxes</span>
              <span id="quick-verified-summary" style="color: var(--accent-green)">0 Done</span>
            </div>
            <div class="recent-chips" id="recent-chips-container">
              <!-- Dynamically rendered -->
            </div>
          </div>
        </div>

        <!-- Right Column: Active Box Display & Pricing Station -->
        <div class="card-display-panel" id="active-card-panel">
          
          <div class="card-header-bar">
            <div class="badge-group">
              <span class="sticker-badge" id="card-sticker-badge">STICKER #1</span>
              <span class="source-tag" id="card-source-tag">White Bill • Line #1</span>
            </div>
            <div id="card-status-pill" class="verification-status-pill unverified">
              <span>⏳</span> <span id="card-status-text">Pending Verification</span>
            </div>
          </div>

          <div class="item-title-section">
            <h2 id="card-item-name">3 1/2 Lakshmi (15P)</h2>
            <div class="item-pack-info">
              <span>📦 Quantity in Stock:</span>
              <strong id="card-units-text" style="color: #fff; font-size: 1.25rem;">20 Units</strong>
              <span id="card-pack-details" style="color: var(--text-dim)">(Pack of 20)</span>
            </div>
          </div>

          <!-- Costing Rates Grid -->
          <div class="rates-overview-grid">
            <div class="rate-stat-card wholesale-card">
              <div class="stat-label">Wholesale Rate (Base)</div>
              <div class="stat-val" id="card-wholesale-rate">₹150.00</div>
              <div class="stat-sub">From bill invoice</div>
            </div>

            <div class="rate-stat-card overhead-card">
              <div class="stat-label">Rate + 10% Overhead</div>
              <div class="stat-val" id="card-overhead-rate">₹165.00</div>
              <div class="stat-sub">+10% buffer added</div>
            </div>

            <div class="rate-stat-card units-card">
              <div class="stat-label">Total Box Cost (+10%)</div>
              <div class="stat-val" id="card-total-cost">₹3,300.00</div>
              <div class="stat-sub">Wholesale: ₹3,000</div>
            </div>
          </div>

          <!-- Selling Price Station -->
          <div class="selling-control-section">
            <div class="selling-header">
              <h3>
                <span>🎯</span>
                <span>Retail Selling Price to Write on Box</span>
              </h3>
              <span class="margin-badge" id="card-margin-badge">+51% MARGIN</span>
            </div>

            <div class="selling-input-row">
              <div class="sp-input-wrap">
                <span class="currency-symbol">₹</span>
                <input type="number" id="card-sp-input" value="250" step="5" oninput="onSellingPriceChange(this.value)">
              </div>
            </div>

            <div class="margin-buttons-row">
              <span class="margin-btn-label">Quick Set:</span>
              <button class="margin-btn" onclick="applyMarginPreset(0.30)">+30%</button>
              <button class="margin-btn" onclick="applyMarginPreset(0.40)">+40%</button>
              <button class="margin-btn active" onclick="applyMarginPreset(0.50)">+50%</button>
              <button class="margin-btn" onclick="applyMarginPreset(0.75)">+75%</button>
              <button class="margin-btn" onclick="applyMarginPreset(1.00)">+100% (2x)</button>
              <button class="margin-btn" onclick="applyMarginPreset(1.50)">2.5x</button>
              <button class="margin-btn" onclick="roundSellingPrice(10)">Round to ₹10</button>
            </div>

            <!-- Calculated Profit Metrics -->
            <div class="profit-metrics-bar">
              <div class="profit-sub-item">
                <div class="title">Net Profit per Unit</div>
                <div class="val green" id="card-profit-per-unit">₹85.00</div>
              </div>
              <div class="profit-sub-item">
                <div class="title">Total Revenue (Box)</div>
                <div class="val" id="card-box-revenue">₹5,000.00</div>
              </div>
              <div class="profit-sub-item">
                <div class="title">Net Profit (Box)</div>
                <div class="val green" id="card-box-profit">₹1,700.00</div>
              </div>
            </div>
          </div>

          <!-- Big Verification and Action Buttons -->
          <div class="action-cta-row">
            <button class="btn-verify-main" id="btn-toggle-verify" onclick="toggleCurrentVerified()">
              <span id="btn-verify-icon">✅</span>
              <span id="btn-verify-text">MARK VERIFIED & LABELED</span>
            </button>
            
            <button class="btn-nav-step" onclick="navigateItem(-1)">
              <span>◀</span> Prev
            </button>
            <button class="btn-nav-step" onclick="navigateItem(1)">
              Next <span>▶</span>
            </button>

            <button class="btn-voice-toggle" id="btn-voice" onclick="toggleVoiceSpeech()" title="Toggle Voice Announcement">
              <span>🔊</span>
            </button>
          </div>

        </div>

      </div>
    </section>


    <!-- TAB 2: MASTER CATALOG & PRICE TABLE -->
    <section id="tab-catalog" class="tab-content">
      
      <div class="table-controls-bar">
        <div class="table-filter-group">
          <button class="filter-btn active" onclick="setCatalogFilter('all')">All Items (94)</button>
          <button class="filter-btn" onclick="setCatalogFilter('white')">White Bill (74)</button>
          <button class="filter-btn" onclick="setCatalogFilter('pink')">Pink Bill (20)</button>
          <button class="filter-btn" onclick="setCatalogFilter('unverified')">Pending Boxes</button>
          <button class="filter-btn" onclick="setCatalogFilter('verified')">Verified Boxes</button>
        </div>

        <input type="text" class="table-search-input" id="table-search" placeholder="Search item name, rate, sticker #..." oninput="filterMasterTable()">
      </div>

      <div class="bulk-tools-panel">
        <div class="bulk-tools-left">
          <span class="bulk-label">Bulk Pricing Tools:</span>
          <button class="btn-bulk-action" onclick="bulkSetMargin(0.40)">Apply +40% Margin to All</button>
          <button class="btn-bulk-action" onclick="bulkSetMargin(0.50)">Apply +50% Margin to All</button>
          <button class="btn-bulk-action" onclick="bulkSetMargin(0.75)">Apply +75% Margin to All</button>
          <button class="btn-bulk-action" onclick="bulkRoundAll(10)">Round All to ₹10</button>
        </div>
        <div>
          <button class="btn-bulk-action" style="border-color: var(--accent-gold); color: var(--accent-gold);" onclick="exportCatalogCSV()">📥 Export to Excel / CSV</button>
        </div>
      </div>

      <div class="table-responsive">
        <table class="master-table" id="master-table">
          <thead>
            <tr>
              <th>Sticker #</th>
              <th>Bill Source</th>
              <th>Product Description</th>
              <th>Units</th>
              <th>Rate (₹)</th>
              <th>Rate + 10% (₹)</th>
              <th>Total Wholesale (₹)</th>
              <th>Total (+10%) (₹)</th>
              <th>Selling Price (₹)</th>
              <th>Total Sales (₹)</th>
              <th>Profit (₹)</th>
              <th>Margin %</th>
              <th>Status</th>
              <th>Action</th>
            </tr>
          </thead>
          <tbody id="master-table-body">
            <!-- Rendered by JS -->
          </tbody>
        </table>
      </div>
    </section>


    <!-- TAB 3: TOTAL EXPENSE & PROFIT ANALYTICS -->
    <section id="tab-analytics" class="tab-content">
      <div class="analytics-grid">
        
        <!-- Stock Procurement Breakdown -->
        <div class="analytics-card">
          <h3><span>📦</span> Consignment Purchase Cost</h3>
          <div class="expense-list">
            <div class="expense-row">
              <span>White Bill (Nandigama Items 1–74)</span>
              <span class="mono-amount">₹1,98,970</span>
            </div>
            <div class="expense-row">
              <span>Pink Bill (Lakshmi Vasavi Chinna Pasumarru)</span>
              <span class="mono-amount">₹1,33,548</span>
            </div>
            <div class="expense-row total-row">
              <span>Fireworks Materials Total</span>
              <span class="mono-amount">₹3,32,518</span>
            </div>
            <div class="expense-row" style="color: var(--accent-gold);">
              <span>+10% Buffer Overhead</span>
              <span class="mono-amount">₹33,252</span>
            </div>
            <div class="expense-row total-row" style="color: var(--accent-gold-light);">
              <span>Stock Value (+10% Overhead)</span>
              <span class="mono-amount">₹3,65,770</span>
            </div>
          </div>
        </div>

        <!-- Operational & Shed Setup Expenses -->
        <div class="analytics-card">
          <h3><span>🎪</span> Shed & Operational Expenses</h3>
          <div class="expense-list">
            <div class="expense-row">
              <span>1. Shed Permissions Charges</span>
              <span class="mono-amount">₹50,000</span>
            </div>
            <div class="expense-row">
              <span>2. Auto Transportation Charges</span>
              <span class="mono-amount">₹10,000</span>
            </div>
            <div class="expense-row">
              <span>3. Wooden Poles Rental Advance (₹400/day)</span>
              <span class="mono-amount">₹5,000</span>
            </div>
            <div class="expense-row">
              <span>4. Shed Setup Charges</span>
              <span class="mono-amount">₹3,000</span>
            </div>
            <div class="expense-row">
              <span>5. Labour (10 workers unloading)</span>
              <span class="mono-amount">₹2,000</span>
            </div>
            <div class="expense-row">
              <span>6. Car Petrol Expenses</span>
              <span class="mono-amount">₹2,200</span>
            </div>
            <div class="expense-row">
              <span>7. Food Expenses for Workers</span>
              <span class="mono-amount">₹1,000</span>
            </div>
            <div class="expense-row">
              <span>8. Ropes & Miscellaneous Setup</span>
              <span class="mono-amount">₹1,000</span>
            </div>
            <div class="expense-row">
              <span>9. Additional Auto Charges</span>
              <span class="mono-amount">₹500</span>
            </div>
            <div class="expense-row total-row">
              <span>Total Operational Overhead</span>
              <span class="mono-amount">₹74,700</span>
            </div>
          </div>
        </div>

        <!-- Grand Financial Summary & ROI -->
        <div class="analytics-card" style="border-color: var(--accent-gold);">
          <h3><span>💰</span> Grand Financial Position & ROI</h3>
          <div class="expense-list">
            <div class="expense-row">
              <span>Materials Purchase</span>
              <span class="mono-amount">₹3,32,518</span>
            </div>
            <div class="expense-row">
              <span>Shed & Operations Expenses</span>
              <span class="mono-amount">₹74,700</span>
            </div>
            <div class="expense-row total-row" style="font-size: 1.15rem; color: #f87171;">
              <span>Grand Total Project Investment</span>
              <span class="mono-amount">₹4,07,218</span>
            </div>
            <div class="expense-row total-row" style="font-size: 1.15rem; color: #34d399; margin-top: 10px;">
              <span>Projected Total Sales Revenue</span>
              <span class="mono-amount" id="analytics-projected-sales">₹0</span>
            </div>
            <div class="expense-row total-row" style="font-size: 1.25rem; color: #fbbf24;">
              <span>Net Business Profit</span>
              <span class="mono-amount" id="analytics-net-profit">₹0</span>
            </div>
            <div class="expense-row" style="font-size: 0.85rem; color: var(--text-dim);">
              <span>ROI on Total Capital</span>
              <span class="mono-amount" id="analytics-roi">0%</span>
            </div>
          </div>
        </div>

        <!-- Wholesaler Payment Ledger -->
        <div class="analytics-card">
          <h3><span>🧾</span> Wholesaler Account Ledger (Lakshmi Vasavi)</h3>
          <div class="expense-list">
            <div class="expense-row">
              <span>Total Invoice Bill Amount</span>
              <span class="mono-amount">₹3,32,518</span>
            </div>
            <div class="expense-row" style="color: #34d399;">
              <span>Cash Deposited (జమ)</span>
              <span class="mono-amount">₹60,000</span>
            </div>
            <div class="expense-row" style="color: #34d399;">
              <span>GPay Transfer 1</span>
              <span class="mono-amount">₹80,000</span>
            </div>
            <div class="expense-row" style="color: #34d399;">
              <span>GPay Transfer 2</span>
              <span class="mono-amount">₹80,000</span>
            </div>
            <div class="expense-row total-row" style="color: #34d399;">
              <span>Total Paid So Far</span>
              <span class="mono-amount">₹2,20,000</span>
            </div>
            <div class="expense-row total-row" style="color: #f87171;">
              <span>Balance Outstanding to Wholesaler</span>
              <span class="mono-amount">₹1,12,518</span>
            </div>
          </div>
        </div>

      </div>
    </section>


    <!-- TAB 4: PRINTABLE STICKERS / BOX LABELS -->
    <section id="tab-labels" class="tab-content">
      <div class="table-controls-bar no-print">
        <h3 style="font-weight: 700; color: var(--accent-gold-light);">🏷️ Printable Price Stickers & Box Tags</h3>
        <div style="display: flex; gap: 10px;">
          <button class="btn-bulk-action" onclick="printLabels('all')">Print All 94 Labels</button>
          <button class="btn-bulk-action" style="background: var(--accent-gold); color: #000; font-weight: 800;" onclick="window.print()">🖨️ Print to Paper / PDF</button>
        </div>
      </div>

      <div class="printable-sheet" id="printable-labels-container">
        <!-- Rendered by JS -->
      </div>
    </section>


    <!-- TAB 5: ORIGINAL BILLS & SLIPS GALLERY -->
    <section id="tab-bills" class="tab-content">
      <div class="gallery-grid">
        
        <div class="bill-card">
          <div class="bill-card-img-wrap" onclick="openImageModal('WhatsApp Image 2026-11-06 at 8.20.07 AM.jpeg')">
            <img src="WhatsApp Image 2026-11-06 at 8.20.07 AM.jpeg" alt="Pink Bill Chinna Pasumarru">
          </div>
          <div class="bill-card-info">
            <h4>Pink Bill (Lakshmi Vasavi, Chinna Pasumarru)</h4>
            <p>20 line items (P1–P20) • Subtotal: ₹1,33,548</p>
          </div>
        </div>

        <div class="bill-card">
          <div class="bill-card-img-wrap" onclick="openImageModal('WhatsApp Image 2026-11-06 at 8.20.07 AM (1).jpeg')">
            <img src="WhatsApp Image 2026-11-06 at 8.20.07 AM (1).jpeg" alt="White Bill Page 1">
          </div>
          <div class="bill-card-info">
            <h4>White Bill – Page 1 (Nandigama)</h4>
            <p>Numbered Items 1 to 35 • Subtotal: ₹1,14,670</p>
          </div>
        </div>

        <div class="bill-card">
          <div class="bill-card-img-wrap" onclick="openImageModal('WhatsApp Image 2026-11-06 at 8.20.07 AM (2).jpeg')">
            <img src="WhatsApp Image 2026-11-06 at 8.20.07 AM (2).jpeg" alt="White Bill Page 2">
          </div>
          <div class="bill-card-info">
            <h4>White Bill – Page 2 (Nandigama)</h4>
            <p>Numbered Items 36 to 70 • Subtotal: ₹79,270</p>
          </div>
        </div>

        <div class="bill-card">
          <div class="bill-card-img-wrap" onclick="openImageModal('WhatsApp Image 2026-11-06 at 8.20.08 AM.jpeg')">
            <img src="WhatsApp Image 2026-11-06 at 8.20.08 AM.jpeg" alt="White Bill Page 3">
          </div>
          <div class="bill-card-info">
            <h4>White Bill – Page 3 & Payment Records</h4>
            <p>Items 71 to 74 (₹5,030) • Cash ₹60k + GPay ₹1.6L = ₹2.2L Paid</p>
          </div>
        </div>

        <div class="bill-card">
          <div class="bill-card-img-wrap" onclick="openImageModal('ChatGPT Image Nov 6, 2026, 08_27_55 AM.png')">
            <img src="ChatGPT Image Nov 6, 2026, 08_27_55 AM.png" alt="Expense Infographic">
          </div>
          <div class="bill-card-info">
            <h4>Diwali Complete Expense Infographic</h4>
            <p>All items itemized • Grand Total: ₹4,07,700</p>
          </div>
        </div>

      </div>
    </section>

  </main>

  <!-- Modal for full size bill image -->
  <div class="modal-overlay" id="image-modal" onclick="closeImageModal()">
    <div class="modal-content" onclick="event.stopPropagation()">
      <button class="modal-close-btn" onclick="closeImageModal()">✕</button>
      <img id="modal-img" src="" alt="Full size bill view">
    </div>
  </div>

  <!-- APPLICATION LOGIC & DATA -->
  <script>
    // Embedded Master Data
    const RAW_ITEMS = """ + items_json_str + """;

    // Application State with LocalStorage persistence
    let items = [];
    let currentIndex = 0;
    let voiceEnabled = false;
    let currentCatalogFilter = 'all';

    // Web Audio Sound Synthesizer
    const audioCtx = new (window.AudioContext || window.webkitAudioContext)();
    function playBeep(freq = 600, duration = 0.08) {
      try {
        if (audioCtx.state === 'suspended') audioCtx.resume();
        const osc = audioCtx.createOscillator();
        const gain = audioCtx.createGain();
        osc.frequency.value = freq;
        osc.connect(gain);
        gain.connect(audioCtx.destination);
        gain.gain.setValueAtTime(0.12, audioCtx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + duration);
        osc.start();
        osc.stop(audioCtx.currentTime + duration);
      } catch (e) {}
    }

    function playSuccessChime() {
      playBeep(523.25, 0.1); // C5
      setTimeout(() => playBeep(659.25, 0.1), 100); // E5
      setTimeout(() => playBeep(783.99, 0.18), 200); // G5
    }

    // Initialize State
    function initApp() {
      const saved = localStorage.getItem('diwali_cracker_items_v1');
      if (saved) {
        try {
          items = JSON.parse(saved);
        } catch (e) {
          items = JSON.parse(JSON.stringify(RAW_ITEMS));
        }
      } else {
        items = JSON.parse(JSON.stringify(RAW_ITEMS));
      }

      // Check current index
      const savedIndex = localStorage.getItem('diwali_last_index');
      if (savedIndex !== null && items[savedIndex]) {
        currentIndex = parseInt(savedIndex);
      }

      renderActiveCard();
      renderRecentChips();
      renderMasterTable();
      renderPrintableLabels();
      updateGlobalMetrics();

      // Setup Input listeners
      const input = document.getElementById('sticker-input');
      input.addEventListener('input', (e) => {
        handleStickerSearch(e.target.value.trim());
      });
      input.addEventListener('keydown', (e) => {
        if (e.key === 'Enter') {
          e.preventDefault();
          toggleCurrentVerified();
        }
      });
    }

    function saveState() {
      localStorage.setItem('diwali_cracker_items_v1', JSON.stringify(items));
      localStorage.setItem('diwali_last_index', currentIndex.toString());
      updateGlobalMetrics();
    }

    // Tab Switching
    function switchTab(tabId) {
      document.querySelectorAll('.tab-content').forEach(el => el.classList.remove('active'));
      document.querySelectorAll('.nav-tab').forEach(el => el.classList.remove('active'));

      const targetTab = document.getElementById('tab-' + tabId);
      if (targetTab) targetTab.classList.add('active');

      const tabs = document.querySelectorAll('.nav-tab');
      if (tabId === 'verifier') tabs[0].classList.add('active');
      else if (tabId === 'catalog') tabs[1].classList.add('active');
      else if (tabId === 'analytics') tabs[2].classList.add('active');
      else if (tabId === 'labels') tabs[3].classList.add('active');
      else if (tabId === 'bills') tabs[4].classList.add('active');

      if (tabId === 'verifier') {
        setTimeout(() => document.getElementById('sticker-input').focus(), 100);
      }
    }

    // Numpad Keypress Handling
    function pressKey(key) {
      playBeep(450, 0.04);
      if (navigator.vibrate) navigator.vibrate(20);

      const input = document.getElementById('sticker-input');
      if (key === 'BACK') {
        input.value = input.value.slice(0, -1);
      } else {
        input.value += key;
      }
      handleStickerSearch(input.value.trim());
    }

    function clearStickerInput() {
      const input = document.getElementById('sticker-input');
      input.value = '';
      input.focus();
    }

    // Lookup algorithm: finds matching item by sticker number or fuzzy name
    function handleStickerSearch(val) {
      if (!val) return;
      const term = val.toLowerCase();

      // Check exact sticker match first (e.g. "33", "p5")
      let matchIdx = items.findIndex(item => item.sticker_no.toLowerCase() === term);

      // If not exact, check if user typed number for pink slip like "101" or "P1"
      if (matchIdx === -1) {
        matchIdx = items.findIndex(item => item.search_keys && item.search_keys.includes(term));
      }

      // If still not, match starting digits
      if (matchIdx === -1) {
        matchIdx = items.findIndex(item => item.sticker_no.toLowerCase().startsWith(term));
      }

      // If still not, match name
      if (matchIdx === -1) {
        matchIdx = items.findIndex(item => item.name.toLowerCase().includes(term));
      }

      if (matchIdx !== -1) {
        currentIndex = matchIdx;
        renderActiveCard();
      }
    }

    // Render Active Card
    function renderActiveCard() {
      const item = items[currentIndex];
      if (!item) return;

      const badge = document.getElementById('card-sticker-badge');
      badge.textContent = 'STICKER #' + item.sticker_no;
      if (item.bill_type === 'pink') {
        badge.classList.add('pink-badge');
      } else {
        badge.classList.remove('pink-badge');
      }

      document.getElementById('card-source-tag').textContent = `${item.bill_name} • Line #${item.bill_item_no}`;
      document.getElementById('card-item-name').textContent = item.name;
      document.getElementById('card-units-text').textContent = `${item.units} Units`;
      document.getElementById('card-pack-details').textContent = `(Pack info: ${item.pack_details})`;

      document.getElementById('card-wholesale-rate').textContent = `₹${item.rate.toFixed(2)}`;
      document.getElementById('card-overhead-rate').textContent = `₹${item.rate_plus_10.toFixed(2)}`;
      document.getElementById('card-total-cost').textContent = `₹${(item.units * item.rate_plus_10).toLocaleString('en-IN', {minimumFractionDigits: 2})}`;

      const spInput = document.getElementById('card-sp-input');
      spInput.value = item.selling_price;

      updateCardCalculations();

      // Verification Status Pill
      const statusPill = document.getElementById('card-status-pill');
      const statusText = document.getElementById('card-status-text');
      const verifyBtn = document.getElementById('btn-toggle-verify');
      const verifyBtnText = document.getElementById('btn-verify-text');
      const verifyBtnIcon = document.getElementById('btn-verify-icon');
      const panel = document.getElementById('active-card-panel');

      if (item.verified) {
        statusPill.className = 'verification-status-pill verified';
        statusText.textContent = 'Verified & Tagged';
        verifyBtn.className = 'btn-verify-main is-verified';
        verifyBtnText.textContent = 'VERIFIED ✓ (CLICK TO UNMARK)';
        verifyBtnIcon.textContent = '✔';
        panel.classList.add('verified-glow');
      } else {
        statusPill.className = 'verification-status-pill unverified';
        statusText.textContent = 'Pending Verification';
        verifyBtn.className = 'btn-verify-main';
        verifyBtnText.textContent = 'MARK VERIFIED & LABELED';
        verifyBtnIcon.textContent = '✅';
        panel.classList.remove('verified-glow');
      }

      // Voice callout if active
      if (voiceEnabled) {
        speakItem(item);
      }
    }

    function updateCardCalculations() {
      const item = items[currentIndex];
      const sp = parseFloat(document.getElementById('card-sp-input').value) || 0;
      item.selling_price = sp;

      const costPlus10 = item.rate_plus_10;
      const profitPerUnit = sp - costPlus10;
      const marginPct = costPlus10 > 0 ? ((sp - costPlus10) / costPlus10 * 100).toFixed(0) : 0;
      const boxRevenue = sp * item.units;
      const boxProfit = profitPerUnit * item.units;

      document.getElementById('card-margin-badge').textContent = (marginPct >= 0 ? '+' : '') + marginPct + '% MARGIN';
      document.getElementById('card-profit-per-unit').textContent = `₹${profitPerUnit.toFixed(2)}`;
      document.getElementById('card-box-revenue').textContent = `₹${boxRevenue.toLocaleString('en-IN', {minimumFractionDigits: 2})}`;
      document.getElementById('card-box-profit').textContent = `₹${boxProfit.toLocaleString('en-IN', {minimumFractionDigits: 2})}`;
    }

    function onSellingPriceChange(newVal) {
      const val = parseFloat(newVal) || 0;
      items[currentIndex].selling_price = val;
      updateCardCalculations();
      saveState();
      renderMasterTableRow(currentIndex);
    }

    function applyMarginPreset(multiplier) {
      playBeep(700, 0.05);
      const item = items[currentIndex];
      const rawPrice = item.rate_plus_10 * (1 + multiplier);
      let rounded = roundSmart(rawPrice);
      item.selling_price = rounded;
      document.getElementById('card-sp-input').value = rounded;
      updateCardCalculations();
      saveState();
      renderMasterTableRow(currentIndex);
    }

    function roundSellingPrice(toNearest) {
      const item = items[currentIndex];
      item.selling_price = Math.ceil(item.selling_price / toNearest) * toNearest;
      document.getElementById('card-sp-input').value = item.selling_price;
      updateCardCalculations();
      saveState();
      renderMasterTableRow(currentIndex);
    }

    function roundSmart(val) {
      if (val <= 30) return Math.round(val);
      if (val <= 100) return Math.ceil(val / 5) * 5;
      if (val <= 500) return Math.ceil(val / 10) * 10;
      return Math.ceil(val / 50) * 50;
    }

    // Toggle Verified State
    function toggleCurrentVerified() {
      const item = items[currentIndex];
      item.verified = !item.verified;
      item.verified_at = item.verified ? new Date().toISOString() : null;

      if (item.verified) {
        playSuccessChime();
        if (navigator.vibrate) navigator.vibrate([40, 60, 80]);
      } else {
        playBeep(300, 0.1);
      }

      saveState();
      renderActiveCard();
      renderRecentChips();
      renderMasterTableRow(currentIndex);

      // Auto-advance to next unverified item if just marked verified
      if (item.verified) {
        setTimeout(() => {
          clearStickerInput();
          navigateItem(1);
        }, 500);
      }
    }

    function navigateItem(step) {
      playBeep(500, 0.04);
      let nextIdx = currentIndex + step;
      if (nextIdx < 0) nextIdx = items.length - 1;
      if (nextIdx >= items.length) nextIdx = 0;
      currentIndex = nextIdx;
      renderActiveCard();
      document.getElementById('sticker-input').value = '';
    }

    // Recent Chips
    function renderRecentChips() {
      const container = document.getElementById('recent-chips-container');
      const verifiedItems = items.filter(i => i.verified);
      document.getElementById('quick-verified-summary').textContent = `${verifiedItems.length} / ${items.length} Done`;

      container.innerHTML = '';
      items.slice(0, 40).forEach((item, idx) => {
        const chip = document.createElement('div');
        chip.className = `recent-chip ${item.verified ? 'verified' : ''}`;
        chip.textContent = `#${item.sticker_no}`;
        chip.onclick = () => {
          currentIndex = idx;
          renderActiveCard();
        };
        container.appendChild(chip);
      });
    }

    // Global Metrics Calculation
    function updateGlobalMetrics() {
      const verifiedCount = items.filter(i => i.verified).length;
      const totalCount = items.length;
      const pct = ((verifiedCount / totalCount) * 100).toFixed(0);
      document.getElementById('header-verified-count').textContent = `${verifiedCount} / ${totalCount} (${pct}%)`;

      let totalSales = 0;
      items.forEach(i => {
        totalSales += (i.selling_price || 0) * i.units;
      });

      const totalInvestment = 407218; // 3,32,518 stock + 74,700 shed
      const netProfit = totalSales - totalInvestment;
      const roi = ((netProfit / totalInvestment) * 100).toFixed(1);

      document.getElementById('header-total-revenue').textContent = `₹${Math.round(totalSales).toLocaleString('en-IN')}`;
      const projEl = document.getElementById('analytics-projected-sales');
      if (projEl) projEl.textContent = `₹${Math.round(totalSales).toLocaleString('en-IN')}`;
      
      const netEl = document.getElementById('analytics-net-profit');
      if (netEl) {
        netEl.textContent = `₹${Math.round(netProfit).toLocaleString('en-IN')}`;
        netEl.style.color = netProfit >= 0 ? '#fbbf24' : '#ef4444';
      }

      const roiEl = document.getElementById('analytics-roi');
      if (roiEl) roiEl.textContent = `${roi}% ROI`;
    }

    // Voice Synthesis
    function toggleVoiceSpeech() {
      voiceEnabled = !voiceEnabled;
      const btn = document.getElementById('btn-voice');
      if (voiceEnabled) {
        btn.classList.add('voice-active');
        playSuccessChime();
        speakText("Voice enabled");
      } else {
        btn.classList.remove('voice-active');
        playBeep(350, 0.1);
      }
    }

    function speakItem(item) {
      if (!('speechSynthesis' in window)) return;
      window.speechSynthesis.cancel();
      const text = `Box ${item.sticker_no}, ${item.name}, Cost ${Math.round(item.rate_plus_10)}, Sell at ${item.selling_price}`;
      speakText(text);
    }

    function speakText(text) {
      if (!('speechSynthesis' in window)) return;
      const utterance = new SpeechSynthesisUtterance(text);
      utterance.rate = 1.05;
      utterance.pitch = 1.0;
      window.speechSynthesis.speak(utterance);
    }

    // MASTER CATALOG TABLE RENDERING
    function renderMasterTable() {
      const tbody = document.getElementById('master-table-body');
      tbody.innerHTML = '';
      items.forEach((item, idx) => {
        const tr = document.createElement('tr');
        tr.id = `table-row-${idx}`;
        if (item.verified) tr.classList.add('row-verified');
        tr.innerHTML = getTableRowHTML(item, idx);
        tbody.appendChild(tr);
      });
    }

    function getTableRowHTML(item, idx) {
      const sp = item.selling_price || 0;
      const totalSales = sp * item.units;
      const profit = (sp - item.rate_plus_10) * item.units;
      const marginPct = item.rate_plus_10 > 0 ? (((sp - item.rate_plus_10) / item.rate_plus_10) * 100).toFixed(0) : 0;
      const badgeClass = item.bill_type === 'pink' ? 'badge-p' : 'badge-w';

      return `
        <td><span class="table-sticker-badge ${badgeClass}">#${item.sticker_no}</span></td>
        <td style="color: var(--text-dim); font-size: 0.75rem;">${item.bill_type.toUpperCase()}</td>
        <td><strong>${item.name}</strong> <span style="font-size: 0.72rem; color: var(--text-dim)">(${item.pack_details})</span></td>
        <td style="font-family: 'JetBrains Mono', monospace; font-weight: 700;">${item.units}</td>
        <td style="font-family: 'JetBrains Mono', monospace;">₹${item.rate}</td>
        <td style="font-family: 'JetBrains Mono', monospace; color: var(--accent-gold);">₹${item.rate_plus_10.toFixed(2)}</td>
        <td style="font-family: 'JetBrains Mono', monospace;">₹${item.bill_total.toLocaleString('en-IN')}</td>
        <td style="font-family: 'JetBrains Mono', monospace; color: var(--accent-gold);">₹${Math.round(item.total_plus_10).toLocaleString('en-IN')}</td>
        <td>
          <input type="number" class="table-sp-input" value="${sp}" onchange="updateTableItemSP(${idx}, this.value)">
        </td>
        <td style="font-family: 'JetBrains Mono', monospace; font-weight: 700;">₹${Math.round(totalSales).toLocaleString('en-IN')}</td>
        <td style="font-family: 'JetBrains Mono', monospace; color: ${profit >= 0 ? '#34d399' : '#f87171'}; font-weight: 700;">₹${Math.round(profit).toLocaleString('en-IN')}</td>
        <td style="font-family: 'JetBrains Mono', monospace; font-weight: 700;">${marginPct}%</td>
        <td>
          <span style="cursor: pointer; font-size: 1.1rem;" onclick="toggleTableVerified(${idx})">
            ${item.verified ? '✅' : '⬜'}
          </span>
        </td>
        <td>
          <button class="btn-bulk-action" onclick="jumpToVerifier(${idx})">🔍 Verify</button>
        </td>
      `;
    }

    function renderMasterTableRow(idx) {
      const tr = document.getElementById(`table-row-${idx}`);
      if (tr) {
        const item = items[idx];
        if (item.verified) tr.classList.add('row-verified');
        else tr.classList.remove('row-verified');
        tr.innerHTML = getTableRowHTML(item, idx);
      }
    }

    function updateTableItemSP(idx, val) {
      items[idx].selling_price = parseFloat(val) || 0;
      saveState();
      renderMasterTableRow(idx);
      if (currentIndex === idx) renderActiveCard();
    }

    function toggleTableVerified(idx) {
      items[idx].verified = !items[idx].verified;
      saveState();
      renderMasterTableRow(idx);
      renderRecentChips();
      if (currentIndex === idx) renderActiveCard();
    }

    function jumpToVerifier(idx) {
      currentIndex = idx;
      switchTab('verifier');
      renderActiveCard();
    }

    // Table Filtering
    function setCatalogFilter(filter) {
      currentCatalogFilter = filter;
      document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
      event.target.classList.add('active');
      filterMasterTable();
    }

    function filterMasterTable() {
      const search = (document.getElementById('table-search').value || '').toLowerCase();
      items.forEach((item, idx) => {
        const tr = document.getElementById(`table-row-${idx}`);
        if (!tr) return;

        let matchesFilter = true;
        if (currentCatalogFilter === 'white' && item.bill_type !== 'white') matchesFilter = false;
        if (currentCatalogFilter === 'pink' && item.bill_type !== 'pink') matchesFilter = false;
        if (currentCatalogFilter === 'verified' && !item.verified) matchesFilter = false;
        if (currentCatalogFilter === 'unverified' && item.verified) matchesFilter = false;

        let matchesSearch = true;
        if (search) {
          matchesSearch = item.name.toLowerCase().includes(search) || 
                          item.sticker_no.toLowerCase().includes(search) ||
                          item.rate.toString().includes(search);
        }

        tr.style.display = (matchesFilter && matchesSearch) ? '' : 'none';
      });
    }

    // Bulk Markup Tools
    function bulkSetMargin(multiplier) {
      if (!confirm(`Apply +${multiplier*100}% margin over cost (+10%) to all 94 items?`)) return;
      items.forEach(item => {
        const raw = item.rate_plus_10 * (1 + multiplier);
        item.selling_price = roundSmart(raw);
      });
      saveState();
      renderMasterTable();
      renderActiveCard();
      renderPrintableLabels();
      alert("Updated selling prices for all items!");
    }

    function bulkRoundAll(nearest) {
      items.forEach(item => {
        item.selling_price = Math.ceil(item.selling_price / nearest) * nearest;
      });
      saveState();
      renderMasterTable();
      renderActiveCard();
      renderPrintableLabels();
      alert(`Rounded all selling prices to nearest ₹${nearest}!`);
    }

    // Export to CSV
    function exportCatalogCSV() {
      let csv = "Sticker No,Bill Source,Item Name,Pack Info,Units,Wholesale Rate,Rate Plus 10pct,Bill Total,Total Plus 10pct,Selling Price,Total Sales,Net Profit,Verified\\n";
      items.forEach(item => {
        const sp = item.selling_price || 0;
        const totalSales = sp * item.units;
        const profit = (sp - item.rate_plus_10) * item.units;
        csv += `"${item.sticker_no}","${item.bill_name}","${item.name}","${item.pack_details}",${item.units},${item.rate},${item.rate_plus_10},${item.bill_total},${item.total_plus_10},${sp},${totalSales},${profit},"${item.verified ? 'YES' : 'NO'}"\\n`;
      });

      const blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' });
      const url = URL.createObjectURL(blob);
      const link = document.createElement("a");
      link.setAttribute("href", url);
      link.setAttribute("download", "Diwali_Crackers_Pricing_Catalog.csv");
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
    }

    // PRINTABLE LABELS GENERATOR
    function renderPrintableLabels() {
      const container = document.getElementById('printable-labels-container');
      container.innerHTML = '';
      items.forEach(item => {
        const card = document.createElement('div');
        card.className = 'print-label-card';
        card.innerHTML = `
          <div>
            <div class="label-card-top">
              <span class="label-sticker-num">#${item.sticker_no}</span>
              <span class="label-units">${item.units} Units</span>
            </div>
            <div class="label-product-name">${item.name}</div>
          </div>
          <div>
            <div class="label-price-block">₹${item.selling_price}</div>
          </div>
        `;
        container.appendChild(card);
      });
    }

    // Modal Image Zoom
    function openImageModal(src) {
      document.getElementById('modal-img').src = src;
      document.getElementById('image-modal').classList.add('active');
    }
    function closeImageModal() {
      document.getElementById('image-modal').classList.remove('active');
    }

    // Start on DOM Ready
    window.addEventListener('DOMContentLoaded', initApp);
  </script>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("index.html created successfully!")
