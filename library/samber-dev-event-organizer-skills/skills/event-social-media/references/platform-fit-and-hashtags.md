# Platform fit and hashtag decisions

Contents:

- The platform-fit table by campaign phase.
- The platform-mechanics caveat.
- The three-purpose hashtag taxonomy.
- The community-signalling contrast.
- How many tags to carry.
- The neutrality-policy scope flag.
- The who-posts-versus-who-requests workflow.

## The platform-fit table, organized by campaign phase

The table below organizes platforms by category and what each is good for in different campaign phases. The posting-frequency column is deliberately absent: those numbers describe a continuous personal or company brand accruing followers over years, not a dated campaign that starts near-cold each edition. Frequency here comes from the campaign's own phase dates, handed down by `samber/dev-event-organizer-skills@event-marketing-plan`.

Platform categories, not brands, because the mix turns over every few years and any brand list ages badly.

| Platform category                     | Reaches                                                                                                       | Strongest phases                                           | Format that works                                                     |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- | --------------------------------------------------------------------- |
| Professional network                  | Managers and employers who approve travel and training budgets; sponsors scouting events; B2B-facing speakers | Announcement, CFP open, sponsor-facing moments, final push | Longer text with one image; the "why your team should be there" angle |
| Microblog / short text                | Practitioners in a community that still gathers there; press and community amplifiers                         | All phases; strongest during live coverage                 | Short, frequent, reply-friendly; threads for agenda releases          |
| Community chat (server, forum, group) | People already adjacent to the event - prior attendees, local meetup members                                  | CFP open, final push, live                                 | Conversational, not broadcast; a post from a person, not the brand    |
| Short-form video                      | Student and early-career audiences, especially campus-scale events                                            | Announcement, final push, wrap                             | Venue and vibe, not information; the link lives elsewhere             |
| Photo-first feed                      | Same audience as short-form video; also the visual archive                                                    | Speaker reveals, live, wrap                                | Speaker cards, room shots, day-after recap                            |
| Link aggregators / community boards   | Topic communities where self-promotion has strict norms                                                       | CFP open only, usually                                     | A genuine contribution, posted by a participant, or nothing           |

Two things this table cannot decide for you:

- Which of these categories your audience actually occupies. That is interview Q3, and it outranks every row here.
- Whether the event may post at all in the last row's communities. Those norms are set per community, and a rule-breaking post costs more than the reach it buys.

MLH's hackathon organizer guide names a six-platform spread - TikTok, Facebook, Twitter, Instagram, Reddit, LinkedIn - plus community groups and named ambassador programs, for a campus-scale student audience. DevOpsDays' organizing guide names LinkedIn specifically as a channel for _finding sponsors_, which is a different job than filling seats. These platform recommendations are specific to campus-scale hackathons and foundation-run conference models; Q3 always outranks any preset list.

## Platform mechanics: verify, never hardcode

Character limits, hashtag conventions, image dimensions and link-preview behavior all change with platform policy, sometimes twice a year. Check the current values when producing assets rather than carrying a number into a template that will quietly be wrong in six months. Design the kit so a changed limit costs an edit, not a rebuild: keep the copy block short enough to survive the tightest platform in the set.

## Hashtags: decide by purpose, not by habit

CNCF's social guidelines name three distinct reasons to use a tag, not one generic "use a hashtag" instruction:

1. **Campaign measurement** - a dedicated event tag (`#KubeCon` in the source) used to track one campaign's reach.
2. **Reach expansion** - a broader trending topic (`#cloudnative`) to reach beyond current followers.
3. **Categorization** - a narrow topical tag (`#Kubernetes`) to label a post by subject.

The reusable consequence: an event needs at minimum **one dedicated campaign tag distinct from any broader community or topic tag it also rides**. Collapsing both into a single tag loses the measurement purpose - you can no longer separate your campaign's traffic from the topic's background noise.

### The community-signalling contrast

DevOpsDays uses a hashtag differently again. Its guide tells a prospective organizer to "Post on social media that you'd be interested in running one in your region. (Use the #devopsdays hashtag.)"

That is a standing community-identity tag: it lets a decentralized, multi-city network find each other and makes the franchise legible as one brand across independently-run cities. It is not a per-edition campaign tag and cannot be measured as one.

Any event on a franchised or federated brand carries both kinds at once: the shared community tag that signals membership, and its own edition tag that measures this cycle. Name which is which in the plan, and never report the community tag's volume as your campaign's reach - most of it belongs to other cities.

### How many tags to carry

Three is usually the whole set: one campaign tag, one community or topic tag, and optionally one categorization tag for a specific track or theme. Beyond that, tags stop routing and start decorating. Fix the campaign tag before the first post ships - a tag changed mid-campaign splits the archive permanently, and there is no way to merge them afterwards.

## Neutrality policy: scope it before importing it

CNCF's content rules are strict and specific:

- Only "vendor-neutral, community-sourced" content is allowed on project channels.
- Nothing may promote a vendor product or point at a company website.
- No sharing of member-company or vendor posts, even when accurate.
- Retweets are limited to an explicit allow-list: news outlets, project handles, personal handles, and the foundation's own accounts.

Community content combining more than one project is prioritized over single-project content, and any publicly-open activity may be promoted "as it benefits the ecosystem as a whole". Reused images and video must be free for commercial use with no attribution required, unless credited to the community member who made it.

**These rules exist to enforce foundation neutrality**, and that constraint does not exist at the other governance poles:

- A **community-run** event with a handful of sponsors has no sponsor-neutrality policy to enforce; applying the allow-list would forbid it from resharing a sponsor's perfectly friendly post about the event for no reason.
- A **vendor-run** event's account exists partly to promote that vendor's product; the rule contradicts the event's purpose outright.
- A **foundation-run or heavily sponsor-diverse** event is the pole where it applies, and where organizers should expect to be held to something like it whether or not they wrote it down.

The image-licensing rule is the one part worth carrying everywhere: reusing a photo you did not take, without a license or a credit, is an exposure at any pole.

## Who posts versus who requests

CNCF routes "please share this" requests through a dedicated internal channel or a named inbox (`social@cncf.io`) rather than ad hoc direct messages to whoever holds the account. That separation is worth copying on any multi-person team, at any scale:

- **One named account owner** posts. Nobody else has the password.
- **One documented request path** - a channel, an inbox, a shared queue - collects requests from speakers, sponsors, volunteers and co-organizers.
- **A stated turnaround** so requesters stop chasing, and one line on what does not get posted (whatever the neutrality decision above settled).

Without this, the account owner spends the campaign fielding one-off messages across three private channels, and a genuine request arriving the night before doors gets lost in exactly the moment it mattered.
