**Mintlify, unless you have a named person who can own the build. In that case, Docusaurus.** This is conditional because I can't answer your questions about owners and constraints, so I've marked what I assumed.

**Why Mintlify is the default.** Public API docs for a new site fall into one of two classes. Docusaurus is a self-hosted generator, which is free but needs a named owner for upgrades, plugins, search and security fixes. Mintlify is a hosted platform, so the vendor runs the build and hosting, and you pay in subscription multipliers instead. The skill's tie-break is the build owner. With no owner, the choice tips to hosted, because an unowned self-hosted site rots within a year. A new site also has no migration or URL-preservation cost to weigh.

**Assumptions.** None of these is confirmed, and any one of them can flip the answer:
- ASSUMED: no named person gives the site committed monthly hours.
- ASSUMED: you have no hosting or residency constraint, such as no third-party hosting or data staying in one region.
- ASSUMED: the API reference comes from an OpenAPI spec, and guides sit alongside it.
- ASSUMED: you have a handful of editors, not dozens.

**Switch to Docusaurus if any of these is true:**
- A named person or team has committed monthly hours to keep the site running.
- You have many editors, or several docs sites, so per-seat and per-site pricing would grow quickly.
- Security or compliance forbids third-party hosting of the editor and content.
- You want the exit cost near zero, since content stays in your own Git repo.

**The one question that decides it:** who keeps this site running after launch, and for how many hours a month?

**Why the comparison posts disagree.** Most "best docs tools" lists are written by a vendor that ranks itself first, and feature rows are claims, not evidence. Tom Johnson, a docs practitioner, observes that readers rarely notice a platform change. Your content structure and API-reference quality matter more than this choice.

**Before you commit:** I didn't check either vendor's current pricing or docs, so verify your must-haves there. Then port your five to eight hardest pages to both, since you have a quarter. Include the generated API reference page, the quickstart and your longest page. Have your least technical editor publish a fix, and run the export to see what leaves with you. Count the Mintlify-specific components those pages needed, because that count is your exit cost.

I didn't run the skill's full interview or write the decision record. If you answer the owner question, I can firm up the pick.