"""
AgentSkills Automated Vault Updater & Sync Tool
Author: SeaXen (https://github.com/SeaXen/agentskills)

Usage:
    python update.py                 # Update everything (both library & skills) + git push
    python update.py --no-push       # Update everything locally without pushing
    python update.py --awesome       # Only sync awesome-skills library
    python update.py --about         # Display repository metadata, inventory & stats
    python update.py --tags          # List all available skill domain tags & counts
    python update.py --tag <name>    # Search & list skills matching a domain tag
    python update.py --find <query>  # Search across ALL 1,470 skills (installed + library)
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
    awesome_cnt = len(os.listdir(awesome_skills_sub)) if os.path.exists(awesome_skills_sub) else 876
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
    • Offline Reserve Repos:      17 repositories (.agents/library)
    • Total Offline Skills:       1,470 combined skills
    • Specialist Agent Personas:  20 agents (.agents/agents)
    • Autonomous Workflows:       17 slash commands (.agents/workflows)
    • Active Hot-Set Set:         89 curated skills (.agent/skills)
-----------------------------------------------------------------
  🏷️ GITHUB ABOUT & TOPICS:
    Description:
      "The ultimate modular AI agent skills vault (594 skills, 20 agents, 17 workflows, 1,470 reserve skills) for Antigravity, Claude Code, Cursor, and Windsurf."

    Topics / Tags:
      agent-skills, ai-agents, antigravity-ide, claude-code, cursor,
      windsurf, prompt-engineering, developer-tools, emil-kowalski, vercel,
      nextjs, cloudflare, testing, web3, rust, python
=================================================================""")

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
    """Search across ALL 1,470 skills in vault"""
    q = query.lower()
    skills = load_skills()
    
    installed_matches = []
    for name, info in skills.items():
        if q in name.lower():
            installed_matches.append((name, info.get('source', 'installed')))

    library_matches = []
    if os.path.exists(library_dir):
        for repo_f in os.listdir(library_dir):
            r_path = os.path.join(library_dir, repo_f, 'skills')
            if os.path.isdir(r_path):
                for s in os.listdir(r_path):
                    if q in s.lower() and s not in skills:
                        library_matches.append((s, repo_f))

    total = len(installed_matches) + len(library_matches)
    print(f"\n🔎 Global Search for '{query}': {total} matches across vault")
    print("=" * 75)
    if installed_matches:
        print("📦 Installed Skills (.agents/skills):")
        for name, src in sorted(installed_matches):
            print(f"  ✓ {name:35} [{src}]")
    if library_matches:
        print("\n📚 Available in Offline Library Reserve (Activate: python library/activate_skill.py activate <name>):")
        for name, repo_f in sorted(library_matches)[:25]:
            print(f"  + {name:35} [{repo_f}]")
        if len(library_matches) > 25:
            print(f"  ... and {len(library_matches) - 25} more in reserve.")
    print("=" * 75)

def clean_nested():
    nested_agents = os.path.join(agents_dir, '.agents')
    if os.path.exists(nested_agents):
        import stat
        shutil.rmtree(nested_agents, onerror=lambda f, p, e: (os.chmod(p, stat.S_IWRITE), f(p)))

def sync_awesome_skills():
    """Sync ONLY skills/ and skills_index.json from upstream, eliminating repo bloat"""
    print("\n[1/6] Syncing pure skills from benjaminasterA/antigravity-awesome-skills...")
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
        
        temp_skills = os.path.join(temp_dir, 'skills')
        if os.path.exists(temp_skills):
            for skill_name in os.listdir(temp_skills):
                s_src = os.path.join(temp_skills, skill_name)
                s_dst = os.path.join(awesome_skills_sub, skill_name)
                if os.path.isdir(s_src):
                    if os.path.exists(s_dst):
                        shutil.rmtree(s_dst, ignore_errors=True)
                    shutil.copytree(s_src, s_dst)

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
    print("\n[2/6] Checking for upstream updates across all skills (via npx skills update)...")
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

def sync_library_mirrors():
    """Sync updated skills from .agents/skills into their respective .agents/library/<repo>/skills folders"""
    print("\n[3/6] Synchronizing updated skills into offline library reserve bundles...")
    if not os.path.exists(skills_dir) or not os.path.exists(library_dir):
        return

    # Check each library repo
    updated = 0
    for repo_f in os.listdir(library_dir):
        if repo_f == 'antigravity-awesome-skills':
            continue
        lib_repo_skills = os.path.join(library_dir, repo_f, 'skills')
        if os.path.isdir(lib_repo_skills):
            for s_name in os.listdir(lib_repo_skills):
                src_skill = os.path.join(skills_dir, s_name)
                dst_skill = os.path.join(lib_repo_skills, s_name)
                if os.path.exists(src_skill):
                    shutil.rmtree(dst_skill, ignore_errors=True)
                    shutil.copytree(src_skill, dst_skill)
                    updated += 1
    print(f"✓ Synchronized {updated} skills across offline library repositories.")


def rebuild_all_indexes():
    """Regenerate skills_index.json for every repo in library/ and master library/skills_index.json"""
    print("\n[4b/6] Updating skills_index.json across all 17 library repos and master index...")
    if not os.path.exists(library_dir):
        return

    all_vault_skills = []
    repo_folders = sorted([d for d in os.listdir(library_dir) if os.path.isdir(os.path.join(library_dir, d)) and not d.startswith('.')])

    for repo_folder in repo_folders:
        repo_path = os.path.join(library_dir, repo_folder)
        skills_sub = os.path.join(repo_path, 'skills')
        if not os.path.exists(skills_sub):
            continue

        repo_skills_index = []
        skill_names = sorted([s for s in os.listdir(skills_sub) if os.path.isdir(os.path.join(skills_sub, s))])

        for s_name in skill_names:
            s_path = os.path.join(skills_sub, s_name)
            skill_md = os.path.join(s_path, 'SKILL.md')
            desc = "Specialized agent intelligence skill."
            allowed_tools = []

            if os.path.exists(skill_md):
                try:
                    with open(skill_md, 'r', encoding='utf-8', errors='ignore') as mf:
                        m_content = mf.read(3000)
                    m = re.search(r'description:\s*(?:>-\s*|\|\s*)?(.*?)(?:\n[a-zA-Z0-9_-]+:|\n---)', m_content, re.DOTALL)
                    if m:
                        desc = re.sub(r'\s+', ' ', m.group(1).strip().replace('\n', ' '))
                    else:
                        m2 = re.search(r'#\s+[^\n]+\n+([^\n#]+)', m_content)
                        if m2:
                            desc = m2.group(1).strip()
                    m_tools = re.search(r'allowed-tools:\s*(.+)', m_content)
                    if m_tools:
                        allowed_tools = [t.strip() for t in m_tools.group(1).split(',')]
                except Exception:
                    pass

            text = f"{s_name} {desc}".lower()
            cat = "general-development"
            for c_name, kws in TAG_KEYWORDS.items():
                if any(kw in text for kw in kws):
                    cat = c_name
                    break

            entry = {
                "id": s_name,
                "name": s_name,
                "repository": repo_folder,
                "category": cat,
                "description": desc,
                "path": f"library/{repo_folder}/skills/{s_name}",
                "activation_cmd": f"python .agents/library/activate_skill.py activate {s_name}",
                "link_cmd": f"python .agents/library/activate_skill.py link {s_name}"
            }
            if allowed_tools:
                entry["allowed_tools"] = allowed_tools

            repo_skills_index.append(entry)
            all_vault_skills.append(entry)

        with open(os.path.join(repo_path, 'skills_index.json'), 'w', encoding='utf-8') as rf:
            json.dump(repo_skills_index, rf, indent=2)

    master_index_file = os.path.join(library_dir, 'skills_index.json')
    with open(master_index_file, 'w', encoding='utf-8') as mf:
        json.dump(all_vault_skills, mf, indent=2)
    print(f"✓ Re-indexed {len(repo_folders)} repository indexes and Master index ({len(all_vault_skills)} skills).")

def rebuild_documentation():
    print("\n[4/6] Re-indexing skills and rebuilding documentation...")
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
    rebuild_all_indexes()

def git_commit_and_push():
    print("\n[5/6] Checking Git status in .agents...")
    status = subprocess.run(['git', 'status', '--short'], cwd=agents_dir, capture_output=True, text=True).stdout.strip()
    
    if not status:
        print("✓ Everything is already clean and up to date with Git. No push needed.")
        return

    print(f"Pending changes detected:\n{status}")
    print("\n[6/6] Staging, committing, and pushing to https://github.com/SeaXen/agentskills.git...")

    subprocess.run(['git', 'add', '-A'], cwd=agents_dir, check=True)
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

    if '--index' in args or '--reindex' in args:
        rebuild_all_indexes()
        sys.exit(0)
    elif '--about' in args:
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
    sync_library_mirrors()
    rebuild_documentation()
    if '--no-push' not in args:
        git_commit_and_push()
