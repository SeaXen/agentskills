# Cloudflare Edge, Workers & Wrangler

> **Category**: ☁️ Cloudflare Workers, D1 & Next.js on Edge  
> **Source / Upstream URL**: [https://github.com/cloudflare/skills](https://github.com/cloudflare/skills)  
> **Total Skills in Reserve**: 4 skills  
> **Storage Mode**: Offline Reserve on Disk Only (0 Active Context Tokens)

---

## 📖 Operational Playbook

### 1. 📥 How to Install / Activate into Active Workspace
To activate any skill from this offline reserve into your active AI workspace (`.agents/skills/`):

#### Via Central Activator CLI (Recommended):
```powershell
python .agents/library/activate_skill.py activate cloudflare
```

#### Via Direct Copy (PowerShell):
```powershell
Copy-Item -Recurse -Force ".agents/library/cloudflare-skills/skills/cloudflare" ".agents/skills/"
```

#### Via Direct Copy (Bash):
```bash
cp -r .agents/library/cloudflare-skills/skills/cloudflare .agents/skills/
```

---

### 2. 🔗 How to Link (Symlink / Junction)
If you want to use the skill without duplicating disk space, create a Directory Junction (Windows) or Symbolic Link (Linux/macOS):

#### Via Central Activator CLI:
```powershell
python .agents/library/activate_skill.py link cloudflare
```

#### Manual Windows Junction:
```powershell
cmd /c mklink /J ".agents\skills\cloudflare" ".agents\library\cloudflare-skills\skills\cloudflare"
```

#### Manual Linux / macOS Symlink:
```bash
ln -s "$(pwd)/.agents/library/cloudflare-skills/skills/cloudflare" ".agents/skills/cloudflare"
```

---

### 3. 🔄 How to Update
To update this skill collection from its upstream source:
```powershell
# Update via master vault updater:
python .agents/update.py

# Or update this repository directly via npx skills:
npx skills add cloudflare/skills
```

---

### 4. 🗑️ How to Remove / Deactivate
To remove an activated skill from your active workspace and return it to offline reserve:

#### Via Central Activator CLI:
```powershell
python .agents/library/activate_skill.py remove cloudflare
```

#### Manual PowerShell:
```powershell
Remove-Item -Recurse -Force ".agents/skills/cloudflare"
```

---

### 5. 🚚 How to Move (Migrate Between Tiers)
To move a skill between the **Active Hot Set** (`.agent/skills`), **Workspace Store** (`.agents/skills`), or **Offline Reserve** (`.agents/library`):
```powershell
python .agents/library/activate_skill.py move cloudflare --to hot
python .agents/library/activate_skill.py move cloudflare --to reserve
```

---

## 📑 Included Skills Catalog (4 Skills)

| Skill Name | Description |
| :--- | :--- |
| **`cloudflare`** | Discover and choose Cloudflare products for apps, APIs, AI agents, storage, networking, and security. Use for architecture and product selection, incl... |
| **`nextjs-on-cloudflare`** | Build, migrate, and deploy Next.js apps on Cloudflare Workers with vinext. Use when starting a Next.js project on Cloudflare, moving an existing app t... |
| **`workers-best-practices`** | Cloudflare Workers best practices for production applications. Use when writing, reviewing, or configuring Workers. |
| **`wrangler`** | Run or troubleshoot Wrangler CLI commands in projects that have a wrangler.jsonc, wrangler.json, or wrangler.toml file, including local development, P... |
