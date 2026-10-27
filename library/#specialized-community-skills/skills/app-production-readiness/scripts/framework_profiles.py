#!/usr/bin/env python3
"""Framework profiles: what each framework injects for you.

Why this exists
---------------
A generic review tool reasons about *source files*, but a modern framework
generates the page at runtime.  Next.js App Router, for example:

* injects ``<meta name="viewport" content="width=device-width, initial-scale=1">``
  unless the app exports its own ``viewport``;
* lets every page inherit ``metadata.title`` from the root layout, so
  "this page has no ``<title>``" is really "this page has a duplicate title";
* ships a dev-only HMR websocket client whose console errors are not app
  defects;
* puts the production bundle in ``.next/static`` - a directory that also
  exists after a *failed* build.

Each of those produced a false positive on a real review.  This module is the
single place where such framework knowledge lives, so the gates can ask
"is this the app's fault or the framework's default?".

Nothing here is framework-specific magic that cannot be checked: every
default is verified against the repository (a ``next.config.*`` file, an
``app/`` or ``src/app/`` directory, a ``vite.config.*`` file, ...).  If the
markers are absent the profile falls back to "unknown" and the gates keep
their strict behaviour.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

# --------------------------------------------------------------------------
# the profiles
# --------------------------------------------------------------------------

PROFILES = {
    "next-app": {
        "label": "Next.js (App Router)",
        "markers": ["next.config.js", "next.config.mjs", "next.config.ts",
                    "next.config.cjs"],
        "app_dirs": ["app", "src/app"],
        # Next.js injects a default viewport meta unless `export const viewport`
        # is present in the root layout.
        "injects_viewport": True,
        # `export const metadata` in the root layout is inherited by every page.
        "inherits_layout_title": True,
        # A dev server always logs HMR websocket errors; they are not app bugs.
        "dev_console_noise": [
            r"_next/webpack-hmr",
            r"_next/static/webpack/hmr",
            r"ERR_INVALID_HTTP_RESPONSE",
            r"WebSocket connection to .* failed",
            r"Fast Refresh had to be performed",
            r"\[HMR\]",
            r"React DevTools",
            r"Download the React DevTools",
        ],
        # The production bundle lives here.  A dev server also writes here, so
        # the presence of the directory proves nothing - only `.next/BUILD_ID`
        # or a `prerender-manifest.json` does.
        "build_output": ".next/static",
        "build_markers": [".next/BUILD_ID", ".next/prerender-manifest.json"],
        "security_headers_by_default": False,
        "notes": [
            "Next.js injects a default responsive viewport meta at runtime",
            "pages inherit `metadata.title` from the root layout",
            "the dev server always logs HMR websocket console errors",
        ],
    },
    "next-pages": {
        "label": "Next.js (Pages Router)",
        "markers": ["next.config.js", "next.config.mjs", "next.config.ts",
                    "next.config.cjs"],
        "app_dirs": ["pages", "src/pages"],
        "injects_viewport": True,
        "inherits_layout_title": False,
        "dev_console_noise": [
            r"_next/webpack-hmr",
            r"ERR_INVALID_HTTP_RESPONSE",
            r"WebSocket connection to .* failed",
            r"\[HMR\]",
        ],
        "build_output": ".next/static",
        "build_markers": [".next/BUILD_ID", ".next/prerender-manifest.json"],
        "security_headers_by_default": False,
        "notes": ["Next.js injects a default responsive viewport meta at runtime"],
    },
    "remix": {
        "label": "Remix",
        "markers": ["remix.config.js", "remix.config.mjs", "remix.config.ts"],
        "app_dirs": ["app", "src/app"],
        "injects_viewport": False,
        "inherits_layout_title": True,
        "dev_console_noise": [r"/socket", r"WebSocket connection to .* failed"],
        "build_output": "build/client",
        "build_markers": ["build/index.js"],
        "security_headers_by_default": False,
        "notes": ["the root layout owns the document head (title, meta, viewport)"],
    },
    "astro": {
        "label": "Astro",
        "markers": ["astro.config.mjs", "astro.config.ts", "astro.config.js",
                    "astro.config.cjs"],
        "app_dirs": ["src/pages", "src/pages"],
        "injects_viewport": False,
        "inherits_layout_title": True,
        "dev_console_noise": [r"\[vite\]", r"hmr"],
        "build_output": "dist",
        "build_markers": ["dist/index.html"],
        "security_headers_by_default": False,
        "notes": ["Astro layouts own the document head"],
    },
    "nuxt": {
        "label": "Nuxt",
        "markers": ["nuxt.config.ts", "nuxt.config.js", "nuxt.config.mjs"],
        "app_dirs": ["pages", "app", "src/pages"],
        "injects_viewport": True,
        "inherits_layout_title": True,
        "dev_console_noise": [r"\[vite\]", r"hmr", r"__nuxt_devtools__"],
        "build_output": ".output/public",
        "build_markers": [".output/server/index.mjs"],
        "security_headers_by_default": False,
        "notes": ["Nuxt injects a default viewport meta"],
    },
    "sveltekit": {
        "label": "SvelteKit",
        "markers": ["svelte.config.js", "svelte.config.ts"],
        "app_dirs": ["src/routes", "routes"],
        "injects_viewport": False,
        "inherits_layout_title": True,
        "dev_console_noise": [r"\[vite\]", r"hmr"],
        "build_output": "build",
        "build_markers": ["build/index.html"],
        "security_headers_by_default": False,
        "notes": ["the root +layout owns the document head"],
    },
    "vite": {
        "label": "Vite (SPA)",
        "markers": ["vite.config.js", "vite.config.ts", "vite.config.mjs"],
        "app_dirs": [],
        "injects_viewport": False,
        "inherits_layout_title": False,
        "dev_console_noise": [r"\[vite\]", r"hmr"],
        "build_output": "dist",
        "build_markers": ["dist/index.html"],
        "security_headers_by_default": False,
        "notes": [],
    },
    "static": {
        "label": "static site (no framework)",
        "markers": [],
        "app_dirs": [],
        "injects_viewport": False,
        "inherits_layout_title": False,
        "dev_console_noise": [],
        "build_output": None,
        "build_markers": [],
        "security_headers_by_default": False,
        "notes": [],
    },
}

DEFAULT_PROFILE = PROFILES["static"]


# --------------------------------------------------------------------------
# detection
# --------------------------------------------------------------------------

DEP_MARKERS = {
    "next-app": ("next",),
    "next-pages": ("next",),
    "remix": ("@remix-run/react", "@remix-run/node", "@remix-run/dev"),
    "astro": ("astro",),
    "nuxt": ("nuxt", "nuxt3"),
    "sveltekit": ("@sveltejs/kit",),
    "vite": ("vite",),
}


def _package_dependencies(root: Path):
    try:
        import json
        data = json.loads((root / "package.json").read_text(encoding="utf-8", errors="ignore"))
    except Exception:
        return set()
    if not isinstance(data, dict):
        return set()
    names = set()
    for key in ("dependencies", "devDependencies", "peerDependencies"):
        block = data.get(key) or {}
        if isinstance(block, dict):
            names.update(k.lower() for k in block)
    return names


def detect(root) -> str:
    """Return the framework key for ``root`` (``static`` when unknown)."""
    root = Path(root)
    deps = _package_dependencies(root)
    for key, profile in PROFILES.items():
        if key == "static":
            continue
        has_marker = any((root / m).exists() for m in profile["markers"])
        has_app_dir = any((root / d).is_dir() for d in profile.get("app_dirs", []))
        has_dep = any(d in deps for d in DEP_MARKERS.get(key, ()))
        if not (has_marker or has_dep):
            continue
        # A framework config alone is not enough - Remix and Astro configs can
        # live in a repo that also carries a Next.js app.  The app directory
        # decides when the profile declares one.
        if profile.get("app_dirs") and not has_app_dir:
            continue
        return key
    # Next.js with only a config and no app/pages dir is still Next.js.
    if any((root / m).exists() for m in PROFILES["next-app"]["markers"]):
        if (root / "src" / "app").is_dir() or (root / "app").is_dir():
            return "next-app"
        if (root / "src" / "pages").is_dir() or (root / "pages").is_dir():
            return "next-pages"
    return "static"


def profile(root) -> dict:
    """Return the resolved profile for ``root`` (detection + defaults)."""
    root = Path(root)
    key = detect(root)
    base = dict(PROFILES.get(key, DEFAULT_PROFILE))
    base["key"] = key
    base["root"] = str(root)
    return base


# --------------------------------------------------------------------------
# the questions the gates ask
# --------------------------------------------------------------------------

def injects_viewport(root) -> bool:
    """True when the framework supplies a responsive viewport meta by default.

    Only a *real* marker combination counts: a ``next.config.*`` file plus an
    app/ or pages/ directory.  Otherwise the answer is "no", and the gate
    keeps telling the truth about a missing viewport.
    """
    prof = profile(root)
    if not prof.get("injects_viewport"):
        return False
    if prof["key"] in ("next-app", "next-pages"):
        root = Path(root)
        has_config = any((root / m).exists() for m in prof["markers"])
        has_app = ((root / "src" / "app").is_dir() or (root / "app").is_dir()
                   or (root / "src" / "pages").is_dir() or (root / "pages").is_dir())
        return has_config and has_app
    return True


def inherits_layout_title(root) -> bool:
    """True when a page without its own title inherits the root layout's."""
    prof = profile(root)
    return bool(prof.get("inherits_layout_title"))


def is_dev_console_noise(message, root=None) -> bool:
    """True when a browser console message is framework dev noise."""
    if not message:
        return False
    prof = profile(root) if root else {"dev_console_noise": []}
    patterns = prof.get("dev_console_noise") or []
    for pattern in patterns:
        if re.search(pattern, message, re.I):
            return True
    return False


def dev_console_noise_patterns(root=None):
    prof = profile(root) if root else DEFAULT_PROFILE
    return list(prof.get("dev_console_noise") or [])


GENERIC_BUILD_MARKERS = ("dist/index.html", "build/index.html", "out/index.html",
                          ".next/BUILD_ID", ".output/server/index.mjs")


def build_markers(root):
    """The files that prove *this framework* completed a production build.

    For a framework with its own markers only those count - a ``dist/`` from
    another tool must not make a failed ``next build`` look complete.
    """
    prof = profile(root)
    markers = list(prof.get("build_markers") or [])
    return markers or list(GENERIC_BUILD_MARKERS)


def build_is_real(root) -> bool:
    """True when a *production* build artefact exists.

    ``.next/static`` also appears after a failed build, so the framework
    profiles carry the marker files that only a completed build writes.
    """
    root = Path(root)
    markers = build_markers(root)
    return any((root / m).exists() for m in markers)


def describe(root) -> dict:
    """A JSON-friendly description of the framework profile."""
    prof = profile(root)
    return {
        "framework": prof["key"],
        "label": prof["label"],
        "injects_viewport": prof.get("injects_viewport", False),
        "inherits_layout_title": prof.get("inherits_layout_title", False),
        "security_headers_by_default": prof.get("security_headers_by_default", False),
        "build_output": prof.get("build_output"),
        "production_build_present": build_is_real(root),
        "dev_console_noise_patterns": prof.get("dev_console_noise", []),
        "notes": prof.get("notes", []),
    }


if __name__ == "__main__":  # pragma: no cover - manual inspection helper
    import sys
    target = sys.argv[1] if len(sys.argv) > 1 else "."
    print(json.dumps(describe(target), indent=2))
