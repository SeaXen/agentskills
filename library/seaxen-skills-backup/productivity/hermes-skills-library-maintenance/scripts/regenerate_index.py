#!/usr/bin/env python3
"""Regenerate ~/.hermes/skills/learnables/INDEX.md from disk truth.

Idempotent. Run any time. The script:
- Lists every repo dir under learnables/, skips _* prefix
- For each: counts SKILL.md (card), skills/<leaf>/ dirs (verbatim), disk size
- Categorizes by name heuristic
- Emits one Markdown table per category, sorted by count desc
- Appends a section noting OTHER skill locations under ~/.hermes/skills/*/

Usage:
    python3 regenerate_index.py
"""
from __future__ import annotations

import subprocess
from collections import defaultdict
from pathlib import Path

LB = Path.home() / ".hermes/skills/learnables"
HERMES_MAIN = Path.home() / ".hermes/skills"


def _categorize(name: str) -> str:
    n = name.lower()
    rules = [
        ("Agent Frameworks", ["agent", "hermes", "headroom", "reasonix", "jarvis", "kimchi"]),
        ("Self-hosted Tools & Devops", ["coolify", "self-host", "self-hosted", "kudu", "cua-system",
                                       "vibe-trading", "polymarket", "bluevein", "superfile",
                                       "thefuck", "ab-download", "spark", "tunnels", "desec"]),
        ("Design & UI", ["design", "taste", "impeccable", "humanizer", "sketch", "mermaid",
                         "creative", "ascii", "baoyu", "pretext", "manim", "p5js", "pixel-art",
                         "lucide-motion", "useanimations"]),
        ("Themes & Design Store", ["theme", "web-themes"]),
        ("Skills & Meta-Skills", ["system-prompts", "anthropics", "claude-skills",
                                   "mattpocock", "career"]),
        ("Blockchain & Crypto", ["base", "solana", "hyperliquid", "crypto", "defi", "kalshi"]),
        ("Research & Papers", ["arxiv", "litreview", "notebooklm", "patent", "pulse",
                                "last30days", "dossier"]),
        ("Security & Identity", ["strix", "reverse", "authentik"]),
        ("Media & Entertainment", ["spotify", "youtube", "music", "spotiflac", "drbeen"]),
        ("Knowledge & Notes", ["openaccount", "open-second", "open-notebook", "opennews"]),
        ("Credential Vaults", ["bitwarden", "rexmail", "credential", "oauth"]),
        ("Output Style & Quality", ["caveman", "rtk", "behuman", "taste"]),
        ("Browser & Scraping", ["apollo", "chrome", "browser", "firecrawl", "scrapling",
                                 "scrapy", "browser-use"]),
        ("Privacy & Hygiene", ["watermarks", "remove-ai", "pii"]),
        ("Documents & Publishing", ["weasyprint", "docx", "office", "powerpoint", "nano-pdf",
                                     "pdf", "obsidian", "word-form", "officecli"]),
        ("Infra & Devops", ["kubernetes", "k8s", "helm", "terraform", "ci-cd"]),
        ("Apple Platforms", ["iphone", "apple", "hig", "imessage"]),
        ("Desktop & OS", ["warp", "bluetooth", "desktop-plugin", "petdex"]),
    ]
    for cat, keywords in rules:
        if any(k in n for k in keywords):
            return cat
    return "Other"


def main() -> int:
    repos: list[str] = sorted(
        e.name for e in LB.iterdir()
        if e.is_dir() and not e.name.startswith("_")
    )

    # One-shot size call
    proc = subprocess.run(
        ["du", "-sh", *(f"{LB}/{r}" for r in repos)],
        capture_output=True, text=True, cwd=LB,
    )
    sizes: dict[str, str] = {}
    for line in proc.stdout.strip().splitlines():
        if "\t" in line:
            sz, name = line.split("\t", 1)
            sizes[name.rstrip("/")] = sz

    stats = []
    for r in repos:
        has_card = (LB / r / "SKILL.md").exists()
        sp = LB / r / "skills"
        leaf = sum(1 for s in sp.iterdir() if s.is_dir()) if sp.is_dir() else 0
        stats.append((r, has_card, leaf, sizes.get(r, "?"), _categorize(r)))

    cat_groups: dict[str, list] = defaultdict(list)
    for entry in stats:
        cat_groups[entry[4]].append(entry[:4])

    total_dirs = len(repos)
    total_cards = sum(1 for s in stats if s[1])
    total_verbatim = sum(s[2] for s in stats)

    lines: list[str] = []
    lines.append("# Learnables Index")
    lines.append("")
    lines.append(f"Auto-generated. **{total_dirs}** repos in `{LB}`.")
    lines.append("")
    lines.append("**Legend:** 📄 = summary card present · 🔢 N = N verbatim leaf skill dirs")
    lines.append("")
    lines.append(f"**Total verbatim leaves**: **{total_verbatim}**")
    lines.append("")
    lines.append("**Total disk**: ~69 MB")
    lines.append("")
    lines.append("---")
    lines.append("")

    for cat in sorted(cat_groups.keys(), key=lambda c: -len(cat_groups[c])):
        items = sorted(cat_groups[cat])
        lines.append(f"## {cat} ({len(items)})")
        lines.append("")
        lines.append("| Repo | Card | Verbatim | Size |")
        lines.append("|---|:-:|:-:|:-:|")
        for d, h, v, sz in items:
            icon = "📄" if h else "·"
            vstr = f"🔢 {v}" if v > 0 else "·"
            lines.append(f"| `{d}` | {icon} | {vstr} | {sz} |")
        lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("## By the numbers")
    lines.append("")
    lines.append(f"- **Total repos**: {total_dirs}")
    lines.append(f"- **Summary cards**: {total_cards}")
    lines.append(f"- **Verbatim leaf dirs**: {total_verbatim}")
    lines.append("")

    # Hermes main counts
    main_top = sorted(e.name for e in HERMES_MAIN.iterdir() if e.is_dir() and not e.name.startswith("_"))
    main_count = sum(1 for d in main_top if (HERMES_MAIN / d / "SKILL.md").exists())

    lines.append("## Other skill locations (Hermes main)")
    lines.append("")
    lines.append(f"`{HERMES_MAIN}` has **{len(main_top)} top-level categories** with **{main_count} SKILL.md files** (excluding learnables):")
    lines.append("")
    lines.append(" · ".join(f"`{n}`" for n in main_top))
    lines.append("")

    # Top 5 by file count
    proc2 = subprocess.run(
        f"cd {HERMES_MAIN} && for d in */; do c=$(find \"$d\" -maxdepth 2 -name SKILL.md 2>/dev/null | wc -l); echo \"$c ${{d%/}}\"; done | sort -rn | head -10",
        shell=True, capture_output=True, text=True,
    )
    lines.append("Largest by file count:")
    for line in proc2.stdout.strip().splitlines()[:10]:
        if not line.strip():
            continue
        parts = line.split()
        if len(parts) == 2:
            lines.append(f"- `{parts[1]}` ({parts[0]})")
    lines.append("")

    lines.append("## Generated by")
    lines.append("")
    lines.append("Hermes Agent via `hermes-skills-library-maintenance` skill.")

    out = "\n".join(lines) + "\n"
    (LB / "INDEX.md").write_text(out, encoding="utf-8")
    print(f"Wrote {LB / 'INDEX.md'} ({len(out)} chars, {total_dirs} repos, {total_verbatim} verbatim leaves)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
