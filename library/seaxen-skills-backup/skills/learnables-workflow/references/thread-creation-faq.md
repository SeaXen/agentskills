# Thread Creation Behavior - FAQ

## Why does a thread auto-create when I say "learn this"?

**Answer**: Because you're in a **Learnables channel** (`#🔰|learnables`), and the `learnables-workflow` skill is auto-loaded.

Per **Procedure B.5** of the learnables workflow:
> Discord only: if message is top-level in learnables parent channel, call `discord` `create_thread` anchored to triggering `message_id`, then continue in that thread.

### Purpose
- **Organization**: Keeps research, review, and commit phases in one dedicated thread
- **Prevents clutter**: Stops the learnables channel from filling with long research discussions
- **Context preservation**: All related messages stay grouped together

### How It Works
1. You post a message in `#🔰|learnables` (e.g., "learn this Scrapy")
2. Hermes detects it's a **top-level message** in a learnables channel
3. Hermes **automatically creates a thread** anchored to your message ID
4. All subsequent research, questions, and commits happen in that thread

### Can I Disable This?

**No, not in a learnables channel.** Thread creation is hardwired for learnables workflows.

**Workarounds:**
1. Move to a **non-learnables channel** - thread creation won't trigger
2. Use `/learn` command directly (if configured) - may bypass auto-thread depending on setup

### Common Confusion

**Q: "Why does it create a thread when I just want a quick answer?"**
A: Learnables mode assumes you want a **structured learning process** (research → review → commit). For quick answers, use a regular channel.

**Q: "Can I make it not create threads?"**
A: Remove the channel from learnables configuration, or move the discussion elsewhere.

### Configuration

Thread creation is controlled by:
- `~/.hermes/learnables/config.yaml` - lists learnables channel IDs
- `python3 ~/.hermes/learnables/apply_config.py` - applies config to Hermes
- Discord bot needs `Create Public Threads` permission

### Verification

To check if a channel is configured for learnables:
```bash
cat ~/.hermes/learnables/config.yaml
```

To test:
1. Post a test message in the channel
2. Hermes should create a thread automatically
3. If not, check bot permissions and config

---

*Source: User question from session + learnables-workflow Procedure B.5*