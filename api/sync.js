const fs = require('fs');
const path = require('path');

const TMP_FILE = '/tmp/diwali_sync_state.json';
const GH_ISSUE_URL = 'https://api.github.com/repos/koushiksirivella/diwali-crackers-scanner/issues/1';

let cachedDefaultItems = null;
function loadDefaultItems() {
  if (cachedDefaultItems) return JSON.parse(JSON.stringify(cachedDefaultItems));
  try {
    const p = path.join(process.cwd(), 'items_data.json');
    if (fs.existsSync(p)) {
      cachedDefaultItems = JSON.parse(fs.readFileSync(p, 'utf8'));
      return JSON.parse(JSON.stringify(cachedDefaultItems));
    }
  } catch (e) {}
  return [];
}

function packCompactState(items, expenses, updatedAt) {
  const map = {};
  const added = [];
  const defaults = loadDefaultItems();
  const defaultIds = new Set(defaults.map(d => String(d.box_no)));

  (items || []).forEach((it, idx) => {
    const bNo = String(it.box_no || (idx + 1));
    if (defaultIds.has(bNo)) {
      map[bNo] = {
        n: it.name,
        p: it.pack_details,
        u: Number(it.total_units || 0),
        s: Number(it.units_sold || 0),
        r: Number(it.rate || 0),
        c20: Number(it.rate_plus_20 || 0),
        sp: Number(it.selling_price || 0),
        cp: Boolean(it.is_custom_price),
        v: Boolean(it.verified)
      };
    } else {
      added.push(it);
    }
  });

  return {
    v: 10,
    updatedAt: Number(updatedAt) || Date.now(),
    map,
    added,
    expenses: Array.isArray(expenses) ? expenses : []
  };
}

function unpackCompactState(compact) {
  const defaults = loadDefaultItems();
  if (!compact || !compact.map) {
    return {
      items: defaults,
      expenses: (compact && compact.expenses) || [],
      updatedAt: (compact && compact.updatedAt) || 0
    };
  }
  const items = defaults.map((d, idx) => {
    const bNo = String(d.box_no || (idx + 1));
    const ov = compact.map[bNo];
    if (!ov) return d;
    return {
      ...d,
      name: ov.n !== undefined ? ov.n : d.name,
      pack_details: ov.p !== undefined ? ov.p : d.pack_details,
      total_units: ov.u !== undefined ? ov.u : d.total_units,
      units_sold: ov.s !== undefined ? ov.s : d.units_sold,
      rate: ov.r !== undefined ? ov.r : d.rate,
      rate_plus_20: ov.c20 !== undefined ? ov.c20 : d.rate_plus_20,
      selling_price: ov.sp !== undefined ? ov.sp : d.selling_price,
      is_custom_price: ov.cp !== undefined ? ov.cp : d.is_custom_price,
      verified: ov.v !== undefined ? ov.v : d.verified
    };
  });
  if (Array.isArray(compact.added) && compact.added.length > 0) {
    compact.added.forEach(a => items.push(a));
  }
  return {
    items,
    expenses: Array.isArray(compact.expenses) ? compact.expenses : [],
    updatedAt: Number(compact.updatedAt || 0)
  };
}

async function fetchFromCloudDB() {
  const token = process.env.GH_SYNC_TOKEN;
  const headers = {
    'Accept': 'application/vnd.github+json',
    'User-Agent': 'diwali-crackers-pos-sync',
    'Cache-Control': 'no-cache, no-store'
  };
  if (token) headers['Authorization'] = `Bearer ${token}`;
  try {
    const res = await fetch(`${GH_ISSUE_URL}?t=${Date.now()}`, { headers, cache: 'no-store' });
    if (!res.ok) return null;
    const issue = await res.json();
    if (!issue || !issue.body) return null;
    const compact = JSON.parse(issue.body);
    if (compact && compact.v === 10) {
      return unpackCompactState(compact);
    }
    return null;
  } catch (e) {
    return null;
  }
}

async function pushToCloudDB(stateObj) {
  const token = process.env.GH_SYNC_TOKEN;
  if (!token) return;
  try {
    const compact = packCompactState(stateObj.items, stateObj.expenses, stateObj.updatedAt);
    await fetch(GH_ISSUE_URL, {
      method: 'PATCH',
      headers: {
        'Authorization': `Bearer ${token}`,
        'Accept': 'application/vnd.github+json',
        'Content-Type': 'application/json',
        'User-Agent': 'diwali-crackers-pos-sync'
      },
      body: JSON.stringify({ body: JSON.stringify(compact) })
    });
  } catch (e) {}
}

async function readState() {
  let localState = global.__DIWALI_LIVE_STATE__ || null;
  try {
    if (fs.existsSync(TMP_FILE)) {
      const tmpParsed = JSON.parse(fs.readFileSync(TMP_FILE, 'utf8'));
      if (!localState || (tmpParsed.updatedAt || 0) > (localState.updatedAt || 0)) {
        localState = tmpParsed;
        global.__DIWALI_LIVE_STATE__ = localState;
      }
    }
  } catch (e) {}

  const cloudState = await fetchFromCloudDB();
  if (cloudState && Array.isArray(cloudState.items) && cloudState.items.length >= 90) {
    if (!localState || (cloudState.updatedAt || 0) >= (localState.updatedAt || 0)) {
      localState = cloudState;
      global.__DIWALI_LIVE_STATE__ = localState;
      try {
        fs.writeFileSync(TMP_FILE, JSON.stringify(localState), 'utf8');
      } catch (e) {}
    }
  }

  if (localState && Array.isArray(localState.items) && localState.items.length >= 90) {
    return localState;
  }

  return {
    items: loadDefaultItems(),
    expenses: [],
    updatedAt: Date.now()
  };
}

async function writeState(newState) {
  const existing = global.__DIWALI_LIVE_STATE__ || {};
  const stateObj = {
    items: Array.isArray(newState.items) ? newState.items : (Array.isArray(newState) ? newState : []),
    expenses: Array.isArray(newState.expenses) ? newState.expenses : (existing.expenses || []),
    updatedAt: Number(newState.updatedAt) || Date.now()
  };
  global.__DIWALI_LIVE_STATE__ = stateObj;
  try {
    fs.writeFileSync(TMP_FILE, JSON.stringify(stateObj), 'utf8');
  } catch (e) {}
  await pushToCloudDB(stateObj);
  return stateObj;
}

module.exports = async (req, res) => {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
  res.setHeader('Cache-Control', 'no-store, no-cache, must-revalidate, proxy-revalidate');

  if (req.method === 'OPTIONS') {
    return res.status(204).end();
  }

  if (req.method === 'GET') {
    const state = await readState();
    return res.status(200).json({
      items: state.items,
      expenses: state.expenses,
      updatedAt: state.updatedAt
    });
  }

  if (req.method === 'POST') {
    try {
      const body = typeof req.body === 'string' ? JSON.parse(req.body) : (req.body || {});
      const items = Array.isArray(body) ? body : body.items;
      if (!Array.isArray(items) || items.length === 0) {
        return res.status(400).json({ error: 'Invalid items payload' });
      }
      const saved = await writeState({
        items,
        expenses: body.expenses,
        updatedAt: body.updatedAt || Date.now()
      });
      return res.status(200).json({
        success: true,
        updatedAt: saved.updatedAt,
        count: saved.items.length
      });
    } catch (e) {
      return res.status(400).json({ error: e.message });
    }
  }

  return res.status(405).json({ error: 'Method not allowed' });
};
