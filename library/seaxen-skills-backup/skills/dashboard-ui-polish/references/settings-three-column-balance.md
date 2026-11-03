# Settings page — three-column balance and empty right column

When the user reports the **right column is empty** or **Discord/notifications are hard to find**:

1. **Rebalance by height**, not card count — move alert integrations into column 3.
2. **Order column 3:** status strip (Discord/Telegram/webhook chips) → Discord block → other channels → shortcuts → data/reset.
3. **Remove** subtitle clutter under the page title if the user asked for compact chrome (no "Personal preferences. Saved locally…").
4. **Verify** with browser scroll + `document.body.innerText` includes `DISCORD` and alert-channel labels.

TradingX reference: `nextjs-dual-deploy/references/tradingx-settings-alerts-perf-social.md`.