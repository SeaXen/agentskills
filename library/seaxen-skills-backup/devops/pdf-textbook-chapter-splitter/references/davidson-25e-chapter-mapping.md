# Davidson 25e — verified chapter → PDF page map

Source: `/mnt/tb/#Sea/Book/Davidson_s Principles and Practice of Medicine 25e.pdf`
Total PDF pages: **1,409**
Split output: `/mnt/tb/#Sea/Book/Davidson 25 Chapters/`

## Why this reference exists

The split was done on 2026-07-11 by scanning chapter listing pages and verifying with running headers (`<printed_page>  •  <CHAPTER TITLE>`). All 33 chapters mapped cleanly. If anyone needs to regenerate the chapter PDFs (e.g. after a source re-export), use this table directly.

## Front matter

PDF pages 1–14 (cover, copyright, contents, contributors, advisory board, acknowledgements, introduction, preface).
Saved as `00_Front_Matter.pdf`.

## Chapter map

| Ch | Title | Listing page (1-indexed PDF) | Pages |
|---:|---|---:|---:|
| 1  | Clinical decision-making | 15  | 12 |
| 2  | Clinical therapeutics and good prescribing | 27  | 23 |
| 3  | Clinical genetics | 50  | 23 |
| 4  | Clinical immunology | 73  | 30 |
| 5  | Nutritional factors in disease | 103 | 29 |
| 6  | Population health and epidemiology | 132 | 11 |
| 7  | Principles of infection | 143 | 34 |
| 8  | Oncology | 177 | 31 |
| 9  | Palliative and supportive care | 208 | 26 |
| 10 | Acute medicine and critical illness | 234 | 47 |
| 11 | Poisoning | 281 | 21 |
| 12 | Envenomation | 302 | 13 |
| 13 | Medicine in austere environments | 315 | 13 |
| 14 | Infectious disease | 328 | 107 |
| 15 | Sexually transmitted infections | 435 | 17 |
| 16 | Cardiology | 452 | 97 |
| 17 | Respiratory medicine | 549 | 81 |
| 18 | Nephrology and urology | 630 | 59 |
| 19 | Clinical biochemistry and metabolic medicine | 689 | 36 |
| 20 | Endocrinology | 725 | 57 |
| 21 | Diabetes mellitus | 782 | 56 |
| 22 | Gastroenterology | 838 | 78 |
| 23 | Hepatology | 916 | 64 |
| 24 | Haematology and transfusion medicine | 980 | 75 |
| 25 | Rheumatology and bone disease | 1055 | 79 |
| 26 | Dermatology | 1134 | 57 |
| 27 | Neurology and stroke medicine | 1191 | 97 |
| 28 | Medical ophthalmology | 1288 | 24 |
| 29 | Medical psychiatry | 1312 | 32 |
| 30 | Maternal medicine | 1344 | 18 |
| 31 | Adolescence, transition and young adult medicine | 1362 | 21 |
| 32 | Older adult medicine and frailty | 1383 | 16 |
| 33 | Laboratory reference ranges | 1399 | 11 |

## Notable quirks

- Ch 2 title wraps: "Clinical therapeutics and good / prescribing" on the listing page.
- Ch 6 title wraps: "Population health and / epidemiology".
- Ch 9 title wraps: "Palliative and / supportive care".
- Ch 10 title wraps: "Acute medicine and / critical illness".
- Ch 12 title wraps: title fits on one line but is preceded by author name on a separate line.
- Ch 24 title wraps: "Haematology and transfusion / medicine".
- Ch 31 title wraps across three lines: "Adolescence, transition / and young adult medicine".

All handled by whitespace normalization in the splitter script.

## Regen command

```bash
/usr/local/lib/hermes-agent/venv/bin/python /tmp/split_davidson.py
```

Source script: `/tmp/split_davidson.py` (created during the original split, contains the chapter map verbatim).
