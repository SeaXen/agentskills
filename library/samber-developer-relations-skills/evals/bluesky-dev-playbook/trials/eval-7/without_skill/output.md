# Verdict

1. **Paid posts without disclosure: don't do it.** Disclose, and you can still keep the posts authentic.
2. **Mastodon to Bluesky mirror:** fine. A working script is below, plus a no-code option.

---

## 1. Undisclosed paid posts

I'd say no, for three reasons.

- **It's illegal in most markets.** In the US, the FTC Endorsement Guides (16 CFR 255) require a clear disclosure of any paid relationship. Hiding it is deceptive advertising. In the EU, hidden advertising is a banned unfair practice. France has a specific influencer law that requires labels like "Publicité" or "Collaboration commerciale". Liability lands on Velarion as well as the three developers. I'm not a lawyer, so run this past yours.
- **It will probably leak.** The Go community is small. Someone will notice three well-known developers posting about the same SDK in the same week. Once "undisclosed paid shills" is the story, it outweighs the SDK launch.
- **It cuts against what makes these developers valuable.** Their credibility is the asset you're paying for. Burning it for them is a bad trade, and they carry most of the downside.

**What to do instead:**

1. **Disclose plainly.** Bluesky has no branded-content tool, so put it in the text. Examples:
   - "Velarion pays me to try their Go SDK. Honest notes below."
   - "#ad Sponsored by Velarion."
2. **Write the contract for honesty.** Require the disclosure. Give no script and no approval rights over opinions. Let them name what they dislike. A post that says "paid, and the retry API is clunky, but the typed errors are great" persuades better than polished praise.
3. **Give them real access.** Offer early builds, a direct channel to the SDK maintainers, and a hands-on task such as "port one of your services". Posts about actual use feel organic because they are.
4. **Add unpaid reach alongside it.** Ship a good quickstart, answer questions in public, and post as the Velarion team. Those need no disclosure.

If they "would rather not mention it", that is the moment to renegotiate. Developers who insist on hiding it are the risk to the launch.

---

## 2. Mastodon (fosstodon) to Bluesky

### Option A: no code

Bridgy Fed can bridge a Fediverse account into Bluesky. You opt in by following its bridge account from Mastodon. The bridged account has a bridge-style handle, not a custom one, and replies don't round-trip cleanly. Check the current docs before relying on it.

### Option B: the script

**What it does:**

- Mirrors public toots only, oldest first, with original timestamps.
- Skips boosts, replies, and unlisted or private toots.
- Keeps link and hashtag facets, so links stay clickable.
- Copies up to 4 images with alt text, re-encoded under Bluesky's size cap.
- Posts longer than 300 characters are cut and end with a "↗ original" link.
- Toots with video or GIF attachments also get the link.
- Saves progress in a state file after every post, so it is safe to rerun.

**Install:** `pip install atproto requests pillow`

**Environment:**

| Variable | Value |
|---|---|
| `MASTODON_HOST` | `fosstodon.org` |
| `MASTODON_ACCT` | your username, without the `@` |
| `BSKY_HANDLE` | the new Bluesky handle |
| `BSKY_APP_PASSWORD` | an app password from Bluesky settings; never use the main password |
| `STATE_FILE` | optional, defaults to `state.json` |

```python
#!/usr/bin/env python3
"""Mirror public toots from a Mastodon account to a Bluesky account.

Usage: mirror.py [--backfill] [--dry-run]
Env:   MASTODON_HOST, MASTODON_ACCT, BSKY_HANDLE, BSKY_APP_PASSWORD, STATE_FILE (optional)
Deps:  pip install atproto requests pillow
"""
import argparse
import io
import json
import os
import time
from html.parser import HTMLParser
from pathlib import Path

import requests
from atproto import Client, client_utils, models
from PIL import Image

BSKY_LIMIT = 300           # Bluesky post length cap (code points here; graphemes <= code points, so safe)
MAX_BLOB_BYTES = 950_000   # Bluesky image cap is 1,000,000 bytes; margin for safety
MAX_IMAGES = 4             # Bluesky image embed cap
PAGE_SIZE = 40             # Mastodon max page size for the statuses endpoint
HTTP_TIMEOUT = 30          # seconds; avoid hanging a cron run forever
POST_DELAY = 1.0           # seconds between posts; keeps backfills far below Bluesky write limits
ORIGINAL_LABEL = "↗ original"
JPEG_QUALITIES = (90, 80, 70, 60, 50)
MAX_IMAGE_SIDE = 2000      # px; downscale before trying qualities


class Segmenter(HTMLParser):
    """Turns Mastodon HTML into (kind, text, arg) segments: text | link | tag | mention."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.segs, self._kind, self._href, self._buf = [], None, None, []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "br":
            self.segs.append(("text", "\n", None))
        elif tag == "a":
            cls = a.get("class") or ""
            self._href = a.get("href")
            self._kind = "tag" if "hashtag" in cls else "mention" if "mention" in cls else "link"
            self._buf = []

    def handle_endtag(self, tag):
        if tag == "p":
            self.segs.append(("text", "\n\n", None))
        elif tag == "a" and self._kind:
            self.segs.append((self._kind, "".join(self._buf), self._href))
            self._kind = None

    def handle_data(self, data):
        (self._buf if self._kind else self.segs).append(data if self._kind else ("text", data, None))


def to_segments(html):
    p = Segmenter()
    p.feed(html)
    segs = p.segs
    while segs and segs[-1][0] == "text" and not segs[-1][1].strip():
        segs.pop()
    return segs


def build(segs, toot_url, force_link):
    total = sum(len(t) for _, t, _ in segs)
    needs_link = total > BSKY_LIMIT or force_link
    budget = BSKY_LIMIT - (len(ORIGINAL_LABEL) + 1 if needs_link else 0)
    tb, used = client_utils.TextBuilder(), 0
    for kind, text, arg in segs:
        if used + len(text) > budget:
            if kind == "text":
                tb.text(text[: budget - used])
            break
        used += len(text)
        if kind == "link" and arg:
            tb.link(text, arg)
        elif kind == "tag":
            tb.tag(text, text.lstrip("#"))
        else:
            tb.text(text)
    if needs_link:
        tb.text("\n")
        tb.link(ORIGINAL_LABEL, toot_url)
    return tb


def fit_image(data):
    img = Image.open(io.BytesIO(data)).convert("RGB")
    img.thumbnail((MAX_IMAGE_SIDE, MAX_IMAGE_SIDE))
    for q in JPEG_QUALITIES:
        buf = io.BytesIO()
        img.save(buf, "JPEG", quality=q)
        if buf.tell() <= MAX_BLOB_BYTES:
            return buf.getvalue()
    raise RuntimeError("image cannot be shrunk under the Bluesky blob limit")


def fetch_statuses(host, account_id, since_id, max_pages=None):
    params = {"exclude_replies": "true", "exclude_reblogs": "true", "limit": PAGE_SIZE}
    if since_id:
        params["since_id"] = since_id
    out, pages = [], 0
    while max_pages is None or pages < max_pages:
        r = requests.get(f"https://{host}/api/v1/accounts/{account_id}/statuses",
                         params=params, timeout=HTTP_TIMEOUT)
        r.raise_for_status()
        batch = r.json()
        if not batch:
            break
        out += batch
        params["max_id"] = batch[-1]["id"]
        pages += 1
    return out


def publish(client, status):
    segs = to_segments(status["content"])
    if status.get("spoiler_text"):
        segs = [("text", status["spoiler_text"] + "\n\n", None)] + segs
    media = status["media_attachments"]
    images = [m for m in media if m["type"] == "image"][:MAX_IMAGES]
    tb = build(segs, status["url"], force_link=len(media) > len(images))
    embed = None
    if images:
        items = []
        for m in images:
            resp = requests.get(m["url"], timeout=HTTP_TIMEOUT)
            resp.raise_for_status()
            blob = client.upload_blob(fit_image(resp.content)).blob
            items.append(models.AppBskyEmbedImages.Image(alt=m.get("description") or "", image=blob))
        embed = models.AppBskyEmbedImages.Main(images=items)
    lang = status.get("language")
    record = models.AppBskyFeedPost.Record(
        text=tb.build_text(), facets=tb.build_facets(), embed=embed,
        langs=[lang] if lang else None, created_at=status["created_at"])
    client.com.atproto.repo.create_record(models.ComAtprotoRepoCreateRecord.Data(
        repo=client.me.did, collection="app.bsky.feed.post", record=record))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--backfill", action="store_true", help="mirror full history on first run")
    ap.add_argument("--dry-run", action="store_true", help="print, post nothing, save nothing")
    args = ap.parse_args()

    host, acct = os.environ["MASTODON_HOST"], os.environ["MASTODON_ACCT"]
    state_file = Path(os.environ.get("STATE_FILE", "state.json"))
    last_id = json.loads(state_file.read_text())["last_id"] if state_file.exists() else None

    r = requests.get(f"https://{host}/api/v1/accounts/lookup", params={"acct": acct}, timeout=HTTP_TIMEOUT)
    r.raise_for_status()
    account_id = r.json()["id"]

    if last_id is None and not args.backfill:
        # First run without --backfill: mark current position, mirror only future toots.
        newest = fetch_statuses(host, account_id, None, max_pages=1)
        last_id = max((s["id"] for s in newest), key=int, default="0")
        if not args.dry_run:
            state_file.write_text(json.dumps({"last_id": last_id}))
        print(f"seeded at {last_id}; nothing posted")
        return

    todo = [s for s in fetch_statuses(host, account_id, last_id) if s["visibility"] == "public"]
    todo.sort(key=lambda s: int(s["id"]))
    client = None
    if not args.dry_run:
        client = Client()
        client.login(os.environ["BSKY_HANDLE"], os.environ["BSKY_APP_PASSWORD"])
    for s in todo:
        if args.dry_run:
            print(s["id"], s["url"])
            continue
        publish(client, s)  # raises on failure: state stays on the last success, next run retries
        state_file.write_text(json.dumps({"last_id": s["id"]}))
        print("mirrored", s["url"])
        time.sleep(POST_DELAY)


if __name__ == "__main__":
    main()
```

**How to run it:**

1. Run `./mirror.py --dry-run --backfill` first. It prints what it would post.
2. **Posts to Bluesky and writes the state file:** `./mirror.py --backfill` for the first run with full history. Without `--backfill`, the first run only records the current position.
3. **Posts to Bluesky and writes the state file:** schedule `./mirror.py` in cron, for example every 5 minutes.

### Caveats

- **Backdated posts:** history is imported with original timestamps. Check how it looks on a throwaway account first.
- **Mentions:** `@someone@instance` stays plain text on Bluesky. It won't notify anyone.
- **GIFs and video:** these are not uploaded, only linked.
- **Threads:** self-reply chains are skipped, because `exclude_replies` drops all replies.
- **Edits and deletes:** these are not synced. Edited or deleted toots stay as first posted.
- **One-way only:** Bluesky replies never reach Mastodon.
- **Automation label:** mark the Bluesky account as automated in its bio.
- **Not run:** I haven't run this script. The dry run on step 1 is your first test.

If you want, I can add edit and delete sync, or a two-way reply notice.