**Yes, there are problems.** The plan loses most of what marketing paid for, and the flip creates a new legal risk.

**1. Six months of zero SEO**
- With `login_required` on, Google only sees the login page, so nothing is indexed.
- Every thread posted in those six months starts with no ranking history on the day you flip. Indexing then takes weeks to months.
- Links people share to threads during that time hit a login wall, so they earn little SEO value.
- A closed community also grows slowly. Visitors can't see any value before signing up, so you get few lurkers and little organic joining.

**2. The flip exposes old content retroactively**
- Members will have posted believing the forum was members-only. The flip makes all of it public and searchable at once.
- That can include customer details, internal-ish questions, and personal data. Real names, avatars and profiles become visible too.
- This is the opposite of the "see what people post" goal. The riskiest posts get published without their authors' consent.
- Under GDPR, changing the audience changes the processing. You would need to update the privacy policy and ToS before flipping, give members notice, and offer deletion or anonymization.

**3. A login wall doesn't remove the liability counsel likely cares about**
- Defamation, copyright and illegal content are your problem whether or not the forum is public. The controls are moderation, ToS, and a takedown process.
- It's worth asking counsel what specific risk they're worried about.

**What I'd propose instead**
1. Make the forum public to read and login-required to post. Use the Discourse defaults.
2. Pre-moderate new users. Use the approval queue (`approve_unless_trust_level`) and restrict links and images for new accounts. Add watched words.
3. Put anything sensitive in private categories, such as a customers-only or support category.
4. Publish the ToS, privacy policy and takedown process before launch.
5. If counsel still wants a soak period, keep the forum public but turn off search indexing (`allow_index_in_robots_txt`) for 4 to 8 weeks. Flip it only when written exit criteria are met, such as moderators trained, queue stable, and ToS live. Don't use a calendar date. Indexing is also easier to reverse than a login wall.
6. If the six-month login wall is non-negotiable, split it. Keep the support and customer categories behind login, and leave a public category for general discussion and evergreen content, so that part can rank from day one.

I haven't looked at community.ferrolink.io itself, so check its current settings. Counsel may have contract or regulatory constraints I can't see, such as regulated customer data.

**Next step:** ask counsel which risk the login wall is meant to address. If it's "bad posts", the answer is pre-moderation. If it's "private customer data", the answer is private categories. Neither needs a six-month blackout.