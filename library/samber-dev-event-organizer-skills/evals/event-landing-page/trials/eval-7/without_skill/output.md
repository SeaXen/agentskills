**Launch verdict: no-go tonight on the registration path as it stands.** The marketing pages can ship if the contrast fix goes in first. Registration needs a keyboard-accessible path, or a documented fallback, before it goes live.

**Next action:** tell the contractor tonight's ship is blocked on three items (below). Ask the ticketing vendor for a conformance report today.

## 1. The 96/100 score proves little

- Automated checkers catch roughly 30–40% of WCAG issues. A tester found a keyboard failure the checker missed.
- A score is not a conformance claim. The score is a weighted average of passing checks, and one blocker can sit under a 96.
- Many checkers only scan the pages they are pointed at. Check whether it crawled the checkout and registration steps at all.
- Cite the score as "no automated errors found". Don't cite it as "compliant".

## 2. Keyboard failure on seat selection and discount code: a blocker

- **Violates:** 2.1.1 Keyboard, Level A. It would fail even the 2.1 A target the contractor wants.
- **Not just the vendor's problem:**
  - WCAG conformance is judged per page, in the context of a complete process. 5.2.1 and 5.2.2 both address whole-process conformance.
  - The working group's target covers "the site and the registration path". The path your attendees use is the target.
  - An embedded third-party widget counts. You chose it, and you ship it to attendees.
- **Legal exposure (Toronto, Ontario):**
  - AODA requires public websites to meet WCAG 2.0 AA, which applies to larger organizations.
  - The Ontario Human Rights Code's duty to accommodate applies regardless of the vendor.
  - Check your obligations with counsel. I am not giving legal advice.
- **Practical impact:** a keyboard or screen-reader user cannot pick a seat or apply a discount. They cannot buy a ticket independently.

**Options, fastest first:**
1. **Vendor fix.** Send the tester's reproduction steps to the vendor today. Ask for a fix date in writing and a current VPAT or ACR.
2. **Vendor setting.** Check for a simpler checkout mode, such as general admission with no seat map, or an accessible-mode toggle.
3. **Accessible fallback.** Offer a documented alternative path with a staffed phone line or email that completes registration within about one business day. Link it from the registration page before the widget. Name a contact who responds.
4. **Delay or switch.** If the vendor can't commit and no fallback works, delay opening registration.

A fallback is mitigation. Under WCAG it does not make the widget conformant, so record it as a known exception with an owner and a date.

## 3. Do not quietly re-scope to WCAG 2.1 A

- The working group set the target. The contractor can't change it, and a silent change would hide it from them.
- Level A is a floor. It drops contrast, focus visibility, reflow, target size, and status messages, which are the things most event sites fail.
- 2.2 AA adds only a few criteria beyond 2.1 AA. Of those, 2.4.11 Focus Not Obscured, 2.5.8 Target Size and 3.3.8 Accessible Authentication matter for registration. It is not overkill.
- Any re-scope is a decision for the working group, made openly and in writing.
- A silent downgrade creates a worse record than an honest "not yet conformant".

## 4. Body text at 3.9:1 fails

- **Violates:** 1.4.3 Contrast (Minimum), Level AA. Normal text needs 4.5:1, so 3.9:1 fails.
- "Close enough" is not a pass. The threshold is binary.
- **Fix:** darken the text colour. This is a CSS change that takes minutes.
  - Light grey on white at 3.9:1 usually fixes with a small shift, such as `#767676` or darker on white.
  - Check the exact pairs with a contrast tool.
- **Also check:** placeholder text, link colour, button text, focus rings, and form borders. UI components need 3:1 under 1.4.11.
- The checker should have flagged this one. Ask why it didn't, which points back to what it scanned.

## 5. Before any sign-off

Have someone do these manual checks on the whole registration path:
1. Tab through every step with no mouse. Check the order, visible focus, no traps, and that nothing is hidden behind sticky bars.
2. Run a screen reader through it: VoiceOver on Mac, or NVDA on Windows.
3. Zoom to 200%, and test at 320px width for reflow.
4. Check form labels, error messages, and the confirmation screen.
5. Check payment and login steps against 3.3.8. Paste into fields must work.
6. Check captions on any video. Add a transcript for audio.

## 6. Plan

| Item | Owner | When |
|---|---|---|
| Fix body-text contrast, rerun checker | Contractor | Tonight |
| Send tester's repro to vendor, request VPAT and fix date | You | Today |
| Set up the accessible fallback with a named contact | You | Before registration opens |
| Manual keyboard and screen-reader pass | Tester | Before launch |
| Publish an accessibility statement listing known gaps, the fallback, and a contact | You | At launch |
| Working group decides on any scope change | Working group | Written, not quiet |

## 7. What you can say

- **To the contractor:** "Not compliant until the keyboard blocker and contrast are fixed. The scope stays WCAG 2.2 AA. Raise any change with the working group."
- **To the working group:** "Marketing pages ready after the contrast fix. Registration is blocked on a vendor keyboard defect. We have asked the vendor for a fix date and are setting up a fallback."

**Launch condition:** contrast fixed, and a keyboard-accessible registration path (vendor fix or documented fallback) in place and tested. If both are met, launch with a published accessibility statement. If not, hold registration.