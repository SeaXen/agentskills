# Windlass Docs Roadmap — Draft

**Source signal:** Beacontree ships (1) an in-browser "run this" sandbox on every docs page and (2) a three-column docs layout (nav / content / code panel). A Beacontree team member claimed a signup lift from the sandbox on a podcast — anecdotal, unsourced, no number attached. ⚠️ Treat as a hypothesis to validate, not a proven result, before sizing the bet.

---

## Item 1 — Interactive code sandbox on every docs page

- **Target:** end of quarter (2026-09-30) — **⚠️ 10 days out as of today.** A full-site rollout in that window is not realistic. Recommend committing to a **scoped Phase 1** by quarter-end and treating full coverage as a Q4 item.
- **Why:** live, editable, runnable code lowers time-to-first-success — the same mechanism the quickstart-conversion literature attributes signup lifts to. Independent of whether Beacontree's specific number holds up, the mechanism is sound.
- **Phase 1 (by 2026-09-30):**
  - Ship the sandbox on the Quickstart page only — highest-traffic, highest-intent page.
  - One language runtime to start (match Windlass's primary SDK language).
  - Instrument: sandbox-run rate, run→signup rate, quickstart completion rate. Baseline these *before* ship so the lift is measurable, not assumed.
- **Phase 2 (Q4 2026):** expand to top 10 guide pages by traffic, then full docs coverage.
- **Dependencies:** sandboxed execution environment (security review required — arbitrary code execution surface, rate-limit and isolate it). Flag to security before scoping.
- **Success metric:** signup rate from sandboxed pages vs. non-sandboxed control pages, measured 30 days post-launch. This is how we confirm or reject the Beacontree claim on our own funnel instead of inheriting theirs.
- **Risk:** shipping broad and fast to hit the quarter deadline without the security review is the likeliest failure mode. Don't compress that step to make the date.

## Item 2 — Three-column docs layout (nav / content / code panel)

- **Target:** none set — proposing **Q4 2026 / early Q1 2027**, sequenced after Item 1 Phase 1.
- **Why:** this is a structural rebuild (IA + layout), bigger surface area than the sandbox alone. It also becomes the natural permanent home for the sandbox's code panel, so building it after Phase 1 lets the sandbox UX inform the panel design instead of guessing upfront.
- **Scope:**
  - Persistent left nav, center content, right code panel (matches Beacontree's pattern).
  - Code panel hosts the Phase-1 sandbox output once both land, rather than a separate static snippet block.
  - Responsive fallback: collapse to two-column (nav + content, code panel inline) below desktop width — Beacontree's pattern likely assumes desktop developer traffic; verify Windlass's mobile/tablet docs traffic share before committing to this fallback design.
- **Dependencies:** Item 1 Phase 1 shipped (de-risks the code-panel content contract before the full layout rebuild).
- **Success metric:** time-on-page and internal-search-to-content-found rate, pre/post redesign — layout changes risk hurting findability even when they look better, so measure it directly rather than assuming the redesign is a pure win.

---

**Sequencing note:** Item 1 Phase 1 → Item 1 Phase 2 → Item 2. Running Item 2 first would mean rebuilding the code panel's shell before knowing what the sandbox actually needs to render.