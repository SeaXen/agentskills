# Stream Timeout Workaround for Large Medical Notes

## Problem
The Hermes `write_file` tool has an ~8K token limit per call. Full FCPS/MRCP notes with all 18 sections typically range 12-20K tokens, causing stream timeouts.

## Solution: Split Write Strategy

### Token Estimation
- Frontmatter + Sections 1-9 (Learning Objectives through Differential Diagnosis): ~6-8K tokens
- Sections 10-18 (Management through Local Navigation): ~8-12K tokens
- **Total**: 12-20K tokens

### Write Pattern
```bash
# Call 1: Frontmatter + Sections 1-9
write_file(
  path=".../Topic.md",
  content="---\nfrontmatter...\n---\n\n# Topic\n\n## Learning Objectives\n...\n## Differential Diagnosis\n..."
)

# Call 2: Sections 10-18
write_file(
  path=".../Topic.md",
  content="## Management\n...\n## Local Navigation\n..."
)
```

**Note**: Each `write_file` call **overwrites** the entire file. The second call must contain the COMPLETE file content (frontmatter + all sections), not just the second half.

### Correct Pattern: Two Complete Writes
```bash
# Write 1: Full file up to section 9
write_file(path, full_content_part1)

# Write 2: Full file (same content + rest)
write_file(path, full_content_part1 + full_content_part2)
```

**Wait!** `write_file` **overwrites** the entire file each time. So you must build the complete content in your script/state first, then either:
1. Send it all in ONE call if <8K tokens
2. If >8K, you CANNOT split across write_file calls because each overwrites

**Actual Solution**: Build the complete content in your working context, then if it exceeds the token limit, you must send it as a SINGLE write_file call but the tool will timeout. 

**Actual Working Pattern Used in Session**:
- Write the note as a single complete string in your context
- Use `write_file` once with the full content
- The timeout occurs on the **response stream**, not the write itself
- The write SUCCEEDS even if response times out
- Next action: verify file written with `read_file`

## Batch Size Optimization

### Recommended: 5-8 notes per commit
- 10-15 notes caused git operations to timeout
- 5-8 notes + commit = stable
- After each batch: run verification, update MOC, commit

### Verification Protocol
```bash
# After each batch:
1. search_files for "status: full-fcps-mrcp-note" → verify count
2. search_files for "status: scaffold" → verify remaining
3. Update MOC with ✅ links
4. git add -A && git commit -m "descriptive message"
5. git push
```

## Template Token Estimates

| Section Range | Approx Tokens |
|---------------|---------------|
| Frontmatter + Sections 1-9 | 6,000-8,000 |
| Sections 10-18 | 8,000-12,000 |
| **Total** | **14,000-20,000** |

**Always assume ~15K tokens for a complete note** → will timeout on response stream but write succeeds.