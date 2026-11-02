# Homepage plan: now through June 2

## Recommendation

1. **Do now:** replace Submit a Talk with a "CFP closed" banner. Point Register at a holding page, labelled honestly. Publish no price.
2. **Skip:** the countdown timer and the "$249 from June 2" teaser.
3. **Make June 2 a single edit:** the Register button should link to a URL whose content changes on June 2. The homepage itself then needs no edit for the button.
4. **Give the flip an owner:** one named person, one backup, one calendar slot, and a pre-flight check on June 1.

## What the homepage should show

**Banner (replaces Submit a Talk):**
> CFP submissions are now closed. Registration opens June 2.

Your draft said "opens soon". A date is better because it gives visitors a reason to return.

**Register button:**
- Label it **"Registration opens June 2"**, not "Register". A button labelled "Register" that leads to a "not yet" page reads as broken.
- Link it to `/register`.
- The page at `/register` should have three things:
  - the date
  - an email capture for "Notify me" (or a link to your newsletter or mailing list)
  - one line with the event: Quarrydata Summit, Austin, September 9-10

**Also check:**
- The CFP page itself and any other Submit a Talk links, such as the nav, footer, and sponsor and speaker pages. Mark them closed or redirect them to the banner.
- Remove the deadline wording from anywhere else on the site.

## Why not the countdown and early-bird teaser

1. **The price isn't confirmed.** Once "$249" is public, people screenshot it and expect it. If pricing lands at $279, you either honor the lower price or take the trust hit. Wait for confirmation.
2. **A countdown on a hand-edited page fails visibly.** If June 2 passes and the volunteer is late, the page shows "0 days" next to a dead button.
3. **You can still tease early-bird without a number.** Put this on the holding page: "Early-bird pricing at launch. Notify me." Once pricing confirms, add the number on June 2.

## Making it happen

Nothing on the page changes by itself, so the plan has to cover who does it, when, and how you know it worked.

1. **Do the June 2 work in advance.** Before May 26, the volunteer prepares the June 2 versions of two things:
   - the homepage banner, changed to "Registration is open", or removed
   - the `/register` page, replaced by a redirect to the ticketing provider
   Keep them in a branch or a spare file, ready to swap in. Because the button already points at `/register`, the flip touches one page, plus the banner on the homepage.
2. **Assign names.** One owner and one backup, both with edit and deploy access confirmed today. The backup matters because a single volunteer is a single point of failure.
3. **Set a deadline for pricing.** Ask the pricing group to confirm the early-bird price by about May 26. If they miss it, launch June 2 with the confirmed tiers. Don't hold the flip for the early-bird number.
4. **Run a pre-flight on June 1:**
   - The ticketing provider is live, and someone has completed a test purchase.
   - Prices on the page match what the checkout shows.
   - The prepared files are ready to deploy.
   - Everyone involved knows the flip time.
5. **Flip at a fixed time on June 2**, for example 9:00 Central. Publish it as part of the same step as your announcement email or social post, so the page and the announcement go out together.
6. **Verify after the flip.** The owner checks on a phone and a desktop, in a private window to avoid cache:
   - The banner is gone or says registration is open.
   - The Register button reaches checkout.
   - No "opens June 2" text remains anywhere.
   - If you use a CDN or host cache, purge it.
7. **Add a fallback line.** If ticketing isn't ready on June 2, the owner changes the holding page to a new date and tells your list. The page never goes silent.

## Before you build the countdown

If the volunteer still wants a countdown, count down to the date only, with no price. Don't rely on it for anything that matters, because the manual flip is what actually happens.