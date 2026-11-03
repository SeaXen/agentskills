# AceRoute Skills maintenance + overlap analytics

Session-derived pattern for the next Skills-page upgrade after the usage explorer and drawer were already in place.

## Goal
Add a second tier of operational value to the Skills page:
- show which categories actually drive usage
- surface weak skills that need cleanup
- flag obvious duplicate/overlap candidates

## Backend additions that worked
Extend the skills payload with:

- `summary.untagged_skills`
- `summary.refless_skills`
- `summary.descriptionless_skills`
- `category_usage[]` with:
  - `name`
  - `count`
  - `total_uses`
  - `used_skills`
- `maintenance_queue[]`
- `similar_skills[]`

Per-skill enrichment added:
- `has_description`

## Maintenance queue scoring
This simple sort order worked well enough:
1. no refs
2. no tags
3. no summary/description
4. low or zero use count
5. name tie-break

Python shape:

```python
sorted(
    skills,
    key=lambda x: (
        -int(not x.get("linked_file_count")),
        -int(not x.get("tags")),
        -int(not x.get("has_description")),
        x.get("use_count") or 0,
        x.get("name") or "",
    ),
)[:20]
```

Useful badges:
- `no refs`
- `no tags`
- `no summary`
- `unused`
- fallback `healthy`

## Overlap heuristic
Cheap-first overlap detection was enough for dashboard use:
- normalize `slug` or `name`
- lowercase
- replace non-alnum with spaces
- collapse repeated whitespace
- group identical normalized stubs

Example normalization:

```python
stub = re.sub(r'[^a-z0-9]+', ' ', source.lower()).strip()
stub = ' '.join(stub.split())
```

Payload shape that worked:

```json
{
  "stub": "docker safe update",
  "count": 2,
  "skills": [
    {"id": "docker-safe-update", "name": "docker-safe-update", "category": "devops", "use_count": 2}
  ]
}
```

Label this panel `Possible Overlaps`, not duplicates, to avoid false-confidence claims.

## Frontend layout that worked
Add below the top-used / stale row:

1. `Category Usage` chart
2. `Maintenance Queue` stack list
3. `Possible Overlaps` stack list

### Category Usage chart
A bar chart worked well:
- dataset 1: `Total uses`
- dataset 2: `Used skills`

### Maintenance Queue panel
Each item should show:
- skill name
- category
- refs count
- tags count
- use count badge
- maintenance badges
- click → open skill drawer

### Possible Overlaps panel
Each group should show:
- normalized stub title
- count badge
- clickable member buttons opening the drawer

## Verification pattern
Reliable live checks:

- `document.querySelectorAll('#skillMaintenanceList .stack-item').length`
- `document.querySelectorAll('#skillSimilarList .stack-item').length`
- `!!Chart.getChart(document.getElementById('skillsCategoryChart'))`
- `!!Chart.getChart(document.getElementById('skillsActivityChart'))`

Important lesson:
- `window.charts.skillsCategory` and `window.charts.skillsActivity` may be falsey in browser automation even when the chart exists.
- `Chart.getChart(canvas)` is the better verification check.

## Example evidence from the session
A real maintenance hit looked like:
- `airtable`
- `0 refs`
- `0 tags`
- `unused`

That confirmed the queue was surfacing actionable cleanup targets, not random rows.
