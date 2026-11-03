# Obsidian Medicine Vault Bootstrap

Use this when the user wants a real file-backed study vault instead of chat-only notes.

## Proven layout

```text
<root>/
├── 00_Index/
│   └── Medicine MOC.md
├── Templates/
│   ├── Generic Topic Template.md
│   ├── Nephrology Topic Template.md
│   ├── Respiratory Topic Template.md
│   └── Neurology Topic Template.md
├── Nephrology/
│   └── Nephrology MOC.md
├── Respiratory/
│   └── Respiratory MOC.md
├── Neurology/
│   └── Neurology MOC.md
├── Cardiology/
│   └── Cardiology MOC.md
├── Gastroenterology/
│   └── Gastroenterology MOC.md
├── Endocrinology/
│   └── Endocrinology MOC.md
├── Hematology/
│   └── Hematology MOC.md
├── Rheumatology/
│   └── Rheumatology MOC.md
├── Infectious Disease/
│   └── Infectious Disease MOC.md
├── README.md
└── .gitignore
```

## Obsidian conventions

- Prefer normal readable filenames like `AKI.md`, `CKD.md`, `Stroke.md`
- Use chapter-level MOC files for navigation
- Use `[[wikilinks]]` between related topics
- Add tags in frontmatter or inline (`#medicine #nephrology`)
- Use Mermaid for flowcharts and mind maps when helpful
- Keep notes graph-view friendly by linking disease, investigation, physiology, and management notes

## Git/GitHub workflow

1. Initialize git in the vault root
2. Make an initial commit after creating the folder structure and starter notes
3. If `gh` is missing on Debian-like systems, install it with:
   ```bash
   sudo apt-get update && sudo apt-get install -y gh
   ```
4. Authenticate with:
   ```bash
   gh auth login
   ```
5. Create/push repo:
   ```bash
   gh repo create <owner>/<repo> --public --source . --remote origin --push --description "Obsidian-friendly FCPS/MRCP medicine notes vault"
   ```

## Practical notes

- `gh auth login` may fail to open a browser on headless systems; the device-code flow still works if the user manually opens `https://github.com/login/device` and enters the code.
- After login, verify with `gh auth status`.
- If the repo already exists, add/set `origin` and push `main`.
