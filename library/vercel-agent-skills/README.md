# Vercel Labs React & Next.js Patterns

> **Category**: ▲ Vercel React 19, Next.js & Server Action Patterns  
> **Source / Upstream URL**: [https://github.com/vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills)  
> **Total Skills in Reserve**: 9 skills  
> **Storage Mode**: Offline Reserve on Disk Only (0 Active Context Tokens)

---

## 📖 Operational Playbook

### 1. 📥 How to Install / Activate into Active Workspace
To activate any skill from this offline reserve into your active AI workspace (`.agents/skills/`):

#### Via Central Activator CLI (Recommended):
```powershell
python .agents/library/activate_skill.py activate deploy-to-vercel
```

#### Via Direct Copy (PowerShell):
```powershell
Copy-Item -Recurse -Force ".agents/library/vercel-agent-skills/skills/deploy-to-vercel" ".agents/skills/"
```

#### Via Direct Copy (Bash):
```bash
cp -r .agents/library/vercel-agent-skills/skills/deploy-to-vercel .agents/skills/
```

---

### 2. 🔗 How to Link (Symlink / Junction)
If you want to use the skill without duplicating disk space, create a Directory Junction (Windows) or Symbolic Link (Linux/macOS):

#### Via Central Activator CLI:
```powershell
python .agents/library/activate_skill.py link deploy-to-vercel
```

#### Manual Windows Junction:
```powershell
cmd /c mklink /J ".agents\skills\deploy-to-vercel" ".agents\library\vercel-agent-skills\skills\deploy-to-vercel"
```

#### Manual Linux / macOS Symlink:
```bash
ln -s "$(pwd)/.agents/library/vercel-agent-skills/skills/deploy-to-vercel" ".agents/skills/deploy-to-vercel"
```

---

### 3. 🔄 How to Update
To update this skill collection from its upstream source:
```powershell
# Update via master vault updater:
python .agents/update.py

# Or update this repository directly via npx skills:
npx skills add vercel-labs/agent-skills
```

---

### 4. 🗑️ How to Remove / Deactivate
To remove an activated skill from your active workspace and return it to offline reserve:

#### Via Central Activator CLI:
```powershell
python .agents/library/activate_skill.py remove deploy-to-vercel
```

#### Manual PowerShell:
```powershell
Remove-Item -Recurse -Force ".agents/skills/deploy-to-vercel"
```

---

### 5. 🚚 How to Move (Migrate Between Tiers)
To move a skill between the **Active Hot Set** (`.agent/skills`), **Workspace Store** (`.agents/skills`), or **Offline Reserve** (`.agents/library`):
```powershell
python .agents/library/activate_skill.py move deploy-to-vercel --to hot
python .agents/library/activate_skill.py move deploy-to-vercel --to reserve
```

---

## 📑 Included Skills Catalog (9 Skills)

| Skill Name | Description |
| :--- | :--- |
| **`deploy-to-vercel`** | Deploy applications and websites to Vercel. Use when the user requests deployment actions like "deploy my app", "deploy and give me the link", "push t... |
| **`vercel-cli-with-tokens`** | Deploy and manage projects on Vercel using token-based authentication. Use when working with Vercel CLI using access tokens rather than interactive lo... |
| **`vercel-composition-patterns`** | React composition patterns that scale. Use when refactoring components with boolean prop proliferation, building flexible component libraries, or desi... |
| **`vercel-optimize`** | "Use for Vercel cost and performance optimization on deployed projects, especially Next.js, SvelteKit, Nuxt, and limited Astro apps. Collect Vercel me... |
| **`vercel-react-best-practices`** | React and Next.js performance optimization guidelines from Vercel Engineering. This skill should be used when writing, reviewing, or refactoring React... |
| **`vercel-react-native-skills`** | React Native and Expo best practices for building performant mobile apps. Use when building React Native components, optimizing list performance, impl... |
| **`vercel-react-view-transitions`** | Guide for implementing smooth, native-feeling animations using React's View Transition API (`<ViewTransition>` component, `addTransitionType`, and CSS... |
| **`web-design-guidelines`** | Review UI code for Web Interface Guidelines compliance. Use when asked to "review my UI", "check accessibility", "audit design", "review UX", or "chec... |
| **`writing-guidelines`** | Review docs/prose for Writing Guidelines compliance. Use when asked to "review my docs", "check writing style", "audit prose", "review docs voice and ... |
