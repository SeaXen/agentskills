# Verdict: don't resend the whole issue. Send a short correction email.

**Why not a full resend**
- It lands in 9,400 inboxes as a duplicate. Some people will unsubscribe, and many will assume it's the same issue and ignore it.
- The security fix gets buried. Anyone who ran `pip install kestrel-cli==3.1.0` needs to see the fix in the first two lines, and a full resend puts it below an apology and a newsletter's worth of content.
- A full resend also re-sends the pinned bad command. If any copy of the old tip survives, you've doubled the exposure.

**What to do instead, in this order**
1. **Today:** send the correction below to the full list, not just openers. The security issue affects people who never opened the email but may still follow the tip through a forward or the archive.
2. **Now:** fix the web archive copy. Change the tip to `>=3.1.2` and add a "Corrected on 2026-10-30" note at the top. Don't silently edit it.
3. **Check with your maintainers:** should 3.1.0 be yanked on PyPI? A yank still allows exact pins (`==3.1.0`) but stops resolvers from choosing it, which would cover the people who already ran the bad command.
4. **Message Ines and Tomasz directly,** before or at the same time as the send. Ines was credited for work she didn't do, and Tomasz was left out of credit he earned.

## The email

**Subject:** Correction: upgrade to kestrel-cli 3.1.2, not 3.1.0

**Body:**

> Hi,
>
> Yesterday's issue had two errors. The first one matters for your security.
>
> **1. Please don't install kestrel-cli 3.1.0.**
> Our "upgrade now" tip told you to run `pip install kestrel-cli==3.1.0`. That version has a path traversal vulnerability ([CVE-XXXX-XXXXX]), fixed in 3.1.2.
>
> If you ran that command, upgrade now:
>
> ```
> pip install --upgrade "kestrel-cli>=3.1.2"
> ```
>
> If you pinned `kestrel-cli==3.1.0` in a requirements file, lockfile, or CI config, change the pin to 3.1.2 or later. You can check your version with `kestrel --version`. Details on the issue: [link to advisory].
>
> **2. The caching deep-dive was written by Tomasz Vey, not Ines Okonjo.**
> We credited the wrong person. Tomasz wrote it, and you can read it here: [link]. Sorry, Tomasz, and sorry, Ines, for putting your name on work you didn't do.
>
> I'm sorry for both mistakes, and especially for the bad install command. The archived version of the issue now carries the corrected command and a correction note. [Add one line on what changes in your review process, only if it's true, e.g. "Every version number in the newsletter is now checked against the release notes before sending."]
>
> [Name]
> Kestrel CLI newsletter

## Notes on the draft
- **Fill the placeholders** from the advisory: the CVE ID, the advisory link, and the article link. I don't have them.
- **Confirm 3.1.2 is the right floor.** If 3.1.1 also has the bug, say so. If 3.1.2 is no longer the latest, say "3.1.2 or later".
- **Keep exploit details out.** The draft names the bug class, as the CVE does, and nothing more.
- **Keep the apology short.** One sentence plus a real fix reads better than a long apology, and it keeps the subject line and first paragraph on what readers need to do.
- **Tell your manager** that a short correction gets the right action from more people than a full resend, and it avoids unsubscribes and spam complaints. If they still want the full issue re-sent, offer to put it in next week's issue, with the corrected credit and a one-line "last week's fix" note.