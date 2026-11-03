# Facebook metadata format (what yt-dlp actually returns)

Real-world dump from `yt-dlp --dump-json --cookies-from-browser firefox <FB-url>` on share-link videos. Captured 2026-08-19.

## Title pattern
```
<engagement stats> | <real title>
```
The engagement prefix always includes `| K|M| |` notation (`100 shares`, `78K views`, `2K reactions`, `556K views · 18K reactions`). **Splitting on ` | ` and taking index [1] gives the real title.**

## Real samples (from the session)

```
facebook_1015121037677035_Most_students_sit_down_to_study_and_wonder_why_focus_takes_so_long_to_arrive._Th.mp4
  uploader: Tom Vorselen
  upload_date: 20260621
  raw title len: 2007 chars (long description embedded)

facebook_1646796213726872_Still_forgetting_what_you_studied_yesterday_Maybe_the_problem_isnt_your_memory....mp4
  uploader: GroNexa Official
  upload_date: 20260715
  raw title len: 644 chars

facebook_1723576699090399_কন_পডত_ভল_লগন_বঝছ_ত_এবর_reality_study_raihan_Study_With_Raihan.mp4
  uploader: Study With Raihan
  upload_date: 20260606
  raw title len: 109 chars
  Note: Bengali text in title — UTF-8 preserved through sanitize step.

facebook_1044090321357767_Im_so_glad_youre_here_Welcome_to_The_Bridge_Library_We_take_you_from_the_shows_y.mp4
  uploader: Annaberlin.writes
  upload_date: 20260809
  raw title len: 497 chars

facebook_1979204276291871_The_Sugar_Doctors_WARNING_The_Healthy_Foods_Quietly_Destroying_Your_Body_-_Dr_Da.mp4
  uploader: (medical channel — long-form interview)

facebook_864989063157942_Day_169-365_hard_work_challenge_discipline_army_trending_viral_fitnessboyt94_Fit.mp4
  uploader: fitness challenge page

facebook_1411556474164002_Day_186-365_hard_challenge_discipline_army_trending_viral_fitnessboyt94_Fitnessb.mp4
  uploader: same fitness challenge series — note consistent hashtag-style tags
```

## Sanitization rules (in `scripts/fbdl.py`)
```python
parts = raw.split(" | ", 1)
real = parts[1].strip() if len(parts) == 2 else raw.strip()
clean = re.sub(r"[^\w\s.\-]", "", real, flags=re.UNICODE)
clean = re.sub(r"\s+", "_", clean.strip())
clean = re.sub(r"-+", "-", clean).strip("_-")
clean = clean[:80].rstrip("_-")
```
- Strips the engagement prefix via `" | "` split
- Keeps Unicode letters/digits/`_`/`.`/`-`/space
- Collapses whitespace to single `_`
- Caps at 80 chars; right-trims `_`/`-` to avoid ugly trailing chars

## Title-length distribution observed
- Shortest useful: ~30 chars (simple study tips)
- Median: ~100 chars
- Longest (with embedded description): 2212 chars — truncate cap is essential

## Edge cases handled by the wrapper
- Empty title → fall back to `facebook_<ID>.mp4`
- Title with no ` | ` separator → use the whole string
- All-emojis title → sanitize strips them; result is empty → fall back to ID-only
- Pure Bengali / non-Latin script → preserved as Unicode (filesystem must be UTF-8, which is the default on Linux)

## Pitfall: shell-escape hazard with yt-dlp regex templates
yt-dlp's `-o "%(title&^...&...&)s"` syntax uses `&` as the regex delimiter, which is a special char in bash. Trying to use it inline in a terminal command (or in a quote-wrapped string passed via subprocess) reliably gets mangled. That's why the wrapper pre-fetches metadata via `--dump-json` and computes the filename in Python — much safer than fighting yt-dlp's template DSL across shell escaping.
