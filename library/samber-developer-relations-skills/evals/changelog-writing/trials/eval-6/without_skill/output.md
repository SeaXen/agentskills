# Wexley 3.4.0 — Release Notes

*2026-09-18*

```
Two ledgers, one truth—
reconcile() finds every gap.
Sleep well tonight, ops.
```

Somewhere in every reconciliation job, there's one transaction that refuses to match. We call it the **Ghost Cent** — it shows up in every currency, every timezone, every bank's nightly batch, and it has personally ruined more Friday evenings than any outage. This release doesn't exorcise it completely (nothing will), but we got faster at finding it, and we finally caught two of its favorite hiding spots.

---

## Added

### `reconcile()` batch mode

Previously, matching a day's settlement file meant calling `reconcile()` once per transaction — fine for a corner café, painful for anyone clearing six-figure transaction volumes before their coffee gets cold. `reconcile()` now accepts a batch:

```java
BatchReconciliationRequest request = BatchReconciliationRequest.builder()
    .transactions(dailySettlementFile)
    .matchStrategy(MatchStrategy.AMOUNT_AND_REFERENCE)
    .build();

BatchReconciliationResult result = wexleyClient.reconcile(request);

result.unmatched().forEach(tx -> log.warn("Unmatched: {}", tx.reference()));
```

One call, one connection, one set of retries to reason about. The Ghost Cent now has to hide among thousands of transactions instead of getting caught one lonely `reconcile()` call at a time — small mercies.

## Changed

### CSV parsing, now with less patience for your 10-million-row file

The CSV reader was rewritten around a streaming tokenizer instead of loading rows into intermediate `String[]` buffers before mapping them. On our internal benchmark (a 10M-row end-of-day settlement export, JVM 21, single core), parse time dropped roughly 3x and peak heap usage dropped with it — which matters when your batch job runs at 2 a.m. and nobody's awake to bump the container memory limit.

Nothing changes in your code. `CsvTransactionReader` keeps its existing API; it's just no longer the slowest part of your pipeline.

## Fixed

- **Zero-decimal currencies were quietly losing the argument with `Math.pow(10, 2)`.** Amounts in currencies like JPY and KRW — which have zero decimal places, not two — were being divided by 100 during matching, so every yen-denominated batch reconciled with a mismatch that was, delightfully, *always* off by a factor of 100. `CurrencyDecimals` now looks up the correct exponent per currency before comparing amounts. Apologies to every engineer in Tokyo who has stared at a ¥1,000,000 "discrepancy" that was actually ¥10,000. (#412)

- **Concurrent `reconcile()` calls on a shared client could double-count a transaction under load** — most visible in multi-threaded batch jobs clearing large BRL settlement files, where the match cache was scoped to the client instance instead of the request. Two threads, one transaction, twice the reconciliation. The cache is now request-scoped. Your end-of-day totals in São Paulo should no longer mysteriously duplicate themselves. (#437)

---

**Upgrading:**

```xml
<dependency>
    <groupId>com.wexley</groupId>
    <artifactId>wexley-sdk</artifactId>
    <version>3.4.0</version>
</dependency>
```

No breaking changes. `reconcile(Transaction)` still works exactly as before — `reconcile(BatchReconciliationRequest)` is additive, not a replacement.

---

*This note ships in 7 languages, so the Ghost Cent now haunts your ops team in Japanese and Portuguese too — global consistency, at last.*

*Note for translators: keep "the Ghost Cent" as a proper noun/consistent motif rather than translating literally each time — it recurs across releases. Everything else translates normally.*