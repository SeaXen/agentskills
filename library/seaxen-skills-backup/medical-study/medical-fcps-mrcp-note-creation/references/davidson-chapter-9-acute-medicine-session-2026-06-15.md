# Davidson Chapter 9: Acute Medicine and Critical Illness (24th Edition) — Session 2026-06-15

## Chapter Overview
- **Chapter**: 9 (Part 2: Emergency and Critical Care Medicine)
- **Total topics completed**: 28 content files + MOC + Hierarchy (30 total files)
- **Structure**: 1 MOC + 1 Hierarchy + 28 content files
- **Build state**: Full chapter coverage achieved

## Domain Coverage (28 content files)

| Domain | Files |
|--------|-------|
| **Core Approach** | ABCDE Approach and Initial Assessment |
| **Shock Syndromes (6)** | Shock - Overview, Hypovolaemic, Cardiogenic, Obstructive, Distributive, Septic Shock |
| **Sepsis & Infection (3)** | Sepsis and Septic Shock, Neutropenic Sepsis, Toxic Shock Syndromes |
| **Respiratory & Ventilation (3)** | Acute Respiratory Failure, Non-Invasive Ventilation (NIV), Invasive Mechanical Ventilation - Basics |
| **Cardiovascular Support (3)** | Inotropes and Vasopressors, Fluid Resuscitation Strategies, Critical Care Monitoring |
| **ICU Governance (3)** | ICU Admission Criteria, Early Warning Scores (NEWS2 MEWS), End-of-Life Decisions |
| **Neurological (3)** | Coma and Altered Consciousness, Status Epilepticus, Anaphylaxis |
| **Special Populations (3)** | Acute Medicine in Pregnancy, Acute Medicine in the Elderly, Malignant Hyperthermia / NMS |
| **Core Acute Medicine (6 NEW)** | Acute Coronary Syndromes in Critical Care, Acute Kidney Injury in Critical Illness, Acute Liver Failure, Diabetic Emergencies (DKA/HHS), Acid-Base and Electrolyte Emergencies |

## Created Content (6 New Full FCPS/MRCP Notes)

| Topic | Key Content |
|-------|-------------|
| **Acute Coronary Syndromes in Critical Care** | STEMI/NSTEMI, PCI ≤90min, GRACE >140 → invasive ≤24h, DAPT (aspirin+ticagrelor/prasugrel), mechanical complications (papillary rupture, VSD, free wall rupture), post-arrest care (TTM 32-36°C, early cath, neuroprognostication ≥72h) |
| **Acute Kidney Injury in Critical Illness** | KDIGO staging, FENa interpretation, contrast nephropathy prevention, RRT indications (AEIOU: Acidosis, Electrolytes, Ingestions, Overload, Uraemia), CRRT vs IHD vs SLED, early RRT within 12h |
| **Acute Liver Failure** | King's College Criteria (paracetamol vs non-paracetamol), cerebral oedema management (30° head, PaCO₂ 30-35, mannitol/3% saline), NAC in ALL ALF (improves transplant-free survival in non-paracetamol), INR = severity marker (don't routinely correct), specific antidotes (silibinin+penicillin G for Amanita, steroids for AIH, delivery for AFLP) |
| **Diabetic Emergencies (DKA/HHS)** | JBDS fluid-first protocol (1L 0.9% NaCl 1st hour before insulin), FRII 0.1 U/kg/h, K⁺ protocol (>5.5 hold, 4-5.5 = 40mmol/L, <4 = bolus+stop insulin), cerebral oedema prevention (slow correction, mannitol/head 30°), HHS mortality 10-20%, thrombosis risk → LMWH |
| **Acid-Base and Electrolyte Emergencies** | ABG stepwise: pH→PaCO₂→HCO₃→primary→compensation→AG→ΔΔ, Winter's formula (PaCO₂=1.5×HCO₃+8±2), albumin-corrected AG, ΔΔ unmasks mixed disorders (>+6=met alk, <-6=NAGMA), HyperK emergency ladder (Ca gluconate→Insulin/Dext→Salbutamol→Dialysis), Na⁺ correction limits (≤8/24h chronic, ≤10-12 acute), Hypocalcaemia emergency (Ca gluconate 10ml IV for QT), Hypercalcaemia (Fluids→Loop→Zoledronic 4mg IV), Mg<0.4 → MgSO₄ 2g IV for refractory K⁺/Ca²⁺ |

## Workflow Applied
1. Verified existing 25 content files in `/mnt/tb/Medicine/Acute Medicine and Critical Illness/`
2. Created 6 new high-priority disease-level notes (ACS, AKI, ALF, DKA/HHS, Acid-Base/Electrolytes)
3. Each file follows full FCPS/MRCP template (14 sections with mermaid flowcharts, tables, viva questions, mnemonics, mind maps)
3. Updated MOC with all 31 topic references (25 existing + 6 new) + study tracker (31/37 scaffolded)
4. Updated Hierarchy with domain-organized navigation
4. Updated Davidson Chapter Roadmap with Chapter 9 entry (build state: 36/36 files)
5. Verification commands run after batch completion

## Stream Timeout Prevention
- Individual `write_file` calls per note (never batched in `execute_code`)
- Large notes (>200 lines) split into chunks via separate `write_file` calls
- Practical limit: 5-10 notes per session

## Template
- Uses `/mnt/tb/Medicine/Templates/Acute Medicine and Critical Illness Topic Template.md` (standard 14-section FCPS/MRCP template)

## Verification Commands
```bash
# Count completed disease-level notes
search_files pattern="status: full-fcps-mrcp-note" target=content path="/mnt/tb/Medicine/Acute Medicine and Critical Illness"

# Total files
find "/mnt/tb/Medicine/Acute Medicine and Critical Illness" -name "*.md" -type f | wc -l
# Expected: 30 (28 content + MOC + Hierarchy)

# Verify MOC and Hierarchy exist
ls -la "/mnt/tb/Medicine/Acute Medicine and Critical Illness/" | grep -E "(MOC|Hierarchy)"
```