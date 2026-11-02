Here's the two sections, ready to drop into the tutorial as-is — a learning objective block for the top (right under the title, before Step 1) and a summary block for the bottom (right after Step 9).

---

### Top: Learning Objective

```markdown
## What you'll learn

This tutorial gets you from zero to publishing and consuming your first event with the Nomadic Labs streaming SDK. It assumes you're already comfortable with our REST API — so instead of re-explaining auth or general concepts, each step calls out where the streaming model works differently from the request/response pattern you already know.

By the end, you'll be able to:

- Install and configure the streaming CLI against your environment
- Read and modify the SDK config file with confidence
- Create a stream and a consumer group, and know when you need each
- Find and list your existing streams
- Navigate the admin dashboard to inspect stream and consumer state
- Publish an event and consume it back through the SDK
- Know which of our other SDKs to reach for outside this workflow

**Time to complete:** ~20–30 minutes
**Prerequisites:** A Nomadic Labs account with API access; comfort with our REST API and the command line
```

---

### Bottom: Summary

```markdown
## Summary

You went from an empty environment to a working end-to-end streaming flow: installing the CLI, understanding the config file, creating a stream and a consumer group, and publishing and consuming your first event through the admin dashboard and the SDK.

The core shift from the REST API is worth restating: streams and consumer groups are long-lived resources you create once and read from continuously, not one-off request/response calls. The consumer group you created in step 5 is what lets you resume consumption where you left off instead of replaying the whole stream.

**Where to go next:**

- Explore the other SDKs covered in step 9 if your stack needs a language we didn't use here
- Use the admin dashboard from step 6 to monitor consumer lag and stream health as you build
- Reach out to support if a stream or consumer group ends up in a state this tutorial didn't cover
```

---

Drop the first block directly under the tutorial's title, and the second right after the last step. Both are scoped to only the two additions you asked for — the nine steps themselves are untouched.