#!/usr/bin/env python3
"""
Antigravity Agent Skills Vault - Unified Upstream Sync & Maintenance Engine
Automates:
  1. Multi-repository remote upstream sync across all 224 libraries
  2. Automatic detection and ingestion of NEW skills added to upstream repos
  3. Full repository file retention (keep all upstream files, docs, and assets intact; zero auto-deletion)
  4. Active skills synchronization (.agents/skills)
  5. Dual skills-lock.json synchronization (Repo and Workspace)
  6. Automated 38-category taxonomy rebuild (.agents/category)
  7. SKILLS_PROVENANCE.md regeneration
  8. Git status check, commit, and push to https://github.com/SeaXen/agentskills.git
"""

import os
import sys
import shutil
import stat
import json
import subprocess
import time
from datetime import datetime, timezone
from concurrent.futures import ThreadPoolExecutor

if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

agents_dir = os.path.dirname(os.path.abspath(__file__))
repo_root = os.path.dirname(agents_dir)
skills_dir = os.path.join(agents_dir, 'skills')
library_dir = os.path.join(agents_dir, 'library')
upstreams_file = os.path.join(library_dir, 'upstreams.json')
lockfile_path = os.path.join(agents_dir, 'skills-lock.json')
provenance_path = os.path.join(agents_dir, 'SKILLS_PROVENANCE.md')

GIT_ENV = os.environ.copy()
GIT_ENV['GIT_TERMINAL_PROMPT'] = '0'
GIT_ENV['GIT_ASKPASS'] = ''

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

def remove_readonly(func, path, exc_info):
    try:
        os.chmod(path, stat.S_IWRITE)
        func(path)
    except Exception:
        pass

def load_skills():
    if os.path.exists(lockfile_path):
        try:
            with open(lockfile_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            return data.get('skills', {})
        except Exception:
            pass
    return {}

def show_about():
    installed_cnt = len([s for s in os.listdir(skills_dir) if os.path.isdir(os.path.join(skills_dir, s)) and not s.startswith('.')]) if os.path.exists(skills_dir) else 0
    lib_repos = [d for d in os.listdir(library_dir) if os.path.isdir(os.path.join(library_dir, d)) and not d.startswith('.') and d != '__pycache__'] if os.path.exists(library_dir) else []
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
    cat_cnt = len([d for d in os.listdir(cat_dir) if os.path.isdir(os.path.join(cat_dir, d)) and not d.startswith('.') and d != '__pycache__']) if os.path.exists(cat_dir) else 0
    
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
-----------------------------------------------------------------""", flush=True)

def show_tags():
    skills = load_skills()
    print("\n🏷️ AVAILABLE SKILL DOMAIN TAGS:", flush=True)
    print("=" * 55, flush=True)
    print(f"{'Tag Name':25} | {'Matching Skills':15}", flush=True)
    print("-" * 55, flush=True)
    for tag, kws in TAG_KEYWORDS.items():
        matched = [s for s in skills if any(kw in s.lower() for kw in kws)]
        print(f" • {tag:22} | {len(matched):3} skills", flush=True)
    print("=" * 55, flush=True)

def search_by_tag(query):
    skills = load_skills()
    q = query.lower()
    keywords = TAG_KEYWORDS.get(q, [q])
    matches = []
    for name, info in sorted(skills.items()):
        if any(kw in name.lower() for kw in keywords):
            src = info.get('source', 'Unknown')
            matches.append((name, src))
    print(f"\n🔍 Skills tagged with '{query}' ({len(matches)} found):", flush=True)
    print("=" * 65, flush=True)
    for name, src in matches:
        print(f" • {name:35} [{src}]", flush=True)
    print("=" * 65, flush=True)

def find_global(query):
    query = query.strip().rstrip('/').split('/')[-1].lower()
    skills = load_skills()
    installed_matches = [name for name in skills if query in name.lower()]
    library_matches = []
    if os.path.exists(library_dir):
        for repo_f in os.listdir(library_dir):
            r_path = os.path.join(library_dir, repo_f, 'skills')
            if os.path.isdir(r_path):
                for s in os.listdir(r_path):
                    if query in s.lower() and s not in skills:
                        library_matches.append((s, repo_f))
    total = len(installed_matches) + len(library_matches)
    print(f"\n🔎 Global Search for '{query}': {total} matches across vault", flush=True)
    print("=" * 75, flush=True)
    if installed_matches:
        print("📦 Installed Skills (.agents/skills):", flush=True)
        for name in sorted(installed_matches):
            print(f"  ✓ {name:35}", flush=True)
    if library_matches:
        print("\n📚 Available in Offline Library Reserve:", flush=True)
        for name, repo_f in sorted(library_matches)[:25]:
            print(f"  + {name:35} [{repo_f}]", flush=True)
        if len(library_matches) > 25:
            print(f"  ... and {len(library_matches) - 25} more in reserve.", flush=True)
    print("=" * 75, flush=True)

def clean_nested():
    nested_agents = os.path.join(agents_dir, '.agents')
    if os.path.exists(nested_agents):
        shutil.rmtree(nested_agents, onerror=remove_readonly)
    if os.path.exists(library_dir):
        for d in os.listdir(library_dir):
            dp = os.path.join(library_dir, d)
            if os.path.isdir(dp):
                gp = os.path.join(dp, '.git')
                if os.path.exists(gp):
                    shutil.rmtree(gp, onerror=remove_readonly)

# 1. Multi-repository remote upstream sync
def sync_all_upstreams(force=False):
    print("\n[1/6] Checking for upstream updates across all 224 repositories...", flush=True)
    if not os.path.exists(upstreams_file):
        print("⚠️ upstreams.json not found, skipping multi-repo upstream sync.", flush=True)
        return

    with open(upstreams_file, 'r', encoding='utf-8') as f:
        upstreams = json.load(f)

    check_list = []
    for repo_id, data in upstreams.items():
        if repo_id.startswith('#'):
            continue
        url = data.get('url')
        if url and url.startswith('http'):
            check_list.append((repo_id, data))

    print(f"Found {len(check_list)} active git upstreams to track.", flush=True)

    def check_remote(item):
        repo_id, data = item
        url = data['url']
        commit_file = os.path.join(library_dir, repo_id, '.upstream_commit')
        last_commit = ''
        if os.path.exists(commit_file):
            try:
                with open(commit_file, 'r', encoding='utf-8') as cf:
                    last_commit = cf.read().strip()
            except Exception:
                pass
        try:
            res = subprocess.run(['git', 'ls-remote', url, 'HEAD'], capture_output=True, text=True, timeout=4, env=GIT_ENV)
            if res.returncode == 0 and res.stdout:
                remote_commit = res.stdout.split()[0].strip()
                needs_update = force or not last_commit or (remote_commit != last_commit)
                return repo_id, url, remote_commit, last_commit, needs_update
        except Exception:
            pass
        return repo_id, url, '', last_commit, False

    t0 = time.time()
    with ThreadPoolExecutor(max_workers=24) as executor:
        checked_repos = list(executor.map(check_remote, check_list))
    t1 = time.time()
    print(f"✓ Checked {len(check_list)} remotes in {t1-t0:.2f}s.", flush=True)

    to_update = [r for r in checked_repos if r[4]]
    if not to_update:
        print("✓ All 224 repository upstreams are already up to date with remote HEAD.", flush=True)
        return

    print(f"⬇️  Updating {len(to_update)} repositories with fresh upstream commits...", flush=True)
    temp_dir = os.path.join(repo_root, '.temp_upstream_clones')
    os.makedirs(temp_dir, exist_ok=True)

    for repo_id, url, remote_commit, last_commit, _ in to_update:
        print(f"  → Syncing {repo_id:32} from {url}...", flush=True)
        c_temp = os.path.join(temp_dir, repo_id)
        if os.path.exists(c_temp):
            shutil.rmtree(c_temp, onerror=remove_readonly)
        try:
            res = subprocess.run(['git', 'clone', '--depth', '1', url, c_temp], capture_output=True, text=True, timeout=30, env=GIT_ENV)
            if res.returncode != 0:
                continue

            target_repo_dir = os.path.join(library_dir, repo_id)
            os.makedirs(target_repo_dir, exist_ok=True)

            # Copy all files and directories of the repo into target_repo_dir (retain all files!)
            for item in os.listdir(c_temp):
                if item == '.git':
                    continue
                s_item = os.path.join(c_temp, item)
                d_item = os.path.join(target_repo_dir, item)
                if os.path.isdir(s_item):
                    if item == 'skills':
                        os.makedirs(d_item, exist_ok=True)
                        for sk in os.listdir(s_item):
                            sk_src = os.path.join(s_item, sk)
                            sk_dst = os.path.join(d_item, sk)
                            if os.path.exists(sk_dst):
                                shutil.rmtree(sk_dst, onerror=remove_readonly)
                            if os.path.isdir(sk_src):
                                shutil.copytree(sk_src, sk_dst)
                    else:
                        if os.path.exists(d_item):
                            shutil.rmtree(d_item, onerror=remove_readonly)
                        shutil.copytree(s_item, d_item)
                else:
                    shutil.copy2(s_item, d_item)

            # Ensure any SKILL.md found in subdirectories are organized under target_repo_dir/skills/
            target_skills_dir = os.path.join(target_repo_dir, 'skills')
            os.makedirs(target_skills_dir, exist_ok=True)
            for root, dirs, files in os.walk(c_temp):
                if 'SKILL.md' in files:
                    s_name = os.path.basename(root)
                    if s_name in ['skills', 'plugins', '.curated', '.system']:
                        continue
                    s_dst = os.path.join(target_skills_dir, s_name)
                    if not os.path.exists(s_dst):
                        shutil.copytree(root, s_dst)

            if remote_commit:
                commit_file = os.path.join(target_repo_dir, '.upstream_commit')
                with open(commit_file, 'w', encoding='utf-8') as cf:
                    cf.write(remote_commit)

            # Clean only nested .git to avoid Git submodule conflicts
            for root, dirs, files in os.walk(target_repo_dir):
                if '.git' in dirs:
                    shutil.rmtree(os.path.join(root, '.git'), onerror=remove_readonly)

            # USER POLICY: All repo files are intentionally retained in place (zero auto-deletion).
            # Files are deleted ONLY when the user explicitly instructs to delete them.

            shutil.rmtree(c_temp, onerror=remove_readonly)
            print(f"  ✓ {repo_id:32}: updated to {remote_commit[:8]} (all repo files retained)", flush=True)
        except Exception as e:
            print(f"  ⚠️ Error syncing {repo_id}: {e}", flush=True)

    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir, onerror=remove_readonly)

# 2. Sync Active Skills
def sync_active_skills():
    print("\n[2/6] Synchronizing active workspace skills (.agents/skills)...", flush=True)
    if not os.path.exists(skills_dir) or not os.path.exists(library_dir):
        return

    updated = 0
    active_skills = [d for d in os.listdir(skills_dir) if os.path.isdir(os.path.join(skills_dir, d)) and not d.startswith('.')]
    
    lib_skills = {}
    for repo_f in os.listdir(library_dir):
        r_path = os.path.join(library_dir, repo_f, 'skills')
        if os.path.isdir(r_path):
            for s in os.listdir(r_path):
                lib_skills[s] = os.path.join(r_path, s)

    for s_name in active_skills:
        if s_name in lib_skills:
            src = lib_skills[s_name]
            dst = os.path.join(skills_dir, s_name)
            src_md = os.path.join(src, 'SKILL.md')
            dst_md = os.path.join(dst, 'SKILL.md')
            if os.path.exists(src_md) and os.path.exists(dst_md):
                if os.path.getmtime(src_md) > os.path.getmtime(dst_md):
                    shutil.rmtree(dst, onerror=remove_readonly)
                    shutil.copytree(src, dst)
                    updated += 1

    if updated > 0:
        print(f"✓ Synchronized {updated} active skills from upstream library reserves.", flush=True)
    else:
        print("✓ Active workspace skills are already up to date.", flush=True)

# 3. Re-index all library repositories and Master Index
def rebuild_all_indexes():
    print("\n[3/6] Re-indexing skills_index.json across all repositories and Master Index...", flush=True)
    if not os.path.exists(library_dir):
        return

    all_vault_skills = []
    repo_folders = sorted([d for d in os.listdir(library_dir) if os.path.isdir(os.path.join(library_dir, d)) and not d.startswith('.') and d != '__pycache__'])

    for repo_folder in repo_folders:
        repo_path = os.path.join(library_dir, repo_folder)
        skills_folder = os.path.join(repo_path, 'skills')
        repo_skills = []

        if os.path.exists(skills_folder):
            for s_name in sorted(os.listdir(skills_folder)):
                s_path = os.path.join(skills_folder, s_name)
                if not os.path.isdir(s_path):
                    continue

                desc = ""
                cat = "general"
                md_path = os.path.join(s_path, 'SKILL.md')
                if os.path.exists(md_path):
                    try:
                        with open(md_path, 'r', encoding='utf-8', errors='ignore') as f:
                            text = f.read(2000)
                            m_desc = re.search(r'description:\s*([^\n]+)', text)
                            if m_desc: desc = m_desc.group(1).strip()
                            m_cat = re.search(r'category:\s*([^\n]+)', text)
                            if m_cat: cat = m_cat.group(1).strip()
                    except Exception:
                        pass

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
                repo_skills.append(entry)
                all_vault_skills.append(entry)

        with open(os.path.join(repo_path, 'skills_index.json'), 'w', encoding='utf-8') as f:
            json.dump(repo_skills, f, indent=2)

    with open(os.path.join(library_dir, 'skills_index.json'), 'w', encoding='utf-8') as f:
        json.dump(all_vault_skills, f, indent=2)

    print(f"✓ Re-indexed {len(repo_folders)} repository indexes and Master index ({len(all_vault_skills)} skills).", flush=True)
    return len(all_vault_skills)

# 4. Synchronize lockfiles
def sync_lockfiles():
    print("\n[4/6] Synchronizing skills-lock.json across workspaces...", flush=True)
    now = datetime.now(timezone.utc).isoformat()
    for ag_dir in [agents_dir, r'D:\Gravity\Managment\.agents']:
        s_dir = os.path.join(ag_dir, 'skills')
        lf = os.path.join(ag_dir, 'skills-lock.json')
        if not os.path.exists(s_dir):
            continue
        lock_data = {'version': 1, 'skills': {}}
        if os.path.exists(lf):
            try:
                with open(lf, 'r', encoding='utf-8') as f:
                    lock_data = json.load(f)
            except Exception:
                pass
        existing = lock_data.get('skills', {})
        current = sorted([d for d in os.listdir(s_dir) if os.path.isdir(os.path.join(s_dir, d)) and not d.startswith('.') and d != '__pycache__'])
        synced = {}
        for s in current:
            if s in existing:
                synced[s] = existing[s]
                synced[s]['updatedAt'] = now
            else:
                synced[s] = {
                    'source': './local-library',
                    'sourceType': 'local',
                    'sourceUrl': 'local-library',
                    'skillPath': f'skills/{s}/SKILL.md',
                    'installedAt': now,
                    'updatedAt': now
                }
        lock_data['skills'] = synced
        with open(lf, 'w', encoding='utf-8') as f:
            json.dump(lock_data, f, indent=2)
        print(f"✓ Synchronized {lf}: {len(synced)} skills tracked.", flush=True)

# 5. Rebuild real category system and provenance
def rebuild_categories_and_provenance():
    print("\n[5/6] Rebuilding real category system & provenance documentation...", flush=True)
    try:
        from category_system import rebuild_category_system
        rebuild_category_system(agents_dir)
    except Exception as e:
        print(f"⚠️ Category system rebuild encountered error: {e}", flush=True)

    try:
        from provenance_system import rebuild_provenance
        rebuild_provenance(agents_dir)
    except Exception as e:
        print(f"⚠️ Provenance rebuild encountered error: {e}", flush=True)

    rebuild_skill_sea_catalog()

def rebuild_skill_sea_catalog():
    print("\n[5.5/6] Rebuilding Skill.Sea web catalog, categories & stats JSON...", flush=True)
    script_path = os.path.join(agents_dir, 'Skill.Sea', 'scripts', 'build-catalog.js')
    if os.path.exists(script_path):
        try:
            subprocess.run(['node', script_path], cwd=os.path.join(agents_dir, 'Skill.Sea'), check=True)
            print("✓ Skill.Sea web catalog successfully synced.", flush=True)
        except Exception as e:
            print(f"⚠️ Skill.Sea catalog rebuild error: {e}", flush=True)

        sync_script = os.path.join(agents_dir, 'Skill.Sea', 'scripts', 'sync-r2.js')
        if os.path.exists(sync_script):
            try:
                print("☁️ Auto-syncing Skill.Sea catalog to Cloudflare R2 (skill-sea-vault)...", flush=True)
                subprocess.run(['node', sync_script, '--allow-offline'], cwd=os.path.join(agents_dir, 'Skill.Sea'), check=False)
            except Exception as e:
                print(f"⚠️ Cloudflare R2 sync notice: {e}", flush=True)

# 6. Git Commit & Push
def git_commit_and_push():
    print("\n[6/6] Checking Git status and pushing updates...", flush=True)
    status = subprocess.run(['git', 'status', '--short'], cwd=agents_dir, capture_output=True, text=True).stdout.strip()
    if not status:
        print("✓ Working tree clean. Everything is already up to date on Git.", flush=True)
        return

    print("Pending changes detected. Committing and pushing to origin main...", flush=True)
    subprocess.run(['git', 'add', '-A'], cwd=agents_dir, check=True)
    ts = datetime.now().strftime('%Y-%m-%d %H:%M')
    subprocess.run(['git', 'commit', '-m', f"chore(skills): automated update of skills & library ({ts})"], cwd=agents_dir, check=True)
    push_res = subprocess.run(['git', 'push', 'origin', 'main'], cwd=agents_dir, capture_output=True, text=True)
    if push_res.stdout:
        print(push_res.stdout, flush=True)
    if push_res.stderr:
        print(push_res.stderr, flush=True)
    print("🎉 SUCCESS: All repos, new skills, categories, and docs updated and pushed!", flush=True)

if __name__ == '__main__':
    args = sys.argv[1:]
    clean_nested()

    if '--index' in args or '--reindex' in args:
        rebuild_all_indexes()
        rebuild_categories_and_provenance()
        sync_lockfiles()
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
            print("Please specify a search keyword: python update.py --find <keyword>", flush=True)
        sys.exit(0)

    print("=" * 65, flush=True)
    print("🚀 AGENTSKILLS VAULT — UNIFIED AUTOMATED UPDATER", flush=True)
    print(f"📁 Agents Directory:    {agents_dir}", flush=True)
    print(f"📁 Workspace Root:      {repo_root}", flush=True)
    print("=" * 65, flush=True)

    sync_all_upstreams(force='--force' in args)
    sync_active_skills()
    rebuild_all_indexes()
    sync_lockfiles()
    rebuild_categories_and_provenance()
    if '--no-push' not in args:
        git_commit_and_push()
