import os
import sys
import shutil
import json
import re

if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

def word_match(pattern, text):
    return bool(re.search(r"\b" + re.escape(pattern) + r"\b", text, re.IGNORECASE))

GRANULAR_CATEGORIES = {
    # Software Engineering (broken down from 722)
    "code-quality-refactoring": {
        "title": "🧹 Code Quality, Refactoring & Clean Code",
        "keywords": ["clean-code", "refactor", "tech-debt", "code review", "code quality", "ponytail", "caveman", "lint", "naming", "formatting"]
    },
    "architecture-system-design": {
        "title": "🏛️ Architecture, System Design & Patterns",
        "keywords": ["architecture", "system-design", "system design", "domain-model", "adr", "microservice", "design-pattern", "pattern", "c4-", "atlas", "system-atlas"]
    },
    "git-version-control": {
        "title": "🐙 Git, Worktrees & PR Workflows",
        "keywords": ["git-", "worktree", "branch", "pull request", "pr-", "commit", "github", "gitlab", "finishing-a-development"]
    },
    "terminal-system-tools": {
        "title": "💻 Terminal, Shell & System Automation",
        "keywords": ["bash", "linux", "powershell", "shell", "terminal", "cli-", "command", "desktop-commander", "cline-skills", "sysadmin"]
    },
    "programming-languages-core": {
        "title": "📐 Programming Languages & Type Systems",
        "keywords": ["typescript", "python-patterns", "rust", "golang", "csharp", "java", "scala", "cpp", "type-system", "shoehorn", "fp-ts"]
    },
    "fullstack-web-frameworks": {
        "title": "🌐 Fullstack Web Frameworks & Apps",
        "keywords": ["fullstack", "nextjs", "remix", "astrojs", "astro.build", "app-router", "server-action", "serverless-web", "tanstack", "app-builder"]
    },
    "algorithms-logic": {
        "title": "🧮 Algorithms, Logic & Math",
        "keywords": ["algorithm", "algorithmic", "math", "logic", "olympiad", "calculation", "sorting", "solver"]
    },

    # Frontend (broken down from 115)
    "frontend-ui-components": {
        "title": "🎨 Frontend Components & Design Systems",
        "keywords": ["radix", "shadcn", "tailwind", "css", "component", "styling", "ui-kit", "widgets", "html", "vue", "angular", "stencil", "dark-ts"]
    },
    "frontend-motion-animation": {
        "title": "✨ UI Motion, Animations & Polish",
        "keywords": ["animation", "motion", "emil", "micro-interaction", "transitions", "scroll", "interactive-ui", "gsap", "framer"]
    },
    "frontend-visual-taste": {
        "title": "👁️ Visual Taste, Critique & Typography",
        "keywords": ["taste", "impeccable", "typography", "font", "anti-slop", "visual-rhythm", "aesthetic", "apple-design", "color"]
    },

    # Backend & API (59)
    "backend-api-design": {
        "title": "⚡ Backend Systems, REST & Microservices",
        "keywords": ["api-patterns", "api", "rest", "graphql", "trpc", "nodejs", "nestjs", "express", "endpoint", "microservices-resilience", "backend", "server-management"]
    },

    # Database (broken down from 50)
    "database-sql-relational": {
        "title": "🗄️ SQL Databases, ORMs & Indexing",
        "keywords": ["postgres", "mysql", "sqlite", "sql", "prisma", "drizzle", "query-optimizer", "indexing", "migration", "schema"]
    },
    "database-nosql-serverless": {
        "title": "⚡ NoSQL, Serverless & Vector DBs",
        "keywords": ["supabase", "neon", "redis", "firebase", "firestore", "nosql", "cosmos", "vector", "dsql"]
    },

    # DevOps & Cloud (47)
    "cloudflare-edge": {
        "title": "☁️ Cloudflare Workers, Pages & Edge",
        "keywords": ["cloudflare", "workers", "wrangler", "edge", "d1", "pages-build"]
    },
    "devops-docker-cicd": {
        "title": "🚀 DevOps, Containers & Deployment",
        "keywords": ["deploy", "docker", "kubernetes", "vercel", "teamcity", "netlify", "ci/cd", "terraform", "render", "railway", "container"]
    },

    # Testing & QA (broken down from 109)
    "testing-playwright-e2e": {
        "title": "🎭 Playwright & Browser Automation",
        "keywords": ["playwright", "browser-use", "headless", "browser-automation", "e2e", "crawler", "scraper", "webapp-testing"]
    },
    "testing-unit-tdd": {
        "title": "🧪 Unit Testing, TDD & Verification",
        "keywords": ["tdd", "test-driven", "unit-test", "vitest", "jest", "mutation-testing", "property-based", "benchmark", "verify", "test-runner"]
    },

    # Security (broken down from 99)
    "security-vulnerability-audit": {
        "title": "🛡️ Vulnerability Auditing & Pentesting",
        "keywords": ["vulnerability", "security-audit", "penetration", "red-team", "threat", "mitre", "owasp", "security-scanner", "hack"]
    },
    "security-compliance-auth": {
        "title": "🔒 Auth, Hardening & Compliance",
        "keywords": ["auth", "oauth", "jwt", "hardened", "sox", "compliance", "permission", "iam", "privacy", "guardrail"]
    },

    # AI & Agents (broken down from 97)
    "autonomous-agents-hermes": {
        "title": "🧠 NousResearch Hermes Agent Skills",
        "keywords": ["hermes", "nousresearch"]
    },
    "multi-agent-orchestration": {
        "title": "🤖 Multi-Agent Systems & Swarms",
        "keywords": ["orchestrat", "parallel-agents", "subagent", "agent-team", "dispatching-parallel", "swarm", "agent-browser"]
    },
    "prompt-llm-engineering": {
        "title": "💬 Prompt Engineering, LLMs & RAG",
        "keywords": ["prompt", "llm", "rag", "eval", "fine-tuning", "avatar", "gemini", "claude-api", "openai", "token"]
    },
    "lobehub-ecosystem": {
        "title": "🌐 LobeHub Agent Skills Suite",
        "keywords": ["lobehub", "lobe-"]
    },

    # Data & ML (11)
    "data-engineering-ml": {
        "title": "📊 Data Pipelines, BigQuery & Machine Learning",
        "keywords": ["spark", "dataproc", "dataflow", "beam", "bigquery", "dbt", "dataform", "machine-learning", "ml-", "notebook", "pandas"]
    },

    # Mobile (21)
    "mobile-ios-android": {
        "title": "📱 Mobile Development (iOS, Android, React Native)",
        "keywords": ["mobile", "ios", "android", "flutter", "swift", "kotlin", "expo", "app-store", "uizze"]
    },

    # Web3 (13)
    "web3-smart-contracts": {
        "title": "🪙 Web3, Solidity & DeFi Architecture",
        "keywords": ["solidity", "defi", "web3", "evm", "smart-contract", "token", "hyperliquid", "blockchain", "crypto", "wallet"]
    },

    # Creative & Design (broken down from 127)
    "video-motion-production": {
        "title": "🎬 Video Creation & Generative Motion",
        "keywords": ["heygen", "hyperframes", "opuscar", "remotion", "video", "cinema", "motion-graphic"]
    },
    "graphics-branding-design": {
        "title": "🎨 Visual Design, Branding & Graphics",
        "keywords": ["figma", "canvas", "logo", "thumbnail", "canva", "banner", "branding", "book-cover", "character-design"]
    },
    "3d-web-threejs": {
        "title": "🧊 3D Web Experiences & Three.js",
        "keywords": ["3d-web", "three.js", "threejs", "webgl", "spline", "r3f", "shader"]
    },
    "diagrams-technical-visuals": {
        "title": "📊 Technical Diagrams & Isometric SVG",
        "keywords": ["diagram", "anatomy", "isometric", "svg", "visual-architecture", "chart", "d3js"]
    },
    "audio-voice-sound": {
        "title": "🎙️ Audio, Voice Cloning & Sound Design",
        "keywords": ["audio", "speech", "voice", "sound", "elevenlabs", "podcast", "stt", "tts", "music"]
    },

    # Business (broken down from 192)
    "business-finance-accounting": {
        "title": "💰 Financial Modeling, Tax & Accounting",
        "keywords": ["finance", "accounting", "tax", "payroll", "invoice", "balance sheet", "cash flow", "openpyxl", "excel", "statement", "revenue"]
    },
    "business-sales-crm": {
        "title": "📈 Sales Outreach, Leads & CRM",
        "keywords": ["sales", "crm", "lead", "prospect", "outreach", "customer", "deal", "pipeline", "apollo", "enrich"]
    },
    "business-strategy-legal": {
        "title": "📋 Business Strategy, Legal & HR",
        "keywords": ["contract", "nda", "legal", "hiring", "interview", "onboarding", "product-strategy", "prd", "roadmap", "pricing"]
    },

    # Productivity (27)
    "productivity-workspace-tools": {
        "title": "🚀 Productivity, Slack, Notion & Linear",
        "keywords": ["notion", "slack", "linear", "jira", "schedule", "calendar", "standup", "briefing", "meeting", "task-management"]
    },

    # Academic & Science (broken down from 189)
    "academic-writing-publishing": {
        "title": "📚 Academic Writing, Research & Literature",
        "keywords": ["academic-paper", "paper", "literature", "citation", "peer-review", "abstract", "academic-pipeline", "scholar"]
    },
    "scientific-bio-data": {
        "title": "🔬 Scientific, Bio-Informatics & Astrophysics",
        "keywords": ["astrophysics", "astronomy", "astropy", "fits", "physics", "kdense", "scientific", "bioinformatics", "rna-qc", "clinical", "molecular", "laboratory", "scvi"]
    },

    # Core Antigravity
    "core-antigravity-protocols": {
        "title": "⚔️ Core Antigravity Kit Protocols",
        "keywords": ["battle", "benchmark", "compaction", "owl", "antigravity", "customization"]
    }
}

print(f"Total granular categories defined: {len(GRANULAR_CATEGORIES)}")

def classify_granular(name, desc, tags=None, repo=""):
    full_text = f"{name} {desc} {' '.join(tags or [])}".lower()
    name_l = name.lower()
    repo_l = repo.lower()

    # Exact repo overrides
    if "kdense" in repo_l:
        return "scientific-bio-data"
    if "academic-research" in repo_l:
        return "academic-writing-publishing"
    if "lobehub" in repo_l:
        return "lobehub-ecosystem"
    if "hermes" in repo_l:
        if any(w in full_text for w in ["finance", "excel", "balance sheet", "income statement", "cash flow", "openpyxl"]):
            return "business-finance-accounting"
        if any(w in full_text for w in ["diagram", "svg", "draw", "sketch"]):
            return "diagrams-technical-visuals"
        return "autonomous-agents-hermes"
    if "heygen" in repo_l or "lemomo" in repo_l:
        return "video-motion-production"
    if "anatomy" in repo_l or "diagram" in repo_l:
        return "diagrams-technical-visuals"
    if "emilkowalski" in repo_l:
        return "frontend-motion-animation"
    if "ui-ux-pro-max" in repo_l:
        return "frontend-ui-components"
    if "taste" in repo_l or "impeccable" in repo_l:
        return "frontend-visual-taste"
    if "crypto-skills" in repo_l:
        return "web3-smart-contracts"
    if "browser-use" in repo_l:
        return "testing-playwright-e2e"
    if "cloudflare-security" in repo_l:
        return "security-vulnerability-audit"
    if "cloudflare-skills" in repo_l:
        return "cloudflare-edge"
    if "ponytail" in repo_l:
        return "code-quality-refactoring"
    if "antigravity-elite" in repo_l:
        return "core-antigravity-protocols"

    # Match based on keywords in taxonomy
    scores = {}
    for cat_slug, cat_data in GRANULAR_CATEGORIES.items():
        score = 0
        for kw in cat_data["keywords"]:
            if word_match(kw, full_text):
                score += 3
            elif kw in full_text:
                score += 1
        if score > 0:
            scores[cat_slug] = score

    if scores:
        return max(scores.items(), key=lambda x: x[1])[0]

    # Defaults
    if "test" in full_text:
        return "testing-unit-tdd"
    if "security" in full_text:
        return "security-vulnerability-audit"
    if "ui" in full_text or "component" in full_text:
        return "frontend-ui-components"
    if "api" in full_text:
        return "backend-api-design"
    if "data" in full_text:
        return "data-engineering-ml"
        
    return "code-quality-refactoring"


def inject_category(file_path, category):
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
    except Exception:
        return False

    if not content.startswith("---"):
        new_content = f"---\ncategory: {category}\n---\n\n" + content
    else:
        parts = content.split("---", 2)
        if len(parts) >= 3:
            fm = parts[1]
            body = parts[2]
            if re.search(r"^category:\s*", fm, re.MULTILINE):
                fm = re.sub(r"^category:\s*.*$", f"category: {category}", fm, flags=re.MULTILINE)
            else:
                fm = fm.rstrip() + f"\ncategory: {category}\n"
            new_content = "---" + fm + "---" + body
        else:
            return False

    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        return True
    except Exception:
        return False

def parse_skill_description(content):
    if not content:
        return ""
    # 1. Frontmatter multiline folded scalar: description: >- \n ...
    multi_m = re.search(r'description:\s*(?:[\|\>][\-\+]?|["\'][\|\>][\-\+]?["\'])\r?\n((?:[ \t]+[^\r\n]+(?:\r?\n|$))+)', content, re.IGNORECASE)
    if multi_m:
        lines = [l.strip() for l in multi_m.group(1).splitlines() if l.strip()]
        combined = " ".join(lines).strip()
        if combined and combined not in [".", ">", ">-", "|", "|-", '""', "''"]:
            return combined.strip('"\'')

    # 2. Frontmatter single-line
    fm_m = re.search(r'^---\r?\n([\s\S]*?)\r?\n---', content)
    if fm_m:
        fm = fm_m.group(1)
        m = re.search(r'description:\s*([^\r\n]+)', fm, re.IGNORECASE)
        if m:
            val = m.group(1).strip().strip('"\'')
            if val and val not in [">", ">-", "|", "|-", '""', "''"]:
                return val

    # 3. Markdown lead paragraph or blockquote fallback
    for line in content.splitlines()[:25]:
        line = line.strip()
        if line.startswith(">"):
            val = line.lstrip("> *").strip()
            if len(val) > 15:
                return val
        elif line and not line.startswith("#") and not line.startswith("-") and not line.startswith("---"):
            if len(line) > 15 and not line.startswith("```"):
                return line

    return ""

def rebuild_category_system(agents_dir=None):
    if not agents_dir:
        agents_dir = os.path.dirname(os.path.abspath(__file__))

    skills_dir = os.path.join(agents_dir, "skills")
    lib_dir = os.path.join(agents_dir, "library")
    cat_root = os.path.join(agents_dir, "category")
    master_index = os.path.join(lib_dir, "skills_index.json")

    os.makedirs(cat_root, exist_ok=True)

    unique_skills = {}

    active_skills_list = sorted([d for d in os.listdir(skills_dir) if os.path.isdir(os.path.join(skills_dir, d)) and not d.startswith('.')]) if os.path.exists(skills_dir) else []
    for s in active_skills_list:
        s_path = os.path.join(skills_dir, s)
        skill_md = os.path.join(s_path, "SKILL.md")
        desc = ""
        cat = "general"
        if os.path.exists(skill_md):
            try:
                with open(skill_md, "r", encoding="utf-8", errors="ignore") as f:
                    txt = f.read(3000)
                    desc = parse_skill_description(txt)
                    m2 = re.search(r"category:\s*([^\n]+)", txt)
                    if m2: cat = m2.group(1).strip()
            except Exception:
                pass
        unique_skills[s] = {
            "name": s,
            "category": cat,
            "description": desc,
            "source_dir": s_path,
            "repo": "active",
            "is_active": True
        }

    repos = sorted([d for d in os.listdir(lib_dir) if os.path.isdir(os.path.join(lib_dir, d)) and not d.startswith(".") and d != "__pycache__"]) if os.path.exists(lib_dir) else []
    for r in repos:
        r_skills = os.path.join(lib_dir, r, "skills")
        if not os.path.exists(r_skills):
            continue
        for s in os.listdir(r_skills):
            s_path = os.path.join(r_skills, s)
            if not os.path.isdir(s_path):
                continue
            if s in unique_skills:
                continue
            skill_md = os.path.join(s_path, "SKILL.md")
            desc = ""
            cat = "general"
            if os.path.exists(skill_md):
                try:
                    with open(skill_md, "r", encoding="utf-8", errors="ignore") as f:
                        txt = f.read(3000)
                        desc = parse_skill_description(txt)
                        m2 = re.search(r"category:\s*([^\n]+)", txt)
                        if m2: cat = m2.group(1).strip()
                except Exception:
                    pass
            unique_skills[s] = {
                "name": s,
                "category": cat,
                "description": desc,
                "source_dir": s_path,
                "repo": r,
                "is_active": False
            }

    for slug in GRANULAR_CATEGORIES:
        c_dir = os.path.join(cat_root, slug)
        os.makedirs(c_dir, exist_ok=True)

    skills_by_cat = {slug: [] for slug in GRANULAR_CATEGORIES}
    for s_name, item in unique_skills.items():
        chosen_cat = classify_granular(item["name"], item["description"], [item["category"]], item["repo"])
        item["granular_category"] = chosen_cat
        skills_by_cat[chosen_cat].append(item)

    for slug, meta in GRANULAR_CATEGORIES.items():
        c_dir = os.path.join(cat_root, slug)
        c_list = skills_by_cat[slug]
        c_list.sort(key=lambda x: x["name"])

        title_display = meta.get('title', slug)

        readme_content = f"""# {title_display}

> **Category**: `{slug}`  
> **Total Curated Skills**: {len(c_list)} skills  
> **Taxonomy Standard**: 38-Domain Granular AI Skills Vault

---

## 📖 Operational Playbook

### 1. 📥 How to Install / Activate
```powershell
python .agents/library/activate_skill.py activate <skill-name>
```

---

## 🗂️ Curated Skill Inventory

| Skill Name | Status | Origin Repository | Description |
| :--- | :---: | :--- | :--- |
"""
        for item in c_list:
            status_badge = "🟢 Active" if item["is_active"] else "⚪ Reserve"
            desc_clean = item["description"][:95] + "..." if len(item["description"]) > 95 else item["description"]
            desc_clean = desc_clean.replace("|", "/")
            rel_link = f"../../skills/{item['name']}" if item["is_active"] else f"../../library/{item['repo']}/skills/{item['name']}"
            readme_content += f"| [`{item['name']}`]({rel_link}) | {status_badge} | `{item['repo']}` | {desc_clean} |\n"

        with open(os.path.join(c_dir, "README.md"), "w", encoding="utf-8") as f:
            f.write(readme_content)

        c_index = []
        for item in c_list:
            c_index.append({
                "id": item["name"],
                "name": item["name"],
                "category": slug,
                "repository": item["repo"],
                "description": item["description"],
                "path": f"category/{slug}/{item['name']}"
            })
        with open(os.path.join(c_dir, "skills_index.json"), "w", encoding="utf-8") as f:
            json.dump(c_index, f, indent=2)

    # Master category/README.md
    master_cat_readme = f"""# 🗂️ AgentSkills Functional Categories Directory

> **Total Unique Skills**: {len(unique_skills)} standalone modular skills  
> **Granular Categories**: {len(GRANULAR_CATEGORIES)} specialized domain folders  
> **Architecture**: **100% Real folders & files** (No symlinks, fully portable across all operating systems).  
> **Purpose**: Cleanly categorizes all skills into focused, human-sized collections.

---

## 🧭 Functional Categories Directory ({len(GRANULAR_CATEGORIES)} Domains)

| Category Folder | Domain Title | Skills | Individual Catalog |
| :--- | :--- | :---: | :--- |
"""
    for slug, meta in sorted(GRANULAR_CATEGORIES.items(), key=lambda x: -len(skills_by_cat[x[0]])):
        cnt = len(skills_by_cat[slug])
        master_cat_readme += f"| **[`{slug}`](./{slug})** | {meta['title']} | **{cnt}** | [Open Catalog](./{slug}/README.md) |\n"

    with open(os.path.join(cat_root, "README.md"), "w", encoding="utf-8") as f:
        f.write(master_cat_readme)

    # category/categories_index.json
    cat_index_data = {
        "version": "2.0.0",
        "total_unique_skills": len(unique_skills),
        "total_categories": len(GRANULAR_CATEGORIES),
        "categories": {}
    }
    for slug, meta in GRANULAR_CATEGORIES.items():
        s_list = sorted(skills_by_cat[slug], key=lambda x: x["name"])
        cat_index_data["categories"][slug] = {
            "title": meta["title"],
            "count": len(s_list),
            "skills": [
                {
                    "name": s["name"],
                    "is_active": s["is_active"],
                    "repo": s["repo"],
                    "description": s["description"]
                }
                for s in s_list
            ]
        }
    with open(os.path.join(cat_root, "categories_index.json"), "w", encoding="utf-8") as f:
        json.dump(cat_index_data, f, indent=2, ensure_ascii=False)

    print(f"✓ Rebuilt category system: 38 categories with {len(unique_skills)} unique skills.", flush=True)

if __name__ == '__main__':
    rebuild_category_system()
