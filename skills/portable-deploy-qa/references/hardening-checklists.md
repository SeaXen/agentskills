# Gates E-M — Hardening Checklists

## Gate E — Security (script: security_scan.py)
- [ ] Zero HIGH findings; MEDIUM reviewed and justified
- [ ] No secrets in repo; `.env` gitignored; `.env.example` has no real values
- [ ] No `eval` / `new Function` / shell exec in request paths
- [ ] TLS verification never disabled
- [ ] Cookies: httpOnly + secure + sameSite
- [ ] CORS explicit origins on authed routes (not `*`)
- [ ] Auth/authz checked server-side, not only client
- [ ] Inputs validated/sanitized; file uploads size+type limited
- [ ] Rate limiting on public/auth endpoints
- [ ] `npm audit` clean (or exceptions documented)

## Gate F — Accessibility (WCAG 2.1 AA)
- [ ] Full keyboard-only pass, no traps
- [ ] Visible focus indicator on every interactive element
- [ ] Heading hierarchy h1 -> h2 -> h3, no skips
- [ ] Landmarks: header/nav/main/footer
- [ ] Contrast: text 4.5:1, large text 3:1, UI components 3:1
- [ ] Every input labeled; errors announced
- [ ] Images have meaningful alt (decorative = empty alt)
- [ ] `prefers-reduced-motion` respected
- [ ] axe/Lighthouse: no critical or serious violations

## Gate G — SEO
- [ ] Unique title + meta description per route
- [ ] Open Graph + Twitter card tags
- [ ] Canonical URL; `lang` attribute set
- [ ] robots.txt + sitemap.xml present and correct
- [ ] 404 page; SPA fallback returns 200 HTML for deep links
- [ ] No console errors; no mixed content

## Gate H — Tests
- [ ] `npm test` passes, zero skipped, no `.only`
- [ ] Unit tests cover core logic
- [ ] API/integration tests for each route
- [ ] Build-output smoke test
- [ ] Critical paths covered

## Gate I — Reliability
- [ ] Every fetch/API call has error handling + timeout
- [ ] Retry/backoff on transient failures
- [ ] Error boundary at route level
- [ ] No unhandled promise rejections
- [ ] Loading / error / retry UI on async surfaces
- [ ] Graceful degradation if KV/R2/DB unavailable
- [ ] 404 + 500 pages styled

## Gate J — Docs & DX
- [ ] README follows `readme-standard.md` exactly
- [ ] `.env.example` matches code usage
- [ ] CONTRIBUTING.md, LICENSE present
- [ ] Clear commit/branch conventions

## Gate K — Observability
- [ ] Structured JSON logs in production
- [ ] Request IDs / correlation
- [ ] Error tracking (Sentry free tier or equivalent)
- [ ] `/healthz` (or `/api/health`) returns 200
- [ ] No secrets/PII logged
- [ ] Uptime check documented

## Gate L — Free-tier cost
- [ ] Every service has a free tier; no paid-only API
- [ ] Documented limits: Workers 100k req/day, D1 5M rows read/day, KV 100k reads/day, GH Actions 2000 min/mo
- [ ] What breaks at limit + fallback documented
- [ ] Sleep/hibernation behavior noted for Railway/Render/Fly
- [ ] Cold-start impact measured and stated

## Gate M — README & screenshots (blocking delivery gate)
Scripts: `check_readme.py <root>`, `capture_screenshots.py --root <root> --url <APP_URL> --routes ... --out docs/screenshots`

### M1 — README structure
- [ ] Title + one-line pitch + who it's for
- [ ] Screenshots section near the top
- [ ] Features / highlights
- [ ] Quick start with one copy-pasteable command
- [ ] Environment variable table (every var in code present, and vice versa)
- [ ] Architecture overview
- [ ] Deploy instructions for every supported platform
- [ ] Scripts table
- [ ] Troubleshooting section
- [ ] Contributing, License, Support
- [ ] No `create-next-app` / scaffold boilerplate
- [ ] `check_readme.py` exits 0

### M2 — Screenshots (real, not placeholders)
- [ ] >= 3 real screenshots of the running app
- [ ] Hero/home shot at 1440px, 2x scale
- [ ] At least one feature-in-action shot
- [ ] Mobile shot at 390px
- [ ] `contact-sheet.png` generated and present
- [ ] Every local image path in README resolves on disk
- [ ] Alt text describes the screen content
- [ ] Captions under each image
- [ ] No secrets, personal data, or fake placeholder art
- [ ] Screenshots regenerated after any UI change (no stale UI in docs)

### M3 — Multi-app consistency (workspace mode)
- [ ] All apps use the same README section order
- [ ] Same screenshot directory + naming convention
- [ ] Same env var naming for shared concepts
- [ ] Same deploy platform coverage
- [ ] Aggregate report lists every app, including skipped ones with reasons
