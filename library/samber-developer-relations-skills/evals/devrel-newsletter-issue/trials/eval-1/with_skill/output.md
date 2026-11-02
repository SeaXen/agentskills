# Quillstack developer digest: Shipped section and subject line

The skill covers a single part of the issue here, so I skipped the full interview and the running-order gate. You have no charter or previous issue, so I used the default section order (Lead, Shipped, …). If your programme has a template, that is the gap `devrel-newsletter-program` covers. If Streams 2.0 sits in Lead rather than Shipped, the item text moves unchanged.

## Subject options (recommend #1)

1. **Streams 2.0 is GA for Team and Enterprise** (41 chars). It names the lead and the plans, so Free readers aren't misled. It is the safest option.
2. **Streams 2.0 is now generally available** (38). It is shorter, but it says nothing about plans, and Free readers may click expecting access.
3. **Streams 2.0 GA, plus qs replay in the CLI** (41). It names two items, so the lead is weaker.

## Send-ready copy (subject #1)

**Subject:** Streams 2.0 is GA for Team and Enterprise

**Preview text** (104 chars; your tool's preview field should add the padding):
Live on both plans today. Plus: a new qs replay command in the CLI, and the Streams 2.0 changelog entry.

**Opener:** none. No schedule or format change this issue.

### Shipped

**[Streams 2.0 is generally available](CHANGELOG_URL)**
Streams 2.0 is generally available on the Team and Enterprise plans. **[FIRST STEP: the setting, flag or command a reader uses to move a stream to 2.0.]**

**[`qs replay` in the CLI](CLI_CHANGELOG_URL)**
The CLI has a new command, `qs replay`. **[ONE CLAUSE ON WHAT IT DOES, plus the CLI version it ships in.]**

There are no breaking changes, removals or security fixes in what you sent me. If any exist, they go above both items.

## Plain-text part

```
SHIPPED

Streams 2.0 is generally available
CHANGELOG_URL
Streams 2.0 is generally available on the Team and Enterprise plans.
[FIRST STEP]

qs replay in the CLI
CLI_CHANGELOG_URL
The CLI has a new command, qs replay. [WHAT IT DOES + CLI VERSION]
```

## What I cut from the PM's note, and why

- **"Total game-changer", "customers love it":** hype and an unprovable claim. Both are on the skill's cut lists.
- **"3x faster ingestion":** this is your biggest claim, and it is cut. The note is internal, and no post or changelog states it, so there is nothing to link or attribute it to. If the blog post or a changelog line with the benchmark goes live before Thursday, send me the link. I'll add it as "the post reports up to 3x faster ingestion", linked.
- **"Free tier gets it in Q1":** cut. A future plan or date goes in only if it is already announced publicly. Tell me it is, and I'll add one line.
- **"Make it exciting":** I did not do this. Developer readers punish release copy that reads as an ad, and the skill's rule is capability, availability, first step. The biggest release of the year earns the lead position, not louder adjectives.

## Pre-send report

| Check | Status |
|---|---|
| Subject ≤ ~45 chars, names the lead | ✅ pass (41) |
| Preview complements the subject and reaches 90 chars | ✅ pass (104) |
| No tone-pass cut words in the prose | ✅ pass |
| No number, date or version beyond your note | ✅ pass |
| Streams 2.0 first step | ⚠️ **blocked**: your PM's note names none, and I won't invent a flag |
| `qs replay` capability and CLI version | ⚠️ **blocked**: the note only says it exists |
| Links | ⚠️ **blocked**: I have no URLs. The changelog is a bare version bump, so the headline link is thin until the post exists |
| "GA today" | ⚠️ **blocked**: confirm GA is live on the plans by Thursday's send. The copy says "is generally available", which is true only if so |
| Test send in Gmail, Apple Mail and classic Outlook, light and dark | ⚠️ **blocked**: needs your send |

**Open questions for you or your PM:**
1. What is the first step to try Streams 2.0?
2. What does `qs replay` do, and in which CLI version?
3. Is there a post coming before Thursday, and does it state the 3x figure?
4. Is the Free-plan Q1 date already public?

**Correction owed:** none yet. Note for the next issue: if the blog post lands after Thursday, add it there as a one-line follow-up.