## Talk structure — ObservabilityDays, 30 min + Q&A

**⚠️ First, the thing to push back on with marketing:** 7 features in 30 minutes is 4 minutes each after intro/close — that's a spec sheet read aloud, not a talk, and this audience (90% hands-on/staff engineers) will clock it as a sales pitch and check out. The fix isn't cutting features, it's cutting the *feature-tour format*. Structure below hits all 7, but subordinates them to a single incident narrative — nobody's counting features, they're watching you solve a problem. Tell marketing: "all 7 are in, none of them get their own slide."

### Title (pick one, all avoid "Q3 feature roundup" framing)
- "The 2am Trace: Debugging a Cascading Failure, Live"
- "From Alert to Root Cause in Under Ten Minutes"
- "Zero to Root Cause: One Incident, Everything We Shipped This Quarter"

### The spine

One incident, played out live (or via screen recording — see risk note below), where each feature earns its place because the story needs it, not because a checklist does.

**0:00–0:02 — Cold open (no logo slide, no agenda slide)**
State the failure mode cold: "p99 on checkout triples. Twelve services touched the request. You have four minutes before this trends on your status page." Who you are and Corvid get one sentence, in passing, not a slide.

**0:02–0:04 — Frame**
"I'm going to walk this incident start to finish, live, using what we shipped this quarter." This is the sentence that buys you permission to touch 7 things without it feeling like a tour.

**0:04–0:08 — Setup (fast, infra-as-backdrop)**
- OTel-native ingest: system is instrumented with vanilla OTel, no proprietary agent — one line, one architecture slide.
- Terraform provider: this environment's alerts, budgets, and sampling policy are one `terraform apply` — show a real, short snippet. This is the only place Terraform gets airtime; don't return to it as its own segment, return to it in the resolution beat instead (see below).
Keep this under 4 minutes. Staff engineers want to see it exists; nobody wants a tour of it.

**0:08–0:10 — Detection**
Anomaly alert fires. One sentence on why it's not a static threshold (baseline-modeled, catches the shape of the regression, not a fixed p99 number) — this is the line that earns staff-engineer trust; don't over-explain the algorithm on stage, take it to Q&A if asked.

**0:10–0:13 — The second fire that didn't happen**
Retry storm behind the failure spikes span volume ~10x. This is where adaptive sampling and per-service budgets land together, causally: the budget would have been blown and paged a second, unrelated incident (cost/volume) on top of the first — adaptive sampling backs off automatically and it doesn't. One line: "the system didn't page us twice." This is the strongest place in the talk to make these two features feel indispensable instead of bolted on.

**0:13–0:21 — Investigation (the demo, most of your time budget)**
- Query language: narrow live from "checkout is slow" to "checkout is slow, this version, this region, since this deploy." Show the actual query, not a screenshot of results — SREs judge the tool by the syntax.
- Trace-diff view: pull a slow trace next to a known-good one, side by side, and land on the added hop / N+1 call visually. This is your "aha" beat — give it the most stage time of anything in the talk.

**0:21–0:24 — Resolution, loop closed**
Roll back or patch, alert clears. Then: the budget and alert threshold that nearly got blown get written back as a Terraform diff — one slide, callback to 0:04–0:08, closes the narrative instead of leaving Terraform feeling like a separate plug.

**0:24–0:27 — Zoom out**
One summary slide, all 7 named explicitly (satisfies marketing's checklist for anyone screenshotting slides), reframed as a pipeline not a list: *ingest → cost control → detection → investigation → resolution → provisioned as code.* One sentence for the EM 10%: what this replaces, what it costs to adopt, rollout effort.

**0:27–0:30 — Close**
One quotable line with a real number ("cut this class of incident from 40 minutes to 6" — use your actual number). Call to action: docs/booth, and explicitly "OTel-native, so there's no agent migration to evaluate this" — the objection this audience will actually have. Land exactly at 30:00; Q&A is separate, don't borrow from it.

### If you're running long, cut in this order
1. Terraform snippet at 0:04–0:08 — mention it, skip the code.
2. Per-service budgets explanation — fold into one sentence inside the "second fire" beat.
3. Never cut the trace-diff demo — it's the reason SREs remember the talk.

### Demo risk
Live query + trace-diff over conference wifi is the single biggest failure risk in this structure. Have a screen recording as the actual "live" segment, or a tested offline fallback — don't let a network hiccup eat your best 8 minutes.

### Q&A prep by segment (60/30/10 in the room)
- **SREs (60%):** agent overhead, PagerDuty/on-call integration, "does this replace [incumbent tool]," alert fatigue / false-positive rate.
- **Staff engineers (30%):** anomaly-detection algorithm specifics, sampling math under bursty load, multi-tenant/data-residency, query language's underlying model.
- **EMs (10%):** pricing, migration effort and timeline, security/compliance posture, team size to run it.

### After the talk (per event-marketing content arc — you already have the recording paid for)
- Clip the trace-diff "aha" moment (0:13–0:21) — it's the most shareable 90 seconds, independent of the rest of the talk.
- Say your one hard number out loud and cleanly on stage (MTTR, cost delta, whatever's real) — that's the line that gets quoted in recap posts and picked up by AI-search summaries later.
- Publish the query-language example and the Terraform snippet as a short follow-up post — practitioners who saw the talk will look for exactly those two artifacts afterward.