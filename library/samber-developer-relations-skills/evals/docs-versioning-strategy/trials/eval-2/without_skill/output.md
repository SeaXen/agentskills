**Don't delete 3.x this sprint. Freeze it, point search at 4.x, and delete it when the LTS ends.** 2.x can go now.

Why the plan as written doesn't hold:

- **Contradiction with your release policy.** 3.x is supported until next November (I'm assuming Nov 2027). Deleting docs for a supported version breaks the promise you published.
- **Downloads vs views.** 38% of downloads come from a framework pin, so many of those users never open your docs. They open them when something breaks or a CVE lands, and those are the moments a 301 to the 4.x home page hurts most.
- **Changelog is not a migration path.** A changelog lists what changed. "Read the changelog" leaves 3.x users to do the 3→4 port alone, and they are about 4 in 10 of your installs.
- **301s to the home page.** Search engines treat mass redirects to a home page as soft 404s. The result is lost rankings and dead deep links in Stack Overflow answers and in the framework's own docs.
- **Where the writer's time goes.** Hosting frozen docs costs almost nothing. The cost is maintaining three trees. You can stop that without deleting anything.

## Plan

1. **Freeze 3.x docs (about 3 hours).**
   - Build from the final 3.x tag and accept no more doc edits.
   - Add a banner: "3.x is LTS, security fixes only until Nov 2027. Latest is 4.6." Link the banner to the 4.x equivalent page.
   - Keep 3.x in the dropdown, labelled "LTS".
   - Writer effort from here is zero. Only security advisories touch it.

2. **Point search at 4.x without moving URLs (about half a day).**
   - Set each 3.x page's canonical to its 4.x equivalent (the stable-canonical posture).
   - Where no equivalent exists, keep the page self-canonical.
   - Check the sitemap, canonicals and internal links all agree.

3. **Retire 2.x now (about 2 hours).** It ended two years ago and gets 1% of views. Pick one of these two options. I recommend the first.
   - **Static archive:** keep the pages with an "End of life" banner and `noindex`, and remove them from the dropdown.
   - **Delete:** redirect each page to its 4.x equivalent. Send only unmapped pages to the 4.x home page.

4. **Write one 3→4 migration guide (2–4 days, the main work).**
   - Build it from the 3.x→4.x API diff, not from the changelog.
   - Each breaking change gets a search pattern or error text, before/after code, the fix, and an escape hatch.
   - Run it cold on a real 3.x project, and publish the measured time.
   - This replaces "read the changelog" and cuts support load. The banners from steps 1 and 3 link to it.

5. **Schedule the 3.x deletion for the LTS end date (about 1 hour now).**
   - Write the date into the release policy and the banner.
   - On that date, add per-page redirects to 4.x and archive the old tree.
   - Add a calendar item now.

## Tell the framework maintainers (about 30 minutes)

Their pin is why 3.x is 38% of downloads. Email them with the LTS end date and the migration guide, and ask them to bump to 4.x. Their bump shrinks your 3.x tail more than any docs change will.

## Check afterwards (about 1 hour)

- Search Console: 404s and "canonical chosen by Google" counts for the 3.x paths.
- Page views on 3.x, 2.x and the migration guide.
- Support tickets that mention 3.x.
- The 3.x share of downloads each month.

## What this does for the writer

- Two of three doc trees stop needing edits this sprint.
- The one new task, the migration guide, is bounded.
- If the writer is still underwater after the freeze, the real problem is the 4.x backlog, not the old versions.

## Decisions for you

1. Is the LTS end date Nov 2027? The 3.x deletion date depends on it.
2. 2.x: static archive (my pick) or delete with per-page redirects?
3. Do you have telemetry on who reads 3.x pages, such as referrers from the framework's docs? That would show whether the 2% understates the impact.

**Next step:** answer decision 1, and I'll turn steps 1–5 into tickets with owners.