# AceRoute-style Hermes Skills + Journey dashboard pattern

Use this when adding Hermes-native inventory/timeline pages to an existing SPA dashboard.

## Backend pattern

Add explicit JSON endpoints instead of embedding Hermes reads in the page:

- `/api/hermes/skills`
- `/api/hermes/journey`

### Skills collector shape
Return:
- `summary.total_skills`
- `summary.categories`
- `summary.linked_files`
- `categories[]` with `{name,count}`
- `skills[]` with `{id,name,slug,category,path,description,linked_files,linked_file_count,tags}`

Good source pattern:
- scan `~/.hermes/skills/**/SKILL.md`
- parse frontmatter when present
- derive fallback description from first non-empty body line
- count support files under `references/`, `templates/`, `scripts/`, `assets/`
- cache for ~60s

### Journey collector shape
Use native CLI:
- `hermes journey --json`

Normalize into:
- `summary.total`
- `summary.skills`
- `summary.memories`
- `summary.pinned`
- `summary.active`
- `recent[]`
- `timeline[]` daily aggregates like `{date,total,skill,memory}`
- `categories[]`
- `kinds[]`

Normalization details that worked:
- accept `nodes` / `items` / `entries`
- convert unix timestamps to ISO
- map `useCount -> use_count`, `createdBy -> created_by`
- treat non-`skill` kinds as memory-side entries for summary split
- cache for ~30s

## Frontend SPA pattern

### Header nav
Use explicit page buttons with `data-page` and a shared `switchPage(page)`:
- `Analytics`
- `Skills`
- `Journey`

`switchPage(page)` should:
- toggle `.page-section.active`
- toggle `.nav-btn.active`
- hide analytics-only controls like export/date range on non-analytics pages

### Skills page blocks
A compact, useful first version:
1. summary mini-stats
2. main skills table
3. top categories stack list
4. skill detail/highlight cards

### Journey page blocks
A compact, useful first version:
1. summary mini-stats
2. line chart for growth over time
3. kind mix stack list
4. recent timeline cards
5. category stack list

## Verification pattern

Do not stop at API success. Verify all three layers:

1. **backend syntax/config**
   - `python3 -m py_compile app.py collectors.py`
   - `docker compose config`
2. **live endpoints**
   - fetch `/api/hermes/skills`
   - fetch `/api/hermes/journey`
   - check headline counts
3. **rendered UI state**
   - open the page in browser tools
   - click `SKILLS` and `JOURNEY`
   - use DOM evaluation when snapshots are truncated:

```js
({
  activePage: document.querySelector('.page-section.active')?.id,
  skillsCount: document.querySelectorAll('#skillsTable tbody tr').length,
  categoryCards: document.querySelectorAll('#skillCategoryList .stack-item').length,
  detailCards: document.querySelectorAll('#skillHighlights .stack-item').length,
  journeyRecent: document.querySelectorAll('#journeyRecent .timeline-item').length,
  journeyCategories: document.querySelectorAll('#journeyCategories .stack-item').length,
})
```

This catches the common case where endpoints work but the tab never actually renders.

## Practical counts seen in this pattern
Example successful live verification looked like:
- skills summary present
- `#skillsTable tbody tr` > 0
- `#journeyRecent .timeline-item` > 0
- active page flips correctly between `page-skills` and `page-journey`

## Common pitfall
Browser accessibility snapshots may show only visible text snippets from timeline/detail cards, not the full table/card population. When verifying a data-heavy SPA, use DOM-count expressions in browser console instead of relying only on the snapshot text.