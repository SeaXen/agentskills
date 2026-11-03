# Medical Exam Note Creation - References Index

## Structure
```
medical-exam-note-creation/
├── SKILL.md
├── references/
│   ├── medical-mnemonics.md          # Comprehensive mnemonics bank (all specialties)
│   └── hepatology-scoring-systems.md # Hepatology-specific algorithms & scoring
├── templates/
│   └── hepatology-topic-template.md  # Hepatology-specific note template
└── scripts/                          # For future automation scripts
```

## Quick Reference

### Main Skill: `medical-exam-note-creation`
- **Purpose**: Create FCPS/MRCP exam-ready medical notes using Davidson Chapter template
- **Covers**: Hepatology, Cardiology, Neurology, Respiratory, Oncology, etc.
- **Template**: 13 mandatory sections per note
- **Workflow**: Hierarchy review → Existing files check → Batch creation → Verification

### Key Files Added This Session

| File | Purpose |
|------|---------|
| `templates/hepatology-topic-template.md` | Hepatology-specific note template with all 13 sections |
| `references/medical-mnemonics.md` | 200+ mnemonics across all specialties (hepatology, cardiology, neurology, etc.) |
| `references/hepatology-scoring-systems.md` | 2000+ lines of hepatology algorithms: Child-Pugh, MELD, Maddrey, GAHS, ABIC, Lille, FIB-4, NFS, FibroScan, LI-RADS, BCLC, ALF/ACLF, HRS, HPS/PoPH, Wilson, Haemochromatosis, TIPS, transplant, HCC, etc. |

### Usage
```bash
# Load skill
skill: medical-exam-note-creation

# Access templates
skill: medical-exam-note-creation (templates/hepatology-topic-template.md)

# Access references
skill: medical-exam-note-creation (references/hepatology-scoring-systems.md)
skill: medical-exam-note-creation (references/medical-mnemonics.md)
```

### Next Session: Cardiology Chapter
When starting Cardiology (Chapter 16), the skill will provide:
- Cardiology-specific template (to be created)
- Cardiology scoring systems: GRACE, TIMI, CHA2DS2-VASc, HAS-BLED, CHADS2, ABCD2
- Cardiology algorithms: ACS pathway, HF management, AF rate/rhythm control