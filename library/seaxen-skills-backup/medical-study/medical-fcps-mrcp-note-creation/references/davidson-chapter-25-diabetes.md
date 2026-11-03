# Davidson Chapter 25: Endocrinology and Diabetes - Diabetes Mellitus Section

## Chapter Overview
- **Part**: Part 3: Clinical Medicine
- **Chapter**: Chapter 25: Endocrinology and Diabetes
- **Focus**: Diabetes Mellitus section (other endocrine topics in separate Endocrinology MOC)
- **Edition**: Davidson Medicine 25th Edition

## Hierarchy Structure

### Heading Hubs (12)
1. Classification and Diagnosis of Diabetes Mellitus
2. Pathophysiology of Diabetes
3. Type 1 Diabetes Mellitus
4. Type 2 Diabetes Mellitus
5. Diabetic Emergencies
6. Microvascular Complications
7. Macrovascular Complications
8. Diabetes in Special Populations
9. Diabetes Technology and Digital Health
10. Monogenic and Atypical Diabetes
11. Secondary Diabetes
12. Diabetes Prevention and Remission
13. Diabetes Monitoring and Quality of Care

### Topic-Group Hubs (38)
Total: 38 topic-group hubs across the 12 heading hubs

### Disease-Level Topics (105)
Total: 105 disease-level topics across all topic-groups

## Section Directories (13)
1. Classification and Diagnosis of Diabetes Mellitus
2. Pathophysiology of Diabetes
3. Type 1 Diabetes Mellitus
4. Type 2 Diabetes Mellitus
5. Diabetic Emergencies
6. Microvascular Complications
7. Macrovascular Complications
8. Diabetes in Special Populations
9. Diabetes Technology and Digital Health
10. Monogenic and Atypical Diabetes
11. Secondary Diabetes
12. Diabetes Prevention and Remission
13. Diabetes Monitoring and Quality of Care

## Template
- **File**: `/mnt/tb/Medicine/Templates/Diabetes Topic Template.md`
- **Features**: Diabetes-specific sections including staging tables (DKA, HbA1c, KDIGO), scoring systems (ETDRS, IWGDF, Wagner/UT), management algorithms (ADA/EASD, insulin regimens), diagnostic criteria (FPG, OGTT, HbA1c), eGFR dosing tables

## Priority FCPS/MRCP Topics (High-Yield)

### Diabetic Emergencies
- DKA: diagnostic criteria, severity grading, management protocol, cerebral oedema, euglycaemic DKA
- HHS: diagnostic criteria, differentiation from DKA, management, mortality predictors
- Hypoglycaemia: classification (Level 1/2/3), glucagon dosing, unawareness reversal

### Diagnosis & Classification
- Diabetes diagnostic criteria (FPG, HbA1c, OGTT, random)
- Impaired fasting glucose (IFG) vs IGT vs increased HbA1c
- Type 1 vs Type 2 vs LADA vs MONOGENIC vs SECONDARY diabetes

### Pharmacotherapy
- Metformin: mechanism, renal dosing, B12, lactic acidosis
- Sulfonylureas: gliclazide MR preferred, CAROLINA trial
- DPP-4 inhibitors: linagliptin (no renal adjust), saxagliptin HF risk
- SGLT2 inhibitors: CV/HF/CKD benefits, eGFR thresholds, euglycaemic DKA
- GLP-1 RAs: CV benefit, weight loss, titration, retinopathy (semaglutide)
- Tirzepatide: dual GIP/GLP-1, SURPASS/SURMOUNT, superior to semaglutide
- ADA/EASD 2023+ algorithm: comorbidity-first approach

### Microvascular Complications
- Diabetic retinopathy: ETDRS grading, 4:2:1 rule, anti-VEGF for DMO
- DKD: KDIGO staging (G1-5 x A1-3), ACEi/ARB -> SGLT2i -> finerenone -> GLP-1 RA
- Diabetic neuropathy: DSPN, autonomic, screening (monofilament, vibration, ANNS)
- Diabetic foot: IWGDF risk 0-3, Wagner/UT classification, TCC offloading

### Macrovascular Complications
- ASCVD: CV risk equivalent, QRISK3/ASCVD, statin intensity, aspirin
- Heart failure: SGLT2i in HFrEF/HFpEF (DAPA-HF, DELIVER, EMPEROR)
- PAD: ABI screening, critical limb ischaemia
- Stroke in diabetes

### Special Populations
- GDM: IADPSG universal vs NICE risk-based, targets, postpartum
- Pre-existing diabetes in pregnancy: folic acid 5mg, pre-conception HbA1c
- Elderly: frailty-guided HbA1c targets, deintensification
- CKD/Dialysis: HbA1c pitfalls, drug dosing, dialysis glucose
- HIV: ART metabolic syndrome, protease inhibitor effects

### Technology
- CGM: rtCGM vs isCGM, TIR/TBR/TAR/GMI/CV targets, trend arrows
- Insulin pumps: CSII, AID systems (780G, Control-IQ, Omnipod 5, CamAPS)

### Monogenic/Atypical
- MODY: GCK (no treatment), HNF1A (SU responsive), HNF4A
- Neonatal diabetes: KCNJ11/ABCC8, sulfonylurea response
- Mitochondrial: m.3243A>G (MELAS/MIDD)
- Wolfram: DIDMOAD
- Lipodystrophy: metreleptin

### Secondary Diabetes
- Type 3c: chronic pancreatitis, pancreatic cancer, post-pancreatectomy
- Endocrine: Cushing, acromegaly, thyrotoxicosis, phaeochromocytoma, glucagonoma
- Drug-induced: steroids, antipsychotics, CNI, ICI, protease inhibitors, thiazides/β-blockers

### Prevention/Remission
- T1D: teplizumab (stage 2 delay), immunotherapy trials
- T2D prevention: DPP (lifestyle 58%, metformin 31%), Da Qing, Finnish DPS
- T2D remission: DiRECT trial, low-calorie diet, remission criteria (HbA1c<48 off meds x3mo)

### Monitoring
- Glycaemic targets: individualized HbA1c, TIR, SMBG frequency
- Annual review: 9 care processes (HbA1c, BP, lipids, retinal, foot, ACR, eGFR, BMI, smoking)
- Structured education: DAFNE (T1), DESMOND/X-PERT (T2)
- Psychosocial: diabetes distress, depression, eating disorders/diabulimia

## Batch Processing Notes
- **Batch size**: 10 notes per session (user preference)
- **Total disease-level**: 105 topics
- **Verification**: `search_files pattern="status: full-fcps-mrcp-note" target=content path="/mnt/tb/Medicine/Diabetes"`
- **Git commit**: After each batch with descriptive message
- **MOC update**: Increment completion counters in `Diabetes MOC.md`

## Directory Creation Pattern
```bash
mkdir -p "/mnt/tb/Medicine/Diabetes/Classification and Diagnosis of Diabetes Mellitus"
mkdir -p "/mnt/tb/Medicine/Diabetes/Pathophysiology of Diabetes"
mkdir -p "/mnt/tb/Medicine/Diabetes/Type 1 Diabetes Mellitus"
mkdir -p "/mnt/tb/Medicine/Diabetes/Type 2 Diabetes Mellitus"
mkdir -p "/mnt/tb/Medicine/Diabetes/Diabetic Emergencies"
mkdir -p "/mnt/tb/Medicine/Diabetes/Microvascular Complications"
mkdir -p "/mnt/tb/Medicine/Diabetes/Macrovascular Complications"
mkdir -p "/mnt/tb/Medicine/Diabetes/Diabetes in Special Populations"
mkdir -p "/mnt/tb/Medicine/Diabetes/Diabetes Technology and Digital Health"
mkdir -p "/mnt/tb/Medicine/Diabetes/Monogenic and Atypical Diabetes"
mkdir -p "/mnt/tb/Medicine/Diabetes/Secondary Diabetes"
mkdir -p "/mnt/tb/Medicine/Diabetes/Diabetes Prevention and Remission"
mkdir -p "/mnt/tb/Medicine/Diabetes/Diabetes Monitoring and Quality of Care"
```

## Completed Topics (Tracking)
Target: 105 disease-level topics at `status: full-fcps-mrcp-note`

### Session 2026-06-14 Progress
- **Full notes before session**: ~152
- **Full notes completed this session**: 30
- **Current total full notes**: 181 (includes some hub files; leaf disease topics verified separately)
- **Remaining leaf scaffold topics**: 52

### High-Yield Topics Completed This Batch (30)
**Diabetes Technology & Digital Health (6):**
- CGM metrics (TIR, TBR, TAR, GMI, CV)
- CGM-guided insulin adjustment
- rtCGM vs isCGM
- Pump types (tethered, patch, closed-loop)
- Hybrid closed-loop (670G, 780G, CamAPS, Loop)
- Automated insulin delivery (AID) systems

**Diabetes Monitoring & Quality of Care (4):**
- Psychosocial aspects
- Diabetes education & structured education
- Annual review & complication screening (9 care processes)
- Glycaemic targets (individualised HbA1c, CGM targets)

**Special Populations - Pregnancy (4):**
- GDM management (diet, metformin, insulin)
- GDM screening (IADPSG, NICE, ADA)
- Pre-existing diabetes in pregnancy (T1DM, T2DM)
- Postpartum follow-up & future risk

**Special Populations - Elderly/CKD/HIV (3):**
- Frailty & individualised HbA1c targets
- Diabetes in CKD & dialysis
- Diabetes in HIV

**Macrovascular Complications (5):**
- ASCVD risk calculators (QRISK3, ASCVD Pooled Cohort)
- Aspirin primary prevention (ASCEND, ASPREE, ARRIVE)
- BP targets (NICE, ADA, ESC)
- Statin therapy (intensity, targets, add-on)
- Diabetes as CV risk equivalent

**Classification & Diagnosis (6):**
- Impaired fasting glucose (IFG)
- Impaired glucose tolerance (IGT)
- Increased HbA1c risk category
- Random glucose with symptoms
- GDM epidemiology
- T1DM/T2DM/Monogenic/Secondary diabetes epidemiology

### Remaining High-Yield Scaffold Topics (52)
**Diabetic Foot (6):** DFU classification (Wagner/UT), Foot risk classification (IWGDF), DFU management, Charcot neuroarthropathy, Amputation prevention MDT
**Nephropathy (6):** KDIGO staging, GFR categories (G1-G5), Albuminuria categories (A1-A3), DKD management, Diabetic nephropathy vs other
**Retinopathy (6):** NPDR, PDR, DMO, Screening/grading (ETDRS), Treatment (laser/anti-VEGF)
**Neuropathy (5):** DSPN, Autonomic, Mononeuropathies, Pain management, Screening
**HF in Diabetes (3):** HFrEF/HFpEF, SGLT2i in HF, GLP-1 RA in HF
**PAD (2):** Critical limb ischaemia, ABI screening
**T1DM (2):** Hypoglycaemia unawareness, ZnT8 autoantibodies
**T2DM Pharmacotherapy (9):** Basal/bolus insulin, Concentrated/premixed insulin, Medical nutrition, Physical activity, Weight management, Bariatric surgery, Alpha-glucosidase inhibitors, Meglitinides, TZDs
**Treatment algorithms (3):** CKD/HF guided, CVOT guided, NICE NG28
**Monogenic (2):** Lipodystrophy, Wolfram
**DKA/HHS (4):** Cerebral oedema, Euglycaemic DKA (SGLT2i), HHS mortality/prognosis, HHS vs DKA
**GDM (1):** Main GDM topic
**Hypoglycaemia (1):** Hospital/insulin error