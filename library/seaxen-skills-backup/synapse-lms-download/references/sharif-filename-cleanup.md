# Sharif nested downloads — ugly filenames after `sanitize()`

`download_nested.py` names files with `sanitize(title) + ".mp4"`. LMS titles with Bengali script or trailing punctuation produce bad paths.

## Symptoms (verified 2026-07)

| LMS title | On disk before fix |
|-----------|-------------------|
| `রেসিডেন্সির সাথে বিসিএস প্রস্তুতি।` | `.mp4` (all non-ASCII stripped) |
| `Lecture No:09 Inferior Extremity.` | `Lecture_No_09_Inferior_Extremity..mp4` (trailing dot → double dot before extension) |
| `Inferior Extremity Lecture PDF.'` | `Inferior_Extremity_Lecture_PDF..pdf` |

## Fix after sync

1. `ffprobe` both videos — confirm `mov,mp4` before renaming.
2. Rename on disk; update `accounts/sharif.json` `filename` for matching `downloaded_videos` / `downloaded_notes` entries.

Example renames from 2026-07-03:

```text
Lecture_No_09_Inferior_Extremity..mp4  → Lecture_No_09_Inferior_Extremity.mp4
.mp4                                    → Residency_BCS_Preparation.mp4
Inferior_Extremity_Lecture_PDF..pdf     → Inferior_Extremity_Lecture_PDF.pdf
```

Use the human-readable `title` field in state when choosing the English slug for Bengali-only LMS titles.

## Prevention (future code change)

In `download_nested.py`, post-process `sanitize()`:

- Strip trailing `.` / `'` from title before sanitize
- If sanitized stem is empty or only punctuation, use `stream_id[:8]` or a fixed slug from a small title→slug map

Sagar flat tree uses `normalize_chapter_filenames.py` instead; Sharif keeps section/chapter paths on disk — normalize script targets `/mnt/tb/synapse_26_by_chapter` only unless extended.