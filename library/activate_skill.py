#!/usr/bin/env python3
"""
Antigravity Skill Library Activator
Allows searching, inspecting, and activating skills from the 889+ local library into .agent/skills/
"""

import sys
import os
import shutil
import re
import yaml

if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

LIBRARY_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'antigravity-awesome-skills', 'skills')
ACTIVE_SKILLS_DIR = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'skills'))
AGENTS_SKILLS_DIR = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '.agents', 'skills'))

def get_all_library_skills():
    skills = {}
    if not os.path.exists(LIBRARY_DIR):
        return skills
    for item in sorted(os.listdir(LIBRARY_DIR)):
        skill_path = os.path.join(LIBRARY_DIR, item)
        if os.path.isdir(skill_path):
            skill_md = os.path.join(skill_path, 'SKILL.md')
            desc = 'No description'
            if os.path.exists(skill_md):
                try:
                    with open(skill_md, 'r', encoding='utf-8') as f:
                        content = f.read()
                    fm = re.search(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
                    if fm:
                        data = yaml.safe_load(fm.group(1))
                        desc = data.get('description', desc)
                except Exception:
                    pass
            skills[item] = desc
    return skills

def search_skills(query):
    skills = get_all_library_skills()
    q = query.lower()
    matches = []
    for name, desc in skills.items():
        if q in name.lower() or q in desc.lower():
            matches.append((name, desc))
    
    print(f"\n🔍 Found {len(matches)} matching skills for '{query}':\n")
    for name, desc in matches[:25]:
        first_sentence = desc.split('.')[0].strip() if desc else ''
        print(f"  • {name.ljust(35)} - {first_sentence[:80]}...")
    if len(matches) > 25:
        print(f"\n  ... and {len(matches) - 25} more. Refine your query for more specific matches.")

def activate_skill(skill_name):
    src = os.path.join(LIBRARY_DIR, skill_name)
    if not os.path.exists(src):
        print(f"❌ Error: Skill '{skill_name}' not found in library.")
        return False

    # Copy to .agent/skills/
    dst1 = os.path.join(ACTIVE_SKILLS_DIR, skill_name)
    if os.path.exists(dst1):
        print(f"⚠️ Skill '{skill_name}' is already active in .agent/skills/.")
    else:
        shutil.copytree(src, dst1)
        print(f"✅ Activated '{skill_name}' -> .agent/skills/{skill_name}")

    # Copy to .agents/skills/
    if os.path.exists(os.path.dirname(AGENTS_SKILLS_DIR)):
        dst2 = os.path.join(AGENTS_SKILLS_DIR, skill_name)
        if not os.path.exists(dst2):
            shutil.copytree(src, dst2)
            print(f"✅ Synced '{skill_name}' -> .agents/skills/{skill_name}")
    return True

def info_skill(skill_name):
    skill_path = os.path.join(LIBRARY_DIR, skill_name)
    skill_md = os.path.join(skill_path, 'SKILL.md')
    if not os.path.exists(skill_md):
        print(f"❌ Skill '{skill_name}' not found.")
        return
    with open(skill_md, 'r', encoding='utf-8') as f:
        print(f.read()[:1200])

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python activate_skill.py search <keyword>   - Search 889 library skills")
        print("  python activate_skill.py activate <name>    - Activate skill into workspace")
        print("  python activate_skill.py info <name>        - Inspect skill instructions")
        sys.exit(0)

    cmd = sys.argv[1].lower()
    if cmd == 'search' and len(sys.argv) >= 3:
        search_skills(sys.argv[2])
    elif cmd == 'activate' and len(sys.argv) >= 3:
        activate_skill(sys.argv[2])
    elif cmd == 'info' and len(sys.argv) >= 3:
        info_skill(sys.argv[2])
    elif cmd == 'count':
        print(f"Total skills available in library: {len(get_all_library_skills())}")
    else:
        print("Invalid command. Use search, activate, or info.")
