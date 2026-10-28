import os
import sys
import json
import re

if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

def rebuild_provenance(agents_dir=None):
    if not agents_dir:
        agents_dir = os.path.dirname(os.path.abspath(__file__))
    lib_dir = os.path.join(agents_dir, 'library')
    prov_path = os.path.join(agents_dir, 'SKILLS_PROVENANCE.md')
    upstreams_file = os.path.join(lib_dir, 'upstreams.json')

    upstreams = {}
    if os.path.exists(upstreams_file):
        try:
            with open(upstreams_file, 'r', encoding='utf-8') as f:
                upstreams = json.load(f)
        except Exception:
            pass

    repo_folders = sorted([d for d in os.listdir(lib_dir) if os.path.isdir(os.path.join(lib_dir, d)) and not d.startswith('.') and d != '__pycache__'])

    table_rows = []
    total_skills = 0

    for rf in repo_folders:
        rp = os.path.join(lib_dir, rf)
        skills_sub = os.path.join(rp, 'skills')
        s_count = 0
        sample_skill = "skill-name"
        if os.path.exists(skills_sub):
            s_list = [s for s in os.listdir(skills_sub) if os.path.isdir(os.path.join(skills_sub, s))]
            s_count = len(s_list)
            if s_list:
                sample_skill = s_list[0]
        total_skills += s_count

        u_info = upstreams.get(rf, {})
        u_url = u_info.get('url', f"https://github.com/{rf}")
        u_name = u_info.get('upstream', rf)

        if rf == '#searex-skill':
            u_name = 'SeaRex / Custom'
            u_url = 'https://github.com/SeaXen/agentskills'

        table_rows.append(f"| `{rf}` | [{u_name}]({u_url}) | **{s_count}** | `python .agents/library/activate_skill.py activate {sample_skill}` |")

    header = f"""# 🏛️ Complete Repository Provenance & Upstream Registry

> **Active Reserve Libraries**: {len(repo_folders)} repositories  
> **Total Skills in Reserve**: {total_skills:,} skills  
> **Source Registry**: [`library/upstreams.json`](library/upstreams.json)  
> **Format Standard**: Pure isolated repositories (`['skills', 'README.md', 'skills_index.json']`), 0 `.git` directories.

---

## 🗺️ Complete Multi-Repository Inventory

| Local Repository Folder | Upstream Source & Canonical URL | Skills in Reserve | Quick Activation Command |
| :--- | :--- | :---: | :--- |
"""

    footer = f"""
---

## 🔄 Automated Upstream Synchronization
Every repository in this registry is independently tracked via its upstream GitHub remote:
- To check for upstream updates and ingest new skills:
  ```powershell
  python .agents/update.py
  ```
- To re-index manifests and refresh provenance:
  ```powershell
  python .agents/update.py --index
  ```
"""

    content = header + "\n".join(table_rows) + footer

    with open(prov_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"✓ Successfully generated SKILLS_PROVENANCE.md with {len(repo_folders)} repositories and {total_skills} skills.")
    return total_skills

if __name__ == '__main__':
    rebuild_provenance()
