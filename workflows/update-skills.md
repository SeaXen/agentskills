---
description: Automatically check and update all skills from upstream repositories, sync antigravity-awesome-skills, and git push to GitHub.
---

# /update-skills Workflow

Run this workflow whenever you want to check for upstream updates across all skills and sync the latest versions to your GitHub repository.

## Execution Steps

1. Run the master update script from PowerShell:
   ```powershell
   python .agents/update.py
   # Or using the launcher:
   .\.agents\update.ps1
   ```
2. The script automatically:
   - Syncs and updates skills across all 36 offline reserve repositories (2,031 total skills).
   - Runs skill updates across all active and upstream skill sources.
   - Verifies all skills for valid `SKILL.md` structure.
   - Re-indexes `skills-lock.json` and updates `SKILLS_PROVENANCE.md` and `README.md`.
   - Auto-commits and pushes all changes to `https://github.com/SeaXen/agentskills.git`.
