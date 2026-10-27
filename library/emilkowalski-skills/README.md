# Emil Kowalski UI Polish & Motion Craft

> **Category**: ✨ Micro-interactions, Motion Craft & Animation Design  
> **Source / Upstream URL**: [https://github.com/emilkowalski/skills](https://github.com/emilkowalski/skills)  
> **Total Skills in Reserve**: 15 skills  
> **Storage Mode**: Offline Reserve on Disk Only (0 Active Context Tokens)

---

## 📖 Operational Playbook

### 1. 📥 How to Install / Activate into Active Workspace
To activate any skill from this offline reserve into your active AI workspace (`.agents/skills/`):

#### Via Central Activator CLI (Recommended):
```powershell
python .agents/library/activate_skill.py activate animate
```

#### Via Direct Copy (PowerShell):
```powershell
Copy-Item -Recurse -Force ".agents/library/emilkowalski-skills/skills/animate" ".agents/skills/"
```

#### Via Direct Copy (Bash):
```bash
cp -r .agents/library/emilkowalski-skills/skills/animate .agents/skills/
```

---

### 2. 🔗 How to Link (Symlink / Junction)
If you want to use the skill without duplicating disk space, create a Directory Junction (Windows) or Symbolic Link (Linux/macOS):

#### Via Central Activator CLI:
```powershell
python .agents/library/activate_skill.py link animate
```

#### Manual Windows Junction:
```powershell
cmd /c mklink /J ".agents\skills\animate" ".agents\library\emilkowalski-skills\skills\animate"
```

#### Manual Linux / macOS Symlink:
```bash
ln -s "$(pwd)/.agents/library/emilkowalski-skills/skills/animate" ".agents/skills/animate"
```

---

### 3. 🔄 How to Update
To update this skill collection from its upstream source:
```powershell
# Update via master vault updater:
python .agents/update.py

# Or update this repository directly via npx skills:
npx skills add emilkowalski/skills
```

---

### 4. 🗑️ How to Remove / Deactivate
To remove an activated skill from your active workspace and return it to offline reserve:

#### Via Central Activator CLI:
```powershell
python .agents/library/activate_skill.py remove animate
```

#### Manual PowerShell:
```powershell
Remove-Item -Recurse -Force ".agents/skills/animate"
```

---

### 5. 🚚 How to Move (Migrate Between Tiers)
To move a skill between the **Active Hot Set** (`.agent/skills`), **Workspace Store** (`.agents/skills`), or **Offline Reserve** (`.agents/library`):
```powershell
python .agents/library/activate_skill.py move animate --to hot
python .agents/library/activate_skill.py move animate --to reserve
```

---

## 📑 Included Skills Catalog (15 Skills)

| Skill Name | Description |
| :--- | :--- |
| **`animate`** | Build an animation from scratch, making the decisions in the order that determines whether it feels right — should it animate at all, what purpose, wh... |
| **`animate-expo`** | Build animations in React Native and Expo, making the decisions in the order that determines whether they feel right — should it animate, which thread... |
| **`animation-performance`** | Keep web animations inside the frame budget — animate composite-only properties, keep motion off the main thread when the page is busy, and find the c... |
| **`animation-vocabulary`** | Reverse-lookup glossary that turns a vague description of a web animation or motion effect into its exact term ("the bouncy thing when a popover opens... |
| **`apple-design`** | Apple's approach to interface design and fluid, physical motion, translated for the web. Use when building or reviewing gesture-driven UI, spring anim... |
| **`ask-sonner`** | Guide to Sonner, the React toast library — install and wire up the Toaster, pick the right toast() call, promise and loading toasts, updating, dismiss... |
| **`break-ui`** | Try to break a piece of UI by feeding it worst-case data — long names, unbreakable emails, one-letter names, missing fields, huge counts, zero items, ... |
| **`emil-design-eng`** | This skill encodes Emil Kowalski's philosophy on UI polish, component design, animation decisions, and the invisible details that make software feel g... |
| **`find-animation-opportunities`** | Search a codebase or UI for places that don't animate but should, and reject everything that shouldn't. Read-only; it proposes motion with exact value... |
| **`improve-animations`** | Survey a codebase's animation and motion code as a senior motion advisor, then produce a prioritized audit and self-contained implementation plans for... |
| **`mobile-native`** | Make a web app feel native on a phone — the small CSS and meta-tag fixes that separate "a website in a browser" from something that feels installed. C... |
| **`pick-ui-library`** | Pick the right library for a given frontend task from a curated, opinionated list — numbers, OTP inputs, charts, command menus, virtualization, drag a... |
| **`prototype`** | Build multiple genuinely different versions of a UI piece you describe, rendered behind a visual picker so you can flip through them live and promote ... |
| **`review-animations`** | Reviews animation and motion code against a high craft bar derived from Emil Kowalski's design engineering philosophy. Default to flagging; approval i... |
| **`write-swift`** | How to write modern Swift well — modeling with value types, Swift 6 data-race safety and approachable concurrency (@concurrent, main-actor-by-default,... |
