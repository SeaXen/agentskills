**Pick:** Renderforest — scene-by-scene templates, built-in animated icons/charts, AI voiceover, direct export. No editing skill needed, fits 6-day deadline. Alt: Vyond, more polish, but steeper learning curve — skip it, deadline too tight.

**Timeline (today 2026-09-18 → live 2026-09-24):**
1. Today: lock script below, fill `[bracketed]` numbers from your post/dashboard
2. Day 1-2: build scenes in Renderforest using templates below, generate AI voiceover
3. Day 3: internal review, fix pacing/timing drift
4. Day 4-5: embed on site, QA on mobile + desktop, buffer for GA day

Word count target: ~400-420 words VO total, spoken at ~145 wpm = under 3:00. Read each scene's VO out loud with a timer before recording — that's your real pacing check, not word count math.

---

## SCRIPT — "How We Cut Retry Storms by 90%"

### Scene 1 — Hook (0:00–0:12)
**VO:**
"Every webhook failure used to trigger the same nightmare: hundreds of retries firing at once, hammering the same endpoint, at the same second."

**Visual:** Screen fills fast with pulsing red "retry" icons hitting one server icon. Renderforest template: "alert/notification burst" scene.
**On-screen text:** none — let the icon burst carry it.

### Scene 2 — Background (0:12–0:32)
**VO:**
"Loomcast delivers [X million] webhooks a day for teams who can't afford a missed event. So when a customer's endpoint went down, our system did the responsible thing: it retried. The problem was thousands of other deliveries retried at the exact same moment too."

**Visual:** Server-stack icon, arrow fan-out to many endpoint icons. Stat callout animates in: "[X million]/day."
**On-screen text:** "[X million] webhooks/day"

### Scene 3 — Why retries storm (0:32–1:00)
**VO:**
"Here's why: fixed retry intervals mean every failed delivery lines up on the same clock. One endpoint blip, and suddenly [X thousand] queued jobs all wake up in the same second, all hit the same recovering server, and knock it back down. We call it a retry storm — the fix meant to help was making outages worse."

**Visual:** Clock icon, multiple retry icons all ticking to the same mark, then all firing together — use "synchronized pulse" template animation.
**On-screen text:** "RETRY STORM"

### Scene 4 — Old approach, first fix, still broken (1:00–1:25)
**VO:**
"Our old queue retried on a simple fixed schedule — easy to reason about, brutal under load. We tried adding random jitter first. It softened the spikes but didn't stop them: once queue depth grew past [X], the storms came back."

**Visual:** Before/after split card. Left: fixed-schedule icon, red X. Right: jitter version, still red X but smaller spike. Template: "comparison card" split-screen.
**On-screen text:** "Fixed retries" / "+ Jitter — still not enough"

### Scene 5 — The fix: token bucket (1:25–2:10, core scene, give it the most screen time)
**VO:**
"So we rebuilt retry delivery around a token bucket, one per destination. Each bucket refills at a steady rate — say [X] tokens a second. A retry can only fire if it can spend a token. No tokens left? It waits its turn instead of piling on. A thousand retries queued for the same failing endpoint no longer arrive as one crushing burst — they drip out at a rate that endpoint can actually survive. The failing service gets room to recover, instead of getting buried the moment it comes back up."

**Visual:** Literal animated bucket icon filling with token dots, dripping out one at a time into a steady stream toward the endpoint icon. Renderforest has this as a stock "liquid/token fill" animation — no custom art needed.
**On-screen text:** "1 bucket per destination" → "[X] tokens/sec"

### Scene 6 — Benchmarks (2:10–2:35)
**VO:**
"We measured it against real incident traffic: retry storms dropped by 90 percent. [Latency / CPU / queue-depth stat] improved right alongside it. Same failures, same retry volume — just spread out instead of stacked up."

**Visual:** Simple bar or line chart building left-to-right, landing on "90%" in large text. Use the built-in "chart reveal" template — don't hand-draw this.
**On-screen text:** "−90% retry storms"

### Scene 7 — Conclusion + CTA (2:35–3:00)
**VO:**
"This logic is now built into the Loomcast Retry API, live in general availability September 24th. If you're handling webhook deliveries at scale, this is the retry behavior you want by default. Docs and migration guide at [link]."

**Visual:** Loomcast logo, end-card button style: "Retry API — GA Sept 24." Template: standard CTA end-card.
**On-screen text:** "[loomcast.com/docs/retry-api]"

---

**Fill before recording:** `[X million]` webhooks/day, `[X thousand]` queued jobs example, `[X]` queue-depth threshold, `[X]` tokens/sec refill rate, one benchmark stat for scene 6, final docs URL. Pull these straight from your post — don't guess them, viewers will screenshot the stat card.

**Next:** open Renderforest, start a new "explainer" project, paste Scene 1's VO into the first slide, generate its AI voiceover, and check it lands near 12 seconds.