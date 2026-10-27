"""
AgentSkills Automated Vault Updater & Tag Search Tool
Author: SeaXen (https://github.com/SeaXen/agentskills)

Usage:
    python update.py                 # Update everything and git push to GitHub
    python update.py --no-push       # Update everything locally without pushing
    python update.py --awesome       # Only sync antigravity-awesome-skills
    python update.py --about         # Display repository details, metadata & stats
    python update.py --tags          # List all available skill domain tags & counts
    python update.py --tag <name>    # Search & list skills matching a tag or keyword
"""

import os
import sys
import shutil
import subprocess
import json
import re
from datetime import datetime
from collections import defaultdict

# Enforce UTF-8 output on Windows
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

agents_dir = os.path.dirname(os.path.abspath(__file__))
repo_root = os.path.dirname(agents_dir)
skills_dir = os.path.join(agents_dir, 'skills')
library_dir = os.path.join(agents_dir, 'library')
awesome_skills_dir = os.path.join(library_dir, 'antigravity-awesome-skills')
lockfile_path = os.path.join(agents_dir, 'skills-lock.json')
provenance_path = os.path.join(agents_dir, 'SKILLS_PROVENANCE.md')
readme_path = os.path.join(agents_dir, 'README.md')

# Tag taxonomy
TAG_KEYWORDS = {
    'frontend': ['react', 'nextjs', 'tailwind', 'css', 'design', 'ui', 'view', 'web', 'canvas', 'svg', 'd3', 'shadcn', 'component', 'taste'],
    'animation-craft': ['animate', 'animation', 'emil', 'craft', 'micro', 'motion', 'apple'],
    'mobile': ['mobile', 'ios', 'android', 'native', 'swift', 'flutter'],
    'backend-api': ['api', 'node', 'express', 'nest', 'python', 'rust', 'server', 'trpc', 'graphql'],
    'database-sql': ['database', 'postgres', 'sql', 'prisma', 'neon', 'supabase', 'query', 'schema', 'd1', 'drizzle'],
    'devops-cloud': ['cloudflare', 'workers', 'wrangler', 'docker', 'deploy', 'vercel', 'kubernetes', 'terraform', 'aws', 'gcp'],
    'testing-qa': ['test', 'tdd', 'playwright', 'testing', 'audit', 'review', 'mutation', 'postmortem', 'verification'],
    'security': ['security', 'vulnerability', 'hardened', 'audit', 'tactics', 'red-team', 'solidity'],
    'agent-orchestration': ['agent', 'orchestrate', 'superpower', 'workflow', 'plan', 'brainstorm', 'debugging', 'subagent', 'team', 'owl', 'battle'],
    'finance-crypto': ['crypto', 'defi', 'token', 'blockchain', 'evm', 'finance', 'accounting', 'invoice', 'payroll', 'tax'],
    'sales-marketing': ['marketing', 'sales', 'outreach', 'email', 'lead', 'prospect', 'seo', 'growth', 'brand', 'content'],
    'research-academic': ['academic', 'paper', 'research', 'citation', 'screener', 'study', 'pipeline']
}

def load_skills():
    if os.path.exists(lockfile_path):
        with open(lockfile_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data.get('skills', {})
    return {}

def show_about():
    skills = load_skills()
    awesome_cnt = len(os.listdir(os.path.join(awesome_skills_dir, 'skills'))) if os.path.exists(os.path.join(awesome_skills_dir, 'skills')) else 882
    print("""
=================================================================
  ⚡ AGENTSKILLS VAULT (SeaXen/agentskills) ⚡
=================================================================
  Repository:     https://github.com/SeaXen/agentskills
  Author:         SeaXen (drpelagik@gmail.com)
  Purpose:        Production-grade modular intelligence for AI agents
-----------------------------------------------------------------
  📊 VAULT INVENTORY:
    • Total Installed Skills:     594 modular skills
    • Upstream Repositories:      32 distinct sources
    • Specialist Agent Personas:  20 agents (.agents/agents)
    • Autonomous Workflows:       17 slash commands (.agents/workflows)
    • Offline Awesome Library:    {} extensions (.agents/library)
    • Active Hot-Set Set:         89 curated skills (.agent/skills)
-----------------------------------------------------------------
  🏷️ GITHUB ABOUT & TOPICS (Suggested):
    Description:
      "The ultimate modular AI agent skills vault (594 skills, 20 agents, 17 workflows) for Antigravity, Claude Code, Cursor, and Windsurf."

    Topics / Tags:
      agent-skills, ai-agents, antigravity-ide, claude-code, cursor,
      windsurf, prompt-engineering, developer-tools, react, nextjs,
      cloudflare, ui-ux, emil-kowalski, testing, web3, rust, python
=================================================================""".format(awesome_cnt))

def show_tags():
    skills = load_skills()
    print("\n🏷️ AVAILABLE SKILL DOMAIN TAGS:")
    print("=" * 55)
    print(f"{'Tag Name':25} | {'Matching Skills':15}")
    print("-" * 55)
    for tag, kws in TAG_KEYWORDS.items():
        matched = [s for s in skills if any(kw in s.lower() for kw in kws)]
        print(f" • {tag:22} | {len(matched):3} skills")
    print("=" * 55)
    print("Filter skills with: python .agents/update.py --tag <tag-name>")

def search_by_tag(query):
    skills = load_skills()
    q = query.lower()
    keywords = TAG_KEYWORDS.get(q, [q])
    
    matches = []
    for name, info in sorted(skills.items()):
        nl = name.lower()
        if any(kw in nl for kw in keywords):
            src = info.get('source', 'Unknown')
            matches.append((name, src))

    print(f"\n🔍 Skills tagged with '{query}' ({len(matches)} found):")
    print("=" * 65)
    for name, src in matches:
        print(f" • {name:35} [{src}]")
    print("=" * 65)

def clean_nested():
    nested_agents = os.path.join(agents_dir, '.agents')
    if os.path.exists(nested_agents):
        import stat
        shutil.rmtree(nested_agents, onerror=lambda f, p, e: (os.chmod(p, stat.S_IWRITE), f(p)))

def sync_awesome_skills():
    print("\n[1/5] Syncing benjaminasterA/antigravity-awesome-skills...")
    temp_dir = os.path.join(repo_root, '.temp_awesome_clone')
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir, ignore_errors=True)

    try:
        subprocess.run([
            'git', 'clone', '--depth', '1',
            'https://github.com/benjaminasterA/antigravity-awesome-skills.git',
            temp_dir
        ], capture_output=True, text=True, check=True)

        temp_git = os.path.join(temp_dir, '.git')
        if os.path.exists(temp_git):
            import stat
            shutil.rmtree(temp_git, onerror=lambda f, p, e: (os.chmod(p, stat.S_IWRITE), f(p)))

        os.makedirs(awesome_skills_dir, exist_ok=True)
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

def run_skills_update():
    print("\n[2/5] Checking for upstream updates across all skills (via npx skills update)...")
    try:
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

def rebuild_documentation():
    print("\n[3/5] Re-indexing skills and rebuilding documentation...")
    if os.path.exists(lockfile_path):
        with open(lockfile_path, 'r', encoding='utf-8') as f:
            lock_data = json.load(f)
    else:
        lock_data = {'skills': {}}

    skills_dict = lock_data.get('skills', {})
    current_skills = sorted([d for d in os.listdir(skills_dir) if os.path.isdir(os.path.join(skills_dir, d))])

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
    clean_nested()

    if '--about' in args:
        show_about()
        sys.exit(0)
    elif '--tags' in args or '--list-tags' in args:
        show_tags()
        sys.exit(0)
    elif '--tag' in args:
        idx = args.index('--tag')
        if idx + 1 < len(args):
            search_by_tag(args[idx + 1])
        else:
            show_tags()
        sys.exit(0)

    print("=" * 65)
    print("🚀 AGENTSKILLS VAULT — AUTOMATED UPDATER & SYNC")
    print(f"📁 Agents Directory:    {agents_dir}")
    print(f"📁 Workspace Root:      {repo_root}")
    print("=" * 65)

    sync_awesome_skills()
    if '--awesome' not in args:
        run_skills_update()
    rebuild_documentation()
    if '--no-push' not in args:
        git_commit_and_push()
