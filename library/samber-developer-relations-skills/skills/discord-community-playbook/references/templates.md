# Discord templates

Examples for a fictional product, "Kestrel", a Postgres migration CLI. Adapt every line to the user's product and voice, then run a humanizer pass. Never post a template unedited.

## 1. Answer in someone else's help channel

```text
// ✓ Good - answers in full, discloses, no link unless it is the answer
You're hitting the lock timeout because ALTER TABLE takes an ACCESS
EXCLUSIVE lock and waits behind the open transaction from your worker.
Two fixes: set lock_timeout = '3s' on the migration session and retry,
or run the change as a new column + backfill + swap. (I work on Kestrel,
a migration tool, but you don't need it for this.)

// ✗ Bad - praise plus product link, no answer
Great question! Kestrel handles this automatically, check it out: {url}
```

## 2. Ask a host server's moderators before anything commercial

For an individual maintainer or an indie project. A funded vendor asks for a hosted Q&A (template 3) instead: showcase channels often favour individuals.

```text
Hi {mod team}, I work on Kestrel (open-source Postgres migration CLI)
and I've been answering migration questions in #databases for a few
weeks. We ship 2.0 on {date}. Would a single post in #i-built-this be
welcome, or would you rather we skip it? Happy to follow whatever you
prefer.
```

## 3. Hosted Q&A pitch to a host server

```text
Subject: Q&A offer for #q-and-a: zero-downtime Postgres migrations

Hi {server}, I'm {name}, maintainer of Kestrel. Your members ask about
locking during migrations about weekly. I'd do a 45-minute text Q&A on
zero-downtime schema changes: no slides, no pitch, I answer what they
bring. Any slot from {dates} works. If it doesn't fit, no problem.
```

## 4. Help forum post guidelines (own server)

```text
Before posting:
1. Search this forum and the docs: {docs link}.
2. Title = the error or goal in one line ("ALTER TABLE hangs on 40M rows").
3. Include: Kestrel version, Postgres version, the command, the full output.
   Never paste API keys, tokens, connection strings or customer data: this
   channel is public and can appear on the web. Redact logs first.
4. Pick one tag: bug / question / showcase / feature-request.
When your issue is solved, add the "solved" tag so the next person finds it.
Staff answer every post by the next working day ({time zones}).
```

## 5. Onboarding question (own server)

```text
Question: What brings you here? (multiple answers allowed)
- I need help with Kestrel        -> #help-forum, #announcements
- I'm contributing code           -> #contributors, #dev-chat, role: contributor
- I want release news only        -> #announcements
- I'm evaluating migration tools  -> #general, #showcase
```

## 6. Release announcement (announcement channel, published to followers)

```text
Kestrel 2.0 is out.
- Online index builds now resume after a crash.
- `kestrel plan` shows the lock each step takes.
- Breaking: config key `timeout` renamed `lock_timeout` (migration guide: {link}).
Questions go in #help-forum. Full notes: {link}
```

No @everyone: followed servers strip it, and members who mute it miss the next one.

## 7. Web Presence notice to members (before going Discoverable)

```text
Heads-up: this server becomes Discoverable on {date}. From then:
- AI-written summaries of #general and #help-forum appear on our public
  server page and in web search, without usernames. Discord offers no
  personal setting for summaries; we choose the channels.
- Later, individual messages from those channels can appear too, but
  only if your own setting allows it (User Settings > Data & Privacy).
  It is off by default in the EU, UK, Canada, Brazil, Australia and
  South Korea. Teen accounts never appear.
- #contributors never appears: only the contributor role can view it.
Questions: reply here.
```

## 8. Partnership announcement (no DMs)

```text
We're partnering with the {Partner} server: they run the Postgres
performance community many of you already read. Their #announcements
now follows ours, so Kestrel releases show up there. Their rules apply
when you post there: {link}.
```
