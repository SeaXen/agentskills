---
name: wordpress-mdsagar-publishing
description: Publish professional WordPress posts to mdsagar.com using the local helper script, with SEO/readability cleanup, slug, excerpt, tags, and category/subcategory assignment.
---

# WordPress mdsagar publishing

Use this when posting to `https://mdsagar.com` from Hermes.

## Default workflow
For this user, do this by default unless told otherwise:
1. Draft or refine the content into a professional web article, not raw Obsidian note format.
   - Default preferred style for this user: hybrid public-facing article + FCPS/MRCP exam pearls boxes.
2. Improve for SEO and readability before publishing:
   - clear search-friendly title
   - short paragraphs
   - descriptive H2/H3 headings
   - keyword naturally in intro and headings
   - FAQ or practical takeaways when useful
   - when suitable, add styled callout boxes such as Exam Pearls, Common Viva Traps, Must Not Miss Red Flags, and Practical Clinical Approach
   - specifically, for the `mp-box` classes (yellow, green, red, blue), the text color must be forced for all nested elements (li, strong, p, span, div) in both light and dark modes to ensure clarity against the tinted backgrounds
   - standard CSS for light mode: `.mp-box, .mp-box * { color: #111827 !important; }`
   - standard CSS for dark mode: `[data-theme="dark"] .mp-box, [data-theme="dark"] .mp-box * { color: #f1f5f9 !important; }`
   - when injecting Mermaid.js, use a `<pre class="mermaid">` block and include the CDN script tag directly in the post content to ensure rendering on this site's custom theme; also add a style block to center the diagram and support dark mode (e.g., `background: transparent` in dark mode)
3. Add:
   - slug
   - excerpt
   - tags
   - category/subcategory path
    - **At least one or two relevant internal links** in the article body when possible.
    - At least one or two relevant external links when they improve trust/usefulness.
4. **Post-processing generated HTML (CRITICAL)**:
   - When using the `wp_mdsagar_hybrid_publish.py` script, it often outputs standard HTML (e.g., `<h3>Exam Pearls</h3>`). You **must** manually post-process the generated HTML file (e.g., via a Python script using `re.sub`) before final publishing to ensure it matches the user's exam-hybrid expectations.
   - **Callout Boxes**: Convert standard headings for Pearls, Traps, Red Flags, and Clinical Approach into the explicit `mp-box` div structures (e.g., `<div class="mp-box mp-box-yellow"><span class="mp-box-title">⭐ FCPS/MRCP Exam Pearls</span><ul>...</ul></div>`).
   - **Forced Color CSS**: Injected CSS for boxes must be present: `.mp-box, .mp-box * { color: #111827 !important; }` and `[data-theme="dark"] .mp-box, [data-theme="dark"] .mp-box * { color: #f1f5f9 !important; }`.
   - **Hallucination Cleanup**: The script may inject "Nephrology" or "Kidney Disease" into tags or intro text for non-nephrology topics. Scrub these.
   - **Mermaid Diagrams**: Ensure `<pre class="mermaid">` is centered and has a transparent background.
   - **SEO Metadata**: Always finish by updating `rank_math_focus_keyword` and `rank_math_title` via the standard WP REST `/posts/<id>` endpoint. Use `urllib.request` if `requests` is not available in the environment.
5. **Batching Workflow**:
   - When the user asks for "next topics" or "2-3 more", use a Python automation script to iterate through the topics, running the hybrid publisher, post-processing the HTML (see below), updating content, and setting SEO metadata in one go.
   - Batch 2-3 at a time to maintain high quality while increasing speed.
6. Treat the featured image/banner as optional, not mandatory:
   - if the available image looks cheap, placeholder-like, PowerPoint-like, or the user dislikes it, remove it rather than forcing a weak banner
   - when no high-quality visual is ready, publish cleanly without a banner and let the user add/replace it later
   - for medical posts, prefer premium editorial kidney/organ visuals over boxy text banners or generic slide graphics
6. Keep a clear distinction between source-note style and website style:
   - the Obsidian `/mnt/tb/Medicine` material is FCPS/MRCP study-note content
   - the WordPress version should default to a reader-friendly public article, not a pasted exam note
   - for this user, the preferred balance is a professional hybrid article that stays close to the medicine-folder note feel: preserve more exam-oriented structure and clinical emphasis while still rendering as a clean web article
   - when the user says they want it 'more like the existing CKD/medicine note', bias toward carrying through sections such as Interpretation Frameworks, Differential Diagnosis, and stronger high-yield clinical framing rather than flattening everything into a generic blog post
   - if the user asks for a more exam-oriented feel on the site, prefer a hybrid: public-facing prose plus high-yield boxes/pearls, not full raw study-note scaffolding
7. Use the one-command publisher when the task is straightforward source-note → hybrid article conversion:
   - script: `~/.hermes/scripts/wp_mdsagar_hybrid_publish.py`
   - docs: `~/.hermes/scripts/README-mdsagar-wordpress-one-command.md`
   - `exam-hybrid` is the hard default in the script and should remain the default for this user unless they explicitly want a lighter, more public-facing result
   - `exam-hybrid` should preserve more of the source-note structure than `public-hybrid`, especially for nephrology topics like AKI/CKD
   - when the user says they want the WordPress post closer to the existing medicine-folder note, bias toward carrying over note-native sections such as `Interpretation Frameworks`, `Differential Diagnosis`, and stronger high-yield clinical framing rather than flattening into generic website copy
   - if environment variables for WordPress auth are missing in the current shell, dry-run still works for previewing generated HTML/excerpt, but live publish/update requires restoring `WP_BASE_URL`, `WP_USERNAME`, and `WP_APP_PASSWORD`; gateway interruptions may clear these env vars even when earlier commands in the session worked
8. Publish cleanly after the polish step unless the user explicitly asks to keep it as draft.
9. Verify the final post status, slug, link, categories, tags, and visible SEO elements.
10. When the post was regenerated from the one-command publisher, also verify the user-specific exam-heavy structure survived on the live page:
   - `Interpretation Frameworks`
   - `Differential Diagnosis`
   - `FCPS/MRCP Exam Pearls and Clinical Boxes`
11. Be careful when checking the live page title/HTML from this site:
   - plain `urllib`/non-browser requests to `mdsagar.com` may return `403`
   - use a browser-like `User-Agent` for raw HTML checks
   - if the browser snapshot title appears stale after a content update, distinguish between three layers before claiming failure: post heading/content, raw HTML `<title>`, and SEO/plugin/browser-cache rendering
   - `mdsagar.com` uses LiteSpeed page cache; the base URL may still serve a stale `<title>` with `x-litespeed-cache: hit` even when the live heading and uncached HTML are already correct
   - verify with a cache-busting query string such as `?cb=<timestamp>` before concluding the title is wrong; this can flip the response from cache hit to miss and reveal the real current `<title>`
   - if Rank Math metadata is already correct but the cached base URL still serves the old title, a practical content-side refresh is to toggle the post `publish -> draft -> publish` with the same final title/content so the page cache is invalidated
   - if needed, push Rank Math metadata again via `/wp-json/rankmath/v1/updateMeta` and then re-check with a browser-like request

## Important distinction
The Obsidian note in `/root/Desktop/tb/Medicine/Nephrology/` is the source-style study note. The WordPress post should usually be a rewritten web article:
- less exam-note scaffolding
- fewer Obsidian callouts/wikilinks
- more readable prose
- cleaner web headings
- professional intro/conclusion/disclaimer

Do not blindly paste the Obsidian note into WordPress. Adapt it.

## Local helper
Primary helper script:
- `~/.hermes/scripts/wp_mdsagar_poster.py`

One-command hybrid publisher from medical source notes:
- `~/.hermes/scripts/wp_mdsagar_hybrid_publish.py`

Reference docs:
- `~/.hermes/scripts/README-mdsagar-wordpress.md`
- `~/.hermes/scripts/README-mdsagar-wordpress-one-command.md`
- skill reference: `references/one-command-hybrid-publisher.md`
- skill reference: `references/batch-publishing-workflow.md`
- dark-mode callout fix reference: `references/dark-mode-callout-boxes.md`
- dark-mode and mermaid inject template: `templates/dark-mode-and-mermaid-inject.html`
- Stroke Medicine publishing pattern (category path, verified sections, Rank Math fix, future article list): `references/stroke-medicine-publishing-pattern.md`

Packaged support template:
- `templates/hybrid-medical-article.html` — reusable public-facing medical article skeleton with FCPS/MRCP exam-pearl boxes, TOC, FAQ, disclaimer, and an optional differential box

## Required environment variables
Set these in the shell before running the helper:
```bash
export WP_BASE_URL='https://mdsagar.com'
export WP_USERNAME='sagar'
export WP_APP_PASSWORD='...'
```

## Common commands
### Verify auth
```bash
python3 ~/.hermes/scripts/wp_mdsagar_poster.py whoami
```

### Ensure category/subcategory
```bash
python3 ~/.hermes/scripts/wp_mdsagar_poster.py ensure-category 'Medicine > Nephrology > AKI'
```

### Create a draft post
```bash
python3 ~/.hermes/scripts/wp_mdsagar_poster.py post \
  --title 'Post title' \
  --content-file /tmp/post.html \
  --excerpt-file /tmp/excerpt.txt \
  --slug 'post-slug' \
  --status draft \
  --category 'Medicine > Nephrology > AKI' \
  --tag 'Nephrology' \
  --tag 'AKI'
```

### Update and publish an existing post
```bash
python3 ~/.hermes/scripts/wp_mdsagar_poster.py update-post <POST_ID> \
  --title 'Post title' \
  --content-file /tmp/post.html \
  --excerpt-file /tmp/excerpt.txt \
  --slug 'post-slug' \
  --status publish \
  --category 'Medicine > Nephrology > AKI' \
  --tag 'Nephrology' \
  --tag 'AKI'
```

### Verify final state
```bash
python3 ~/.hermes/scripts/wp_mdsagar_poster.py get-post <POST_ID>
```

## Content prep pattern
When converting a medical note to WordPress:
- keep medical accuracy
- simplify note-like scaffolding
- convert tables/cutoffs into web-friendly bullets when appropriate
- add a concise hook paragraph at the top
- add natural keyword phrasing like `acute kidney injury symptoms`, `AKI causes`, `AKI diagnosis`, `AKI management`
- include a short FAQ when helpful
- end with a brief professional/medical disclaimer

## Rank Math SEO metadata — preferred update method
The `/wp-json/rankmath/v1/updateMeta` endpoint returns HTTP 400 on this site.
Use the standard WP REST posts endpoint instead — it accepts `meta` fields directly:
```python
payload = {
    'meta': {
        'rank_math_focus_keyword': '<keyword>',
        'rank_math_title': '<SEO title>',
        'rank_math_description': '<meta description>',
    }
}
# POST to /wp-json/wp/v2/posts/<id> with this payload → returns 200 OK
```
This works for both new posts and updates. Always do this immediately after creating/updating a post.

## Post-processing generated HTML (CRITICAL)
When using the `wp_mdsagar_hybrid_publish.py` script, it often outputs standard HTML (e.g., `<h3 ...>Exam Pearls</h3>` or raw ````mermaid`) and may lack advanced styling. You **must** manually post-process the generated HTML file (e.g., via a Python script using `re.sub`) before final publishing to ensure it matches the user's exam-hybrid expectations:
1. **Callout Boxes**: Convert standard headings for Pearls, Traps, Red Flags, and Clinical Approach into the explicit `mp-box` div structures (e.g., `<div class="mp-box mp-box-yellow" id="exam-pearls"><span class="mp-box-title">⭐ FCPS/MRCP Exam Pearls</span><ul>...</ul></div>`). See `references/stroke-medicine-publishing-pattern.md` for the exact box classes to use.
2. **Tooltips**: Find complex medical terms in the prose and wrap them in `<span class="md-tip" data-tip="Definition text">Term</span>` so users can hover for definitions.
3. **Mermaid Diagrams**: Raw markdown ` ```mermaid ` fences will fail to render on WordPress. Convert them to `<pre class="wp-block-code"><code>mermaid\n...</code></pre>`.
4. **Specialty Hallucinations**: The template script occasionally injects "Nephrology", "renal", or "KDIGO" text into the intro/outro. Always search for and scrub these cross-specialty hallucinations when posting outside of Nephrology.

## Stroke Medicine category and section checklist
- Category path: `Medicine > Stroke Medicine` (parent category ID 2, sub ID 17)
- confirmed these sections are live on the page:
  - `Table of Contents` (styled blue left-border nav box)
  - `Interpretation Framework`
  - `Differential Diagnosis`
  - `FCPS/MRCP Exam Pearls` (yellow box, high-yield summary)
  - `Common Viva Traps` (green box)
  - `Red Flags` (red box, must-not-miss emergencies)
  - `Practical Clinical Approach` (blue box, numbered list)
  - `FAQ` section
  - `Penumbra / Infarct Core` (for AIS articles)
  - `Mermaid Diagram` (flowchart component)

## Safety
- Prefer WordPress Application Password, never the main cPanel password.
- If credentials were pasted in chat, remind the user to rotate/revoke them later.
