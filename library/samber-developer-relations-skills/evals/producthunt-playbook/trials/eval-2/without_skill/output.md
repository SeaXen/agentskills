## Tagline (54 characters, Product Hunt's limit is 60)

**Zero-copy JSON parser for Rust: borrow, don't allocate**

Alternates:
- A zero-copy JSON parser for Rust (32)
- Zero-copy JSON parsing for Rust, built to stay tiny (51)

## Maker comment

> Hi Product Hunt, I'm the maker of tinyjson-rs. 👋
>
> Most Rust JSON parsers copy every string into a new allocation. That's fine until you parse a lot of JSON on a hot path, where those allocations become the bottleneck.
>
> tinyjson-rs is a zero-copy JSON parser: parsed values borrow straight from your input buffer instead of copying it. The goal is a small API, minimal dependencies, and predictable memory use.
>
> ```toml
> [dependencies]
> tinyjson-rs = "<latest version>"
> ```
>
> It's MIT licensed and has about 1.2k stars on GitHub, thanks to everyone who's used it, filed issues, or sent PRs.
>
> [One sentence with your best benchmark, e.g. "On <dataset>, it parses X% faster than serde_json's `Value` with Y fewer allocations." Delete this line if you don't have a number you'd defend.]
>
> I'd love your feedback on one thing: **what's the first thing you'd want from a zero-copy parser that you can't get today?** I read every comment and reply.
>
> Repo: <github link>

## Before you paste

- **Fill in the three placeholders:** version, benchmark line, repo link. I didn't invent numbers because I don't have your benchmarks. A false performance claim is the fastest way to get picked apart in the comments.
- **Check the "borrow" wording.** Strings with escape sequences normally can't be borrowed as-is. If your crate allocates for those, add "(escaped strings are the exception)". Developers will ask about it.
- **The `tinyjson` account is a risk.** Product Hunt favors personal profiles for makers, and a project-named account can look like a brand or a bot. Consider switching the display name to your own name, keeping the logo as the product thumbnail. I can't tell from here whether Product Hunt restricts this, so check their current maker guidelines.