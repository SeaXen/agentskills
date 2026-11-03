---
name: medsea-multi-platform-sync
description: Sync medical content from /mnt/tb/Medicine to MedSea across 4 platforms — local repo, GitHub (SeaXen/MedSea), Notion (medsea.notion.site), and the MedSea website (localhost:8855). Use when user asks to "sync", "100% match", "add all information", or "check [chapters] all topic" against /mnt/tb/Medicine. Embeds rate-limit handling, APPEND-only strategy, and the channel root IDs so future sessions start ready to sync.
---

# MedSea Multi-Platform Sync

Sync Davidson 25th Edition content from `/mnt/tb/Medicine` to four targets in lockstep: local MedSea repo (`/mnt/tb/Sea-knowledge/#MedSea`), GitHub, Notion, and the Docker-served website.

## When to use

- User asks "is Ch X-Y 100% complete?" or "sync to all platforms"
- User says "I said add all a to z" or "100% match from medicine notes"
- After `/mnt/tb/Medicine` is edited, refresh the four surfaces
- Notion / website / git have drifted from the local repo

## The four platforms (in order)

1. **Local repo** — `/mnt/tb/Sea-knowledge/#MedSea/chapters/{N-name}/`
   - Ch 16, 19 use `diseases/{slug}/topic.md` format
   - Ch 17, 18, 20 use `diseases/{slug}/{slug}.md` (note: same name as dir, not `topic.md`) AND `source/*.md` flat files
   - All chapters have a `hubs/` directory with auto-generated hub manifests
2. **Git** — `git add` then `git commit -m "Ch X-Y: 100% match from /mnt/tb/Medicine source"`, push `origin main`
3. **Notion** — page tree under each chapter root, with topic pages nested under hub pages
4. **Website** — `site/{N-name}/topics.json` + `diseases/{slug}/topic.md` + `topic.html` + `topic.png`. Build via the docker rebuild script in `/tmp/redeploy_medsea_v2.sh`

## Source-of-truth and naming

- Source: `/mnt/tb/Medicine/{ChapterName}/*.md` (or `*.md` in subdirs for Ch 16)
- Davidson 25th Edition chapter numbering: Ch 11 Poisoning, 12 Envenomation, 13 Environmental Medicine (NOT "Austere"), 14 Infectious Disease, 15 STI, 16 Cardiology, 17 Respiratory, 18 Nephrology, 19 Biochemistry, 20 Endocrinology
- Skip source files matching: `*Hierarchy*.md`, `*MOC*.md`, `*Roadmap*.md`, `*.py`, `__pycache__/`
- Subdirs of `/mnt/tb/Medicine/{Ch}/` are HUB OVERVIEWS — they live in `chapters/{N}/hubs/` or are auto-generated manifests. Do NOT count them as missing disease topics.
- MedSea local has BOTH the disease topic and a hub manifest; both come from the same source dir but in different output paths.

## Notion API essentials (read this before any sync)

**Rate limit: 3 RPS per workspace.** The single biggest source of "stuck" runs is ignoring this.

**Use a global threading.Lock + 0.36s sleep = 2.5 RPS, safe under the limit:**
```python
import threading
RATE = 0.36
_last = [0]
_lock = threading.Lock()

def http(method, url, data=None, retries=4):
    with _lock:
        wait = RATE - (time.time() - _last[0])
        if wait > 0: time.sleep(wait)
        _last[0] = time.time()
    # ... urllib.request.Request + handle 429 with Retry-After header
```

**DELETE is 5-10x slower than PATCH** because of the per-block round-trips. For 100+ blocks per page × 100+ pages, DELETE will take hours AND trip rate limits that take 30+ min to recover from. **Prefer APPEND-ONLY:** PATCH new content below the existing content with a divider + callout header so users see "📘 MedSea 100% Content (synced YYYY-MM-DD)".

**APPEND-only is acceptable** for sync (creates a duplicate of the old content above) because the user can manually archive it. DELETE-only will block for hours. PATCH-then-DELETE compounds both problems.

**Don't use `bash -lic` for background Python runs.** Causes `tcsetattr: Inappropriate ioctl for device` and the wrapper exits silently mid-job. Use `terminal(background=true)` instead.

**Topic matching by Notion title** — Notion titles like `11.1.20 General Principles of Poisoning Management` need fuzzy matching against MedSea slugs like `11.1.20-general-principles-of-poisoning-management`. Cleanup regex: `re.sub(r"^\d+\.\d+(?:\.\d+)?\s+", "", title).lower()`. The 139/141 match rate is normal — the 2 missing are usually title mismatches (e.g. `PCP / PJP` suffix) that need special handling.

## Notion chapter root IDs (verified 2026-06-21)

```
11 Poisoning:        abc75846ef544efcb3b78f00134f50b2
12 Envenomation:     fce508f973a64d58b48ad1e2d186e39d
13 Austere/Env Med:  b9b201cbbecc4eaab3c4b6c958c8ac11
14 Infectious Dis:   eb9d6efbe3bb4ccc8302396a8edc57cf
15 STI:              19c59a0895cd4ea4bee4e69d90ce37c8
16 Cardiology:       8baa010d-9cc9-4c48-8261-36417d383973
17 Respiratory:      3855588e-846f-8189-bb8c-ca4e98407910
18 Nephrology:       710f2153-44c3-4692-af75-84e89e714ff0
19 Biochemistry:     184c3802-12d9-4c48-a17c-d879d941e6a3
20 Endocrinology:    9db6455d-6ae8-40f0-ac29-129217d6ccef
```

**Ch 21-32 root IDs (verified 2026-06-21, extracted from MedSea `site/{N}/topics.json` `notion_url` field — see Discovery shortcut below):**

```
21 Diabetes:         e6939ea1-fa3d-4176-84fa-442a673efdb5
22 Gastroenterology:  bbfd9779-dff4-...
23 Hepatology:        b916d8da-dff4-...
24 Haematology:       3b59159a-...
25 Rheumatology:      fbf3e716-...
26 Dermatology:       02211b2a-0d2a-...
27 Neurology:         c76acd09-...
28 Ophthalmology:     ff44045a-...
29 Psychiatry:        9d121dc4-...
30 Maternal Med:      40913537-...
31 Adolescent:        7a368237-...
32 Ageing:            ed39c5f1-...
```

(Full 32-char IDs stored in `references/notion-root-ids.md` — copy from there to avoid transcription errors.)

**Discovery shortcut** (no Notion API call needed for any chapter — the `notion_url` is already in the MedSea site data):
```python
import json, re
ch_slug = "21-diabetes-mellitus"
d = json.load(open(f"/mnt/tb/Sea-knowledge/#MedSea/site/{ch_slug}/topics.json"))
url = d["notion_url"]   # https://medsea.notion.site/Chapter-21-Diabetes-mellitus-e6939ea1fa3d417684fa442a673efdb5
m = re.search(r"([a-f0-9]{32})$", url.replace("-", ""))
hex_id = m.group(1)
root_id = f"{hex_id[:8]}-{hex_id[8:12]}-{hex_id[12:16]}-{hex_id[16:20]}-{hex_id[20:]}"
```

Notion token: `/root/.hermes/.env` line `NOTION_API_KEY=***`. GitHub PAT also in `/root/.hermes/.env`.

## MD to Notion blocks (the conversion)

Block-type mapping (one block per non-empty MD line, not per character):
- `# ` → `heading_1`
- `## ` → `heading_2`
- `### ` → `heading_3`
- `- ` or `* ` → `bulleted_list_item`
- `1. ` → `numbered_list_item`
- `> [!tip]`, `> [!info]`, `> [!important]` → `callout` (extract text after the `[!tag]`)
- ` ```lang ` ... ` ``` ` → `code` block (lang falls back to `plain text`; cap content at 1900 chars)
- everything else → `paragraph`

**Skip Obsidian nav before converting:** `Related: [[...]]` lines and `> ` lines containing `[[` (wiki links). These are navigation, not content.

**Append in batches of 100 blocks per PATCH** (Notion's max). Use `/blocks/{page_id}/children` with `{"children": [...]}` body. A typical MedSea topic with 200+ source lines becomes ~250-500 Notion blocks → 3-5 PATCH calls.

## Pitfalls

- **`git show HEAD --name-only` returns 0 for chapters whose path glob doesn't match.** Use `git ls-tree -r HEAD --name-only | grep chapters/X` instead.
- **`comm` with mixed space/underscore filenames** makes everything look missing. Normalize BOTH sides: `tr ' ' '_' | tr -d '()' | sed 's/_-_/-/g' | sort -u` applied to both source and local before `comm -23`.
- **Ch 16 working-dir drift**: the website build process overwrites `chapters/16-cardiology/diseases/*/topic.md` with a slim 95-line rendered version, REPLACING the full 204-line content committed in `85ad30a`. The full content is preserved in `site/16-cardiology/diseases/*/topic.md` (built from HEAD). Detection: `git status -s chapters/16-cardiology/ | wc -l` > 300 = drift present. To restore: use Python (not bash) — see the Unicode filenames pitfall below. Do NOT commit the rendered slim version — it's a regression.
- **Git working-dir drift can hit ANY chapter after a website rebuild** — always run `git status -s chapters/{N}/` before declaring "100% complete". For each `M ` line, sample one file: HEAD char count vs working dir char count. If HEAD > 2× working dir, the build replaced source with rendered content. Revert: `git checkout HEAD -- chapters/{N}/` (or Python for unicode names).
- **Unicode filenames in `git checkout HEAD --`**: Files with `≥ ≤ → ü ö` (e.g. Ch 16's `16.11.71-definition-lvef-≤40%-…`) FAIL when reverted via `bash xargs` because the shell escapes `\u2265` as literal text, not the unicode char. Use Python `os.listdir()` + `subprocess.run(["git", "checkout", "HEAD", "--", path])` to handle them. About 5 files in Ch 16 need this.
- **Notion `tcsetattr` after-hours** — if a previous sync bombed with rate limits, even 5 min wait is not enough. APPEND-only avoids this entirely.
- **Don't trust "100% match" claims from earlier sessions without re-verifying.** This session discovered Ch 17-20 hubs/ was already in place (the "33 missing" claim was wrong because I only checked one directory). Always check source/, diseases/, AND hubs/ for completeness. Also check `site/{N}/topics.json` for actual served count vs working dir count.
- **The v5-style DELETE+APPEND approach** can take 10+ hours for ~950 topics because each topic's DELETE loop runs 100+ sequential API calls. APPEND-only finishes in 15 min for the same volume.
- **Source file "missing" false positives**: `Chapter X Roadmap.md` (status: draft), hub overviews (`Subdir/Subdir.md` — file name == parent dir name), and MOC drafts are **build tracking, not real content**. Exclude them from source counts. The skip logic: `if normalize(filename) == normalize(parent_dir): continue`.
- **Topic count discrepancies between source and MedSea are normal** when MedSea splits source topics into more granular sub-topics (e.g. Ch 23 Hepatology: 117 source files → 349 MedSea topics). Reverse-check: for each source topic, find at least one MedSea topic sharing ≥2 significant keywords. If 0 unmapped source topics → "100% complete" even with count mismatch.

## Verification (always do this before reporting "100%")

For each chapter, run a content-size check on Notion vs MedSea source:
- Sample 5-10 topics per chapter
- Compare chars (or block count) — Notion should be ≥0.85x of MedSea chars
- A topic with Notion at 0.4-0.6x of MedSea = NOT synced, must be updated

For local/git, the test is simpler: `git ls-tree -r HEAD --name-only | grep chapters/{N}` should match the local `find chapters/{N}/diseases -name "*.md"` count (or `source/` count for Ch 17, 18, 20).

## Reference scripts and notes

- `scripts/notion_append_sync.py` — drop-in APPEND-only sync script. Copy, set `CHAPTER_ROOTS` / `CH_SLUGS` / `CH_SRC` for the chapters you want, run with `terminal(background=true, notify_on_complete=true)`. Handles 139 topics in ~15 min.
- `references/notion-special-cases.md` — patterns for the 1-5 unmatched topics that the regular loop leaves behind: append to existing page with title mismatch, or create new page under a hub.

External scripts in `/tmp/` (one-off runs from previous sessions, may have been cleaned up):
- `/tmp/sync_ch16_20_v5.py` — DELETE+APPEND pattern, 951 topics, ~2.9 hours. Slow but thorough.
- `/tmp/sync_ch11_15_v4.py` — APPEND-only pattern, 139 topics, 15 min. The recommended template.
- `/tmp/sync_ch11_15_missing.py` — special-case handlers for unmatched topics.
- `/tmp/redeploy_medsea_v2.sh` — Docker rebuild of the website after local changes.
- `/tmp/verify_notion.py` — content size check between MedSea local and Notion.

## Related skills

- `medical-fcps-mrcp-note-creation` — for creating individual notes (not sync)
- `medical-folder-audit` — for completeness audits before sync
- `subagent-batch-note-conversion` — for batch-converting scaff directories to FCPS notes
