const skill = require('./scripts/crypto_analysis.mjs');
(async () => {
  const result = await skill({
    args: { coin_id: 'tao', vs_currency: 'usd', include_derivatives: false },
    env: {}
  });
  console.log(result);
})();
