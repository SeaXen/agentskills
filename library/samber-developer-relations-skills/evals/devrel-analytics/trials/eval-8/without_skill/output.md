# Diagnosis and fixes: docs self-referral + launch week "direct" spike

Both problems have the same underlying mechanism: **something between the click and the pageview/signup event is dropping the attribution data, and your tools are filling the gap with whatever's left** — the raw domain (self-referral) or nothing at all (direct). Neither number is telling you what you think it's telling you.

---

## Problem 1: Docs domain showing as source, instead of `utm_source=docs`

If the field said literally "docs" as the source, that would just be your tag working. It's showing the **raw domain as a referral** instead — which means the UTM parameter isn't surviving to the pageview that fires on the pricing page. Two separate things are likely stacked here, and you should fix both:

**A. You're tagging internal links with UTM parameters at all.** This is a known anti-pattern, not a bug in your setup. Google's own guidance is explicit: never put `utm_*` on links between pages of your own site. A campaign parameter tells most analytics tools "a new session/new source has started" — so a visitor who arrived via `google/cpc` or `conference/qr`, browsed your docs, then clicked your `utm_source=docs` link to pricing, has their **real acquisition source overwritten** by "docs" the moment they hit that link. That's likely why almost every session shows this: it's not that most people come from docs, it's that the docs link **stomps on whatever the true source was**, for anyone who touches docs before pricing. The report is structurally incapable of being right as designed.

  - **Fix:** stop using `utm_source`/`utm_medium` for this. To answer "which docs page sends people to pricing," use a non-campaign mechanism instead:
    - Fire a custom event on click (`docs_cta_clicked` with a `docs_page` property), or
    - Use a custom parameter that your tool doesn't treat as a campaign field (e.g. `?ref_page=api-reference` instead of `?utm_source=docs`), or
    - If you're on GA4, just query session path (`page_referrer` → landing page) in Explore/BigQuery — the internal navigation path is already there without touching acquisition dimensions at all.

**B. Self-referral: your docs domain likely isn't in the referral exclusion list**, and/or docs + app aren't configured as one cross-domain property. If they're on different (sub)domains, crossing from docs → pricing can register as a brand-new session with the docs domain as referrer, independent of the UTM issue above.

  - **Fix (GA4):** Admin → Data Streams → your stream → Configure tag settings → "List unwanted referrals" → add the docs domain. If docs and app/marketing site are separate domains, also configure cross-domain measurement (same section → "Configure your domains") so the click ID/session carries across the handoff instead of resetting.
  - **Fix (other tools):** same concept exists everywhere — Mixpanel/Amplitude/PostHog all have a way to whitelist your own domains from referrer classification; the setting name differs but the fix is identical.

**Verify before declaring it fixed:** open dev tools, click the actual docs→pricing link, and watch the full URL through every redirect (www/https normalization, CDN rewrites, trailing slash) to the point the pageview actually fires. If the query string dies anywhere in that chain, that's an independent bug to fix regardless of (A)/(B).

---

## Problem 2: 78% "direct" during launch week

"Direct" is a garbage-collection bucket for lost attribution, not evidence people typed your URL from memory — and launch week, of all weeks, should be dominated by campaign traffic, not organic type-ins. You named the two exact mechanisms that cause this:

**A. The link shortener.** Most shorteners resolve to a **fixed destination URL** — they don't reliably forward whatever query string arrived on the short link unless explicitly configured to pass through, and plenty of teams shorten a bare URL and never bake UTMs into the *long* destination at all. If that's what happened, every scan of a conference QR code lands with zero query params → direct, by construction, not by accident.
  - **Fix:** audit every conference short link now — resolve each one and read the final destination URL. The UTMs need to be baked into the destination URL itself, not assumed to pass through. Don't re-test this once and trust it forever; re-check after any change to the shortener config.

**B. The OAuth redirect.** This is the bigger one and it's structural: user lands with a UTM/referrer → clicks Sign up → gets bounced to an OAuth provider (a different domain) → bounced back to your callback URL. The callback URL almost never carries the original campaign params, and the hop through the OAuth provider's domain either shows up as a referral from `accounts.google.com` (if not excluded) or as direct (if the browser's Referrer-Policy trims it, which is the default in most browsers today). Either way, by the time `signup_completed` fires, the attribution data is already gone — this has nothing to do with whether your tracking snippet is installed correctly.

  - **Fix — capture before the redirect, stitch after it:**
    1. On first landing (before the user ever clicks "Sign up"), write the session's UTM/referrer into a first-party store on your own domain — a cookie or `localStorage`, or your analytics tool's anonymous ID with `$initial_utm_*` properties if it supports that pattern (PostHog/Segment/Amplitude/Mixpanel all do).
    2. Use OAuth's `state` parameter to round-trip a reference to that captured session through the login flow — `state` exists exactly for "survive a redirect to a third party and back" use cases, so this isn't a hack, it's the intended mechanism.
    3. At the callback, when your identify/signup event fires, merge it against the anonymous ID (recovered via `state` or the cookie) so first-touch attribution — the actual conference/campaign/docs source — survives all the way to `signup_completed`, instead of being overwritten by whatever the bare callback URL looks like.
    4. Add `accounts.google.com` / your OAuth provider's login domains (and any `login.*` subdomain of your own) to the referral exclusion list too, as a backstop for the cases that leak through despite (1)-(3).

**One retroactive caveat:** once fixed, don't re-run the same GA4 report on launch week's historical data expecting it to change — the raw hits that already landed as "direct" had no UTM to recover, full stop. For an honest retroactive read on what actually drove launch week, add a lightweight "How did you hear about us?" field at signup now. It's the standard fix for attribution that's structurally invisible to tracking, and it'll give you a real cross-check going forward, not just for this incident.

---

## What to tell your CMO

The 78% direct number isn't evidence the campaign underperformed or that tracking is broadly broken — it's evidence of two specific, now-identified technical gaps (shortener pass-through, OAuth redirect washout) that both erase attribution *before* the signup event ever fires. That's a fixable measurement problem, not a demand-generation problem. Recommend holding off on any budget conclusions from launch week's channel mix until the OAuth stitch and shortener audit are in place and you have at least one clean week of data to compare against the self-reported survey as a sanity check.

## Priority order

1. Shortener audit (cheap, immediate, no engineering) — do this today, conference links may still be live.
2. Referral exclusion list + OAuth domain exclusion (settings change, ~30 min).
3. Stop UTM-tagging internal docs→pricing links; switch to a custom event/parameter (settings + one small dev change).
4. Ship the "how did you hear about us" field at signup (fastest way to get a trustworthy read while the OAuth stitch is built).
5. OAuth `state`-based attribution stitching (the real engineering lift — plan it, don't rush it, since a bug here can also corrupt identity merges if the anonymous/known ID boundary isn't handled carefully).