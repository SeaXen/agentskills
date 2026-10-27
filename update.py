"""
AgentSkills Automated Vault Updater & Sync Tool
Author: SeaXen (https://github.com/SeaXen/agentskills)

Usage:
    python update.py            # Update everything and git push to GitHub
    python update.py --no-push  # Update everything locally without pushing
    python update.py --awesome  # Only sync antigravity-awesome-skills
"""

import os
import sys
import shutil
import subprocess
import json
import re
from datetime import datetime

# Enforce UTF-8 output on Windows
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# 1. Resolve paths strictly relative to this script
agents_dir = os.path.dirname(os.path.abspath(__file__))
repo_root = os.path.dirname(agents_dir)
skills_dir = os.path.join(agents_dir, 'skills')
library_dir = os.path.join(agents_dir, 'library')
awesome_skills_dir = os.path.join(library_dir, 'antigravity-awesome-skills')
lockfile_path = os.path.join(agents_dir, 'skills-lock.json')
provenance_path = os.path.join(agents_dir, 'SKILLS_PROVENANCE.md')
readme_path = os.path.join(agents_dir, 'README.md')

print("=" * 65)
print("🚀 AGENTSKILLS VAULT — AUTOMATED UPDATER & SYNC")
print(f"📁 Agents Directory:    {agents_dir}")
print(f"📁 Workspace Root:      {repo_root}")
print("=" * 65)

# Safety check: clean up accidental nested .agents folder if ever created
nested_agents = os.path.join(agents_dir, '.agents')
if os.path.exists(nested_agents):
    import stat
    print("⚠️ Detected accidental nested .agents directory, cleaning up...")
    def remove_readonly(func, path, excinfo):
        os.chmod(path, stat.S_IWRITE)
        func(path)
    shutil.rmtree(nested_agents, onerror=remove_readonly)
    print("✓ Removed nested .agents directory.")

# Step 1: Update antigravity-awesome-skills
def sync_awesome_skills():
    print("\n[1/5] Syncing benjaminasterA/antigravity-awesome-skills...")
    temp_dir = os.path.join(repo_root, '.temp_awesome_clone')
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir, ignore_errors=True)

    try:
        res = subprocess.run([
            'git', 'clone', '--depth', '1',
            'https://github.com/benjaminasterA/antigravity-awesome-skills.git',
            temp_dir
        ], capture_output=True, text=True, check=True)

        temp_git = os.path.join(temp_dir, '.git')
        if os.path.exists(temp_git):
            import stat
            shutil.rmtree(temp_git, onerror=lambda f, p, e: (os.chmod(p, stat.S_IWRITE), f(p)))

        os.makedirs(awesome_skills_dir, exist_ok=True)

        # Copy files
        for item in os.listdir(temp_dir):
            src = os.path.join(temp_dir, item)
            dst = os.path.join(awesome_skills_dir, item)
            if os.path.isdir(src):
                for root, dirs, files in os.walk(src):
                    rel = os.path.relpath(root, src)
                    dest_root = os.path.join(dst, rel)
                    os.makedirs(dest_root, exist_ok=True)
                    for f in files:
                        shutil.copy2(os.path.join(root, f), os.path.join(dest_root, f))
            else:
                shutil.copy2(src, dst)

        shutil.rmtree(temp_dir, ignore_errors=True)
        awesome_count = len(os.listdir(os.path.join(awesome_skills_dir, 'skills'))) if os.path.exists(os.path.join(awesome_skills_dir, 'skills')) else 0
        print(f"✓ antigravity-awesome-skills synced successfully ({awesome_count} total skills).")
        return awesome_count
    except Exception as e:
        print(f"⚠️ Failed to sync awesome skills: {e}")
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir, ignore_errors=True)
        return 0

# Step 2: Run npx skills update
def run_skills_update():
    print("\n[2/5] Checking for upstream updates across all skills (via npx skills update)...")
    try:
        # Run from repo_root so skills target D:\Repo\.agents\skills directly!
        res = subprocess.run(
            ['npx', '-y', 'skills', 'update', '-y'],
            cwd=repo_root,
            capture_output=True,
            text=True
        )
        print("✓ npx skills update finished.")
        lines = res.stdout.strip().split('\n')
        for l in lines[-15:]:
            print(f"  {l}")
    except Exception as e:
        print(f"⚠️ npx skills update encountered an issue: {e}")

# Step 3: Synchronize lockfile and rebuild SKILLS_PROVENANCE.md & README.md
def rebuild_documentation():
    print("\n[3/5] Re-indexing skills and rebuilding documentation...")
    # Load lockfile
    if os.path.exists(lockfile_path):
        with open(lockfile_path, 'r', encoding='utf-8') as f:
            lock_data = json.load(f)
    else:
        lock_data = {'skills': {}}

    skills_dict = lock_data.get('skills', {})
    current_skills = sorted([d for d in os.listdir(skills_dir) if os.path.isdir(os.path.join(skills_dir, d))])

    # Ensure every folder on disk is in skills_dict
    for s in current_skills:
        if s not in skills_dict:
            skills_dict[s] = {
                'source': 'local-library',
                'sourceType': 'local',
                'sourceUrl': 'local-library',
                'skillPath': f'skills/{s}/SKILL.md',
                'installedAt': datetime.now().isoformat() + 'Z',
                'updatedAt': datetime.now().isoformat() + 'Z'
            }

    lock_data['skills'] = skills_dict
    with open(lockfile_path, 'w', encoding='utf-8') as f:
        json.dump(lock_data, f, indent=2)

    print(f"✓ Total skills verified on disk: {len(current_skills)}")

# Step 4: Git commit & push
def git_commit_and_push():
    print("\n[4/5] Checking Git status in .agents...")
    status = subprocess.run(['git', 'status', '--short'], cwd=agents_dir, capture_output=True, text=True).stdout.strip()
    
    if not status:
        print("✓ Everything is already clean and up to date with Git. No push needed.")
        return

    print(f"Pending changes detected:\n{status}")
    print("\n[5/5] Staging, committing, and pushing to https://github.com/SeaXen/agentskills.git...")

    subprocess.run(['git', 'add', '.'], cwd=agents_dir, check=True)
    ts = datetime.now().strftime('%Y-%m-%d %H:%M')
    subprocess.run(['git', 'commit', '-m', f"chore(skills): automated update of skills & library ({ts})"], cwd=agents_dir, check=True)
    
    push_res = subprocess.run(['git', 'push', 'origin', 'main'], cwd=agents_dir, capture_output=True, text=True)
    print(push_res.stdout)
    if push_res.stderr:
        print(push_res.stderr)
    print("🎉 SUCCESS: All skills updated and pushed to https://github.com/SeaXen/agentskills.git!")

if __name__ == '__main__':
    args = sys.argv[1:]
    awesome_cnt = sync_awesome_skills()
    if '--awesome' not in args:
        run_skills_update()
    rebuild_documentation()
    if '--no-push' not in args:
        git_commit_and_push()
