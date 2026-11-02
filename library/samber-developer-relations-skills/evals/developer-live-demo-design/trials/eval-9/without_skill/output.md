Yes — pre-staging login, CLI auth, and project creation is the right call for a 10-minute slot; setup friction is what actually kills short demos, not the commands themselves.

Two things to check before you're on stage:

- **Auth can expire silently.** If Tinderbox uses OAuth or a token with a short TTL, "logged in this morning" can be logged out by evening. Do a final dry run 15-30 min before your talk, not days before.
- **Network is the real risk, not the CLI.** Meetup wifi is unreliable and often locked down (captive portal, blocked ports). If any of your three commands hit a remote API, have a fallback: either a local/offline demo mode, or a pre-recorded terminal capture (asciinema or a screen recording) you can cut to if the live run stalls.

Two small polish items, since it's a talk not a work session: bump your terminal font size and use a high-contrast theme for the back row, and time the three commands with your narration out loud once — the talking, not the typing, is what usually blows a 10-minute budget.