## Classification calls — Beacon Ledger docs

**(1) reference/api/transactions.md**
File as **reference**. Endpoint table mirrors the product shape, consulted mid-work — textbook reference. The one-sentence immutability explanation is nowhere near the mixing threshold (SKILL.md Step 3: flag only when the second mode is "roughly a fifth" of the page). This is the exact negative example in `diataxis-classification.md`: *"Reporting 'this reference page contains one explanatory sentence' as a finding. That sentence is doing its job."*
**Not a finding.**

**(2) docs/adr/0007…0031**
Don't run these through the four-quadrant compass at all. `diataxis-classification.md` names this pattern explicitly: *"An ADR directory (`docs/adr/`, sequential numbering, immutable once accepted…) is already correctly typed. Do not flag it for not fitting the four-quadrant split."* Log them in the inventory (owner, staleness) but skip mode classification.
**Not a finding** — unless a separate Step 5 mechanical check fails (orphaned from nav, broken supersession links), which is a nav-drift finding, not a classification one.

**(3) release-notes/2026-q2.md**
Hard case, stated directly: *"Release notes / changelog: reference (consulted at work, describes the machinery's history)."* File as reference.
**Finding only if placement disagrees** — e.g. it's filed under "Guides" or absent from nav entirely. On the facts given (just a page existing), there's nothing to flag yet. Check where it actually sits before deciding.

**(4) guides/upgrading-to-v4.md**
Hard case, stated directly: *"Migration guides that walk through upgrading are how-to guides."* Already in `guides/` → mode matches placement.
**Not a finding**, on the facts given. Only flag it if it also carries a full compatibility/breaking-change reference table inline at ≥~⅕ of the page — that would be the "numbered steps followed by a full option table" mixing symptom (how-to + reference). You haven't described a table, so don't manufacture one.

**(5) faq.md — 40 questions, pricing to a 6-step cert rotation**
Hard case, stated directly: *"FAQ: usually a symptom, not a mode — each entry belongs to a real mode. Keep the FAQ as an index if search is weak, and file the answers properly."* A 40-entry FAQ spanning pricing (not even docs — commercial) through a 6-step procedure is the symptom in concentrated form.
**This is a finding.**

```
[should fix] faq.md
- Now: 40 entries spanning at least three modes — pricing (out of docs scope), a 6-step
  certificate-rotation procedure (how-to), presumably conceptual and reference entries mixed in.
  Single URL, no mode-appropriate placement for any of them.
- Reader impact: someone mid-incident rotating a certificate has to scan an unrelated FAQ list
  instead of landing on a titled how-to; the procedure is invisible to anyone who doesn't think
  to check "FAQ" for it.
- Next action: extract the 6-step cert rotation into guides/rotate-a-certificate.md (or similar);
  keep faq.md as a short index linking to the real pages for the questions that have one.
```
Severity: bump to **must fix** if cert rotation shows up as a recurring support/search signal (Step 4's demand-signal rule applies here too) or sits on the adoption path; otherwise **should fix** is right. Don't try to re-mode the other 39 entries individually in this pass — flag the page-level symptom once, per the "one action per finding" rule, and let the team triage entries during the split.

**(6) troubleshooting/errors.md — 60 codes, 12 with fix procedures**
Hard case, stated directly: *"Troubleshooting / error pages: how-to when they prescribe a fix, reference when they enumerate error codes. Split when both."* You have both. 12/60 by *entry count* sits right at the ~⅕ mixing line, but the threshold is about page content, not entry count — a fix procedure runs several lines longer than a bare code+description row, so 12 procedures almost certainly occupy well over a fifth of the page.
**This is a finding.**

```
[should fix] troubleshooting/errors.md
- Now: enumerates 60 error codes (reference) but 12 embed step-by-step fix procedures inline
  (how-to) — procedural content likely exceeds a fifth of the page by length even though it's a
  fifth of entries by count.
- Reader impact: someone scanning for a code's meaning wades through fix steps for unrelated
  codes; someone mid-fix has to find their procedure inside a 60-row reference table instead of
  a titled how-to.
- Next action: keep all 60 codes in the reference table; move the 12 fix procedures into
  how-to pages (or one grouped troubleshooting how-to), link each reference row to its fix.
```
Severity: **must fix** if error resolution is a common support-driven need on the adoption path (worth confirming with a demand signal per Step 4); otherwise **should fix**.

**(7) docs/index.md**
Hard case, stated directly: *"Landing / index pages: not a mode — judge them on whether they route to all four."* Don't classify it; audit its links.
**Finding only if it fails to route to one or more modes** — most commonly "no route to a tutorial/quickstart" or "no route to explanation," which lands as **must fix** under the severity tier ("no entry point for a primary audience"). You haven't told me what it links to — check that before filing anything here.

**(8) reference/glossary.md**
Hard case, stated directly: *"Glossary: reference."* File as reference.
**Not a finding**, unless Step 5's vocabulary check turns up terms defined here that are named differently elsewhere in the docs (the "project/workspace/org" split-vocabulary symptom) — that's a real finding, but it's a Step 5 nav-truth finding, not a classification one, and needs a cross-page comparison you haven't given me yet.

---

### One thing to flag before you keep going

190 findings at partway through a 340-page inventory is heading toward the failure mode the skill names explicitly: *"Over-flagging — 200 findings on a 200-page site → Report only the pages where a reader's need actually fails."* Three of your eight examples here (1, 2, 8) were "not a finding" by the skill's own worked/negative examples and hard-case list — if similar calls elsewhere in your 190 leaned toward flagging rather than the skill's defaults, it's worth a pass back through them against `diataxis-classification.md`'s worked examples before you finalize the queue. A finding whose fix isn't a single doable-in-one-sitting action, or whose only defect is "not Diátaxis-pure," should be cut per Step 8 and the negative example in `audit-report-template.md`.