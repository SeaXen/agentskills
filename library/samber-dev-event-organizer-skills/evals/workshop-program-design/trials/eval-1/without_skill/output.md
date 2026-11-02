## Answer: 4 people for the first 45 minutes, then 2 for the rest

✅ **Two engineers stay for all 3 hours. Both stewards stay for the first 45 minutes, then go back to registration.**

Setup is where the room needs most help. After that, only the engineers can answer Rust questions.

### Why this number

The figures below are my planning estimates, not measured data. Replace them with numbers from a past session or a dry run if you have any.

1. **Setup is the crunch.** Everyone starts at the same moment, and conference wifi with 400 people on it makes `cargo build` slow. Say 25% of 36 people hit a setup problem (toolchain, proxy, slow crate download). That is about 9 people at about 8 minutes each, or roughly 70 helper-minutes in the first 30 minutes. Clearing that queue takes 3 to 4 people. Two engineers alone would leave some people waiting 20 minutes or more.
2. **After setup, demand flattens.** Assume about 30% of people get stuck once per refactor, at about 5 minutes each. That is 36 × 4 × 0.3 × 5, or about 215 helper-minutes spread over about 150 minutes. That is 1.5 helpers busy on average, so 2 engineers is right.
3. **A linear path makes stuck people costly.** Nobody can skip ahead. A person stuck at refactor 1 sits idle for the rest of the three hours unless someone unblocks them. Helper responsiveness matters more here than in a menu-style workshop.
4. **The stewards add value in the first 45 minutes, not afterward.** They can't debug Rust, but they can:
   - run a red/green cup system at each seat, so engineers know who's stuck without walking every row
   - handle wifi and power issues
   - queue people for the engineers
   - pair a stuck person with a finished neighbour

   That keeps the engineers on Rust problems during the crunch. Once people are building, the stewards' skills stop mattering to this room.
5. **The instructor doesn't count.** They are teaching, and every minute they spend debugging one seat stalls 35 others.

### What to say to your volunteer lead

- "I'm not taking the stewards for the whole session. I'm borrowing them for the 45 minutes when this room has a real bottleneck, and returning them for the other 2h15."
- "Registration work doesn't need special skills, so anyone can cover it. The two engineers are the only ones who can unblock a Rust build, so I can't spare them."
- "This room has 36 of our 400 attendees, about 9%. It still needs 2 of our 4 volunteers, because it has a hard dependency chain and the other sessions don't."
- Offer a trigger: if the registration queue passes a length you agree on, a steward leaves the room early.

⚠️ The one thing to check is timing. If the session starts when registration peaks, you can't do both. In that case give registration one steward for the full 45 minutes. The room then gets 3 people during setup instead of 4, which is still acceptable if you do the next section.

### Cheaper than extra people: cut the setup load

These reduce the need for helpers, which strengthens your case to the lead.

- Send pre-work 3 to 5 days ahead: install the toolchain and run `cargo build` once.
- Vendor the dependencies (`cargo vendor`) or put them on USB sticks, so nobody depends on the venue wifi.
- Publish a checkpoint branch for each refactor. A stuck person can jump to the start of the next step, and the linear path becomes recoverable.
- Add a one-command setup check script, so "it works" or "it doesn't" is clear in seconds.
- Plan for roughly 25 to 32 people actually showing up. Registered doesn't equal present. Staff for all 36 anyway, in case of walk-ups.

### Fallback

If the lead refuses to release both stewards for the first 45 minutes, take one. The room then has 3 people during setup instead of 4. That is workable only if you vendor the dependencies and run the pre-work, because setup trouble then drops enough for 3 people to clear.