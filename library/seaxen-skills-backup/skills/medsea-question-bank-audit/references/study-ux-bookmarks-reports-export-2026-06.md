# MedSea study UX — bookmarks, reports, export (2026-06-24)

Local-first queues in `exam-engine.js` (localStorage). No server sync.

## APIs (`window.MedSea`)

| Store | Key | Use |
|-------|-----|-----|
| `Flagged` | `medsea_flagged_v1` | Weak queue — auto on submit miss + manual in review |
| `Bookmarks` | `medsea_bookmarks_v1` | Star questions; **Bookmarks only** exam chip |
| `Reports` | `medsea_reports_v1` | ⚑ Report issue (prompt note, max 200 entries) |
| `SpacedRep` | `medsea_sr_v1` | Flashcard due dates (again/hard/known intervals) |

`downloadStudyExport()` — JSON blob: flagged, bookmarks, reports, spaced_rep, `exported_at`.

**UI:** Exam → History → **Export study data (JSON)**.

## Setup chips

- **Weak queue only** — `SETUP.flaggedOnly`; clears when **All** / **Clear** chapters
- **Bookmarks only** — `SETUP.bookmarksOnly`; pool filter `MedSea.Bookmarks.has(q.id)` (exam **and** flashcards chip `#ch-fc-bookmarks`)

**Flashcards runner:** `#btn-fc-bookmark` toggles same `Bookmarks` store; use `.rate-btn[data-rate]` only for rating buttons (bookmark button has no `data-rate`).

**Exam defaults:** first visit sets `medsea_default_authored=1` and checks **Authored only** unless URL has `authored=0`. User toggle persists in localStorage.

**Rationale honesty in UI:** when `q.explanation_source === 'correct_option'`, show small note *(from correct option text in source)* — do not imply a dedicated `—` line existed.

## Review actions (per question)

- ☆ Flag / ★ Flagged
- 🔖 Bookmark / 🔖 Saved
- ⚑ Report issue → `Reports.add(id, note, { url })`

## Home + chapter discovery

- `assets/medsea-home-stats.js` — header stats from `questions-index.json` + optional `topics.json`
- `site-header.js` — `?topic=` sticky bar → Exam + Flashcards (authored=1)
- Home search hits — **▶ Exam this topic** link

## Feature matrix

Canonical list: `site/docs/FEATURES.md` in repo (ship with tar deploy).

## Honesty

Export is **browser-local backup** for the user to triage reports — not a ticket system. Clinical 10/10 still requires source rationales + expert review.