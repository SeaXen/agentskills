# Verdict: not as planned ❌

Two of the three parts need to change. The goal is fine, but the plan will likely miss it and carries real legal and reputational risk.

## What's wrong

1. **Inferring "under-represented" from photos and names. Drop this.**
   - It is unreliable. Names and faces don't tell you gender, ethnicity, disability, or any other dimension, and you will mislabel people.
   - It is probably illegal for you. Inferring ethnic origin, health, or similar traits is special-category processing under GDPR Art. 9, and you are in France. The board goal does not give you a lawful basis.
   - If it leaks, "the conference profiled contributors by face" is the story. That's worse than missing the number.

2. **Top 200 contributors by commits. This works against the goal.**
   - That list is mostly the established people, who are the least likely to be first-time speakers.
   - Commit count also under-counts docs, tooling, issue triage, and newer contributors.
   - Many of those 200 are bots, employees of the same few companies, or repeat speakers.

3. **Mass Discord DMs. Avoid.**
   - Unsolicited bulk DMs break Discord's rules on spam and unsolicited messages. Accounts and the bot get flagged.
   - They feel like cold outreach from a scraper. Some of the people you most want will not reply, and some will warn others.
   - A script that DMs 200 people at once is the problem. A few personal messages are fine.

4. **speakerline.io.** I can't verify what it is or how it sources its data. Before relying on it, check four things:
   - whether it is opt-in
   - whether it covers WASM component model people
   - how it handles profile data
   - whether you can contact people through it

   Treat it as one source among several.

## What to do instead

Count **first-time** speakers first. It is observable and easy to verify. Under-represented is a harder, self-declared category.

1. **Define the number with Aneta (do this first).**
   - Fix what counts as "first-time" (never spoken at a conference? at any event?) and how "under-represented" is measured.
   - Use voluntary, optional self-identification in the CFP or invite form, with a "prefer not to say" option. Store it separately from the review data and delete it after the event. Keep it out of anything speakers can see.
   - Get the board to confirm the metric before you start. Decide whether "invited lineup" includes keynotes.

2. **Run a CFP, not just invitations.**
   - Invitations alone skew toward people you already know.
   - Publish the CFP in the project's Discord channels, GitHub discussions, and the component-model working-group channels.
   - Add a beginner track or short 15-minute slots. Offer a speaker-mentor program and say so in the call.
   - Review proposals with names hidden where you can.

3. **Source candidates from public work, not demographics.**
   - Use GitHub's API for activity signals: docs, tooling plugins, issue reports, blog posts, and talks given.
   - Build the long list from actual work, not rank. Look at people who ship tools, write guides, or file good issues, not just the top committers.
   - Check each person's public activity for earlier talks. That tells you who is first-time.
   - Contact them through their public contact details, and have a human write each message, ideally a maintainer or someone the person knows.
   - **Pulling the contributor list writes data to a file.** Keep only public handle, repo, and activity. No photos. Add a retention limit and tell people in your privacy notice.

4. **Use Discord openly.**
   - Post the CFP in channels. Ask maintainers of each repo to nominate and to forward it to newcomers.
   - Hold a "first talk" office hours session. Offer help with abstracts and rehearsal.
   - If you do DM, send only a handful, personally, to people who have been active in the server. Avoid scripts.

5. **Do the math early.**
   - A pool of a few hundred people is small. If the lineup has 12 slots, the goal means 6 slots for first-time or under-represented speakers.
   - First-time is the easier half to hit. Prioritize it, and treat under-represented as the stretch part.
   - Set a checkpoint: if CFP submissions are short of the target by a set date, you broaden outreach (adjacent communities like WASI, Bytecode Alliance projects, Rust and JS tooling groups) before you cut standards.

## Next steps

1. Meet Aneta this week and agree on the two definitions and how you'll measure them. ⏳ about 30 min.
2. Draft the CFP, including the optional self-ID form and mentoring offer.
3. Check speakerline.io against the four questions above.
4. I can then write the GitHub activity script (public signals only, no demographics) and the outreach templates. Tell me which one first.