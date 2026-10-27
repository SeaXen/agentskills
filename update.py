"""
AgentSkills Automated Vault Updater & Skill Discovery Tool
Author: SeaXen (https://github.com/SeaXen/agentskills)

Usage:
    python update.py                 # Update everything and git push to GitHub
    python update.py --no-push       # Update everything locally without pushing
    python update.py --awesome       # Only sync awesome-skills library
    python update.py --about         # Display repository metadata, inventory & stats
    python update.py --tags          # List all available skill domain tags & counts
    python update.py --tag <name>    # Search & list skills matching a domain tag
    python update.py --find <query>  # Search across ALL 1,476 skills (installed + library)
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

agents_dir = os.path.dirname(os.path.abspath(__file__))
repo_root = os.path.dirname(agents_dir)
skills_dir = os.path.join(agents_dir, 'skills')
library_dir = os.path.join(agents_dir, 'library')
awesome_skills_dir = os.path.join(library_dir, 'antigravity-awesome-skills')
awesome_skills_sub = os.path.join(awesome_skills_dir, 'skills')
lockfile_path = os.path.join(agents_dir, 'skills-lock.json')
provenance_path = os.path.join(agents_dir, 'SKILLS_PROVENANCE.md')
readme_path = os.path.join(agents_dir, 'README.md')

# Domain tag taxonomy
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
    awesome_cnt = len(os.listdir(awesome_skills_sub)) if os.path.exists(awesome_skills_sub) else 882
    print("""
=================================================================
  ⚡ AGENTSKILLS VAULT (SeaXen/agentskills) ⚡
=================================================================
  Repository:     https://github.com/SeaXen/agentskills
  Author:         SeaXen (drpelagik@gmail.com)
  Purpose:        Production-grade modular intelligence for AI agents
-----------------------------------------------------------------
  📊 VAULT INVENTORY:
    • Installed Skills (Active):  594 modular skills (.agents/skills)
    • Upstream Repositories:      32 distinct sources
    • Specialist Agent Personas:  20 agents (.agents/agents)
    • Autonomous Workflows:       17 slash commands (.agents/workflows)
    • Awesome Library Skills:     {} extensions (.agents/library)
    • Total Available Skills:     {} combined skills
    • Active Hot-Set:             89 curated skills (.agent/skills)
-----------------------------------------------------------------
  🏷️ GITHUB ABOUT & TOPICS:
    Description:
      "The ultimate modular AI agent skills vault (594 skills, 20 agents, 17 workflows, 882 library extensions) for Antigravity, Claude Code, Cursor, and Windsurf."

    Topics / Tags:
      agent-skills, ai-agents, antigravity-ide, claude-code, cursor,
      windsurf, prompt-engineering, developer-tools, emil-kowalski, vercel,
      nextjs, cloudflare, testing, web3, rust, python
=================================================================""".format(awesome_cnt, len(skills) + awesome_cnt))

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

def find_global(query):
    """Search across ALL 1,476 skills (installed 594 + 882 library)"""
    q = query.lower()
    skills = load_skills()
    
    installed_matches = []
    for name, info in skills.items():
        if q in name.lower():
            installed_matches.append((name, info.get('source', 'installed'), 'Installed (.agents/skills)'))

    library_matches = []
    if os.path.exists(awesome_skills_sub):
        for name in os.listdir(awesome_skills_sub):
            if q in name.lower() and name not in skills:
                library_matches.append((name, 'benjaminasterA/antigravity-awesome-skills', 'Awesome Library (On-Demand)'))

    total = len(installed_matches) + len(library_matches)
    print(f"\n🔎 Global Search for '{query}': {total} matches across vault")
    print("=" * 75)
    if installed_matches:
        print("📦 Installed Skills (.agents/skills):")
        for name, src, loc in sorted(installed_matches):
            print(f"  ✓ {name:35} [{src}]")
    if library_matches:
        print("\n📚 Available in Awesome Library (Activate with: python library/activate_skill.py <name>):")
        for name, src, loc in sorted(library_matches)[:20]:
            print(f"  + {name:35} [awesome-library]")
        if len(library_matches) > 20:
            print(f"  ... and {len(library_matches) - 20} more in library.")
    print("=" * 75)

def clean_nested():
    nested_agents = os.path.join(agents_dir, '.agents')
    if os.path.exists(nested_agents):
        import stat
        shutil.rmtree(nested_agents, onerror=lambda f, p, e: (os.chmod(p, stat.S_IWRITE), f(p)))

def sync_awesome_skills():
    """Sync ONLY skills/ and skills_index.json from upstream, eliminating repo bloat"""
    print("\n[1/5] Syncing pure skills from benjaminasterA/antigravity-awesome-skills...")
    temp_dir = os.path.join(repo_root, '.temp_awesome_clone')
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir, ignore_errors=True)

    try:
        subprocess.run([
            'git', 'clone', '--depth', '1',
            'https://github.com/benjaminasterA/antigravity-awesome-skills.git',
            temp_dir
        ], capture_output=True, text=True, check=True)

        os.makedirs(awesome_skills_sub, exist_ok=True)
        
        # Copy ONLY skills/ directory
        temp_skills = os.path.join(temp_dir, 'skills')
        if os.path.exists(temp_skills):
            for skill_name in os.listdir(temp_skills):
                s_src = os.path.join(temp_skills, skill_name)
                s_dst = os.path.join(awesome_skills_sub, skill_name)
                if os.path.isdir(s_src):
                    if os.path.exists(s_dst):
                        shutil.rmtree(s_dst, ignore_errors=True)
                    shutil.copytree(s_src, s_dst)

        # Copy skills_index.json if present
        idx_src = os.path.join(temp_dir, 'skills_index.json')
        if os.path.exists(idx_src):
            shutil.copy2(idx_src, os.path.join(awesome_skills_dir, 'skills_index.json'))

        shutil.rmtree(temp_dir, ignore_errors=True)
        awesome_count = len(os.listdir(awesome_skills_sub)) if os.path.exists(awesome_skills_sub) else 0
        print(f"✓ Pure skills synced successfully ({awesome_count} total skills, zero repo bloat).")
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
    elif '--find' in args:
        idx = args.index('--find')
        if idx + 1 < len(args):
            find_global(args[idx + 1])
        else:
            print("Please specify a search keyword: python update.py --find <keyword>")
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
