# Weekly Terraform drift stream: what to buy and what to run

## Recommendation

Spend about $300–450 now. Start with what the CEO already owns, and upgrade only after 4 episodes.

Twitch viewers for a Terraform-drift show will be few at first, often 5–30. ThePrimeagen's audience comes from his personality and reactions, not from the topic. So plan for a small, high-signal audience, and plan to turn each episode into clips and a YouTube VOD. The VODs and clips will reach more people than the live stream does.

## 1. What to buy

| Item | Buy | Approx. cost | Notes |
|---|---|---|---|
| Microphone | USB dynamic mic, e.g. Samson Q2U or Audio-Technica AT2020USB-X (a Shure MV7+ is the upgrade) | $70–150 | Audio matters more than video. Dynamic mics reject keyboard and room noise. |
| Headphones | Closed-back wired | $50–100 | Prevents echo and feedback from the mic. |
| Camera | Use a recent iPhone or mirrorless camera if one exists. Otherwise a 1080p webcam (Logitech Brio or Razer Kiyo class). | $0–150 | Skip a DSLR or capture-card setup. |
| Key light | One LED panel with a softbox | $50–130 | Fixes most of the look problem for the money. |
| Network | Wired ethernet, at least 10 Mbps upload | $0–20 | Never stream over Wi-Fi. |
| Software | OBS Studio (free) | $0 | Add a free multistream tool for YouTube later. |
| Overlays | Free OBS or Canva templates: a clean camera frame, a lower-third with name and show title, and a "Starting soon" scene | $0 | Skip paid packs and Stream Deck. Add polish after the format works. |

Lean total is about $300. A comfortable setup is about $450.

Also check:
- **Second monitor:** he needs one for chat and OBS while the first shows the terminal.
- **Dark theme, large font:** set terminal and editor to 18–20 pt. Unreadable code is the most common mistake in coding streams.
- **Moderation:** turn on Twitch AutoMod and add 1–2 teammates as mods. That costs minutes per week, not hours.

## 2. What the show should be

**Working title:** *Drift Friday* (or *Break My Terraform*)

**Premise:** the CEO live-debugs real infrastructure drift with chat. It is entertaining because things break, and it demonstrates the product without pitching it.

### Two-hour run of show

| Time | Segment | What happens |
|---|---|---|
| 0:00–0:10 | Intro and news | Terraform/OpenTofu releases, outage post-mortems, any drift horror story from chat. |
| 0:10–0:50 | **Roast the repo** | A viewer submits a public Terraform repo, or sanitized snippets. He reads it live and points out where drift will happen: console edits, unmanaged resources, `ignore_changes` abuse. |
| 0:50–0:55 | Break | |
| 0:55–1:35 | **Cause the drift, then catch it** | In a demo cloud account, chat votes on a click-ops change. He runs the CLI and shows how the drift is detected and explained. He fixes it two ways, by reconciling the code or by reverting the resource. |
| 1:35–1:55 | **Guest or Q&A** | A 20-minute guest (SRE, platform engineer, OpenTofu or Terragrunt maintainer) or open questions. Guests don't need a team member's time. |
| 1:55–2:00 | Outro | Next week's challenge, one clear call to action. |

The call to action should be low-friction, such as "try the CLI on your own repo." Keep sales pitches off the stream.

### Why this format
- **Segments** keep the 2 hours from feeling empty and make it easy to cut clips.
- **Viewer submissions** supply content, so the CEO doesn't need much prep.
- **Breaking things on purpose** is entertaining and demonstrates the product honestly.
- **Guests** share the load and bring their own audiences.

## 3. Risks to settle before episode 1

- **Secrets leaking on stream.** This is the biggest risk for an infrastructure tool.
  - Use a dedicated demo cloud account with no production access.
  - Use throwaway credentials.
  - Never show state files, `.env` files, or account IDs from real accounts.
  - Run a 30-second stream delay.
  - Do one private test run first.
- **Viewer-submitted repos.** Public repos only. Don't run `terraform apply` against anything a viewer sends.
- **Single point of failure.** The show depends entirely on the CEO. If he skips two weeks, the show is dead. Agree a cadence he can sustain, and a rule for missed weeks.
- **The real time cost.** The CEO's time is roughly 2 hours live, 1 hour of prep, and 1 hour of clipping and posting, about 4 hours a week. At a 6-person company that is a real cost. Ask whether 90 minutes, or 2 hours every other week, would still meet the goal. I'd keep the 2-hour weekly format only if he truly wants it.
- **Twitch fit.** The audience for infrastructure content is stronger on YouTube. Stream to Twitch and YouTube together, and push clips to X and LinkedIn.

## 4. How to know it's working

Run it for **8 episodes**, then decide with these checks:

- **Average live viewers.** Don't judge on peak. Expect single digits to low tens at first.
- **Chat participation.** Count chatters and repo submissions per episode.
- **Clip and VOD views.**
- **Concrete outcomes.** CLI installs or signups with a "stream" tag in the link, and any conversations a viewer starts.

If after 8 episodes there are no outcomes, stop, or switch to a monthly show. Settle that kill rule with the CEO before episode 1.

## 5. Next steps

1. Decide the cadence and kill rule with the CEO (20 min).
2. Buy the mic, headphones and light (about $200–300). Test the existing camera first.
3. Set up OBS with three scenes: starting soon, main, and guest.
4. Create the demo cloud account and the secrets checklist.
5. Do a private dry run, then a public episode 1 with a friendly guest.