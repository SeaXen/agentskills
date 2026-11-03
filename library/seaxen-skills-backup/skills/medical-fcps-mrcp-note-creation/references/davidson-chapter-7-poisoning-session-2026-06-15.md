# Davidson Chapter 7: Poisoning (24th Edition) — Session 2026-06-15

## Chapter Overview
- **Chapter**: 7 (Part 2: Emergency and Critical Care Medicine)
- **Total topics completed**: 36 disease-level topics
- **Structure**: 1 MOC + 1 Hierarchy + 36 content files
- **Build state**: Full chapter coverage achieved

## Domain Coverage (36 topics)

| Domain | Topics |
|--------|--------|
| General Principles | 1 (General Principles of Poisoning Management) |
| Toxidromes (5) | Cholinergic, Anticholinergic, Sympathomimetic, Sedative-Hypnotic, Opioid |
| Analgesics (3) | Paracetamol, Salicylate, NSAID |
| Antidepressants/Psychotropic (4) | TCA, SSRI/SNRI + Serotonin Syndrome, Lithium, Antipsychotic/NMS |
| Cardiovascular Drugs (5) | Beta-Blocker, Calcium Channel Blocker, Digoxin, Antiarrhythmic, Antihypertensive |
| Sedatives (4) | Benzodiazepine, Barbiturate, Z-Drug, Alcohol (referenced to toxic alcohol notes) |
| Toxic Alcohols (3) | Methanol, Ethylene Glycol, Isopropyl Alcohol |
| Environmental (5) | CO, Cyanide, H₂S, Organophosphate (in cholinergic), Heavy Metals |
| Other Specific (6) | Iron, Cocaine/Amphetamine, Cannabis/Synthetic, Mushroom, Corrosive, Hydrocarbon |
| Antidotes/Decontamination (3) | Antidotes Overview, GI Decontamination, Enhanced Elimination |

## Key Clinical Topics & High-Yield Points
- **Paracetamol**: Rumack-Matthew nomogram, SNAP 2-bag NAC, staggered ingestion
- **Salicylate**: Respiratory alkalosis + metabolic acidosis, urine alkalinization (pH 7.5-8), dialysis pH<7.2
- **TCA**: QRS>100ms → NaHCO₃, **NO phenytoin/flumazenil/Class Ia/Ic**
- **Beta-Blocker**: Glucagon + HIET, **NO calcium/pacing/atropine**
- **Calcium Channel Blocker**: CaCl₂ 1g IV + HIET, **WBI for SR**, **NO atropine/pacing**
- **Digoxin**: **Fab 10-20 vials**, **HyperK = Fab FIRST (not Ca/insulin)**
- **Benzodiazepine**: **Flumazenil CONTRAINDICATED**: TCA, seizure hx, chronic use, head injury
- **CO**: 100% O₂ half-life 30min, HBO: COHb>25%, LOC, cardiac, preg>15%, neuro
- **Cyanide**: Hydroxocobalamin 5g (safe in CO), **NO nitrites in fire/CO**
- **Iron**: Elemental dose (sulfate 20%, fumarate 33%), deferoxamine 15mg/kg/hr, vin rosé urine, WBI
- **Methanol/EG**: Fomepizole 15→10mg/kg q12h, folinic acid, dialysis pH<7.3/visual/renal
- **Isopropyl Alcohol**: Ketosis WITHOUT acidosis, hemorrhagic gastritis, **NO fomepizole/dialysis**

## Workflow Applied
1. Created chapter directory `/mnt/tb/Medicine/Chapter 7 - Poisoning/`
2. Created hierarchy file and MOC first
3. Created all 36 topic files with full FCPS/MRCP template (14 sections)
4. Each file includes: mermaid flowcharts, tables, viva questions (8-12), mnemonics, mind maps, revision cards, spaced repetition trackers, self-test scorecards, exam answer modes
5. Updated MOC with links to all 36 files + study tracker (36/36 scaffolded)
6. Updated Davidson Chapter Roadmap with Chapter 7 entry
7. Verification: `search_files pattern: "status: full-fcps-mrcp-note" target: content path: "/mnt/tb/Medicine/Chapter 7 - Poisoning/"` → 36 files

## Stream Timeout Prevention
- Individual `write_file` calls per note (never batched in `execute_code`)
- Large notes (>200 lines) split into chunks via separate `write_file` calls
- Practical limit: 5-10 notes per session

## Template
- Uses `/mnt/tb/Medicine/Templates/Poisoning Topic Template.md` (standard 14-section FCPS/MRCP template)

## Verification Commands
```bash
# Count completed disease-level notes
search_files pattern="status: full-fcps-mrcp-note" target=content path="/mnt/tb/Medicine/Chapter 7 - Poisoning"

# Total files
find /mnt/tb/Medicine/Chapter\ 7\ -\ Poisoning -name "*.md" -type f | wc -l
# Expected: 38 (36 content + MOC + Hierarchy)
```