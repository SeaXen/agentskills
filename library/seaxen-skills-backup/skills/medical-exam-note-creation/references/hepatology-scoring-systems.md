# Hepatology Scoring Systems & Algorithms Reference

## Child-Pugh Score

| Parameter | 1 Point | 2 Points | 3 Points |
|-----------|---------|----------|----------|
| **Bilirubin (µmol/L)** | <34 | 34-50 | >50 |
| **Albumin (g/L)** | >35 | 28-35 | <28 |
| **INR** | <1.7 | 1.7-2.3 | >2.3 |
| **Ascites** | None | Mild/controlled | Tense/refractory |
| **Hepatic Encephalopathy** | None | Grade I-II | Grade III-IV |

| Class | Score | 1-Year Survival | 2-Year Survival |
|-------|-------|-----------------|-----------------|
| **A** | 5-6 | 100% | 85% |
| **B** | 7-9 | 80% | 60% |
| **C** | 10-15 | 45% | 35% |

---

## MELD / MELD-Na

**MELD = 3.78 × ln(bilirubin mg/dL) + 11.2 × ln(INR) + 9.57 × ln(creatinine mg/dL) + 6.43**

**MELD-Na = MELD + 1.32 × (137 - Na) - [0.033 × MELD × (137 - Na)]** (Na capped 125-137)

| Parameter | Cap |
|-----------|-----|
| **Bilirubin** | No cap |
| **INR** | No cap |
| **Creatinine** | **Capped at 4.0 mg/dL** (if on dialysis = 4.0) |
| **Sodium** | Capped 125-137 mmol/L |

| MELD Score | 3-Month Mortality | Transplant Priority |
|------------|-------------------|-------------------|
| <10 | <5% | Low |
| 10-19 | 6-20% | Moderate |
| 20-29 | 20-50% | High |
| 30-39 | 50-75% | Very high |
| ≥40 | >75% | Urgent |

---

## Maddrey Discriminant Function (Alcoholic Hepatitis)

**DF = 4.6 × (PT - control PT in seconds) + Bilirubin (mg/dL)**

| DF Score | Severity | 30-Day Mortality | Treatment |
|----------|----------|------------------|-----------|
| **<32** | Mild/Moderate | <10% | Supportive only |
| **≥32** | **Severe** | 30-50% | **Consider corticosteroids** |

---

## Glasgow Alcoholic Hepatitis Score (GAHS)

| Parameter | Score |
|-----------|-------|
| Age >50 | 1 |
| WBC >15 ×10⁹/L | 1 |
| Urea >5 mmol/L | 1 |
| PT ratio >1.5 | 1 |
| Bilirubin >125 µmol/L | 1 |

| GAHS | 28-Day Mortality | Steroid Indication |
|------|------------------|-------------------|
| **≥9** | ~45% | **Consider steroids** |
| <9 | <15% | Supportive |

---

## ABIC Score (Age-Bilirubin-INR-Creatinine)

**ABIC = Age × 0.0039 + Bilirubin (mg/dL) × 0.031 + INR × 0.58 + Creatinine (mg/dL) × 0.47**

| ABIC | 90-Day Mortality | Steroid Indication |
|------|------------------|-------------------|
| **<6.71** | Low (<10%) | Supportive |
| **6.71-8.99** | Intermediate (30%) | **Consider steroids** |
| **≥9.0** | High (>50%) | **Strongly consider steroids** |

---

## Lille Score (Day 7 Steroid Response)

**Lille = 3.19 - 0.101 × Age + 0.147 × Albumin (g/L) + 0.0165 × Bilirubin Day 0 (mg/dL) - 0.206 × Bilirubin Day 7 (mg/dL) - 0.0065 × PT (s) - 0.0096 × Creatinine (mg/dL)**

| Lille Score | Response | Action |
|-------------|----------|--------|
| **<0.45** | **Complete/Partial responder** | **Continue steroids** ×28 days total |
| **0.45-0.56** | Partial responder | Consider continuing (individualised) |
| **>0.56** | **Null responder** | **Stop steroids** (futility, infection risk) |

---

## Child-Pugh vs MELD

| Feature | Child-Pugh | MELD |
|---------|------------|------|
| **Type** | Clinical + Lab (subjective ascites/HE) | Objective lab-based |
| **Use** | Clinical staging, prognosis | Transplant allocation |
| **Components** | Bilirubin, Albumin, INR, Ascites, HE | Bilirubin, INR, Creatinine, Na |
| **Caps** | None | Cr cap 4.0, Na 125-137 |

---

## Fibrosis Non-Invasive Tests

### FIB-4 (First-Line)
**FIB-4 = Age × AST / (Platelets × √ALT)**

| FIB-4 | Risk |
|-------|------|
| **<1.30** | Low risk F3-F4 |
| **1.30-2.67** | Intermediate |
| **>2.67** | High risk F3-F4 |

### NFS (NAFLD Fibrosis Score)
**NFS = Age × 0.037 + BMI × 0.094 + IFG × 0.66 + (AST/ALT) × 0.75 + Platelets × -0.007 + Albumin × -0.52**

| NFS | Risk |
|-----|------|
| **<-1.455** | Low risk |
| **-1.455 to 0.676** | Intermediate |
| **>0.676** | High risk |

### APRI
**APRI = AST/ULN / Platelets (10⁹/L) × 100**

| APRI | Interpretation |
|------|----------------|
| **<0.5** | No significant fibrosis |
| **>1.5** | Cirrhosis |

### FibroScan (VCTE) — Gold Standard Non-Invasive

| kPa | Fibrosis Stage |
|-----|----------------|
| **<8** | F0-F1 |
| **8-9** | F2 |
| **9-12** | F3 |
| **>12** | F4 (cirrhosis) |

> **XL probe if BMI >30**

### ELF Test
Commercial panel: HA + PIIINP + TIMP-1 → **Highest accuracy for F3-F4**

---

## HCC Surveillance

| Population | Interval | Modality |
|------------|----------|----------|
| **Cirrhosis (all aetiologies)** | **6-monthly** | **US ± AFP** |
| **Chronic HBV (Asian M>40, F>50; African >20; Family history)** | **6-monthly** | US ± AFP |
| **NASH F3 Fibrosis** | **12-monthly** | US ± AFP |
| **Post-SVR HCV with cirrhosis** | **6-monthly** | US ± AFP |

> **AFP cut-off**: >20 ng/mL suspicious; **>200 ng/mL + mass = HCC diagnosis** (with imaging)

---

## LI-RADS (Liver Imaging Reporting and Data System)

| Category | Definition | HCC Probability | Management |
|----------|------------|-----------------|------------|
| **LR-1** | Definitely benign | <1% | Routine surveillance |
| **LR-2** | Probably benign | <10% | Routine surveillance |
| **LR-3** | Intermediate | 10-50% | Short-interval follow-up (3-6mo) |
| **LR-4** | Probably HCC | >50% | Diagnostic; consider biopsy |
| **LR-5** | **Definitely HCC** | >95% | **Non-invasive diagnosis** (treat) |
| **LR-M** | Probably malignant, not HCC specific | — | Biopsy / MDT |
| **LR-TIV** | Tumour in vein | — | Stage IV (BCLC D) |

### Major LI-RADS Features (for LR-4/LR-5)

| Feature | LR-5 (Definite HCC) | LR-4 (Probable HCC) |
|---------|---------------------|---------------------|
| **Arterial Phase Hyperenhancement (APHE)** | Present | Present |
| **Washout (Portal Venous/Delayed)** | Present | Present or absent |
| **Capsule** | Present | Present or absent |
| **Threshold Growth** | ≥50% size increase in ≤6mo | May be present |
| **Size** | **≥10mm** | **10-19mm** (if APHE only = LR-4) |

---

## BCLC Staging & Treatment

| BCLC Stage | Criteria | Treatment Options | Median Survival |
|------------|----------|-------------------|-----------------|
| **0 (Very Early)** | Single <2cm, Child-Pugh A, PS 0 | **Ablation** (RFA/MWA) > Resection > Transplant | >5 years (>70%) |
| **A (Early)** | Single ≤5cm or ≤3 nodules ≤3cm, Child-Pugh A-B, PS 0 | **Resection** / **Transplant** (Milan) / **Ablation** | >5 years (50-70%) |
| **B (Intermediate)** | Multinodular, Child-Pugh A-B, PS 0 | **TACE** (cTACE/DEB-TACE) | 20-30 months |
| **C (Advanced)** | Vascular invasion / Extrahepatic spread / PS 1-2 | **Systemic** (Atezolizumab+Bevacizumab 1L; Sorafenib/Lenvatinib 2L) | 10-15 months |
| **D (Terminal)** | Child-Pugh C, PS 3-4 | **Best Supportive Care** | <3 months |

### Milan Criteria (Transplant Eligibility)
- **Single tumour ≤5cm** OR **≤3 nodules ≤3cm**
- **No vascular invasion / extrahepatic spread**
- **Child-Pugh A/B, PS 0**

### Up-to-Seven Criteria (Extended)
- **Number of tumours + largest diameter (cm) ≤7**

---

## HCC Treatment Modalities

| Modality | Indication | Key Details |
|----------|------------|-------------|
| **Resection** | Single tumour, Child-Pugh A, normal bilirubin, no PH (HVPG <10) | 5-yr OS 50-70%; recurrence 70% at 5yr |
| **Ablation (RFA/MWA)** | BCLC 0/A (≤3cm, ≤3 nodules), not resectable | RFA <3cm; MWA larger; 5-yr OS 40-60% |
| **Liver Transplant** | Milan Criteria (or Up-to-Seven) | 5-yr OS 70-80%; recurrence <15% |
| **TACE (cTACE/DEB-TACE)** | BCLC B (multinodular, preserved liver) | Repeat q4-12wks; median OS 20-30mo |
| **TARE (SIRT/Y-90)** | BCLC B/C, bridge to transplant, PVT | Alternative to TACE |
| **Systemic (BCLC C)** | 1L: Atezolizumab+Bevacizumab; 2L: Sorafenib/Lenvatinib | Atezo/Bev: median OS 19.2mo |

---

## ALF vs ACLF

| Feature | ALF | ACLF |
|---------|-----|------|
| **Prior Liver Disease** | **None** | **Chronic liver disease** |
| **Illness Duration** | **<26 weeks** | Acute on chronic |
| **Encephalopathy** | Any grade | Grade III/IV required |
| **Organ Failures** | Not required | **≥1 Organ failure** (CLIF-C ACLF) |

---

## King's College Criteria (ALF Transplant Referral)

### Paracetamol ALF
**Refer if ANY:**
- **Arterial pH <7.30** (after resuscitation)
- **OR ALL THREE**: PT >100s (INR >6.5) + Cr >300 µmol/L + Grade III/IV HE

### Non-Paracetamol ALF
**Refer if ANY:**
- **PT >100s (INR >6.5)**
- **OR ANY THREE**: Age <10/>40, non-A/non-B hepatitis, jaundice-HE >7d, PT >50s, bilirubin >300 µmol/L

---

## NAC Regimen (Paracetamol ALF)

| Phase | Dose | Volume | Duration |
|-------|------|--------|----------|
| **Loading** | 150 mg/kg | 200ml 5% glucose | 1 hour |
| **Phase 2** | 50 mg/kg | 500ml 5% glucose | 4 hours |
| **Phase 3** | 100 mg/kg | 1000ml 5% glucose | 16 hours |
| **Total** | **300 mg/kg** | | 21 hours |

> Continue NAC if: INR >1.3, ALT rising, encephalopathy, renal failure, or <8h post-ingestion above nomogram line

---

## CLIF-C ACLF Score

| Organ System | Failure Definition |
|--------------|--------------------|
| **Liver** | Bilirubin ≥12 mg/dL (204 µmol/L) |
| **Kidney** | Creatinine ≥2.0 mg/dL (177 µmol/L) OR RRT |
| **Brain** | **Grade III/IV HE** (West Haven) |
| **Coagulation** | INR ≥2.5 |
| **Circulation** | Vasopressors required (MAP<70) |
| **Respiration** | PaO2/FiO2 <200 or SpO2/FiO2 <214 or MV |

**ACLF Grade**: Grade 1: 1 OF; Grade 2: 2 OFs; Grade 3: ≥3 OFs

---

## ALF vs ACLF Key Differences

| Feature | ALF | ACLF |
|---------|-----|------|
| **Prior Liver Disease** | **None** | **Chronic liver disease** |
| **Illness Duration** | **<26 weeks** | Acute on chronic |
| **Encephalopathy** | Any grade | **Grade III/IV required** |
| **Organ Failures** | Not required | **≥1 Organ failure** |

---

## SBP (Spontaneous Bacterial Peritonitis)

### Diagnostic Criteria
- **PMNs ≥250/mm³** in ascitic fluid

### Treatment
- **Ceftriaxone 2g IV q12h** + **Albumin 1.5g/kg D1 + 1g/kg D3** (5-7 days)

### Prophylaxis
| Indication | Regimen |
|------------|---------|
| **Prior SBP** | Norfloxacin 400mg OD lifelong |
| **Ascitic protein <15 g/L + Child-Pugh ≥9 or renal impairment** | Norfloxacin 400mg OD |
| **Active GI bleed** | Ceftriaxone 1g IV OD ×7 days |

---

## Variceal Bleeding (TG18 Protocol)

### Acute Management
1. **Resuscitation** (airway, 2 large-bore IV, crossmatch)
2. **Terlipressin 2mg IV q4h** (or Octreotide 50mcg bolus + 50mcg/h)
3. **Ceftriaxone 1g IV OD ×7 days**
4. **Endoscopy ≤12h** → **EVL** (oesophageal) / **Glue injection** (gastric)

### Prophylaxis
| Type | Strategy |
|------|----------|
| **Primary** (no prior bleed) | Medium/large varices: **NSBB (HR 55-60) OR EVL** |
| **Secondary** (post-bleed) | **NSBB + EVL combined** (gold standard) |

### Early TIPS Indications
- Child B/C, HVPG >20, refractory bleed → **TIPS within 72h**
- HVPG target: **<12 mmHg** or **≥20% reduction**

---

## HRS (Hepatorenal Syndrome) - ICA Criteria

### HRS-AKI
**Cr ↑≥26.5 µmol/L/48h OR 1.5× baseline in 7 days** + no shock/nephrotoxins/parenchymal disease + **no response to albumin 1g/kg ×2d**

### Treatment
- **Terlipressin 2mg IV q4-6h + Albumin 20-40g/day** (max 14 days)
- **Response**: Cr ↓≥25% by Day 3 → continue; **No response Day 4 → TIPS**
- **Norepinephrine** (ICU alternative if terlipressin unavailable)

### Prevention
- **SBP**: Albumin 1.5g/kg D1 + 1g/kg D3
- **LVP >5L**: Albumin 8g/L removed

---

## HPS (Hepatopulmonary Syndrome)

### Diagnostic Triad
1. Liver disease
2. **PaO₂ <80 mmHg** (or A-a gradient ≥15mmHg)
3. **Intrapulmonary vasodilation** (contrast echo delayed bubbles 3-6 cycles)

### Hallmark
- **Platypnoea** (dyspnoea worse upright)
- **Orthodeoxia** (PaO₂ drops >5mmHg on sitting)

### Treatment
- **Liver Transplant = Curative**
- **TIPS Contraindicated** (worsens shunting)

---

## PoPH (Portopulmonary Hypertension)

### RHC Criteria
- **mPAP >25 mmHg**
- **PVR >240 dyn·s·cm⁻⁵**
- **PAWP ≤15 mmHg**
- + Portal hypertension

### Treatment
- **Vasodilators** (Epoprostenol, Bosentan, Sildenafil) → Bridge to transplant
- **Liver Transplant** if mPAP <35mmHg on vasodilators
- **TIPS Contraindicated**

---

## HPS vs PoPH

| Feature | HPS | PoPH |
|---------|-----|------|
| **Pathophysiology** | Vasodilation | Vasoconstriction |
| **PaO₂** | Low (<80) | Normal/mildly low |
| **Contrast Echo** | Delayed bubbles (3-6 cycles) | Normal/early |
| **mPAP/PVR** | Normal | ↑ |
| **Treatment** | Transplant (curative) | Vasodilators → Bridge to transplant |
| **TIPS** | Contraindicated | Contraindicated |

---

## Wilson Disease

### Leipzig Score
| Parameter | Normal | Wilson | Score |
|-----------|--------|--------|-------|
| Ceruloplasmin | 20-40 mg/dL | <20 | 2 |
| 24h Urinary Cu | <40 µg | >100 µg | 2 |
| KF Rings | Absent | Present | 2 |
| Hepatic Cu | <50 µg/g | >250 µg/g | 2 |
| ATP7B Mutations | None | 2 pathogenic | 4 |
| Neuro symptoms | None | Present | 1 |
| Coombs-neg haemolysis | No | Yes | 1 |

**≥4 = Definite Wilson**

---

## Haemochromatosis

### HFE Genotype
- **C282Y Homozygous**: 90%
- **C282Y/H63D Compound Het**: 5%

### Diagnostic Criteria
- **TSAT >45%** + **Ferritin >1000 µg/L** + **C282Y Homozygous** = 95% PPV

### Venesection
| Phase | Protocol |
|-------|----------|
| **Induction** | 500ml weekly → Ferritin <50, TSAT <50% |
| **Maintenance** | 500ml q2-4mo (Ferritin 50-100, TSAT <50%) |

---

## Alpha-1 Antitrypsin Deficiency

| Phenotype | Serum A1AT | Risk |
|-----------|------------|------|
| **PiZZ** | **<11 µmol/L** | High (liver + lung) |
| **PiSZ** | 11-20 µmol/L | Intermediate |
| **PiMZ** | ~50% | Carrier, lung risk if smoker |

### Treatment
| System | Therapy |
|--------|---------|
| **Liver** | Monitor; transplant if cirrhosis/HCC |
| **Lung** | **Augmentation: Prolastin-C 60mg/kg IV weekly** + **Smoking cessation** |

---

## Acute Porphyrias

### Urinary Markers
| Porphyria | Urine PBG | Urine ALA | Fecal Porphyrins | Photosensitivity |
|-----------|-----------|-----------|------------------|------------------|
| **AIP** | ↑↑↑ | ↑↑ | Normal | No |
| **VP** | ↑↑ | ↑ | **Proto IX, Copro III ↑** | Yes |
| **HCP** | ↑ | ↑ | **Copro III ↑** | Yes (mild) |

### Acute Attack Management
1. **Stop precipitants** (barbiturates, sulfonamides, oestrogen, valproate, rifampicin)
2. **IV Haemin 3-4 mg/kg/day IV ×4 days**
3. **IV 10% Dextrose 3-5 L/day**
4. Symptomatic: analgesia, antiemetics, β-blockers

---

## Cutaneous Porphyrias

### PCT (Porphyria Cutanea Tarda)
- **Uroporphyrin ↑↑ in urine**, blisters, fragility
- **Iron overload** common (↑ ferritin, ↑ TSAT)
- **Treatment**: Phlebotomy 500ml q2wks → ferritin 20-50 **OR** Chloroquine 125mg 2x/week

### EPP
- **Protoporphyrin ↑ in RBCs/plasma**
- **Immediate burning pain** on sun (no blisters)
- **Beta-carotene**, **Afamelanotide (SCENESSE)**

### CEP
- Severe, **Bone marrow transplant curative**

---

## Acute Attack Triggers (All Porphyrias)
**Barbiturates, Sulfonamides, Oestrogen, Valproate, Rifampicin, Fasting, Alcohol, Stress**

## Safe Drugs in Porphyria
Paracetamol, NSAIDs, most antibiotics (except sulfonamides/rifampicin), heparin, most antihypertensives

---

## Gilbert Syndrome

- **UGT1A1*28** promoter polymorphism (TA)₇/(TA)₇
- **Unconjugated hyperbilirubinaemia** (<80 µmol/L)
- **Benign**, precipitated by fasting/stress/illness
- **No treatment** needed

---

## Crigler-Najjar Syndrome

| Type | UGT1A1 Activity | Bilirubin | Treatment |
|------|----------------|-----------|-----------|
| **Type I** | 0% | >300 µmol/L | **Phototherapy lifelong → Transplant** |
| **Type II** | ~10% | 100-300 | **Phenobarbital 60-180mg/day** |

---

## Dubin-Johnson vs Rotor Syndrome

| Feature | Dubin-Johnson | Rotor |
|---------|---------------|-------|
| **Bilirubin** | Conjugated ↑ | Conjugated ↑ |
| **Liver** | **Black** (melanin) | Normal |
| **Gene** | **ABCC2/MRP2** | **SLCO1B1/1B3** |
| **Coproporphyrin** | **Copro I >80%** (ratio >3.5) | **Copro I ≈ III** (ratio ~1) |
| **BSP Test** | Retained at 90 min | Normal early, delayed late |

---

## Alpha-1 Antitrypsin Deficiency

| Phenotype | Level | Risk |
|-----------|-------|------|
| **PiZZ** | <11 µmol/L | Severe (liver + lung) |
| **PiSZ** | 11-20 µmol/L | Intermediate |
| **PiMZ** | ~50% | Carrier |

### Treatment
- **Liver**: Monitor; transplant if cirrhosis/HCC
- **Lung**: **Augmentation (Prolastin-C 60mg/kg IV weekly)** + **Smoking cessation CRITICAL**

---

## Haemochromatosis

### HFE Genotype
- **C282Y Homozygous**: 90%
- **C282Y/H63D Compound Het**: 5%

### Diagnosis
- **TSAT >45%** + **Ferritin >1000 µg/L** + **C282Y Homozygous** = 95% PPV

### Venesection
- **Induction**: 500ml weekly → Ferritin <50, TSAT <50%
- **Maintenance**: 500ml q2-4mo (Ferritin 50-100, TSAT <50%)

---

## Hemostasis Scores

### BLEEDING SCORE (ISTH)
- Epistaxis, bruising, bleeding, surgery, menorrhagia, postpartum, muscle, joint, CNS, other
- Score ≥3 (males) / ≥4 (females) = likely bleeding disorder

---

## Drug-Induced Liver Injury (DILI)

### R-Value Patterns
| Pattern | R = (ALT/ULN) ÷ (ALP/ULN) | Examples |
|---------|---------------------------|----------|
| **Hepatocellular** | R ≥5 | Paracetamol, INH, Valproate |
| **Cholestatic** | R ≤2 | Co-amoxiclav, Flucloxacillin, OCP |
| **Mixed** | 2 < R < 5 | Anti-TB, Carbamazepine |

### RUCAM (Causality Assessment)
| Score | Causality |
|-------|-----------|
| **≥8** | Highly probable |
| **6-7** | Probable |
| **3-5** | Possible |
| **1-2** | Unlikely |
| **≤0** | Excluded |

### Paracetamol Toxicity
- **Toxic**: >150 mg/kg (7.5g adult)
- **NAC**: 150mg/kg/1h → 50mg/kg/4h → 100mg/kg/16h = 300mg/kg/21h

### Anti-TB Monitoring
- Baseline LFTs → q2wks ×2mo → Monthly
- **Stop if**: ALT >3xULN (symptomatic) OR >5xULN (asymptomatic)

---

## TIPS Indications

| Indication | Details |
|----------|---------|
| **Refractory ascites** | LVP q2wks despite diuretics |
| **Recurrent variceal bleed** | Failed endoscopic/medical therapy |
| **Hepatorenal syndrome** | Failed terlipressin/albumin |
| **Hepatic hydrothorax** | Refractory to diuretics |
| **Budd-Chiari** | Failed anticoagulation |

### Contraindications
- Severe HE (Grade III/IV)
- Severe cardiopulmonary disease
- Uncontrolled sepsis
- Portal vein thrombosis (complete)
- HCC (if not transplant candidate)

---

## Liver Transplant Indications

- **MELD ≥15**
- **ALF** (King's College Criteria)
- **HCC** (Milan / Up-to-7 criteria)
- **PBC/PSC** (UDCA failure, recurrent cholangitis, unresectable CCA)
- **Wilson Disease** (ALF or decompensated cirrhosis)
- **Alpha-1 AT Deficiency** (decompensated cirrhosis)
- **Familial Amyloid Polyneuropathy**

### Contraindications
| Absolute | Relative |
|----------|----------|
| Active sepsis | Age >70 |
| Extrahepatic malignancy | Portal vein thrombosis |
| Active substance abuse (<6mo abstinence) | HIV (CD4>200, controlled) |
| Severe cardiopulmonary disease | Obesity BMI>40 |
| Uncorrectable anatomic anomaly | Severe malnutrition |
| | Active smoking |
| | Psychiatric instability |

### MELD Allocation
- **MELD = 3.78×ln(bili) + 11.2×ln(INR) + 9.57×ln(Cr) + 6.43**
- **Cr cap 4.0** (dialysis = 4.0)
- **Exception points**: HCC Milan = 22 (increases +3/3mo), HPS = 22, PoPH = 22

---

## Post-Transplant Immunosuppression

### Standard Triple Therapy
| Drug | Target Trough |
|------|---------------|
| **Tacrolimus** | 10-15 (0-1m), 8-12 (1-3m), 5-10 (3-12m), 3-7 (>12m) |
| **MMF** | 1-2g/day |
| **Prednisolone** | Taper to 5mg by 3-6mo; steroid-free by 6-12mo |

### Complications Timeline
| Period | Complications |
|--------|---------------|
| **0-30 days** | HAT, PVT, Biliary leak, ACR, Infection, Renal dysfunction |
| **1-12 months** | ACR, Chronic rejection, CMV/EBV, Biliary strictures, Recurrence |
| **>1 year** | Chronic rejection, Metabolic syndrome, Renal failure, CVD, De novo malignancy |

### Rejection
| Type | Histology | Treatment |
|------|-----------|-----------|
| **ACR** | Portal inflammation, bile duct damage, endotheliitis | Methylprednisolone 500mg-1g IV ×3d + Optimise CNI |
| **Chronic** | Ductopenia, arteriopathy, fibrosis | Optimise CNI, Switch mTOR, Retransplant if ductopenia >50% |

### Recurrent Disease
| Disease | Recurrence | Management |
|---------|------------|------------|
| **HCV** | 100% if viraemic | **DAA (SOF/VEL/GLE/PIB) → SVR >95%** |
| **HBV** | <5% (with prophylaxis) | HBIG (short-term) + TDF/ENT |
| **AIH** | 20-30% | Steroids + Azathioprine |
| **PBC** | 20-30% | UDCA 13-15mg/kg |
| **PSC** | 20-30% | ERCP dominant strictures |
| **HCC** | 10-15% (if Milan) | Resection/Ablation/TACE |
| **NASH** | 30-40% | Weight loss, Pioglitazone/GLP-1 |

---

## Immunosuppression - mTOR Inhibitors
- **Sirolimus/Everolimus**: **Recurrent HCC** (anti-tumour), **CNI nephrotoxicity**, **Renal protection**
- **Belatacept**: Experimental CNI-free (EBV+ only)

---

## CNI Nephrotoxicity
- **eGFR decline** → CNI minimise / switch to mTOR / Belatacept

---

## Malignancy Screening (Pre-Tx)
- **CT CAP** (chest/abdomen/pelvis)
- **Colonoscopy** (if >50 or risk factors)
- **Mammography** (women)
- **PSA** (men)
- **Dermatology review** (PSC)

---

## Infection Screening (Pre-Tx)
- **HBV/HIV/HCV/CMV/EBV/VZV/HSV** serology
- **TB** (Quantiferon/TST)
- **Strongyloides** (if endemic travel)

---

## Nutritional Assessment (Pre-Tx)
- **SGA/MUST**
- **Sarcopenia** (CT L3 psoas index)

---

## Psychosocial Assessment (Pre-Tx)
- Psychiatry (alcohol, mental health)
- Social work (support, housing, finances)
- Compliance history

---

## Vaccinations (Pre-Tx)
- Seasonal flu, Pneumococcal (PCV23), Hepatitis A/B
- **Live vaccines CONTRAINDICATED post-transplant**

---

## Bone Health
- **DEXA scan**, Calcium/Vit D if osteoporotic

---

*End of Hepatology Scoring & Algorithms Reference*