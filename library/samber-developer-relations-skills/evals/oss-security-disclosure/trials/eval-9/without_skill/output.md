# Decision: do neither

Reply once, politely, with no money and no threats.

## Why not pay $100

- **It doesn't buy silence.** They already hold the "secret". Nothing stops them asking for more, or publishing anyway.
- **It sets a precedent.** You'd be paying on an unverified claim, which invites every spammer with a template.
- **It makes you the odd one out.** You'd pay for silence, not for a fix, and that is the opposite of how bounties work.

## Why not threaten police or the hosting provider

- **It's weak as extortion.** The email is vague and unverified. It could be a clumsy bounty request from someone who skipped your security policy. Treat it as "unproven".
- **It escalates.** A threat gives them a reason to publish, and a public fight about it is worse than a vague blog post.
- **It doesn't help users.** If the bug is real, the fix matters more than the sender's behaviour.
- **It's risky for you.** Threatening a criminal complaint to gain leverage can backfire in some jurisdictions. Ask a lawyer before going down that road. This is not legal advice.

## What the email suggests

- It names no version, no component, no PoC, and says "account takeover". A caching library has no accounts, so this looks like a mass-mailed template.
- Check whether other Maven Central projects got the same text. Search the exact phrase.
- A real researcher would normally send at least one concrete detail. A blank claim plus a deadline is a pressure tactic.

## Next steps

1. **Today:** keep the original email with full headers. Don't delete anything.
2. **Today:** send the reply below. The 48-hour clock then has a documented, professional answer.
3. **Today:** if the repo has no security policy, enable GitHub private vulnerability reporting and add a `SECURITY.md`. That way you can point to it.
4. **Within 48h:** do a quick review of any auth, session, token, or deserialization code paths. Spend a couple of hours at most, mainly to confirm there is an obvious gap.
5. **If they send real details:** reproduce, fix, and publish a GitHub Security Advisory with a CVE and a patched release. Credit them. Consider a voluntary thank-you payment afterwards, decided on its own merits.
6. **If they publish with no details:** post a short statement ("we asked for details and received none") and carry on.

## Reply to send

> Subject: Re: vulnerability report
>
> Hello,
>
> Thank you for getting in touch. We take security reports seriously.
>
> We don't run a bounty program, and we can't pay for an undisclosed report. We'll gladly credit you in the advisory and release notes if the issue is confirmed.
>
> To investigate, we need: the affected version(s), the component or class involved, and steps or a proof of concept to reproduce. Please send them privately through GitHub's private vulnerability reporting at [link] (or reply here).
>
> Once we have that, we'll acknowledge within 3 business days, and coordinate a fix and a disclosure date with you.
>
> Regards,
> The lattice-cache maintainers

## For Dario

Tell Dario that $100 solves nothing and costs a precedent. The reply costs nothing and leaves you in the better position whether the claim is real or not.