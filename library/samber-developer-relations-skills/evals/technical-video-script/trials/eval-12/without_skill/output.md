## Before she records

**The single biggest risk isn't the version mismatch — it's that three real customers' financial data will be on screen in a recording that outlives the session.** Fix that first; the version skew is a secondary, more mechanical problem.

### 1. Kill the real customer data problem at the source

Don't try to mask live data mid-recording — hand her an environment where the problem doesn't exist:

- **Provision a synthetic demo org inside the staging tenant** (or a separate sandbox) seeded with fake reconciliation data — fake vendor names, fake account numbers, fake dollar amounts, fake bank feeds. This is the only reliable fix; redaction after the fact on financial data (account numbers, running balances, entity names that appear in dropdowns, search-ahead, exception queues) is error-prone and someone always finds the one frame that leaked.
- If a synthetic org isn't buildable in time, **scope her demo login to a role that can't even query the three pilot orgs** — not "please don't click on them," an actual permission boundary. Verify the boundary yourself by logging in as that role and trying to reach the pilot data.
- Confirm with whoever owns those three pilot relationships (CS or legal) whether your contracts/DPAs with them say anything about customer data appearing in recorded materials — even internal ones. If nobody's checked, that's a procurement/security-review question that outranks the demo itself. Get a yes/no before she hits record, not after.

### 2. Neutralize the v7.4-rc / v7.3 mismatch

She's demoing on a build that isn't what ships. Two failure modes: she shows a feature that doesn't exist yet in GA, or she hits an RC bug that doesn't exist in 7.3 either.

- **Get the diff.** Ask engineering for the feature/behavior delta between the 7.3 branch and the 7.4-rc build running on the demo box — flags added, UI changed, workflows altered, known RC bugs.
- **Feature-flag off anything 7.4-only** on the demo tenant, or restrict her script to screens/workflows confirmed unchanged since 7.3. Whichever is faster.
- **Scrub every visible version marker**: about page, build banner, footer, API response headers if any dev tools get opened, page titles. If any of these can't be hidden, at minimum know they're there so review can catch them.
- Have someone from engineering **sanity-check her exact script against a real 7.3 build** (or the 7.3 release notes) right before she records — not a general "looks fine," a literal click-through of her script on the other version.

### 3. Hand her a physical package, not verbal instructions

- **A written script**: exact URLs, exact login, exact click path, exact talking points. No improvising inside a tenant that has real customer data physically reachable, even if permissioned off.
- **A locked-down recording setup**: fresh browser profile (no autofill, no saved logins to other tenants, no bookmarks bar), notifications and Slack/email/calendar fully silenced, only the demo window open, desktop background and dock free of anything internal, VPN/hostname not visible in the address bar.
- **A named go/no-go person** she pings 10 minutes before recording, who confirms: synthetic-or-scoped data is live, RC-only features are flagged off, browser is clean. Recording without that confirmation doesn't happen.
- **A stop-and-redo instruction, explicit**: if anything looks wrong mid-take, she stops and re-records rather than trying to edit it out afterward. Cutting a video is not a substitute for never recording the leak.

## After it's recorded — how you'll know it worked

Don't let the person who made the recording be the only one who reviews it — the SE is the least likely to spot her own leaks because she's watching her talking points, not the background.

1. **Second-person frame-by-frame review**, specifically hunting for:
   - Any of the three real pilot customer names, account numbers, entity names, or dollar figures — including in autocomplete dropdowns, toast notifications, exception/error queues, and browser tab titles, not just the main content pane.
   - Any version string, build number, "rc," staging hostname, or internal URL.
   - Any screen or workflow that doesn't exist, or behaves differently, in 7.3 GA — checked against the engineering diff from step 2 above, not from memory.
   - Anything from outside the demo itself: a Slack toast, a calendar popup, a Finder/Explorer notification that slipped through.
2. **Run a known-string check** against the raw file if you can — the three customer names/domains, any account-number patterns, "rc," internal hostnames — before assuming a visual pass is sufficient. Visual review misses things that a text/OCR grep catches.
3. **Confirm storage and access** on the recording itself: where it lands, who can open it, whether it goes through the same review path as other customer-facing assets before it's used anywhere beyond internal training.
4. **Get explicit sign-off from the pilot-customer owner (CS/legal)** that the final cut is clear, and from engineering that nothing RC-only survived — two separate approvals, not one person checking both boxes.

If any of steps 1–3 turns up a hit, the fix is redo the take from a clean environment, not trim the clip. A reconciliation product's whole value proposition is trustworthy handling of sensitive financial data — a demo that visibly mishandles a pilot customer's numbers undercuts the pitch it's supposed to be making.