# Lighthouse CI — Gate D (desktop)

Run manually + in CI against the detected `$APP_URL` (Section 0). Incognito, desktop preset, Home + 2 key routes from `$ROUTES`.

## Thresholds

Performance >= 90, Accessibility >= 95, Best Practices >= 95, SEO >= 90.
Any miss needs a fix or a written fix-plan — never silently pass.

## Manual run — use the runner, not a raw npx call

```bash
# Runs Lighthouse, writes the artifacts and FAILS when a score is below target.
python scripts/lighthouse_run.py --url <APP_URL> --routes /,<route2> --out qa/lighthouse
```

The runner picks a Lighthouse binary in this order: `node_modules/.bin/lighthouse` → global
`lighthouse` → `npx --yes lighthouse@12`, and finds Chrome via `CHROME_PATH` → the Playwright
Chromium binary → `PATH`. It writes:

```
qa/lighthouse/lighthouse-<route>.json      raw Lighthouse report
qa/lighthouse/lighthouse-<route>.html      viewable report
qa/lighthouse/lighthouse-summary.json      scores + metrics vs thresholds (the Gate D evidence)
```

Thresholds can be overridden: `--perf 90 --a11y 95 --bp 95 --seo 90`.

Exit codes: `0` all thresholds met · `1` a score is below target · `2` Lighthouse could not run
(reported as `SKIPPED` — never a pass).

Raw invocation, only when you need the interactive view:

```bash
npx lighthouse "$APP_URL/" --preset=desktop --view
npx lighthouse "$APP_URL/<route2>" --preset=desktop --output=html --output-path=qa/lh-route2.html
```

Save HTML + JSON under `qa/`.

## CI (`.github/workflows/ci.yml` snippet)

```yaml
- run: $PKG run build
- run: $PKG start & npx wait-on $APP_URL/$HEALTHZ
- uses: treosh/lighthouse-ci-action@v12
  with:
    urls: |
      $APP_URL/
      $APP_URL/<route2>
      $APP_URL/<route3>
    configPath: ./lighthouserc.json
    uploadArtifacts: true
```

> Substitute detected `$APP_URL` (e.g. `http://localhost:5173`, `http://localhost:4200`, `http://localhost:8080`) and `$ROUTES` before running. Never hardcode `:3000`.

`lighthouserc.json`:

```json
{
  "ci": {
    "assert": {
      "preset": "lighthouse:recommended",
      "assertions": {
        "categories:performance": ["error", { "minScore": 0.9 }],
        "categories:accessibility": ["error", { "minScore": 0.95 }],
        "categories:best-practices": ["error", { "minScore": 0.95 }],
        "categories:seo": ["error", { "minScore": 0.9 }],
        "largest-contentful-paint": ["error", { "maxNumericValue": 2500 }],
        "cumulative-layout-shift": ["error", { "maxNumericValue": 0.1 }],
        "total-blocking-time": ["error", { "maxNumericValue": 200 }]
      }
    }
  }
}
```

## Report table (paste into PR/README)

| Route | Perf | A11y | BP | SEO | LCP | CLS | TBT | Report |
|-------|------|------|----|-----|-----|-----|-----|--------|

Fix all error-level diagnostics: unused JS/CSS, unsized images, render-blocking, a11y violations.

The same numbers come from `qa/lighthouse/lighthouse-summary.json`; copy them from there instead of
transcribing by hand so the report cannot drift from the artifact.

## What this gate does not cover

- INP is a field metric — it cannot be measured by Lighthouse. Use it only from real-user data
  (`web-vitals` library) and say where the number came from.
- Lighthouse scores a *lab* run. It does not prove the app is fast on a user's phone.
- A perfect Lighthouse score says nothing about design polish (Gate C) or business correctness.
