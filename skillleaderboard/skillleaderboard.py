#!/usr/bin/env python3
"""
The Skill Leaderboard Tracker & Vault Synchronizer
Website: https://www.skillleaderboard.com/

Enables humans and AI agents to track, audit, and ingest:
  - Top 150 Most Starred skills (--starred [N], default 150)
  - Top 50 Trending skills by 7-day growth (--trending [N], default 50)
  - Top skills by Traction score (--traction [N])
  - Newest skills (--newest [N])
  - Automated downloading and vault ingestion (--ingest / --sync)
  - Clean 3-item vault standardization (skills/, README.md, skills_index.json, .upstream_commit)
  - 38-Category taxonomy and provenance rebuilding

Usage Examples:
  python skillleaderboard.py --trending
  python skillleaderboard.py --starred
  python skillleaderboard.py --trending 50 --json
  python skillleaderboard.py --starred 150 --ingest
  python skillleaderboard.py --trending 50 --ingest --push
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
from datetime import datetime, timezone

if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

# Paths: skillleaderboard/ is directly inside .agents/
script_dir = os.path.dirname(os.path.abspath(__file__))
agents_dir = os.path.dirname(script_dir) if os.path.basename(script_dir) == 'skillleaderboard' else script_dir
lib_dir = os.path.join(agents_dir, 'library')
upstreams_file = os.path.join(lib_dir, 'upstreams.json')
temp_clone_dir = os.path.join(agents_dir, '.temp_leaderboard_clones')

API_CATALOG_URL = "https://www.skillleaderboard.com/api/catalog"

def remove_readonly(func, path, exc_info):
    try:
        os.chmod(path, stat.S_IWRITE)
        func(path)
    except Exception:
        pass

def fetch_catalog():
    """Fetch live catalog from skillleaderboard.com API."""
    req = urllib.request.Request(
        API_CATALOG_URL,
        headers={'User-Agent': 'AntigravityAgent/2.0 (Vault Synchronizer)'}
    )
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            return data.get('catalog', [])
    except Exception as e:
        print(f"❌ Error fetching catalog from {API_CATALOG_URL}: {e}", file=sys.stderr)
        return []

def load_local_knowledge():
    """Load local upstreams and library folders for cross-referencing."""
    upstreams = {}
    if os.path.exists(upstreams_file):
        try:
            with open(upstreams_file, 'r', encoding='utf-8') as f:
                upstreams = json.load(f)
        except Exception as e:
            print(f"⚠️ Warning loading upstreams.json: {e}", file=sys.stderr)

    known_upstreams = set()
    for k, v in upstreams.items():
        if isinstance(v, dict):
            if 'upstream' in v:
                known_upstreams.add(v['upstream'].lower())
            if 'url' in v:
                known_upstreams.add(v['url'].lower().rstrip('.git').replace('https://github.com/', ''))
        elif isinstance(v, str):
            known_upstreams.add(v.lower())
        known_upstreams.add(k.lower())

    local_folders = set()
    if os.path.exists(lib_dir):
        local_folders = set(os.listdir(lib_dir))

    return upstreams, known_upstreams, local_folders

def analyze_leaderboard(catalog, sort_mode='starred', limit=150):
    """Sort and cross-reference catalog against local library."""
    upstreams, known_upstreams, local_folders = load_local_knowledge()

    if sort_mode == 'trending':
        sorted_items = sorted(catalog, key=lambda x: (x.get('stars7d') or 0), reverse=True)
        title = f"Top {limit} Trending Skills (7-Day Star Growth)"
    elif sort_mode == 'traction':
        sorted_items = sorted(catalog, key=lambda x: (x.get('tractionScore') or 0), reverse=True)
        title = f"Top {limit} Skills by Traction Score"
    elif sort_mode == 'newest':
        sorted_items = sorted(catalog, key=lambda x: x.get('githubCreatedAt', ''), reverse=True)
        title = f"Top {limit} Newest Skills"
    else: # 'starred'
        sorted_items = sorted(catalog, key=lambda x: (x.get('stars') or 0), reverse=True)
        title = f"Top {limit} Most Starred Skills"

    selected = sorted_items[:limit]

    already_present = []
    missing = []

    for idx, item in enumerate(selected, 1):
        repo = item.get('repo', f"{item.get('owner')}/{item.get('name')}")
        owner = item.get('owner', '')
        name = item.get('name', '')
        folder_slug = f"{owner}-{name}".lower()

        is_present = False
        matched_by = None

        if repo.lower() in known_upstreams:
            is_present = True
            matched_by = "upstreams.json"
        elif folder_slug in local_folders or name.lower() in local_folders or folder_slug.replace('-', '_') in local_folders:
            is_present = True
            matched_by = "library folder"
        else:
            # Check for substring in upstreams
            for up_k, up_v in upstreams.items():
                u_str = str(up_v).lower()
                if repo.lower() in u_str or f"/{repo.lower()}" in u_str:
                    is_present = True
                    matched_by = f"upstream: {up_k}"
                    break

        entry = {
            'rank': idx,
            'repo': repo,
            'owner': owner,
            'name': name,
            'stars': item.get('stars') or 0,
            'stars7d': item.get('stars7d') or 0,
            'tractionScore': item.get('tractionScore'),
            'category': item.get('category', 'General'),
            'tagline': item.get('tagline') or item.get('summary', ''),
            'url': f"https://github.com/{repo}",
            'is_present': is_present,
            'matched_by': matched_by,
            'folder_slug': folder_slug
        }

        if is_present:
            already_present.append(entry)
        else:
            missing.append(entry)

    return {
        'title': title,
        'mode': sort_mode,
        'limit': limit,
        'total_examined': len(selected),
        'present_count': len(already_present),
        'missing_count': len(missing),
        'coverage_pct': round((len(already_present) / len(selected) * 100) if selected else 0, 1),
        'already_present': already_present,
        'missing': missing
    }

def print_report(analysis):
    """Format and print analysis report."""
    print("=" * 72)
    print(f"📊 SKILL LEADERBOARD AUDIT: {analysis['title']}")
    print(f"🔗 Source: {API_CATALOG_URL}")
    print("=" * 72)
    print(f"Total Examined:    {analysis['total_examined']}")
    print(f"Already in Vault:  {analysis['present_count']} ({analysis['coverage_pct']}%)")
    print(f"Missing from Vault:{analysis['missing_count']}")
    print("=" * 72)

    if analysis['missing']:
        print("\n🔍 MISSING REPOSITORIES:")
        for m in analysis['missing']:
            stars_info = f"★ {m['stars']:,}"
            if m['stars7d']:
                stars_info += f" (+{m['stars7d']:,} 7d)"
            print(f"  #{m['rank']:<3} {m['repo']:<35} | {stars_info:<22} | {m['category']}")
            if m['tagline']:
                print(f"       Description: {m['tagline'][:85]}")
            print(f"       GitHub:      {m['url']}")
        print(f"\n💡 Run with '--ingest' to automatically clone and add these missing skills.")
    else:
        print("\n✨ 100% COVERAGE! All tracked repositories in this category are in your library.")
    print("=" * 72)

def ingest_repository(item, upstreams):
    """Download, clean to 3-item standard, and register an upstream repo."""
    owner = item['owner']
    name = item['name']
    repo = item['repo']
    folder_slug = item['folder_slug']
    target_dir = os.path.join(lib_dir, folder_slug)
    clone_tmp = os.path.join(temp_clone_dir, folder_slug)

    print(f"\n📥 Ingesting {repo}...")
    if os.path.exists(clone_tmp):
        shutil.rmtree(clone_tmp, onerror=remove_readonly)
    os.makedirs(clone_tmp, exist_ok=True)

    # 1. Shallow clone
    cmd = ['git', 'clone', '--depth', '1', f"https://github.com/{repo}.git", clone_tmp]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"❌ Failed to clone {repo}: {res.stderr.strip()}", file=sys.stderr)
        return False

    # Extract commit hash
    commit_res = subprocess.run(['git', 'rev-parse', 'HEAD'], cwd=clone_tmp, capture_output=True, text=True)
    commit_hash = commit_res.stdout.strip() if commit_res.returncode == 0 else 'main'

    # 2. Setup target dir in library
    if os.path.exists(target_dir):
        shutil.rmtree(target_dir, onerror=remove_readonly)
    os.makedirs(target_dir, exist_ok=True)
    skills_sub = os.path.join(target_dir, 'skills')
    os.makedirs(skills_sub, exist_ok=True)

    # 3. Locate skills:
    # A. Check if repo has a 'skills' folder
    src_skills = os.path.join(clone_tmp, 'skills')
    if os.path.exists(src_skills) and any(os.path.isdir(os.path.join(src_skills, d)) for d in os.listdir(src_skills)):
        shutil.rmtree(skills_sub, ignore_errors=True)
        shutil.copytree(src_skills, skills_sub)
    else:
        # B. Check plugins, subdirectories, or .claude
        for root, dirs, files in os.walk(clone_tmp):
            if '.git' in root:
                continue
            for f in files:
                if f.lower() == 'skill.md':
                    parent = os.path.dirname(os.path.join(root, f))
                    skill_id = os.path.basename(parent)
                    if skill_id in ['skills', 'plugins', '.', os.path.basename(clone_tmp)]:
                        skill_id = re.sub(r'[^a-zA-Z0-9_-]', '-', name.lower()).strip('-')
                    dest_skill = os.path.join(skills_sub, skill_id)
                    if not os.path.exists(dest_skill):
                        shutil.copytree(parent, dest_skill)

    # C. If still no skills discovered, synthesize single skill from root SKILL.md/README
    root_skills = [d for d in os.listdir(skills_sub) if os.path.isdir(os.path.join(skills_sub, d))]
    if not root_skills:
        skill_slug = re.sub(r'[^a-zA-Z0-9_-]', '-', name.lower()).strip('-')
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

        tagline = item.get('tagline') or f"Skills for {repo}"
        if content:
            if not content.strip().startswith('---'):
                full_text = f"---\nname: {skill_slug}\ndescription: {tagline}\n---\n\n" + content
            else:
                full_text = content
        else:
            full_text = f"---\nname: {skill_slug}\ndescription: {tagline}\n---\n\n# {repo}\n\n{tagline}\n"

        with open(dest_md, 'w', encoding='utf-8') as sf:
            sf.write(full_text)

        # Copy any supporting agents or scripts
        for sub in ['agents', 'scripts', 'references', 'examples', 'media']:
            sp = os.path.join(clone_tmp, sub)
            if os.path.exists(sp):
                dp = os.path.join(single_skill_dir, sub)
                if not os.path.exists(dp):
                    shutil.copytree(sp, dp)

    # 4. Standard README.md
    readme_src = os.path.join(clone_tmp, 'README.md')
    readme_dst = os.path.join(target_dir, 'README.md')
    if os.path.exists(readme_src):
        shutil.copy2(readme_src, readme_dst)
    else:
        with open(readme_dst, 'w', encoding='utf-8') as rf:
            rf.write(f"# {repo}\n\n{item.get('tagline', '')}\n")

    # 5. .upstream_commit
    with open(os.path.join(target_dir, '.upstream_commit'), 'w', encoding='utf-8') as cf:
        cf.write(f"{commit_hash}\n")

    # 6. Purge any nested .git
    for root, dirs, files in os.walk(target_dir):
        if '.git' in dirs:
            shutil.rmtree(os.path.join(root, '.git'), onerror=remove_readonly)

    # 7. Update upstreams.json
    upstreams[folder_slug] = {
        'type': 'github-repo',
        'upstream': repo,
        'url': f"https://github.com/{repo}"
    }

    skills_count = len(os.listdir(skills_sub)) if os.path.exists(skills_sub) else 0
    print(f"✓ Ingested {repo} into library/{folder_slug} ({skills_count} skills).")
    return True

def run_vault_rebuild(push=False):
    """Trigger update.py reindex and optional git push."""
    print("\n🔄 Rebuilding Vault Indexes, Categories, and Provenance...")
    update_py = os.path.join(agents_dir, 'update.py')
    cmd = [sys.executable, update_py, '--reindex']
    subprocess.run(cmd, check=True)

    if push:
        print("\n🚀 Pushing changes to GitHub origin main...")
        subprocess.run(['git', 'add', '-A'], cwd=agents_dir, check=True)
        ts = datetime.now().strftime('%Y-%m-%d %H:%M')
        subprocess.run(['git', 'commit', '-m', f"feat(leaderboard): auto-sync skills from skillleaderboard.com ({ts})"], cwd=agents_dir, check=True)
        subprocess.run(['git', 'push', 'origin', 'main'], cwd=agents_dir, check=True)

def main():
    parser = argparse.ArgumentParser(
        description="The Skill Leaderboard Tracker & Vault Synchronizer (skillleaderboard.com)"
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--trending', nargs='?', const=50, type=int, help="Check Trending skills by 7-day star growth (default: 50)")
    group.add_argument('--starred', nargs='?', const=150, type=int, help="Check Most Starred skills (default: 150)")
    group.add_argument('--traction', nargs='?', const=50, type=int, help="Check skills by Traction Score (default: 50)")
    group.add_argument('--newest', nargs='?', const=50, type=int, help="Check Newest skills (default: 50)")

    parser.add_argument('--limit', type=int, default=None, help="Override number of top skills to check")
    parser.add_argument('--json', action='store_true', help="Output results in JSON format")
    parser.add_argument('--ingest', '--sync', action='store_true', dest='ingest', help="Automatically ingest any missing skills into the library")
    parser.add_argument('--update', action='store_true', help="Check and pull latest updates for existing repositories on leaderboard")
    parser.add_argument('--push', action='store_true', help="Git commit and push after ingestion or update")

    args = parser.parse_args()

    # Determine mode and limit
    if args.trending is not None:
        sort_mode = 'trending'
        limit = args.limit or args.trending
    elif args.traction is not None:
        sort_mode = 'traction'
        limit = args.limit or args.traction
    elif args.newest is not None:
        sort_mode = 'newest'
        limit = args.limit or args.newest
    elif args.starred is not None:
        sort_mode = 'starred'
        limit = args.limit or args.starred
    else:
        # Default when run without flags: check Top 150 Most Starred
        sort_mode = 'starred'
        limit = args.limit or 150

    catalog = fetch_catalog()
    if not catalog:
        print("❌ Could not retrieve catalog from skillleaderboard.com API. Check internet connection.", file=sys.stderr)
        sys.exit(1)

    analysis = analyze_leaderboard(catalog, sort_mode=sort_mode, limit=limit)

    if args.json:
        print(json.dumps(analysis, indent=2))
    else:
        print_report(analysis)

    # Ingestion or update flow
    if args.update and analysis['in_vault']:
        print(f"\n🔄 UPDATE MODE ACTIVATED ({len(analysis['in_vault'])} existing repositories)")
        upstreams, _, _ = load_local_knowledge()
        updated_count = 0
        try:
            for item in analysis['in_vault']:
                if ingest_repository(item, upstreams):
                    updated_count += 1

            if updated_count > 0:
                with open(upstreams_file, 'w', encoding='utf-8') as f:
                    json.dump(upstreams, f, indent=2)

                run_vault_rebuild(push=args.push)
                print(f"\n🎉 Successfully updated {updated_count} repositories in your vault!")
        finally:
            if os.path.exists(temp_clone_dir):
                shutil.rmtree(temp_clone_dir, onerror=remove_readonly)
    elif args.ingest and analysis['missing']:
        print(f"\n📦 INGESTION MODE ACTIVATED ({len(analysis['missing'])} missing repositories)")
        upstreams, _, _ = load_local_knowledge()
        ingested_count = 0

        try:
            for item in analysis['missing']:
                if ingest_repository(item, upstreams):
                    ingested_count += 1

            if ingested_count > 0:
                with open(upstreams_file, 'w', encoding='utf-8') as f:
                    json.dump(upstreams, f, indent=2)

                run_vault_rebuild(push=args.push)
                print(f"\n🎉 Successfully ingested {ingested_count} repositories into your vault!")
        finally:
            if os.path.exists(temp_clone_dir):
                shutil.rmtree(temp_clone_dir, onerror=remove_readonly)

if __name__ == '__main__':
    main()
