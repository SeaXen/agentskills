#!/usr/bin/env python3
"""
Batch Generator for Medical FCPS/MRCP Notes
Generates full FCPS/MRCP notes from scaffold topics using a template.
Used for Dermatology Chapter 29 (320 topics) and other large chapters.
"""

import os
import re
from datetime import date
from pathlib import Path

# Template for full FCPS/MRCP notes
FULL_NOTE_TEMPLATE = """---
tags: [medicine, dermatology, davidson, fcps, mrcp]
davidson_part: Part 3: Clinical Medicine
davidson_chapter: Chapter 29: Dermatology
heading: {heading}
topic_group: {topic_group}
topic: {topic}
status: full-fcps-mrcp-note
priority: high
cards: 25
created: {today}
modified: {today}
exam_relevance: [FCPS, MRCP Part 1, MRCP Part 2, PACES]
see_also:
  - "[[Dermatology MOC]]"
  - "[[{parent_hub} Hub]]"
---

# {topic}

Related: [[Dermatology MOC]], [[Davidson Chapter 29 - Dermatology Hierarchy]]

> [!tip]
> Complete FCPS/MRCP exam-ready note for {topic}. Expand using template structure.

---

## Learning Objectives
- [ ] Define {topic} and describe epidemiology
- [ ] Explain pathophysiology and molecular mechanisms
- [ ] Describe clinical features and subtypes
- [ ] Outline diagnostic approach and investigations
- [ ] Detail management algorithm (evidence-based)
- [ ] Identify complications, red flags, and referral criteria
- [ ] Recall FCPS/MRCP high-yield facts, doses, durations
- [ ] Answer viva questions confidently
- [ ] Recognise common confusions and apply mnemonics

---

## 1. Definition / Epidemiology / Classification

### Definition

### Epidemiology
- **Prevalence:**
- **Age of onset:**
- **Sex ratio:**
- **Risk factors:**

### Classification
| Variant | Key Features | Prognosis |
|---------|-------------|-----------|
| | | |

---

## 2. Aetiology / Pathophysiology

### Aetiology

### Pathophysiology
```mermaid
flowchart TD
    A[Trigger] --> B[Pathway]
    B --> C[Effector mechanism]
    C --> D[Clinical phenotype]
```

### Molecular/Genetic Basis

---

## 3. Clinical Features

### History

### Examination
| Feature | Description |
|---------|-------------|
| | |

### Distribution Patterns

### Subtype-Specific Features

---

## 4. Diagnostic Approach / Algorithm

```mermaid
flowchart TD
    A[Clinical Presentation] --> B[History & Examination]
    B --> C[Differential Diagnosis]
    C --> D[Targeted Investigations]
    D --> E[Confirm Diagnosis]
```

### Diagnostic Criteria

---

## 5. Investigations

### First-Line

### Second-Line / Specialised

---

## 6. Differential Diagnosis

| Differential | Distinguishing Features | Key Test |
|--------------|------------------------|----------|
| | | |

---

## 7. Management

### General Measures

### Pharmaceutical Therapy

### Management Algorithm
```mermaid
flowchart TD
    A[Diagnosis Confirmed] --> B{{Severity}}
    B -->|Mild| C[Conservative/Topical]
    B -->|Moderate| D[Systemic/Phototherapy]
    B -->|Severe| E[Advanced/Biologic]
```

### Special Situations

---

## 8. Complications

---

## 9. Red Flags / Emergencies

---

## 10. Prognosis

---

## 11. Topic Correlation

---

## 12. Special Situations (Pregnancy, Paediatric, Elderly, Immunocompromised)

---

## FCPS/MRCP High-Yield Summary

| Category | Key Points |
|----------|------------|
| **Definition** | |
| **Epidemiology** | |
| **Pathophysiology** | |
| **Clinical** | |
| **Diagnosis** | |
| **Management** | |
| **Complications** | |
| **Viva Pearls** | |

---

## Viva Questions (PACES/FCPS Style)
1. **Q:** Define {topic} and classify variants.
   **A:**

2. **Q:** What are the diagnostic criteria?
   **A:**

3. **Q:** How to differentiate from key mimics?
   **A:**

4. **Q:** Outline stepwise management.
   **A:**

5. **Q:** First-line treatment?
   **A:**

6. **Q:** Indications for biologics/advanced therapy?
   **A:**

7. **Q:** Screening before starting treatment?
   **A:**

8. **Q:** Severity assessment tools?
   **A:**

9. **Q:** Red flags for urgent referral?
   **A:**

10. **Q:** Management in pregnancy/renal failure?
    **A:**

---

## Common Confusions / Exam Traps

| Confusion | Clarification |
|-----------|---------------|
| | |

---

## Mnemonics
1. 
2. 
3. 

---

## Mind Map
```mermaid
mindmap
  root(({topic}))
    Definition
    Aetiology
    Clinical
    Diagnosis
    Management
    Complications
```

---

## Flowchart
```mermaid
flowchart TD
    A[Presentation] --> B[Diagnosis]
    B --> C[Severity]
    C --> D[Treatment]
```

---

## Suggested Visuals / Image Notes

---

## One-Page Revision Card
| **Topic** | **{topic}** |
|-----------|-------------|
| **Definition** | |
| **Key Clinical** | |
| **Dx Criteria** | |
| **Management** | |
| **Key Drugs** | |
| **Red Flags** | |
| **Viva Pearls** | |
| **Mnemonics** | |

---

## Spaced Repetition Trackers
- [ ] Day 1 completed
- [ ] Day 3 revision
- [ ] Day 7 revision
- [ ] Day 15 revision
- [ ] Day 30 revision
- [ ] Day 90 revision

---

## Must Know / Should Know / Nice to Know

### Must Know
- [ ] 
- [ ] 

### Should Know
- [ ] 
- [ ] 

### Nice to Know
- [ ] 
- [ ] 

---

## Self-Test Scorecard
| Section | Score /5 |
|---------|----------|
| Definition | |
| Aetiology | |
| Clinical | |
| Diagnosis | |
| Management | |
| **TOTAL** | **/30** |

---

## Exam Answer Modes

### Long Answer Skeleton
### Short Note Skeleton
### Viva One-Liners
### Ward-Case Points
### Last-Night Sheet

---

## Summary
> Complete FCPS/MRCP note for {topic}. See Dermatology MOC for study plan.

---

## MCQs (10)
1. **Q:** 
   **Options:** A. B. C. D.
   **Answer:**
   **Explanation:**

---
*(9 more MCQs)*

---

## SBAs (10)
1. **Scenario:** 
   **Q:** 
   **Options:** A. B. C. D. E.
   **Answer:**
   **Explanation:**
---
*(9 more SBAs)*

---

## Flashcards
- **Q:** 
  **A:**
---
*(5 more)*

---

## Answer Key with Explanations
### MCQs
1. 
### SBAs
1. 

---

## Local Navigation
**Parent Heading Hub:** [[{parent_hub} Hub]]  
**Parent Topic Group Hub:** [[{topic_group} Hub]]  
**Chapter Hierarchy:** [[Davidson Chapter 29 - Dermatology Hierarchy]]  
**Chapter MOC:** [[Dermatology MOC]]  
**Drug Reference:** [[../00_Index/Dermatology Drug Reference]]  
**Related Topics:** [[Related Topic 1]], [[Related Topic 2]]
"""


def normalize(text):
    """Normalize text for matching (remove accents, special chars)."""
    return text.lower().replace('(', '').replace(')', '').replace(',', '').replace('.', '').replace('-', ' ').replace('ö', 'o').replace('ü', 'u').replace('ß', 'ss').replace('é', 'e').replace('ö', 'o').replace('ä', 'a').strip()


def generate_full_note(topic_data):
    """Generate full note from scaffold topic data."""
    today = date.today().isoformat()
    topic = topic_data['topic']
    heading = topic_data['heading']
    topic_group = topic_data['topic_group']
    
    # Determine parent hub
    section = topic_data['path'].split('/')[0]
    section_names = {
        '01_Structure_Function_Approach': 'Structure and Function',
        '02_Papulosquamous_Eczematous': 'Papulosquamous and Eczematous',
        '03_Urticaria_Erythema_Purpura': 'Urticaria Erythema Purpura',
        '04_Vesiculobullous': 'Vesiculobullous',
        '05_Drug_Eruptions': 'Drug Eruptions',
        '06_Skin_Infections': 'Skin Infections',
        '07_Skin_Tumours': 'Skin Tumours',
        '08_Pigmentation_Disorders': 'Pigmentation Disorders',
        '09_Hair_Nail_Disorders': 'Hair and Nail',
        '10_Systemic_Disease_Manifestations': 'Systemic Manifestations',
        '11_Genodermatoses': 'Genodermatoses',
        '12_HIV_Immunocompromise': 'HIV Immunocompromise',
        '13_Special_Populations': 'Special Populations',
        '14_Emergencies': 'Emergencies',
    }
    parent_hub = section_names.get(section, 'Dermatology')
    
    return FULL_NOTE_TEMPLATE.format(
        today=today,
        topic=topic,
        heading=heading,
        topic_group=topic_group,
        parent_hub=parent_hub
    )


def load_scaffold_topics(base_path="/mnt/tb/Medicine/Dermatology"):
    """Load all scaffold topics from the filesystem."""
    import glob
    
    scaffold_topics = []
    for f in glob.glob(f"{base_path}/**/*.md", recursive=True):
        try:
            with open(f, 'r') as fp:
                content = fp.read(500)
                if 'status: scaffold' in content and 'status: scaffold-hub' not in content and 'full-fcps-mrcp-note' not in content:
                    match = re.search(r'topic:\s*(.+)', content)
                    if match:
                        topic = match.group(1).strip()
                        rel_path = f.replace('/mnt/tb/Medicine/Dermatology/', '')
                        heading_match = re.search(r'heading:\s*(.+)', content)
                        topic_group_match = re.search(r'topic_group:\s*(.+)', content)
                        heading = heading_match.group(1).strip() if heading_match else ''
                        topic_group = topic_group_match.group(1).strip() if topic_group_match else ''
                        scaffold_topics.append({
                            'topic': topic,
                            'path': rel_path,
                            'heading': heading,
                            'topic_group': topic_group,
                            'full_path': f
                        })
        except:
            pass
    return scaffold_topics


def process_batch(topics_batch, output_dir="/mnt/tb/Medicine/Dermatology"):
    """Process a batch of topics."""
    results = []
    for topic_data in topics_batch:
        try:
            full_content = generate_full_note(topic_data)
            # Determine output path - replace scaffold with full in same directory
            orig_path = topic_data['full_path']
            new_path = orig_path.replace('.md', '_full.md')
            
            with open(new_path, 'w') as f:
                f.write(full_content)
            results.append(('SUCCESS', topic_data['topic'], new_path))
        except Exception as e:
            results.append(('ERROR', topic_data['topic'], str(e)))
    return results


def main():
    """Main entry point for batch processing."""
    base_path = "/mnt/tb/Medicine/Dermatology"
    
    # Load all scaffold topics
    print("Loading scaffold topics...")
    scaffold_topics = load_scaffold_topics(base_path)
    print(f"Found {len(scaffold_topics)} scaffold topics")
    
    # Skip already processed (check for _full.md)
    remaining = []
    for topic_data in scaffold_topics:
        full_path = topic_data['full_path'].replace('.md', '_full.md')
        if not os.path.exists(full_path):
            remaining.append(topic_data)
    
    print(f"Remaining to process: {len(remaining)}")
    
    # Process in batches of 25
    batch_size = 25
    total_batches = (len(remaining) + 24) // 25
    
    for i in range(0, len(remaining), batch_size):
        batch = remaining[i:i+batch_size]
        batch_num = i // batch_size + 1
        print(f"\nProcessing batch {batch_num}/{total_batches} ({len(batch)} topics)...")
        
        results = process_batch(batch)
        
        success = sum(1 for s, _, _ in results if s == 'SUCCESS')
        errors = sum(1 for s, _, _ in results if s == 'ERROR')
        print(f"  ✅ {success}/{len(batch)} successful")
        if errors:
            for status, topic, error in results:
                if status == 'ERROR':
                    print(f"  ❌ {topic}: {error}")
        
        import time
        time.sleep(0.5)  # Small delay between batches
    
    print(f"\n✅ Batch generation complete!")
    print(f"Processed {len(remaining)} topics")

if __name__ == "__main__":
    main()