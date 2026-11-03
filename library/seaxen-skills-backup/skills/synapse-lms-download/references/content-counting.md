# Counting actual course content (don't trust marketing)

The course brochure / landing page may list "50 Classes" or "30 Lectures" but the actual published content can be much smaller. **Before telling the user "there are X videos / Y PDFs", enumerate from the LMS itself.**

## One-liner to count actual content per chapter

After logging in (any chapter page loads it into localStorage), open browser DevTools console:

```js
const chapters = JSON.parse(localStorage.allLectures);
const totalVids = chapters.reduce((a, c) => a + (c.videoContents?.length || 0), 0);
const totalFiles = chapters.reduce((a, c) => a + (c.fileContents?.length || 0), 0);
const table = chapters.map(c => ({
  id: c._id,
  name: c.name,
  videos: c.videoContents?.length || 0,
  files: c.fileContents?.length || 0,
}));
console.table(table);
console.log('TOTAL:', totalVids, 'videos,', totalFiles, 'files across', chapters.length, 'chapters');
```

Output (real example from Sagar's Synapse enrollment, 2026-06-18):

```
┌─────┬──────────────────────────────────────────────┬────────┬───────┐
│ (i) │ name                                         │ videos │ files │
├─────┼──────────────────────────────────────────────┼────────┼───────┤
│ 0   │ "Davidson's Review Batch-02"                 │   2    │   0   │
│ 1   │ "FCPS P-I Basic Classes"                     │   0    │   0   │
│ 2   │ "Davidson's Notes"                           │   0    │  16   │
│ 3   │ "Basic Notes"                                │   0    │   0   │
└─────┴──────────────────────────────────────────────┴────────┴───────┘
TOTAL: 2 videos, 16 files across 4 chapters
```

## Why this matters

The course brochure screenshot said "Total 50 Classes · 30 Davidson's Review Classes · 5 Basic Classes · ..." — making the assistant report "49 other lectures" as if they existed. Actual published content was 2 videos and 16 PDFs. The user explicitly corrected this with "I only see 2 lecture".

**Rule:** never quote content counts from course landing pages, brochures, or marketing screenshots. Always run the `allLectures` query first.

## Same recipe from Python (Playwright)

```python
chapters_json = await page.evaluate("localStorage.getItem('allLectures') || '[]'")
chapters = json.loads(chapters_json)
total_v = sum(len(c.get("videoContents") or []) for c in chapters)
total_f = sum(len(c.get("fileContents") or []) for c in chapters)
for c in chapters:
    print(f"  {c['_id']}  {c['name']!r}  videos={len(c.get('videoContents') or [])}  files={len(c.get('fileContents') or [])}")
print(f"Total: {total_v} videos, {total_f} files across {len(chapters)} chapters")
```

## Empty-chapter pattern

Some chapters in the enrollment are placeholders (Basic Notes, FCPS P-I Basic Classes in the example) — `videoContents` and `fileContents` are both empty arrays. Don't report these as "broken"; they're just not published yet. Mark them clearly in output:

```
- 6a251aa4585213c2b6778498  "Basic Notes"   0 videos, 0 files   (empty - not published)
```
