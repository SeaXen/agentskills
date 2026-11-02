# Orrery Weekly #58: draft for tonight

I couldn't open any of the three links. The sandbox blocked the fetch, and `.internal` hosts are probably unreachable from here anyway. Every item below comes only from what you told me, and any line I couldn't source is marked **blocked**.

I did not invent forum threads or generic tips for the empty sections. A summary of a thread I haven't read is a claim I can't source, and the skill bars padding a section with filler. All 7 headings stay, as you asked, and each empty one says so in one line and asks readers to submit.

## 1. Running order and subject options

Order: Lead, Project news, Ecosystem, Community showcase, Help wanted, Tutorials, Events, ask, footer. There's no sponsor this issue, as far as I know.

1. **"Scheduler rewrite RFC approved"** (30 characters). It names the lead item, so it's the safest option.
2. **"RFC 412: the new Orrery scheduler"** (34). It names the RFC number, but "new" overstates it, since approval isn't shipping.
3. **"Orrery Weekly #58: scheduler RFC"** (33). It's plain, but the issue number adds nothing.

I'd pick option 1. I've drafted with it.

## 2. The issue

**Subject:** Scheduler rewrite RFC approved
**Preview:** RFC 412 is approved: the Orrery scheduler gets a rewrite. Plus: Q3 performance notes and a new docs guide.

(The preview is 109 characters. The news is in the first 35.)

**Opener:** none. Nothing changed in schedule or format.

### Lead

**[RFC 412: the scheduler rewrite is approved](https://wiki.orrery.internal/rfc-412)**
The RFC proposing a rewrite of the Orrery scheduler was approved on Tuesday. **[blocked: add one sentence on what changes for users, plus timeline and availability, from the RFC or your own note]**

### Project news

**[BLOCKED: title needed](https://wiki.orrery.internal/notes/perf-2024-q3)**
Q3 performance notes. **[blocked: I need the page title and a person to read it. I won't quote any figure from internal notes unless a published post states it.]**

### Ecosystem

Nothing from the wider ecosystem this week. Seen a post, release or talk worth sharing? Reply and we'll consider it for #59.

### Community showcase

No showcase this week. Built something with Orrery? Reply with a link and a line about it.

### Help wanted

Nothing open this week. Maintainers: reply with a task where you'd like a hand.

### Tutorials

**[BLOCKED: title needed](https://docs.orrery.internal/guides/9a7f2c)**
A docs guide. **[blocked: I need the guide's title and a one-line summary from you, or someone has to read it. I won't build a headline from the URL slug.]**

### Events

No events to list this week.

### Ask

**Reply to this email** with a project for the showcase or a task for Help wanted in #59.

### Footer

Submit an item: reply to this email. Spotted an error? Reply and we'll fix the archive. [Archive link] · [Unsubscribe] · [sender address]

## 3. Plain-text part

```
ORRERY WEEKLY #58

LEAD
RFC 412: the scheduler rewrite is approved
https://wiki.orrery.internal/rfc-412
The RFC proposing a rewrite of the Orrery scheduler was approved on Tuesday.

PROJECT NEWS
[title needed]
https://wiki.orrery.internal/notes/perf-2024-q3

ECOSYSTEM
Nothing this week. Reply with a post, release or talk to share.

COMMUNITY SHOWCASE
Nothing this week. Reply with a link to something you built.

HELP WANTED
Nothing open this week. Maintainers: reply with a task.

TUTORIALS
[title needed]
https://docs.orrery.internal/guides/9a7f2c

EVENTS
None this week.

REPLY with a showcase project or a Help wanted task for #59.

Submit an item or report an error: reply to this email.
Archive: [url]
Unsubscribe: [url]
```

## 4. Pre-send report

**Issue is thin.** Only 2 of the 6 content sections have an item, and the skill's threshold is half. You can ship it as drafted, ship it shorter, or fold it into #59. Keeping 4 near-empty sections is your call, but readers who see "nothing this week" four times may skim the next issue.

**Blocked, needs you:**
- **Internal links.** All three URLs are `.internal`. If the newsletter goes to the public, readers will get dead links. Please confirm they resolve for readers, or give me public versions.
- **Lead.** I need what changes for the reader, a timeline, and availability.
- **Project news and Tutorials.** I need titles. A person must read both pages before send.
- **Date of the perf notes.** The URL says `perf-2024-q3`, but today is 2026-10-30. Check that this isn't a stale page.
- **"Approved Tuesday".** I wrote "on Tuesday". If the issue goes out later than this week, change it to the date.
- **Test send.** I need one checked in Gmail, Apple Mail on a phone, and classic Outlook, in light and dark mode. Mark it blocked if you can't send one.
- **Archive page.** It must exist and match the send.
- **Link resolution.** Every link must resolve through the click-tracking domain in the test send.

**Pass:**
- The subject is 30 characters and names the lead.
- The preview is 109 characters and doesn't repeat the subject.
- There is one issue-level ask.
- No sponsor slot is used.
- There are no hype words, no invented figures and no code blocks.

**Open questions, if you want a fuller pass:**
1. Which sending tool are you using, and does it have a preview-text field?
2. Is there a charter with empty-section rules? I applied "keep the heading, one honest line" because you said readers expect all 7.
3. If you want the empty sections filled with real content, that is item sourcing, and the sourcing skill (`devrel-newsletter-sourcing`) handles it. Give me 2–3 links you've actually read, and I'll write them up.

I'm storing the subject, lead item and the "ship thin" decision as task memory for #59.