# Specialized Community Skills & Integrations

> **Category**: 🧩 Specialized Integrations (Playwright, Supabase, Neon, Shadcn, Caveman, Sentry, Apple)  
> **Source / Upstream URL**: [Various Open-Source Curated Repositories](Various Open-Source Curated Repositories)  
> **Total Skills in Reserve**: 20 skills  
> **Storage Mode**: Offline Reserve on Disk Only (0 Active Context Tokens)

---

## 📖 Operational Playbook

### 1. 📥 How to Install / Activate into Active Workspace
To activate any skill from this offline reserve into your active AI workspace (`.agents/skills/`):

#### Via Central Activator CLI (Recommended):
```powershell
python .agents/library/activate_skill.py activate app-production-readiness
```

#### Via Direct Copy (PowerShell):
```powershell
Copy-Item -Recurse -Force ".agents/library/specialized-community-skills/skills/app-production-readiness" ".agents/skills/"
```

#### Via Direct Copy (Bash):
```bash
cp -r .agents/library/specialized-community-skills/skills/app-production-readiness .agents/skills/
```

---

### 2. 🔗 How to Link (Symlink / Junction)
If you want to use the skill without duplicating disk space, create a Directory Junction (Windows) or Symbolic Link (Linux/macOS):

#### Via Central Activator CLI:
```powershell
python .agents/library/activate_skill.py link app-production-readiness
```

#### Manual Windows Junction:
```powershell
cmd /c mklink /J ".agents\skills\app-production-readiness" ".agents\library\specialized-community-skills\skills\app-production-readiness"
```

#### Manual Linux / macOS Symlink:
```bash
ln -s "$(pwd)/.agents/library/specialized-community-skills/skills/app-production-readiness" ".agents/skills/app-production-readiness"
```

---

### 3. 🔄 How to Update
To update this skill collection from its upstream source:
```powershell
# Update via master vault updater:
python .agents/update.py

# Or update this repository directly via npx skills:
npx skills update
```

---

### 4. 🗑️ How to Remove / Deactivate
To remove an activated skill from your active workspace and return it to offline reserve:

#### Via Central Activator CLI:
```powershell
python .agents/library/activate_skill.py remove app-production-readiness
```

#### Manual PowerShell:
```powershell
Remove-Item -Recurse -Force ".agents/skills/app-production-readiness"
```

---

### 5. 🚚 How to Move (Migrate Between Tiers)
To move a skill between the **Active Hot Set** (`.agent/skills`), **Workspace Store** (`.agents/skills`), or **Offline Reserve** (`.agents/library`):
```powershell
python .agents/library/activate_skill.py move app-production-readiness --to hot
python .agents/library/activate_skill.py move app-production-readiness --to reserve
```

---

## 📑 Included Skills Catalog (20 Skills)

| Skill Name | Description |
| :--- | :--- |
| **`app-production-readiness`** | Build portable apps (any stack - TypeScript, Python, Go, Rust) for localhost, Docker, Vercel, Netlify, Railway, Render, Fly.io, Cloudflare Free plan, ... |
| **`caveman-review`** | > Compressed code review - one line per finding with location, problem and fix. Use for /caveman-review, "review this PR", or "review the diff". |
| **`crypto-bd-agent`** | ">" Autonomous crypto business development patterns — multi-chain token discovery, 100-point scoring with wallet forensics, x402 micropayments, ERC-80... |
| **`design-mobile-apps`** | Design mobile app screens with Sleek, edit Sleek projects, and implement their designs in React Native or HTML. |
| **`design-taste-frontend`** | tasteskill v2, the anti-slop frontend skill. Art direction for websites, distilled from a study of 247 curated gallery sites (One Page Love, Awwwards ... |
| **`dev`** | Development workflows for the playwright-cli repository. Use when the user asks about rolling dependencies, releasing, or other repo maintenance tasks... |
| **`find-bugs`** | Find bugs, security vulnerabilities, and code quality issues in local branch changes. Use when asked to review changes, find bugs, security review, or... |
| **`find-skills`** | Helps users discover and install agent skills when they ask questions like "how do I do X", "find a skill for X", "is there a skill that can...", or e... |
| **`gravitas`** | > Use for software implementation, debugging, refactoring, review, migration, and other repository-changing engineering work where correctness must be... |
| **`impeccable`** | "Use when the user wants to design, redesign, shape, critique, audit, polish, simplify, harden, animate, or otherwise improve a frontend interface: we... |
| **`ios-design`** | Design and review iOS UI/UX for iPhone apps in SwiftUI, UIKit, or React Native. Use for mobile app design, screen redesigns, navigation flows, typogra... |
| **`neon`** | Overview of Neon, a complete set of cloud backend primitives around Lakebase Postgres: Auth, Object Storage, Functions, the AI Gateway, and Realtime. ... |
| **`playwright-cli`** | Automate browser interactions, test web pages and work with Playwright tests. |
| **`portable-deploy-qa`** | (Legacy alias for app-production-readiness) Build portable apps (any stack - TypeScript, Python, Go, Rust) for localhost, Docker, Vercel, Netlify, Rai... |
| **`pr`** | "Use when writing a PR body." |
| **`screenshots`** | "Generate marketing screenshots of your app using Playwright. Use when the user wants to create screenshots for Product Hunt, social media, landing pa... |
| **`shadcn`** | Manages shadcn components and projects — adding, searching, fixing, debugging, styling, and composing UI, including chat interfaces. Provides project ... |
| **`supabase`** | "Use when doing ANY task involving Supabase. Triggers: Supabase products (Database, Auth, Edge Functions, Realtime, Storage, Vectors, Cron, Queues); c... |
| **`supabase-postgres-best-practices`** | "Postgres best practices maintained by Supabase, for Postgres running anywhere. Load this skill BEFORE writing or changing anything that lives in a Po... |
| **`ui-taste`** | Give your coding agent better UI taste. Build and polish web and iOS interfaces with Uizze's anti-ui-slop playbooks and optional real-product referenc... |
