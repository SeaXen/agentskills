---
name: wordpress-rest-publishing
description: "Publish to WordPress via REST API using Application Passwords — verify auth, create drafts, publish posts, and upload media safely."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [wordpress, blogging, cms, rest-api, publishing, application-passwords]
---

# WordPress REST Publishing

Use this skill when a user wants Hermes to create, draft, publish, or update blog posts on a WordPress site from chat or terminal workflows.

## When to use

Trigger this skill when the task involves any of:
- connecting a WordPress site to Hermes
- verifying whether a site supports API posting
- creating a draft post
- publishing a post immediately
- editing an existing post via API
- uploading media for featured images or inline content

## Preferred auth

Use a **WordPress Application Password** for a posting-capable user account.

Do **not** ask for or use:
- cPanel passwords
- the user's main WordPress password
- XML-RPC unless the REST API route is unavailable and the user explicitly wants a fallback

## Core endpoints

Typical endpoints:
- API root: `https://example.com/wp-json/`
- Posts: `https://example.com/wp-json/wp/v2/posts`
- Media: `https://example.com/wp-json/wp/v2/media`
- Auth test: `https://example.com/wp-json/wp/v2/users/me?context=edit`

## Safe workflow

1. **Check API root first**
   - Verify that `/wp-json/` responds and exposes `wp/v2`.
2. **Verify auth before posting**
   - Use `GET /wp-json/wp/v2/users/me?context=edit` with Basic Auth built from `username:application-password`.
   - Confirm the returned user and role.
3. **Do not create a live post without explicit user intent**
   - Draft creation and publish are side effects.
   - Ask before creating even a test draft unless the user clearly requested it.
4. **Prefer draft for first test**
   - First end-to-end test should usually be `status: draft`.
5. **Recommend password rotation after chat-shared secrets**
   - If the user pasted the Application Password into chat, advise revoking it after testing and creating a dedicated replacement.

## Verification commands

### Probe API root with a browser-like User-Agent

```bash
python3 - <<'PY'
import urllib.request, json
url = 'https://example.com/wp-json/'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, timeout=20) as r:
    data = json.load(r)
print({
    'name': data.get('name'),
    'home': data.get('home'),
    'namespaces': data.get('namespaces', [])[:10],
    'app_passwords': data.get('authentication', {}).get('application-passwords', {}),
})
PY
```

### Verify Application Password auth

```bash
python3 - <<'PY'
import urllib.request, urllib.error, json, base64
user = 'USERNAME'
app_pass = 'APPLICATION PASSWORD'
url = 'https://example.com/wp-json/wp/v2/users/me?context=edit'
credentials = base64.b64encode(f'{user}:{app_pass}'.encode()).decode()
req = urllib.request.Request(url, headers={
    'Authorization': f'Basic {credentials}',
    'User-Agent': 'Hermes-Agent WordPress Check/1.0',
    'Accept': 'application/json',
})
with urllib.request.urlopen(req, timeout=20) as r:
    data = json.loads(r.read().decode())
print({
    'status': r.status,
    'id': data.get('id'),
    'name': data.get('name'),
    'slug': data.get('slug'),
    'roles': data.get('roles'),
})
PY
```

## Create a post

### Draft post

```bash
python3 - <<'PY'
import urllib.request, json, base64
site = 'https://example.com'
user = 'USERNAME'
app_pass = 'APPLICATION PASSWORD'
payload = {
    'title': 'Test draft from Hermes',
    'content': '<p>Hello from Hermes.</p>',
    'status': 'draft'
}
credentials = base64.b64encode(f'{user}:{app_pass}'.encode()).decode()
req = urllib.request.Request(
    site + '/wp-json/wp/v2/posts',
    data=json.dumps(payload).encode(),
    headers={
        'Authorization': f'Basic {credentials}',
        'User-Agent': 'Hermes-Agent WordPress Publisher/1.0',
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    },
    method='POST',
)
with urllib.request.urlopen(req, timeout=30) as r:
    data = json.loads(r.read().decode())
print({
    'status': r.status,
    'id': data.get('id'),
    'link': data.get('link'),
    'post_status': data.get('status'),
    'title': data.get('title', {}).get('rendered'),
})
PY
```

### Publish immediately

Same as above, but set:

```json
{"status":"publish"}
```

## Category and subcategory creation

WordPress categories are hierarchical and can be managed over REST.

Recommended workflow:
1. search existing categories first with `GET /wp-json/wp/v2/categories?search=...&context=edit`
2. match exact case-insensitive names
3. verify the existing category's `parent` matches the intended hierarchy level
4. create missing ancestors top-down with `POST /wp-json/wp/v2/categories`
5. assign the final category IDs in the post payload's `categories` field

Useful payload examples:

```json
{"name":"Medicine"}
```

```json
{"name":"Nephrology","parent":2}
```

```json
{"name":"AKI","parent":3}
```

A practical path convention is:
- `Medicine > Nephrology > AKI`

Parse the path from left to right, creating or reusing each level before creating the post.

## Post formatting guidance

For first-pass WordPress posting, prefer **WordPress-ready HTML** rather than raw plain text or assuming Markdown support. Use real:
- `<h2>` / `<h3>` headings
- `<p>` paragraphs
- `<ul><li>` bullet lists
- `<hr />` separators when useful

This renders predictably across themes and avoids depending on a Markdown plugin.

## Reusable helper script

A generic helper script is available at:
- `scripts/wp_rest_publish.py`

Typical usage:

```bash
export WP_BASE_URL='https://example.com'
export WP_USERNAME='USERNAME'
export WP_APP_PASSWORD='APPLICATION PASSWORD'
python3 ~/.hermes/skills/productivity/wordpress-rest-publishing/scripts/wp_rest_publish.py whoami
python3 ~/.hermes/skills/productivity/wordpress-rest-publishing/scripts/wp_rest_publish.py ensure-category 'Medicine > Nephrology > AKI'
python3 ~/.hermes/skills/productivity/wordpress-rest-publishing/scripts/wp_rest_publish.py post \
  --title 'Test draft from Hermes' \
  --content-file /tmp/post.html \
  --status draft \
  --category 'Medicine > Nephrology > AKI'
```

## Upload media

For images, POST the binary file to `/wp-json/wp/v2/media` with:
- `Authorization: Basic ...`
- `Content-Disposition: attachment; filename="..."`
- correct `Content-Type`

Then use the returned media `id` as `featured_media` in the post payload.

## Common pitfalls

- **403 on `/wp-json/` with Python but 200 in browser**
  - Some hosts/WAFs block requests that use the default Python urllib User-Agent.
  - Retry with a browser-like `User-Agent: Mozilla/5.0` before concluding the API is blocked.
- **API root works but posting fails**
  - Verify auth with `/users/me?context=edit` before troubleshooting post payloads.
- **User sends credentials in chat**
  - Use them only for the immediate task.
  - Recommend revoking and recreating the Application Password after testing.
- **Confusing cPanel with WordPress auth**
  - cPanel access is irrelevant for API posting unless the user needs help generating the WordPress-side credential or inspecting plugins/firewall behavior.

## Response style for this task class

When the API probe succeeds, tell the user plainly:
- whether WordPress is confirmed
- whether REST API is live
- whether Application Password auth works
- what Hermes can do next: draft, publish, update, media

Keep the answer operational and concise; avoid long WordPress background unless the user asks.

## Support files

- `references/mdsagar-wordpress-verification.md` — live example from a successful site verification, including the User-Agent 403 pitfall.
- `references/category-hierarchy-and-draft-workflow.md` — proven pattern for hierarchical categories/subcategories and polished first-draft posting.
- `scripts/wp_rest_publish.py` — reusable env-driven helper for auth checks, category-path creation, and draft/publish posting.
