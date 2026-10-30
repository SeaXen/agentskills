# The Skill Leaderboard Tracker & Vault Synchronizer

> **Website**: [https://www.skillleaderboard.com/](https://www.skillleaderboard.com/)  
> **API Feed**: `https://www.skillleaderboard.com/api/catalog` (700+ curated agent skills & repositories)  
> **Vault Integration**: Real-time cross-referencing, automated ingestion, 3-item standardization, 38-category classification, and Cloudflare R2 web catalog synchronization.

---

## 📌 Overview

The **Skill Leaderboard Tracker** is an automated auditing and synchronization engine designed for humans and AI agents. It tracks open-source AI agent skills from GitHub ranked by:
1. **Most Starred**: Ranked by total cumulative GitHub stars (default top 150).
2. **Trending**: Ranked by 7-day GitHub star velocity/gain (default top 50).
3. **Traction Score**: Ranked by the platform's multi-signal momentum score.
4. **Newest**: Filtered by repositories created in the last 45 days.

The tool cross-references each leaderboard repository against your local AgentSkills vault (`library/`, `upstreams.json`, and `category/`). If missing repositories are detected, it can automatically shallow-clone, sanitize to the vault's **strict 3-item standard**, register upstreams, rebuild all indexes, and update your web catalog.

---

## 🚀 Quick Start Commands

### 🐧 Linux & macOS (`bash`)

```bash
# 1. Audit Top 150 Most Starred skills
./skillleaderboard.sh --starred 150

# 2. Audit Top 50 Trending skills (7-day star growth)
./skillleaderboard.sh --trending 50

# 3. Output clean JSON for AI agents or CI/CD pipelines
./skillleaderboard.sh --trending 50 --json

# 4. Automatically ingest any missing skills into the library
./skillleaderboard.sh --trending 50 --ingest

# 5. Ingest missing skills and git commit + push to GitHub
./skillleaderboard.sh --trending 50 --ingest --push
```

### 🪟 Windows (`cmd` / `PowerShell`)

```powershell
# Command Prompt / Batch
.\skillleaderboard.bat --starred 150
.\skillleaderboard.bat --trending 50
.\skillleaderboard.bat --trending 50 --ingest --push

# PowerShell
.\skillleaderboard.ps1 -starred 150
.\skillleaderboard.ps1 -trending 50
.\skillleaderboard.ps1 -trending 50 -ingest -push
```

### 🐍 Direct Python (Cross-Platform)

```bash
# Using the dedicated script
python scripts/skillleaderboard.py --starred 150
python scripts/skillleaderboard.py --trending 50

# Using the main vault updater
python update.py --starred 150
python update.py --trending 50
```

---

## ⚙️ Complete Command-Line Options

| Flag | Default | Description |
| :--- | :---: | :--- |
| `--starred [N]` | `150` | Audits the top `N` most starred repositories on the leaderboard. |
| `--trending [N]` | `50` | Audits the top `N` trending repositories ranked by 7-day GitHub star gain. |
| `--traction [N]` | `50` | Audits the top `N` repositories ranked by Traction Score (0–100). |
| `--newest [N]` | `50` | Audits the newest repositories created in the last 45 days. |
| `--limit <N>` | — | Overrides the number of repositories to examine (e.g. `--starred --limit 300`). |
| `--json` | `false` | Emits machine-readable JSON format for AI agents, scripts, and automation. |
| `--ingest`, `--sync` | `false` | Automatically downloads, sanitizes, and ingests missing repositories into `library/`. |
| `--push` | `false` | Automatically stages, commits, and pushes changes to `origin main` on GitHub. |

---

## 🏗️ Automated Ingestion Pipeline (`--ingest`)

When you run `skillleaderboard` with `--ingest` and missing repositories are discovered, the engine executes the following automated workflow:

```
[Fetch API] ──► [Audit vs Vault] ──► [Shallow Clone] ──► [3-Item Standardization]
                                                                    │
┌───────────────────────────────────────────────────────────────────┘
▼
[Register upstreams.json] ──► [Rebuild 38 Categories] ──► [Sync Skill.Sea & R2] ──► [Git Push]
```

1. **Shallow Clone (`git clone --depth 1`)**:
   Fetches only the latest commit to prevent cloning massive historical git histories.
2. **Extraction & 3-Item Standardization**:
   - Parses the repository for all nested `SKILL.md` playbooks (or synthesizes one from root docs if a single-skill repo).
   - Generates/copies a clean `README.md`.
   - Pins the upstream commit hash into `.upstream_commit`.
   - Purges all nested `.git` folders and temporary build bloat.
3. **Upstream Registration**:
   Registers the repository in `library/upstreams.json` with its canonical GitHub URL.
4. **Category & Provenance Rebuild**:
   Calls `category_system.py` and `provenance_system.py` to classify skills into the 38 granular categories and update `SKILLS_PROVENANCE.md`.
5. **Skill.Sea Web App Sync**:
   Rebuilds `catalog.json`, `categories.json`, `repositories.json`, and `stats.json`, and uploads them to the Cloudflare R2 bucket (`skill-sea-vault`).

---

## 🤖 AI Agent Integration Guide

AI agents can interact with `skillleaderboard` headlessly using `--json`:

```bash
python scripts/skillleaderboard.py --trending 50 --json
```

### JSON Schema Output:
```json
{
  "title": "Top 50 Trending Skills (7-Day Star Growth)",
  "mode": "trending",
  "limit": 50,
  "total_examined": 50,
  "present_count": 50,
  "missing_count": 0,
  "coverage_pct": 100.0,
  "already_present": [
    {
      "rank": 1,
      "repo": "cloudflare/security-audit-skill",
      "owner": "cloudflare",
      "name": "security-audit-skill",
      "stars": 52240,
      "stars7d": 14212,
      "tractionScore": 81.32,
      "category": "Security",
      "tagline": "Automated vulnerability research and security reviews...",
      "url": "https://github.com/cloudflare/security-audit-skill",
      "is_present": true,
      "matched_by": "upstreams.json",
      "folder_slug": "cloudflare-security-audit-skill"
    }
  ],
  "missing": []
}
```

### Agent Decision Rule:
- If `missing_count == 0`: Report that the vault has 100% coverage.
- If `missing_count > 0`: Agent can report the missing list, or invoke `./skillleaderboard.sh --trending [N] --ingest --push` to autonomously synchronize the vault.

---

## 📁 File Structure

```
.agents/
├── skillleaderboard.sh        # Linux & macOS shell executable (chmod +x)
├── skillleaderboard.bat       # Windows Command Prompt batch launcher
├── skillleaderboard.ps1       # Windows PowerShell launcher
├── skillleaderboard.md        # This comprehensive documentation file
├── scripts/
│   └── skillleaderboard.py    # Core tracking, cross-referencing & ingestion engine
├── update.py                  # Main vault updater (forwards --trending / --starred)
└── library/
    ├── upstreams.json         # Master upstream registry
    └── skills_index.json      # Master vault skills index
```
