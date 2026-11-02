## Subject, preview and intro for Ferncastle Dev Digest #37

**Subject** (45 characters)

> TypeScript SDK 5.0: ESM-only, Node 18 dropped

**Preview text** (about 100 characters)

> If you run Node 18 or build CommonJS, read this before you bump the version. Migration steps inside.

**Intro**

Drop it. The skill allows an opener only when something changed, such as the schedule, the format or a correction owed. You said nothing changed, so a "welcome to the October edition" line is filler. Some inboxes now show a generated summary instead of the preview, so the first paragraph under the lead headline carries the news:

> **[TypeScript SDK 5.0 is out: ESM-only builds, Node 18 dropped](LINK-TO-CHANGELOG)**
> Node 18 is no longer supported, and 5.0 ships ESM-only builds. If you run Node 18 or load the SDK from CommonJS, change that before you upgrade. [Migration guide](LINK-TO-GUIDE).

### What I changed in your draft

- **Subject:** It now names the lead item. "#37", "October Edition" and the 🚀 tell the reader nothing about what's inside. Put the issue number in the archive title or the sender name instead.
- **Intro:** I cut "busy month", "tons of exciting updates" and "grab a coffee and dive in". They are on the hype list, and they promise content without naming any.
- **Breaking change first:** Per the release order, the copy says what stops working, then the action, then the guide link. The ESM-only change comes first because it affects the most readers.

### Open before sending

- ❌ **Blocked, links:** I need the changelog and migration guide URLs. I can't check them from here.
- ❌ **Blocked, CommonJS wording:** "Load the SDK from CommonJS" is my reading of "ESM-only". Confirm it matches the migration guide. If the guide names a minimum Node version, add it. I didn't invent one.
- ⚠️ **Deadline:** If 4.x keeps getting fixes for Node 18 users, add one line with the end date. Include it only if it's already announced.
- ℹ️ **Preview padding:** If your sending tool has no preview-text field, pad the hidden text so the first body line doesn't leak into the inbox preview.
- ℹ️ **Test send:** Do one before tomorrow and check the subject and preview in Gmail and Apple Mail.