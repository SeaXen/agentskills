**Step 0 (do now, 20 min):** Open one misplaced page's front matter / CMS config. Check: does "section" live in the URL path (`/docs/section/page`) or only in a nav/sidebar field separate from the URL? This answer gates items 3 and 4 below — write it down.

Queue, ranked, for one writer at 6 hr/week. No redirect layer this quarter — every item below is written to avoid new 404s.

**1. Fix Snowflake IAM conflict — P0, 2-3 hr, this week**
Two copies disagree on required IAM role, sitting at onboarding step 3. Wrong role = broken or over-permissioned connections for every new customer right now. Confirm correct role with infra/security first (don't guess). Pick one page as canonical, rewrite it. Turn the second copy into a stub that transcludes/includes the canonical block if your static site generator supports partials — kills future drift for good. If no partials support, at minimum add a visible "canonical version: [link]" banner on the non-canonical copy. Neither URL gets deleted.

**2. Rename 3 confusing sections — P0, 1 hr, this week (only if Step 0 shows section is nav-only)**
If section label ≠ URL slug: rename the display label only, ship same day, zero broken links. If section name is baked into the URL path: do NOT rename this quarter — blast radius is every URL under that section with no redirect to catch fallout. Flag it instead as "needs URL migration + redirect layer" for next quarter's planning, and park it.

**3. Write Terraform provider tutorial — P1, 8-10 hr, weeks 2-3**
18 tickets in 90 days = real, measurable support cost, highest ROI item in this queue. New page, new URL — no breakage risk. Draft steps 1: outline + working example (2 hr). Get it validated against real infra by an SME (calendar wait, not writer hours). Then finish write-up + publish (6-8 hr). Start this in week 2 right after item 1.

**4. Relocate 9 misplaced pages — P2, 3-9 hr, weeks 4-5**
Depends on Step 0:
- Section is nav-only → cheap fix: change each page's section field, done, no URL change. ~20 min/page, 3 hr total.
- Section is in the URL → moving breaks the old URL permanently (no redirect layer). Do NOT move the file. Instead: keep old URL alive as-is, and add a link to it from the correct section's index page. Cross-link, don't relocate. ~30-45 min/page, 4.5-7 hr total.

**5. Split 6 mixed procedure/reference pages — P3, 6-9 hr, weeks 6-8**
Lowest urgency, real usability drag. For each: keep the how-to steps on the existing URL (no breakage), move the full option table to a new reference page, cross-link both directions. ~1-1.5 hr/page.

Total: ~20-30 writer-hours across 8 weeks, fits the 6 hr/week budget with slack for SME wait time on items 1 and 3.

Next: verify the IAM role with infra/security for item 1 — that's the blocker on the whole queue.