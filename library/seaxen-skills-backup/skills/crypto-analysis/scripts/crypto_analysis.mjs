// crypto-analysis — multi-source crypto intelligence with selective source routing.
//
// Goals:
// - Use only relevant public sources for a given token/coin.
// - Prefer low-friction public APIs first.
// - Fall back gracefully and always return a compact, human-readable verdict.
//
// Supported sources:
// - CoinGecko (baseline price/market data, always try)
// - CoinMarketCap (optional key)
// - DeFiLlama (only for mapped DeFi/protocol tokens or when explicitly requested)
// - Coinglass (only when derivatives requested + key present)
// - DexScreener / GeckoTerminal (DEX liquidity/volume tokens)
// - Binance/Bybit/OKX/Hyperliquid public market data when relevant
//
// The module exports a default async function for Hermes skill runtime, and also
// supports a small CLI for local testing.

const fetchFn = globalThis.fetch;

const DEFAULT_TIMEOUT_MS = 12000;
const DEFAULT_VS = 'usd';

const COINGECKO_TO_DEFILLAMA = {
  tao: 'bittensor',
  bittensor: 'bittensor',
  ethereum: 'ethereum',
  bitcoin: 'bitcoin',
  solana: 'solana',
  avalanche: 'avalanche',
  polygon: 'polygon',
  arbitrum: 'arbitrum',
  optimism: 'optimism',
  uniswap: 'uniswap',
  aave: 'aave',
  chainlink: 'chainlink',
  sushiswap: 'sushiswap',
};

const DEX_HINTS = new Set([
  'dex', 'memecoin', 'meme', 'fair-launch', 'solana', 'base', 'ethereum', 'bsc', 'tron', 'avax', 'polygon'
]);

function normalizeId(x) {
  return String(x || '').trim().toLowerCase();
}

function fmtMoney(x, digits = 2) {
  if (x === null || x === undefined || Number.isNaN(Number(x))) return 'n/a';
  return Number(x).toLocaleString(undefined, { minimumFractionDigits: digits, maximumFractionDigits: digits });
}

function fmtAssetPrice(x) {
  if (x === null || x === undefined || Number.isNaN(Number(x))) return 'n/a';
  const n = Number(x);
  const digits = n >= 100 ? 2 : n >= 1 ? 4 : n >= 0.01 ? 6 : 8;
  return n.toLocaleString(undefined, { minimumFractionDigits: digits, maximumFractionDigits: digits });
}

function fmtNum(x, digits = 2) {
  if (x === null || x === undefined || Number.isNaN(Number(x))) return 'n/a';
  return Number(x).toLocaleString(undefined, { minimumFractionDigits: digits, maximumFractionDigits: digits });
}

function pct(x, digits = 2) {
  if (x === null || x === undefined || Number.isNaN(Number(x))) return 'n/a';
  const n = Number(x);
  return `${n >= 0 ? '+' : ''}${n.toFixed(digits)}%`;
}

async function getJSON(url, { headers = {}, timeoutMs = DEFAULT_TIMEOUT_MS } = {}) {
  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), timeoutMs);
  try {
    const resp = await fetchFn(url, { headers, signal: controller.signal });
    if (!resp.ok) throw new Error(`HTTP ${resp.status}`);
    return await resp.json();
  } finally {
    clearTimeout(timer);
  }
}

function parseSources(args) {
  if (!args.sources) return null;
  return new Set(String(args.sources).split(',').map(s => s.trim().toLowerCase()).filter(Boolean));
}

function inferTokenProfile({ coinId, name, symbol, tags = [], marketData = {} }) {
  const tokenText = [coinId, name, symbol, ...(tags || [])].map(normalizeId).join(' ');

  const profile = {
    isDeFi: false,
    isDEXToken: false,
    isDerivativesRelevant: false,
    isL1L2: false,
    isMeme: false,
  };

  profile.isMeme = /meme|doge|shib|pepe|bonk|wif|frog|inu|cat|dog/.test(tokenText);
  profile.isL1L2 = /layer ?1|layer ?2|l1|l2|chain|network|rollup/.test(tokenText) || ['bitcoin', 'ethereum', 'solana', 'avax', 'polygon', 'arbitrum', 'optimism', 'bittensor'].includes(coinId);
  profile.isDeFi = /defi|dex|amm|lending|yield|liquid staking|staking|vault|derivative|perp|oracle/.test(tokenText) || COINGECKO_TO_DEFILLAMA[coinId];
  profile.isDEXToken = /dex|amm|lp|liquidity|swap/.test(tokenText) || profile.isMeme;
  profile.isDerivativesRelevant = /perp|futures|derivative|funding|open interest|oi/.test(tokenText) || profile.isMeme || profile.isL1L2;

  if (!profile.isDeFi && marketData?.tvl && Number(marketData.tvl) > 0) profile.isDeFi = true;
  return profile;
}

function pickRelevantSources({ args, profile }) {
  const requested = parseSources(args);
  const selected = new Set();

  const addIfAllowed = (k, condition = true) => {
    if (!condition) return;
    if (!requested || requested.has(k)) selected.add(k);
  };

  // Baseline market data always:
  addIfAllowed('coingecko');

  // Optional by request or by relevance:
  addIfAllowed('cmc');
  addIfAllowed('defillama', profile.isDeFi);
  addIfAllowed('dexscreener', profile.isDEXToken);
  addIfAllowed('geckoterminal', profile.isDEXToken);
  addIfAllowed('coinglass', profile.isDerivativesRelevant);
  addIfAllowed('exchange', profile.isL1L2 || profile.isDerivativesRelevant);

  // Heavy / optional sources stay opt-in unless explicitly requested.
  if (requested?.has('coinpaprika')) selected.add('coinpaprika');
  if (requested?.has('messari')) selected.add('messari');
  if (requested?.has('lunarcrush')) selected.add('lunarcrush');
  if (requested?.has('etherscan')) selected.add('etherscan');
  if (requested?.has('fundamentals')) selected.add('fundamentals');

  return selected;
}

async function fetchCoinGecko(coinId) {
  return getJSON(
    `https://api.coingecko.com/api/v3/coins/${encodeURIComponent(coinId)}?localization=false&tickers=false&market_data=true&community_data=false&developer_data=false&sparkline=false`
  );
}

const COMMON_COIN_ALIASES = {
  sol: 'solana',
  solana: 'solana',
  btc: 'bitcoin',
  bitcoin: 'bitcoin',
  eth: 'ethereum',
  ethereum: 'ethereum',
  bnb: 'binancecoin',
  avax: 'avalanche-2',
  arb: 'arbitrum',
  op: 'optimism',
  matic: 'polygon',
  pol: 'polygon-ecosystem-token',
  tao: 'bittensor',
  link: 'chainlink',
  xrp: 'ripple',
  ada: 'cardano',
  doge: 'dogecoin',
  shib: 'shiba-inu',
  pepe: 'pepe',
};

async function resolveCoinGeckoId(query) {
  const q = normalizeId(query);
  if (COMMON_COIN_ALIASES[q]) return COMMON_COIN_ALIASES[q];
  try {
    const data = await getJSON(`https://api.coingecko.com/api/v3/search?query=${encodeURIComponent(q)}`);
    const coins = Array.isArray(data.coins) ? data.coins : [];
    if (!coins.length) return q;

    // Best effort ranking: exact symbol > exact name > prefix matches.
    const exactSymbol = coins.find(c => normalizeId(c.symbol) === q);
    if (exactSymbol) return exactSymbol.id;
    const exactName = coins.find(c => normalizeId(c.name) === q);
    if (exactName) return exactName.id;
    const prefixSymbol = coins.find(c => normalizeId(c.symbol).startsWith(q));
    if (prefixSymbol) return prefixSymbol.id;
    const prefixName = coins.find(c => normalizeId(c.name).startsWith(q));
    if (prefixName) return prefixName.id;
    return coins[0].id || q;
  } catch {
    return q;
  }
}

function pickPeerGroup(profile, coinId) {
  const id = normalizeId(coinId);
  if (profile.isMeme) {
    return ['dogecoin', 'shiba-inu', 'pepe', 'bonk', 'dogwifcoin', 'floki'];
  }
  if (profile.isDeFi) {
    return ['uniswap', 'aave', 'chainlink', 'pancakeswap-token', 'curve-dao-token', 'maker', 'synthetix-network-token'];
  }
  if (profile.isL1L2 || /ton|sol|avax|near|apt|sui|sei/.test(id)) {
    return ['solana', 'avalanche-2', 'near', 'aptos', 'sui', 'sei-network', 'injective-protocol', 'ethereum'];
  }
  return ['ethereum', 'solana', 'avalanche-2', 'near', 'aptos', 'sui'];
}

async function fetchPeerSnapshot(peerIds, vs = DEFAULT_VS) {
  const ids = [...new Set(peerIds.filter(Boolean))].join(',');
  if (!ids) return null;
  const data = await getJSON(
    `https://api.coingecko.com/api/v3/simple/price?ids=${encodeURIComponent(ids)}&vs_currencies=${encodeURIComponent(vs)}&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true`
  );
  return data;
}

function summarizeRelativeValuation({ currentMarketCap, currentFDV, peerMap }) {
  const rows = Object.entries(peerMap || {}).map(([id, d]) => ({
    id,
    marketCap: Number(d?.usd_market_cap ?? 0),
    volume24h: Number(d?.usd_24h_vol ?? 0),
  })).filter(r => Number.isFinite(r.marketCap) && r.marketCap > 0);
  if (!rows.length || !currentMarketCap) return null;
  const sorted = rows.map(r => r.marketCap).sort((a, b) => a - b);
  const median = sorted[Math.floor(sorted.length / 2)];
  const ratio = currentMarketCap / median;
  let stance = 'neutral';
  if (ratio < 0.65) stance = 'undervalued';
  else if (ratio > 1.55) stance = 'overvalued';
  return {
    peerMedianMarketCap: median,
    ratio: Number(ratio.toFixed(2)),
    stance,
    peerCount: rows.length,
    currentFDV,
    peerIds: rows.map(r => r.id),
  };
}

async function fetchCoinMarketCap(symbol, vs, key) {
  return getJSON(
    `https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest?symbol=${encodeURIComponent(symbol)}&convert=${encodeURIComponent(vs.toUpperCase())}`,
    { headers: { 'X-CMC_PRO_API_KEY': key, Accept: 'application/json' } }
  );
}

async function fetchBinanceSpot(symbol) {
  const pair = `${String(symbol || '').toUpperCase()}USDT`;
  if (!/^[A-Z0-9]{2,20}USDT$/.test(pair)) return null;
  try {
    const d = await getJSON(`https://api.binance.com/api/v3/ticker/24hr?symbol=${encodeURIComponent(pair)}`);
    return {
      venue: 'binance',
      pair,
      lastPrice: Number(d.lastPrice ?? d.prevClosePrice ?? 0),
      change24h: Number(d.priceChangePercent ?? 0),
      quoteVolume: Number(d.quoteVolume ?? 0),
      baseVolume: Number(d.volume ?? 0),
    };
  } catch {
    return null;
  }
}

async function fetchCoinbaseSpot(symbol) {
  const pair = `${String(symbol || '').toUpperCase()}-USD`;
  if (!/^[A-Z0-9]{2,20}-USD$/.test(pair)) return null;
  try {
    const d = await getJSON(`https://api.coinbase.com/v2/prices/${encodeURIComponent(pair)}/spot`);
    const amount = Number(d?.data?.amount ?? 0);
    return amount ? {
      venue: 'coinbase',
      pair,
      lastPrice: amount,
      change24h: null,
    } : null;
  } catch {
    return null;
  }
}

async function fetchBybitSpot(symbol) {
  const pair = `${String(symbol || '').toUpperCase()}USDT`;
  if (!/^[A-Z0-9]{2,20}USDT$/.test(pair)) return null;
  try {
    const d = await getJSON(`https://api.bybit.com/v5/market/tickers?category=spot&symbol=${encodeURIComponent(pair)}`);
    const row = d?.result?.list?.[0];
    if (!row) return null;
    return {
      venue: 'bybit',
      pair,
      lastPrice: Number(row.lastPrice ?? 0),
      change24h: Number(row.price24hPcnt ?? 0) * 100,
      quoteVolume: Number(row.turnover24h ?? 0),
      baseVolume: Number(row.volume24h ?? 0),
    };
  } catch {
    return null;
  }
}

async function fetchBybitPerpSnapshot(symbol) {
  const pair = `${String(symbol || '').toUpperCase()}USDT`;
  if (!/^[A-Z0-9]{2,20}USDT$/.test(pair)) return null;
  const [ticker, oi, funding] = await Promise.all([
    getJSON(`https://api.bybit.com/v5/market/tickers?category=linear&symbol=${encodeURIComponent(pair)}`).catch(() => null),
    getJSON(`https://api.bybit.com/v5/market/open-interest?category=linear&symbol=${encodeURIComponent(pair)}&intervalTime=5min`).catch(() => null),
    getJSON(`https://api.bybit.com/v5/market/funding/history?category=linear&symbol=${encodeURIComponent(pair)}&limit=1`).catch(() => null),
  ]);
  const t = ticker?.result?.list?.[0];
  if (!t && !oi && !funding) return null;
  return {
    venue: 'bybit',
    pair,
    lastPrice: t ? Number(t.lastPrice ?? 0) : null,
    change24h: t ? Number(t.price24hPcnt ?? 0) * 100 : null,
    openInterest: oi?.result?.list?.[0]?.openInterest ?? oi?.result?.list?.[0]?.openInterestValue ?? null,
    fundingRate: funding?.result?.list?.[0]?.fundingRate ?? null,
  };
}

function summarizeExchangeConsensus(exchanges = []) {
  const rows = (exchanges || []).filter(x => x && Number.isFinite(Number(x.lastPrice)) && Number(x.lastPrice) > 0);
  if (rows.length < 2) return null;
  const prices = rows.map(x => Number(x.lastPrice)).sort((a, b) => a - b);
  const median = prices[Math.floor(prices.length / 2)];
  const spreadPct = ((prices[prices.length - 1] - prices[0]) / median) * 100;
  return {
    venues: rows.map(x => x.venue),
    medianPrice: median,
    minPrice: prices[0],
    maxPrice: prices[prices.length - 1],
    spreadPct: Number(spreadPct.toFixed(2)),
  };
}

async function fetchBinanceKlines(symbol, interval, limit = 100) {
  const pair = `${String(symbol || '').toUpperCase()}USDT`;
  if (!/^[A-Z0-9]{2,20}USDT$/.test(pair)) return null;
  try {
    const data = await getJSON(`https://api.binance.com/api/v3/klines?symbol=${encodeURIComponent(pair)}&interval=${encodeURIComponent(interval)}&limit=${encodeURIComponent(limit)}`);
    if (!Array.isArray(data)) return null;
    return data.map(row => ({
      o: Number(row[1]),
      h: Number(row[2]),
      l: Number(row[3]),
      c: Number(row[4]),
      v: Number(row[5]),
    }));
  } catch {
    return null;
  }
}

async function fetchDeFiLlamaProtocol(slug) {
  return getJSON(`https://api.llama.fi/protocol/${encodeURIComponent(slug)}`);
}

async function fetchDexScreener(coinIdOrSymbol) {
  // Search by token symbol/name and then read top pairs.
  return getJSON(`https://api.dexscreener.com/latest/dex/search/?q=${encodeURIComponent(coinIdOrSymbol)}`);
}

async function fetchGeckoTerminal(coinIdOrSymbol) {
  return getJSON(`https://api.geckoterminal.com/api/v2/search/pools?query=${encodeURIComponent(coinIdOrSymbol)}`,
    { headers: { Accept: 'application/json' } });
}

async function fetchCoinPaprikaSearch(query) {
  return getJSON(`https://api.coinpaprika.com/v1/search?q=${encodeURIComponent(query)}&c=currencies&limit=10`);
}

async function fetchCoinPaprikaTicker(coinId) {
  return getJSON(`https://api.coinpaprika.com/v1/tickers/${encodeURIComponent(coinId)}?quotes=USD`);
}

async function fetchMessariAsset(assetId) {
  return getJSON(`https://data.messari.io/api/v1/assets/${encodeURIComponent(assetId)}/metrics`);
}

async function fetchLunarCrush(symbol, key) {
  return getJSON(
    `https://api.lunarcrush.com/v2?data=assets&symbol=${encodeURIComponent(symbol)}&key=${encodeURIComponent(key)}`
  );
}

function getExplorerApiBase(platform) {
  const p = normalizeId(platform);
  if (p.includes('ethereum')) return 'https://api.etherscan.io/api';
  if (p.includes('binance') || p.includes('bsc')) return 'https://api.bscscan.com/api';
  if (p.includes('polygon')) return 'https://api.polygonscan.com/api';
  if (p.includes('arbitrum')) return 'https://api.arbiscan.io/api';
  if (p.includes('optimism')) return 'https://api-optimistic.etherscan.io/api';
  if (p.includes('base')) return 'https://api.basescan.org/api';
  if (p.includes('avalanche') || p.includes('snow')) return 'https://api.snowtrace.io/api';
  if (p.includes('fantom')) return 'https://api.ftmscan.com/api';
  return null;
}

function findBestContract(platforms = {}) {
  const priority = ['ethereum', 'binance-smart-chain', 'bsc', 'polygon-pos', 'arbitrum-one', 'optimistic-ethereum', 'base', 'avalanche'];
  for (const key of priority) {
    if (platforms[key]) return { platform: key, address: platforms[key] };
  }
  const [platform, address] = Object.entries(platforms).find(([, addr]) => typeof addr === 'string' && addr.startsWith('0x')) || [];
  if (platform && address) return { platform, address };
  return null;
}async function fetchCoinglass(symbol, key) {
  const headers = { Authorization: key };
  const [oi, funding] = await Promise.allSettled([
    getJSON(`https://open-api.coinglass.com/api/pro/v1/futures/open interest?symbol=${encodeURIComponent(symbol)}&interval=5m`, { headers }),
    getJSON(`https://open-api.coinglass.com/api/pro/v1/futures/funding_rate?symbol=${encodeURIComponent(symbol)}`, { headers }),
  ]);
  return {
    oi: oi.status === 'fulfilled' ? oi.value : null,
    funding: funding.status === 'fulfilled' ? funding.value : null,
  };
}

async function fetchCandleSummary(coinId, interval, last = 12) {
  const now = Date.now();
  const spanMs = interval === '15m' ? 15 * 60 * 1000
    : interval === '4h' ? 4 * 60 * 60 * 1000
    : 24 * 60 * 60 * 1000;
  const start = now - spanMs * (last + 4);
  return getJSON('https://api.hyperliquid.xyz/info', {
    headers: { 'Content-Type': 'application/json' },
    timeoutMs: 15000,
  }, {
    type: 'candleSnapshot',
    req: { coin: coinId.toUpperCase(), interval, startTime: start, endTime: now },
  });
}

async function fetchHyperliquidCandles(coinId, interval, last = 20) {
  const now = Date.now();
  const ms = interval === '15m' ? 15 * 60 * 1000 : interval === '4h' ? 4 * 60 * 60 * 1000 : 24 * 60 * 60 * 1000;
  const start = now - ms * (last + 4);
  const body = {
    type: 'candleSnapshot',
    req: { coin: coinId.toUpperCase(), interval, startTime: start, endTime: now },
  };
  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), 15000);
  try {
    const resp = await fetchFn('https://api.hyperliquid.xyz/info', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(body),
      signal: controller.signal,
    });
    if (!resp.ok) throw new Error(`HTTP ${resp.status}`);
    return await resp.json();
  } finally {
    clearTimeout(timer);
  }
}

function clamp(x, min, max) {
  return Math.min(max, Math.max(min, x));
}

function mean(arr) {
  const vals = (arr || []).map(Number).filter(Number.isFinite);
  if (!vals.length) return null;
  return vals.reduce((a, b) => a + b, 0) / vals.length;
}

function stddev(arr) {
  const vals = (arr || []).map(Number).filter(Number.isFinite);
  if (vals.length < 2) return null;
  const m = mean(vals);
  const variance = vals.reduce((acc, x) => acc + ((x - m) ** 2), 0) / vals.length;
  return Math.sqrt(variance);
}

function last(arr) {
  return Array.isArray(arr) && arr.length ? arr[arr.length - 1] : null;
}

function emaArray(values, period) {
  const nums = (values || []).map(Number).filter(Number.isFinite);
  if (!nums.length) return [];
  const k = 2 / (period + 1);
  const out = [nums[0]];
  let ema = nums[0];
  for (let i = 1; i < nums.length; i++) {
    ema = nums[i] * k + ema * (1 - k);
    out.push(ema);
  }
  return out;
}

function rsiLast(closes, period = 14) {
  const nums = (closes || []).map(Number).filter(Number.isFinite);
  if (nums.length <= period) return null;
  let gains = 0;
  let losses = 0;
  for (let i = 1; i <= period; i++) {
    const diff = nums[i] - nums[i - 1];
    if (diff >= 0) gains += diff;
    else losses -= diff;
  }
  let avgGain = gains / period;
  let avgLoss = losses / period;
  for (let i = period + 1; i < nums.length; i++) {
    const diff = nums[i] - nums[i - 1];
    const gain = Math.max(diff, 0);
    const loss = Math.max(-diff, 0);
    avgGain = ((avgGain * (period - 1)) + gain) / period;
    avgLoss = ((avgLoss * (period - 1)) + loss) / period;
  }
  if (avgLoss === 0) return 100;
  const rs = avgGain / avgLoss;
  return 100 - (100 / (1 + rs));
}

function atrLast(candles, period = 14) {
  const rows = Array.isArray(candles) ? candles : [];
  if (rows.length <= period) return null;
  const trs = [];
  for (let i = 1; i < rows.length; i++) {
    const high = Number(rows[i].h ?? rows[i].high ?? 0);
    const low = Number(rows[i].l ?? rows[i].low ?? 0);
    const prevClose = Number(rows[i - 1].c ?? rows[i - 1].close ?? 0);
    const tr = Math.max(high - low, Math.abs(high - prevClose), Math.abs(low - prevClose));
    trs.push(tr);
  }
  let atr = mean(trs.slice(0, period));
  if (!Number.isFinite(atr)) return null;
  for (let i = period; i < trs.length; i++) {
    atr = ((atr * (period - 1)) + trs[i]) / period;
  }
  return atr;
}

function macdLast(closes) {
  const nums = (closes || []).map(Number).filter(Number.isFinite);
  if (nums.length < 26) return null;
  const fast = emaArray(nums, 12);
  const slow = emaArray(nums, 26);
  const macdSeries = nums.map((_, i) => (fast[i] ?? fast[fast.length - 1]) - (slow[i] ?? slow[slow.length - 1]));
  const signalSeries = emaArray(macdSeries, 9);
  const line = last(macdSeries);
  const signal = last(signalSeries);
  if (!Number.isFinite(line) || !Number.isFinite(signal)) return null;
  return { line, signal, hist: line - signal };
}

function vwapLast(candles) {
  const rows = Array.isArray(candles) ? candles : [];
  let pv = 0;
  let vol = 0;
  for (const c of rows) {
    const high = Number(c.h ?? c.high ?? 0);
    const low = Number(c.l ?? c.low ?? 0);
    const close = Number(c.c ?? c.close ?? 0);
    const volume = Number(c.v ?? c.volume ?? 0);
    const tp = (high + low + close) / 3;
    if (Number.isFinite(tp) && Number.isFinite(volume)) {
      pv += tp * volume;
      vol += volume;
    }
  }
  if (!vol) return null;
  return pv / vol;
}

function obvStats(candles) {
  const rows = Array.isArray(candles) ? candles : [];
  if (rows.length < 2) return null;
  const values = [0];
  for (let i = 1; i < rows.length; i++) {
    const prevClose = Number(rows[i - 1].c ?? rows[i - 1].close ?? 0);
    const close = Number(rows[i].c ?? rows[i].close ?? 0);
    const volume = Number(rows[i].v ?? rows[i].volume ?? 0);
    let next = values[values.length - 1];
    if (close > prevClose) next += volume;
    else if (close < prevClose) next -= volume;
    values.push(next);
  }
  const ema = emaArray(values, Math.min(10, Math.max(3, Math.floor(values.length / 4))));
  return { value: last(values), trend: last(values) - (ema.length > 1 ? ema[ema.length - 2] : ema[0]) };
}

function adxLast(candles, period = 14) {
  const rows = Array.isArray(candles) ? candles : [];
  if (rows.length <= period + 1) return null;
  const trs = [];
  const plusDM = [];
  const minusDM = [];
  for (let i = 1; i < rows.length; i++) {
    const high = Number(rows[i].h ?? rows[i].high ?? 0);
    const low = Number(rows[i].l ?? rows[i].low ?? 0);
    const prevHigh = Number(rows[i - 1].h ?? rows[i - 1].high ?? 0);
    const prevLow = Number(rows[i - 1].l ?? rows[i - 1].low ?? 0);
    const prevClose = Number(rows[i - 1].c ?? rows[i - 1].close ?? 0);
    const upMove = high - prevHigh;
    const downMove = prevLow - low;
    plusDM.push(upMove > downMove && upMove > 0 ? upMove : 0);
    minusDM.push(downMove > upMove && downMove > 0 ? downMove : 0);
    trs.push(Math.max(high - low, Math.abs(high - prevClose), Math.abs(low - prevClose)));
  }
  let atr = mean(trs.slice(0, period));
  let pDM = mean(plusDM.slice(0, period));
  let mDM = mean(minusDM.slice(0, period));
  if (!Number.isFinite(atr) || !Number.isFinite(pDM) || !Number.isFinite(mDM) || atr === 0) return null;
  let dxVals = [];
  for (let i = period; i < trs.length; i++) {
    atr = ((atr * (period - 1)) + trs[i]) / period;
    pDM = ((pDM * (period - 1)) + plusDM[i]) / period;
    mDM = ((mDM * (period - 1)) + minusDM[i]) / period;
    if (atr > 0) {
      const plusDI = 100 * (pDM / atr);
      const minusDI = 100 * (mDM / atr);
      const denom = plusDI + minusDI;
      const dx = denom === 0 ? 0 : (100 * Math.abs(plusDI - minusDI) / denom);
      dxVals.push(dx);
    }
  }
  const adx = mean(dxVals.slice(-period));
  if (!Number.isFinite(adx)) return null;
  const plusDI = atr > 0 ? 100 * (pDM / atr) : null;
  const minusDI = atr > 0 ? 100 * (mDM / atr) : null;
  return { adx, plusDI, minusDI };
}

function bollingerLast(closes, period = 20, mult = 2) {
  const nums = (closes || []).map(Number).filter(Number.isFinite);
  if (nums.length < period) return null;
  const window = nums.slice(-period);
  const mid = mean(window);
  const sd = stddev(window);
  if (!Number.isFinite(mid) || !Number.isFinite(sd)) return null;
  return { mid, upper: mid + mult * sd, lower: mid - mult * sd, width: (mult * sd * 2), widthPct: mid ? ((mult * sd * 2) / mid) * 100 : null };
}

function summarizeCandles(candles = []) {
  if (!Array.isArray(candles) || candles.length < 2) return null;
  const first = candles[0];
  const lastCandle = candles[candles.length - 1];
  const highs = candles.map(c => Number(c.h ?? c.high ?? 0));
  const lows = candles.map(c => Number(c.l ?? c.low ?? Infinity));
  const closes = candles.map(c => Number(c.c ?? c.close ?? 0));
  const volumes = candles.map(c => Number(c.v ?? c.volume ?? 0));
  const high = Math.max(...highs);
  const low = Math.min(...lows);
  const change = ((Number(lastCandle.c) - Number(first.o)) / Number(first.o)) * 100;
  const trend = change > 1.2 ? 'bullish' : change < -1.2 ? 'bearish' : 'range';
  const range = high - low;
  const support = low + range * 0.236;
  const resistance = high - range * 0.236;
  const avgClose = mean(closes);
  return {
    start: Number(first.o),
    end: Number(lastCandle.c),
    high,
    low,
    support,
    resistance,
    avgClose,
    changePct: change,
    trend,
    avgVolume: mean(volumes),
    volumeLast: last(volumes),
    range,
  };
}

function resolveTaMode(raw) {
  const mode = normalizeId(raw);
  if (mode === 'auto' || mode === 'full' || mode === 'scalp' || mode === 'swing') return mode;
  return 'auto';
}

function getStyle(profile) {
  if (profile?.isMeme) return 'meme';
  if (profile?.isDeFi) return 'defi';
  if (profile?.isDerivativesRelevant && !profile?.isL1L2) return 'perps';
  if (profile?.isL1L2) return 'major';
  return 'alt';
}

function scoreBias(tf, snap, indicators = {}, profile = {}, mode = 'auto') {
  if (!snap) return { bias: 'neutral', score: 0, signals: [], focus: [] };
  const style = getStyle(profile);
  const tfWeights = mode === 'scalp'
    ? { '15m': 1.35, '4h': 1.0, '1d': 0.65 }
    : mode === 'swing'
      ? { '15m': 0.65, '4h': 1.15, '1d': 1.35 }
      : { '15m': 1.0, '4h': 1.12, '1d': 1.24 };
  const weights = {
    major: { trend: 1.15, momentum: 1.1, mean: 0.65, vol: 0.8, range: 0.55 },
    meme: { trend: 0.8, momentum: 1.05, mean: 1.25, vol: 1.45, range: 1.1 },
    defi: { trend: 1.0, momentum: 1.0, mean: 0.7, vol: 0.9, range: 0.6 },
    perps: { trend: 1.05, momentum: 1.05, mean: 0.6, vol: 0.9, range: 0.7 },
    alt: { trend: 1.0, momentum: 1.0, mean: 0.85, vol: 1.0, range: 0.8 },
  }[style] || { trend: 1.0, momentum: 1.0, mean: 0.8, vol: 1.0, range: 0.8 };

  const close = Number(snap.end);
  let score = clamp(snap.changePct / 3, -2.3, 2.3) * tfWeights[tf] * weights.trend;
  if (snap.trend === 'bullish') score += 0.55 * tfWeights[tf];
  if (snap.trend === 'bearish') score -= 0.55 * tfWeights[tf];

  const signals = [];
  const add = (delta, text) => {
    if (!Number.isFinite(delta) || delta === 0) return;
    score += delta;
    signals.push(text);
  };

  if (Number.isFinite(indicators.ema20) && Number.isFinite(indicators.ema50)) {
    const bull = close > indicators.ema20 && indicators.ema20 > indicators.ema50;
    const bear = close < indicators.ema20 && indicators.ema20 < indicators.ema50;
    if (bull) add(1.1 * weights.trend, `EMA bull (${fmtAssetPrice(indicators.ema20)}/${fmtAssetPrice(indicators.ema50)})`);
    else if (bear) add(-1.1 * weights.trend, `EMA bear (${fmtAssetPrice(indicators.ema20)}/${fmtAssetPrice(indicators.ema50)})`);
    else add(0.15 * Math.sign(close - indicators.ema20 || 0), `EMA mixed (${fmtAssetPrice(indicators.ema20)})`);
  }

  if (Number.isFinite(indicators.vwap)) {
    if (close > indicators.vwap) add(0.8 * weights.trend, `VWAP above (${fmtAssetPrice(indicators.vwap)})`);
    else if (close < indicators.vwap) add(-0.8 * weights.trend, `VWAP below (${fmtAssetPrice(indicators.vwap)})`);
  }

  if (Number.isFinite(indicators.rsi)) {
    if (indicators.rsi >= 60 && style !== 'meme') add(0.55 * weights.momentum, `RSI ${fmtNum(indicators.rsi, 1)} bullish`);
    else if (indicators.rsi <= 40 && style !== 'meme') add(-0.55 * weights.momentum, `RSI ${fmtNum(indicators.rsi, 1)} bearish`);
    else if (indicators.rsi >= 70) add(-0.35 * weights.mean, `RSI ${fmtNum(indicators.rsi, 1)} overbought`);
    else if (indicators.rsi <= 30) add(0.35 * weights.mean, `RSI ${fmtNum(indicators.rsi, 1)} oversold`);
    else signals.push(`RSI ${fmtNum(indicators.rsi, 1)}`);
  }

  if (indicators.macd) {
    if (indicators.macd.hist > 0 && indicators.macd.line > indicators.macd.signal) add(0.75 * weights.momentum, `MACD bull (${fmtMoney(indicators.macd.hist, 4)})`);
    else if (indicators.macd.hist < 0 && indicators.macd.line < indicators.macd.signal) add(-0.75 * weights.momentum, `MACD bear (${fmtMoney(indicators.macd.hist, 4)})`);
    else signals.push(`MACD flat (${fmtMoney(indicators.macd.hist, 4)})`);
  }

  if (Number.isFinite(indicators.adx)) {
    const adxBoost = indicators.adx >= 25 ? 0.4 : indicators.adx >= 20 ? 0.2 : -0.15;
    if (snap.trend === 'bullish') add(adxBoost, `ADX ${fmtNum(indicators.adx, 1)} trend`);
    else if (snap.trend === 'bearish') add(-adxBoost, `ADX ${fmtNum(indicators.adx, 1)} trend`);
    else signals.push(`ADX ${fmtNum(indicators.adx, 1)}`);
  }

  if (Number.isFinite(indicators.volRatio)) {
    if (indicators.volRatio >= 1.5) add((snap.trend === 'bearish' ? -1 : 1) * 0.35 * weights.vol, `Vol x${fmtNum(indicators.volRatio, 2)}`);
    else signals.push(`Vol x${fmtNum(indicators.volRatio, 2)}`);
  }

  if (indicators.bb) {
    const bbPos = (close - indicators.bb.lower) / Math.max(1e-9, indicators.bb.upper - indicators.bb.lower);
    if (bbPos <= 0.15 && indicators.rsi <= 45) add(0.65 * weights.range, `BB lower (${fmtNum(bbPos * 100, 0)}%)`);
    else if (bbPos >= 0.85 && indicators.rsi >= 55) add(-0.65 * weights.range, `BB upper (${fmtNum(bbPos * 100, 0)}%)`);
    else if (indicators.bb.widthPct !== null) signals.push(`BB ${fmtNum(indicators.bb.widthPct, 1)}%`);
  }

  if (indicators.obv) {
    if (indicators.obv.trend > 0) add(0.3 * weights.vol, `OBV up`);
    else if (indicators.obv.trend < 0) add(-0.3 * weights.vol, `OBV down`);
  }

  if (Number.isFinite(indicators.atrPct)) {
    if (indicators.atrPct >= 8) signals.push(`ATR ${fmtNum(indicators.atrPct, 1)}% high`);
    else signals.push(`ATR ${fmtNum(indicators.atrPct, 1)}%`);
  }

  if (indicators.rangePos !== null && indicators.rangePos !== undefined) {
    if (indicators.rangePos > 0.78 && score > 0) score += 0.15;
    if (indicators.rangePos < 0.22 && score < 0) score -= 0.15;
  }

  const bias = score > 0.8 ? 'long' : score < -0.8 ? 'short' : 'neutral';
  const focus = signals.slice(0, mode === 'full' ? 5 : 3);
  return {
    bias,
    score: Number(score.toFixed(2)),
    signals,
    focus,
    style,
  };
}

function buildVerdict(frames, profile, priceData, taMode = 'auto') {
  const weights = { '15m': 0.9, '4h': 1.2, '1d': 1.35 };
  const totals = { long: 0, short: 0, neutral: 0 };
  for (const frame of frames) {
    const tfWeight = weights[frame.tf] ?? 1;
    const dirWeight = 1 + Math.min(1.2, Math.abs(Number(frame.score) || 0) / 2.5);
    const effective = tfWeight * dirWeight;
    totals[frame.bias || 'neutral'] += effective;
  }

  let verdict = 'neutral';
  if (totals.long > totals.short * 1.1 && totals.long >= 1.75) verdict = 'long';
  else if (totals.short > totals.long * 1.1 && totals.short >= 1.75) verdict = 'short';

  const tradeAction = verdict === 'long' ? 'BUY' : verdict === 'short' ? 'SELL' : 'HOLD';
  const styleTag = taMode === 'scalp' ? 'SCALP' : taMode === 'swing' ? 'SWING' : taMode === 'full' ? 'FULL' : 'AUTO';
  const setupLabel = `${styleTag} ${verdict.toUpperCase()}`;

  const riskNotes = [];
  if (profile.isMeme) riskNotes.push('meme coin = high wick risk');
  if (priceData?.market_data?.market_cap?.usd && Number(priceData.market_data.market_cap.usd) < 500000000) riskNotes.push('smaller market cap = higher slippage/volatility');

  return { verdict, tradeAction, setupLabel, riskNotes, totals };
}

function normalizeLayout(raw) {
  const layout = normalizeId(raw);
  if (layout === 'discord' || layout === 'telegram' || layout === 'compact') return layout;
  return 'compact';
}

function renderReport({ result, verdict, tradeAction, setupLabel, riskNotes, warnings, errors, layout = 'compact' }) {
  const p = result.price;
  const s15 = result.ta['15m'];
  const s4h = result.ta['4h'];
  const s1d = result.ta['1d'];
  const titleName = p?.name || result.coinId.toUpperCase();
  const titleSymbol = p?.symbol || result.coinId.toUpperCase();
  const lines = [];
  const bullet = layout === 'telegram' ? '•' : '•';

  lines.push(layout === 'discord' ? `**${titleName} quick read**` : `🔎 ${titleName} quick read`);

  if (p?.current !== null && p?.current !== undefined) {
    lines.push(`${bullet} Price: ~$${fmtAssetPrice(p.current)}`);
    lines.push(`${bullet} 24h change: about ${pct(p.change24h)}`);
    lines.push(`${bullet} Market cap: about $${fmtNum(p.marketCap, 0)}`);
    lines.push(`${bullet} 24h volume: about $${fmtNum(p.volume24h, 0)}`);
  } else {
    lines.push(`${bullet} Price: n/a`);
  }

  if (result.external.bybitPerp?.fundingRate !== undefined && result.external.bybitPerp?.fundingRate !== null) {
    const fr = Number(result.external.bybitPerp.fundingRate);
    const fundingBias = Number.isFinite(fr)
      ? fr > 0
        ? 'slightly long-biased, but not crowded'
        : fr < 0
          ? 'slightly short-biased, but not crowded'
          : 'neutral'
      : 'n/a';
    const fundingText = Number.isFinite(fr) ? `${fr > 0 ? '+' : ''}${fmtNum(fr * 100, 4)}%` : 'n/a';
    lines.push(`${bullet} Perp funding: ${fundingText} -> ${fundingBias}`);
  }

  if (result.external.exchangeConsensus) {
    lines.push(`${bullet} Spot check: ${result.external.exchangeConsensus.venues.join(', ')} aligned | spread ${fmtNum(result.external.exchangeConsensus.spreadPct, 2)}%`);
  } else if (result.external.exchange) {
    lines.push(`${bullet} Spot check: ${result.external.exchange.venue} ${result.external.exchange.pair} | last $${fmtAssetPrice(result.external.exchange.lastPrice)}`);
  }

  if (result.external.relative) {
    lines.push(`${bullet} Relative valuation: ${result.external.relative.stance} vs peers | ratio ${fmtNum(result.external.relative.ratio, 2)} | peer median mcap $${fmtNum(result.external.relative.peerMedianMarketCap, 0)}`);
  }

  const summarizeFrame = (t) => {
    const indicators = t?.indicators || {};
    const focus = (t?.focus || []).slice(0, 2).join(', ');
    const rsi = Number.isFinite(indicators.rsi) ? `RSI ~${fmtNum(indicators.rsi, 1)}` : null;
    const vwapSide = Number.isFinite(indicators.vwap) && Number.isFinite(p?.current)
      ? `price ${p.current < indicators.vwap ? 'below' : 'above'} VWAP`
      : null;
    const macdSide = indicators.macd
      ? indicators.macd.hist > 0
        ? 'MACD positive'
        : indicators.macd.hist < 0
          ? 'MACD negative'
          : 'MACD flat'
      : null;
    const emaSide = focus && /EMA/i.test(focus) ? focus.split(', ')[0] : null;
    const structure = t?.bias === 'short' ? 'bearish structure' : t?.bias === 'long' ? 'bullish structure' : 'mixed-to-weak';
    const tilt = t?.bias === 'short' ? 'NEUTRAL / slight SHORT' : t?.bias === 'long' ? 'NEUTRAL / slight LONG' : 'NEUTRAL';
    const bits = [structure, rsi, macdSide, emaSide, vwapSide].filter(Boolean).join(', ');
    return `${bits}${tilt ? ` -> ${tilt}` : ''}`;
  };

  lines.push('');
  lines.push('**Timeframe bias**');
  lines.push(`${bullet} 15m: ${summarizeFrame(s15)}`);
  lines.push(`${bullet} 4h: ${summarizeFrame(s4h)}`);
  lines.push(`${bullet} 1d: ${summarizeFrame(s1d)}`);

  lines.push('');
  lines.push(`**Read on ${titleName}**`);
  if (verdict === 'short') {
    lines.push(`${bullet} Short-term trend is soft / corrective`);
    lines.push(`${bullet} No strong long signal yet`);
    lines.push(`${bullet} Also not a clean dump setup unless 1d support breaks`);
  } else if (verdict === 'long') {
    lines.push(`${bullet} Short-term trend is constructive / improving`);
    lines.push(`${bullet} No strong short signal yet`);
    lines.push(`${bullet} Momentum favors continuation if support holds`);
  } else {
    lines.push(`${bullet} Short-term trend is mixed`);
    lines.push(`${bullet} No clean breakout or breakdown setup yet`);
    lines.push(`${bullet} Better to wait for confirmation`);
  }

  lines.push('');
  lines.push('**Levels to watch**');
  const supportCandidates = [s15?.support, s4h?.support, s1d?.support].filter(Number.isFinite);
  const resistanceCandidates = [s15?.resistance, s4h?.resistance, s1d?.resistance].filter(Number.isFinite);
  const belowSupports = Number.isFinite(p?.current) ? supportCandidates.filter(v => v < p.current) : supportCandidates.slice();
  const aboveResistances = Number.isFinite(p?.current) ? resistanceCandidates.filter(v => v > p.current) : resistanceCandidates.slice();
  const nearestSupport = belowSupports.length ? Math.max(...belowSupports) : (supportCandidates.length ? Math.max(...supportCandidates) : null);
  const nextSupport = belowSupports.length > 1 ? Math.min(...belowSupports) : null;
  const nearestResistance = aboveResistances.length ? Math.min(...aboveResistances) : (resistanceCandidates.length ? Math.min(...resistanceCandidates) : null);
  const nextResistance = aboveResistances.length > 1 ? Math.max(...aboveResistances) : null;
  if (nearestResistance !== null && nextResistance !== null) {
    lines.push(`${bullet} Resistance: ~${fmtAssetPrice(nearestResistance)}–${fmtAssetPrice(nextResistance)}`);
  } else if (nearestResistance !== null) {
    lines.push(`${bullet} Resistance: ~${fmtAssetPrice(nearestResistance)}`);
  }
  if (nearestSupport !== null && nextSupport !== null) {
    lines.push(`${bullet} Support: ~${fmtAssetPrice(nearestSupport)} then ~${fmtAssetPrice(nextSupport)}`);
  } else if (nearestSupport !== null) {
    lines.push(`${bullet} Support: ~${fmtAssetPrice(nearestSupport)}`);
  }

  lines.push('');
  lines.push('**Bias**');
  lines.push(`${bullet} Overall: ${verdict.toUpperCase()} | Action: ${tradeAction} | Setup: ${setupLabel}`);
  if (verdict === 'short') {
    lines.push(`${bullet} Trading tilt: slight SHORT on the 4h until price reclaims resistance`);
  } else if (verdict === 'long') {
    lines.push(`${bullet} Trading tilt: slight LONG on the 4h while support holds`);
  } else {
    lines.push(`${bullet} Trading tilt: wait for a better confirmation candle`);
  }
  lines.push(`${bullet} Confidence: ${result.confidence}%`);
  if (result.tradePlan) {
    lines.push(`${bullet} Entry/stop/target: ${fmtAssetPrice(result.tradePlan.entry)} / ${fmtAssetPrice(result.tradePlan.stop)} / ${fmtAssetPrice(result.tradePlan.target)}${result.tradePlan.rr ? ` | RR ${result.tradePlan.rr}` : ''}`);
  }

  if (riskNotes.length) lines.push(`${bullet} Risk: ${riskNotes.join('; ')}`);
  if (warnings.length) lines.push(`${bullet} Warnings: ${warnings.join(' | ')}`);
  if (errors.length) lines.push(`${bullet} Errors: ${errors.join(' | ')}`);
  lines.push(`${bullet} Sources: ${result.sourcesUsed?.length ? result.sourcesUsed.join(', ') : 'n/a'}`);
  lines.push(`${bullet} Links: TV ${result.links.tradingview} | CG ${result.links.coingecko}`);
  if (result.links.defillama) lines.push(`  DL ${result.links.defillama}`);
  if (result.links.dexscreener) lines.push(`  DX ${result.links.dexscreener}`);
  return lines.join('\n');
}

export default async function cryptoAnalysis({ args = {}, env = {} } = {}) {
  const mergedEnv = { ...process.env, ...env };
  const userInput = normalizeId(args.coin_id || args.symbol || args[0]);
  if (!userInput) return '❌ Please provide a coin id or symbol (e.g. tao, bitcoin, solana).';

  const vs = normalizeId(args.vs_currency || args.vs || DEFAULT_VS);
  const includeDerivatives = args.include_derivatives === true || String(args.include_derivatives).toLowerCase() === 'true';
  const requestedSources = parseSources(args);

  const resolvedCoinId = await resolveCoinGeckoId(userInput);
  const coinId = resolvedCoinId;
  const baseProfile = inferTokenProfile({ coinId: resolvedCoinId, name: resolvedCoinId, symbol: resolvedCoinId.toUpperCase(), tags: [] });
  const sources = pickRelevantSources({ args, profile: baseProfile });
  const cmcKeyAvailable = Boolean(mergedEnv.COINMARKETCAP_KEY);
  if (!cmcKeyAvailable) sources.delete('cmc');

  const errors = [];
  const warnings = [];
  const result = {
    coinId,
    vs,
    price: null,
    profile: baseProfile,
    sourcesUsed: [...sources],
    ta: {},
    external: {},
    verdict: null,
  };

  // 1) CoinGecko baseline
  let cg = null;
  if (sources.has('coingecko')) {
    try {
      cg = await fetchCoinGecko(coinId);
      const md = cg.market_data || {};
      result.price = {
        source: 'coingecko',
        name: cg.name,
        symbol: cg.symbol,
        current: md.current_price?.[vs] ?? md.current_price?.usd ?? null,
        marketCap: md.market_cap?.[vs] ?? md.market_cap?.usd ?? null,
        volume24h: md.total_volume?.[vs] ?? md.total_volume?.usd ?? null,
        change24h: md.price_change_percentage_24h ?? null,
        fdv: md.fully_diluted_valuation?.[vs] ?? md.fully_diluted_valuation?.usd ?? null,
        circulating: md.circulating_supply ?? null,
        totalSupply: md.total_supply ?? null,
        ath: md.ath?.[vs] ?? md.ath?.usd ?? null,
        atl: md.atl?.[vs] ?? md.atl?.usd ?? null,
        platforms: cg.platforms || {},
      };
      result.profile = inferTokenProfile({ coinId, name: cg.name, symbol: cg.symbol, tags: cg.categories || [], marketData: md });
      const refreshedSources = [...pickRelevantSources({ args, profile: result.profile })];
      if (!mergedEnv.COINMARKETCAP_KEY) {
        const idx = refreshedSources.indexOf('cmc');
        if (idx !== -1) refreshedSources.splice(idx, 1);
      }
      result.sourcesUsed = refreshedSources;
    } catch (e) {
      errors.push(`CoinGecko: ${e.message}`);
    }
  }

  // 2a) Quick exchange spot / perps check (lightweight, no-key)
  if (sources.has('exchange')) {
    try {
      const symbol = (cg?.symbol || coinId).toUpperCase();
      const spotChecks = [];
      const binanceSpot = await fetchBinanceSpot(symbol);
      if (binanceSpot) spotChecks.push(binanceSpot);
      const bybitSpot = await fetchBybitSpot(symbol);
      if (bybitSpot) spotChecks.push(bybitSpot);
      const coinbaseSpot = await fetchCoinbaseSpot(symbol);
      if (coinbaseSpot) spotChecks.push(coinbaseSpot);
      if (spotChecks.length) {
        result.external.exchanges = spotChecks;
        result.external.exchange = spotChecks[0];
        result.external.exchangeConsensus = summarizeExchangeConsensus(spotChecks);
      }
      if (includeDerivatives || result.profile.isDerivativesRelevant) {
        const perp = await fetchBybitPerpSnapshot(symbol);
        if (perp) result.external.bybitPerp = perp;
      }
    } catch (e) {
      warnings.push(`Exchange quick fetch failed: ${e.message}`);
    }
  }

  // 2b) CoinMarketCap optional enrichment / fallback
  if (sources.has('cmc')) {
    const cmcKey = mergedEnv.COINMARKETCAP_KEY;
    if (cmcKey) {
      try {
        const symbol = (cg?.symbol || coinId).toUpperCase();
        const cmc = await fetchCoinMarketCap(symbol, vs, cmcKey);
        const data = cmc?.data?.[symbol] || Object.values(cmc?.data || {})[0];
        const q = data?.quote?.[vs.toUpperCase()];
        if (q) {
          if (!result.price?.current) {
            result.price = {
              source: 'coinmarketcap',
              name: data.name,
              symbol: data.symbol,
              current: q.price,
              marketCap: q.market_cap,
              volume24h: q.volume_24h,
              change24h: q.percent_change_24h,
              fdv: q.fully_diluted_market_cap ?? null,
              circulating: data.circulating_supply ?? null,
              totalSupply: data.total_supply ?? null,
              ath: data.ath ?? null,
              atl: data.atl ?? null,
            };
          } else {
            result.external.cmc = {
              rank: data.cmc_rank,
              marketCapRank: data.market_cap_rank,
              category: data.category,
              supply: data.total_supply,
            };
          }
        }
      } catch (e) {
        errors.push(`CoinMarketCap: ${e.message}`);
      }
    } else {
      warnings.push('CoinMarketCap skipped: COINMARKETCAP_KEY not set');
    }
  }

  // 2c) Relative valuation vs peers / category
  if (result.price?.marketCap) {
    try {
      const peerIds = pickPeerGroup(result.profile, coinId);
      const peerData = await fetchPeerSnapshot(peerIds, vs);
      const relative = summarizeRelativeValuation({
        currentMarketCap: Number(result.price.marketCap),
        currentFDV: Number(result.price.fdv || 0),
        peerMap: peerData,
      });
      if (relative) {
        result.external.relative = relative;
      }
    } catch (e) {
      warnings.push(`Relative valuation failed: ${e.message}`);
    }
  }

  // 3) DeFiLlama if relevant
  if ((!result.price || !result.price.current) && sources.has('coinpaprika')) {
    try {
      const search = await fetchCoinPaprikaSearch(userInput);
      const candidate = search?.currencies?.[0] || search?.currencies?.find?.(c => normalizeId(c.name) === userInput) || null;
      const paprikaId = candidate?.id || candidate?.coin_id || candidate?.slug || null;
      if (paprikaId) {
        const ticker = await fetchCoinPaprikaTicker(paprikaId);
        const q = ticker?.quotes?.USD || ticker?.quotes?.[vs.toUpperCase()] || null;
        if (q) {
          result.external.coinpaprika = {
            id: paprikaId,
            name: ticker?.name || candidate?.name || userInput,
            symbol: ticker?.symbol || candidate?.symbol || userInput.toUpperCase(),
            rank: ticker?.rank ?? null,
          };
          result.price = {
            source: 'coinpaprika',
            name: ticker?.name || candidate?.name || userInput,
            symbol: ticker?.symbol || candidate?.symbol || userInput.toUpperCase(),
            current: q.price ?? null,
            marketCap: q.market_cap ?? null,
            volume24h: q.volume_24h ?? null,
            change24h: q.percent_change_24h ?? null,
            fdv: ticker?.fully_diluted_market_cap ?? null,
            circulating: ticker?.circulating_supply ?? null,
            totalSupply: ticker?.total_supply ?? null,
            ath: ticker?.quotes?.USD?.ath_price ?? null,
            atl: ticker?.quotes?.USD?.ath_date ?? null,
          };
        }
      }
    } catch (e) {
      warnings.push(`CoinPaprika failed: ${e.message}`);
    }
  }


  // 4) DEX analytics when token likely trades on DEXs
  if (sources.has('dexscreener')) {
    try {
      const dx = await fetchDexScreener(cg?.symbol || coinId);
      const pair = dx.pairs?.[0];
      if (pair) {
        result.external.dexscreener = {
          chainId: pair.chainId,
          dexId: pair.dexId,
          pairAddress: pair.pairAddress,
          priceUsd: pair.priceUsd,
          liquidityUsd: pair.liquidity?.usd,
          volume24h: pair.volume?.h24,
          fdv: pair.fdv,
          marketCap: pair.marketCap,
          txns24h: pair.txns?.h24,
          url: pair.url,
        };
      }
    } catch (e) {
      warnings.push(`DexScreener failed: ${e.message}`);
    }
  }

  if (sources.has('geckoterminal')) {
    try {
      const gt = await fetchGeckoTerminal(cg?.symbol || coinId);
      const pool = gt.data?.[0];
      if (pool) {
        result.external.geckoterminal = {
          chainId: pool.relationships?.network?.data?.id || null,
          poolAddress: pool.id,
          attributes: pool.attributes ? {
            name: pool.attributes.name,
            baseTokenPriceUsd: pool.attributes.base_token_price_usd,
            quoteTokenPriceUsd: pool.attributes.quote_token_price_usd,
            reserveInUsd: pool.attributes.reserve_in_usd,
            volume24h: pool.attributes.volume_usd?.h24,
          } : null,
        };
      }
    } catch (e) {
      warnings.push(`GeckoTerminal failed: ${e.message}`);
    }
  }

  // 5) Coinglass only when relevant + key present
  if (includeDerivatives && sources.has('coinglass')) {
    const key = mergedEnv.COINGLASS_KEY;
    if (key) {
      try {
        const cgx = await fetchCoinglass((cg?.symbol || coinId).toUpperCase(), key);
        result.external.coinglass = {
          oi: cgx.oi?.data ?? null,
          funding: cgx.funding?.data ?? null,
        };
      } catch (e) {
        warnings.push(`Coinglass failed: ${e.message}`);
      }
    } else {
      warnings.push('Coinglass skipped: COINGLASS_KEY not set');
    }
  }

  // 5b) Optional fundamentals / sentiment / on-chain
  if (sources.has('messari')) {
    try {
      const assetId = cg?.symbol ? normalizeId(cg.symbol) : coinId;
      const ms = await fetchMessariAsset(assetId);
      const m = ms?.data?.market_data || ms?.data?.metrics?.market_data || {};
      result.external.messari = {
        assetId,
        priceUsd: m.price_usd ?? null,
        marketCapUsd: m.marketcap_usd ?? null,
        volumeLast24h: m.volume_last_24_hours ?? null,
        fdv: m.fully_diluted_market_cap_usd ?? null,
        supply: ms?.data?.supply || null,
        chain: ms?.data?.profile?.blockchain || null,
      };
    } catch (e) {
      warnings.push(`Messari failed: ${e.message}`);
    }
  }

  if (sources.has('lunarcrush')) {
    const key = mergedEnv.LUNARCRUSH_KEY || mergedEnv.LUNARCRUSH_API_KEY;
    if (key) {
      try {
        const lc = await fetchLunarCrush((cg?.symbol || coinId).toUpperCase(), key);
        const d = lc?.data?.[0] || lc?.data || lc;
        result.external.lunarcrush = {
          galaxyScore: d?.galaxy_score ?? null,
          altRank: d?.alt_rank ?? null,
          socialVolume: d?.social_volume ?? null,
          socialScore: d?.social_score ?? null,
          sentiment: d?.sentiment ?? null,
          priceCorrelation: d?.price_correlation_rank ?? null,
        };
      } catch (e) {
        warnings.push(`LunarCrush failed: ${e.message}`);
      }
    } else {
      warnings.push('LunarCrush skipped: LUNARCRUSH_KEY not set');
    }
  }

  if (sources.has('etherscan') && cg?.platforms) {
    const contract = findBestContract(cg.platforms);
    if (contract) {
      const key = mergedEnv.ETHERSCAN_KEY || mergedEnv.BSCSCAN_KEY || mergedEnv.POLYGONSCAN_KEY || mergedEnv.ARBISCAN_KEY || mergedEnv.BASESCAN_KEY;
      const baseUrl = getExplorerApiBase(contract.platform);
      if (key && baseUrl) {
        try {
          const chainKey = mergedEnv.ETHERSCAN_KEY || mergedEnv.BSCSCAN_KEY || mergedEnv.POLYGONSCAN_KEY || mergedEnv.ARBISCAN_KEY || mergedEnv.BASESCAN_KEY;
          const ex = await fetchEtherscanContract(contract.address, chainKey, baseUrl);
          const holdersPayload = ex.holders?.result ?? ex.holders;
          const supplyPayload = ex.supply?.result ?? ex.supply;
          const sourcePayload = Array.isArray(ex.source?.result) ? ex.source.result[0] : ex.source?.result;
          result.external.onchain = {
            platform: contract.platform,
            contract: contract.address,
            holderCount: holdersPayload?.tokenholdercount ?? holdersPayload ?? null,
            totalSupplyRaw: supplyPayload ?? null,
            verified: sourcePayload?.SourceCode ? true : false,
            compilerVersion: sourcePayload?.CompilerVersion ?? null,
          };
        } catch (e) {
          warnings.push(`Explorer API failed: ${e.message}`);
        }
      }
    }
  }

  const taMode = resolveTaMode(args.ta_mode || args.ta || args.mode || mergedEnv.HERMES_TA_MODE || 'auto');
  result.taMode = taMode;

  // 6) Hyperliquid technical snapshot
  const tfList = ['15m', '4h', '1d'];
  for (const tf of tfList) {
    let candles = [];
    let taSource = 'hyperliquid';
    try {
      const raw = await fetchHyperliquidCandles((cg?.symbol || coinId).toUpperCase(), tf, tf === '1d' ? 30 : tf === '4h' ? 25 : 50);
      candles = Array.isArray(raw) ? raw : raw?.data?.candles ?? raw?.candles ?? raw?.result ?? raw?.candleSnapshot ?? [];
      if (!Array.isArray(candles) || candles.length < 10) throw new Error('insufficient candles');
    } catch (e) {
      warnings.push(`Hyperliquid ${tf} failed: ${e.message}`);
      const intervalMap = { '15m': '15m', '4h': '4h', '1d': '1d' };
      const fallback = await fetchBinanceKlines((cg?.symbol || coinId).toUpperCase(), intervalMap[tf], tf === '1d' ? 30 : tf === '4h' ? 25 : 50);
      if (Array.isArray(fallback) && fallback.length >= 10) {
        candles = fallback;
        taSource = 'binance';
      }
    }
    const snap = summarizeCandles(candles);
    const closes = candles.map(c => Number(c.c ?? c.close ?? 0)).filter(Number.isFinite);
    const indicators = snap ? {
      ema20: last(emaArray(closes, 20)),
      ema50: last(emaArray(closes, 50)),
      rsi: rsiLast(closes, 14),
      macd: macdLast(closes),
      atr: atrLast(candles, 14),
      atrPct: snap.end ? (atrLast(candles, 14) / snap.end) * 100 : null,
      vwap: vwapLast(candles),
      bb: bollingerLast(closes, 20, 2),
      adx: adxLast(candles, 14)?.adx ?? null,
      volRatio: snap.avgVolume && snap.volumeLast ? snap.volumeLast / snap.avgVolume : null,
      obv: obvStats(candles),
      rangePos: snap.range ? (snap.end - snap.low) / snap.range : null,
    } : {};
    result.ta[tf] = snap ? { ...snap, taSource, indicators, ...scoreBias(tf, snap, indicators, result.profile, taMode) } : { bias: 'neutral', score: 0, signals: [], focus: [], taSource };
  }

  // 7) Final verdict
  const biases = tfList.map(tf => ({ tf, ...(result.ta[tf] || { bias: 'neutral', score: 0 }) }));
  const { verdict, tradeAction, setupLabel, riskNotes } = buildVerdict(biases, result.profile, result.price, taMode);
  result.verdict = verdict;
  result.tradeAction = tradeAction;
  result.setupLabel = setupLabel;
  result.riskNotes = riskNotes;

  const scoreSum = biases.reduce((a, b) => a + (Number(b.score) || 0), 0);
  const coverageCount = [cg, result.external.coinpaprika, result.external.defillama, result.external.dexscreener, result.external.geckoterminal, result.external.coinglass, result.external.messari, result.external.lunarcrush, result.external.onchain].filter(Boolean).length;
  result.confidence = Math.max(20, Math.min(95, Math.round(50 + Math.abs(scoreSum) * 7 + coverageCount * 2)));

  const s15 = result.ta['15m'];
  const s4h = result.ta['4h'];
  const s1d = result.ta['1d'];
  const current = result.price?.current;
  let tradePlan = null;
  if (verdict === 'long' && s15?.support && s4h?.resistance) {
    tradePlan = {
      entry: s15.support,
      stop: s15.low ? s15.low * 0.995 : s15.support * 0.985,
      target: s4h.resistance,
      rr: current ? Number(((s4h.resistance - s15.support) / Math.max(0.0000001, s15.support - (s15.low ? s15.low * 0.995 : s15.support * 0.985))).toFixed(2)) : null,
    };
  } else if (verdict === 'short' && s15?.resistance && s4h?.support) {
    tradePlan = {
      entry: s15.resistance,
      stop: s15.high ? s15.high * 1.005 : s15.resistance * 1.015,
      target: s4h.support,
      rr: current ? Number(((s15.resistance - s4h.support) / Math.max(0.0000001, (s15.high ? s15.high * 1.005 : s15.resistance * 1.015) - s15.resistance)).toFixed(2)) : null,
    };
  } else if (s15?.support && s15?.resistance) {
    tradePlan = {
      entry: current ?? s15.end ?? null,
      stop: s15.support,
      target: s15.resistance,
      rr: null,
    };
  }
  result.tradePlan = tradePlan;

  const riskFlags = [];
  const mcap = result.price?.marketCap ? Number(result.price.marketCap) : null;
  const fdv = result.price?.fdv ? Number(result.price.fdv) : null;
  const vol = result.price?.volume24h ? Number(result.price.volume24h) : null;
  const liq = result.external.dexscreener?.liquidityUsd ? Number(result.external.dexscreener.liquidityUsd) : null;
  if (result.external.bybitPerp?.fundingRate !== null && result.external.bybitPerp?.fundingRate !== undefined) {
    const fr = Number(result.external.bybitPerp.fundingRate);
    if (Number.isFinite(fr)) {
      if (fr > 0.0005) riskFlags.push('perp funding elevated');
      if (fr < -0.0005) riskFlags.push('perp funding deeply negative');
    }
  }
  if (result.external.exchangeConsensus?.spreadPct !== null && result.external.exchangeConsensus?.spreadPct !== undefined) {
    const spread = Number(result.external.exchangeConsensus.spreadPct);
    if (Number.isFinite(spread) && spread > 0.4) riskFlags.push('cross-exchange price spread elevated');
  }
  if (mcap && fdv && fdv > mcap * 4) riskFlags.push('FDV much higher than market cap');
  if (mcap && vol && vol < mcap * 0.02) riskFlags.push('24h volume is thin vs market cap');
  if (mcap && liq && liq < mcap * 0.01) riskFlags.push('DEX liquidity is thin vs market cap');
  if (result.external.onchain && result.external.onchain.verified === false) riskFlags.push('contract/source code not verified');
  if (result.external.lunarcrush?.sentiment && /bear/i.test(String(result.external.lunarcrush.sentiment))) riskFlags.push('social sentiment weak');
  result.riskFlags = riskFlags;

  // 8) Helpful public links for manual verification
  const symbol = (cg?.symbol || coinId).toUpperCase();
  result.links = {
    tradingview: `https://www.tradingview.com/symbols/${symbol === 'TAO' ? 'BINANCE-TAO' : `BINANCE-${symbol}`}/`,
    coingecko: `https://www.coingecko.com/en/coins/${coinId}`,
    coinglass: `https://www.coinglass.com/`,
    defillama: result.external.defillama?.slug ? `https://defillama.com/protocol/${result.external.defillama.slug}` : null,
    dexscreener: result.external.dexscreener?.url ?? null,
  };

  const layout = normalizeLayout(args.layout || mergedEnv.HERMES_LAYOUT || mergedEnv.HERMES_PLATFORM || mergedEnv.DISCORD_LAYOUT || mergedEnv.TELEGRAM_LAYOUT);
  return renderReport({ result, verdict, tradeAction, setupLabel, riskNotes, warnings, errors, layout });
}

async function cli() {
  const argv = process.argv.slice(2);
  const coinId = normalizeId(argv[0]);
  const args = {};
  for (let i = 1; i < argv.length; i++) {
    const k = argv[i];
    const v = argv[i + 1];
    if (k.startsWith('--')) {
      args[k.slice(2)] = v;
      i++;
    }
  }
  args.coin_id = coinId;
  const out = await cryptoAnalysis({ args, env: process.env });
  console.log(out);
}

if (import.meta.url === `file://${process.argv[1]}`) {
  cli().catch(err => {
    console.error(err);
    process.exit(1);
  });
}
