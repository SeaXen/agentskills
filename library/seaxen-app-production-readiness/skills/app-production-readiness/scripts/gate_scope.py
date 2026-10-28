#!/usr/bin/env python3
"""Decide which of the 21 quality gates actually apply to an app.

Running all 21 gates on every app produces noise, not signal: a static
marketing site has no migrations, no payments and no API contract, and an
API service has no screenshots.  This script inspects the project and
classifies every gate as:

    applies          - the gate is meaningful for this app, it must be run
    conditional      - the gate only matters for some deployments (single
                       locale vs multi-market, static vs server)
    not_applicable   - the app has no such surface, the gate is out of scope

The classification is derived from evidence in the repository (frameworks,
dependencies, source files, database folders), never from the name of the
project or from the report being reviewed.  `verify_claims.py` uses it so a
claimed PASS on a gate that does not exist for this app is reported as
NOT_APPLICABLE instead of as a failure.

Usage:
  python gate_scope.py --root <app_root> [--json] [--gates A,B,C]

Exit 0: scope computed (this is a scoping tool, not a pass/fail gate)
Exit 1: the root is not a usable project directory
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from qa_common import (  # noqa: E402
    emit,
    load_json,
    parse_cli,
    resolve_root,
    root_error,
    walk_files,
)

APPLIES = "applies"
CONDITIONAL = "conditional"
NOT_APPLICABLE = "not_applicable"

GATE_TITLES = {
    "A": "cross-browser visual QA",
    "B": "performance / bundle budget",
    "C": "design polish",
    "D": "desktop Lighthouse",
    "E": "security",
    "F": "accessibility (WCAG 2.1 AA)",
    "G": "SEO & metadata",
    "H": "tests & correctness",
    "I": "reliability & error handling",
    "J": "docs & DX",
    "K": "observability",
    "L": "free-tier cost check",
    "M": "README & screenshots",
    "N": "business logic & API contract",
    "O": "load & soak",
    "P": "migrations & schema",
    "Q": "privacy & GDPR",
    "R": "i18n & RTL",
    "S": "assistive technology contract",
    "T": "payment & email flows",
    "U": "code quality & AI risk",
}

UI_DEPS = {"react", "vue", "svelte", "preact", "solid-js", "@angular/core",
           "@builder.io/qwik", "lit"}
UI_FRAMEWORKS = {"next", "nuxt", "astro", "@sveltejs/kit", "remix",
                 "@remix-run/react", "gatsby", "eleventy", "vuepress"}
SERVER_DEPS = {"express", "fastify", "koa", "hapi", "@hapi/hapi", "hono",
               "restify", "@nestjs/core", "apollo-server", "graphql-yoga"}
SERVER_PY = {"django", "flask", "fastapi", "falcon", "sanic", "aiohttp",
             "starlette", "tornado", "bottle"}
DB_DEPS = {"prisma", "@prisma/client", "drizzle-orm", "sequelize", "typeorm",
           "mongoose", "knex", "sqlalchemy", "psycopg2", "pg", "mysql2",
           "mysql", "sqlite3", "better-sqlite3", "diesel", "sqlx", "tokio-postgres"}
PAYMENT_HINTS = ("stripe", "paypal", "braintree", "razorpay", "adyen",
                 "square", "paddle", "lemonsqueezy", "checkout.com")
EMAIL_HINTS = ("resend", "sendgrid", "mailgun", "nodemailer", "postmark",
               "mailchimp", "sendinblue", "smtp", "ses", "emailjs", "postjet")
I18N_DEPS = {"i18next", "react-i18next", "vue-i18n", "next-intl", "@lingui/core",
             "i18n", "i18next-browser-languagedetector"}
ANALYTICS_HINTS = ("gtag", "googletagmanager", "plausible", "segment",
                   "mixpanel", "posthog", "amplitude", "matomo", "hotjar")

CODE_SUFFIXES = {".js", ".jsx", ".ts", ".tsx", ".mjs", ".cjs", ".vue", ".svelte",
                  ".py", ".go", ".rs", ".rb", ".php", ".java", ".kt", ".swift",
                  ".html", ".css", ".scss", ".sql", ".json", ".yaml", ".yml",
                  ".toml", ".md"}


def _text_of(path: Path, limit: int = 200_000) -> str:
    try:
        raw = path.read_bytes()[:limit]
    except OSError:
        return ""
    return raw.decode("utf-8", errors="ignore")


def _has_server_routes(root: Path, files) -> bool:
    """Framework-native server routes (Next/Nuxt/Astro/SvelteKit/Remix).

    A Next.js app has no ``server.js`` and no express dependency, yet it runs a
    server.  Without this check every full-stack Next/Nuxt app was classified
    as a static site and the reliability/observability/load/contract gates were
    downgraded to "conditional" for no reason.
    """
    for p in files:
        name = p.name.lower()
        # Next.js app router: route.ts / route.js ; SvelteKit: +server.ts
        if name.startswith("route.") and name.endswith((".ts", ".js", ".tsx", ".jsx")):
            return True
        if name.startswith("+server."):
            return True
        try:
            parts = p.relative_to(root).as_posix().lower().split("/")
        except ValueError:
            continue
        # pages/api/** (Next pages router, Astro endpoints), server/api/** (Nuxt),
        # server/routes/** (Nuxt), functions/** (Netlify), api/ under a server dir
        if "api" in parts and any(d in parts for d in ("pages", "server", "functions")):
            return True
    return False


def detect_app(root: Path) -> dict:
    """What kind of app is this? Only repository evidence is used."""
    pkg = load_json(root / "package.json")
    pkg = pkg if isinstance(pkg, dict) else {}
    deps = {}
    for key in ("dependencies", "devDependencies", "peerDependencies"):
        deps.update(pkg.get(key) or {})

    files = []
    try:
        for p in walk_files(root):
            files.append(p)
    except Exception:
        pass

    names = {p.name.lower() for p in files}
    suffix_counts = {}
    for p in files:
        suffix_counts[p.suffix.lower()] = suffix_counts.get(p.suffix.lower(), 0) + 1

    # --- source text corpus (bounded) ------------------------------------
    corpus_parts = []
    for p in files:
        if p.suffix.lower() in CODE_SUFFIXES and p.stat().st_size < 400_000:
            corpus_parts.append(_text_of(p, 60_000))
    corpus = "\n".join(corpus_parts)
    lower = corpus.lower()
    deps_text = " ".join(deps.keys()).lower()

    html_files = [p for p in files if p.suffix.lower() in (".html", ".htm")]
    has_ui_framework = bool(UI_DEPS & set(deps)) or bool(UI_FRAMEWORKS & set(deps))
    has_ui = bool(html_files) or has_ui_framework
    # Next/Nuxt/SvelteKit render HTML at runtime from .tsx/.vue files
    ssr_framework = bool({"next", "nuxt", "@sveltejs/kit", "remix",
                          "@remix-run/react", "astro"} & set(deps))

    server_entry_names = {"server.js", "server.ts", "server.mjs", "main.py",
                          "app.py", "wsgi.py", "asgi.py", "main.go", "main.rs",
                          "index.js", "index.ts", "app.js", "app.ts",
                          "run.py", "manage.py"}
    has_server = bool(server_entry_names & names) or bool(SERVER_DEPS & set(deps)) \
        or any(d in deps_text for d in SERVER_PY) \
        or _has_server_routes(root, files) \
        or '"use server"' in corpus

    mobile = any(h in deps_text for h in ("react-native", "expo", "flutter",
                                           "ionic", "capacitor")) \
        or (root / "pubspec.yaml").is_file() or (root / "app.json").is_file()

    db_dirs = ("migrations", "migrate", "alembic", "prisma", "drizzle",
               "db", "database", "schema")
    has_db = bool(DB_DEPS & set(deps)) or any(d in {str(p.parent.name).lower()
                                                    for p in files} for d in db_dirs) \
        or any(p.suffix.lower() == ".sql" for p in files)

    pii_markers = ("type=\"email\"", "type='email'", "password", "sign up",
                   "signup", "log in", "login", "register", "newsletter",
                   "subscribe", "account", "checkout", "customer")
    collects_pii = any(m in lower for m in pii_markers) or bool(has_db) \
        or any(h in lower for h in ANALYTICS_HINTS)

    payments = any(h in deps_text or h in lower for h in PAYMENT_HINTS)
    email = any(h in deps_text or h in lower for h in EMAIL_HINTS)
    i18n = bool({"locales", "i18n", "lang", "translations", "locale"}
                & {str(p.parent.name).lower() for p in files}) \
        or bool(I18N_DEPS & set(deps)) \
        or any(p.suffix.lower() in (".po", ".mo") for p in files)

    static_only = has_ui and not has_server and not ssr_framework
    if mobile and not has_ui:
        kind = "mobile"
    elif has_server and has_ui:
        kind = "ssr-web"
    elif has_server and not has_ui:
        kind = "api-or-service"
    elif has_ui:
        kind = "static-site" if static_only else "spa"
    else:
        kind = "cli-or-library"

    return {
        "name": pkg.get("name") or root.name,
        "kind": kind,
        "frameworks": sorted((UI_FRAMEWORKS | SERVER_DEPS | SERVER_PY | UI_DEPS)
                             & set(deps)),
        "has_ui": has_ui,
        "has_server": has_server,
        "has_db": has_db,
        "has_html": bool(html_files),
        "ssr_framework": ssr_framework,
        "static_only": static_only,
        "mobile": mobile,
        "collects_pii": collects_pii,
        "payments": payments,
        "email": email,
        "i18n": i18n,
        "has_tests": bool({"test", "tests", "spec", "__tests__"}
                          & {str(p.parent.name).lower() for p in files})
        or bool("test" in (pkg.get("scripts") or {})),
        "file_count": len(files),
        "html_pages": len(html_files),
    }


def _rule(app: dict, status: str, reason: str):
    return {"status": status, "reason": reason}


def classify(app: dict) -> dict:
    """Map the detected app onto the 21 gates."""
    ui = app["has_ui"]
    server = app["has_server"]
    g = {}

    # A - visual QA
    if ui:
        g["A"] = _rule(app, APPLIES, f"{app['html_pages']} HTML page(s) / a UI framework - visual QA applies")
    else:
        g["A"] = _rule(app, NOT_APPLICABLE, "no user interface in this project (no HTML, no UI framework)")

    # B - bundle / performance
    if ui:
        g["B"] = _rule(app, APPLIES, "ships a browser bundle - route JS budgets apply")
    elif app["kind"] in ("cli-or-library",):
        g["B"] = _rule(app, CONDITIONAL, "no browser bundle; only apply if the package ships browser code")
    else:
        g["B"] = _rule(app, APPLIES, "server-rendered app - response size and latency budgets apply")

    # C - design polish
    if ui:
        g["C"] = _rule(app, APPLIES, "there is a UI to polish")
    else:
        g["C"] = _rule(app, NOT_APPLICABLE, "no user interface - design polish has nothing to judge")

    # D - Lighthouse
    if ui:
        g["D"] = _rule(app, APPLIES, "web pages can be measured by Lighthouse")
    else:
        g["D"] = _rule(app, NOT_APPLICABLE, "no web page to audit")

    # E - security
    g["E"] = _rule(app, APPLIES, "security applies to every project")

    # F - accessibility
    if ui:
        g["F"] = _rule(app, APPLIES, "WCAG applies to every user interface")
    else:
        g["F"] = _rule(app, NOT_APPLICABLE, "no user interface - no WCAG surface")

    # G - SEO
    if ui and not app["mobile"]:
        g["G"] = _rule(app, APPLIES, "public web pages - metadata, robots and sitemap apply")
    elif app["mobile"]:
        g["G"] = _rule(app, NOT_APPLICABLE, "native mobile app - store metadata replaces web SEO")
    else:
        g["G"] = _rule(app, NOT_APPLICABLE, "no public web page (API/service or CLI)")

    # H - tests
    g["H"] = _rule(app, APPLIES, "correctness applies to every project"
                   + ("" if app["has_tests"] else " (note: no test suite detected)"))

    # I - reliability
    if server:
        g["I"] = _rule(app, APPLIES, "a server runtime exists - health endpoint and error handling apply")
    elif ui:
        g["I"] = _rule(app, CONDITIONAL, "static site - verify the host's error page and uptime instead of /healthz")
    else:
        g["I"] = _rule(app, CONDITIONAL, "no long-running server - resilience is about the CLI/package")

    # J - docs
    g["J"] = _rule(app, APPLIES, "every project ships documentation")

    # K - observability
    if server:
        g["K"] = _rule(app, APPLIES, "server logs and request tracing can be checked in the source")
    elif ui:
        g["K"] = _rule(app, CONDITIONAL, "static site - observability is host/edge logging, not app logs")
    else:
        g["K"] = _rule(app, CONDITIONAL, "no server telemetry to inspect")

    # L - cost
    g["L"] = _rule(app, APPLIES, "the deployment cost of this project must be known")

    # M - README + screenshots
    if ui:
        g["M"] = _rule(app, APPLIES, "there are screens to document")
    else:
        g["M"] = _rule(app, CONDITIONAL, "no screens - the README still must be complete, but screenshots do not apply")

    # N - business logic / API contract
    if server:
        g["N"] = _rule(app, APPLIES, "server code - error paths and the API contract apply")
    elif ui:
        g["N"] = _rule(app, CONDITIONAL, "client-only app - only the client state machine is testable")
    else:
        g["N"] = _rule(app, CONDITIONAL, "library/CLI - logic correctness applies to the public API only")

    # O - load
    if server:
        g["O"] = _rule(app, APPLIES, "a live endpoint exists - load and soak can be measured")
    elif ui:
        g["O"] = _rule(app, CONDITIONAL, "static site - the limit is the CDN, not the app; check the plan's quotas")
    else:
        g["O"] = _rule(app, NOT_APPLICABLE, "no endpoint to load test")

    # P - migrations
    if app["has_db"]:
        g["P"] = _rule(app, APPLIES, "a database is in use - migrations and rollback paths apply")
    else:
        g["P"] = _rule(app, NOT_APPLICABLE, "no database or migration folder - nothing to roll back")

    # Q - privacy
    if app["collects_pii"]:
        g["Q"] = _rule(app, APPLIES, "the app handles personal data - privacy and GDPR apply")
    else:
        g["Q"] = _rule(app, NOT_APPLICABLE, "no personal data, no accounts, no analytics - no privacy surface")

    # R - i18n / RTL
    if app["i18n"]:
        g["R"] = _rule(app, APPLIES, "locale files or an i18n framework are present")
    else:
        g["R"] = _rule(app, CONDITIONAL, "single-locale product - required only when more markets are served")

    # S - screen-reader contract
    if ui:
        g["S"] = _rule(app, APPLIES, "assistive technology must work on every screen")
    else:
        g["S"] = _rule(app, NOT_APPLICABLE, "no user interface - no assistive-technology surface")

    # T - payment / email
    if app["payments"] or app["email"]:
        bits = []
        if app["payments"]:
            bits.append("a payment provider")
        if app["email"]:
            bits.append("an email provider")
        g["T"] = _rule(app, APPLIES, " and ".join(bits) + " detected - money and mail flows apply")
    else:
        g["T"] = _rule(app, NOT_APPLICABLE, "no payment or email provider in the project")

    # U - code quality
    g["U"] = _rule(app, APPLIES, "code quality applies to every project")

    return g


def analyse(root: Path) -> dict:
    app = detect_app(root)
    gates = classify(app)
    required = [k for k, v in gates.items() if v["status"] == APPLIES]
    recommended = [k for k, v in gates.items() if v["status"] == CONDITIONAL]
    skipped = [k for k, v in gates.items() if v["status"] == NOT_APPLICABLE]
    return {
        "root": str(root),
        "app": app,
        "gates": gates,
        "required": required,
        "recommended": recommended,
        "skipped": skipped,
        "summary": {
            "applies": len(required),
            "conditional": len(recommended),
            "not_applicable": len(skipped),
            "total": len(gates),
        },
    }


def scope_for_gate(report: dict, gate: str):
    """(status, reason) for one gate; (None, '') when the gate is unknown."""
    entry = (report.get("gates") or {}).get(gate)
    if not entry:
        return None, ""
    return entry.get("status"), entry.get("reason", "")


def main() -> int:
    args = sys.argv[1:]
    root_arg, json_mode, want_help = parse_cli(args)
    only = None
    i = 0
    while i < len(args):
        if args[i] == "--gates" and i + 1 < len(args):
            only = [g.strip().upper() for g in args[i + 1].split(",") if g.strip()]
            i += 1
        i += 1
    if want_help:
        print(__doc__)
        return 0
    root = resolve_root(root_arg)
    err = root_error(root)
    if err:
        print(f"ERROR: {err}", file=sys.stderr)
        return 1
    report = analyse(root)
    lines = ["=" * 62, "GATE SCOPE (what actually applies to this app)", "=" * 62]
    app = report["app"]
    lines.append(f"app: {app['name']} ({app['kind']})"
                 f" ui={'yes' if app['has_ui'] else 'no'}"
                 f" server={'yes' if app['has_server'] else 'no'}"
                 f" db={'yes' if app['has_db'] else 'no'}"
                 f" pii={'yes' if app['collects_pii'] else 'no'}"
                 f" payments={'yes' if app['payments'] else 'no'}"
                 f" email={'yes' if app['email'] else 'no'}")
    lines.append("-" * 62)
    for gate in sorted(report["gates"]):
        if only and gate not in only:
            continue
        entry = report["gates"][gate]
        icon = {APPLIES: "run", CONDITIONAL: "maybe", NOT_APPLICABLE: "skip"}.get(entry["status"], "?")
        lines.append(f"[{icon:>5}] {gate} {GATE_TITLES.get(gate, gate)}: {entry['reason']}")
    s = report["summary"]
    lines.append("-" * 62)
    lines.append(f"run {s['applies']} | maybe {s['conditional']} | skip {s['not_applicable']}"
                 f" | of {s['total']} gates")
    lines.append("=" * 62)
    emit(lines, report, json_mode)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
