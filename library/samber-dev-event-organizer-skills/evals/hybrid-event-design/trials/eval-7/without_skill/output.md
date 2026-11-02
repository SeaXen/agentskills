# Harborlight remote-side figures for the sponsor deck

None of these come from Harborlight data. I had no prior-year registrations or stream logs, so they are planning commitments built on common industry rules of thumb. Label them "targets" in the deck, not "expected results". If you have last year's remote numbers, swap them in and rerun the arithmetic below.

## Deck table

| Question | Figure to publish |
|---|---|
| Remote share of Q&A time | **40% guaranteed floor**, with remote and in-person questions interleaved 1:1 |
| Moderators | **1 per 100 peak concurrent remote viewers**, minimum 2 per track |
| Stream latency | **≤ 5 s glass-to-glass at p95** (target 3 s), using low-latency HLS or WebRTC |
| Remote attendance vs 500 in-person | **Base 500 unique live viewers** (range 250–900), peak concurrent about 300 |

## How each figure was derived

**Attendance forecast**
- Free or low-cost remote registration usually runs 2–3× in-person, so plan for 1,000–1,500 registrations.
- Live show-up for virtual events is typically 35–45% of registrants.
- That gives a base of about 500 unique live viewers, a low case of 250 and a high case of 900.
- Peak concurrent viewers are roughly 55–60% of uniques, so the base peak is about 300.

| Case | Unique live viewers | Peak concurrent | Moderators at 1:100 |
|---|---|---|---|
| Low | 250 | ~150 | 2 (the per-track minimum) |
| Base | 500 | ~300 | 3 |
| High | 900 | ~540 | 6 |

**Q&A share**
- Base peak concurrent remote of 300 against 500 in-room is about 38% of the live audience.
- Rounding up to a 40% floor means remote is never underserved relative to its size.
- Interleaving 1:1 stops the room from absorbing the whole Q&A before remote questions are heard.
- State it as a floor. Do not promise proportional share, because the share would shrink if remote underperforms.

**Moderators**
- Size to peak concurrent, not registrations.
- Each moderator is either a chat moderator or a question curator. Never combine the roles on one person during Q&A.
- Add one spare per event day.

**Latency**
- Standard HLS runs 15–30 s behind live, which makes remote questions arrive after the speaker has moved on.
- Low-latency HLS holds 2–5 s. WebRTC holds under 1 s but costs more at scale.
- Promise 5 s at p95 rather than an average. The sponsor can test it, and averages hide the spikes.
- Remote askers who go live on audio should use a WebRTC path under 500 ms.

## Caveats to settle before sending

- **Don't publish the 40% as a result.** It's a commitment you have to staff. Confirm the host and room-mic workflow can enforce it.
- **The attendance range is wide on purpose.** If the sponsor asks for one number, give 500 and show the low and high cases next to it.
- **The show-up rate depends on pricing.** Paid remote tickets show up at 60–70%, but you'd sell fewer. Tell me the pricing and I'll recompute.

Do you have last year's remote registrations or concurrent peak? Those would replace the show-up and ratio assumptions and make the base case defensible.