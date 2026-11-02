**Verdict: not enough.** The plan lists real techniques, but none of them would have caught last year's failure. A recorder stopped and nobody noticed, and nothing in this plan changes that. This is for two rooms and 22 sessions over two days, recorded and not streamed.

## Why it falls short

| Plan item | Problem |
|---|---|
| Spare mic and camera in the cupboard at the back | They sit far from the lectern, so a dead mic means a walk and a swap while the talk runs. The spare camera also covers the layer least likely to fail silently. Nothing here would have caught the stopped recorder. |
| Copy SD cards to the NAS at day end | This is verification after the fact. If a recorder stopped at 10:40, you find out at 18:00 or later, and the session is gone. During the day each talk exists as one copy on one card. |
| Same copy, bulk and in the evening | One big copy over the office network is a single manual step. It has no named owner and no check that the files play. |
| No labels, clocks or test playback | A second copy nobody has opened is not a backup. |

## Revised plan

**Capture posture:** recorded, not streamed. That forgives short failures, but not one that nobody notices.

**1. Catch silent failure.** This is the fix for last year.
- Split the signal to a monitor at a production desk in each room. The monitor shows the recorder's actual output, not the camera's live view.
- The room's production owner checks it at the start of every session and again about 5 minutes in.
- Write down the check as a card for the owner: "Recording indicator on, time elapsed rising, audio meter moving."
- Check each camera's record limits (file size, continuous recording time, card capacity) against your longest session. A camera can stop on its own limit. I can't tell from here whether that is what happened last year.

**2. Keep the live session running.**
- Put a second mic live at the lectern, on its own channel.
- Keep spare batteries with the room lead.
- Tape down a labelled spare cable for every run.
- Carry a spare adapter for every connector your speakers asked for.
- Keep the spare camera in the cupboard as a last resort. Don't count it as redundancy.

**3. Make the audio archive independent.**
- Add a standalone audio recorder per room, fed from the mixing board but outside the live mix. Audio is what makes a recording usable.
- Name files `roomA-YYYYMMDD-HHMM`.
- Set every device's clock against one shared time source each morning.
- Recording audio from the camera's own mic is not an acceptable chain. Take audio off the board.

**4. Copy between sessions, not at 18:00.**
- Offload and verify cards at changeovers, or whenever the network is otherwise idle.
- Open each offloaded file and play a few seconds, not just a file-size check.
- Keep the card unformatted until the NAS copy plays.
- If the venue network is shared, don't bulk-copy over it during sessions.

**5. Test before the doors open.**
- Walk each room's signal path end to end.
- Record 60 seconds and play it back in full. A moving level meter proves nothing.
- Unplug the primary mic and time the swap with the person who will actually do it.

**6. Name owners.** Each room needs one production owner, and that person is not also MCing, speaking or running registration. If the venue has a house technician, keep them, but they run the house system, not your recording. Also name who owns the post-event pipeline, and the date by which every file has been verified.

## Targets to track

I'm setting these myself, not citing benchmarks:
- **Capture completeness:** sessions with a usable recording over 22. Count "recorded but unusable" as a failure.
- **Failures caught by redundancy** versus failures that reached the audience.

## Questions I need answered

1. Where does recording audio come from today: the mixing board or the camera's own mic?
2. What is the grid? I need the shortest changeover, which sessions can't be repeated (keynotes), and how many people can be on production only.
3. Do speakers have live demos, audio playback or non-standard connectors?
4. Is there a consent record covering recording and publication per session? Nothing publishes outside it.
5. Does the venue have a house technician and installed AV?
6. What is the last date you can still add equipment?
7. Is this recurring? If so, a trained crew and a written checklist pay off in later editions.

Answers to 1 and 2 would change the ranking most. If audio comes off the camera mic, fix that before anything else.