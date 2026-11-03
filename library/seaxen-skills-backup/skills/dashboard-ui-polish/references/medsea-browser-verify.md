# MedSea browser verify (dashboard-ui-polish companion)

When user asks **"did you verify in browser?"** after header/exam/flashcards polish on `:8855`:

1. Do not answer yes from curl or snapshot alone.
2. Run minimum probe in `sagar-hermes-ops` → `references/medsea-live-browser-verification.md`.
3. Pass criteria: `window.MedSea` true, topic URL fills `#topic-filter`, avail count not `—`, Start opens runner.

Pointer only — full recipe lives in **sagar-hermes-ops**.