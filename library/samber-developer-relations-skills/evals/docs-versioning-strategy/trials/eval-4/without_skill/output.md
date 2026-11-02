# Tarnhelm docs: version banners and version switcher

## Decisions I need from you

1. **Don't reuse the old-version banner on 5.0 beta.** It says "You are viewing an older version", which is false on a pre-release. A reader would think 5.0 beta is stale and 4.x is newer. Use one banner component with a message per status (below). That is still one component to maintain, not two.
2. **Change the docs home from 5.0 beta to 4.x.** Today most readers, and Google, land on a beta. Keep beta one click away and badged. Beta pages should also be `noindex` or canonical to the matching 4.x page, so search results don't send people to pre-release docs.
3. **The CVE needs a decision.** The 2.x banner copy below assumes you'll publish an advisory. I've left a placeholder for the CVE ID. Please confirm two things:
   - Does 1.x share the XML parser? If it does, it gets the same banner.
   - Is a documented mitigation available? If there is none, say so in the banner. Don't put technical detail of the flaw on public pages.
4. **I can't verify "31 versions".** I don't know your minor-release counts, so the spec generates the list from a manifest instead of hard-coding it. Please send the real list. Also confirm that each minor has its own docs tree, such as `/docs/4.3/`, rather than one tree per major.

## Banner copy

All variants use one component, `<VersionBanner status=… />`, driven by `versions.json`. Links go to the same page in the target version when it exists. If it doesn't, they go to that version's root. They never go to the docs home.

| Status | Versions | Copy | Link |
|---|---|---|---|
| `beta` | 5.0 | **Tarnhelm 5.0 beta.** This version is a pre-release and may change before general availability. For production use, see the current docs. | Go to 4.x docs (this page) |
| `supported` | 3.x | **You're viewing Tarnhelm 3.x.** This version still receives fixes, but 4.x is current. | Go to 4.x docs (this page) |
| `unsupported` | 1.x | **Tarnhelm 1.x is no longer supported** and won't receive fixes, including security fixes. These docs stay online for reference. | Go to 4.x docs (this page) |
| `unsupported` + `advisory` | 2.x | **Tarnhelm 2.x is no longer supported and has a known, unpatched security vulnerability in its XML parser ([CVE-YYYY-NNNNN]).** Upgrade to 3.x or later. [Mitigation: one sentence from the advisory, or "no mitigation is available".] | Read the advisory · Upgrade guide |
| `current` | 4.x | No banner. | none |

Behavior:
- The `beta` and `supported` banners can be dismissed for the session. The `unsupported` and `advisory` banners can't be dismissed.
- Use `role="region"` with `aria-label="Version notice"`, not `role="alert"`. Contrast must meet WCAG AA.
- The `advisory` banner gets a distinct warning style. The other variants share a neutral style.
- If the 1.x docs are affected too, add `advisory` to 1.x. The flag is data, so no code change is needed.

## Version-switcher spec

### Data: `versions.json` (single source of truth)

```json
[
  { "version": "5.0", "label": "5.0 beta", "status": "beta", "path": "/docs/5.0/" },
  { "version": "4.7", "label": "4.7", "status": "current", "path": "/docs/4.7/" },
  { "version": "3.x", "…": "one entry per released minor, through 1.0" },
  { "version": "2.9", "label": "2.9", "status": "unsupported",
    "advisory": { "id": "CVE-YYYY-NNNNN", "url": "/security/CVE-YYYY-NNNNN" }, "path": "/docs/2.9/" }
]
```

- The build fails if `versions.json` and the docs tree disagree. That check also catches a count that isn't 31 plus the beta.
- The build emits a `pages-by-version.json` page manifest. The "same page in another version" links use it, with a fallback to the version root.

### Dropdown

- List all released versions, one entry per minor, plus 5.0 beta. Enterprise readers need exact versions.
- Group by major, newest first, with a status badge on each entry: `beta`, `current`, `supported`, `unsupported`. 2.x entries also get a warning marker.
- Use a native `<select>` with `<optgroup>` for a first implementation. It gives you keyboard and screen-reader support for free. Only build a custom widget if you need search.
- The trigger always shows the current page's version and its badge.
- Choosing a version navigates to the same page in that version, with the root as fallback. It also writes the preference (see below).

### Remembered version

- **Storage:** write a first-party cookie, `tarnhelm_docs_version=<version>`, only when the reader picks a version in the dropdown. Use `Path=/docs; Max-Age=180 days; SameSite=Lax; Secure`. There is no tracking and no third parties.
- **Consent:** this is a user-initiated preference. I expect it to count as functional, so no consent banner is needed. Confirm with whoever owns your GDPR position. It also fits your rule of refusing data collection on cookie banners.
- **Redirect:** run an inline script in `<head>` so there is no flash. Redirect only when all of these are true:
  1. `document.referrer` is a search engine host.
  2. The cookie exists and names a version different from the landing page's version.
  3. The target page exists in the manifest. If it doesn't, don't redirect.
  4. A session flag, `sessionStorage`, shows no redirect has happened yet. This prevents loops.
- **Crawlers:** crawlers send no cookie, so they always see the real page. Keep canonical tags intact so the redirect can't create duplicate-content problems.
- **After redirect:** the destination shows its normal banner. A reader pinned to 2.x therefore sees the CVE banner on every visit. That is intended, because silently returning people to an unpatched version without a warning would be the wrong outcome.
- **Opt-out:** the dropdown has a "Reset to latest" item that clears the cookie.

### Acceptance checks

- Each status renders the right banner, and 4.x renders none.
- The 2.x banner contains the CVE ID and can't be dismissed.
- No banner link points at the docs home.
- The dropdown count equals `versions.json`.
- A Google-referred visit with the cookie set lands on the preferred version. Without the cookie, or with a missing page, it doesn't redirect.
- Two consecutive redirects don't occur.