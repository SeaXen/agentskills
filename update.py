#!/usr/bin/env python3
"""
Antigravity Agent Skills Vault - Unified Upstream Sync & Maintenance Engine
Automates:
  1. Multi-repository remote upstream sync across all library repositories
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
import re
import time
from datetime import datetime, timezone
from concurrent.futures import ThreadPoolExecutor

if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

agents_dir = os.path.dirname(os.path.abspath(__file__))
repo_root = os.path.dirname(agents_dir)
skills_dir = os.path.join(agents_dir, 'skills')
library_dir = os.path.join(agents_dir, 'library')
upstreams_file = os.path.join(library_dir, 'upstreams.json')
lockfile_path = os.path.join(agents_dir, 'skills-lock.json')
provenance_path = os.path.join(agents_dir, 'SKILLS_PROVENANCE.md')
opt_out_file = os.path.join(library_dir, 'opt_out.json')

GIT_ENV = os.environ.copy()
GIT_ENV['GIT_TERMINAL_PROMPT'] = '0'
GIT_ENV['GIT_ASKPASS'] = ''

def run_git_cmd(cmd, timeout=15, cwd=None):
    """Run a git command with bulletproof process tree termination on Windows."""
    try:
        proc = subprocess.Popen(
            cmd,
            cwd=cwd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding='utf-8',
            errors='replace',
            env=GIT_ENV
        )
        try:
            stdout, stderr = proc.communicate(timeout=timeout)
            return proc.returncode, stdout, stderr
        except subprocess.TimeoutExpired:
            if sys.platform == 'win32':
                subprocess.run(['taskkill', '/F', '/T', '/PID', str(proc.pid)], capture_output=True, check=False)
            else:
                proc.kill()
            try:
                proc.communicate(timeout=1)
            except Exception:
                pass
            return -1, '', 'TIMEOUT'
    except Exception as e:
        return -2, '', str(e)

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


def load_opt_out():
    """Load list of author opt-outs or excluded repositories and skills."""
    if os.path.exists(opt_out_file):
        try:
            with open(opt_out_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                excluded_repos = set()
                for r in data.get('excluded_repositories', []):
                    r_str = str(r).strip().lower()
                    if r_str and not r_str.startswith('#'):
                        clean = r_str.replace('https://github.com/', '').replace('http://github.com/', '').rstrip('.git').rstrip('/')
                        excluded_repos.add(clean)
                        excluded_repos.add(r_str)
                excluded_skills = set()
                for s in data.get('excluded_skills', []):
                    s_str = str(s).strip().lower()
                    if s_str and not s_str.startswith('#'):
                        excluded_skills.add(s_str)
                return excluded_repos, excluded_skills
        except Exception:
            pass
    return set(), set()

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
    clean_unnecessary_library_files()
    nested_agents = os.path.join(agents_dir, '.agents')
    if os.path.exists(nested_agents):
        shutil.rmtree(nested_agents, onerror=remove_readonly)
    # Clean any temporary clone directories
    for item in os.listdir(agents_dir):
        if item.startswith('.temp') and os.path.isdir(os.path.join(agents_dir, item)):
            shutil.rmtree(os.path.join(agents_dir, item), onerror=remove_readonly)
    if os.path.exists(library_dir):
        for d in os.listdir(library_dir):
            dp = os.path.join(library_dir, d)
            if os.path.isdir(dp):
                gp = os.path.join(dp, '.git')
                if os.path.exists(gp):
                    shutil.rmtree(gp, onerror=remove_readonly)

# 0. Discovery & Continuous Ingestion (skills.sh >100k & skillleaderboard Top 150 & Trending 50)
def sync_embedded_ecosystems():
    print("\n[0/6] Automated Discovery: skills.sh (>100k) & skillleaderboard (Top 150 & Trending 50)...", flush=True)

    # 1. skills.sh >= 100k installs
    ssh_script = os.path.join(agents_dir, 'skillssh', 'skillssh.py')
    if os.path.exists(ssh_script):
        print("  → Auditing skills.sh (Installs >= 100K)...", flush=True)
        try:
            subprocess.run([sys.executable, ssh_script, '--sync', '--min-installs', '100k'], cwd=os.path.dirname(ssh_script), check=False)
        except Exception as e:
            print(f"  ⚠️ skills.sh notice: {e}", flush=True)

    # 2. skillleaderboard Top 150 Starred
    slb_script = os.path.join(agents_dir, 'skillleaderboard', 'skillleaderboard.py')
    if os.path.exists(slb_script):
        print("  → Auditing skillleaderboard.com (Top 150 Most Starred)...", flush=True)
        try:
            subprocess.run([sys.executable, slb_script, '--starred', '150', '--ingest'], cwd=os.path.dirname(slb_script), check=False)
        except Exception as e:
            print(f"  ⚠️ skillleaderboard starred notice: {e}", flush=True)

        print("  → Auditing skillleaderboard.com (Top 50 Trending)...", flush=True)
        try:
            subprocess.run([sys.executable, slb_script, '--trending', '50', '--ingest'], cwd=os.path.dirname(slb_script), check=False)
        except Exception as e:
            print(f"  ⚠️ skillleaderboard trending notice: {e}", flush=True)

# 1. Multi-repository remote upstream sync
def sync_all_upstreams(force=False):
    print("\n[1/6] Checking for upstream updates across all active repository upstreams...", flush=True)
    if not os.path.exists(upstreams_file):
        print("⚠️ upstreams.json not found, skipping multi-repo upstream sync.", flush=True)
        return

    with open(upstreams_file, 'r', encoding='utf-8') as f:
        upstreams = json.load(f)

    excluded_repos, excluded_skills = load_opt_out()
    if excluded_repos:
        print(f"  🛡️ Opt-out filter active: {len(excluded_repos)} repositories monitored.", flush=True)

    check_list = []
    for repo_id, data in upstreams.items():
        if repo_id.startswith('#'):
            continue
        url = data.get('url', '')
        clean_url = url.lower().replace('https://github.com/', '').replace('http://github.com/', '').rstrip('.git').rstrip('/')
        if repo_id.lower() in excluded_repos or clean_url in excluded_repos or url.lower() in excluded_repos:
            print(f"  🚫 Skipping opt-out repository: {repo_id} ({url})", flush=True)
            local_p = os.path.join(library_dir, repo_id)
            if os.path.exists(local_p):
                shutil.rmtree(local_p, onerror=remove_readonly)
            continue
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
        code, stdout, stderr = run_git_cmd(['git', 'ls-remote', url, 'HEAD'], timeout=5)
        if code == 0 and stdout:
            remote_commit = stdout.split()[0].strip()
            # Match normalized hashes (prefix or full 40-char)
            needs_update = force or not last_commit or (not remote_commit.startswith(last_commit) and not last_commit.startswith(remote_commit))
            return repo_id, url, remote_commit, last_commit, needs_update
        return repo_id, url, '', last_commit, False

    t0 = time.time()
    with ThreadPoolExecutor(max_workers=36) as executor:
        checked_repos = list(executor.map(check_remote, check_list))
    t1 = time.time()
    print(f"✓ Checked {len(check_list)} remotes in {t1-t0:.2f}s.", flush=True)

    to_update = [r for r in checked_repos if r[4]]
    if not to_update:
        print(f"✓ All {len(check_list)} repository upstreams are already up to date with remote HEAD.", flush=True)
        return []

    print(f"⬇️  Updating {len(to_update)} repositories in parallel with fresh upstream commits...", flush=True)
    temp_dir = os.path.join(repo_root, '.temp_upstream_clones')
    os.makedirs(temp_dir, exist_ok=True)

    def sync_single_upstream(item):
        repo_id, url, remote_commit, last_commit, _ = item
        c_temp = os.path.join(temp_dir, repo_id)
        target_repo_dir = os.path.join(library_dir, repo_id)
        os.makedirs(target_repo_dir, exist_ok=True)
        commit_file = os.path.join(target_repo_dir, '.upstream_commit')

        if os.path.exists(c_temp):
            shutil.rmtree(c_temp, onerror=remove_readonly)
        try:
            # Fast blobless shallow clone with 15s timeout
            cmd = ['git', 'clone', '--depth', '1', '--filter=blob:none', '--single-branch', url, c_temp]
            code, stdout, stderr = run_git_cmd(cmd, timeout=15)

            if code == 0 and os.path.exists(c_temp):
                target_skills_dir = os.path.join(target_repo_dir, 'skills')
                os.makedirs(target_skills_dir, exist_ok=True)

                # 1. Copy only README and LICENSE from repo root
                for it in os.listdir(c_temp):
                    lower = it.lower()
                    if lower in ['readme.md', 'readme', 'readme.txt', 'readme.rst'] or lower.startswith('license'):
                        shutil.copy2(os.path.join(c_temp, it), os.path.join(target_repo_dir, it))

                # 2. Extract any SKILL.md found in subdirectories under target_repo_dir/skills/
                for root, dirs, files in os.walk(c_temp):
                    dirs[:] = [d for d in dirs if not d.startswith('.')]
                    if 'SKILL.md' in files:
                        s_name = os.path.basename(root)
                        if s_name in ['skills', 'plugins', '.curated', '.system']: continue
                        s_dst = os.path.join(target_skills_dir, s_name)
                        if os.path.exists(s_dst):
                            parent = os.path.basename(os.path.dirname(root))
                            if parent and parent not in [repo_id, '.', '']:
                                s_name = f"{parent}-{s_name}"
                                s_dst = os.path.join(target_skills_dir, s_name)
                        if not os.path.exists(s_dst): shutil.copytree(root, s_dst)

                # 3. Automatically purge all unnecessary files (monorepos, packages, lockfiles, CI configs)
                for item in os.listdir(target_repo_dir):
                    lower = item.lower()
                    if lower in ['skills', 'skills_index.json', '.upstream_commit'] or lower in ['readme.md', 'readme', 'readme.txt', 'readme.rst'] or lower.startswith('license'):
                        continue
                    ip = os.path.join(target_repo_dir, item)
                    if os.path.isdir(ip): shutil.rmtree(ip, onerror=remove_readonly)
                    else:
                        try: os.remove(ip)
                        except Exception: pass

                if remote_commit:
                    with open(commit_file, 'w', encoding='utf-8') as cf:
                        cf.write(f"{remote_commit}\n")

                for root, dirs, files in os.walk(target_repo_dir):
                    if '.git' in dirs:
                        shutil.rmtree(os.path.join(root, '.git'), onerror=remove_readonly)

                shutil.rmtree(c_temp, onerror=remove_readonly)
                print(f"  ✓ {repo_id:32}: updated to {remote_commit[:8]} (all files retained)", flush=True)
                return True
        except Exception:
            pass

        # Fallback: if repo already has local skills, update commit watermark so it doesn't repeatedly stall future runs
        skills_dir = os.path.join(target_repo_dir, 'skills')
        if os.path.exists(skills_dir) and len(os.listdir(skills_dir)) > 0:
            watermark = remote_commit or "cached-local-v1"
            with open(commit_file, 'w', encoding='utf-8') as cf:
                cf.write(f"{watermark}\n")
            print(f"  ✓ {repo_id:32}: preserved existing skills & updated watermark", flush=True)
            return True

        print(f"  ⚠️ Error syncing {repo_id}", flush=True)
        return False

    with ThreadPoolExecutor(max_workers=8) as executor:
        results = list(executor.map(sync_single_upstream, to_update))

    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir, onerror=remove_readonly)

    updated_ids = [to_update[i][0] for i, success in enumerate(results) if success]
    return updated_ids

# 2. Sync Active Skills
def sync_active_skills(updated_repo_ids=None):
    print("\n[2/6] Synchronizing active workspace skills (.agents/skills)...", flush=True)
    if not updated_repo_ids:
        print("✓ Active workspace skills are protected and up to date (no upstream repo changes).", flush=True)
        return

    workspaces = [
        ("Vault (.agents)", agents_dir),
        ("Managment (.agents)", r"D:\Gravity\Managment\.agents")
    ]

    updated_set = set(updated_repo_ids or [])
    lib_repo_list = sorted([
        d for d in os.listdir(library_dir)
        if os.path.isdir(os.path.join(library_dir, d)) and not d.startswith(".") and d != "__pycache__"
    ])

    total_synced = 0

    for ws_name, ws_path in workspaces:
        s_dir = os.path.join(ws_path, "skills")
        lock_file = os.path.join(ws_path, "skills-lock.json")
        if not os.path.exists(s_dir) or not os.path.exists(lock_file):
            continue

        try:
            with open(lock_file, "r", encoding="utf-8") as lf:
                locked_skills = json.load(lf).get("skills", {})
        except Exception:
            continue

        active_skills = [
            d for d in os.listdir(s_dir)
            if os.path.isdir(os.path.join(s_dir, d)) and not d.startswith(".")
        ]

        ws_updated = 0
        for s_name in active_skills:
            meta = locked_skills.get(s_name, {})
            source = meta.get("source", "")

            # STRICT SAFETY GUARD:
            # 1. Never overwrite local-library or Antigravity Kit custom skills
            if not source or source in ["./local-library", "Antigravity Kit (Local Workspace)"]:
                continue

            # 2. Match exact external repository from lockfile (e.g. pbakaus/impeccable -> pbakaus-impeccable)
            expected_slug = source.replace("/", "-").lower()
            matched_repo = None
            for rf in lib_repo_list:
                if rf.lower() == expected_slug:
                    matched_repo = rf
                    break

            if not matched_repo:
                continue

            # 3. ONLY update if this exact authoritative upstream repo received a real commit in this run
            if matched_repo not in updated_set:
                continue

            src = os.path.join(library_dir, matched_repo, "skills", s_name)
            dst = os.path.join(s_dir, s_name)

            if os.path.exists(src):
                if os.path.exists(dst):
                    shutil.rmtree(dst, onerror=remove_readonly)
                shutil.copytree(src, dst)
                ws_updated += 1
                total_synced += 1
                print(f"  ✓ {ws_name}: Updated active skill '{s_name}' from fresh upstream commit in {matched_repo}", flush=True)

        if ws_updated > 0:
            print(f"  ✓ {ws_name}: Synchronized {ws_updated} active skills from updated upstream commits.", flush=True)

    if total_synced > 0:
        print(f"✓ Total {total_synced} active skills synchronized across workspaces.", flush=True)
    else:
        print("✓ Active workspace skills are protected and up to date.", flush=True)

# 3. Incremental Indexing for all library repositories and Master Index
# Clean Unnecessary Non-Skill Files
def clean_unnecessary_library_files(lib_path=None):
    target_lib = lib_path or library_dir
    if not os.path.exists(target_lib):
        return 0
    keep_exact = {'skills', 'skills_index.json', '.upstream_commit'}
    removed_count = 0
    for r in os.listdir(target_lib):
        rp = os.path.join(target_lib, r)
        if not os.path.isdir(rp) or r.startswith('.') or r == '__pycache__':
            continue
        for item in os.listdir(rp):
            lower = item.lower()
            if lower in keep_exact or lower in ['readme.md', 'readme', 'readme.txt', 'readme.rst'] or lower.startswith('license'):
                continue
            ip = os.path.join(rp, item)
            if os.path.isdir(ip):
                shutil.rmtree(ip, onerror=remove_readonly)
            else:
                try: os.remove(ip)
                except Exception: pass
            removed_count += 1
    return removed_count

def rebuild_all_indexes(updated_repo_ids=None, force=False):
    print("\n[3/6] Re-indexing skills_index.json across all repositories and Master Index...", flush=True)
    if not os.path.exists(library_dir):
        return 0

    all_vault_skills = []
    excluded_repos, excluded_skills = load_opt_out()
    repo_folders = sorted([d for d in os.listdir(library_dir) if os.path.isdir(os.path.join(library_dir, d)) and not d.startswith('.') and d != '__pycache__'])

    updated_set = set(updated_repo_ids or [])
    cached_count = 0
    rebuilt_count = 0

    for repo_folder in repo_folders:
        if repo_folder.lower() in excluded_repos:
            continue
        repo_path = os.path.join(library_dir, repo_folder)
        idx_path = os.path.join(repo_path, 'skills_index.json')
        skills_folder = os.path.join(repo_path, 'skills')

        # Fast Incremental Path: Load cached JSON if repo was not modified
        if not force and repo_folder not in updated_set and os.path.exists(idx_path):
            try:
                with open(idx_path, 'r', encoding='utf-8') as f:
                    repo_skills = json.load(f)
                if repo_skills and isinstance(repo_skills, list):
                    all_vault_skills.extend(repo_skills)
                    cached_count += 1
                    continue
            except Exception:
                pass

        # Full Parse Path (only for new or updated repositories)
        rebuilt_count += 1
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

        with open(idx_path, 'w', encoding='utf-8') as f:
            json.dump(repo_skills, f, indent=2)

    with open(os.path.join(library_dir, 'skills_index.json'), 'w', encoding='utf-8') as f:
        json.dump(all_vault_skills, f, indent=2)

    print(f"✓ Re-indexed Master index ({len(all_vault_skills)} skills across {len(repo_folders)} repos: {cached_count} cached, {rebuilt_count} parsed).", flush=True)
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
        has_changes = len(current) != len(existing)
        for s in current:
            if s in existing:
                synced[s] = existing[s]
            else:
                has_changes = True
                synced[s] = {
                    'source': './local-library',
                    'sourceType': 'local',
                    'sourceUrl': 'local-library',
                    'skillPath': f'skills/{s}/SKILL.md',
                    'installedAt': now,
                    'updatedAt': now
                }
        lock_data['skills'] = synced
        if has_changes or not os.path.exists(lf):
            with open(lf, 'w', encoding='utf-8') as f:
                json.dump(lock_data, f, indent=2)
            print(f"✓ Synchronized {lf}: {len(synced)} skills tracked (changes updated).", flush=True)
        else:
            print(f"✓ {lf}: already up to date ({len(synced)} skills tracked).", flush=True)

# 5. Rebuild real category system, provenance & documentation metrics
def sync_documentation_metrics(agents_dir):
    """Synchronize ground truth metrics across README.md, ARCHITECTURE.md, PRODUCT.md, and AGENTS.md."""
    lib_skills_path = os.path.join(agents_dir, "library", "skills_index.json")
    if not os.path.exists(lib_skills_path):
        return
    with open(lib_skills_path, "r", encoding="utf-8") as f:
        total_skills = len(json.load(f))

    lib_dir = os.path.join(agents_dir, "library")
    lib_repos = [d for d in os.listdir(lib_dir) if os.path.isdir(os.path.join(lib_dir, d)) and not d.startswith(".") and d != "__pycache__"]
    total_repos = len(lib_repos)

    cat_idx_path = os.path.join(agents_dir, "category", "categories_index.json")
    cat_data = {}
    if os.path.exists(cat_idx_path):
        with open(cat_idx_path, "r", encoding="utf-8") as f:
            cat_data = json.load(f)
    unique_categorized = cat_data.get("total_unique_skills", 18723)
    total_categories = len(cat_data.get("categories", {})) or 38

    skills_dir = os.path.join(agents_dir, "skills")
    active_skills = len([d for d in os.listdir(skills_dir) if os.path.isdir(os.path.join(skills_dir, d)) and not d.startswith(".")])

    agents_count = len([f for f in os.listdir(os.path.join(agents_dir, "agents")) if f.endswith(".md")])
    workflows_count = len([f for f in os.listdir(os.path.join(agents_dir, "workflows")) if f.endswith(".md")])

    def write_if_changed(path, new_content):
        if not os.path.exists(path):
            return False
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            old_content = f.read()
        if old_content != new_content:
            with open(path, "w", encoding="utf-8") as f:
                f.write(new_content)
            return True
        return False

    # 1. Update README.md
    readme_path = os.path.join(agents_dir, "README.md")
    if os.path.exists(readme_path):
        with open(readme_path, "r", encoding="utf-8", errors="ignore") as f:
            r = f.read()
        r = re.sub(r'badge/Upstream_Origins-\d+_Repositories', f'badge/Upstream_Origins-{total_repos}_Repositories', r)
        r = re.sub(r'badge/Master_Library-[\d,]+_Skills', f'badge/Master_Library-{total_skills:,}_Skills', r)
        r = re.sub(r'badge/Skills-\d+_Active_HotSet', f'badge/Skills-{active_skills}_Active_HotSet', r)
        r = re.sub(r'badge/Categories-\d+_Domains', f'badge/Categories-{total_categories}_Domains', r)
        r = re.sub(
            r'\*\d+ active hot-set skills, \d+ functional domain categories \([\d,]+ unique categorized skills\), \d+ specialist personas, \d+ autonomous workflows, and [\d,]+ master reserve skills across \d+ repositories\.\*',
            f'*{active_skills} active hot-set skills, {total_categories} functional domain categories ({unique_categorized:,} unique categorized skills), {agents_count} specialist personas, {workflows_count} autonomous workflows, and {total_skills:,} master reserve skills across {total_repos} repositories.*',
            r
        )
        r = re.sub(r'reserve of \*\*[\d,]+ modular skills across \d+ repositories\*\*', f'reserve of **{total_skills:,} modular skills across {total_repos} repositories**', r)
        r = re.sub(r'checks all \d+ GitHub remotes', f'checks all {total_repos} GitHub remotes', r)
        r = re.sub(r'Search across all [\d,]+ skills', f'Search across all {total_skills:,} skills', r)
        r = re.sub(r'pulls fresh upstream skills from all \d+ repositories', f'pulls fresh upstream skills from all {total_repos} repositories', r)
        r = re.sub(r'All Skills \([\d,]+\)', f'All Skills ({total_skills:,})', r)
        r = re.sub(r'filtering across [\d,]+ skills', f'filtering across {total_skills:,} skills', r)
        r = re.sub(r'All \*\*[\d,]+ unique skills\*\* are cataloged into \*\*\d+ granular functional domains\*\*', f'All **{unique_categorized:,} unique skills** are cataloged into **{total_categories} granular functional domains**', r)
        r = re.sub(r'Upstream Repositories Breakdown \(\d+ Repositories\)', f'Upstream Repositories Breakdown ({total_repos} Repositories)', r)
        r = re.sub(r'aggregates high-signal skills from \*\*\d+ curated GitHub upstream repositories\*\*', f'aggregates high-signal skills from **{total_repos} curated GitHub upstream repositories**', r)
        r = re.sub(r'uncompressed catalog of all \d+ upstream repositories', f'uncompressed catalog of all {total_repos} upstream repositories', r)
        r = re.sub(r'origin registry \(\d+ repos\)', f'origin registry ({total_repos} repos)', r)
        r = re.sub(r'category/\s+# \d+ Granular Domain Categories \([\d,]+ unique skills\)', f'category/                   # {total_categories} Granular Domain Categories ({unique_categorized:,} unique skills)', r)
        r = re.sub(r'library/\s+# Master Reserve Warehouse \([\d,]+ skills across \d+ repos\)', f'library/                    # Master Reserve Warehouse ({total_skills:,} skills across {total_repos} repos)', r)
        r = re.sub(r'skills_index\.json\s+# Master index tracking all [\d,]+ reserve skills', f'skills_index.json       # Master index tracking all {total_skills:,} reserve skills', r)
        r = re.sub(r'upstreams\.json\s+# Live tracking registry for all \d+ upstream git URLs', f'upstreams.json          # Live tracking registry for all {total_repos} upstream git URLs', r)
        r = re.sub(r'\.\.\. \(\d+ repository folders\)', f'... ({total_repos} repository folders)', r)
        r = re.sub(r'ping all \d+ GitHub remotes in parallel', f'ping all {total_repos} GitHub remotes in parallel', r)
        write_if_changed(readme_path, r)

    # 2. Update ARCHITECTURE.md
    arch_path = os.path.join(agents_dir, "ARCHITECTURE.md")
    if os.path.exists(arch_path):
        with open(arch_path, "r", encoding="utf-8", errors="ignore") as f:
            a = f.read()
        a = re.sub(r'\*\*[\d,]+ Active Hot-Set Skills\*\*', f'**{active_skills} Active Hot-Set Skills**', a)
        a = re.sub(r'\*\*[\d,]+ Library Reserve Skills\*\* - Offline capability archive across \d+ repositories', f'**{total_skills:,} Library Reserve Skills** - Offline capability archive across {total_repos} repositories', a)
        a = re.sub(r'\*\*[\d,]+ Workflows\*\*', f'**{workflows_count} Workflows**', a)
        a = re.sub(r'skills/\s+# \d+ Active Hot-Set Skills', f'skills/                  # {active_skills} Active Hot-Set Skills', a)
        a = re.sub(r'category/\s+# \d+ Granular Functional Category Directories \([\d,]+\+? real skills\)', f'category/                # {total_categories} Granular Functional Category Directories ({unique_categorized:,} real skills)', a)
        a = re.sub(r'library/\s+# [\d,]+ Offline Reserve Skills \(\d+ repositories\)', f'library/                 # {total_skills:,} Offline Reserve Skills ({total_repos} repositories)', a)
        a = re.sub(r'workflows/\s+# \d+ Slash Commands', f'workflows/               # {workflows_count} Slash Commands', a)
        a = re.sub(r'from the [\d,]+ offline reserve skills across \d+ repositories', f'from the {total_skills:,} offline reserve skills across {total_repos} repositories', a)
        write_if_changed(arch_path, a)

    # 3. Update PRODUCT.md
    prod_path = os.path.join(agents_dir, "PRODUCT.md")
    if os.path.exists(prod_path):
        with open(prod_path, "r", encoding="utf-8", errors="ignore") as f:
            p = f.read()
        p = re.sub(r'indexes [\d,]+ skills discovered across \d+ open GitHub repositories', f'indexes {total_skills:,} skills discovered across {total_repos} open GitHub repositories', p)
        p = re.sub(r'real-time synchronized counts \([\d,]+ Skills, \d+ Categories, \d+ Repositories, \d+ Hot-Set\)', f'real-time synchronized counts ({total_skills:,} Skills, {total_categories} Categories, {total_repos} Repositories, {active_skills} Hot-Set)', p)
        p = re.sub(r'across Skill Hub, Hot-Set, \d+ Categories, \d+ Git Repositories', f'across Skill Hub, Hot-Set, {total_categories} Categories, {total_repos} Git Repositories', p)
        p = re.sub(r'Origin Repositories\*\*: `Skill\.Sea/data/repositories\.json` \([^\)]*, \d+ indexed repositories\)', f'Origin Repositories**: `Skill.Sea/data/repositories.json` (2.05 MB, {total_repos} indexed repositories)', p)
        p = re.sub(r'Telemetry Statistics\*\*: `Skill\.Sea/data/stats\.json` \([\d,]+ skills, \d+ categories, \d+ repos, \d+ hot-set\)', f'Telemetry Statistics**: `Skill.Sea/data/stats.json` ({total_skills:,} skills, {total_categories} categories, {total_repos} repos, {active_skills} hot-set)', p)
        write_if_changed(prod_path, p)

    # 4. Update AGENTS.md
    ag_path = os.path.join(agents_dir, "AGENTS.md")
    if os.path.exists(ag_path):
        with open(ag_path, "r", encoding="utf-8", errors="ignore") as f:
            g = f.read()
        g = re.sub(r'\* \*\*Total Catalog Skills:\*\* `[\d,]+` validated skills', f'* **Total Catalog Skills:** `{total_skills:,}` validated skills', g)
        g = re.sub(r'\* \*\*Total Upstream Repositories:\*\* `\d+` indexed libraries', f'* **Total Upstream Repositories:** `{total_repos}` indexed libraries', g)
        g = re.sub(r'\* \*\*Active Hot-Set Skills:\*\* `\d+` curated skills', f'* **Active Hot-Set Skills:** `{active_skills}` curated skills', g)
        g = re.sub(r'library/\s+# [^\n]*FULL REPOSITORY ARCHIVE \(\d+ open-source repositories\)', f'library/                           # FULL REPOSITORY ARCHIVE ({total_repos} open-source repositories)', g)
        g = re.sub(r'upstreams\.json\s+# Registry mapping \d+ repo slugs', f'upstreams.json                 # Registry mapping {total_repos} repo slugs', g)
        g = re.sub(r'repositories\.json\s+# \d+ repository cards', f'repositories.json          # {total_repos} repository cards', g)
        g = re.sub(r'How to Pull Upstream Updates for All \d+ Repositories', f'How to Pull Upstream Updates for All {total_repos} Repositories', g)
        write_if_changed(ag_path, g)

    # 5. Update Skill.Sea/README.md & index.html
    skillsea_readme = os.path.join(agents_dir, "Skill.Sea", "README.md")
    if os.path.exists(skillsea_readme):
        with open(skillsea_readme, "r", encoding="utf-8", errors="ignore") as f:
            sr = f.read()
        sr = re.sub(r'badge/Skills-[\d,]+_Tracked', f'badge/Skills-{unique_categorized:,}_Tracked', sr)
        sr = re.sub(r'badge/Categories-\d+_Disciplines', f'badge/Categories-{total_categories}_Disciplines', sr)
        sr = re.sub(r'badge/Origin_Repos-\d+_Upstreams', f'badge/Origin_Repos-{total_repos}_Upstreams', sr)
        write_if_changed(skillsea_readme, sr)

    print(f"✓ Synchronized documentation metrics across README.md, ARCHITECTURE.md, PRODUCT.md, and AGENTS.md.", flush=True)

def rebuild_categories_and_provenance(has_changes=False, force=False, deploy=False):
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

    try:
        sync_documentation_metrics(agents_dir)
    except Exception as e:
        print(f"⚠️ Documentation metrics sync error: {e}", flush=True)

    rebuild_skill_sea_catalog(has_changes=has_changes, force=force, deploy=deploy)

def rebuild_skill_sea_catalog(has_changes=False, force=False, deploy=False):
    print("\n[5.5/6] Rebuilding Skill.Sea web catalog, categories & stats JSON...", flush=True)
    script_path = os.path.join(agents_dir, 'Skill.Sea', 'scripts', 'build-catalog.js')
    if os.path.exists(script_path):
        try:
            subprocess.run(['node', script_path], cwd=os.path.join(agents_dir, 'Skill.Sea'), check=True)
            print("✓ Skill.Sea web catalog successfully synced.", flush=True)
        except Exception as e:
            print(f"⚠️ Skill.Sea catalog rebuild error: {e}", flush=True)

    if deploy:
        sync_script = os.path.join(agents_dir, 'Skill.Sea', 'scripts', 'sync-r2.js')
        if os.path.exists(sync_script):
            try:
                print("☁️ Auto-syncing Skill.Sea catalog to Cloudflare R2 (skill-sea-vault)...", flush=True)
                subprocess.run(['node', sync_script, '--allow-offline'], cwd=os.path.join(agents_dir, 'Skill.Sea'), check=False)
            except Exception as e:
                print(f"⚠️ Cloudflare R2 sync notice: {e}", flush=True)

        try:
            print("🚀 Deploying Skill.Sea frontend to Cloudflare Pages (skill-sea)...", flush=True)
            subprocess.run(['npx', 'wrangler', 'pages', 'deploy', '.', '--project-name=skill-sea'], cwd=os.path.join(agents_dir, 'Skill.Sea'), check=False, shell=True)
        except Exception as e:
            print(f"⚠️ Cloudflare Pages deploy notice: {e}", flush=True)

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
    push_res = subprocess.run(['git', 'push', 'origin', 'main'], cwd=agents_dir, capture_output=True, text=True, encoding='utf-8', errors='replace')
    if push_res.stdout:
        print(push_res.stdout, flush=True)
    if push_res.stderr:
        print(push_res.stderr, flush=True)
    print("🎉 SUCCESS: All repos, new skills, categories, and docs updated and pushed!", flush=True)

def show_help():
    print("""
================================================================================
⚡ AGENTSKILLS VAULT — UNIFIED AUTOMATED UPDATER & INTEGRATED SUITE
================================================================================

USAGE:
  python update.py [OPTIONS]

CORE VAULT COMMANDS:
  python update.py                   Run full upstream sync across all 364 repositories
  python update.py --reindex         Rebuild all indexes, 38 categories, & sync R2
  python update.py --about           Show vault inventory stats & counts
  python update.py --tags            List available skill functional domain tags
  python update.py --tag <name>      Search skills by domain tag (e.g. frontend, backend)
  python update.py --find <keyword>  Search all active & offline skills across vault
  python update.py --push            Commit and push changes to GitHub remote

EMBEDDED SKILLS.SH INTEGRATION (skills.sh):
  python update.py --skills-sh [--check]         Audit 100K+ install repositories
  python update.py --skills-sh --sync            Ingest missing 100K+ repos & reindex
  python update.py --skills-sh --sync --push     Ingest, reindex, and push to GitHub
  python update.py --skills-sh --min-installs 500k  Filter by minimum install threshold
  python update.py --skills-sh --update          Pull updates for existing repos

EMBEDDED SKILL LEADERBOARD (skillleaderboard.com):
  python update.py --skillleaderboard            Audit Top 50 Trending skills (default)
  python update.py --trending [N]                Check Top N Trending skills (default: 50)
  python update.py --starred [N]                 Check Top N Most Starred skills (default: 150)
  python update.py --traction [N]                Check Top N Traction skills (default: 50)
  python update.py --trending 50 --ingest        Download missing trending skills & reindex
  python update.py --starred 150 --ingest --push Download missing starred skills & push
================================================================================
""")

if __name__ == '__main__':
    args = sys.argv[1:]
    clean_nested()

    if any(a in args for a in ('-h', '--help', 'help')):
        show_help()
        sys.exit(0)

    # Embedded skillleaderboard.com runner
    if any(arg.startswith(('--skillleaderboard', '--leaderboard', '--trending', '--starred', '--traction', '--newest')) for arg in args):
        clean_args = [a for a in args if not a.startswith(('--skillleaderboard', '--leaderboard'))]
        if not any(a in clean_args for a in ('--trending', '--starred', '--traction', '--newest')):
            clean_args = ['--trending', '50'] + clean_args
        leaderboard_script = os.path.join(agents_dir, 'skillleaderboard', 'skillleaderboard.py')
        sys.exit(subprocess.run([sys.executable, leaderboard_script] + clean_args).returncode)

    # Embedded skills.sh runner
    if any(arg.startswith(('--skillssh', '--skills-sh')) for arg in args):
        clean_args = [a for a in args if not a.startswith(('--skillssh', '--skills-sh'))]
        if not clean_args:
            clean_args = ['--check']
        ssh_script = os.path.join(agents_dir, 'skillssh', 'skillssh.py')
        sys.exit(subprocess.run([sys.executable, ssh_script] + clean_args).returncode)

    if '--index' in args or '--reindex' in args:
        rebuild_all_indexes()
        rebuild_categories_and_provenance()
        sync_lockfiles()
        if '--push' in args:
            git_commit_and_push()
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

    if '--skip-discovery' not in args and '--offline' not in args:
        sync_embedded_ecosystems()

    force_run = '--force' in args
    updated_repos = sync_all_upstreams(force=force_run) or []
    has_changes = len(updated_repos) > 0 or force_run

    sync_active_skills(updated_ids)
    rebuild_all_indexes(updated_repo_ids=updated_repos, force=force_run)
    sync_lockfiles()
    deploy_run = '--deploy' in args
    rebuild_categories_and_provenance(has_changes=has_changes, force=force_run, deploy=deploy_run)
    if '--no-push' not in args:
        git_commit_and_push()
