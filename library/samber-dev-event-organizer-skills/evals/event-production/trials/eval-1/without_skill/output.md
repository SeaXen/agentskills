**Next action:** email the venue the questions in section 7 (10 min). Everything else depends on the answers.

## 1. Core plan

- Audio quality decides whether talks are watchable. Spend there first.
- Do not film the projector or TV screen. Capture the slides straight from the laptop's HDMI output.
- Use one video mixer per room. Record the finished picture directly, so there is almost no editing. The mixer I suggest is the Blackmagic **ATEM Mini Pro**.
- Use the same kit in both rooms, so volunteers learn it once.
- Run a single 1080p25 setting everywhere (UK frame rate).

## 2. Per-room signal chain

1. A house laptop outputs slides over HDMI to an HDMI splitter.
2. One splitter output goes to the projector or TV. The other goes to the ATEM.
3. The camcorder's HDMI output goes to a second ATEM input. Its tripod sits at the back, locked off, framing the speaker wide.
4. Audio goes into the ATEM mic input:
   - **Room B:** a wireless lapel mic on the speaker.
   - **Room A:** a feed from the mixing desk. Use a spare aux send, set pre-fader, so nobody changing the PA volume changes the recording. Ask for a spare output on the desk, then buy the matching cable.
5. The ATEM records to a USB-C SSD. Start and stop recording for each talk, so you get one file per talk.
6. Put a separate audio recorder (Zoom H1essential or similar) on the same audio source as insurance. Audio is the one thing you can't fix afterwards.
7. Use closed-back headphones on the ATEM so the operator can hear what is recorded.

**Camcorder check (this week):** confirm each one has a clean HDMI output with no on-screen display, a working battery plus mains adapter, and auto power-off disabled. If one has no clean HDMI, the fallback is to record it internally to SD and sync it to the audio in editing with a clap. That costs about 20 extra editing minutes per talk.

## 3. Shopping list (UK prices are my estimates, so verify before buying)

| Item | Qty | Approx. total |
|---|---|---|
| ATEM Mini Pro | 2 | £700 |
| Wireless lapel mic kit (Rode Wireless GO II, DJI Mic 2 or similar) | 2 | £400–500 |
| Cheap wired lapel mic with a long cable (backup) | 2 | £30 |
| Zoom H1essential or similar | 2 | £200 |
| HDMI splitter that handles EDID, plus 2 spare | 2+2 | £80 |
| Long HDMI cables (10 m), short HDMI cables, mini-HDMI adapters | ~8 | £100 |
| USB-C SSD 500 GB, plus SD cards | 2 + 4 | £140 |
| Closed-back headphones | 2 | £40 |
| Audio adapters for the desk feed (XLR/jack to 3.5 mm) | 2 | £30 |
| Extension leads, gaffer tape, cable mats, spare AA batteries | – | £100 |
| Spare camcorder batteries | 2 | £60 |

- **Total:** about £1,900–2,100.
- **Optional:** one LED panel (~£80) for Room A if the stage is dim.
- **Cheaper route (about £900):** replace the ATEMs with a laptop running OBS plus two cheap HDMI capture cards per room. It is fiddlier and crashes more often, which is risky with first-timers.
- **Rent instead:** ATEMs can be rented for about £60 each per weekend. Buy only if you plan a second edition.

## 4. Roles (3 per room, six volunteers)

- **Operator:** runs the ATEM, watches audio levels, starts and stops recording.
- **Camera and mic:** frames the shot once, fits the mic on the speaker, swaps batteries, checks the SD card.
- **Float:** runs the slides laptop and changeovers, keeps time, and in Room A owns the PA desk.

The ATEM operator needs only three buttons:

- Slides with a small speaker picture in the corner is the default.
- Full slide is for code or demos.
- Full camera is for Q&A.

## 5. Room-specific points

**Room A (180 seats, PA):**
- Ask who runs the PA. Do not make the ATEM operator do both jobs.
- Keep the stage lit while the projector is on, or the speaker will be a silhouette.

**Room B (80 seats, TV, no PA):**
- A speaker's voice should carry in an 80-seat room without amplification. Use a lapel mic for the recording only.
- The speaker repeats each audience question before answering, or it won't be on the recording.
- Close the blinds so the speaker isn't backlit.
- On a flat floor, heads will block the camera. Raise the camera on a table or crates, or put it at the centre aisle on the tallest tripod.

**Both rooms:**
- Use a house laptop per room. Speakers send slides a week before the event, and you test them all. Their own laptops are the exception, not the default.
- Mark the audience off camera with signs.
- Play no music, so YouTube won't flag copyright claims.

## 6. Timeline

1. **6 weeks out:** send the venue questions and order the kit.
2. **4 weeks out:** test the camcorders and record a fake talk at home with all six volunteers.
3. **3 weeks out:** collect signed recording consent from every speaker and set the slide deadline.
4. **Day before:** install and test both rooms, with every mic, every cable and a full-length recording played back.
5. **On the day:** each Operator starts recording at the start of the talk and stops after the Q&A. Do not rotate roles mid-day.
6. **After:** offload and back up the files the same night to two places.

## 7. Questions for the venue

1. Can we get in the day before, and for how long?
2. What mics does the Room A PA have? Does the desk have a spare aux send or output?
3. Who operates the PA?
4. What are the Room A projector inputs (HDMI or VGA)? Does the Room B TV take HDMI?
5. Where are the power sockets in each room? Can we tape cables down?
6. Can the Room B blinds be closed?
7. Are there any recording restrictions or insurance requirements?

## 8. Editing the 14 talks

- Budget about 20–30 minutes per talk for trimming, a title card, loudness normalisation and export.
- That totals roughly 6–7 hours. Give it to one volunteer, using DaVinci Resolve (free).
- Upload as private first and let speakers review. Then publish with auto-generated captions, which someone checks quickly. Aim for within 3 weeks of the event.

## 9. Open risks

- **Splitter handshake:** HDMI splitters sometimes fail to negotiate with the projector or TV. Test the exact splitter at the venue, and buy the spares.
- **Mic interference:** with 260 phones in the building, 2.4 GHz wireless mics can drop out. Keep the receiver near the speaker and keep the wired backup ready.
- **Battery and storage:** a failed battery or full card mid-talk loses that talk. Swap them at every break.

Do you know yet whether Room A's PA has wireless mics, or only a handheld on a stand? That decides whether you need the lapel kit in Room A at all.