#!/usr/bin/env python3
r"""Summarize AI-assistant traffic in a web access log, by bot role and docs version.

Reads access logs in the combined log format (Apache/nginx default) and reports:
  - hits per AI agent, grouped by role (AI search index, user-triggered fetch, training),
    with classic search crawlers that also feed AI answers reported apart
  - per agent, hits split by the docs version found in the request path
  - the most-fetched paths per version, and requests for llms.txt files
  - referral visits from AI assistant domains, split by version
  - optionally, how many bot hits come from the vendor's published IP ranges

Stdlib only. Reads local files; never fetches anything. Download the vendors'
IP-range JSON files yourself and pass them with --ip-ranges.

Examples:
  python3 ai-bot-log-summary.py access.log
  python3 ai-bot-log-summary.py access.log.1 access.log --path-prefix /docs/
  python3 ai-bot-log-summary.py access.log --version-regex '/docs/(\d+\.x)/' --json
  python3 ai-bot-log-summary.py access.log --ip-ranges searchbot.json --ip-ranges bots.json
"""

import argparse
import gzip
import ipaddress
import json
import re
import sys
from collections import Counter, defaultdict
from urllib.parse import urlsplit

# Agent tokens matched case-insensitively against the User-Agent header, with the role
# each vendor documents for them. Vendors rename and add agents several times a year:
# extend this table from each vendor's crawler page rather than trusting it as complete.
# Order matters: the first token found in the header wins.
AGENT_ROLES = [
    ("OAI-SearchBot", "ai-search"),
    ("OAI-AdsBot", "ads-check"),
    ("ChatGPT-User", "user-fetch"),
    ("GPTBot", "training"),
    ("Claude-SearchBot", "ai-search"),
    ("Claude-User", "user-fetch"),
    ("ClaudeBot", "training"),
    ("PerplexityBot", "ai-search"),
    ("Perplexity-User", "user-fetch"),
    ("Google-Agent", "user-fetch"),
    ("Google-NotebookLM", "user-fetch"),
    ("Google-GeminiNotebook", "user-fetch"),
    # Classic search crawlers also feed AI Overviews, AI Mode and Copilot. Reported
    # apart, because their volume dwarfs the AI-specific agents.
    ("bingbot", "classic-search"),
    ("Googlebot", "classic-search"),
    # Historic tokens: still worth counting, since spoofers and stale configs use them.
    ("Claude-Web", "historic"),
    ("anthropic-ai", "historic"),
]

# Referrer hosts of AI assistants. ChatGPT also appends utm_source=chatgpt.com to links.
AI_REFERRER_HOSTS = [
    "chatgpt.com",
    "chat.openai.com",
    "perplexity.ai",
    "gemini.google.com",
    "copilot.microsoft.com",
    "claude.ai",
]

# Combined log format: ip ident user [time] "request" status size "referer" "user-agent"
LOG_LINE = re.compile(
    r'^(?P<ip>\S+) \S+ \S+ \[[^\]]*\] "(?P<request>[^"]*)" (?P<status>\d{3}) \S+ '
    r'"(?P<referer>[^"]*)" "(?P<agent>[^"]*)"'
)

# Default version pattern: a path segment like /v2/ or /v2.3/. The "v" is required so
# that /errors/404/ or /blog/2024/ never count as versions; pass --version-regex for
# bare-number schemes. Version subdomains are not in the combined format: split those
# logs per host and run once per file instead.
DEFAULT_VERSION_REGEX = r"/(v\d+(?:\.\d+){0,2})/"

UNVERSIONED = "(unversioned)"

# How many paths to list per version in the top-paths table: enough to spot an old page
# that assistants keep fetching, short enough to read.
TOP_PATHS_PER_VERSION = 5


def open_log(path):
    if path == "-":
        return sys.stdin
    if path.endswith(".gz"):
        return gzip.open(path, "rt", encoding="utf-8", errors="replace")
    return open(path, "r", encoding="utf-8", errors="replace")


def load_ip_ranges(paths):
    """Collect IPv4/IPv6 prefixes from vendor JSON files ({"prefixes": [{"ipv4Prefix": ...}]})."""
    networks = []
    for path in paths:
        try:
            with open(path, "r", encoding="utf-8") as handle:
                data = json.load(handle)
        except (OSError, json.JSONDecodeError) as err:
            sys.exit(f"error: cannot read IP-range file {path}: {err}")
        prefixes = data.get("prefixes", []) if isinstance(data, dict) else []
        for entry in prefixes:
            for key in ("ipv4Prefix", "ipv6Prefix"):
                value = entry.get(key) if isinstance(entry, dict) else None
                if value:
                    try:
                        networks.append(ipaddress.ip_network(value, strict=False))
                    except ValueError:
                        print(f"warning: skipping bad prefix {value!r} in {path}", file=sys.stderr)
        if not prefixes:
            print(f"warning: no 'prefixes' list found in {path}", file=sys.stderr)
    return networks


def ip_in(networks, ip_text):
    try:
        ip = ipaddress.ip_address(ip_text)
    except ValueError:
        return False
    return any(ip.version == net.version and ip in net for net in networks)


def classify_agent(agent):
    lowered = agent.lower()
    for token, role in AGENT_ROLES:
        if token.lower() in lowered:
            return token, role
    return None, None


def ai_referrer(referer, path):
    # Match on the referrer's host only, so "google.com/search?q=claude.ai" is not a claude.ai visit.
    try:
        ref_host = (urlsplit(referer).hostname or "").lower()
    except ValueError:
        ref_host = ""
    for host in AI_REFERRER_HOSTS:
        if ref_host == host or ref_host.endswith("." + host):
            return host
    if "utm_source=chatgpt.com" in path.lower():
        return "chatgpt.com (utm)"
    return None


def main():
    parser = argparse.ArgumentParser(
        description="Summarize AI bot fetches and AI referrals in access logs, by role and docs version."
    )
    parser.add_argument("logs", nargs="+", help="access log files (combined format; .gz ok; '-' for stdin)")
    parser.add_argument("--path-prefix", default="", help="only count requests whose path starts with this, e.g. /docs/")
    parser.add_argument("--version-regex", default=DEFAULT_VERSION_REGEX,
                        help="regex with one capture group extracting the version from the path")
    parser.add_argument("--ip-ranges", action="append", default=[], metavar="FILE",
                        help="vendor IP-range JSON file downloaded beforehand (repeat the flag per file); "
                             "marks bot hits verified or not. Pass every vendor's files: an agent whose "
                             "vendor file is missing reads as unverified")
    parser.add_argument("--json", action="store_true", help="print JSON instead of text tables")
    args = parser.parse_args()

    try:
        version_re = re.compile(args.version_regex)
    except re.error as err:
        sys.exit(f"error: bad --version-regex: {err}")
    if version_re.groups < 1:
        sys.exit("error: --version-regex needs one capture group")

    networks = load_ip_ranges(args.ip_ranges) if args.ip_ranges else []

    bot_hits = Counter()                 # (role, agent) -> hits
    bot_versions = defaultdict(Counter)  # (role, agent) -> version -> hits
    top_paths = defaultdict(Counter)     # version -> path -> AI bot hits (classic search excluded)
    llms_hits = Counter()                # (agent or "other") -> requests for llms*.txt
    bot_status = defaultdict(Counter)    # role -> status class -> hits
    verified = Counter()                 # (agent, verified bool) -> hits
    referrals = Counter()                # host -> visits
    referral_versions = Counter()        # version -> visits
    lines_total = 0
    lines_unparsed = 0

    for path in args.logs:
        try:
            handle = open_log(path)
        except OSError as err:
            sys.exit(f"error: cannot open {path}: {err}")
        with handle:
            for line in handle:
                lines_total += 1
                match = LOG_LINE.match(line)
                if not match:
                    lines_unparsed += 1
                    continue
                request = match.group("request").split(" ")
                req_path = request[1] if len(request) >= 2 else ""
                bare_path = req_path.split("?", 1)[0]
                agent_token, role = classify_agent(match.group("agent"))
                # llms.txt usually sits at the site root: count it before the path filter.
                if re.search(r"/llms(-full)?\.txt$", bare_path):
                    llms_hits[agent_token or "other"] += 1
                if args.path_prefix and not req_path.startswith(args.path_prefix):
                    continue
                version_match = version_re.search(req_path)
                version = version_match.group(1) if version_match else UNVERSIONED
                if agent_token:
                    bot_hits[(role, agent_token)] += 1
                    bot_versions[(role, agent_token)][version] += 1
                    if role != "classic-search":
                        top_paths[version][bare_path] += 1
                    bot_status[role][match.group("status")[0] + "xx"] += 1
                    if networks:
                        verified[(agent_token, ip_in(networks, match.group("ip")))] += 1
                    continue

                host = ai_referrer(match.group("referer"), req_path)
                if host:
                    referrals[host] += 1
                    referral_versions[version] += 1

    if lines_total and lines_unparsed / lines_total > 0.5:
        print(f"warning: {lines_unparsed}/{lines_total} lines did not match the combined log format",
              file=sys.stderr)

    report = {
        "lines_read": lines_total,
        "lines_unparsed": lines_unparsed,
        "bot_hits": [{"role": r, "agent": a, "hits": n} for (r, a), n in bot_hits.most_common()],
        "bot_hits_by_version": {f"{r}/{a}": dict(c.most_common()) for (r, a), c in bot_versions.items()},
        "top_ai_paths_by_version": {v: dict(c.most_common(TOP_PATHS_PER_VERSION)) for v, c in top_paths.items()},
        "llms_txt_requests": dict(llms_hits.most_common()),
        "bot_status_by_role": {r: dict(c) for r, c in bot_status.items()},
        "ai_referrals": dict(referrals.most_common()),
        "ai_referrals_by_version": dict(referral_versions.most_common()),
    }
    if networks:
        report["ip_verification"] = [
            {"agent": a, "in_published_ranges": v, "hits": n} for (a, v), n in verified.most_common()
        ]

    if args.json:
        json.dump(report, sys.stdout, indent=2)
        print()
        return

    print(f"lines read: {lines_total}  unparsed: {lines_unparsed}")
    print("\nAI bot hits by role and agent")
    for (role, agent), hits in bot_hits.most_common():
        print(f"  {role:<14} {agent:<21} {hits:>8}")
    print("\nBot hits by agent and docs version")
    for (role, agent), counts in sorted(bot_versions.items()):
        cells = ", ".join(f"{v}: {n}" for v, n in counts.most_common())
        print(f"  {role:<14} {agent:<21} {cells}")
    print(f"\nMost-fetched paths per version, AI agents only (top {TOP_PATHS_PER_VERSION})")
    for version, counts in sorted(top_paths.items()):
        print(f"  {version}")
        for path_seen, hits in counts.most_common(TOP_PATHS_PER_VERSION):
            print(f"    {hits:>6}  {path_seen}")
    print("\nRequests for llms.txt / llms-full.txt")
    if not llms_hits:
        print("  none")
    for agent, hits in llms_hits.most_common():
        print(f"  {agent:<21} {hits:>8}")
    print("\nAI bot responses by status class")
    for role, counts in bot_status.items():
        cells = ", ".join(f"{s}: {n}" for s, n in sorted(counts.items()))
        print(f"  {role:<14} {cells}")
    print("\nAI assistant referrals (a lower bound: apps strip referrers)")
    for host, visits in referrals.most_common():
        print(f"  {host:<24} {visits:>8}")
    if referral_versions:
        cells = ", ".join(f"{v}: {n}" for v, n in referral_versions.most_common())
        print(f"  by version: {cells}")
    if networks:
        print("\nIP verification against the supplied ranges")
        for (agent, ok), hits in verified.most_common():
            print(f"  {agent:<21} {'verified' if ok else 'NOT in ranges':<14} {hits:>8}")


if __name__ == "__main__":
    main()
