# README audit — quillmark/parsely (audience: Java developers evaluating a streaming-CSV dependency)

No repo access here — this is a structural plan built from the section inventory you gave me, not a line-by-line audit. Before you commit, run `scripts/readme-audit.sh` against the real file and verify every flag/method name in Section 5 and Section 6 against source, per the skill's Step 4 — I can't confirm claims I haven't read.

## Diagnosis

**Band A:**
- A1 (identity) — likely pass if the logo doesn't push the description below the fold; check.
- A5 (licence reachable) — pass, Section 12 exists.
- A3 (every claim verifiable) — unscored here; the 61-method reference and 40-row config table are exactly where unverified claims hide. Verify before shipping.

**Band B — the number that matters:** median README is 7 sections, half sit between 5 and 12. You're at 12 sections and 1,400 lines — the section *count* is borderline, the *line count* is the actual problem. B8 (overflow lives elsewhere) is failing hard: five of your twelve sections are reference material or community-health content that has a conventional home outside the README and doesn't need to be read to decide whether to adopt the library.

**Missing, not present in your list — flag before you ship:**
- **B1, differentiation.** Nothing says why parsely over OpenCSV, Apache Commons CSV, or Jackson CSV. This is the scarcest, highest-leverage category (25.7% of READMEs have it) and costs three sentences.
- **A4, status.** No maturity/stability statement (semver policy, what's frozen vs. in flux). One sentence.

## Fix order (value per hour, not effort)

1. Delete the hand-written TOC — zero effort, removes 22 lines of maintenance debt.
2. Relocate the five overflow sections (API reference, config table, contributing, code of conduct, changelog) — mechanical, no writing required, this is most of your 1,400 lines.
3. Trim config and API sections to what most users touch, link the rest.
4. Add differentiation + status (currently missing — highest value per line of anything on this list).
5. Reorder what remains into a funnel.

## Section-by-section verdict

| # | Current section | Verdict | Action |
|---|---|---|---|
| 1 | Title + logo | **Keep, shrink** | Logo at reasonable size, not screen-filling. One sentence of identity right under it — name, "streaming CSV library for Java," the one thing that differentiates it (e.g., constant-memory / SAX-style parsing). |
| 2 | Table of Contents (22 entries) | **Delete** | GitHub renders an outline from headings automatically. A hand-written 22-entry TOC for a page you're about to cut to ~7 sections is also a stale-content risk the moment you edit a heading. |
| 3 | Installation (Maven + Gradle) | **Keep, trim** | Both snippets, plus the JDK version requirement stated as text (not just implied by the pom). Cut anything beyond the two dependency blocks — no build-tool history, no alternative package managers unless real. |
| 4 | Quick Start | **Keep, promote** | This is your highest-value section. One smallest-complete example with real output shown, not a fragment. Per the library skeleton, usage should sit *above* install — a reader who dislikes the API shape doesn't care how to install it. |
| 5 | Full API Reference (61 methods) | **Move to Javadoc / docs site** | Keep a "Core API" section in the README: 5–8 entry points a reader actually starts with (e.g. `CsvReader.of()`, `stream()`, `withHeaders()`), each one line. One-line pointer: `Full API reference: <javadoc URL>`. Zero readers evaluate a library by scrolling 61 signatures — that's B3-zero content (a bare list of signatures scores nothing as "usage"). |
| 6 | Configuration table (40 rows) | **Move, keep a stub** | Inline only the options most users actually set (buffer size, delimiter, quote char, charset, error-handling mode — pick the real top 5–8). One-line pointer to the full table in docs. |
| 7 | Contributing (~80 lines) | **Move to `CONTRIBUTING.md`** | One-line pointer in the README: `Contributing: see CONTRIBUTING.md`. GitHub already surfaces this file in the repo's own UI at the moment it matters — inlining it only adds scroll distance before a *user* (not a contributor) can decide anything. |
| 8 | Code of Conduct (full Contributor Covenant text) | **Move to `CODE_OF_CONDUCT.md`, delete from README** | No pointer needed beyond what the Contributing link already implies; GitHub's community-standards checklist picks up the file at the conventional path regardless of whether the README mentions it. |
| 9 | Security policy | **Move to `SECURITY.md`** | GitHub surfaces this in the repo's "Security" tab automatically once the file exists at the conventional path. Skip a README pointer unless you have enterprise/procurement readers who'd look for it here specifically — not indicated for this project. |
| 10 | Changelog (every release since 2021) | **Move to `CHANGELOG.md`** | One-line pointer: `Changelog: CHANGELOG.md`. A multi-year release history inline is pure scroll cost for someone deciding whether to adopt. |
| 11 | Credits | **Keep, shrink to one line or fold into footer** | A sentence with names/links, not a section. If there's a logo or sponsor requiring larger placement, that's the one exception worth keeping visible. |
| 12 | License | **Keep** | Name + link, stays near the bottom — fine for a permissive OSS licence (non-permissive would need to move near the top; confirm which parsely uses). |

## New skeleton (Library/SDK order, funnel-first)

1. Name + one-line description
2. Badge row — cap at 4, assessment signals only (latest version, licence, supported JDK versions, build status); cut anything conventional like "PRs welcome"
3. 2–4 sentence description: the problem, the streaming approach, the shape of the API
4. **Why parsely** *(new — currently missing)*: concrete axis vs. OpenCSV/Commons-CSV/Jackson — memory profile, throughput, or API ergonomics, whichever is real and checkable
5. Quick Start: smallest complete example + its output
6. Install: Maven and Gradle blocks, JDK version requirement
7. Core API: 5–8 entry points, one line each, link to full Javadoc for the rest
8. **Status** *(new — currently missing)*: one sentence — maintained/stable/semver policy
9. Configuration: top 5–8 options inline, link full table
10. Links out: full docs, changelog, contributing, licence pointers (one line each)
11. Licence + credits

## Result

~1,400 lines → roughly 150–220 lines in the README itself. Nothing is deleted outright except the hand-written TOC and the inline Code of Conduct text (both have zero destination value — GitHub already provides both mechanically). Everything else moves to its conventional file with a one-line pointer, so no content is lost, only relocated to where a reader who actually needs it will find it.

Companion files to create if they don't exist: `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, `CHANGELOG.md`, plus wherever the full API reference and full config table live (Javadoc site or a `/docs` page).