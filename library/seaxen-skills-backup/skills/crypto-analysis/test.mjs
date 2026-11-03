import analysis from './scripts/crypto_analysis.mjs';
const result = await analysis({ args: { coin_id: 'tao', vs_currency: 'usd', include_derivatives: false }, env: {} });
console.log(result);
