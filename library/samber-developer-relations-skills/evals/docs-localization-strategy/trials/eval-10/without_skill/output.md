**Verdict: don't build the full nightly pipeline yet. Run a 1-day demand check first, then a scoped 4-week pilot. Skip the pilot if the data says no.**

## Why not the full version

- **Reviewer math fails.** Jonas has about 4 hours a week. He can review perhaps 20–40 pages of diffs in that time, and the site has 2,000 pages. Most of the site would ship unreviewed, so you would be publishing machine German under your brand.
- **Nightly re-translation of everything is the wrong design.** LLM output varies between runs. Unchanged pages would produce diff noise and bury real changes. Translate only changed source segments and reuse cached translations for the rest.
- **Your doubt has real support.** Many German developers read English docs fine. One customer is n=1, but it points the same way. Search and error-message lookup also work better in English.
- **Check the MDN premise.** I recall MDN freezing its community translations in 2025. I did not verify that, and I don't know of a nightly LLM pipeline there. Confirm before using MDN as precedent.
- **Machine translation cost is small.** Rough guess: 2,000 pages is a few million words, so tens of dollars per full pass. The real cost is review time, wrong content, and keeping two versions in sync.

## Step 1: demand check (about 1 day)

1. Pull docs traffic by browser locale and country: German share of sessions.
2. Pull Search Console queries in German and impressions on `google.de`.
3. Count support tickets and sales notes that mention German docs.
4. Ask 5–8 German customers: "English docs OK, or do you want German?" Include enterprise and non-developer readers such as installers and operators.

**Go/no-go rule (my starting thresholds, adjust to your numbers):** go if German is at least 5–8% of docs traffic, or at least 3 customers say they want it. Otherwise stop and spend the budget elsewhere (search, examples, quickstart quality).

## Step 2: pilot design (if go)

**Scope in three tiers:**
- **Tier 1 (about 30–50 pages):** getting started, core concepts, device onboarding, and anything about security or compliance. Jonas reviews every page before it publishes.
- **Tier 2 (guides and tutorials):** machine-translated, published with a visible banner such as "Maschinell übersetzt, Englisch ist maßgeblich" and an English link. Jonas samples about 10% a week.
- **Tier 3 (stays English):** API reference, CLI reference, changelogs, error messages, and code. Translating these hurts searchability. If German-only readers matter here, translate only the prose around the code.

**Pipeline:**
1. Use Hugo's native multilingual mode with `content/de/` and a shared `translationKey`. Add `hreflang` and a language switcher that falls back to English when no German page exists.
2. Split pages into segments and hash them. Re-translate only segments whose hash changed. Store the output as a translation memory in git.
3. Maintain a glossary: IoT terms, product names, and terms to keep in English (e.g. "gateway", "firmware"). Jonas owns it. Pass it into every prompt.
4. Keep code blocks, URLs, shortcodes, and front-matter keys out of the model's reach. Substitute placeholders before translating and re-insert them after.
5. Run automated gates before any human sees a page:
   - the Hugo build passes
   - placeholders and anchors are intact
   - glossary terms are used
   - the length ratio is sane
   - a second LLM pass flags suspect segments
6. The nightly job opens a PR with diffs only. Flagged segments go to Jonas first. Tier 2 auto-merges after the gates pass. Tier 1 waits for Jonas's approval.
7. If a Tier 1 source page changes after approval, show an "outdated translation" banner or fall back to English until Jonas re-approves. Never show stale German as current.

**Risks:**
- **Wrong instructions:** a mistranslated safety, wiring, or security step on an IoT product is worse than no translation. Keep those pages Tier 1 or English-only.
- **Drift:** two versions will diverge. The fallback rule above handles it.
- **Jonas as single point of failure:** if he is out, Tier 1 freezes at the last approved state.

## Step 3: measure and decide (week 4)

Compare German-locale users on translated pages against the English baseline:
- bounce and time on page
- search impressions on `google.de`
- support tickets about those topics
- German customers' feedback (a short survey)

**Keep and expand** if engagement or tickets improve, or customers ask for more. **Kill** if there is no measurable difference, or if Jonas reports more than about 15% of segments needing rewrites (a signal the model is not good enough for your domain).

## Timeline

- Demand check: 1 day
- Pipeline MVP: 1–2 weeks
- Pilot run: 4 weeks
- Decision: week 6–7

## Next action

Run the traffic-by-locale query on your analytics tool (about 15 minutes) and send the 5–8 customers the one-line question. If you tell me which analytics stack you use (GA, PostHog, other), I can write the exact queries.