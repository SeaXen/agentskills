## Docs → Signup Tracking Plan — Q3 OKR

### Flag before you lock the target

The 25% target borrows a number from the wrong funnel stage. "20-40% activation" for dev tools almost always means **signup → first key action** (first API call, first successful build, first project created) — not **visitor → signup**. Those are different populations with different conversion economics:

- Docs traffic is mostly people who were never going to sign up: existing customers looking up a reference, people who landed via a Google error-message search, competitors, students, bots/scrapers.
- Benchmarks for content-to-signup (docs, blog, landing pages) for dev tools typically run **1–8%**, with best-in-class quickstart pages reaching maybe 10–15%. 25% of *all* docs traffic converting to signup would be exceptional to the point of implausible.
- If you ship 25% as the OKR, one of two things happens: it's missed and reads as a visible failure to the board, or it's "hit" only by narrowing the definition (e.g., counting just quickstart-page visitors) after the fact — which looks like goalpost-moving, not performance.

Recommendation: use the five weeks of data you already have to compute a real baseline, then set Q3 as a **relative lift over baseline**, not an absolute number borrowed from a different metric. Take this back to the CEO as "baseline is X%, we're targeting +N% relative improvement" rather than a flat 25%.

---

### 1. Define the metric precisely (do this before anything else)

Pick one definition and write it down — "docs conversion rate" without this is not a metric, it's a phrase people will each interpret differently at OKR review time.

| Decision | Recommended choice | Why |
|---|---|---|
| Numerator | Unique visitors who complete `signup_completed` within N days of a docs session | Same-session-only undercounts; devs often read docs, close the tab, sign up later on another device |
| Attribution window | 7 days | Long enough to catch delayed signup, short enough to stay causally plausible |
| Denominator population | New, non-authenticated, non-bot unique visitors to `/docs/*` | Excludes existing customers referencing docs (they can't "convert" — they're already customers) and excludes bot/crawler traffic, which inflates the denominator and silently deflates the rate |
| Counting | Per unique visitor, not per session | A visitor reading 12 doc pages before signing up shouldn't count as 12 chances against the rate |

Write this definition into the tracking plan doc itself, not just this conversation — it's the thing people will disagree about in six months.

### 2. Baseline first, then set the target

1. Re-run your existing five weeks of docs analytics against the definition above (new + non-authenticated + non-bot only). If your current setup can't isolate those three dimensions, that's a data-quality gap to close **before** the OKR is finalized — an unfiltered five-week number may already be misleading the CEO right now.
2. Take the resulting baseline CVR (call it `B`).
3. Propose the Q3 target as `B × 1.1` to `B × 1.3` (a 10–30% relative lift is a defensible single-quarter stretch for an existing funnel with no major redesign planned). Reserve anything above that for a quarter where you're shipping a specific docs/signup redesign, not steady-state improvement.
4. Present both numbers to the CEO: the corrected baseline and the relative-lift target. That's a more defensible OKR than an absolute figure with no connection to your actual traffic.

### 3. Event schema

| Event | Fires when | Key properties |
|---|---|---|
| `docs_page_view` | Any `/docs/*` page loads | `page_path`, `docs_section` (quickstart / api-reference / guides / troubleshooting), `is_new_visitor`, `is_authenticated`, `referrer_type` (organic / direct / referral / social / internal-app), `utm_source/medium/campaign` |
| `docs_engaged_view` | ≥30s on page **or** ≥50% scroll depth | same as above — separates real reading from bounce/bot traffic |
| `docs_cta_clicked` | Click on any in-docs signup/CTA link | `cta_location`, `cta_text`, `docs_page_path` |
| `signup_started` | Signup form rendered/opened | `entry_point` (`docs`, `marketing_site`, `app`, etc.), `first_touch_docs_page` (last-viewed docs page in session, if any) |
| `signup_completed` | Account created | `method`, `source_attribution` (`docs` if a `docs_page_view` occurred in the prior 7 days, else null), `days_since_first_docs_visit` |

Naming convention: lowercase, `object_action`, matches the pattern your other events should already follow — keep it consistent if you have existing events elsewhere.

### 4. Segmentation you need, or the number will lie to you

- **New vs. returning visitor** — mandatory, per above.
- **Authenticated vs. anonymous** — mandatory, excludes existing customers from the denominator.
- **Docs section** — a quickstart page and an API-reference page have wildly different conversion intent; blending them hides where the real opportunity is.
- **Traffic source** — organic search docs traffic (someone Googled an error) converts differently than docs traffic linked from your own marketing site.
- **Bot filtering** — docs pages get disproportionate crawler/scraper traffic (LLM training crawlers, uptime monitors, SEO tools) compared to app pages. Filter by known bot user-agent lists at minimum; consider a session-based heuristic (single-page, <1s dwell) as a backstop.

### 5. Implementation notes (GA4 assumed — adapt if you're on Mixpanel/PostHog/Amplitude)

- **Cross-domain tracking is the most likely silent killer of this exact metric.** If docs live on `docs.yourproduct.com` and signup lives on `app.yourproduct.com` (or `yourproduct.com`), GA4's default session model breaks the docs→signup thread at the domain boundary unless you explicitly configure cross-domain measurement (linker parameters, or a shared first-party ID passed through). Without this, docs-driven signups misattribute as "direct," and your conversion rate silently reads near-zero regardless of what's actually happening. Check this first — it's a common, easy-to-miss trap for exactly this funnel shape.
- Add custom dimensions: `is_new_visitor`, `is_authenticated`, `docs_section`.
- Mark `signup_completed` (with `source_attribution = docs`) as the GA4 conversion event, not raw `signup_completed` overall — you want the docs-attributed slice reportable on its own, not buried in total signups.
- Validate in DebugView before trusting five more weeks of data: confirm `is_new_visitor`/`is_authenticated` populate correctly, confirm the cross-domain handoff preserves the client ID, confirm bot filtering isn't also filtering real users (check for false positives on fast-scrolling power users).

### 6. Reporting cadence and how "hit" gets graded

- Weekly dashboard: baseline CVR trend, split by the segments above, plus raw docs traffic volume (so a rate change isn't confused with a volume change).
- **Grade the OKR on a trailing 4-week average at quarter end**, not a single week or a cherry-picked peak day — with only 5 weeks of history behind you, week-to-week noise will be large, and a single-day spike (launch, HN front page, etc.) shouldn't be allowed to make or break the number.
- Re-check the baseline at the start of Q3 (week 1) before committing hard to the target number in front of the CEO — five weeks is thin enough that a second data pull may shift `B` meaningfully.