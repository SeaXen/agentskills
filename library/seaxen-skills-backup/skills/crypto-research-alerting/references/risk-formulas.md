# Risk Formulas

## Core

- Risk amount = account_equity × risk_percent
- Stop distance = abs(entry - stop)
- Position size (units) = risk_amount / stop_distance
- Position notional = position_size × entry

## Reward / Risk

For each target:
- reward_per_unit = abs(target - entry)
- R multiple = reward_per_unit / stop_distance

## Example

- Equity: 10,000
- Risk: 1% = 100
- Entry: 105
- Stop: 100
- Stop distance: 5
- Size: 100 / 5 = 20 units
- Notional: 20 × 105 = 2,100

## Notes

- Lower risk for illiquid assets
- Reduce size further when slippage is likely
- Never approve a plan with undefined stop distance
