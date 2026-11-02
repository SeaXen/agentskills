**Bottom line: at current numbers, capacity covers roughly 1 in 8 incoming issues. No label scheme fixes that — intake has to shrink hard, and the response promise has to be honest, not aspirational. Single most urgent action, do today: turn on GitHub's private vulnerability reporting. 40,000 dependents means a security report sitting in the public tracker is a real risk, and this is a 2-minute settings toggle, not an ongoing time cost.**

I answered this as one complete deliverable instead of the skill's normal one-question-at-a-time interview, since you asked for the final artifact directly. That means I filled in unstated facts myself — flagged below. Correct any of them and the numbers downstream change.

## Assumptions made (flag any that are wrong)

1. Tracker is GitHub (labels + forms language fits; adjust mechanics if not).
2. Nobody else has **or wants commit access** — but a label-only **Triage role** (no merge rights) wasn't ruled out. Worth 30 seconds of thought: this is the one lever that could actually change the math, not just rearrange it.
3. Inflow mix unknown (bug/feature/question split not given) — designed to be robust to any mix rather than guessed.
4. No contractual response obligation (pure OSS, not company-backed).
5. Security reports currently have no defined path — treated as true given nothing was said.
6. No hard deadline — treated as "make it survive long-term with near-zero time," not "clear the backlog once."

## 1. Baseline

- Open: 380. Inflow: 12/week (~52/month).
- Capacity: 20 min/month, one person. Using this skill's own unverified placeholder (3 min/item, until you time a real session): **~7 items/month decided.**
- Gap: capacity is ~13% of inflow. Net backlog growth ~45 items/month, ~500+/year, untouched. 380 → close to 900 within a year on the current trajectory.
- Per-item vs. clustering call: **both.** Old backlog gets a one-time bulk reset (below); a handful of recurring root causes (e.g. known spec-edge-case behavior) get merged into 2-4 tracking issues instead of staying open individually.

Get the real numbers once, cheaply:

```bash
gh issue list --state all --limit 2000 \
  --json number,title,state,createdAt,updatedAt,closedAt,labels,author,comments > issues.json
python3 scripts/triage-baseline.py issues.json --stale-days 120 --format json > baseline.json
```

That replaces my 3-min/item placeholder with your real one — the whole capacity read hinges on it.

## 2. Triage policy (publish this, next to CONTRIBUTING.md, link it from every issue form)

```markdown
# How cindermark is triaged

cindermark has one maintainer with about 20 minutes a month for issue triage.
This is not a support contract — treat replies as a courtesy, not a guarantee.

## What belongs here
Bugs and feature requests, with the required form fields filled in.
Usage questions → GitHub Discussions.
Security reports → GitHub's private vulnerability reporting (Security tab). Never the public tracker.

## What to expect
No guaranteed first-response time. New issues are auto-labeled and reviewed in
a monthly batch. A pull request against an already-`accepted` issue gets looked
at before a new report does — code that's ready to merge is the fastest path
to a fix.

## States
- `needs-triage`: nobody has looked yet.
- `needs-info`: waiting on you. Reply with the missing detail and it re-enters the queue.
- `accepted`: real, will be worked when there's time. No ETA implied.
- `blocked`: waiting on something outside this project's control.

## When we close
- No reply to a `needs-info` request for 30 days (automated, with a 14-day warning first).
- Out of scope, with a one-line reason and a link.
Closed isn't final — comment with what was missing and reopen.

## Who triages
One person, one ~20-minute batch a month. No fixed rotation — it's solo.
If you're interested in triage-only access (labeling, closing duplicates — no
merge rights), open a discussion; that's the one thing that could change this.

## If volume outruns even this
If sustained inflow passes ~20/week, or most of a month's batch turns out to
be duplicates or invalid, new issue creation gets temporarily restricted to
people with prior contributions to the repo.
```

## 3. Label change list

Type moves to GitHub's native **Issue Types** (Bug / Feature / Task) — zero labels spent on an axis the tracker already has built in.

State axis only, 4 labels total (solo-maintainer tier — priority and area are deliberately skipped; a one-person queue doesn't need them, and a "contributor-facing" pair like `good first issue` is skipped because nobody has time to curate it honestly):

| Action | Label | Definition |
|---|---|---|
| create | `needs-triage` | Default on every new issue via form automation. Nobody has decided yet. |
| create | `needs-info` | Waiting on the reporter. Stale-sweep target. |
| create | `accepted` | Real, will be worked eventually. Never auto-applied. |
| create | `blocked` | Waiting on something external (upstream dep, spec ambiguity, etc). |
| delete | anything else currently in use once (single-use labels) | Private notes, not a taxonomy. |

## 4. Intake change list (the part that actually matters here — cutting intake is the only lever with real leverage)

1. **Bug report form** (`.github/ISSUE_TEMPLATE/bug.yml`), all required: what happened / expected, minimal reproduction using only cindermark's own API, version (dropdown, not free text), environment, log output as a code block, a "searched existing issues" checkbox. Auto-applies `needs-triage` + Issue Type: Bug.
2. **Feature request form**, fields ordered problem → proposed solution → alternatives (never "describe your solution" first — that produces solutions to unstated problems).
3. **No usage-question form.** Chooser (`config.yml`) points those to Discussions instead; `blank_issues_enabled: false`.
4. **Enable private vulnerability reporting** (repo Settings → Security) — do this before anything else on this list.
5. **DCO/sign-off bot** on PRs, enforced automatically, zero human time per PR.

Later, once the above is live and you have a real minutes-per-item number:
- **Stale-sweep automation** (`actions/stale`), scoped only to `needs-info`, 14-day warn / 7-day close, `accepted`/`blocked` exempt, **dry-run first** — a live first run on a 380-issue backlog can close hundreds at once and generate a notification storm.
- **Interaction limit** (GitHub Settings → Moderation) as the volume-gating action, held in reserve until the trigger above fires — don't turn it on preemptively.

## 5. Duty and gate design

No rotation is possible solo — this replaces it with the closest honest equivalent:

1. One fixed monthly 20-minute session, calendar-blocked. Hard stop at 20 minutes — whatever's left rolls to next month.
2. Session order: newest `needs-triage` first, then `needs-info` items with a fresh reply, then a small fixed quota from backlog.
3. The one interrupt allowed to break the monthly batch: a security report notification. Everything else waits.
4. If you ever get one volunteer for label-only **Triage role** access — that's the only change that raises capacity rather than just reshuffling it. Worth revisiting assumption #2 above for this reason alone.

Pull request gate order (PRs compete for the same 20 minutes, so automate what costs zero human time first):
1. DCO sign-off + CI green — automated precondition, not a menu item.
2. Direction check ("does this belong in cindermark at all") — kills most externally authored, wrong-scope PRs before any code gets read.
3. Auto size label from the diff (routes, decides nothing).
4. Code-correctness review — reserved for PRs against an already-`accepted` issue first; anything else waits for a slower pass.

## One-time backlog reset (do once, not repeatable)

380 open issues won't get triaged one by one at 7 items/month — that's 4+ years. Do this once, the same day the new intake above goes live:

1. Dry-run a stale sweep across the full 380: idle >180 days, not `accepted`/`blocked`. Read the list before it fires.
2. Run it live, one message of explanation, one open door to reopen.
3. Whatever real, recurring bugs survive — merge them into 2-4 tracking issues by shared root cause instead of triaging each individually.

This is a bounded exception to the 20-min/month budget, not a new steady-state cost.

## Metrics — relaxed from the skill's default monthly cadence, deliberately

Monthly baseline re-runs cost time you don't have. Automate it instead: a scheduled action posts open count, untriaged share, and inflow-vs-outflow to a pinned issue. You read it **quarterly**, not monthly — that's the one deviation from the skill's default, made explicit because even reading a report costs minutes you're already short on.

---

Next: enable **private vulnerability reporting** in repo settings (2 minutes) — everything else on this list can wait for next month's batch, that one can't.