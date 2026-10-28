# QA Checklists — Gates A + B + C

## Gate A — cross-browser visual QA

Matrix: Chrome, Edge, Firefox, Safari (latest) x 1280 / 1440 / 1920 + 360 / 390 mobile.

Per route:
- [ ] No horizontal scroll at any width
- [ ] Header/footer/sticky correct, no overlap
- [ ] Flex/grid intact, no collapsed or overflowing cards
- [ ] Type, color, spacing (4/8pt), radius, shadow, icons match design system
- [ ] States checked: default, hover, active, focus-visible, disabled, loading, empty, error
- [ ] Focus ring visible, tab order sane, landmarks present, images have alt, contrast passes
- [ ] Screenshots saved: `qa/<route>-<browser>-<width>.png`

Output table:

| Route | Chrome | Edge | Firefox | Safari | Mobile 360 | Notes/fixes |
|-------|--------|------|---------|--------|------------|-------------|

## Gate B — performance

- [ ] Routes code-split, below-fold lazy-loaded
- [ ] Images: WebP/AVIF, sized srcset, lazy except hero, explicit width/height
- [ ] No unused deps (`npx depcheck` / `knip` clean); none > 50 kB gzipped unjustified
- [ ] No fetch waterfall / N+1; abort/cleanup listeners, timers, subs
- [ ] Cache headers + compression on; minified build
- [ ] Measured (throttled broadband, desktop): LCP <= 2.5s, CLS <= 0.1, INP <= 200ms, TBT <= 200ms, route JS <= 200 kB gzip

Record before/after: bundle kB, LCP, CLS, INP, TBT.

## Gate C — polish 10/10

- [ ] Spacing rhythm consistent, alignment pixel-clean at 100% + 125% zoom
- [ ] Hierarchy clear, line length 45-75 chars, no truncated text
- [ ] Touch targets >= 44px, no layout shift across breakpoints
- [ ] Empty/loading/error states designed, not blank
- [ ] Micro-interactions 150-250 ms ease, respect `prefers-reduced-motion`
- [ ] Dark/light (if any) both checked; print not broken where relevant
- [ ] Before/after screenshots for every fix, signed off 10/10
