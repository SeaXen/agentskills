# UI/UX Pro Max Design System

> **Category**: 🎨 Design Reasoning, Typography & Stack Palettes  
> **Source / Upstream URL**: [https://github.com/nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)  
> **Total Skills in Reserve**: 6 skills  
> **Storage Mode**: Offline Reserve on Disk Only (0 Active Context Tokens)

---

## 📖 Operational Playbook

### 1. 📥 How to Install / Activate into Active Workspace
To activate any skill from this offline reserve into your active AI workspace (`.agents/skills/`):

#### Via Central Activator CLI (Recommended):
```powershell
python .agents/library/activate_skill.py activate banner-design
```

#### Via Direct Copy (PowerShell):
```powershell
Copy-Item -Recurse -Force ".agents/library/ui-ux-pro-max-skill/skills/banner-design" ".agents/skills/"
```

#### Via Direct Copy (Bash):
```bash
cp -r .agents/library/ui-ux-pro-max-skill/skills/banner-design .agents/skills/
```

---

### 2. 🔗 How to Link (Symlink / Junction)
If you want to use the skill without duplicating disk space, create a Directory Junction (Windows) or Symbolic Link (Linux/macOS):

#### Via Central Activator CLI:
```powershell
python .agents/library/activate_skill.py link banner-design
```

#### Manual Windows Junction:
```powershell
cmd /c mklink /J ".agents\skills\banner-design" ".agents\library\ui-ux-pro-max-skill\skills\banner-design"
```

#### Manual Linux / macOS Symlink:
```bash
ln -s "$(pwd)/.agents/library/ui-ux-pro-max-skill/skills/banner-design" ".agents/skills/banner-design"
```

---

### 3. 🔄 How to Update
To update this skill collection from its upstream source:
```powershell
# Update via master vault updater:
python .agents/update.py

# Or update this repository directly via npx skills:
npx skills add nextlevelbuilder/ui-ux-pro-max-skill
```

---

### 4. 🗑️ How to Remove / Deactivate
To remove an activated skill from your active workspace and return it to offline reserve:

#### Via Central Activator CLI:
```powershell
python .agents/library/activate_skill.py remove banner-design
```

#### Manual PowerShell:
```powershell
Remove-Item -Recurse -Force ".agents/skills/banner-design"
```

---

### 5. 🚚 How to Move (Migrate Between Tiers)
To move a skill between the **Active Hot Set** (`.agent/skills`), **Workspace Store** (`.agents/skills`), or **Offline Reserve** (`.agents/library`):
```powershell
python .agents/library/activate_skill.py move banner-design --to hot
python .agents/library/activate_skill.py move banner-design --to reserve
```

---

## 📑 Included Skills Catalog (6 Skills)

| Skill Name | Description |
| :--- | :--- |
| **`banner-design`** | "Design banners for social media, ads, website heroes, creative assets, and print. Multiple art direction options with optional generated or supplied ... |
| **`brand`** | Brand voice, visual identity, messaging frameworks, asset management, brand consistency. Activate for branded content, tone of voice, marketing assets... |
| **`design`** | "Comprehensive design skill: brand identity, design tokens, UI styling, logo generation (55 styles, Gemini, Atlas Cloud, or MuAPI AI), corporate ident... |
| **`slides`** | Create strategic HTML presentations with Chart.js, design tokens, responsive layouts, copywriting formulas, and contextual slide strategies. |
| **`ui-styling`** | Create beautiful, accessible user interfaces with shadcn/ui components (built on Radix UI + Tailwind), Tailwind CSS utility-first styling, and canvas-... |
| **`ui-ux-pro-max`** | "UI/UX design intelligence for web, mobile, and desktop. This skill should be used when designing, building, reviewing, or fixing interfaces, includin... |
