# QA Checklists — Gates A + B + C

> Before running any of these, scope the gates to the app:
> `python scripts/gate_scope.py --root <app_root>` — a gate the app cannot have
> is reported as skipped, never as a failure and never as a pass.

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

**Capture it (all installed engines, one command):**

```bash
python scripts/capture_screenshots.py --root <app_root> --url <APP_URL> \
    --routes /,/dashboard --out docs/screenshots --browsers chromium,firefox,webkit
```

The script writes one PNG per engine (`<slug>-<browser>.png`), a `contact-sheet.png` and a
`manifest.json` recording the engines used, the engines skipped (not installed), the routes and any
console errors. **The manifest is the Gate A evidence** — screenshots alone prove nothing about
which engine rendered them.

Engines that are not installed are reported as *skipped*, never as a pass. Install them with
`python -m playwright install chromium firefox webkit`.

Output table:

| Route | Chrome | Edge | Firefox | Safari | Mobile 360 | Notes/fixes |
|-------|--------|------|---------|--------|-------------|-------------|

## Gate B — performance

- [ ] Routes code-split, below-fold lazy-loaded
- [ ] Images: WebP/AVIF, sized srcset, lazy except hero, explicit width/height
- [ ] No unused **runtime** deps; none > 50 kB gzipped unjustified
- [ ] No fetch waterfall / N+1; abort/cleanup listeners, timers, subs
- [ ] Cache headers + compression on; minified build
- [ ] No source maps shipped to production
- [ ] Measured (throttled broadband, desktop): LCP <= 2.5s, CLS <= 0.1, INP <= 200ms, TBT <= 200ms, route JS <= 200 kB gzip

**Measure it:**

```bash
python scripts/bundle_report.py <app_root>          # route JS budget 200 kB gz, per-asset 50 kB gz
python scripts/lighthouse_run.py --url <APP_URL> --routes /,/dashboard   # LCP / CLS / TBT
```

`bundle_report.py` reads the Vite manifest (`dist/.vite/manifest.json`) or the Next build manifest
when available, falls back to the total-JS estimate, and reports gzip sizes, oversized assets,
shipped source maps, oversized images and unused runtime dependencies. Exit `2` when there is no
build output — an unbuilt app has no measurable budget.

Record before/after: bundle kB, LCP, CLS, INP, TBT.

## Gate C — polish 10/10

- [ ] Spacing rhythm consistent, alignment pixel-clean at 100% + 125% zoom
- [ ] Hierarchy clear, line length 45-75 chars, no truncated text
- [ ] Touch targets >= 44px, no layout shift across breakpoints
- [ ] Empty/loading/error states designed, not blank
- [ ] Micro-interactions 150-250 ms ease, respect `prefers-reduced-motion`
- [ ] Dark/light (if any) both checked; print not broken where relevant
- [ ] Before/after screenshots for every fix, signed off 10/10

**Gate C is the one gate no script can certify.** `verify_claims.py` reports it as `UNVERIFIABLE`
by design — sign it off with the checklist and before/after screenshots, not with a claim in the
report.

## Depth gates N-U

The business-rules, load, migration, privacy, i18n, screen-reader, payment/email and code-quality checklists live in [depth-gates.md](depth-gates.md). Each one names the script that proves it:

- N business rules (executable contract + domain sign-off) - `business_logic_check.py` (+ `qa/scenarios.json` + `qa/signoff/business-rules.json`)
- O load & soak - `load_check.py` (p95, error rate, drift)
- P migrations & schema - `migration_check.py` (rollback, destructive DDL)
- Q privacy & GDPR (policy + legal sign-off) - `privacy_check.py` (+ `qa/signoff/privacy.json`)
- R i18n & RTL - `i18n_check.py` (locales, keys, RTL)
- S screen-reader contract - `at_check.py` (labels, live regions, landmarks)
- T payment & email flows - `payment_email_check.py` (card data, webhook signature)
- U code quality & AI risk - `code_quality.py` (complexity, duplication, dead code)

Gates N and Q are only VERIFIED when the machine half passes **and** a
fingerprint-bound human sign-off exists. Without it they stay UNVERIFIABLE -
never silently green. See [deep-modes.md](deep-modes.md) §6.

