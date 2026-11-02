# Before closing the LoopState Conf accessibility ticket

**Recommendation: don't close it, and don't publish "fully accessible".** A 100/100 scanner score means the automated checks passed. Those checks catch roughly 30–40% of WCAG issues. I haven't opened the site, so what follows is a list of what to verify, not findings.

## 1. Fix the claim wording

- "Fully accessible" is an absolute claim. In the EU (European Accessibility Act, in force since June 2025) and in the US (ADA), an absolute claim that turns out to be false is a legal and reputational risk.
- Safer hero copy: "We're committed to an accessible conference. Report a barrier: accessibility@…" Link it to an accessibility statement.
- The statement should name the standard (WCAG 2.2 AA), the date of the last audit, known gaps, and a contact route.
- The claim also has to cover the venue, sessions, and live captioning. Right now the scope is only the website.

## 2. Schedule grid (color-coded by track)

Automated scanners only check a limited set of contrast pairs. They don't check whether meaning depends on color alone.

1. **Color as the only signal (WCAG 1.4.1).** Check whether the track is also shown as text, an icon, or a pattern. A color-blind attendee can't tell tracks apart if it isn't. Simulate protanopia/deuteranopia in browser DevTools.
2. **Contrast of track colors (1.4.3, 1.4.11).**
   - Text on each track color needs 4.5:1.
   - Borders, badges, and chips need 3:1 against their background.
   - Check each track color, plus hover, focus, and selected states.
3. **Table semantics (1.3.1).**
   - A real `<table>` needs `<th scope>` for the time and room headers, and spanning sessions need correct `rowspan`/`colspan` headers.
   - If it's CSS grid built from `<div>`s, a screen reader may read it as an undifferentiated list. Test it.
4. **Keyboard and screen reader.**
   - Tab through the grid. Is the order logical (by time, then room)?
   - Can you open session details without a mouse?
   - Do filters and track toggles announce their state (`aria-pressed`, a live region for result counts)?
   - Does a session card announce title, time, room, and track?
5. **Reflow and zoom (1.4.10, 1.4.4).** At 400% zoom (320px wide), a wide grid often forces two-axis scrolling. Check that there is an alternative list or agenda view.
6. **Mobile and touch.** Check target sizes of at least 24×24 px (2.5.8). Check for hover-only details.
7. **Sticky header overlap (2.4.11).** Make sure focused cells aren't hidden under a sticky time or track header.
8. **Calendar export and "add to my schedule".** Check that these controls are labelled and keyboard operable.

## 3. Speaker slides as PDFs

The site scan won't open PDFs. This is the biggest gap, and it will keep growing after the conference as slides are posted.

1. **Tagged PDF.** Each PDF needs a tag structure, which exports from PowerPoint or Keynote often lose. Check with Acrobat's accessibility checker or PAC (the free PDF Accessibility Checker).
2. **Reading order and headings.** Check that the tags read in the order of the slides and that slide titles are headings.
3. **Alt text** on images, diagrams, and charts. Mark decorative ones as artifacts.
4. **Text, not images.** Slides exported as page screenshots have no readable text, so a screen reader reads nothing.
5. **Document language and title** are set in the PDF properties. Set the display title to the talk name, not "Slide1.pdf".
6. **Contrast, fonts, and code screenshots.** Code shown as an image needs a text equivalent.
7. **Links and embedded video.** Links need descriptive text. Embedded video needs captions.
8. **Process.** Decide who is responsible. Options:
   - Give speakers an accessible-slides checklist before the event.
   - Require an accessible source file.
   - Have someone remediate each PDF before it is posted.
   - Offer a "request an accessible version" contact for anything not yet remediated.
   - Publish an accessible HTML or text version alongside each PDF.

   If you can't guarantee remediation, say so in the accessibility statement. Do not claim "fully accessible".

## 4. Other things the scanner doesn't cover

- **Manual keyboard pass of the whole site.** Check for focus visibility, traps, a skip link, and logical order.
- **Screen reader pass.** Run VoiceOver (macOS and iOS) and NVDA on the key flows: homepage, schedule, speaker pages, and registration or ticketing.
- **Registration and checkout.** This is usually a third-party embed (Eventbrite, Tito, etc.) that is outside the agency's scan.
  - Check form labels, error messages, and whether the flow is operable with the keyboard.
  - Check CAPTCHAs and accessible authentication (3.3.8).
  - Check whether access needs (dietary, mobility, captioning) can be entered, and whether the form collects them at all.
- **Media.** Check captions on promo videos, transcripts for audio, and no autoplay.
- **Embeds and widgets.** Check maps, chat, cookie banners, and the video player. A cookie banner often traps focus.
- **Cognitive and content checks.** Link text such as "read more", plain language, heading hierarchy, and page titles.
- **Motion.** Check carousels and animations against `prefers-reduced-motion`, and that anything moving can be paused.
- **Dynamic states.** Scanners often test only the default page state. Check open menus, modals, filtered schedule views, error states, and logged-in pages.
- **Coverage of the scan itself.** Confirm which pages and templates were scanned (all of them, or a sample?), and whether staging and production match.
- **Which scanner and which version.** A Lighthouse score is a subset of axe-core rules. Re-run axe-core and WAVE, and compare.

## 5. Close or keep the ticket?

Suggested wording for the ticket: "Automated scan passed (100/100). Manual audit pending."

Closing checklist:

- [ ] Manual keyboard and screen-reader pass of the key flows, with notes.
- [ ] Schedule grid verified (color independence, contrast, semantics, 400% zoom).
- [ ] Registration flow tested, including the third-party embed.
- [ ] PDF slide process defined, with an owner and a checklist for speakers.
- [ ] Accessibility statement published with a contact route.
- [ ] Hero copy changed to a commitment, not "fully accessible".
- [ ] Decision on in-person scope: venue, captioning, and a quiet room, to be stated separately from the website.
- [ ] Ticket left open, or a follow-up created, for post-event slide remediation.

If you can only do three things this week, do these: a keyboard and screen-reader pass of the schedule and registration, a color-blind simulation of the grid, and a written PDF process. Those cover the specific risks you mentioned.