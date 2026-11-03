# Trade verdict labels

Session learning: keep the core verdict and the trade label separate.

## Rendering contract
- `verdict`: `LONG`, `SHORT`, or `NEUTRAL`
- `action`: `BUY`, `SELL`, or `HOLD`
- `setup`: `SCALP LONG`, `SWING SHORT`, `FULL NEUTRAL`, etc.

## When to use each
- Use `verdict` for the analytical bias.
- Use `action` for the one-line trading instruction.
- Use `setup` to encode the selected TA mode and direction.

## Example
- `Verdict: SHORT | Action: SELL | Setup: SWING SHORT`

## Notes
- This keeps Discord/Telegram output fast to scan.
- Prefer short labels over explanatory prose in chat layouts.
