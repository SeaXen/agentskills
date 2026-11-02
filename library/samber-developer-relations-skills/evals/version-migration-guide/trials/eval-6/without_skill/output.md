# Migrating to Brightmoor Pay API version 2026-11-02

**Applies to:** upgrading from your current default version to `2026-11-02`.
**Your account default does not change until Brightmoor flips it for you.** Nothing breaks until you opt in or we flip your account, and we will tell you before we do.

## Before you publish: items to confirm

I wrote this without access to your API specs or SDK repos. Each `[CONFIRM]` below marks a fact I assumed. Replace or delete each one before this ships.

- The version-pinning header name and the SDK option names.
- The SDK versions that support `2026-11-02`.
- Whether old 18-character IDs stay valid after the change, and whether the API still accepts them.
- Whether `pending_review` maps 1:1 to `in_review`.
- Whether requests, as well as responses, use decimal strings for money.
- The flip date, the notice period and the rollback window.
- The 14 webhook event type names and which carry the changed fields.

## What changes

| # | Change | Old | New |
|---|---|---|---|
| 1 | Money fields | Integer cents (`1999`) | Decimal string (`"19.99"`) |
| 2 | `charge.id` length | 18 characters | 26 characters |
| 3 | `status` enum | includes `pending_review` | `pending_review` removed, `in_review` added |

This changes the type of every money field, the shape of one identifier and the vocabulary of one enum, so it is a breaking release. Assume every integration is affected until you have checked.

Do the changes in this order. I ranked them by how many integrations they hit. If you have telemetry on field usage, re-rank them with it.

1. Money. Every integration reads or writes an amount.
2. Charge ID length. It hits anyone who stores, validates or displays IDs.
3. Status enum. It hits anyone who branches on `status`.

## Choose your path

1. **Test per request first.** Send `2026-11-02` on individual requests while your account default stays unchanged.
2. **Fix your code** with the entries below.
3. **Test in sandbox**, then in production with a small share of traffic.
4. **Switch your default** when you are ready, or wait for us to flip it.

This is a single hop. There is no interim version. Skip any step in the list at your own risk, because there is no deprecation-warning release to point you at the remaining call sites.

## Step 0: version floors and the compatibility matrix

Upgrade every package in your stack to a version that understands `2026-11-02` before you change anything. A half-upgraded stack produces errors that look like the breaking changes below but are not.

| Surface | Minimum version for `2026-11-02` | How it gets the version |
|---|---|---|
| Node SDK | `[CONFIRM]` | `[CONFIRM: client option]` |
| Python SDK | `[CONFIRM]` | `[CONFIRM: client option]` |
| `browser.js` | `[CONFIRM]` | `[CONFIRM: script URL or init option]` |
| iOS SDK | `[CONFIRM]` | `[CONFIRM: configuration property]` |
| Webhooks | n/a | Endpoint-level setting, see [Webhooks](#webhooks) |

Check these before you start:

- All SDKs in your stack are at or above the minimums above.
- Your server SDK and your client SDK (`browser.js` or iOS) agree on the version they target. The client and server must not decode the same charge differently.
- Your webhook endpoints are on the version you intend (see below).

**Warning for mobile apps:** an iOS app already in the field keeps running the SDK it shipped with, and users update on their own schedule. `[CONFIRM: does the SDK pin a version per release, or does it follow the account default?]` If it follows the account default, an account flip changes what old app builds receive. If it pins a version, old builds keep working but cannot use new behavior. State which applies, and keep your backend able to serve both until old builds age out.

## How to test the new version before any default moves

Send the version on a single request:

```bash
# [CONFIRM: header name]
curl https://api.brightmoor.example/v1/charges/CHARGE_ID \
  -H "Authorization: Bearer $BRIGHTMOOR_SECRET_KEY" \
  -H "Brightmoor-Version: 2026-11-02"
```

Or set it on the SDK client (`[CONFIRM: option names]`):

```js
// Node
import Brightmoor from "brightmoor";
const client = new Brightmoor(process.env.BRIGHTMOOR_SECRET_KEY, { apiVersion: "2026-11-02" });
```

```python
# Python
import brightmoor
client = brightmoor.Client(api_key=os.environ["BRIGHTMOOR_SECRET_KEY"], api_version="2026-11-02")
```

Run your integration tests against the sandbox with this version. Fix failures using the entries below.

---

## Changed: money fields are decimal strings {#money-decimal-string}

**Affected if:** your code reads or writes any amount field (`amount`, `fee`, `refunded`, and every other money field in the API reference `[CONFIRM: list]`). Search for:

```bash
grep -rnE "\b(amount|fee|refund|balance|total|price)\w*\b" src/ | grep -vE "test|spec"
```

Typical symptoms after upgrade:

- `TypeError`, `NaN`, or `"19.99" + 1 === "19.991"` in JavaScript.
- `TypeError: unsupported operand type(s) for +: 'int' and 'str'` in Python.
- `typeMismatch` decoding errors in Swift.

**What changed and why.** Money fields were integers counted in the currency's minor unit (cents). They are now strings holding a decimal in the major unit, for example `"19.99"`. Strings avoid floating-point rounding and handle currencies whose minor unit is not 1/100.

**Before and after:**

```jsonc
// Before
{ "amount": 1999, "currency": "usd" }
// After
{ "amount": "19.99", "currency": "usd" }
```

```js
// Before
const total = charge.amount + fee.amount;           // cents
const display = (charge.amount / 100).toFixed(2);
// After: use a decimal library, never Number or parseFloat
import Decimal from "decimal.js";
const total = new Decimal(charge.amount).plus(fee.amount);
const display = total.toFixed(2);
```

```python
# Before
total = charge["amount"] + fee["amount"]            # cents
# After
from decimal import Decimal
total = Decimal(charge["amount"]) + Decimal(fee["amount"])
```

```swift
// Before
let cents: Int = charge.amount
// After
let amount: Decimal = Decimal(string: charge.amount, locale: Locale(identifier: "en_US_POSIX"))!
```

**The fix:**

1. Find every place you read a money field and parse it with a decimal type. Never use floats.
2. Find every place you send a money field `[CONFIRM: if requests also use strings]` and send a decimal string.
3. Check every stored amount. If you store cents as integers in your own database, convert at the API boundary only. Do not change your own schema unless you want to.
4. Check currencies where the minor unit is not 1/100 (for example zero-decimal and three-decimal currencies). The old integer encoding hid this: `1000` meant different amounts depending on currency. The new string is the actual amount. Remove any per-currency divisor tables.
5. Check comparisons and sums, such as reconciliation jobs, reports and "refund ≤ original" checks. String comparison (`"9.99" > "10.00"`) is wrong. Compare as decimals.

**Escape hatch:** none. Pin the old version per request if you need time. `[CONFIRM]`

---

## Changed: `charge.id` is 26 characters {#charge-id-26}

**Affected if:** you store, validate or display charge IDs. Search for:

```bash
grep -rnE "varchar\(18\)|CHAR\(18\)|\{18\}|length\s*(==|===|!=|<=?|>=?)\s*18|\[:18\]|\.prefix\(18\)|maxlength=.?18" .
```

Typical symptoms after upgrade:

- `value too long for type character varying(18)` (PostgreSQL), `Data too long for column` (MySQL).
- Silent truncation, leaving orphaned or colliding records.
- A validation regex such as `^ch_[A-Za-z0-9]{15}$` rejecting good IDs.
- Truncated IDs in logs, UI or support tools.

**What changed and why.** Charge IDs grow from 18 to 26 characters to give more room for unique IDs. `[CONFIRM: prefix and alphabet unchanged?]`

**Before and after:**

```jsonc
// Before
{ "id": "ch_0123456789abcdef" }                    // 18 characters [CONFIRM: example format]
// After
{ "id": "ch_0123456789abcdef01234567" }            // 26 characters [CONFIRM: example format]
```

```sql
-- Before
charge_id VARCHAR(18) NOT NULL
-- After
ALTER TABLE payments ALTER COLUMN charge_id TYPE VARCHAR(64);  -- headroom; do not pin to 26
```

**The fix, in this order:**

1. **Widen your database columns first**, and any index, foreign key or cache key built on them. Do this before any request carries the new version. Widening is safe on the old version.
2. Remove length checks, fixed-width regexes, `maxlength` attributes and fixed-width fields in logs, CSV exports and UI.
3. Treat IDs as opaque strings. Do not parse, slice or length-check them.
4. Check third-party systems that receive the ID (data warehouse, accounting export, support tools).
5. Decide what to do with charges already stored. `[CONFIRM: do existing 18-character IDs remain valid in both versions, and does the API accept an old-format ID in lookups under 2026-11-02?]` Until you know, keep your lookups working for both formats.

**Escape hatch:** none. The ID format follows the version, so pin the old version per request if you need time.

---

## Changed: `status` loses `pending_review`, gains `in_review` {#status-in-review}

**Affected if:** you branch on, filter by, store or display `charge.status`. Search for:

```bash
grep -rnE "pending_review|PendingReview|pendingReview|PENDING_REVIEW" .
```

Typical symptoms after upgrade:

- A charge sits in your system forever because your handler never matches `in_review`.
- `ValueError: 'in_review' is not a valid ChargeStatus` (Python enum).
- `DecodingError.dataCorrupted ... Cannot initialize Status from invalid String value in_review` (Swift `Codable` enum).
- A TypeScript `switch` that compiles but falls into `default`.

**What changed and why.** `pending_review` is removed and `in_review` replaces it. `[CONFIRM: state semantics are identical, i.e. a 1:1 rename. If not, say exactly what differs.]`

**Before and after:**

```ts
// Before
type ChargeStatus = "pending_review" | "succeeded" | "failed"; // [CONFIRM: full list]
// After
type ChargeStatus = "in_review" | "succeeded" | "failed";       // [CONFIRM: full list]
```

```swift
// Make decoding survive values you do not know yet
enum ChargeStatus: String, Codable {
    case inReview = "in_review"
    case succeeded, failed
    case unknown
    init(from decoder: Decoder) throws {
        let raw = try decoder.singleValueContainer().decode(String.self)
        self = ChargeStatus(rawValue: raw) ?? .unknown
    }
}
```

**The fix:**

1. Accept both `pending_review` and `in_review` in your handlers during the rollout. Both appear while versions are mixed, for example webhooks on one version and API reads on another.
2. Update list filters: `status=pending_review` becomes `status=in_review`. `[CONFIRM: what the API returns if the old value is sent under the new version.]`
3. Update database enums, analytics dimensions, dashboards and alert rules that mention `pending_review`.
4. Give every enum decoder an explicit unknown case, as in the Swift example.
5. After you are fully on `2026-11-02`, delete the `pending_review` handling.

**Escape hatch:** none. Pin the old version per request.

---

## Webhooks {#webhooks}

You receive 14 event types. Payloads embed the objects above, so the same three changes apply inside them.

1. Open your webhook endpoint settings. `[CONFIRM: where the version is set, and whether it can differ per endpoint.]`
2. **Create a second endpoint pinned to `2026-11-02`** that points at a staging handler, and keep the existing endpoint where it is.
3. Compare payloads from both endpoints for the same event. Fix your handler until the new endpoint's events process cleanly.
4. Switch your production endpoint last, after your API reads are on the new version. Do not run your API client on one version and your webhook consumer on the other without handling both shapes.

| Event type | Contains money fields | Contains `charge.id` | Contains `status` |
|---|---|---|---|
| `[CONFIRM: event 1]` | `[CONFIRM]` | `[CONFIRM]` | `[CONFIRM]` |
| … | … | … | … |
| `[CONFIRM: event 14]` | `[CONFIRM]` | `[CONFIRM]` | `[CONFIRM]` |

**Before you flip:**

- Handlers deduplicate by event ID, not by charge ID length or format.
- Signature verification still uses the raw request body. Parsing and re-serializing the JSON changes it.
- Stored raw events from before the flip are still readable by your replay tooling.
- Retries of events created before the flip: `[CONFIRM: delivered in the old shape or the new one?]` Handle both.

---

## Cutover and rollback

**For testing**, nothing to do. Per-request pinning has no side effects on your account.

**When you are ready to move your default:** `[CONFIRM: self-serve in the dashboard, or by request]`. Run through the checklist below first.

**When we flip your default:** we will notify you at least `[CONFIRM: N days]` before the date, by email to your account's technical contacts. Keep those contacts current.

**Rollback:** `[CONFIRM: you can revert your default to the previous version for N days after the change.]` If you revert, in-flight webhooks and new charges may be in either shape. Your handlers from the status and ID sections already tolerate that.

### Cutover checklist

1. SDKs upgraded and matching across server and client (Step 0).
2. Database columns widened for 26-character IDs.
3. Money parsed as decimals everywhere; no float arithmetic.
4. `in_review` handled; `pending_review` still tolerated.
5. Test endpoint receiving new-version webhooks without errors.
6. Dashboards and alerts updated.
7. A rollback owner is named and knows the revert procedure.

## Housekeeping after the move

Once everything runs on `2026-11-02`, remove:

- Per-request version pins you added for testing.
- The second webhook endpoint.
- The `pending_review` handling and any old-ID-format fallbacks.
- Cents-to-decimal conversion shims.
- Any wide-open `varchar` workarounds you want to tighten.

## Troubleshooting by error text

| You see | Cause | Fix |
|---|---|---|
| `value too long for type character varying(18)` / `Data too long for column 'charge_id'` | 26-character IDs hitting 18-character columns | [Widen the column](#charge-id-26) |
| `TypeError: unsupported operand type(s) for +: 'int' and 'str'` | Money field is now a string | [Parse as `Decimal`](#money-decimal-string) |
| `"19.99" + 1 === "19.991"` or `NaN` totals | Same | [Use a decimal library](#money-decimal-string) |
| `'in_review' is not a valid ChargeStatus` | Enum has no `in_review` | [Update the enum](#status-in-review) |
| `Cannot initialize Status from invalid String value in_review` | Swift enum decoding | [Add an unknown case](#status-in-review) |
| Charges stuck in a "pending" state | Handler never matches `in_review` | [Handle both values](#status-in-review) |
| Webhook handler errors only for some events | Payload shape differs per version | [Webhooks](#webhooks) |
| Client and server disagree on a charge's fields | SDKs on different versions | [Step 0](#step-0-version-floors-and-the-compatibility-matrix) |

## Support

`[CONFIRM: support channel, escalation path, status page, changelog link]`

If a step here fails and the guide does not tell you what to do next, that is a defect in this guide. Report it.

---

## Notes for you, not for publication

- **I did not run a cold upgrade.** Before publishing, have someone who did not write this guide upgrade a real sample integration using only the guide, and publish the elapsed time you measure.
- **Completeness.** Diff the guide against the real API schema difference between the two versions. My three changes come from your brief. Hyrum's Law says some customers also depend on behavior you did not list.
- **Check the 14 webhooks.** The table above is empty on purpose. Fill it from the event catalog.
- **Unanswered decisions that block publication:** the flip date, the notice period, the rollback window, and the iOS in-the-field policy. Customers cannot schedule against a guide that has no date.
- **Track adoption.** Join your account list to API version usage before release, so you can see who is on `2026-11-02` at 30, 60 and 90 days. Plan to work the last ~15% by name.