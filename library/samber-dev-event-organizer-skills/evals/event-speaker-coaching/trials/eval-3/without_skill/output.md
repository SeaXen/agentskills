**Subject: Coppervale Frontend Days: slide review 1 of 2 for your talk**

Hi Tomas,

Thanks for sending the deck. Here is review 1 of 2. The final slides are due **2 March**. I've put the changes that matter most first.

**Must fix**

1. **Body text colour (all slides).** #777777 on white has a contrast ratio of about 4.5:1, which is borderline and fails WCAG AA for body-size text. A projector in a lit room will wash it out further.
   - Change body text to #333333 or darker (#595959 is the lightest I'd accept).
   - Make the headings the same darker colour. At 28pt they pass the large-text threshold, but they should match.

2. **Code on slides 11 to 13.** At 11pt, showing whole files, nobody past the front row can read it.
   - Cut each slide to the 6 to 10 lines that carry the point.
   - Set the code at 24pt or larger.
   - Highlight the line that matters.
   - Put the full files in a repo or gist and link it from the last slide.
   - Check that these three slides are your three traps. If they are, give each one a title that names the trap.

3. **Slide 6 diff.** Red and green are the only markers, so anyone with red-green colour blindness, or anyone on a washed-out projector, can't tell added lines from removed ones.
   - Add a `+` or `-` at the start of each line.
   - Keep the colours as a second signal. A subtle background tint helps as well.
   - Use the same size rule as the code slides.

4. **No closing summary.** Add a final slide that recaps the migration path and names the three traps in one line each.
   - That is what your abstract promised, so the last slide should show it was delivered.
   - Leave this slide up during the 5-minute Q&A.
   - Put the URL from point 6 on it.

**Should fix**

5. **Slide 9 GIF.** A cursor flashing five or six times a second is distracting on a big screen. It is also above the 3-flashes-per-second limit that accessibility guidelines use for flashing content. A small area like a cursor is unlikely to be a seizure risk, but it is still worth removing.
   - Replace it with a static screenshot, or re-record it with the cursor solid or blinking at 1Hz or slower.
   - If it must stay animated, make it play once and not loop.

6. **Slide 17 QR code.** Add the short URL as large text next to the code. Some people can't scan from their seat, and slides shared afterwards or watched remotely need a typed address. Say in a few words what the link gives people.

7. **Slides 3, 8 and 15 have no title.** Untitled slides are skipped or unlabelled by screen readers and by slide navigation, and they leave the audience without a signpost.
   - Give each one a real title in the slide's title field, not a text box.
   - Where you can, state the point of the slide as the title.

**Timing**

I haven't seen your slide count beyond slide 17. At 20 minutes, three dense code slides plus a diff and a demo GIF will run long. Rehearse once with a timer and cut a slide if you pass 18 minutes. That leaves room for the summary slide and a clean handover to Q&A.

**Abstract check**

The abstract promises "a migration path off a legacy Redux store, with the three traps we hit". Make sure the deck shows the path as a sequence of steps, not only the traps. Name the three traps explicitly, so the audience can count them.

Please send the revised deck for review 2 once these are done. If any of these changes is a problem, tell me and we'll find another fix.

Thanks,
[Your name]
Slide volunteer, Coppervale Frontend Days

**Notes for you before sending**
- I computed #777777 on white at about 4.48:1 myself. It fails AA only for text below the large-text size, so check Tomas's body size. If it's 24pt or larger, the contrast passes but I'd still darken it.
- I haven't seen the deck, so the slide 9 and code-size points rest on your description.
- Add the review 2 date if you have one.