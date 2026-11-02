**No, a "click yes to keep receiving" email is not the right fix.** Stop sending the newsletter to the 1,400 first, and treat re-permission as a separate step that only applies if you can show they opted in. I'm not a lawyer, so have your DPO or counsel confirm the points below.

## Why the re-permission email fails

1. **It is itself a marketing email to people who never opted in.** In Germany (UWG §7, plus the ePrivacy rules), an email asking for consent can count as unsolicited advertising when the recipient never agreed to be emailed. The B2B exception many countries have doesn't exist there. You'd be repeating the violation to try to fix it.
2. **It can't fix past sends.** The newsletters since May are already out. The email only affects future sends.
3. **Silence is not consent.** Anyone who doesn't click has to come off the list. Your manager's plan only works if you remove every non-clicker.
4. **A badge scan is usually not a newsletter opt-in.** Consent has to be specific, informed, and a clear opt-in action. A scan typically covers "the exhibitor may follow up about this conversation", at most. The "existing customer" exception needs a prior sale and an opt-out offered at collection, and a booth visit rarely meets that.

## Do now (about 2 hours)

1. **Pause newsletter sends to the 1,400.** Move them to a suppression segment. Don't delete yet, because you need the records to show what happened.
2. **Pull the evidence.** Find the exact text the scanner app showed and what the booth signage said. Check the conference organizer's attendee terms and any sales notes on who asked for the newsletter. Per Art. 7(1) GDPR, you have to prove consent, not assume it.
3. **Split the 1,400 into three groups:**
   - **Documented newsletter opt-in** (rare): keep them, and confirm with a double opt-in.
   - **Real sales conversation, no newsletter consent:** sales may do one-to-one follow-up tied to that conversation. This is a sales decision, not a list decision.
   - **Scan only, no conversation:** suppress and remove them from the newsletter.
4. **Check the privacy notice duty.** If the data came through the organizer or a scanner vendor, people had to be told how you use it (Art. 13/14 GDPR). Confirm that happened.
5. **Tell your legal contact about the May to October sends.** Exposure in Germany is mostly a cease-and-desist from a recipient or a complaint to a data protection authority. A fine is less likely. Legal should know before it arrives.

## Check that the damage is really these 1,400

Compare unsubscribes and complaints by cohort. A rough check on your numbers:

- The original list is about 4,200 people at 0.2%, which gives about 8 unsubscribes per send.
- 0.7% of 5,600 is about 39 unsubscribes per send.
- That leaves about 31 from the scan cohort, or **roughly 2.2% per send**, about 10x your baseline.

If the cohort split confirms that, the cause is clear. If it doesn't, look at content fit and send frequency instead.

## Protect the other 4,200 subscribers

Complaints hurt every send. Gmail and Yahoo bulk-sender rules want spam complaints under 0.1% and treat 0.3% as the danger line.

- Check **Google Postmaster Tools**, bounce rates, and any spam-trap hits.
- Look at engagement per cohort. The scan cohort is probably dragging down your inbox placement.
- Check whether sales also emails the same people from a different system. Complaints may come from both.

## Fix the process

- **Audit every other import** (past events, webinar lists, any bought or partner list) for the same problem.
- Store a source, timestamp, and consent text on every subscriber record.
- **At the next event:** use a separate, unticked newsletter checkbox on the scan form, or a QR code to a signup page. Use double opt-in for EU signups. Then badge scans become permission-based leads.

## If legal allows one confirmation email

Only send it to the "documented opt-in" group. Make it a plain double opt-in link, say where you got their details, and don't send a reminder. Expect a low response rate. Treat that as an accurate count of who actually wants the newsletter. The other 1,400 or so were never going to read it.

## Next step

Find the badge scanner's consent text and the booth signage (about 10 minutes), then send it to me. I can tell you which of the three groups the 1,400 fall into and draft the note for your manager.