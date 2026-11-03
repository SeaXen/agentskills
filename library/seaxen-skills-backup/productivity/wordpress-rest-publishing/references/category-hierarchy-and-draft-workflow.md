# Category hierarchy and first-draft workflow

This reference captures two practical patterns proven in live use.

## 1) Category and subcategory creation via REST API

WordPress categories are hierarchical and can be created over REST with `POST /wp-json/wp/v2/categories`.

Key fields:
- `name`: display label
- `parent`: parent category ID; omit or set `0` for a top-level category

Practical workflow:
1. search existing categories first (`GET /wp-json/wp/v2/categories?search=...&context=edit`)
2. match on exact case-insensitive `name`
3. verify the `parent` matches the intended level
4. create missing ancestors from top to bottom
5. use the final category ID in the post payload's `categories` list

Example path expansion:
- `Medicine`
- `Medicine > Nephrology`
- `Medicine > Nephrology > AKI`

## 2) First end-to-end post should usually be a polished draft

When the user wants professional blog posting, prefer this sequence:
1. verify auth
2. ensure category path exists
3. write WordPress-ready HTML with real headings/paragraphs/lists
4. create the post as `draft`
5. verify the created post by ID with `context=edit`
6. only publish after explicit user confirmation unless they directly asked for publish

Why HTML instead of plain text/Markdown:
- REST post content accepts HTML cleanly
- headings, lists, and separators render predictably in WordPress themes
- avoids depending on a Markdown plugin that may not exist

## Live example pattern
- Site had a WAF/host quirk: `/wp-json/` returned 403 to default Python `urllib` but 200 with a browser-like `User-Agent`
- Application Password auth succeeded against `/wp-json/wp/v2/users/me?context=edit`
- Draft creation succeeded with hierarchical category creation in the same workflow
