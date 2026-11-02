Using the tech-press-relations skill. Before the draft, a few things the skill forces me to flag rather than silently ignore:

**The boilerplate is unusable as written.** Every phrase in it — "world-class," "next-generation," "revolutionary," "seamless," "paradigm shift," "excited to announce" — is on the skill's banned-on-sight list: "each one tells a technical reporter the sender has nothing checkable to offer." I dropped it entirely.

**Comprehensive and 500 words work against you here, not for you.** The skill caps pitches at ~150 words on the logic that technical reporters get their pick and a long pitch reads as an announcement, not a story. I wrote to that limit and moved the extra material behind a link instead.

**The PDF shouldn't be attached.** The skill is explicit: "never send a press release PDF as the pitch," "put nothing load-bearing in an attachment" — reporters can't quote-copy from a PDF on deadline, and a 9-page press release almost certainly still carries the boilerplate voice. Link to a press/methodology page instead; hold the PDF for if she asks.

**The evidence is the weak point, and it's worth being honest about before you send anything.** This is a self-measured benchmark on Fernloom's own CI, not independently run — and it's a raw-speed number, not the total-cost/payback number Dana's piece was actually arguing about for teams under 50 engineers. Pitching it as a rebuttal would read as talking past her argument, which is the fastest way to lose a skeptical reporter. The draft below concedes that gap on purpose — "the good version concedes something true and unflattering" is the skill's own rule for why pitches get read.

**I couldn't run the Step 3 verification** (confirm Dana Whitlock's current outlet, beat, and contact route) — no web access was authorized this turn. Do that before sending; a pitch to a reporter who's moved beats is the most common wasted send.

---

**Subject:** Re: your build-cache piece — our own numbers

**Body:**

> Hi Dana,
>
> Your piece on build caches being a false economy under 50 engineers is the argument most vendor pitches dodge, so I want to be upfront about what this data does and doesn't answer.
>
> We make a distributed build cache (Fernloom). On v4.2, across 62 of our own repos on 16-core CI runners, p95 build time went from 11:40 to 2:05. That's real, but it's self-measured — not independently run — and it's a speed number, not the total-cost-and-payback number your piece was actually about. We don't have that breakdown for teams under 50 engineers yet.
>
> Happy to share the methodology and a harness someone else can rerun, put you with the engineer who ran it, or dig up cost data from smaller customers if that's the more useful angle.
>
> Worth a look, or is this just not the data your argument needs?
>
> [Name], [title], Fernloom

(~145 words)

**What she'll check first:** whether "our own CI" means nobody outside Fernloom has run this, and whether the 62 repos are a real team under 50 engineers or Fernloom's own larger internal test set — either one undercuts the pitch if the methodology link doesn't hold up.

**Before sending:** fill in the sender name/title, get the methodology + harness page live (not attached), and confirm Dana still covers this beat at that outlet.