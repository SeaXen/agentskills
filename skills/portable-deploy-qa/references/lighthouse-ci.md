# Lighthouse CI — Gate D (desktop)

Run manually + in CI against the detected `$APP_URL` (Section 0). Incognito, desktop preset, Home + 2 key routes from `$ROUTES`.

## Thresholds

Performance >= 90, Accessibility >= 95, Best Practices >= 95, SEO >= 90.
Any miss needs a fix or a written fix-plan — never silently pass.

## Manual run

```bash
APP_URL="${APP_URL:-http://localhost:3000}"   # use detected value, e.g. http://localhost:5173 for Vite
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
