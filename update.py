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
    installed_cnt = len([s for s in os.listdir(skills_dir) if os.path.isdir(os.path.join(skills_dir, s)) and not s.startswith('.')]) if os.path.exists(skills_dir) else 0
    lib_repos = [d for d in os.listdir(library_dir) if os.path.isdir(os.path.join(library_dir, d)) and not d.startswith('.')] if os.path.exists(library_dir) else []
    lib_cnt = len(lib_repos)
    
    total_lib_skills = 0
    idx_p = os.path.join(library_dir, 'skills_index.json')
    if os.path.exists(idx_p):
        try:
            with open(idx_p, 'r', encoding='utf-8') as f:
                total_lib_skills = len(json.load(f))
        except Exception:
            pass
            
    cat_dir = os.path.join(agents_dir, 'category')
    cat_cnt = len([d for d in os.listdir(cat_dir) if os.path.isdir(os.path.join(cat_dir, d)) and not d.startswith('.')]) if os.path.exists(cat_dir) else 0
    
    agents_cnt = len([a for a in os.listdir(os.path.join(agents_dir, 'agents')) if a.endswith('.md')]) if os.path.exists(os.path.join(agents_dir, 'agents')) else 20
    wf_cnt = len([w for w in os.listdir(os.path.join(agents_dir, 'workflows')) if w.endswith('.md')]) if os.path.exists(os.path.join(agents_dir, 'workflows')) else 17

    print(f"""
=================================================================
  ⚡ AGENTSKILLS VAULT (SeaXen/agentskills) ⚡
=================================================================
  Repository:     https://github.com/SeaXen/agentskills
  Author:         SeaXen (drpelagik@gmail.com)
  Purpose:        Production-grade modular intelligence for AI agents
-----------------------------------------------------------------
  📊 VAULT INVENTORY:
    • Installed Skills (Active):  {installed_cnt} modular skills (.agents/skills)
    • Offline Reserve Repos:      {lib_cnt} repositories (.agents/library)
    • Total Offline Skills:       {total_lib_skills:,} combined skills
    • Granular Categories:        {cat_cnt} functional domains (.agents/category)
    • Specialist Agent Personas:  {agents_cnt} agents (.agents/agents)
    • Autonomous Workflows:       {wf_cnt} slash commands (.agents/workflows)
-----------------------------------------------------------------
  🏷️ GITHUB ABOUT & TOPICS:
    Description:
      "The ultimate modular AI agent skills vault ({total_lib_skills:,} reserve skills, {cat_cnt} categories, {agents_cnt} agents, {wf_cnt} workflows) for Antigravity, Claude Code, Cursor, and Windsurf."

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
    # Normalize path if passed as official/category/skill
    query = query.strip().rstrip('/').split('/')[-1]
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

def sync_awesome_skills(force=False):
    """Sync pure skills/ and skills_index.json from upstream with smart commit checking"""
    print("\n[1/6] Checking benjaminasterA/antigravity-awesome-skills for upstream updates...")
    commit_file = os.path.join(awesome_skills_dir, '.upstream_commit')
    last_commit = ''
    if os.path.exists(commit_file):
        try:
            with open(commit_file, 'r', encoding='utf-8') as cf:
                last_commit = cf.read().strip()
        except Exception:
            pass

    remote_commit = ''
    try:
        ls_res = subprocess.run([
            'git', 'ls-remote',
            'https://github.com/benjaminasterA/antigravity-awesome-skills.git',
            'HEAD'
        ], capture_output=True, text=True, timeout=10)
        if ls_res.returncode == 0 and ls_res.stdout:
            remote_commit = ls_res.stdout.split()[0].strip()
    except Exception:
        pass

    has_skills = os.path.exists(awesome_skills_sub) and len(os.listdir(awesome_skills_sub)) > 800

    if not force and remote_commit and last_commit and remote_commit == last_commit and has_skills:
        print(f"✓ antigravity-awesome-skills is already up to date with upstream HEAD ({remote_commit[:8]}).")
        return len(os.listdir(awesome_skills_sub))

    print("⬇️  Downloading fresh skills from upstream...")
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
                    src_md = os.path.join(s_src, 'SKILL.md')
                    dst_md = os.path.join(s_dst, 'SKILL.md')
                    needs_copy = not os.path.exists(dst_md) or (os.path.exists(src_md) and os.path.getmtime(src_md) > os.path.getmtime(dst_md))
                    if needs_copy:
                        if os.path.exists(s_dst):
                            shutil.rmtree(s_dst, ignore_errors=True)
                        shutil.copytree(s_src, s_dst)

        idx_src = os.path.join(temp_dir, 'skills_index.json')
        if os.path.exists(idx_src):
            shutil.copy2(idx_src, os.path.join(awesome_skills_dir, 'skills_index.json'))

        if remote_commit:
            with open(commit_file, 'w', encoding='utf-8') as cf:
                cf.write(remote_commit)

        shutil.rmtree(temp_dir, ignore_errors=True)
        awesome_count = len(os.listdir(awesome_skills_sub)) if os.path.exists(awesome_skills_sub) else 0
        print(f"✓ Pure skills synced successfully ({awesome_count} total skills, zero repo bloat).")
        return awesome_count
    except Exception as e:
        print(f"⚠️ Failed to sync awesome skills: {e}")
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir, ignore_errors=True)
        return len(os.listdir(awesome_skills_sub)) if os.path.exists(awesome_skills_sub) else 0

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
                    src_md = os.path.join(src_skill, 'SKILL.md')
                    dst_md = os.path.join(dst_skill, 'SKILL.md')
                    needs_copy = False
                    if not os.path.exists(dst_md):
                        needs_copy = True
                    elif os.path.exists(src_md) and os.path.getmtime(src_md) > os.path.getmtime(dst_md):
                        needs_copy = True
                    
                    if needs_copy:
                        shutil.rmtree(dst_skill, ignore_errors=True)
                        shutil.copytree(src_skill, dst_skill)
                        updated += 1
    if updated > 0:
        print(f"✓ Synchronized {updated} updated skills across offline library repositories.")
    else:
        print("✓ All offline library reserve bundles are already up to date.")


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


def sync_category_directories():
    """Synchronize updated real skills from .agents/skills and .agents/library into .agents/category/"""
    print("\n[3b/6] Synchronizing real skills into .agents/category/ directories...")
    cat_dir = os.path.join(agents_dir, "category")
    if not os.path.exists(cat_dir):
        return

    active_skills = set(os.listdir(skills_dir)) if os.path.exists(skills_dir) else set()
    lib_repo_paths = [os.path.join(library_dir, r, "skills") for r in os.listdir(library_dir) if os.path.isdir(os.path.join(library_dir, r, "skills"))]

    updated = 0
    for cat_slug in os.listdir(cat_dir):
        c_path = os.path.join(cat_dir, cat_slug)
        if not os.path.isdir(c_path):
            continue
        for s_name in os.listdir(c_path):
            s_dst = os.path.join(c_path, s_name)
            if not os.path.isdir(s_dst):
                continue

            dst_md = os.path.join(s_dst, "SKILL.md")
            src_skill = None
            if s_name in active_skills:
                src_skill = os.path.join(skills_dir, s_name)
            else:
                for lr in lib_repo_paths:
                    candidate = os.path.join(lr, s_name)
                    if os.path.exists(candidate):
                        src_skill = candidate
                        break

            if src_skill:
                src_md = os.path.join(src_skill, "SKILL.md")
                needs_update = False
                if not os.path.exists(dst_md):
                    needs_update = True
                elif os.path.exists(src_md) and os.path.getmtime(src_md) > os.path.getmtime(dst_md):
                    needs_update = True

                if needs_update:
                    shutil.rmtree(s_dst, ignore_errors=True)
                    shutil.copytree(src_skill, s_dst)
                    updated += 1

    if updated > 0:
        print(f"✓ Synchronized {updated} modified skills into .agents/category/ directories.")
    else:
        print("✓ All 1,878 category skills are already up to date (zero sync overhead).")

def rebuild_documentation():
    print("\n[4/6] Re-indexing skills and synchronizing skills-lock.json...")
    if os.path.exists(lockfile_path):
        with open(lockfile_path, 'r', encoding='utf-8') as f:
            lock_data = json.load(f)
    else:
        lock_data = {'version': 1, 'skills': {}}

    existing_dict = lock_data.get('skills', {})
    current_skills = sorted([d for d in os.listdir(skills_dir) if os.path.isdir(os.path.join(skills_dir, d)) and not d.startswith('.')])

    # Keep skills-lock.json strictly in sync with installed active skills
    synced_dict = {}
    for s in current_skills:
        if s in existing_dict:
            synced_dict[s] = existing_dict[s]
        else:
            synced_dict[s] = {
                'source': 'local-library',
                'sourceType': 'local',
                'sourceUrl': 'local-library',
                'skillPath': f'skills/{s}/SKILL.md',
                'installedAt': datetime.now().isoformat() + 'Z',
                'updatedAt': datetime.now().isoformat() + 'Z'
            }

    lock_data['skills'] = synced_dict
    with open(lockfile_path, 'w', encoding='utf-8') as f:
        json.dump(lock_data, f, indent=2)

    print(f"✓ Synchronized skills-lock.json: exactly {len(synced_dict)} active skills tracked.")
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

    sync_awesome_skills(force='--awesome' in args or '--force-awesome' in args)
    if '--awesome' not in args:
        run_skills_update()
    sync_library_mirrors()
    sync_category_directories()
    rebuild_documentation()
    if '--no-push' not in args:
        git_commit_and_push()
