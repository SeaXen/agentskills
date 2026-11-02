## Sanity check: troubleshooting page restructure

Verdict up front: 2 of the 4 decisions will hurt the page, 1 needs a fix not a scrap, 1 is a data question, not a design question.

### 1. One page, 28 errors as H3s — ⚠️ defensible, but verify before committing

Single reference pages for error catalogs are a real pattern (Postgres error codes, Stripe's error list) — not automatically wrong. It works **only if**:
- Every H3 has a stable, unique anchor (`#invalid-grant`, not `#authentication-problems-3`).
- The page title/meta stays broad ("OAuth Error Reference"), so it isn't fighting itself for ranking against dedicated pages.
- Nothing that identifies the error (see #4) is hidden from in-page search.

What tips this from "fine" to "wrong": if your top handful of errors already drive meaningful organic search traffic (check Search Console for exact-match error-string queries), those deserve their own URL — a dedicated page out-ranks a 28-way-diluted section every time for an exact-match query, and it's a straight hub-and-spoke fix, not a rewrite: keep the single page as the hub/index, peel the top 3-5 searched errors into their own pages, link both ways. Pull that data before locking the IA, don't guess.

### 2. Friendly topic titles ('Authentication problems', etc.) — ✅ fine, with one boundary

Keep the friendly names for the **H2 groupings only**. Do not let them replace the literal error string at the **H3 level**. The H3 is what a scanning user (or Ctrl+F, or Google) matches against — it needs to contain the actual error code/string (`invalid_grant`, `AADSTS700016`), with the friendly framing as a subtitle or lead-in sentence underneath, not instead of it. "Friendly so the reader isn't scared" is a good instinct for the page's tone; applied to the one heading users are pattern-matching against their console output, it actively hides the thing they're looking for.

### 3. DRY clock-skew explanation, linked from 9 entries — ❌ wrong model, fix don't scrap

"Same as we'd do in code" is the tell — troubleshooting entries aren't code, they're search-and-rescue for someone mid-outage. Each of the 9 entries needs to answer "what's wrong and how do I fix it" **without a click**, because that's the highest-abandonment moment on the whole page. A required hop to a different section for the actual explanation costs you support-ticket deflection, which is the entire point of a troubleshooting page.

Fix: put a self-contained 2-3 sentence explanation + fix inline in all 9 entries ("Your server clock is more than N minutes off NTP. Fix: sync via `ntpd`/`chrony`."). Keep the shared 'Understanding token validity' section too, but as a deep-dive link for people who want the mechanism, not the load-bearing explanation. If copy drift across 9 near-identical paragraphs is the actual worry, solve it at the CMS/templating layer with a shared content partial rendered into all 9 pages — that gets you one source of truth without making the reader pay for it.

### 4. Error strings in a collapsed 'Technical details' accordion — 🔴 worst of the four, change regardless of the others

The exact error string is the single most important piece of content in each section — it's what the user searched for and what they'll Ctrl+F for on landing. Putting it last, behind a click, inverts the actual priority order. Two separate problems stack here:

- **UX**: forces a click before the user can even confirm they're on the right entry. Put the literal string in a `<code>` block right under the H3, always visible. If there's a genuine "secondary" tier of content — full request/response dumps, vendor-specific variants, stack traces — that's what the accordion is for, not the identifying string itself.
- **Accessibility/technical**: if this ships as accordions at all, it must be `<details>/<summary>`, not a JS-only div toggle — that's the only implementation that's keyboard-operable and exposes state to assistive tech without manual ARIA wiring (`aria-expanded`, `aria-controls`, focus management) that's easy to get wrong. It also happens to be the only accordion type modern browsers will auto-expand on in-page find — but don't rely on that as your reason for hiding the error string; visible-by-default is still correct even with `<details>`.

### Net recommendation

Ship the friendly H2 groupings and the DRY deep-dive as a supplementary link. Reverse the accordion (error string visible, secondary detail collapsed) and make every H3 lead with the literal error text. Hold the single-page-vs-hub-and-spoke call until you've checked which specific errors already pull search traffic — that's a five-minute Search Console query, not a debate.