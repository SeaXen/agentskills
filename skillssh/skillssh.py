#!/usr/bin/env python3
"""
skills.sh Vault Tracker & Synchronizer
Website: https://www.skills.sh/

Enables humans and AI agents to track, audit, and ingest:
  - Repositories with >= 100K installs (--min-installs 100k, default)
  - Custom install ranges (e.g. --min-installs 500k, --min-installs 1m)
  - Full audit of vault status (--check)
  - Markdown report generation (--markdown [FILE])
  - Automated downloading and vault ingestion (--sync / --ingest)
  - Automated taxonomy re-indexing across all 38 categories
  - Automatic git commit & push (--push)

Usage Examples:
  python skillssh.py --check
  python skillssh.py --check --min-installs 500k
  python skillssh.py --markdown
  python skillssh.py --sync
  python skillssh.py --sync --push
  python skillssh.py --sync --repo vercel-labs/skills
  python skillssh.py --check --json
"""

import os
import sys
import json
import urllib.request
import argparse
import subprocess
import shutil
import stat
import re
import io
import zipfile
import threading
from datetime import datetime, timezone
from concurrent.futures import ThreadPoolExecutor, as_completed

if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

def resolve_agents_dir():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    parent = os.path.dirname(script_dir)
    if os.path.exists(os.path.join(parent, 'library')):
        return parent
    if os.path.exists(os.path.join(script_dir, 'library')):
        return script_dir
    default_vault = "D:/Repo/.agents"
    if os.path.exists(os.path.join(default_vault, 'library')):
        return default_vault
    for ws_cand in ["D:/Gravity/Managment/.agents", os.path.expanduser("~/.agents")]:
        if os.path.exists(os.path.join(ws_cand, 'library')):
            return ws_cand
    return default_vault

agents_dir = resolve_agents_dir()
lib_dir = os.path.join(agents_dir, 'library')
upstreams_file = os.path.join(lib_dir, 'upstreams.json')
update_py = os.path.join(agents_dir, 'update.py')
script_dir = os.path.dirname(os.path.abspath(__file__))
cache_file = os.path.join(script_dir, '.cache_skills_sh.json')
temp_clone_dir = os.path.join(agents_dir, '.temp_skillssh_clones')

GIT_ENV = os.environ.copy()
GIT_ENV['GIT_LFS_SKIP_SMUDGE'] = '1'
GIT_ENV['GIT_TERMINAL_PROMPT'] = '0'
GIT_ENV['GIT_ASKPASS'] = ''

def remove_readonly(func, path, exc_info):
    try:
        os.chmod(path, stat.S_IWRITE)
        func(path)
    except Exception:
        pass

def parse_install_str(s):
    if not s:
        return 0
    s = s.strip().upper().replace(',', '')
    try:
        if s.endswith('M'):
            return int(float(s[:-1]) * 1_000_000)
        elif s.endswith('K'):
            return int(float(s[:-1]) * 1_000)
        return int(float(s))
    except Exception:
        return 0

def format_installs(num):
    if num >= 1_000_000:
        return f"{num / 1_000_000:.2f}M"
    elif num >= 1_000:
        return f"{num / 1_000:.1f}K"
    return str(num)

def parse_threshold_arg(val):
    if not val:
        return 100_000
    return parse_install_str(str(val))

def load_local_knowledge():
    upstreams = {}
    if os.path.exists(upstreams_file):
        try:
            with open(upstreams_file, 'r', encoding='utf-8') as f:
                upstreams = json.load(f)
        except Exception:
            pass

    existing_folders = set()
    if os.path.exists(lib_dir):
        for d in os.listdir(lib_dir):
            if os.path.isdir(os.path.join(lib_dir, d)):
                existing_folders.add(d.lower())

    known_upstreams = set()
    for k, v in upstreams.items():
        if isinstance(v, dict):
            if 'upstream' in v:
                known_upstreams.add(v['upstream'].lower())
            if 'url' in v:
                m = re.search(r'github\.com/([^/]+/[^/]+)', v['url'], re.IGNORECASE)
                if m:
                    known_upstreams.add(m.group(1).lower().rstrip('.git'))

    return existing_folders, known_upstreams, upstreams

def fetch_skills_sh_dataset(refresh=False):
    if not refresh and os.path.exists(cache_file):
        try:
            with open(cache_file, 'r', encoding='utf-8') as f:
                cached = json.load(f)
                cached_time = cached.get('timestamp', 0)
                if (datetime.now(timezone.utc).timestamp() - cached_time) < 86400:
                    return cached.get('repositories', [])
        except Exception:
            pass

    print("🌐 Fetching skills.sh sitemap and live data...", flush=True)
    sitemap_urls = [
        "https://www.skills.sh/sitemaps/sitemap-skills-1.xml",
        "https://www.skills.sh/sitemap.xml"
    ]
    
    headers = {'User-Agent': 'AntigravityAgent/2.0 (skills.sh sync tool)'}
    repo_urls = set()
    for sm in sitemap_urls:
        try:
            req = urllib.request.Request(sm, headers=headers)
            with urllib.request.urlopen(req, timeout=15) as resp:
                xml_content = resp.read().decode('utf-8', errors='ignore')
                locs = re.findall(r'<loc>(https://www\.skills\.sh/([^/<]+)/([^/<]+))</loc>', xml_content)
                for full_url, owner, name in locs:
                    if owner in ('sitemaps', 'api', '_next', 'static', 'categories'):
                        continue
                    repo_slug = f"{owner}/{name}"
                    repo_urls.add((repo_slug, full_url))
        except Exception as e:
            print(f"⚠️ Notice fetching {sm}: {e}", file=sys.stderr)

    print(f"Discovered {len(repo_urls)} repository candidates. Inspecting install stats...", flush=True)

    def inspect_repo(item):
        repo_slug, url = item
        req = urllib.request.Request(url, headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=12) as resp:
                html = resp.read().decode('utf-8', errors='ignore')
                installs_str = None
                inst_m = re.search(r'([0-9]+(?:\.[0-9]+)?[KMkm])\s*(?:installs|active installs)', html, re.IGNORECASE)
                if not inst_m:
                    inst_m = re.search(r'([0-9]+(?:\.[0-9]+)?(?:[KMkm]))', html)
                if inst_m:
                    installs_str = inst_m.group(1).upper()
                    
                installs_val = parse_install_str(installs_str)
                skills_count = 1
                sk_m = re.search(r'([0-9]+)\s+agent skills from', html, re.IGNORECASE)
                if sk_m:
                    skills_count = int(sk_m.group(1))
                else:
                    sk_list = re.findall(r'href=["\']/' + re.escape(repo_slug) + r'/([a-zA-Z0-9_-]+)["\']', html)
                    if sk_list:
                        skills_count = len(set(sk_list))
                        
                desc_m = re.search(r'<meta name="description" content="([^"]+)"', html)
                desc = desc_m.group(1) if desc_m else f"Skills bundle from {repo_slug}"

                return {
                    'repo': repo_slug,
                    'url': url,
                    'github': f"https://github.com/{repo_slug}",
                    'installs_str': installs_str or "0",
                    'installs': installs_val,
                    'skills_count': skills_count,
                    'desc': desc
                }
        except Exception:
            return None

    results = []
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = {executor.submit(inspect_repo, item): item for item in repo_urls}
        for future in as_completed(futures):
            res = future.result()
            if res:
                results.append(res)

    results.sort(key=lambda x: x['installs'], reverse=True)

    try:
        os.makedirs(os.path.dirname(cache_file), exist_ok=True)
        with open(cache_file, 'w', encoding='utf-8') as f:
            json.dump({
                'timestamp': datetime.now(timezone.utc).timestamp(),
                'updated_at': datetime.now(timezone.utc).isoformat(),
                'repositories': results
            }, f, indent=2)
    except Exception:
        pass

    return results

def check_repositories(min_installs=100_000, max_installs=None, limit=None, refresh=False):
    all_repos = fetch_skills_sh_dataset(refresh=refresh)
    existing_folders, known_upstreams, _ = load_local_knowledge()

    filtered = []
    for r in all_repos:
        installs = r.get('installs', 0)
        if installs < min_installs:
            continue
        if max_installs is not None and installs > max_installs:
            continue
        filtered.append(r)

    if limit:
        filtered = filtered[:limit]

    in_vault = []
    missing = []

    for r in filtered:
        slug = r['repo']
        owner, name = slug.split('/')
        folder_slug = re.sub(r'[^a-zA-Z0-9_-]', '-', f"{owner}-{name}".lower()).strip('-')

        matched_folder = None
        if folder_slug in existing_folders:
            matched_folder = folder_slug
        elif slug.lower() in known_upstreams:
            matched_folder = folder_slug
        else:
            for ef in existing_folders:
                if ef == name.lower() or ef == f"{name.lower()}-skills" or ef.endswith(f"-{name.lower()}"):
                    matched_folder = ef
                    break

        if matched_folder:
            r['in_library'] = True
            r['library_folder'] = matched_folder
            in_vault.append(r)
        else:
            r['in_library'] = False
            r['library_folder'] = None
            missing.append(r)

    return in_vault, missing, filtered

def print_audit_table(in_vault, missing, total_repos, min_installs, max_installs=None):
    min_str = format_installs(min_installs)
    range_str = f">= {min_str}" if max_installs is None else f"{min_str} - {format_installs(max_installs)}"
    
    print("\n" + "=" * 80)
    print(f"📊 SKILLS.SH AUDIT REPORT (Installs: {range_str})")
    print("=" * 80)
    print(f"Total Repositories Matching Criteria : {len(total_repos)}")
    print(f"  ✅ Installed in Local Vault        : {len(in_vault)}")
    print(f"  ❌ Missing from Local Vault        : {len(missing)}")
    pct = (len(in_vault) / len(total_repos) * 100) if total_repos else 100.0
    print(f"  📈 Local Vault Coverage Ratio      : {pct:.1f}%")
    print("-" * 80)

    display_repos = total_repos[:20]
    print(f"{'#':<4} {'Repository':<35} {'Installs':<10} {'Skills':<8} {'Vault Status'}")
    print("-" * 80)
    for idx, r in enumerate(display_repos, 1):
        status = f"✅ library/{r['library_folder']}" if r.get('in_library') else "❌ Missing"
        repo_name = r['repo'][:33]
        inst_str = r.get('installs_str') or format_installs(r.get('installs', 0))
        skills_str = str(r.get('skills_count', 1))
        print(f"{idx:<4} {repo_name:<35} {inst_str:<10} {skills_str:<8} {status}")

    if len(total_repos) > 20:
        print(f"... and {len(total_repos) - 20} more repositories.")
    print("=" * 80 + "\n")

def generate_markdown_report(total_repos, in_vault, missing, min_installs, max_installs, output_path=None):
    min_str = format_installs(min_installs)
    range_str = f">= {min_str}" if max_installs is None else f"{min_str} - {format_installs(max_installs)}"
    
    if not output_path:
        output_path = os.path.join(agents_dir, "SKILLS_SH_100K_PLUS_REPOS.md")

    md = []
    md.append(f"# 🏆 Skills.sh Repositories Leaderboard ({range_str} Installs)\n")
    md.append(f"> **Audit Date**: {datetime.now(timezone.utc).strftime('%B %d, %Y')}  ")
    md.append(f"> **Source**: [skills.sh](https://www.skills.sh/)  ")
    md.append(f"> **Vault Coverage**: **{len(in_vault)} / {len(total_repos)} ({len(in_vault)/len(total_repos)*100:.1f}%)**\n")
    md.append("## 📊 Repositories Leaderboard\n")
    md.append("| Rank | Repository | Installs | Skills | Vault Status | Skills.sh | GitHub | CLI Install |")
    md.append("| :--- | :--- | :---: | :---: | :--- | :---: | :---: | :--- |")

    for idx, r in enumerate(total_repos, 1):
        rank = f"**#{idx:03d}**"
        repo = f"[`{r['repo']}`]({r['url']})"
        inst = f"**{r.get('installs_str') or format_installs(r.get('installs', 0))}**"
        sk_cnt = str(r.get('skills_count', 1))
        if r.get('in_library'):
            v_status = f"✅ [`library/{r['library_folder']}`](file:///D:/Repo/.agents/library/{r['library_folder']})"
        else:
            v_status = "❌ Missing"
        ssh_link = f"[skills.sh]({r['url']})"
        gh_link = f"[GitHub]({r['github']})"
        cmd = f"`npx skills add {r['repo']}`"
        md.append(f"| {rank} | {repo} | {inst} | {sk_cnt} | {v_status} | {ssh_link} | {gh_link} | {cmd} |")

    md_text = "\n".join(md) + "\n"
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(md_text)
    print(f"✓ Generated Markdown report: {output_path}")

def ingest_repository(r, upstreams):
    repo_slug = r['repo']
    gh_url = r['github']
    owner, repo_name = repo_slug.split('/')
    folder_slug = re.sub(r'[^a-zA-Z0-9_-]', '-', f"{owner}-{repo_name}".lower()).strip('-')
    target_dir = os.path.join(lib_dir, folder_slug)
    clone_tmp = os.path.join(temp_clone_dir, folder_slug)

    print(f"📥 Ingesting {repo_slug} into library/{folder_slug}...", flush=True)

    if os.path.exists(clone_tmp):
        shutil.rmtree(clone_tmp, onerror=remove_readonly)
    os.makedirs(clone_tmp, exist_ok=True)

    success = False
    commit_hash = "HEAD"

    # Strategy A: Git Blobless Sparse Checkout
    cmd = ['git', 'clone', '--filter=blob:none', '--no-checkout', '--depth', '1', gh_url, clone_tmp]
    try:
        res = subprocess.run(cmd, env=GIT_ENV, capture_output=True, text=True, timeout=60)
        if res.returncode == 0:
            subprocess.run(['git', 'sparse-checkout', 'init', '--cone'], cwd=clone_tmp, env=GIT_ENV, capture_output=True)
            subprocess.run(['git', 'sparse-checkout', 'set', 'skills', 'plugins', 'docs', 'README.md', 'SKILL.md'], cwd=clone_tmp, env=GIT_ENV, capture_output=True)
            chk = subprocess.run(['git', 'checkout'], cwd=clone_tmp, env=GIT_ENV, capture_output=True, text=True, timeout=60)
            if chk.returncode == 0:
                c_res = subprocess.run(['git', 'rev-parse', 'HEAD'], cwd=clone_tmp, env=GIT_ENV, capture_output=True, text=True)
                if c_res.returncode == 0:
                    commit_hash = c_res.stdout.strip()
                success = True
    except Exception:
        success = False

    # Strategy B: Zip Download Fallback
    if not success:
        print(f"  ⚡ Git clone skipped/slow for {repo_slug}. Falling back to GitHub Zip stream...", flush=True)
        zip_data = None
        for branch in ['main', 'master']:
            try:
                z_url = f"https://github.com/{owner}/{repo_name}/archive/refs/heads/{branch}.zip"
                req = urllib.request.Request(z_url, headers={'User-Agent': 'Mozilla/5.0'})
                with urllib.request.urlopen(req, timeout=30) as z_resp:
                    zip_data = z_resp.read()
                    break
            except Exception:
                continue

        if zip_data:
            try:
                with zipfile.ZipFile(io.BytesIO(zip_data)) as zf:
                    zf.extractall(clone_tmp)
                    root_folder = zf.namelist()[0].split('/')[0]
                    extracted_path = os.path.join(clone_tmp, root_folder)
                    for item in os.listdir(extracted_path):
                        shutil.move(os.path.join(extracted_path, item), os.path.join(clone_tmp, item))
                    success = True
            except Exception as e:
                print(f"  ❌ Zip extraction failed: {e}", file=sys.stderr)

    if not success:
        print(f"❌ Failed to download {repo_slug}", file=sys.stderr)
        return False

    if os.path.exists(target_dir):
        shutil.rmtree(target_dir, onerror=remove_readonly)
    os.makedirs(target_dir, exist_ok=True)
    skills_sub = os.path.join(target_dir, 'skills')
    os.makedirs(skills_sub, exist_ok=True)

    discovered = False
    src_skills = os.path.join(clone_tmp, 'skills')
    if os.path.exists(src_skills) and os.path.isdir(src_skills):
        for d in os.listdir(src_skills):
            s_src = os.path.join(src_skills, d)
            if os.path.isdir(s_src):
                s_dst = os.path.join(skills_sub, d)
                if not os.path.exists(s_dst):
                    shutil.copytree(s_src, s_dst, ignore=shutil.ignore_patterns('.git', '*.mp4', '*.mov', '*.bin'))
        discovered = True

    if not discovered or len(os.listdir(skills_sub)) == 0:
        for root, dirs, files in os.walk(clone_tmp):
            if '.git' in root or '.github' in root:
                continue
            for f in files:
                if f.lower() == 'skill.md':
                    parent = os.path.dirname(os.path.join(root, f))
                    skill_id = os.path.basename(parent)
                    if skill_id in ['skills', 'plugins', '.', os.path.basename(clone_tmp)]:
                        skill_id = re.sub(r'[^a-zA-Z0-9_-]', '-', repo_name.lower()).strip('-')
                    dest_skill = os.path.join(skills_sub, skill_id)
                    if not os.path.exists(dest_skill):
                        shutil.copytree(parent, dest_skill, ignore=shutil.ignore_patterns('.git', '*.mp4', '*.mov', '*.bin'))
                        discovered = True

    if len(os.listdir(skills_sub)) == 0:
        skill_slug = re.sub(r'[^a-zA-Z0-9_-]', '-', repo_name.lower()).strip('-')
        single_skill_dir = os.path.join(skills_sub, skill_slug)
        os.makedirs(single_skill_dir, exist_ok=True)
        dest_md = os.path.join(single_skill_dir, 'SKILL.md')

        content = None
        for cand in ['SKILL.md', 'skill.md', 'AGENTS.md', 'CLAUDE.md', 'README.md']:
            cp = os.path.join(clone_tmp, cand)
            if os.path.exists(cp) and os.path.getsize(cp) > 50:
                with open(cp, 'r', encoding='utf-8', errors='ignore') as cf:
                    content = cf.read()
                break

        tagline = r.get('desc') or f"Skills bundle for {repo_slug}"
        if content:
            if not content.strip().startswith('---'):
                full_text = f"---\nname: {skill_slug}\ndescription: {tagline}\n---\n\n" + content
            else:
                full_text = content
        else:
            full_text = f"---\nname: {skill_slug}\ndescription: {tagline}\n---\n\n# {repo_slug}\n\n{tagline}\n"

        with open(dest_md, 'w', encoding='utf-8') as sf:
            sf.write(full_text)

    readme_src = os.path.join(clone_tmp, 'README.md')
    readme_dst = os.path.join(target_dir, 'README.md')
    if os.path.exists(readme_src):
        shutil.copy2(readme_src, readme_dst)
    else:
        with open(readme_dst, 'w', encoding='utf-8') as rf:
            rf.write(f"# {repo_slug}\n\n{r.get('desc', '')}\n")

    with open(os.path.join(target_dir, '.upstream_commit'), 'w', encoding='utf-8') as cf:
        cf.write(f"{commit_hash}\n")

    for root, dirs, files in os.walk(target_dir):
        if '.git' in dirs:
            shutil.rmtree(os.path.join(root, '.git'), onerror=remove_readonly)

    shutil.rmtree(clone_tmp, onerror=remove_readonly)

    skills_count = len(os.listdir(skills_sub)) if os.path.exists(skills_sub) else 0
    print(f"✓ Ingested {repo_slug} -> library/{folder_slug} ({skills_count} skills).", flush=True)

    upstreams[folder_slug] = {
        'type': 'github-repo',
        'upstream': repo_slug,
        'url': gh_url,
        'git_url': gh_url
    }

    return True

def sync_missing(missing_repos):
    if not missing_repos:
        print("🎉 All repositories are already present in your local vault! Nothing to ingest.")
        return 0

    print(f"\n🚀 Starting sync for {len(missing_repos)} missing repositories...", flush=True)
    _, _, upstreams = load_local_knowledge()
    os.makedirs(temp_clone_dir, exist_ok=True)

    ingested_count = 0
    for idx, r in enumerate(missing_repos, 1):
        print(f"[{idx}/{len(missing_repos)}] Processing {r['repo']}...", flush=True)
        ok = ingest_repository(r, upstreams)
        if ok:
            ingested_count += 1

    try:
        with open(upstreams_file, 'w', encoding='utf-8') as f:
            json.dump(upstreams, f, indent=2)
    except Exception as e:
        print(f"Error saving upstreams.json: {e}", file=sys.stderr)

    if os.path.exists(temp_clone_dir):
        shutil.rmtree(temp_clone_dir, onerror=remove_readonly)

    print(f"\nIngested {ingested_count}/{len(missing_repos)} repositories into local library.", flush=True)

    if os.path.exists(update_py):
        print("\n🔄 Re-indexing skills and 38 categories via update.py --reindex...", flush=True)
        try:
            res = subprocess.run([sys.executable, update_py, '--reindex'], cwd=agents_dir, env=GIT_ENV, text=True)
            if res.returncode == 0:
                print("✓ Successfully rebuilt taxonomy categories and Master index.")
            else:
                print(f"⚠️ Re-indexing exited with code {res.returncode}")
        except Exception as e:
            print(f"Error running update.py: {e}", file=sys.stderr)

    return ingested_count

def git_push_vault():
    print("\n📦 Staging, committing, and pushing vault updates to GitHub...", flush=True)
    try:
        subprocess.run(['git', 'add', '-A'], cwd=agents_dir, env=GIT_ENV, check=True)
        msg = f"feat(skills.sh): sync 100K+ repositories ({datetime.now(timezone.utc).strftime('%Y-%m-%d')})"
        c_res = subprocess.run(['git', 'commit', '-m', msg], cwd=agents_dir, env=GIT_ENV, capture_output=True, text=True)
        if "nothing to commit" in c_res.stdout:
            print("✓ Working tree already clean. Nothing to commit.")
            return True
        print(c_res.stdout.strip()[:200])
        push_res = subprocess.run(['git', 'push', 'origin', 'main'], cwd=agents_dir, env=GIT_ENV, text=True, timeout=180)
        if push_res.returncode == 0:
            print("🎉 Successfully pushed to GitHub origin main!")
            return True
        else:
            print("❌ Git push failed.")
            return False
    except Exception as e:
        print(f"Error during git push: {e}", file=sys.stderr)
        return False

def main():
    parser = argparse.ArgumentParser(
        description="skills.sh Vault Tracker & Ingestion Tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""Examples:
  skillssh --check                     # Audit all >=100K install repos against vault
  skillssh --check --min-installs 500k # Audit repos with >=500K installs
  skillssh --markdown                  # Generate markdown report
  skillssh --sync                      # Ingest missing >=100K repos & reindex categories
  skillssh --sync --push               # Ingest, reindex, and push to GitHub
  skillssh --sync --repo owner/repo    # Ingest a single repository
        """
    )
    parser.add_argument('--check', action='store_true', help='Audit vault against skills.sh (default mode)')
    parser.add_argument('--markdown', nargs='?', const=True, default=False, help='Generate markdown report')
    parser.add_argument('--sync', '--ingest', action='store_true', help='Download missing repositories & reindex')
    parser.add_argument('--push', action='store_true', help='Commit and push changes to GitHub after sync')
    parser.add_argument('--min-installs', default='100k', help='Minimum installs threshold (default: 100k)')
    parser.add_argument('--max-installs', default=None, help='Optional maximum installs threshold')
    parser.add_argument('--limit', type=int, default=None, help='Limit number of repositories')
    parser.add_argument('--refresh', action='store_true', help='Bypass cache and re-fetch from skills.sh')
    parser.add_argument('--repo', default=None, help='Target a single repository (e.g. owner/repo)')
    parser.add_argument('--json', action='store_true', help='Output JSON format')

    args = parser.parse_args()

    min_inst = parse_threshold_arg(args.min_installs)
    max_inst = parse_threshold_arg(args.max_installs) if args.max_installs else None

    if args.repo:
        slug = args.repo.strip().lower()
        if '/' not in slug:
            print("❌ Repo must be formatted as owner/repo", file=sys.stderr)
            sys.exit(1)
        r = {
            'repo': slug,
            'github': f"https://github.com/{slug}",
            'url': f"https://www.skills.sh/{slug}",
            'desc': f"Skills bundle for {slug}"
        }
        if args.sync:
            _, _, upstreams = load_local_knowledge()
            ok = ingest_repository(r, upstreams)
            if ok and os.path.exists(update_py):
                subprocess.run([sys.executable, update_py, '--reindex'], cwd=agents_dir)
            if args.push:
                git_push_vault()
        else:
            folders, known_upstreams, _ = load_local_knowledge()
            present = slug in known_upstreams or any(slug.split('/')[1] in f for f in folders)
            print(f"Repository {slug}: {'✅ In Library' if present else '❌ Missing'}")
        return

    in_vault, missing, total_repos = check_repositories(
        min_installs=min_inst,
        max_installs=max_inst,
        limit=args.limit,
        refresh=args.refresh
    )

    if args.json:
        out = {
            'min_installs': min_inst,
            'max_installs': max_inst,
            'total_count': len(total_repos),
            'in_library_count': len(in_vault),
            'missing_count': len(missing),
            'in_library': in_vault,
            'missing': missing
        }
        print(json.dumps(out, indent=2))
        return

    print_audit_table(in_vault, missing, total_repos, min_inst, max_inst)

    if args.markdown:
        out_p = args.markdown if isinstance(args.markdown, str) else None
        generate_markdown_report(total_repos, in_vault, missing, min_inst, max_inst, output_path=out_p)

    if args.sync:
        ingested = sync_missing(missing)
        if args.push:
            git_push_vault()
    elif missing:
        print(f"💡 Tip: Run 'skillssh --sync' to download all {len(missing)} missing repositories and categorize their skills.\n")

if __name__ == '__main__':
    main()
