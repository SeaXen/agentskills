# Rheumatology Chapter 26 Scaffold Reference (Davidson 24th Edition)

## Chapter Overview
- **Davidson Part**: Part 3: Clinical Medicine
- **Chapter**: Chapter 26: Rheumatology and bone disease
- **Authors**: S.H. Ralston, I.B. McInnes

## Scaffold Structure

### Heading Hubs (10)
1. Clinical Approach to Musculoskeletal Disease
2. Osteoarthritis and Related Disorders
3. Inflammatory Arthritis
4. Crystal Arthropathies
5. Infectious Arthritis and Bone Infections
6. Autoimmune Rheumatic Diseases
7. Vasculitis
8. Bone Metabolic Diseases
9. Polymyalgia Rheumatica and Related Disorders
10. Soft Tissue Rheumatism and Chronic Pain Syndromes

### Topic-Group Hubs (20)
1. Clinical approach (Musculoskeletal history, GALS, Investigations, Drugs)
2. Musculoskeletal anatomy & physiology (Bone structure & remodelling)
3. Common regional musculoskeletal problems (Hand, Knee, Hip, Spine, 1st CMC OA)
4. Chronic pain syndromes and fibromyalgia
5. Rheumatoid Arthritis
6. Seronegative spondyloarthritis (AS, PsA, ReA, Enteropathic, Undifferentiated, JIA)
6. Crystal arthritis (Gout, CPPD, Basic calcium phosphate)
7. Joint and bone infections (Septic arthritis, Rheumatic fever, Osteomyelitis, Lyme, TB, Viral)
7. Connective tissue diseases (SLE, SSc, Sjögren's, MCTD, PM/DM, APS, Still's, Relapsing polychondritis)
7. Primary systemic vasculitides (GCA, Takayasu, ANCA: GPA/MPA/EGPA, PAN, Kawasaki, IgA/HSP, Behçet's, Secondary)
7. Bone metabolic disorders (Osteoporosis, Osteomalacia/rickets, Paget's, GIOP, Renal osteodystrophy, Hyperparathyroidism)
8. PMR and GCA
9. Other granulomatous conditions (Sarcoidosis, IgG4-RD)
10. Regional soft tissue rheumatism (Shoulder, Elbow, Hip, Knee, Foot)
11. Chronic pain syndromes and fibromyalgia (Fibromyalgia, CWP, CRPS)

### Disease-Level Topics (78 total)
- 8 Preserved Root-Level Core Notes (legacy, to upgrade)
- 70 Disease-Level Scaffolds (to upgrade to full notes)

### 8 Preserved Root-Level Core Notes
1. Rheumatoid Arthritis
2. Systemic Lupus Erythematosus
3. Osteoarthritis
4. Gout
5. Osteoporosis
6. Vasculitis (Primary systemic vasculitides overview)
7. Polymyalgia Rheumatica
8. Septic Arthritis

### FCPS/MRCP High-Yield Priority Topics (Must Upgrade First)
1. Clinical Approach: History, GALS, Investigations, Drugs
2. Rheumatoid Arthritis
3. Systemic Lupus Erythematosus
4. Osteoarthritis
4. Gout
5. Osteoporosis
6. Septic Arthritis
7. Polymyalgia Rheumatica / Giant Cell Arteritis
8. Vasculitis (GCA, ANCA: GPA/MPA/EGPA, PAN, Kawasaki, HSP, Behçet's)
9. Ankylosing Spondylitis / Spondyloarthritis
10. Psoriatic Arthritis
11. Crystal: CPPD, Basic Calcium Phosphate
12. Autoimmune: SSc, Sjögren's, MCTD, PM/DM, APS, Still's, Relapsing Polychondritis
13. Bone: Osteomalacia/Rickets, Paget's, GIOP, Renal Osteodystrophy, Hyperparathyroidism
14. Infectious: Rheumatic Fever, Osteomyelitis, Lyme, TB, Viral
15. Soft Tissue: Fibromyalgia, CWP, CRPS, Regional (Shoulder, Elbow, Hip, Knee, Foot)

## Scaffold File Status Conventions
- **scaffold-hub**: Hub files (heading hubs, topic-group hubs) — NOT upgraded to full notes
- **scaffold**: Disease-level placeholder files — to be upgraded to full-fcps-mrcp-note
- **scaffold-hub** topic-group hubs: 20 total (do not convert to full notes)
- **scaffold-hub** heading hubs: 10 total (do not convert to full notes)

## File Status Tracking
- **status: scaffold** = disease-level scaffold (needs upgrade)
- **status: scaffold-hub** = hub file (not for upgrade)
- **status: full-fcps-mrcp-note** = fully upgraded with all 6 mandatory sections
- **status: template** = template files

## Tracking Files
- **MOC**: Rheumatology MOC.md — tracks completed full notes with ✅
- **Hierarchy**: Davidson Chapter 26 - Rheumatology Hierarchy.md — tracks all 78 disease topics with ✅ on leaves
- **Resume**: Rheumatology Channel Session Resume 2026-06-11.md — queue and continuation prompt
- **Template**: Templates/Rheumatology Topic Template.md — standardized scaffold template

## Git Workflow for Rheumatology
```bash
# After each batch (5-10 full notes):
git add Rheumatology/<new_files> Rheumatology/Rheumatology\ MOC.md Rheumatology/Davidson\ Chapter\ 26\ -\ Rheumatology\ Hierarchy.md 00_Index/Rheumatology\ Channel\ Session\ Resume\ 2026-06-11.md
git commit -m "feat(rheumatology): add N full FCPS/MRCP notes (topic1, topic2, ...)"
git push
```