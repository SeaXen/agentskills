# Marrowgate: record of truth and routing rules

Assumptions, since I didn't interview you: about 10 feature requests a week, SDK maintainers and PM both exist, and nothing contractual covers response times. Correct me where these are wrong.

## 1. Decision

**The public GitHub issue is the record of truth for any request that someone outside Marrowgate raised on GitHub. The private planning tool is the system of record for prioritisation, and every item in it links back to its GitHub issue.**

I'm declining two parts of the ask:

1. **Do not reply "tracked internally, closing" on GitHub issues.**
2. **Do not let the stale bot close feature requests.**

### Why not move GitHub requests into the private tool and close them

- **The reporter hits a dead end.** The link goes nowhere they can open, so they can't see status, add detail or correct a misunderstanding.
- **Demand stops being visible.** The 👍 count and the comment thread are public evidence of demand, and closing the issue discards them. Duplicates arrive within weeks, because search no longer finds the request.
- **It reads as a brush-off.** For open source SDKs, a "closing" reply tells contributors the repo is a suggestion box with no listener. That costs goodwill and contributions, and the PM team gains nothing from it.
- **The stale bot compounds it.** After 30 days of quiet, it would close accepted requests that are simply waiting on the roadmap. Reporters read that as "ignored". It also breaks the PM team's own count of open demand.
- **The arithmetic doesn't need it.** About 10 items a week at roughly 3 minutes each is about 30 minutes of triage a week. This is not a capacity problem. Hiding the requests solves nothing, and a 5-minute weekly pass is enough.

### What PM actually needs

PM needs one view of all demand, with customer context attached. A one-way link gives them that.

- Each GitHub feature request gets a linked record in the private tool, with the GitHub URL as the key. This can be a native integration or a small script.
- Customer names, ARR and internal priority live only on the private side.
- Nothing from the private tool flows back to GitHub except a status label.
- **Never post customer names, ARR or "enterprise asked for this" on a public issue.** That discloses commercial relationships. If PM wants to cite demand publicly, they say "multiple customers" and nothing more.

## 2. Routing rules

| Inflow | Where it lives | What reaches the private tool | Reply or action |
|---|---|---|---|
| **Feature request (GitHub)** | Stays open in the public SDK repo | A linked record, created by sync or by the weekly triage pass | Human reply within 5 business days. Apply one `status/` label. Don't close. |
| **Feature request (customer, sales, support)** | Private tool first | Native | If it concerns an SDK and the customer doesn't object, open a public issue with generic wording and link the two. |
| **Bug (SDK)** | Public GitHub issue, using a form with required fields: SDK version, runtime, minimal repro | Linked record only if it blocks a customer or is severity high | Reproduce, label, and close with the fix release. |
| **Bug (hosted API)** | Support or status channel | Native | Don't track API incidents in the SDK repos. |
| **Security report** | **Private channel only**: GitHub private vulnerability reporting on each SDK repo, plus a `security@` address | **Not into general PM intake.** Use a restricted security-tracker with a named responder group | Acknowledge, assess and coordinate disclosure under embargo. Publish an advisory, then a public changelog entry. |
| **How-to question (Discord)** | Stays on Discord, or a GitHub Discussion if it needs a durable answer | **Nothing flows to intake.** | Answer it. If the same question appears 3 or more times, open a docs issue. Only clusters become work items. |
| **Question filed as a GitHub issue** | Move it to Discussions or Discord | None | Transfer or convert it, with a one-line explanation and a link. |

Reasons for the less obvious rows:

- **Security stays out of general intake.** A shared planning tool is visible to far more people than a vulnerability reporter expects, and embargoed details can leak. Put it in a separately access-controlled place.
- **Discord how-to questions stay out of intake.** Each one is a support answer, and routing them all to PM buries real signal. A cluster of repeats is the real signal, and it belongs in docs.

### Status labels (one per issue, applied by a human)

| Label | Meaning |
|---|---|
| `status/needs-info` | Waiting on the reporter. |
| `status/under-consideration` | We've read it and are weighing it. |
| `status/planned` | On the roadmap. |
| `status/not-planned` | Declined, with a reason in the comment. |

Close `not-planned` items with a reason. Close `planned` items only when they ship.

Reply template for a public feature request:

> Thanks, this is logged on our roadmap list and we'll update this issue when its status changes. 👍 reactions help us gauge demand.

Never write "tracked internally" without saying what the reporter can expect next.

## 3. Stale bot configuration

- **Scope:** `status/needs-info` only. Warn after 14 days of reporter silence, then close after 14 more, with a note on how to reopen.
- **Exempt:** `under-consideration`, `planned`, `security`, any issue with an assignee, and any issue with 5 or more 👍.
- **Rollout:** run the first pass as a dry run to see what it would close.
- Never auto-close an item that is waiting on Marrowgate.

## 4. Owners and cadence

- **Triage duty:** one SDK maintainer per week, with a named backup. A 30-minute session on a fixed day covers new issues, reporter replies and sync checks. Stop at the time box, not at inbox zero.
- **Weekly handoff to PM:** the duty maintainer links new feature requests into the private tool. PM changes `status/` labels only through the maintainer, so GitHub and the private tool can't disagree.
- **Security responder group:** named, small, and separate from the triage rotation.

## 5. Risks and decisions for you

- **PM may push back that the sync costs effort.** A one-way link with a weekly pass takes about 15 minutes a week. If PM won't accept public issues as the source, the fallback is a public roadmap page that links each GitHub issue to a status, which PM controls.
- **Discord ban and moderation records** are a separate matter and stay private. Don't route them through this intake.
- **Decide:** whether the private tool's integration can sync the GitHub URL as a key without exposing private fields. Confirm that before PM builds anything.

## 6. Measuring whether it works

Re-measure monthly for the first quarter. The targets below are starting points I set, not industry benchmarks:

- Untriaged share of open items below 10%.
- A human first response within 5 business days, on at least 90% of new items.
- Zero feature requests closed by the stale bot.
- Duplicate-request rate falling, as a check that search finds existing requests.