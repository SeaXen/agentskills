# Deliverable: migration guide for Brightmoor Pay API version 2026-11-02

I read `SKILL.md` and its references and followed the hosted-API route. I couldn't interview you, so section 1 lists every assumption, and the guide carries `{{Qn}}` markers where a fact is assumed. The guide can't publish until those markers are cleared.

## 1. Assumptions and open questions

**Churn Rule position:** the consumers are customers' own codebases, so a guide is the right deliverable. Brightmoor can't migrate them in place.

**Audience:** commercial customers under a notice window. The guide leads with the deadline, a named support path and rollback. It also needs support and legal/comms sign-off before publish.

**Placeholder conventions**
- Field names (`amount`, `fee`, `status`), the example IDs and the SDK option names are illustrative. I had no schema.
- The pin header `Brightmoor-Version` and the `Brightmoor` client class are assumed.
- Swap in real names from the schema diff before publish.
- Code snippets have not been compiled or run yet.

**Open questions, highest impact first**

| # | Question | Why it matters |
|---|---|---|
| Q1 | Dates: notice date, flip date, old-version sunset, and an end date for managed/enterprise accounts. | Without dates, contractual readers can't schedule. Today is 2026-10-03, so a guide published before 2026-11-02 has 30 days at most. |
| Q2 | Pin mechanism: header or parameter name, SDK option names, base URL. Does a per-request pin beat the account default? | The guide's most valuable instruction depends on it. |
| Q3 | `charge.id`: do existing charges get 26-character IDs, or only new ones? Is a 26-character ID accepted on the old version? What are the maximum length, charset, case-sensitivity and prefix? | This decides whether the break is pinned to the version or leaks across versions. |
| Q4 | Money: major units with the currency's exponent digits, and does that hold for JPY (0 decimals) and KWD (3)? Does it apply to request parameters too? Does the new version still accept integers on input? What is the full field list? | The helper code and the inventory both depend on it. |
| Q5 | Is `in_review` a straight rename of `pending_review`? How are existing records mapped? What does `?status=pending_review` return on the new version? | Persisted rows and the fix steps depend on it. |
| Q6 | Which of the 14 webhook event types carry changed fields? Can a new-version test endpoint be registered? What shape do events created before the flip but retried after it use? Does the payload carry an `api_version` field? | Webhooks can't be pinned per request, so this is the riskiest surface. |
| Q7 | Which SDKs pin the API version at compile time (the typed ones) and which allow per-request overrides? What are the minimum SDK versions? Do shipped iOS binaries pin a version or follow the account default? How is browser.js pinned, given that it is evergreen? | A shipped iOS binary can't be recalled. If it follows the default, the flip breaks it. |
| Q8 | Do you have telemetry on usage per field and per surface? | The blast-radius order below is a maintainer-style estimate until you have it. |
| Q9 | Is there a codemod, a lint rule or SDK-side conversion, and who owns it after release? | I assumed none. The guide ships search patterns and literal messages only. |
| Q10 | Rollback after the flip: what mechanism, and for how long? How long does the old version stay available? | Required for contractual readers. |
| Q11 | Did the current version warn about these changes? Is an interim warnings release possible? | I assumed it breaks cold. |

## 2. Inventory

| Change | Type | Blast radius (rank) | Evidence |
|---|---|---|---|
| Money fields: integer cents → decimal string | Wire/format | 1. Every integration that reads or writes an amount. Fails silently in JavaScript. | Maintainer estimate ({{Q8}}) |
| `charge.id`: 18 → 26 characters | Wire/format (length) | 2. Every integration that stores, validates or displays IDs. Loud with strict SQL, silent truncation otherwise. | Maintainer estimate |
| `status`: `pending_review` removed, `in_review` added | Enum change | 3. Integrations that branch on, persist or filter by that value. | Maintainer estimate |
| 14 webhook event types | Wire/format, not pinnable | Cross-cutting. Gets its own section. | Needs the schema diff ({{Q6}}) |
| SDK models, browser.js, iOS `Decodable` | Type-level | Per surface. | Needs the SDK diff ({{Q7}}) |

**Hyrum's Law additions** (not in the changelog, but customers will have noticed them):
- Fixed-width ID columns in receipts, CSV exports and log formats.
- `id.length === 18` validators.
- Sorting or comparing IDs as strings.
- Alert rules that match the literal `pending_review`.
- Warehouse tables whose schema was auto-detected as INTEGER for money.
- Raw REST clients in other languages, such as Go's `int64` unmarshalling.

## 3. Recommended path shape

**Single hop with per-request pinning and a customer-side flip date.**
- With 30 days or less before the cut, a staged interim release is not realistic.
- The three changes are small enough to land in one sitting per service.
- The pin lets each customer test first without changing anything permanent.
- No compat build, because no owner is named ({{Q9}}).

**Process suggestion:** add a "How we teach this" section to your API-change RFC template (the Ember and Rust gate). Then every future version cut produces its guide automatically.

## 4. The guide

---

# Migrating to Brightmoor API version 2026-11-02

**Covers:** `{{CURRENT_VERSION}}` → `2026-11-02`. Surfaces: Node SDK, Python SDK, browser.js, iOS SDK, webhooks, and raw REST clients.
**Expected effort:** not yet measured. This line will carry the measured time of the cold upgrade run.

## What changes and when

| | |
|---|---|
| Notice date | `{{Q1}}` |
| **Flip date** (Brightmoor moves your account default) | `{{Q1}}` |
| Old version available until | `{{Q1}}` |
| Managed / enterprise exception ends | `{{Q1}}` |
| Support | `{{support channel}}` · escalation `{{contact}}` |

**If you do nothing:** on the flip date, requests without an explicit version pin start receiving the new shapes. Until then, your account stays on `{{CURRENT_VERSION}}`. Requests pinned to the old version are unaffected until the sunset date `{{Q2}}`.

**Three things break:**

1. [Money fields are decimal strings, not integer cents.](#changed-money-decimal-string)
2. [`charge.id` grows from 18 to 26 characters.](#changed-charge-id-length)
3. [`status` loses `pending_review` and gains `in_review`.](#changed-status-enum)

## Before you start

Do these in order. Each step is safe before the flip.

1. **Meet the floors** (next section).
2. **Pin explicitly to your current version everywhere**, so the flip never changes an application nobody touched.
3. **Widen your ID columns** ([charge.id entry](#changed-charge-id-length)). This is the only step that must precede the others, because 26-character IDs can arrive from new-version calls.
4. **Make webhook handlers accept both shapes** ([Webhook payload changes](#webhook-payload-changes)). Webhooks can't be pinned per request, so they flip with your account.
5. **Change your code for the three entries.** Test it in sandbox with the new pin.
6. **Move your pin to `2026-11-02` one service at a time.**
7. **Delete the dead code** ([Housekeeping](#housekeeping)).

## Requirements

Machine-checkable floors. Fill these from the release manifest ({{Q7}}).

- Node SDK `>= {{x.y.z}}`, Node `>= {{x}}`
- Python SDK `>= {{x.y.z}}`, Python `>= {{x.y}}`
- iOS SDK `>= {{x.y.z}}`, Xcode `>= {{x}}`
- browser.js release `{{name}}`
- All Brightmoor packages in one family on matching versions. A half-upgraded family produces errors that look like these breaking changes but aren't.

## Surfaces and versions

*Rows marked {{Q7}} are assumptions to confirm.*

| Surface | Versioning | How it picks the API version |
|---|---|---|
| Node SDK | Semver | Per client or per request. {{Q7}} |
| Python SDK | Semver | Per client or per request. {{Q7}} |
| browser.js | Named evergreen releases | Pinned to one API version per release. {{Q7}} |
| iOS SDK | Semver | Pinned at build time. Binaries already in the App Store keep their pin. {{Q7}} |
| Webhooks | Follows account default | **Not pinnable per request** |
| Raw REST | n/a | Your pin header |

## Test before you switch

Pin one request to the new version. Nothing permanent changes.

```bash
curl https://api.brightmoor.com/v1/charges/8f3k2m9x4q7w1z5b6c0d8e4h2j \
  -H "Authorization: Bearer $BRIGHTMOOR_API_KEY" \
  -H "Brightmoor-Version: 2026-11-02"
```

Same pin in an SDK. The option names are assumed ({{Q2}}).

```ts
import { Brightmoor } from "brightmoor";

const brightmoor = new Brightmoor(process.env.BRIGHTMOOR_API_KEY!, {
  apiVersion: "2026-11-02",
});
```

```python
import os
import brightmoor

client = brightmoor.Client(os.environ["BRIGHTMOOR_API_KEY"], api_version="2026-11-02")
```

**Precedence:** a per-request pin wins over the account default. {{Q2}}

**Always pin in code.** An inherited default turns the next cutover into an incident.

## Breaking changes

Ordered by how many integrations hit each one. This is a maintainer estimate until usage telemetry confirms it.

### Changed: money fields are decimal strings {#changed-money-decimal-string}

**Affects you if** your code reads, compares, sums or sends any amount field. Search for:

```
\bamount\b|_cents|\* ?100\b|/ ?100\b|parseInt\(|parseFloat\(|Int\(.*amount|BIGINT|INTEGER.*amount
```

You will see one of these at runtime:

```
Swift:   DecodingError.typeMismatch ... Expected to decode Int but found a string instead.
Go:      json: cannot unmarshal string into Go struct field Charge.amount of type int64
Python:  TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

JavaScript raises no error: `"12.50" + 100` is `"12.50100"`.

Every money field is now a decimal string in major units, for example `"12.50"`. {{Q4}}

An integer in minor units forces every consumer to know each currency's exponent, and the 32-bit integer ceiling bites on large amounts. {{Q4: confirm rationale}}

```json
// Before ({{CURRENT_VERSION}})
{ "id": "8f3k2m9x4q7w1z5b6c", "amount": 1250, "fee": 75 }

// After (2026-11-02)
{ "id": "8f3k2m9x4q7w1z5b6c0d8e4h2j", "amount": "12.50", "fee": "0.75" }
```

**Fix:**

1. Run the search above and list every call site.
2. Never use `parseFloat`: `parseFloat("19.99") * 100` is `1998.9999999999998` in JavaScript.
3. Convert at one boundary, keep integer minor units internally, and pass each currency's exponent explicitly (2 for USD, 0 for JPY, 3 for KWD).

```ts
// money.ts (target ES2020 or later for BigInt)
export function toMinorUnits(amount: string, exponent: number): bigint {
  const match = /^(-?)(\d+)(?:\.(\d+))?$/.exec(amount);
  if (!match) throw new Error(`invalid money string: ${amount}`);
  const [, sign, whole, fraction = ""] = match;
  if (fraction.length > exponent) {
    throw new Error(`too many decimals for exponent ${exponent}: ${amount}`);
  }
  const minor = BigInt(whole + fraction.padEnd(exponent, "0"));
  return sign ? -minor : minor;
}

export function toMoneyString(minor: bigint, exponent: number): string {
  const negative = minor < 0n;
  const digits = (negative ? -minor : minor).toString().padStart(exponent + 1, "0");
  const whole = digits.slice(0, digits.length - exponent);
  const fraction = digits.slice(digits.length - exponent);
  return `${negative ? "-" : ""}${whole}${exponent > 0 ? "." + fraction : ""}`;
}
```

```python
# money.py
from decimal import Decimal


def to_minor_units(amount: str, exponent: int) -> int:
    scaled = Decimal(amount).scaleb(exponent)
    if scaled != scaled.to_integral_value():
        raise ValueError(f"too many decimals for exponent {exponent}: {amount}")
    return int(scaled)


def to_money_string(minor: int, exponent: int) -> str:
    return format(Decimal(minor).scaleb(-exponent), f".{exponent}f")
```

```swift
// Money.swift
import Foundation

enum MoneyError: Error { case invalid(String) }

func toMinorUnits(_ amount: String, exponent: Int) throws -> Int64 {
    guard let decimal = Decimal(string: amount, locale: Locale(identifier: "en_US_POSIX")) else {
        throw MoneyError.invalid(amount)
    }
    var scaled = decimal * pow(10, exponent)
    var rounded = Decimal()
    NSDecimalRound(&rounded, &scaled, 0, .plain)
    guard rounded == scaled else { throw MoneyError.invalid(amount) }
    return NSDecimalNumber(decimal: rounded).int64Value
}

struct Charge: Decodable {
    let id: String
    let amount: String   // Before: let amount: Int
}
```

4. **browser.js:** treat `charge.amount` as a string and never do arithmetic on it. Format it for display with the same helper, or pass it to `Intl.NumberFormat` as a string.
5. **Warehouse and BI:** change money columns from INTEGER to a decimal or string type before the first new-version row lands. Auto-detected schemas reject the type change.
6. **Requests:** send money as decimal strings under the new version. {{Q4}}

**Escape hatch:** pin to `{{CURRENT_VERSION}}`. Integer cents are returned until `{{Q1: sunset}}`. There is no per-field switch.

### Changed: `charge.id` grows from 18 to 26 characters {#changed-charge-id-length}

**Affects you if** anything stores, validates, indexes or displays a charge ID. Search for:

```
varchar\(18\)|char\(18\)|VARCHAR\(18\)|\{18\}|length === 18|len\(.*\) == 18|maxLength.*18|String\(18\)
```

Strict SQL fails on insert:

```
Postgres: ERROR:  value too long for type character varying(18)
MySQL:    ERROR 1406 (22001): Data too long for column 'charge_id' at row 1
```

With non-strict MySQL, the ID is silently truncated. Retrieval of that charge then fails with `{{API error text for unknown id}}`.

New charge IDs are 26 characters. Fixed-width storage, validation and layout built for 18 truncate or reject them. Existing charges: `{{Q3}}`. Maximum length, charset, case-sensitivity and prefix: `{{Q3}}`.

```sql
-- Before: charge_id VARCHAR(18)
-- After (Postgres): widening a varchar limit does not rewrite the table
ALTER TABLE charges ALTER COLUMN brightmoor_charge_id TYPE varchar(32);

-- After (MySQL): fails loudly instead of locking if it can't run in place.
-- Keep your existing NOT NULL and character set.
ALTER TABLE charges
  MODIFY brightmoor_charge_id VARCHAR(32) NOT NULL,
  ALGORITHM=INPLACE, LOCK=NONE;
```

**Fix:**

1. Widen every column holding a charge ID to `VARCHAR(32)`. That is 6 characters of headroom over 26. It is also small enough that MySQL `utf8mb4` keeps the one-byte length prefix and the change stays in place. Replace 32 with Brightmoor's published maximum `{{Q3}}` once it exists.
2. Widen foreign-key columns, join tables, cache keys and index definitions together.
3. Replace `{18}` and `length == 18` validators with `{26}` only after step 1. Accept both lengths until the old version is retired.
4. Check fixed-width outputs: receipts, CSV exports, log formats, UI columns.
5. Don't sort or compare IDs as strings across the two lengths.

**Escape hatch:** the pin behaves as in [Test before you switch](#test-before-you-switch). Whether old-version calls can read a charge created under the new version is `{{Q3}}`. There is no escape for rows you have already widened and written: they stay 26 characters.

### Changed: `status` loses `pending_review` and gains `in_review` {#changed-status-enum}

**Affects you if** you branch on, persist, filter by or alert on `status`. Search for `pending_review` in code, SQL, dashboards and alert rules. At runtime:

```
Swift:   Cannot initialize ChargeStatus from invalid String value in_review
Python:  ValueError: 'in_review' is not a valid ChargeStatus
```

TypeScript raises no error. An unhandled value falls through to your `default` branch.

`in_review` replaces `pending_review` as the state of a charge awaiting review. {{Q5: confirm same meaning and how existing records map}} Adding a member is backward compatible under the [compatibility contract](#compatibility-contract). Removing one is not, so it gets this entry.

```swift
// Before
enum ChargeStatus: String, Decodable { case pendingReview = "pending_review", succeeded }

// After: decode unknown values instead of crashing. The other members are
// listed in your schema; this example names only the changed one.
enum ChargeStatus: Decodable, Equatable {
    case inReview
    case other(String)

    init(from decoder: Decoder) throws {
        let raw = try decoder.singleValueContainer().decode(String.self)
        self = raw == "in_review" ? .inReview : .other(raw)
    }
}
```

**Fix:**

1. Add `in_review` to every enum, switch and condition. Keep `pending_review` until the old version is retired.
2. Make decoders tolerate unknown values.
3. Backfill stored `pending_review` rows to `in_review` after the flip, in throttled batches.
4. Update filters: `?status=pending_review` on the new version returns `{{Q5}}`.
5. Update alert rules and dashboard filters.
6. Remove `pending_review` once the old version is gone.

**Escape hatch:** pin to `{{CURRENT_VERSION}}`. `pending_review` is returned until `{{Q1: sunset}}`.

## Compatibility contract

Brightmoor treats these as non-breaking. Code defensively against exactly this list, and nothing else:

- new resources
- new optional request parameters
- new response properties
- reordered properties
- new enum members
- new event types

Anything outside the list gets a dated version and a guide like this one. {{Q2: confirm this list is the published policy}}

## Webhook payload changes

You can't pin an inbound request. Webhook shape follows your **account default**, so it changes on the flip date, regardless of what your API calls pin.

**Before the flip, make every handler accept both shapes.** Parse once, at the boundary.

```ts
import { toMinorUnits } from "./money";

export function parseAmount(value: unknown, exponent: number): bigint {
  if (typeof value === "number" && Number.isInteger(value)) return BigInt(value);
  if (typeof value === "string") return toMinorUnits(value, exponent);
  throw new TypeError(`unsupported amount: ${JSON.stringify(value)}`);
}

const LEGACY_STATUS = "pending_review";
const CURRENT_STATUS = "in_review";
export const normalizeStatus = (s: string) => (s === LEGACY_STATUS ? CURRENT_STATUS : s);
```

```python
from decimal import Decimal
from money import to_minor_units


def parse_amount(value, exponent: int) -> int:
    if isinstance(value, bool):
        raise TypeError(f"unsupported amount: {value!r}")
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        return to_minor_units(value, exponent)
    raise TypeError(f"unsupported amount: {value!r}")
```

Events created before the flip and retried after it carry `{{Q6: old or new shape}}`. Assume either shape can arrive until your last pre-flip event stops retrying (`{{retry window}}`).

Test endpoint: `{{Q6: can a new-version endpoint be registered?}}` If yes, put the instructions here. If not, replay fixtures of both shapes against your handler.

Fill this table from the payload schema diff. One row per event type, 14 in total.

| Event type | Money fields | `charge.id` | `status` |
|---|---|---|---|
| `{{event.type}}` | yes / no | yes / no | yes / no |

## Data-layer impact

These break weeks after a successful cutover, so check each one:

- **ID width:** columns, indexes, foreign keys, cache keys and fixed-width exports (see the `charge.id` entry).
- **Persisted enum values:** rows holding `pending_review`, plus any lookup table or analytics dimension.
- **Mixed money shapes in stored raw payloads:** anything that saved the raw JSON now has integer cents before the flip and strings after it. Re-parse with the dual-shape helper.
- **Warehouse schemas:** auto-detected INTEGER money columns reject strings.
- **Reconciliation:** exports with 18-character IDs must still join to 26-character IDs. `{{Q3}}`

## Cutover and rollback

1. **Who flips:** Brightmoor moves your account default on `{{Q1: flip date}}`. {{Q2: can you request an earlier or later date?}}
2. **Before that date, you must finish** steps 1 to 5 of [Before you start](#before-you-start).
3. **Roll back** by pinning requests to `{{CURRENT_VERSION}}` `{{Q10: or the dashboard setting}}`. This works until `{{Q1: sunset}}`. Webhook shape reverts only if `{{Q10}}`.
4. **What rollback does not undo:** rows you have already written in the new shape. Keep dual-read code until the old version is retired.
5. **Old version availability:** until `{{Q1}}`. Managed and enterprise deployments get their own end date: `{{Q1}}`.

## Deprecation timeline

| Item | Replacement | Warning level | Removed from default |
|---|---|---|---|
| Integer money fields | Decimal strings | None. Breaks at the flip. {{Q11}} | `{{flip date}}` |
| 18-character `charge.id` | 26-character IDs | None | `{{flip date}}` |
| `pending_review` | `in_review` | None | `{{flip date}}` |
| Old version | `2026-11-02` | n/a | `{{sunset}}` |

## Automated migration

There is no codemod, lint rule or compat build for this version. {{Q9}} The search patterns and literal messages in each entry are the automation. Use them from a script or a coding agent.

## Housekeeping

After you've moved to `2026-11-02`, delete:

- dual-shape parsers and the `pending_review` branches
- the cents-to-dollars conversion helpers
- the temporary 18-or-26 ID validators
- backfill jobs
- the old-version pin, once you no longer need rollback

## Troubleshooting

Match on the text you see.

| Error text | Entry |
|---|---|
| `ERROR:  value too long for type character varying(18)` | [charge.id](#changed-charge-id-length) |
| `ERROR 1406 (22001): Data too long for column` | [charge.id](#changed-charge-id-length) |
| `Expected to decode Int but found a string instead.` | [money](#changed-money-decimal-string) |
| `json: cannot unmarshal string into Go struct field Charge.amount of type int64` | [money](#changed-money-decimal-string) |
| `unsupported operand type(s) for +: 'int' and 'str'` | [money](#changed-money-decimal-string) |
| `Cannot initialize ChargeStatus from invalid String value in_review` | [status](#changed-status-enum) |
| `ValueError: 'in_review' is not a valid ChargeStatus` | [status](#changed-status-enum) |
| `{{API error: integer sent to a money field}}` | [money](#changed-money-decimal-string) |
| `{{API error: unknown status filter}}` | [status](#changed-status-enum) |
| `{{API error: charge not found}}` after an ID was truncated | [charge.id](#changed-charge-id-length) |

**Still stuck:** `{{support channel}}`, escalation `{{contact}}`.

---

## 5. Verification plan

The guide has not been verified yet. Before publish:

1. **Cold run, one per surface.** Someone who did not write the guide upgrades a real project: an example app for each of Node, Python, browser.js and iOS, plus one webhook consumer. Measure each elapsed time and publish the effort figure only from those measurements.
2. **Completeness diff.** Diff the guide against the schema diff between `{{CURRENT_VERSION}}` and `2026-11-02`, across all 14 webhook events and every money field. Add anything support or early-access customers already saw break.
3. **Helper tests.** Run the Node, Python and Swift helpers in CI. Include vectors `"0.05"`, `"12.50"`, `"19.99"`, `"-0.01"`, a JPY value (exponent 0), a KWD value (exponent 3), and a rejected `"1.234"` at exponent 2.
4. **ID migration.** Run the widening `ALTER` on a copy of production-shaped data. Execute the rollback once.
5. **Webhooks.** Replay 14 fixtures in each shape against a handler built from the guide.
6. **Pass threshold:** all six criteria (completeness, detectability, sufficiency, automation honesty, path validity, self-containment). Automation honesty applies trivially, since no codemod is claimed.
7. **Sign-off.** Support and legal/comms review the dates and the escalation path.

## 6. KPIs

In wiring order:

| KPI | Source |
|---|---|
| Tickets per thousand upgrading accounts that quote an error above, and which entry generates most | Support tickets. Rewrite the top entry first. |
| Share of requests and accounts still on the old version, per surface | API gateway logs. This is the equivalent of deprecation-warning telemetry. |
| Webhook delivery failures (non-2xx) per endpoint after the flip | Webhook delivery logs |
| Guide behavior: in-page error-string searches and exits to support | Docs analytics |
| **Adoption curve:** share of accounts on `2026-11-02` at 30, 60 and 90 days after the flip | Account-to-version join. **Start the join before release**, or the first 90 days are unmeasurable. |
| **Stragglers:** named accounts still on the old version after the deadline | The same join. This is the list your success team works. |

Plan the last ~15% of accounts as named-account work, not a docs problem. Start hard enforcement only after the curve visibly flattens.

**Next step:** answer Q1 to Q11 (Q1 to Q4 and Q6 to Q7 block publishing). I'll then clear the markers and tighten the guide.