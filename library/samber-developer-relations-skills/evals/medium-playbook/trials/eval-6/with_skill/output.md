**Next action:** run the script below on a cron, and import each flagged post by hand. I did not build two of the three things you asked for, because `medium-playbook` rules them out.

## What I didn't build, and why

| Your request | Verdict | Reason |
|---|---|---|
| Create a Medium integration token | ❌ Not possible | Medium accepts no new API tokens. Publishing goes through the editor or **Stories > Import a story** [platform]. |
| Post via API with `canonicalUrl` | ❌ Not possible | Same cause. The import tool sets the canonical link and original date automatically, and only the story's author can set one [platform]. |
| Auto-reply to every new `kubernetes` story with a link to your operator | ❌ Refused | Bulk or programmatic responses, and responses used for promotion, are banned. Reach is lost first and the account can be suspended [platform]. Even a hand-written response that points at your own product is spam. |

Tag search is a smaller problem. Medium has no documented search API, so the script reads the public tag RSS feed instead. That feed is my own reasoning, not a platform guarantee, and Medium may change or block it.

**Why "everywhere" backfires here:** a promotional response gets your account flagged, and your brand's stories then reach followers only. A response that adds a fact and has no link earns profile visits, and the playbook calls that "earn-first".

## What the script does

1. Polls `blog.tessera.dev/rss` and remembers which posts it has seen.
2. For each new post, runs the playbook's hygiene checks:
   - **Teaser check:** the playbook calls a clipped story spam.
   - **English-only check:** other languages get no reach.
   - **Strip-the-product test reminder.**
3. Writes an import checklist for the named author, with the canonical URL, the AI-label reminder and the paywall-off reminder.
4. Builds a digest of recent `kubernetes` stories for a human to read and answer. It posts nothing.

```python
#!/usr/bin/env python3
"""DevRel helper: queue new Tessera blog posts for canonical import to Medium.

Medium has no token or API for publishing, and bulk or programmatic responses
are banned, so this script prepares work for humans and posts nothing.

Usage:
    python3 medium_import_queue.py            # poll once (run from cron)
    python3 medium_import_queue.py --digest   # also write a k8s reading digest

Environment:
    SLACK_WEBHOOK_URL   optional; notifies the DevRel channel of new posts.
"""

import argparse
import html
import json
import logging
import os
import re
import sys
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path

BLOG_RSS_URL = "https://blog.tessera.dev/rss"
# Medium publishes public RSS per tag; undocumented as a contract, so failures are non-fatal.
MEDIUM_TAG_FEED_URL = "https://medium.com/feed/tag/kubernetes"

STATE_FILE = Path("medium_import_state.json")
OUTPUT_DIR = Path("medium_queue")

HTTP_TIMEOUT_S = 20  # cron job; a hung feed must not block the next run
USER_AGENT = "tessera-devrel-import-queue/1.0 (+https://blog.tessera.dev)"

# Medium counts a story as short-form at 150 words or fewer; a post this short
# in the RSS body is almost certainly a clipped teaser, which Medium treats as spam.
TEASER_WORD_THRESHOLD = 150
# Max remembered GUIDs, so the state file cannot grow without bound.
MAX_SEEN_IDS = 500
# A digest longer than this stops being read; the playbook budgets under 1 hour per response.
DIGEST_MAX_ITEMS = 10
# Crude English check: share of ASCII letters among letters. Medium reviews English only.
ENGLISH_ASCII_RATIO_MIN = 0.95

NS = {"content": "http://purl.org/rss/1.0/modules/content/"}
TAG_RE = re.compile(r"<[^>]+>")
WORD_RE = re.compile(r"\w+")

log = logging.getLogger("medium_import_queue")


def fetch(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=HTTP_TIMEOUT_S) as resp:
        return resp.read()


def strip_html(raw: str) -> str:
    return html.unescape(TAG_RE.sub(" ", raw or ""))


def parse_items(xml_bytes: bytes) -> list[dict]:
    root = ET.fromstring(xml_bytes)
    items = []
    for item in root.iter("item"):
        full = item.findtext("content:encoded", default="", namespaces=NS)
        desc = item.findtext("description", default="")
        body = strip_html(full or desc)
        items.append(
            {
                "id": item.findtext("guid") or item.findtext("link") or "",
                "title": (item.findtext("title") or "").strip(),
                "link": (item.findtext("link") or "").strip(),
                "author": (
                    item.findtext("{http://purl.org/dc/elements/1.1/}creator") or ""
                ).strip(),
                "has_full_content": bool(full),
                "words": len(WORD_RE.findall(body)),
                "text": body,
            }
        )
    return items


def load_seen() -> set[str]:
    if not STATE_FILE.exists():
        return set()
    # A corrupt state file would re-queue the whole feed; fail loudly instead.
    return set(json.loads(STATE_FILE.read_text()))


def save_seen(seen: list[str]) -> None:
    STATE_FILE.write_text(json.dumps(seen[-MAX_SEEN_IDS:], indent=2))


def hygiene_flags(item: dict) -> list[str]:
    flags = []
    if not item["has_full_content"]:
        flags.append("RSS has no full text: check the feed is not publishing excerpts only")
    if item["words"] <= TEASER_WORD_THRESHOLD:
        flags.append(f"{item['words']} words: reads as a teaser; Medium removes teasers as spam")
    letters = [c for c in item["text"] if c.isalpha()]
    if letters and sum(c.isascii() for c in letters) / len(letters) < ENGLISH_ASCII_RATIO_MIN:
        flags.append("text looks non-English: no Boost, followers-only reach")
    if not item["author"]:
        flags.append("no named author in the feed: import under a named engineer, not a brand account")
    return flags


def write_checklist(item: dict, flags: list[str]) -> Path:
    OUTPUT_DIR.mkdir(exist_ok=True)
    slug = re.sub(r"[^a-z0-9]+", "-", item["title"].lower()).strip("-")[:60] or "post"
    path = OUTPUT_DIR / f"{datetime.now(timezone.utc):%Y-%m-%d}-{slug}.md"
    flag_block = "\n".join(f"- ⚠️ {f}" for f in flags) or "- ✅ no automatic flags"
    path.write_text(
        f"# Import to Medium: {item['title']}\n\n"
        f"Author: {item['author'] or 'UNKNOWN'}\n"
        f"Canonical URL: {item['link']}\n\n"
        f"## Automatic flags\n{flag_block}\n\n"
        "## Steps (the named author does these)\n"
        "1. Strip-the-product test: remove our product name; if nothing worth reading is left, skip Medium.\n"
        "2. Medium > Stories > Import a story > paste the canonical URL above.\n"
        "3. Check Story settings > More settings > Advanced settings shows the original URL.\n"
        "4. Pick up to 5 topics the story is really about. Paywall off.\n"
        "5. Add an affiliation line in the first paragraph. Add an AI-assistance label in the first two paragraphs if it applies.\n"
        "6. Submit to the company publication; feature it if it is this week's best (4 credits, +1 per 7 days).\n"
        "7. Answer responses within two days.\n"
    )
    return path


def notify_slack(message: str) -> None:
    url = os.environ.get("SLACK_WEBHOOK_URL")
    if not url:
        return
    req = urllib.request.Request(
        url,
        data=json.dumps({"text": message}).encode(),
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=HTTP_TIMEOUT_S):
        pass


def write_digest() -> Path:
    """List recent k8s stories for a human to read and answer. Posts nothing."""
    items = parse_items(fetch(MEDIUM_TAG_FEED_URL))[:DIGEST_MAX_ITEMS]
    OUTPUT_DIR.mkdir(exist_ok=True)
    path = OUTPUT_DIR / f"digest-k8s-{datetime.now(timezone.utc):%Y-%m-%d}.md"
    lines = [
        "# Kubernetes stories worth a real response\n",
        "Respond only where you hold a first-hand fact the author can use.",
        "No links to our stories or product. Code blocks do not render in responses.\n",
    ]
    lines += [f"- [{i['title']}]({i['link']}) by {i['author']}" for i in items]
    path.write_text("\n".join(lines) + "\n")
    return path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--digest", action="store_true", help="also write the k8s reading digest")
    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

    try:
        items = parse_items(fetch(BLOG_RSS_URL))
    except (urllib.error.URLError, ET.ParseError, TimeoutError) as exc:
        log.error("cannot read %s: %s", BLOG_RSS_URL, exc)
        return 1

    seen_list = sorted(load_seen())
    seen = set(seen_list)
    new_items = [i for i in items if i["id"] and i["id"] not in seen]
    log.info("%d items in feed, %d new", len(items), len(new_items))

    for item in new_items:
        flags = hygiene_flags(item)
        path = write_checklist(item, flags)
        log.info("queued %s -> %s (%d flags)", item["link"], path, len(flags))
        try:
            notify_slack(f"New post ready for Medium import: {item['title']} ({path})")
        except (urllib.error.URLError, TimeoutError) as exc:
            # Checklist is on disk, so the work is not lost; surface the failure anyway.
            log.error("slack notification failed: %s", exc)
        seen_list.append(item["id"])

    save_seen(seen_list)

    if args.digest:
        try:
            log.info("digest written: %s", write_digest())
        except (urllib.error.URLError, ET.ParseError, TimeoutError) as exc:
            log.error("tag feed unavailable: %s", exc)
            return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

I did not run this script, so it is untested.

## How to use it (about 15 min of setup)

1. Run `python3 medium_import_queue.py --digest` once to seed the state file and check the feed parses.
2. Add it to cron, daily is enough for a blog.
3. When a checklist appears, the named engineer imports the post (under an hour per post). Give the import a day or two before the next one.
4. Once a week, someone reads the digest and writes substantive responses to a few stories. These responses carry no links.

## Template for an earn-first response (from the playbook)

```text
✓ Good: adds a fact, no link
We hit the same operator reconcile storm once CRDs passed 2k objects:
batching status updates every 5 s cut API-server load by half. Did you
try rate-limiting the workqueue, or did sharding come first?

✗ Bad: reads as promotion through responses
Great post! Our operator solves exactly this, check it out: tessera.dev
```

(The numbers are made up. Use your own.)

## Where your operator link can go

- **Canonical import:** the post keeps its link home. The playbook ranks this as the best value per hour.
- **One closing call to action** in a native first-hand story, such as a repo or docs link. Say you work on Tessera in the first paragraph.
- **Established tech publications,** such as ITNEXT or Level Up Coding. Read each one's current rules first, and ask the editor before any paid-plan mention. A free tier or open-source repo usually reads as acceptable.

## Open questions (they change the plan)

1. Do the posts have named engineers as authors? If not, import should wait. Boost rewards first-hand experience, which a brand account cannot show.
2. Is the blog English-only? Other languages reach followers only.
3. Roughly how many hours a week can the team spend? Under 2 hours means imports and a few responses, nothing more.