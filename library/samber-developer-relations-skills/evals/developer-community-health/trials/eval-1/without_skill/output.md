# Tessellate Discord — Monthly Community Health Dashboard

## ⚠️ Read this before anything else

The "9-second median first response" is almost certainly measuring your welcome bot's auto-ack, not a human helping anyone. You described the bot as posting a templated reply in every #help thread within ~5 seconds — a 9-second median first-response time is exactly what you'd expect from that bot alone, independent of whether a real answer ever follows. If the analytics panel's "first response" event fires on *any* reply (bot or human), this number tells you the bot works, not that support works.

This matters because the <24h benchmark almost certainly means "time to first human help," not "time to auto-ack." Reporting 9 seconds against a 24-hour benchmark to leadership would be reporting the wrong metric — and a fantastic-looking wrong metric is more dangerous than a bad one, because nobody goes looking behind it.

**Fix before anything else goes in the monthly deck:** split "first response" into three distinct events.

| Metric | Definition | What it currently tells you |
|---|---|---|
| Time to bot acknowledgment | Timestamp of first bot message − thread creation | What your dashboard reports today (~9s) — bot health, not support health |
| Time to first human response | Timestamp of first non-bot reply − thread creation | Unmeasured. This is the real <24h metric |
| Time to resolution | Timestamp thread marked solved/archived − thread creation | Unmeasured. What members actually experience |

Until "time to first human response" exists as its own tracked event, you cannot honestly claim a position against the 24h benchmark — treat it as **unmeasured**, not as 9 seconds.

---

## 1. Executive scorecard — this month

| Benchmark | Target | Current reading | Status | Note |
|---|---|---|---|---|
| Support response time | < 24h | 9s bot-ack (not the real metric) | 🔴 Unmeasured / likely misreported | See above. Real number could be fine or could be bad — no way to know yet |
| Monthly active ratio | > 20% MAU/members | No tracking in place | 🔴 Unmeasured | Discord doesn't expose this natively; needs instrumentation |
| Staff share of messages | < 30% | No tracking in place | 🟠 Unmeasured, at risk | See §3 — the welcome bot's own posts may push this close to the ceiling by itself |
| Member growth (context, not a pass/fail benchmark) | — | 3,050 → 4,213 (+1,163, +38.1%) since January | 🟢 Healthy acquisition | Growth is top-of-funnel only — it says nothing about whether those 4,213 people are active or helped |

Bottom line: on the three benchmarks leadership actually asked about, you don't yet have an honest answer for any of them. The one number you do have (9s) is measuring the wrong thing. That's the real finding for month one — not a red/green score, but "we were about to report a vanity metric as a success metric."

---

## 2. Why the staff-share benchmark is riskier than it looks

Do the arithmetic before assuming you're under 30%. Take a typical short #help thread: one question, the bot's auto-ack, and a handful of replies.

- Thread of 5 total messages (1 question + 1 bot ack + 3 replies) → the bot's single message is already **20% of that thread's volume**, before any human staff member types a word.
- Add a staff member answering even a third of threads directly, and you cross 30% quietly, without headcount or tone ever feeling "staff-heavy."

Decide now, in writing, whether the welcome bot counts as "staff" for this ratio. Recommendation: yes, but track it as its own category (**automated**) separate from **human staff** and **community**, so you can see which one is actually driving the number:

```
staff_share  = (human_staff_messages + automated_messages) / total_messages   ← what the 30% benchmark checks
human_share  = human_staff_messages / total_messages                          ← the part you can influence via community answers
```

If `automated_messages` alone is near 30%, the fix isn't "staff should reply less" — it's "the bot is doing the counting, not the helping," which is the same root issue as §1.

Scope this ratio to **#help specifically**, not the whole server. Blending in off-topic/general channels (where staff rarely post) will artificially dilute the number and hide a real support-channel problem.

---

## 3. What's missing to compute MAU ratio

Discord's Server Insights (available once Community mode is on) gives you join/leave and some retention curves, but not a clean daily-unique-active-senders count you can turn into a DAU/MAU ratio. You need to log it yourself:

```
MAU ratio = unique human accounts who sent ≥1 message in the last 30 days / total members
```

Two things to decide before the first real reading:
- **Exclude bots from both sides of the ratio** — a bot posting daily is not a member being "active."
- **Denominator: total members (4,213) or non-bot members?** Use non-bot members so the ratio isn't diluted by your own integrations.

---

## 4. Minimal instrumentation to close the gap (before next month's report)

You need one thing: a log of every message with `author_id`, `is_bot`, `has_staff_role`, `channel/thread_id`, `timestamp`, and (for #help) `thread_created_at`. A small script running monthly against the Discord API is enough — no need for a full analytics stack yet.

```js
// monthly-community-health.js — discord.js v14
// Run monthly, scoped to the reporting window (e.g. calendar month).
import { Client, GatewayIntentBits, ChannelType } from 'discord.js';

const STAFF_ROLE_ID = process.env.STAFF_ROLE_ID; // set once, real role id
const HELP_CHANNEL_ID = process.env.HELP_CHANNEL_ID; // forum/parent channel for #help

const client = new Client({ intents: [
  GatewayIntentBits.Guilds,
  GatewayIntentBits.GuildMessages,
  GatewayIntentBits.GuildMembers,
  GatewayIntentBits.MessageContent,
]});

async function run(windowStart, windowEnd) {
  const guild = client.guilds.cache.first();
  const helpChannel = await guild.channels.fetch(HELP_CHANNEL_ID);

  const activeHumans = new Set();
  let totalMessages = 0, staffMessages = 0, botMessages = 0;
  const firstHumanReplyDeltas = [];   // ms, thread creation -> first non-bot reply
  const resolutionDeltas = [];        // ms, thread creation -> archived/closed

  const threads = await helpChannel.threads.fetch({ archived: { fetchAll: true } });

  for (const thread of threads.threads.values()) {
    if (thread.createdTimestamp < windowStart || thread.createdTimestamp > windowEnd) continue;

    const messages = await thread.messages.fetch({ limit: 100 });
    let firstHumanReplyAt = null;

    for (const msg of messages.values()) {
      totalMessages++;
      if (msg.author.bot) { botMessages++; continue; }

      activeHumans.add(msg.author.id);
      const member = await guild.members.fetch(msg.author.id).catch(() => null);
      if (member?.roles.cache.has(STAFF_ROLE_ID)) staffMessages++;

      if (!firstHumanReplyAt && msg.createdTimestamp > thread.createdTimestamp) {
        firstHumanReplyAt = msg.createdTimestamp;
      }
    }

    if (firstHumanReplyAt) {
      firstHumanReplyDeltas.push(firstHumanReplyAt - thread.createdTimestamp);
    }
    if (thread.archived) {
      resolutionDeltas.push(thread.archiveTimestamp - thread.createdTimestamp);
    }
  }

  const members = await guild.members.fetch();
  const humanMemberCount = members.filter(m => !m.user.bot).size;

  return {
    mauRatio: activeHumans.size / humanMemberCount,
    staffShare: (staffMessages + botMessages) / totalMessages,
    humanStaffShareOnly: staffMessages / totalMessages,
    medianFirstHumanResponseMs: median(firstHumanReplyDeltas),
    medianResolutionMs: median(resolutionDeltas),
    threadsWithNoHumanReply: threads.threads.size - firstHumanReplyDeltas.length,
  };
}

function median(arr) {
  if (!arr.length) return null;
  const s = [...arr].sort((a, b) => a - b);
  const mid = Math.floor(s.length / 2);
  return s.length % 2 ? s[mid] : (s[mid - 1] + s[mid]) / 2;
}
```

This gives you, per month: real MAU ratio, real staff share (split automated vs. human), real median time-to-first-human-response, time-to-resolution, and — worth watching closely — **threads with no human reply at all**, which the current 9-second bot metric completely hides.

---

## 5. Monthly reporting template (use this shape going forward)

**Tessellate Discord — Community Health — [Month Year]**

| Section | This month | Last month | Δ | Target | Status |
|---|---|---|---|---|---|
| Total members | 4,213 | — | — | — | 🟢 growth |
| MAU ratio (unique human senders / members) | — | — | — | >20% | 🔴 not yet measured |
| Time to first human response (median) | — | — | — | <24h | 🔴 not yet measured |
| Time to resolution (median) | — | — | — | (no formal target — track as leading indicator) | ℹ️ |
| Staff+bot share of #help messages | — | — | — | <30% | 🔴 not yet measured |
| Human-staff-only share (excl. bot) | — | — | — | (diagnostic, not a target) | ℹ️ |
| Threads with zero human reply | — | — | — | trending to 0 | ℹ️ |
| New members who post within 7 days | — | — | — | (activation signal) | ℹ️ |

Narrative section (3–5 sentences): what changed, one root cause, one action for next month. Don't pad it — leadership wants the row above, not prose.

---

## 6. Before you can say "where we stand"

Honest answer to your actual question right now: **you can't yet score against two of the three benchmarks, and the one number you have for the third is measuring the bot, not the team.** Growth is real and healthy (+38.1% since January), but that's not one of the three benchmarks you were given — don't let it stand in for them in the leadership deck.

Priority order for next 30 days:
1. Split first-response tracking into bot-ack vs. first-human-reply (§1) — this is the single highest-value fix, it's currently misleading, not just incomplete.
2. Ship the logging above, scoped to #help (§4), so next month's report has real MAU and staff-share numbers instead of blanks.
3. Decide and document the bot-counts-as-staff policy (§2) before the first real staff-share number lands, so it isn't relitigated the moment the number looks bad.