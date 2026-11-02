**Stat check first:** no GitHub research shows "detailed README = 50% more contributions." Real GitHub Open Source Survey (2017) found incomplete docs is contributors' #1 pain point — but no 50% figure attached. That number's likely a blog's misremember, not GitHub's own data.

**Judgment call:** roadmap + contributors wall sections go stale fast, cost upkeep. Writing them anyway since you asked — kept each section real, not padded filler.

**Caveat:** I don't have your actual source, so API calls below (`NewFromString`, `Add`, `Mul`, `Div`, `Round`) are illustrative, modeled on typical fixed-point decimal Go APIs. Swap for your real exported names before commit.

Here's the README:

```markdown
<div align="center">
  <h1>Tessarine</h1>
  <p><strong>Fixed-point decimal arithmetic for money, without float rounding errors.</strong></p>

  <a href="https://github.com/samber/tessarine/actions"><img src="https://github.com/samber/tessarine/workflows/CI/badge.svg" alt="CI"></a>
  <a href="https://pkg.go.dev/github.com/samber/tessarine"><img src="https://pkg.go.dev/badge/github.com/samber/tessarine.svg" alt="Go Reference"></a>
  <a href="https://goreportcard.com/report/github.com/samber/tessarine"><img src="https://goreportcard.com/badge/github.com/samber/tessarine" alt="Go Report Card"></a>
  <a href="https://github.com/samber/tessarine/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License"></a>
  <a href="https://github.com/samber/tessarine/stargazers"><img src="https://img.shields.io/github/stars/samber/tessarine?style=social" alt="GitHub stars"></a>
</div>

---

## Table of contents

- [Why Tessarine](#why-tessarine)
- [Install](#install)
- [Quick start](#quick-start)
- [Architecture](#architecture)
- [FAQ](#faq)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)

## Why Tessarine

`float64` cannot represent most decimal fractions exactly (`0.1 + 0.2 != 0.3`). For money, that error compounds across every add, multiply, and rounding step. Tessarine represents amounts as a scaled integer (mantissa × 10⁻ˢᶜᵃˡᵉ) instead, so arithmetic stays exact until you explicitly choose to round.

- **No float in the arithmetic path.** Every operation stays in scaled-integer space.
- **Explicit rounding, no silent default.** Division and rescale always take a `RoundingMode` argument.
- **Overflow-safe.** Operations that would overflow `int64` promote internally to `big.Int` instead of wrapping silently.
- **Immutable values.** Every method returns a new `Decimal`; safe to share across goroutines.
- **Zero dependencies.**

## Install

```bash
go get github.com/samber/tessarine
```

## Quick start

### Basic arithmetic

```go
price, err := tessarine.NewFromString("19.99")
if err != nil {
    log.Fatal(err)
}

taxRate, _ := tessarine.NewFromString("0.0825")
total := price.Add(price.Mul(taxRate))

fmt.Println(total.Round(2, tessarine.RoundHalfEven)) // 21.64
```

### Division with explicit rounding

Division can't always land on an exact scale, so it takes a target precision and a rounding mode instead of guessing:

```go
bill := tessarine.NewFromInt64(1000, 2) // 10.00
split, err := bill.Div(tessarine.NewFromInt(3), 2, tessarine.RoundHalfEven)
if err != nil {
    log.Fatal(err)
}

fmt.Println(split) // 3.33
```

### JSON and SQL marshaling

```go
type LineItem struct {
    SKU   string            `json:"sku"`
    Price tessarine.Decimal `json:"price"` // implements MarshalJSON, Scan, Value
}

data, _ := json.Marshal(LineItem{SKU: "SKU-1", Price: price})
// {"sku":"SKU-1","price":"19.99"}
```

## Architecture

Tessarine stores each `Decimal` as an `int64` mantissa plus an `int32` scale (`value = mantissa * 10^-scale`), the same shape as SQL's `NUMERIC` and most database decimal columns.

**Why not `math/big.Rat`?** `big.Rat` is exact but has no concept of "2 decimal places" — every value would need explicit rescaling before formatting or comparing, which is exactly the footgun this library exists to remove.

**Overflow handling.** Every arithmetic op checks for `int64` overflow before it happens. On the rare path where it would overflow (large multiplications, mostly), the operation transparently redoes the computation with `big.Int` and downgrades back to `int64` only if the result fits. You never get a silently wrapped value.

**Rounding.** There is no default rounding mode anywhere in the API. `Round`, `Div`, and `Rescale` all require you to pass one (`RoundHalfEven`, `RoundHalfUp`, `RoundDown`, `RoundUp`, `RoundCeiling`, `RoundFloor`). This is deliberate: silent rounding defaults are how ledgers drift over millions of transactions.

**Currency-agnostic by design.** `Decimal` is a pure number, not a `Money` type — it doesn't carry a currency code. Adding `1.00` USD to `1.00` EUR won't error, because Tessarine has no idea either is a currency. If you need that guardrail, wrap `Decimal` in your own `Money{Amount Decimal; Currency string}` (see [Roadmap](#roadmap) for a built-in version).

**Package layout.** Single package, no internal sub-packages, no reflection in the hot path, no third-party dependencies.

## FAQ

**Why not just use `float64`?** Binary floats can't represent most base-10 fractions exactly. `0.1 + 0.2 == 0.3` is false in `float64`. For money, that's not a rounding curiosity — it's a ledger that doesn't reconcile.

**Why not `shopspring/decimal` or `cockroachdb/apd`?** Both are solid, arbitrary-precision libraries. Tessarine trades arbitrary precision for a narrower, currency-shaped API: fixed `int64`-backed scale for the common case, explicit rounding modes everywhere, and `big.Int` only as an overflow escape hatch rather than the default representation. Pick Tessarine if your amounts are currency-shaped (2-4 decimal places); pick `apd` if you need arbitrary-precision scientific decimal.

**Is this multi-currency safe?** Not on its own — see [Architecture](#architecture). It's a number type, not a currency-aware `Money` type.

**Is `Decimal` safe for concurrent use?** Yes. Every value is immutable; methods return new values.

**What's the default rounding mode?** There isn't one. Any operation that needs to round requires you to pass a `RoundingMode` explicitly.

**What happens on overflow?** Internally promotes to `big.Int` for that operation. No silent wraparound, no panic.

**Minimum Go version?** Go 1.21+.

## Roadmap

No committed dates — tracked in [GitHub Discussions](https://github.com/samber/tessarine/discussions). Order isn't priority order.

- [ ] `Money` type wrapping `Decimal` with an ISO 4217 currency code, so adding USD to EUR is a compile-time or runtime error instead of a silent bug
- [ ] `database/sql` `Scanner`/`Valuer` conformance tests against Postgres `NUMERIC` and MySQL `DECIMAL`
- [ ] Optional arbitrary-precision mode for non-currency use cases
- [ ] Published benchmarks vs. `shopspring/decimal` and `cockroachdb/apd`

## Contributing

Bug reports, benchmarks, and PRs welcome — see [CONTRIBUTING.md](CONTRIBUTING.md). Issues tagged [`good first issue`](https://github.com/samber/tessarine/labels/good%20first%20issue) are a good starting point.

### Contributors

<!-- ALL-CONTRIBUTORS-LIST:START -->
<!-- Generated by https://allcontributors.org — comment "@all-contributors please add @user for code" on any issue/PR to add someone -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

## License

MIT — see [LICENSE](LICENSE).
```

Next: swap the `samber/tessarine` badge URLs and the `NewFromString`/`Add`/`Mul`/`Div`/`Round` calls for your real exported names, then run `go doc ./...` to confirm every signature in the README actually matches.