#!/usr/bin/env python3
import argparse
import base64
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request

BASE_URL = os.environ.get("WP_BASE_URL", "").rstrip("/")
WP_USERNAME = os.environ.get("WP_USERNAME", "")
WP_APP_PASSWORD = os.environ.get("WP_APP_PASSWORD", "")
USER_AGENT = "Hermes-WordPress-Poster/1.0"


def fail(message, code=1):
    print(json.dumps({"success": False, "error": message}, indent=2))
    sys.exit(code)


def auth_header():
    if not BASE_URL or not WP_USERNAME or not WP_APP_PASSWORD:
        fail("Set WP_BASE_URL, WP_USERNAME, and WP_APP_PASSWORD environment variables.")
    token = base64.b64encode(f"{WP_USERNAME}:{WP_APP_PASSWORD}".encode()).decode()
    return {"Authorization": f"Basic {token}"}


def request_json(method, path, payload=None, query=None):
    url = f"{BASE_URL}{path}"
    if query:
        url += "?" + urllib.parse.urlencode(query)
    data = None
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/json",
        **auth_header(),
    }
    if payload is not None:
        data = json.dumps(payload).encode()
        headers["Content-Type"] = "application/json"
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            body = r.read().decode()
            return r.status, json.loads(body) if body else None
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", "replace")
        try:
            parsed = json.loads(body)
        except Exception:
            parsed = {"raw": body}
        fail(f"HTTP {e.code} for {method} {url}: {json.dumps(parsed)}", code=2)


def get_me():
    _, data = request_json("GET", "/wp-json/wp/v2/users/me", query={"context": "edit"})
    return data


def find_category_by_name(name):
    _, cats = request_json("GET", "/wp-json/wp/v2/categories", query={"search": name, "per_page": 100, "context": "edit"})
    lname = name.strip().lower()
    for cat in cats:
        if cat.get("name", "").strip().lower() == lname:
            return cat
    return None


def ensure_category(name, parent=0):
    existing = find_category_by_name(name)
    if existing and int(existing.get("parent", 0)) == int(parent):
        return existing
    payload = {"name": name}
    if parent:
        payload["parent"] = int(parent)
    _, created = request_json("POST", "/wp-json/wp/v2/categories", payload=payload)
    return created


def ensure_category_path(path_text):
    parts = [p.strip() for p in path_text.split(">") if p.strip()]
    if not parts:
        return None, []
    parent = 0
    created = []
    last = None
    for part in parts:
        cat = find_category_by_name(part)
        if not cat or int(cat.get("parent", 0)) != int(parent):
            cat = ensure_category(part, parent=parent)
            created.append({"id": cat["id"], "name": cat["name"], "parent": cat.get("parent", 0)})
        parent = cat["id"]
        last = cat
    return last, created


def create_post(title, content, status, category_paths):
    category_ids = []
    created_categories = []
    for path_text in category_paths:
        last, created = ensure_category_path(path_text)
        if last:
            category_ids.append(last["id"])
        created_categories.extend(created)
    payload = {"title": title, "content": content, "status": status}
    if category_ids:
        payload["categories"] = category_ids
    _, post = request_json("POST", "/wp-json/wp/v2/posts", payload=payload)
    return post, created_categories


def main():
    parser = argparse.ArgumentParser(description="Create WordPress drafts/published posts with optional hierarchical categories.")
    sub = parser.add_subparsers(dest="cmd", required=True)

    sub.add_parser("whoami", help="Verify credentials")

    cat_p = sub.add_parser("ensure-category", help="Create category or subcategory path")
    cat_p.add_argument("path", help='Category path like "Medicine > Nephrology > AKI"')

    post_p = sub.add_parser("post", help="Create a draft or published post")
    post_p.add_argument("--title", required=True)
    post_p.add_argument("--content-file", required=True, help="Path to HTML/text file for post body")
    post_p.add_argument("--status", choices=["draft", "publish"], default="draft")
    post_p.add_argument("--category", action="append", default=[], help='Category path like "Medicine > Nephrology". Repeatable.')

    args = parser.parse_args()

    if args.cmd == "whoami":
        me = get_me()
        print(json.dumps({"success": True, "base_url": BASE_URL, "user": me.get("slug"), "roles": me.get("roles")}, indent=2))
        return

    if args.cmd == "ensure-category":
        cat, created = ensure_category_path(args.path)
        print(json.dumps({"success": True, "category": cat, "created_categories": created}, indent=2))
        return

    if args.cmd == "post":
        with open(args.content_file, "r", encoding="utf-8") as f:
            content = f.read()
        post, created_categories = create_post(args.title, content, args.status, args.category)
        print(json.dumps({
            "success": True,
            "post_id": post.get("id"),
            "status": post.get("status"),
            "link": post.get("link"),
            "categories": post.get("categories", []),
            "created_categories": created_categories,
        }, indent=2))


if __name__ == "__main__":
    main()
