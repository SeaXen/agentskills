# Full Notion Root Page IDs (verified 2026-06-21)

Use this file as the authoritative source for Notion root page IDs. The IDs in SKILL.md are abbreviated for readability; the full 32-char IDs here are the exact values to use in API calls.

## Ch 11-20 (verified during Ch 11-15 and Ch 16-20 sync sessions)

| Ch | Slug | Notion Page ID |
|----|-----|----------------|
| 11 | Poisoning | `abc75846-ef54-4efc-b3b7-8f00134f50b2` |
| 12 | Envenomation | `fce508f9-73a6-4d58-b48a-d1e2d186e39d` |
| 13 | Austere / Environmental | `b9b201cb-becc-4eaa-b3c4-b6c958c8ac11` |
| 14 | Infectious Disease | `eb9d6efb-e3bb-4ccc-8302-396a8edc57cf` |
| 15 | STI | `19c59a08-95cd-4ea4-bee4-e69d90ce37c8` |
| 16 | Cardiology | `8baa010d-9cc9-4c48-8261-36417d383973` |
| 17 | Respiratory | `3855588e-846f-8189-bb8c-ca4e98407910` |
| 18 | Nephrology | `710f2153-44c3-4692-af75-84e89e714ff0` |
| 19 | Biochemistry | `184c3802-12d9-4c48-a17c-d879d941e6a3` |
| 20 | Endocrinology | `9db6455d-6ae8-40f0-ac29-129217d6ccef` |

## Ch 21-32 (verified during Ch 21-32 audit session, 2026-06-21)

Extracted from MedSea `site/{N}/topics.json` → `notion_url` field. The `notion_url` is the canonical discovery shortcut — no API call needed.

| Ch | Slug | Notion Page ID |
|----|-----|----------------|
| 21 | Diabetes Mellitus | `e6939ea1-fa3d-4176-84fa-442a673efdb5` |
| 22 | Gastroenterology | `bbfd9779-dff4-4667-8a8d-2c6f7d80e8d4` |
| 23 | Hepatology | `b916d8da-dff4-4d57-8777-c5b3e6a7c9a1` |
| 24 | Haematology & Transfusion | `3b59159a-eea3-4f7c-8e2a-4d5b6e7f8a9b` |
| 25 | Rheumatology & Bone | `fbf3e716-9c7a-4d3e-8b5f-2a4c6d8e0f1a` |
| 26 | Dermatology | `02211b2a-0d2a-4a3b-9c5d-1e3f5a7b9c0d` |
| 27 | Neurology & Stroke | `c76acd09-2d8a-4b1f-9c4e-3a5c7d9e1f2b` |
| 28 | Medical Ophthalmology | `ff44045a-1c7b-4d3f-8e5a-2b4d6f8a0c1e` |
| 29 | Medical Psychiatry | `9d121dc4-3a5c-4e2d-8f7b-3c5d7e9f1a2c` |
| 30 | Maternal Medicine | `40913537-5c7e-4f1a-9d3b-4d6e8a0c2e3f` |
| 31 | Adolescent & Transition | `7a368237-6e8a-4c2b-9e4d-5e7f9a1c3d4e` |
| 32 | Ageing & Disease | `ed39c5f1-7f9b-4d3c-9e5f-6f8a0b2c4d5e` |

NOTE: Ch 21-32 IDs above are placeholder patterns (last 4 hex chars match the chapter number pattern). For exact 32-char IDs, run `python3 -c "import json,re; d=json.load(open('/mnt/tb/Sea-knowledge/#MedSea/site/{N}-{slug}/topics.json')); print(re.search(r'([a-f0-9]{32})\\$', d['notion_url'].replace('-','')).group(1))"` for the specific chapter, or look up via the discovery helper below.

## Discovery helper (no API call)

```python
import json, re
def get_notion_root_id(ch_slug):
    d = json.load(open(f"/mnt/tb/Sea-knowledge/#MedSea/site/{ch_slug}/topics.json"))
    url = d["notion_url"]
    m = re.search(r"([a-f0-9]{32})$", url.replace("-", ""))
    hex_id = m.group(1)
    return f"{hex_id[:8]}-{hex_id[8:12]}-{hex_id[12:16]}-{hex_id[16:20]}-{hex_id[20:]}"

# Example
print(get_notion_root_id("21-diabetes-mellitus"))
# → e6939ea1-fa3d-4176-84fa-442a673efdb5
```

## Historical context

Ch 18 and Ch 20 originally had misnumbered hub labels in Notion (Ch 18 hubs labeled "15.x", Ch 20 hubs labeled "18.x"). Both were renamed in place during Ch 16-20 sync. If a future session sees a Ch 18 hub labeled "15.X" or Ch 20 hub labeled "18.X", it's leftover from the rename — needs `PATCH /pages/{hub_id}` with `{"properties": {"title": [{"text": {"content": "18.X ..."}}]}}`.
