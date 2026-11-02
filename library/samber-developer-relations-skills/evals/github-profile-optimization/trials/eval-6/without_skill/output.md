Kill "currently building [scheduler]" line first. Most damage, fastest fix, do it now.

**5 steps, ~2h work inside your 4h budget:**

1. **Rewrite intro (20 min).** Delete stale "currently building" line — project-status framing goes stale again next year. Use role-based framing instead (doesn't expire). Add one self-expiring line pointing to the talk — zero upkeep, high relevance exactly when eyes land on profile. Template below.
2. **Banner: fix or cut, 15 min cap (15 min).** Open image URL direct in browser. Typo/dead path → fix. Anything else → delete image line, keep plain text header. Don't burn budget debugging a decorative asset you'll never touch again.
3. **Set 6 pins (45 min).** Pick live, non-archived repos tied to Go / talk topic. Archived scheduler stays unpinned — it's the thing you're moving away from.
4. **Check pinned repo descriptions (30 min).** One-line description + topics per repo, only where missing or wrong. Skip repos already fine — don't redo all 6 blind.
5. **QA logged-out (15 min).** Open profile in incognito. Confirm: banner renders or absence looks clean, intro reads right, all 6 pins visible and public (private repo = blank pin to visitors). Repeat this 5-min check morning of Nov 3 — catches CDN cache lag or a repo someone else silently flipped private.

**Skip entirely:** stats cards, streak widgets, visitor counters, GitHub Actions automation. Gh-profile skill pushes these hard, but each is an external dependency that can silently break later, and you said nobody revisits this file — zero payoff for the maintenance risk.

Intro template — fill brackets, this part is normal prose since it's README content, not chat:

```markdown
Hi, I'm Renske — [your role, e.g. "backend engineer working on distributed systems in Go"].

Speaking at [conference name] on Nov 3, 2026: "[talk title]".
```

Next: open README now, delete the stale scheduler line.