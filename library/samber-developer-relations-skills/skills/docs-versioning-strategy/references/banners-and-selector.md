# Banners and version selector behaviour

Load at Step 6, when writing banner copy or specifying how the switcher behaves.

## Banner anatomy

Every banner on a non-current page carries three parts, in this order:

1. **Status word** the reader recognises: unreleased, not the latest, unsupported, insecure, static snapshot, archived.
2. **Consequence** in the reader's terms: may describe features not yet installable, no longer receives fixes, has known security issues.
3. **Same-page link** to `current`, falling back to the nearest ancestor section when the page no longer exists.

```
// ✓ Good - status, consequence, same-page link
This page documents v2.4, which no longer receives fixes. See this page for the current version (3.1).

// ✗ Bad - no status word, no consequence, links to the docs home
You are viewing an older version. Go to the docs.
```

## Templates per state

| State | Template |
| --- | --- |
| `next` | "This page documents an unreleased version. Features here may change or not ship. See this page for the current release ({current})." |
| `maintained` | "This page documents {version}, a supported older release. See this page for the latest release ({current})." |
| `frozen` | "{version} is no longer supported and this page is a static snapshot. Upgrade, and see this page for the current version ({current})." |
| `frozen`, security-relevant product | "{version} is no longer supported and has known security issues. Upgrade, and see this page for the current version ({current})." |
| `archived` index | "These versions are archived and receive no updates. Each page links to its current equivalent where one exists." |

Keep `next` wording distinct from `frozen` wording: PostgreSQL reuses its "unsupported version" banner on devel docs, which tells beta readers the opposite of what is true.

## Real wordings, for calibration

- PostgreSQL: "This documentation is for an unsupported version of PostgreSQL. You may want to view the same page for the current version, or one of the other supported versions listed above instead."
- Kubernetes: "Kubernetes v1.34 documentation is no longer actively maintained. The version you are currently viewing is a static snapshot. For up-to-date information, see the latest version."
- Django: "This document is for an insecure version of Django that is no longer supported. Please upgrade to a newer release!"
- Angular: "This is the archived documentation for Angular v17. Please visit angular.dev to see this page for the current version of Angular."

Django added its banner partly to ward off tickets and pull requests against old versions: a banner also reduces maintainer load.

## Selector behaviour

**Do:**

- Default to `current`; give `next` a visible label (Spring groups "Stable / Preview / Snapshot").
- Keep the reader on the same page when switching; fall back to the nearest ancestor section with a one-line notice.
- Group `frozen` versions under an "Older versions" heading; list `archived` ones on an archive index page, not in the dropdown.
- Show which versions are supported next to their labels (PostgreSQL's header splits supported, development and unsupported).
- Link the alias (`latest`, `stable`, `current`) from support replies, README and blog posts.

**Don't:**

- List every version ever released in one dropdown; SciPy's list ran off the bottom of the screen.
- Auto-redirect visitors from search results to a remembered version; PostgreSQL contributors listed cookie redirects from search visits as not recommended.
- Drop the reader on the version root or a 404 when the page is missing in the target version.

No public study measures selector use or switching success. Instrument switcher clicks and switcher 404s before treating any selector change as an improvement.
