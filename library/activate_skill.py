#!/usr/bin/env python3
"""
AgentSkills Universal Activator, Linker & Tier Migration Tool
Author: SeaXen (https://github.com/SeaXen/agentskills)

Usage:
  python activate_skill.py search <keyword>           - Search across all 1,476 skills in library
  python activate_skill.py activate <name>            - Copy skill from library into active workspace
  python activate_skill.py link <name>                - Link skill (Junction/Symlink, 0 duplicate disk space)
  python activate_skill.py remove <name>              - Deactivate / remove skill from workspace
  python activate_skill.py move <name> --to <hot|store|reserve> - Move skill between storage tiers
  python activate_skill.py repos                      - List all offline repositories in library
  python activate_skill.py categories                 - List all 16 functional categories & counts
  python activate_skill.py category <name>            - List all skills in a specific category
  python activate_skill.py info <name>                - Inspect skill documentation & frontmatter
"""

import sys
import os
import shutil
import re
import subprocess

if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
AGENTS_DIR = os.path.dirname(SCRIPT_DIR)
WORKSPACE_ROOT = os.path.dirname(AGENTS_DIR)

STORE_SKILLS_DIR = os.path.join(AGENTS_DIR, 'skills')
HOT_SKILLS_DIR = os.path.join(WORKSPACE_ROOT, '.agent', 'skills')

def get_all_library_repos():
    repos = {}
    for item in os.listdir(SCRIPT_DIR):
        fp = os.path.join(SCRIPT_DIR, item)
        if os.path.isdir(fp) and not item.startswith('.'):
            skills_sub = os.path.join(fp, 'skills')
            if os.path.exists(skills_sub):
                skills = [s for s in os.listdir(skills_sub) if os.path.isdir(os.path.join(skills_sub, s))]
                repos[item] = {
                    'path': fp,
                    'skills_path': skills_sub,
                    'count': len(skills),
                    'skills': set(skills)
                }
    return repos

def find_skill_source(skill_name):
    # Support Hermes 'official/category/skill-name' or relative paths
    skill_name = skill_name.strip().rstrip('/').split('/')[-1]
    repos = get_all_library_repos()
    for repo_name, rdata in repos.items():
        if skill_name in rdata['skills']:
            return os.path.join(rdata['skills_path'], skill_name), repo_name
    return None, None

def search_skills(query):
    q = query.lower()
    repos = get_all_library_repos()
    matches = []
    
    for repo_name, rdata in repos.items():
        for s in sorted(rdata['skills']):
            if q in s.lower():
                desc = "No description"
                s_md = os.path.join(rdata['skills_path'], s, 'SKILL.md')
                if os.path.exists(s_md):
                    try:
                        with open(s_md, 'r', encoding='utf-8', errors='ignore') as f:
                            m = re.search(r'description:\s*(?:>-\s*|\|\s*)?(.*?)(?:\n[a-zA-Z0-9_-]+:|\n---)', f.read(1500), re.DOTALL)
                            if m:
                                desc = m.group(1).strip().replace('\n', ' ')
                                desc = re.sub(r'\s+', ' ', desc)[:100]
                    except:
                        pass
                matches.append((s, repo_name, desc))

    print(f"\n🔍 Found {len(matches)} matching skills for '{query}':")
    print("=" * 75)
    for s, r, d in matches[:30]:
        print(f" • {s:32} [{r:26}] - {d}...")
    if len(matches) > 30:
        print(f"\n ... and {len(matches) - 30} more matches. Refine your query for more specific results.")
    print("=" * 75)

def activate_skill(skill_name):
    src, repo = find_skill_source(skill_name)
    if not src:
        print(f"❌ Error: Skill '{skill_name}' was not found in any offline library repository.")
        return False

    os.makedirs(STORE_SKILLS_DIR, exist_ok=True)
    dst = os.path.join(STORE_SKILLS_DIR, skill_name)

    if os.path.exists(dst):
        print(f"⚠️ Skill '{skill_name}' is already installed in .agents/skills/.")
    else:
        shutil.copytree(src, dst)
        print(f"✅ Installed '{skill_name}' -> .agents/skills/ (from {repo})")

    # Sync to hot set if .agent/skills exists
    if os.path.exists(os.path.dirname(HOT_SKILLS_DIR)):
        os.makedirs(HOT_SKILLS_DIR, exist_ok=True)
        dst_hot = os.path.join(HOT_SKILLS_DIR, skill_name)
        if not os.path.exists(dst_hot):
            shutil.copytree(src, dst_hot)
            print(f"🔥 Activated '{skill_name}' -> .agent/skills/ (Active Hot Set)")
    return True

def link_skill(skill_name):
    src, repo = find_skill_source(skill_name)
    if not src:
        print(f"❌ Error: Skill '{skill_name}' was not found in any offline library repository.")
        return False

    os.makedirs(STORE_SKILLS_DIR, exist_ok=True)
    dst = os.path.join(STORE_SKILLS_DIR, skill_name)

    if os.path.exists(dst):
        print(f"⚠️ Target '{dst}' already exists. Please remove it first before linking.")
        return False

    try:
        if sys.platform == 'win32':
            # Create Windows Directory Junction (no admin privileges needed)
            subprocess.run(['cmd', '/c', 'mklink', '/J', dst, src], check=True, capture_output=True)
        else:
            os.symlink(src, dst)
        print(f"🔗 Linked '{skill_name}' -> .agents/skills/{skill_name}")
        print(f"   (Points directly to {repo}, consuming 0 duplicated disk space!)")
        return True
    except Exception as e:
        print(f"❌ Linking failed: {e}. Falling back to standard copy...")
        return activate_skill(skill_name)

def remove_skill(skill_name):
    removed = False
    for path, label in [(os.path.join(STORE_SKILLS_DIR, skill_name), ".agents/skills"),
                        (os.path.join(HOT_SKILLS_DIR, skill_name), ".agent/skills")]:
        if os.path.exists(path):
            if os.path.islink(path):
                os.unlink(path)
                print(f"✓ Removed link: {label}/{skill_name}")
                removed = True
            elif sys.platform == 'win32' and os.path.isdir(path):
                try:
                    os.rmdir(path) # Works for junctions without deleting target contents!
                    print(f"✓ Unlinked junction: {label}/{skill_name}")
                    removed = True
                except Exception:
                    shutil.rmtree(path)
                    print(f"✓ Removed directory: {label}/{skill_name}")
                    removed = True
            else:
                shutil.rmtree(path)
                print(f"✓ Removed directory: {label}/{skill_name}")
                removed = True

    if not removed:
        print(f"⚠️ Skill '{skill_name}' was not active in either .agents/skills or .agent/skills.")
    else:
        print(f"🗑️ Deactivation complete. '{skill_name}' remains safely preserved in library reserve.")

def move_skill(skill_name, target_tier):
    t = target_tier.lower()
    if t == 'hot':
        src = os.path.join(STORE_SKILLS_DIR, skill_name)
        if not os.path.exists(src):
            src, _ = find_skill_source(skill_name)
        if not src or not os.path.exists(src):
            print(f"❌ Skill '{skill_name}' not found.")
            return
        dst = os.path.join(HOT_SKILLS_DIR, skill_name)
        os.makedirs(HOT_SKILLS_DIR, exist_ok=True)
        if not os.path.exists(dst):
            shutil.copytree(src, dst)
        print(f"🔥 Moved '{skill_name}' to Active Hot Set (.agent/skills)")

    elif t == 'store':
        activate_skill(skill_name)
        # remove from hot if desired
        hot_p = os.path.join(HOT_SKILLS_DIR, skill_name)
        if os.path.exists(hot_p):
            shutil.rmtree(hot_p)
            print(f"✓ Demoted '{skill_name}' from Hot Set to Workspace Store (.agents/skills)")

    elif t == 'reserve':
        remove_skill(skill_name)
        print(f"📦 '{skill_name}' moved to Offline Reserve only (0 active context tokens)")


def list_categories():
    cat_file = os.path.join(AGENTS_DIR, "category", "categories_index.json")
    if os.path.exists(cat_file):
        import json
        with open(cat_file, "r", encoding="utf-8") as f:
            cdata = json.load(f)
        print("\n🗂️ AGENTSKILLS FUNCTIONAL CATEGORIES:")
        print("=" * 70)
        print(f"{'Category Slug':24} | {'Skills':7} | {'Domain Title'}")
        print("-" * 70)
        for c_slug, c_info in cdata["categories"].items():
            print(f" • {c_slug:22} | {c_info['count']:4}   | {c_info['title']}")
        print("=" * 70)
        print(f"Total: {cdata.get('total_unique_skills', cdata.get('total_skills', 0))} unique skills organized across {len(cdata['categories'])} categories.")
        print(f"Direct browsing: {os.path.join(AGENTS_DIR, 'category')}\n")
    else:
        print("❌ categories_index.json not found.")

def list_category_skills(cat_name):
    cat_file = os.path.join(AGENTS_DIR, "category", "categories_index.json")
    if os.path.exists(cat_file):
        import json
        with open(cat_file, "r", encoding="utf-8") as f:
            cdata = json.load(f)
        if cat_name not in cdata["categories"]:
            print(f"❌ Unknown category '{cat_name}'. Run 'activate_skill.py categories' to view valid categories.")
            return
        info = cdata["categories"][cat_name]
        print(f"\n📂 Category: {info['title']} ({len(info['skills'])} skills)")
        if 'description' in info: print(f"Description: {info['description']}")
        print("=" * 75)
        print(f"{'Skill Name':30} | {'Status':8} | {'Repository'}")
        print("-" * 75)
        for s in info["skills"]:
            status = "🟢 Active" if s["is_active"] else "📦 Library"
            print(f" • {s['name']:28} | {status:8} | {s['repo']}")
        print("=" * 75)
        print(f"To link any skill: python activate_skill.py link <skill-name>\n")

def list_repos():
    repos = get_all_library_repos()
    total_skills = sum(r['count'] for r in repos.values())
    print("\n📚 OFFLINE RESERVE REPOSITORIES IN LIBRARY:")
    print("=" * 65)
    print(f"{'Repository Folder':35} | {'Skills Count':12}")
    print("-" * 65)
    for r_name, rdata in sorted(repos.items(), key=lambda x: x[1]['count'], reverse=True):
        print(f" • {r_name:33} | {rdata['count']:4} skills")
    print("=" * 65)
    print(f"Total Available Reserve Skills: {total_skills} skills across {len(repos)} repositories.")

def info_skill(skill_name):
    src, repo = find_skill_source(skill_name)
    if not src:
        print(f"❌ Skill '{skill_name}' not found.")
        return
    skill_md = os.path.join(src, 'SKILL.md')
    if os.path.exists(skill_md):
        print(f"\n--- Skill: {skill_name} (Repository: {repo}) ---")
        with open(skill_md, 'r', encoding='utf-8', errors='ignore') as f:
            print(f.read()[:1500])

if __name__ == '__main__':
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        sys.exit(0)

    cmd = args[0].lower()
    if len(args) >= 2 and cmd != 'search':
        args[1] = args[1].strip().rstrip('/').split('/')[-1]
    if cmd == 'search' and len(args) >= 2:
        search_skills(args[1])
    elif cmd == 'activate' and len(args) >= 2:
        activate_skill(args[1])
    elif cmd == 'link' and len(args) >= 2:
        link_skill(args[1])
    elif cmd == 'remove' and len(args) >= 2:
        remove_skill(args[1])
    elif cmd == 'move' and len(args) >= 4 and args[2] == '--to':
        move_skill(args[1], args[3])
    elif cmd in ['repos', 'repositories']:
        list_repos()
    elif cmd in ['categories', 'cats']:
        list_categories()
    elif cmd in ['category', 'cat'] and len(args) >= 2:
        list_category_skills(args[1])
    elif cmd == 'info' and len(args) >= 2:
        info_skill(args[1])
    elif cmd not in ['help', '--help', '-h']:
        # Direct 1-click activation: user typed skill name directly!
        target_skill = cmd.strip().rstrip('/').split('/')[-1]
        print(f"âš¡ 1-Click Activation requested for '{target_skill}'...")
        link_skill(target_skill)
    else:
        print(__doc__)
