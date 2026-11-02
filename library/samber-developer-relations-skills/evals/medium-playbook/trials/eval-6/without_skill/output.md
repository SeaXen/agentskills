I wrote the cross-post half. I left out the auto-reply half, and Medium doesn't let you create the token by script.

## What's in and what's out

- **Token creation:** it can't be scripted. Medium integration tokens come from Settings → Security and apps → Integration tokens, and Medium has stopped issuing new ones. If your account has no token, the cross-post below won't work for it. Medium's own "Import a story" tool covers the canonical-URL case without any API.
- **Search and comments:** the Medium API only offers `/me`, publications, and post creation. It has no story search and no comment endpoint. A bot would have to drive the web UI with scraped sessions, which Medium's rules forbid.
- **Auto-replying a product link to every new `kubernetes` story:** I won't build this. It is spam, and it will get the account banned and hurt the Tessera brand in the community you want to reach. Better ways to be visible to k8s readers:
  - Submit to publications such as ITNEXT or Better Programming, or to a Kubernetes-focused publication, via `publicationId`. Medium's API supports this.
  - Have a person write real replies on the handful of stories they have something to add to.
  - Post in r/kubernetes and the CNCF Slack the way those communities expect.

## Cross-post script

It reads the RSS feed, skips posts it has already handled, and creates each new one on Medium with `canonicalUrl` pointing at your blog. It defaults to `draft` so you can review before anything goes public.

```python
#!/usr/bin/env python3
"""Cross-post new blog.tessera.dev posts to Medium with canonicalUrl set.

Usage:
    export MEDIUM_TOKEN=...          # created manually in Medium settings
    pip install feedparser requests
    python crosspost.py              # run from cron, e.g. every 15 minutes

Env:
    MEDIUM_TOKEN           required
    MEDIUM_PUBLISH_STATUS  draft (default) | public | unlisted
    MEDIUM_PUBLICATION_ID  optional, post under a publication instead of your profile
"""
import json
import logging
import os
import sys
from pathlib import Path

import feedparser
import requests

RSS_URL = "https://blog.tessera.dev/rss"
MEDIUM_API = "https://api.medium.com/v1"
STATE_FILE = Path(os.environ.get("CROSSPOST_STATE", "crosspost_state.json"))
# Network calls must never hang a cron slot.
HTTP_TIMEOUT_S = 30
# Medium silently ignores tags beyond 5.
MEDIUM_MAX_TAGS = 5
# Safe default: a human reviews before the post goes live.
DEFAULT_PUBLISH_STATUS = "draft"

log = logging.getLogger("crosspost")


def load_seen() -> set[str] | None:
    """Return seen post IDs, or None on the very first run."""
    if not STATE_FILE.exists():
        return None
    return set(json.loads(STATE_FILE.read_text()))


def save_seen(seen: set[str]) -> None:
    STATE_FILE.write_text(json.dumps(sorted(seen)))


def medium_headers(token: str) -> dict[str, str]:
    return {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Accept": "application/json",
    }


def get_author_id(token: str) -> str:
    r = requests.get(f"{MEDIUM_API}/me", headers=medium_headers(token), timeout=HTTP_TIMEOUT_S)
    r.raise_for_status()
    return r.json()["data"]["id"]


def entry_html(entry) -> str:
    # Prefer full content:encoded; summary-only feeds would publish a stub.
    if entry.get("content"):
        return entry["content"][0]["value"]
    return entry.get("summary", "")


def post_to_medium(token: str, entry, author_id: str) -> str:
    publication_id = os.environ.get("MEDIUM_PUBLICATION_ID")
    url = (
        f"{MEDIUM_API}/publications/{publication_id}/posts"
        if publication_id
        else f"{MEDIUM_API}/users/{author_id}/posts"
    )
    tags = [t["term"] for t in entry.get("tags", [])][:MEDIUM_MAX_TAGS]
    body = {
        "title": entry["title"],
        "contentFormat": "html",
        # Medium renders the title itself; the h1 is not repeated in content.
        "content": entry_html(entry),
        # Credits the original for SEO and keeps your blog the source of truth.
        "canonicalUrl": entry["link"],
        "tags": tags,
        "publishStatus": os.environ.get("MEDIUM_PUBLISH_STATUS", DEFAULT_PUBLISH_STATUS),
    }
    r = requests.post(url, headers=medium_headers(token), json=body, timeout=HTTP_TIMEOUT_S)
    r.raise_for_status()
    return r.json()["data"]["url"]


def main() -> int:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    token = os.environ.get("MEDIUM_TOKEN")
    if not token:
        log.error("MEDIUM_TOKEN is not set")
        return 1

    feed = feedparser.parse(RSS_URL)
    if feed.bozo and not feed.entries:
        log.error("could not parse feed: %s", feed.bozo_exception)
        return 1

    seen = load_seen()
    if seen is None:
        # First run: record the backlog so we don't republish the whole archive.
        save_seen({e.get("id", e["link"]) for e in feed.entries})
        log.info("first run: seeded %d existing posts, nothing published", len(feed.entries))
        return 0

    new_entries = [e for e in feed.entries if e.get("id", e["link"]) not in seen]
    if not new_entries:
        log.info("no new posts")
        return 0

    author_id = get_author_id(token)
    failures = 0
    # Oldest first so Medium ordering matches the blog.
    for entry in reversed(new_entries):
        post_id = entry.get("id", entry["link"])
        try:
            medium_url = post_to_medium(token, entry, author_id)
        except requests.RequestException as exc:
            # Leave unseen so the next run retries it.
            log.error("failed to post %s: %s", entry["link"], exc)
            failures += 1
            continue
        seen.add(post_id)
        # Persist after each success so a crash can't cause a duplicate post.
        save_seen(seen)
        log.info("posted %s -> %s", entry["link"], medium_url)

    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
```

## Notes

- The first run only records existing posts. It publishes nothing, so your archive doesn't flood Medium.
- Run it from cron, for example `*/15 * * * * cd /opt/crosspost && python crosspost.py`.
- Keep `MEDIUM_TOKEN` in a secrets manager or env var, never in the repo.
- I haven't run this against the live feed or Medium API. Test it with `draft` first.

I can add a publication-targeting setup or a Slack/Reddit notification step for new posts if you want more reach. Tell me which one.