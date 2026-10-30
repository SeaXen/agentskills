# ⚡ skills.sh Vault Tracker & Synchronizer

> Dedicated tool for humans and AI agents to audit, track, and ingest high-traction skill bundles from [skills.sh](https://www.skills.sh/) directly into your local agent vault (`.agents/library`), categorize their skills across all 38 taxonomy domains, and synchronize Cloudflare R2 / Git remote.

---

## 🎯 Features

- **Install Threshold Filtering**: Default to `>= 100K` installs (`--min-installs 100k`), or filter by any threshold (`--min-installs 500k`, `--min-installs 1m`).
- **Audit & Coverage Reporting (`--check`)**: Instantly inspect which skills.sh repositories are already in your vault vs. which are missing.
- **One-Command Ingestion (`--sync`)**: Automatically clones and downloads missing repositories using blobless sparse checkout with fast GitHub Zip fallback.
- **Automated Taxonomy Categorization**: Automatically calls `update.py --reindex` to classify newly ingested skills across all 38 categories (`category/*`), update the Master index, and sync to Cloudflare R2.
- **Git Push Integration (`--push`)**: Automatically stages, commits, and pushes to remote `main`.
- **Targeted Single-Repo Ingestion (`--repo <owner/repo>`)**: Ingest any specific skills.sh bundle repository on demand.
- **Cross-Platform**: Run natively via Python, Windows CMD (`.bat`), PowerShell (`.ps1`), or Linux/macOS Bash (`.sh`).

---

## 💻 CLI Commands & Examples

### 1. Audit Vault Status (Default Check)

Audit all repositories with >= 100K installs against your local library:

```bash
# Windows (CMD / PowerShell)
skillssh.bat --check
.\skillssh.ps1 --check

# Linux / macOS
./skillssh.sh --check

# Direct Python
python skillssh.py --check
```

### 2. Audit by Custom Install Range

```bash
# Check only 500K+ install repositories
python skillssh.py --check --min-installs 500k

# Check only 1M+ mega repositories
python skillssh.py --check --min-installs 1m

# Check repositories in a specific range (e.g. 100K to 500K)
python skillssh.py --check --min-installs 100k --max-installs 500k
```

### 3. Generate Markdown Report

Export an updated markdown leaderboard document:

```bash
python skillssh.py --check --markdown
```

### 4. Ingest Missing Repositories & Re-index

Download all missing repositories matching threshold and automatically categorize their skills:

```bash
python skillssh.py --sync
```

### 5. Full End-to-End Sync & Git Push

Download missing repositories, re-index categories, and push cleanly to GitHub:

```bash
python skillssh.py --sync --push
```

### 6. Ingest a Single Specific Repository

Target any repository from skills.sh directly:

```bash
python skillssh.py --sync --repo vercel-labs/skills
```

### 7. Force Refresh Live Data

Bypass the 24-hour local cache and re-crawl the live sitemap from skills.sh:

```bash
python skillssh.py --check --refresh
```

### 8. JSON Output for AI Agents & CI/CD

```bash
python skillssh.py --check --json
```

---

## 📁 File Structure

```text
D:/Repo/.agents/skillssh/
├── skillssh.py               # Core Python engine
├── skillssh.bat              # Windows Command Prompt launcher
├── skillssh.ps1              # Windows PowerShell launcher
├── skillssh.sh               # Linux & macOS Bash launcher
├── .cache_skills_sh.json     # 24h cached sitemap and repository dataset
└── README.md                 # Complete documentation and usage guide
```
