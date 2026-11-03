# Batch Generation via subprocess.run — Stream Timeout Avoidance

## Problem
In `execute_code`, calling `write_file` 300+ times in a single Python script causes the stream to time out before delivery. You get the error:

> Your previous tool call (write_file) was too large and the stream timed out before it could be delivered. Do NOT retry the same tool call with the same large content. Instead, break the content into multiple smaller tool calls...

Even when individual writes are small (8-15 KB), the cumulative stream payload from 300 calls exceeds the limit.

## Solution: Subprocess Delegation

1. Write the generator script to `/tmp/gen_xxx.py` using a single `write_file` call (the script itself, not its output)
2. Run it via `subprocess.run(["python3", script_path], capture_output=True, text=True, timeout=120)`
3. The script does all the heavy file writing silently
4. Return only the summary in the execute_code response

### Pattern That Works (Cardiology session, 2026-06-15):

```python
# Step 1: Save generator to /tmp
generator_code = """
import json
from pathlib import Path

with open("/tmp/cardio_topics_organized.json") as f:
    organized = json.load(f)

def make_note(topic_data):
    # ... build note string from topic_data ...
    return note

created = 0
for topic_data in organized:
    note = make_note(topic_data)
    Path(topic_data["path"]).write_text(note)
    created += 1

print(f"Created {created} notes")
"""

Path("/tmp/gen_all_notes.py").write_text(generator_code)

# Step 2: Run via subprocess
import subprocess
result = subprocess.run(
    ["python3", "/tmp/gen_all_notes.py"],
    capture_output=True, text=True, timeout=120
)
print("STDOUT:", result.stdout)
```

**Result**: 329 notes created in 0.42 seconds. No timeout.

### What Did NOT Work:

```python
# INLINE — timed out at ~200 writes
import json
with open("/tmp/cardio_topics_organized.json") as f:
    organized = json.load(f)

for topic_data in organized:
    note = make_note(topic_data)
    with open(topic_data["path"], 'w') as f:  # ← This is the call that fills the stream
        f.write(note)
# After 200+ writes, stream payload exceeds 50KB cap, times out
```

## Why This Works

The `execute_code` tool returns the script's `print()` output as the result, capped at ~50KB. When you call `write_file` 300 times from inside the script, each call's output gets included in the cumulative stream. But:

- `subprocess.run` keeps all child-process output isolated
- The child process does file I/O silently
- Only the parent's print() (small) returns to the agent

## When to Use This Pattern

Use it whenever you need to:
- Generate 50+ files in one session
- Bulk-transform existing files
- Run any heavy I/O from a single tool call

The Cardiology session generated 549 files (329 + 220) across two subprocess calls, total runtime under 1 second.

## Limits

- subprocess timeout: 120s (5-minute timeout is for foreground)
- subprocess can fail silently if it hits an unhandled exception — always check `result.returncode`
- For 500+ files, split into 2-3 batches to keep debugging tractable

## Alternative: Multiple Smaller execute_code Calls

If the script itself is too large to fit in one write_file (e.g., contains medical content databases), split the work:

1. First call: Save data files to /tmp (JSON with topic mappings, content databases)
2. Second call: Run subprocess pointing at the data
3. Iterate per category if categories are large

This is what the Cardiology session did:
- /tmp/cardio_topics_organized.json (parsed hierarchy)
- /tmp/cardio_orphans.json (orphan scaffold mapping)
- /tmp/gen_all_notes.py (generator for hierarchy topics)
- /tmp/upgrade_orphans.py (generator for orphan scaffolds)

## Endocrinology Session (2026-06-15): Template Application at Scale

A variation of the subprocess pattern was used for **template application at scale** (not note generation from scratch):

### Pattern: Pre-generate + Batch Apply via Single execute_code

1. **Load all templates** into memory (pre-generated template sections for each category)
2. **Single execute_code call**: Iterate through all files, apply template sections where missing
3. **Single pass**: Reads file, inserts sections before "## Local Navigation", writes back

### Code Pattern (Endocrinology - 25 templates applied to 25 files in ~1 second):

```python
# Pre-generate sections for all templates
template_sections = {}
for cat, template in all_templates.items():
    template_sections[cat] = generate_sections(template)

# Apply in single execute_code call
applied = 0
for filename, category in file_categories.items():
    if category in template_sections:
        content = read_file(filepath)
        if "## MCQs" not in content:
            new_content = content.replace("## Local Navigation", 
                template_sections[category] + "\n## Local Navigation")
            write_file(filepath, new_content)
            applied += 1
```

**Result**: Applied 25 templates to 25 files in a single execute_code call (no stream timeout, since each `read_file`/`write_file` is a separate tool call, not 300 `write_file` calls in one script).

### Why This Works

- Unlike the inline pattern (which calls `write_file` 300+ times inside one script), each `write_file` here is a **separate tool call** in the agent loop
- The `execute_code` call just orchestrates; the actual file I/O happens in the agent's tool loop
- Each tool call returns its result independently — stream payload stays small

### Endocrinology Results

- **25 templates** applied to **25 files** in ~1 second
- **76 disease files** now have MCQ/SBA/Flashcard/Answer Key sections
- **100% completion** for Endocrinology Chapter 20 (94 topics, 76 files)
- Tracking files (MOC, Hierarchy, 11 Hub files) updated programmatically
