# Which fix first: neither one as written

Do a narrowed version of (1) first. Drop (2) as written. Give the Zendesk customers TL1 or TL2 instead of TL3. I haven't looked at your instance, so setting names below may differ slightly by Discourse version.

## Why not (1) as written: queue everyone

- Your spam comes from brand-new accounts. Regulars, staff and customers don't post it, but a blanket queue holds all their posts too.
- Every legitimate reply waits for a moderator. Your 2,000 imported customers are your most valuable users, and they would hit the queue on every post.
- The cause is that new accounts can post links freely. The fix is to gate only accounts that haven't earned trust yet.

## Why not (2) as written: bulk TL3

- TL3 is a moderation-adjacent role in Discourse. It can recategorize and retitle topics, edit wiki posts, and its flags carry heavy weight. Giving that to 2,000 accounts you haven't vetted is a bigger risk than the limits you're trying to fix.
- A TL3 granted by script and not locked is not stable. Discourse's nightly job recalculates levels, and accounts that don't meet the TL3 stats can be demoted back. A locked TL3 stays but bypasses the earn-it checks.
- The new-user limits only need TL1 or TL2 to lift. TL3 solves nothing extra and adds risk.
- Check that the Zendesk emails were verified or come through SSO. If not, anyone who can claim an imported address inherits the elevated level.

## Do this, in order

1. **Customers to TL1 or TL2 (about 30 min).** Put them in a group first, e.g. `customers`, and promote that group.
   - Use TL2 for verified customers, TL1 for the rest.
   - Optionally lock the level with `trust_level_locked` so the nightly recalculation can't move it.
   - Do this *before* step 2, or customers who are still TL0 will be queued.
2. **Queue only unproven accounts (about 10 min).** Set the post-approval settings so users below TL1 go to review:
   - `approve_unless_allowed_groups` and `approve_new_topics_unless_allowed_groups` in current versions. In older versions they are `approve_unless_trust_level` and `approve_new_topics_unless_trust_level`.
   - Set them to `trust_level_1`. Don't remove `trust_level_0` from the exempt list. `trust_level_0` contains every user, so that would queue everyone.
   - Your ~40 spammers a day stay invisible. A bulk reject plus "delete user and block" clears the queue fast.
3. **Close the door (about 1 hour).** This cuts the volume you have to review:
   - Add an Akismet plugin or Discourse AI spam detection.
   - Add Turnstile or hCaptcha at signup.
   - Block casino and SEO terms with watched words set to "block".
   - Lower `newuser_max_links` and block disposable email domains.
4. **Re-check after a week.** Look at queue volume, how many legitimate TL0 posts get stuck, and how many spam posts still get through. If queue time is high, add the step 3 filters before widening anything.

## The one-line rule

Gate by trust, not by person. Move proven customers above the gate (TL1/TL2), and keep the gate on newcomers.