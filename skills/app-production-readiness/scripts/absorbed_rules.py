#!/usr/bin/env python
"""Extra review rules absorbed from the sibling skills that had no runnable code.

Every function here returns a list of findings shaped like the findings of
``security_scan.py``::

    {"severity": "HIGH" | "MEDIUM" | "LOW", "type": "<label>", "file": "<path>", "line": <int>}

The sibling skills that were absorbed (documentation only) and the gate each of
them now feeds:

=========================  ==========================================  ======
sibling skill              rule family                                  gate
=========================  ==========================================  ======
api-contract-testing       OpenAPI / contract coverage                  N
security-hardened-api      OWASP API Top 10 hardening                   E
observability-and-instr.   logs, metrics, traces, alerts                K
microservices-resilience   timeouts, retries, breakers, rate limits     I
ai-debt-detector           the debt an AI author leaves behind          U
property-based-testing     property-based test coverage                 H
mutation-testing           mutation testing coverage                    H
=========================  ==========================================  ======

The reference text of every absorbed skill is kept verbatim under
``references/knowledge/<skill>/`` so the skill stays self-contained and the
rules can be traced back to their source.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

CODE_EXT = {".js", ".jsx", ".mjs", ".cjs", ".ts", ".tsx", ".py", ".go", ".rs", ".rb", ".php", ".java", ".kt", ".vue", ".svelte", ".cs", ".swift", ".dart", ".scala", ".ex", ".exs", ".sh", ".bash", ".m", ".mm"}
SKIP_DIRS = {
    "node_modules", ".git", "dist", "build", "out", ".next", ".nuxt", ".svelte-kit",
    "coverage", ".vercel", ".netlify", ".wrangler", ".turbo", ".cache", ".pytest_cache",
    "__pycache__", ".venv", "venv", "target", "qa", "docs",
}


def _files(root: Path, extensions: set[str] | None = None):
    """Yield the source files of the project.

    A directory is skipped only when one of its *path parts* is exactly a
    skip marker. A substring match on the whole path is wrong: it silently
    dropped every file whose name contains "out" (``route.ts``, ``about.ts``,
    ``layout.tsx``, ``checkout.ts`` ...) and every project whose path
    contained a marker.
    """
    for path in sorted(root.rglob("*")):
        if not path.is_file():
            continue
        try:
            parts = path.relative_to(root).parts[:-1]
        except ValueError:
            parts = path.parts[:-1]
        if any(part.lower() in SKIP_DIRS for part in parts):
            continue
        if extensions and path.suffix.lower() not in extensions:
            continue
        yield path


def _read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""


def _finding(severity: str, kind: str, path: Path, root: Path, line: int = 0, detail: str = "") -> dict:
    try:
        rel = path.relative_to(root).as_posix()
    except ValueError:
        rel = path.name
    label = f"[{kind}] {detail}" if detail else f"[{kind}]"
    return {"severity": severity, "type": label, "file": rel, "line": line}


def _grep(root: Path, pattern: str, extensions: set[str] | None = None) -> list[tuple[Path, int]]:
    regex = re.compile(pattern, re.IGNORECASE)
    hits: list[tuple[Path, int]] = []
    for path in _files(root, extensions):
        for number, line in enumerate(_read(path).splitlines(), 1):
            if regex.search(line):
                hits.append((path, number))
    return hits


# --------------------------------------------------------------------------- #
# api-contract-testing -> Gate N
# --------------------------------------------------------------------------- #
CONTRACT_FILES = ("openapi.yaml", "openapi.yml", "openapi.json", "swagger.yaml", "swagger.yml", "swagger.json", "api-spec.yaml", "api-spec.json")


def api_contract_findings(root: Path) -> list[dict]:
    """An API without a machine-readable contract cannot be reviewed against one."""
    findings: list[dict] = []
    spec = None
    for name in CONTRACT_FILES:
        for candidate in root.rglob(name):
            if any(marker in candidate.as_posix().lower() for marker in SKIP_DIRS):
                continue
            spec = candidate
            break
        if spec:
            break

    has_api_route = bool(_grep(root, r"@(app|router)\.(get|post|put|patch|delete)\s*\(|url_for|/api/", CODE_EXT))
    if not has_api_route:
        return findings

    if spec is None:
        findings.append(_finding("MEDIUM", "api-contract", root, root, 0,
                                 "the app exposes API routes but has no openapi/swagger contract"))
        return findings

    text = _read(spec)
    if spec.suffix.lower() == ".json":
        try:
            data = json.loads(text)
            paths = data.get("paths") or {}
            operations = sum(1 for value in paths.values() if isinstance(value, dict))
        except (ValueError, AttributeError):
            findings.append(_finding("HIGH", "api-contract", spec, root, 0,
                                     "the API contract is not valid JSON"))
            return findings
        if not paths:
            findings.append(_finding("MEDIUM", "api-contract", spec, root, 0,
                                     "the API contract declares no paths"))
        elif operations < 2:
            findings.append(_finding("LOW", "api-contract", spec, root, 0,
                                     "the API contract declares very few operations"))
    else:
        if "paths:" not in text:
            findings.append(_finding("MEDIUM", "api-contract", spec, root, 0,
                                     "the API contract has no paths section"))
        if "responses:" not in text:
            findings.append(_finding("MEDIUM", "api-contract", spec, root, 0,
                                     "the API contract documents no responses"))
        if re.search(r"(?m)^\s{0,4}operationId\s*:", text) is None:
            findings.append(_finding("LOW", "api-contract", spec, root, 0,
                                     "no operationId - generated clients and tests lose their names"))
    return findings


# --------------------------------------------------------------------------- #
# security-hardened-api -> Gate E
# --------------------------------------------------------------------------- #
RATE_LIMIT_MARKERS = ("rateLimit", "rate_limit", "ratelimit", "express-rate-limit", "upstash/ratelimit", "slowapi", "limiter")
CSRF_MARKERS = ("csurf", "csrf", "csrftoken", "csrf_token", "x-csrf-token")
AUTH_MARKERS = ("passport", "auth0", "next-auth", "nextauth", "jwt", "session(", "clerk", "supabase")


def api_hardening_findings(root: Path) -> list[dict]:
    """OWASP API Top 10: missing rate limiting, missing CSRF, credentialed CORS."""
    findings: list[dict] = []
    has_server = bool(_grep(root, r"@(app|router)\.(get|post|put|patch|delete)\s*\(|app\.listen\s*\(|Flask\s*\(|FastAPI\s*\(", CODE_EXT))
    if not has_server:
        return findings

    corpus = "\n".join(_read(path) for path in _files(root, CODE_EXT))[:2_000_000]
    if not any(marker.lower() in corpus.lower() for marker in RATE_LIMIT_MARKERS):
        findings.append(_finding("MEDIUM", "api-hardening", root, root, 0,
                                 "no rate limiting found on an API surface"))
    uses_cookie_auth = "req.headers.cookie" in corpus.lower() or "cookies(" in corpus.lower() or "session(" in corpus.lower()
    if uses_cookie_auth and not any(marker.lower() in corpus.lower() for marker in CSRF_MARKERS):
        findings.append(_finding("MEDIUM", "api-hardening", root, root, 0,
                                 "cookie based auth without a CSRF defence"))
    if re.search(r"(?i)access-control-allow-credentials['\"]?\s*[:,]\s*['\"]true", corpus) and \
            re.search(r"(?i)access-control-allow-origin['\"]?\s*[:,]\s*['\"]\*", corpus):
        findings.append(_finding("HIGH", "api-hardening", root, root, 0,
                                 "CORS allows credentials with a wildcard origin"))
    if re.search(r"(?i)['\"]?stack['\"]?\s*:\s*(err|error|e)\.stack", corpus):
        findings.append(_finding("MEDIUM", "api-hardening", root, root, 0,
                                 "a stack trace can be returned to the client"))
    return findings


# --------------------------------------------------------------------------- #
# observability-and-instrumentation -> Gate K
# --------------------------------------------------------------------------- #
OBSERVABILITY_SIGNALS = {
    "correlation id": (r"x-request-id|requestId|request_id|traceparent|correlation-?id", "req"),
    "error tracking": (r"sentry|@sentry|bugsnag|rollbar|datadog|newrelic|opentelemetry|@opentelemetry", "otel"),
    "metrics": (r"prom-client|prometheus|micrometer|openmetrics|/metrics|statsd", "prom"),
    "health endpoint": (r"['\"]/healthz?['\"]|['\"]/health['\"]|['\"]/livez?['\"]|['\"]/readyz?['\"]", "health"),
    "alerting": (r"alert(s|ing)?\b.*(slack|pagerduty|opsgenie|webhook)|pagerduty|opsgenie", "alert"),
    "audit trail": (r"audit_?log|audit trail|actor_id|performed_by", "audit"),
}

# "Structured logging" needs two things to be true in the *same* file: a log
# sink and a structured payload. A bare console.log() is not structured, and a
# JSON.stringify() that never reaches a log sink is not logging either.
LOG_SINK = (r"logger\.(info|warn|error|debug)\s*\(|console\.(info|warn|error|log)\s*\("
             r"|log\.(info|warn|error|debug)\s*\(|pino\.|winston|zerolog|zap\.|logrus|structlog")
LOG_PAYLOAD = (r"JSON\.stringify\(\s*\{|logger\.\w+\(\s*\{|log\.\w+\(\s*\{"
               r"|log\.\w+\(\s*\w+\s*,|logger\.\w+\(\s*\w+\s*,")

ALL_OBSERVABILITY_SIGNALS = tuple(OBSERVABILITY_SIGNALS) + ("structured logging",)


def observability_signals(root: Path) -> set[str]:
    """Return the observability signals that are actually present in the source.

    This is the single source of truth for Gate K: the verdict in
    ``verify_claims.verify_K`` and the advisory in
    ``observability_findings`` are both derived from it, so the report can
    never claim a signal is present while advising that it is missing.
    """
    present: set[str] = set()
    for path in _files(root, CODE_EXT):
        text = _read(path)
        if not text:
            continue
        if ("structured logging" not in present
                and re.search(LOG_SINK, text, re.IGNORECASE)
                and re.search(LOG_PAYLOAD, text, re.IGNORECASE)):
            present.add("structured logging")
        for name, (pattern, _) in OBSERVABILITY_SIGNALS.items():
            if name in present:
                continue
            if re.search(pattern, text, re.IGNORECASE):
                present.add(name)
    return present


def observability_findings(root: Path) -> list[dict]:
    """Report the observability signals that are missing, not the ones present."""
    findings: list[dict] = []
    present = observability_signals(root)
    if not present and not any(_files(root, CODE_EXT)):
        return findings
    missing = [name for name in ALL_OBSERVABILITY_SIGNALS if name not in present]
    for name in missing:
        findings.append(_finding("LOW", "observability", root, root, 0,
                                 f"no {name} signal found in the source"))
    return findings


# --------------------------------------------------------------------------- #
# microservices-resilience -> Gate I
# --------------------------------------------------------------------------- #
RESILIENCE_SIGNALS = {
    "request timeout": (r"timeout\s*[:=]|AbortController|AbortSignal|asyncio\.wait_for|context\.WithTimeout", "timeout"),
    "retry with backoff": (r"retry|backoff|tenacity|exponential_backoff|cockatiel", "retry"),
    "circuit breaker": (r"circuit_?breaker|circuitbreaker|opossum|polly", "breaker"),
    "bulkhead / queue": (r"semaphore|bulkhead|concurrency_?limit|worker_?pool", "bulkhead"),
    "graceful shutdown": (r"SIGTERM|graceful_?shutdown|on\(['\"]SIGTERM|atexit|shutdown_hook", "shutdown"),
    "idempotency": (r"idempotency|Idempotency-Key|request_?id", "idem"),
    "rate limit": (r"rate_?limit", "ratelimit"),
}


def resilience_findings(root: Path) -> list[dict]:
    """Report the resilience mechanisms a server is missing."""
    findings: list[dict] = []
    has_server = bool(_grep(root, r"app\.listen\s*\(|Flask\s*\(|FastAPI\s*\(|uvicorn|@app\.(get|post)\s*\(", CODE_EXT))
    if not has_server:
        return findings
    corpus = "\n".join(_read(path) for path in _files(root, CODE_EXT))[:2_000_000]
    for name, (pattern, _) in RESILIENCE_SIGNALS.items():
        if not re.search(pattern, corpus, re.IGNORECASE):
            findings.append(_finding("LOW", "resilience", root, root, 0,
                                     f"no {name} mechanism found"))
    return findings


# --------------------------------------------------------------------------- #
# ai-debt-detector -> Gate U
# --------------------------------------------------------------------------- #
AI_DEBT_PATTERNS = (
    (r"(?i)#\s*(todo|fixme|hack|xxx)\b", "LOW", "an unresolved TODO/FIXME/HACK comment"),
    (r"(?i)\b(for now|for now,|temporarily|temporary hack|should work|works for now|quick fix)\b", "LOW",
     "a 'it works for now' comment - debt an AI author left behind"),
    (r"(?i)TODO\s*:\s*remove|remove\s+(this|before|once)\b", "LOW", "a temporary workaround that was never removed"),
    (r"(?i)console\.log\s*\(", "LOW", "a debug log left in the code"),
    (r"(?i)\bdebugger\b\s*;?", "LOW", "a debugger statement left in the code"),
    (r"(?i)catch\s*\([^)]*\)\s*\{\s*\}", "LOW", "an empty catch block swallows the error"),
    (r"(?i)except[^:]*:\s*\n\s*pass\b", "LOW", "an except block that only passes"),
    (r"(?i)\bpass\s*(#.*)?$", "LOW", "a bare pass statement"),
    (r"(?i)\bnot implemented\b|NotImplementedError", "LOW", "a stub that is not implemented"),
    (r"(?i)//\s*(const|let|var|function|return|if|for|import)\b", "LOW", "commented-out code"),
)


def ai_debt_findings(root: Path) -> list[dict]:
    """The debt that an AI-written codebase usually leaves behind."""
    findings: list[dict] = []
    for path in _files(root, CODE_EXT):
        text = _read(path)
        for number, line in enumerate(text.splitlines(), 1):
            for pattern, severity, message in AI_DEBT_PATTERNS:
                if re.search(pattern, line):
                    findings.append(_finding(severity, "ai-debt", path, root, number, message))
                    break
    return findings


# --------------------------------------------------------------------------- #
# property-based-testing / mutation-testing -> Gate H
# --------------------------------------------------------------------------- #
PBT_MARKERS = ("hypothesis", "fast-check", "fast_check", "jsverify", "jqwik", "quickcheck", "pytest-benchmark")
MUTATION_MARKERS = ("stryker", "mutmut", "cosmic-ray", "mutation-testing", "pitest", "mutant", "stryker.conf")


def test_quality_findings(root: Path) -> list[dict]:
    """The project has tests but no property-based or mutation testing."""
    findings: list[dict] = []
    corpus = "\n".join(_read(path) for path in _files(root, CODE_EXT | {".toml", ".cfg", ".ini", ".json", ".yaml", ".yml"}))[:2_000_000]
    has_tests = bool(re.search(r"(?i)\b(describe|it|test)\s*\(|def test_|unittest|pytest|@Test", corpus))
    if not has_tests:
        return findings
    if not any(marker.lower() in corpus.lower() for marker in PBT_MARKERS):
        findings.append(_finding("LOW", "test-quality", root, root, 0,
                                 "no property-based tests (hypothesis / fast-check)"))
    if not any(marker.lower() in corpus.lower() for marker in MUTATION_MARKERS):
        findings.append(_finding("LOW", "test-quality", root, root, 0,
                                 "no mutation testing (stryker / mutmut / pitest)"))
    return findings
