## Why 62% never reach "create branch"

You, and the two engineers who wrote it, can't see the friction because you structurally don't experience it: you already have the CLI installed, you're already authenticated, and you already have a project. The page reads fine to you because for you it effectively starts at step 4. That's not a documentation problem you can proofread your way out of — it's a structural one.

Four things are almost certainly compounding:

1. **It's a waterfall of independent failure points.** Install → auth → create project → create branch is four sequential steps, each with its own way to silently break (PATH issues, an OAuth redirect that doesn't return cleanly, a region/plan picker that stalls someone). Even at a generous 90% success per step, four steps compound to ~66% — remarkably close to your 62%. You don't need one big broken step to explain the number; four slightly-leaky ones do it.
2. **No checkpoints.** None of the four steps shows "you should see X." A user who hits a silent failure has no signal they're stuck — they don't file a bug, they just close the tab. That's exactly the kind of drop-off that's invisible to three people who never fail a step.
3. **"Create project" is a decision-heavy step placed before the user has any reason to care.** Region, plan, naming — none of that has anything to do with understanding what a branch even is, and it's asked for before the payoff, not after.
4. **There's nothing to see.** A freshly created, empty project makes "create a branch" a CLI incantation with no visible result. Branching only feels valuable when there's data to watch get copied instantly.

The fix isn't better prose on the existing five sections — it's cutting a step (pre-provision a demo project instead of making people configure one before they've seen value), collapsing another (install+auth as one verified command), and adding a payoff people can actually see. Below is the rewritten page.

---

# Create your first Postgres branch in under 5 minutes

A branch is an instant, full copy of your Postgres database — schema and data — that you can write to without touching production. This walks you through creating one and proving to yourself it's real, using a demo project we've already loaded with sample data so you're not branching an empty database.

**Time:** ~5 minutes
**You'll need:** a terminal, and an email address (no credit card).

Prefer clicking over typing? Open the demo project in the [dashboard](https://app.halyard.example/demo) and hit **New Branch** — it's instant and skips the CLI entirely. The rest of this guide covers the CLI, since that's what you'll use day to day once you're branching real projects.

---

## Step 1: Install and log in

One command does both:

```bash
curl -fsSL https://cli.halyard.example/install.sh | sh
```

This installs the `halyard` CLI and opens your browser to log in (or create an account if you're new). Come back to the terminal once the browser shows "You're logged in."

**Check it worked:**

```bash
halyard whoami
```

You should see:

```
Logged in as you@example.com
Demo project ready: halyard-demo (postgres 16, ~4k sample rows)
```

If you see `command not found: halyard` instead, your shell's PATH hasn't picked up the new binary yet — open a new terminal tab and try again. If `halyard whoami` says `not logged in`, run `halyard login` directly.

---

## Step 2: Create a branch

Every new account gets a ready-to-go demo project — no setup, already has data in it. Branch it:

```bash
halyard branch create --project halyard-demo --name my-first-branch
```

You should see:

```
Creating branch 'my-first-branch' from halyard-demo (main)...
Branch ready in 0.8s
Connection string: postgres://my-first-branch.halyard-demo...
```

That's it — you just forked a full Postgres database. Not a snapshot, not a subset: a complete, independently-writable copy, ready in under a second regardless of the source database's size.

---

## Step 3: See that it's real

Connect to your branch and confirm the data came with it:

```bash
halyard branch connect my-first-branch
```

This drops you into `psql` against your new branch. Run:

```sql
SELECT count(*) FROM orders;
```

You'll get the same row count as the demo project's `main` branch — because it's the same data. Now try writing to it:

```sql
DELETE FROM orders WHERE id = 1;
```

Then check `main` is untouched:

```bash
\q
halyard branch connect main --project halyard-demo
```

```sql
SELECT count(*) FROM orders WHERE id = 1;
```

Still there. Your branch is a fully isolated copy — this is what lets you test migrations, run a destructive query, or give a PR its own database, without any risk to `main`.

---

## Troubleshooting

**`halyard: command not found` after install**
Your shell hasn't reloaded its PATH. Open a new terminal window, or run `source ~/.zshrc` (or `~/.bashrc`).

**Browser login window didn't open**
Some remote/SSH environments can't open a browser. Run `halyard login --device` instead — it prints a code and a URL to open on any device.

**`halyard branch create` hangs or times out**
Usually a network/firewall issue blocking outbound HTTPS. Run `halyard doctor` — it checks connectivity and prints exactly what's blocked.

**`psql: command not found`**
`halyard branch connect` shells out to your local `psql`. Install Postgres client tools (`brew install libpq` on macOS, `apt install postgresql-client` on Debian/Ubuntu), or pass `--connection-string-only` to get a string you can use with any client.

---

## What you just did

You created and connected to a Postgres branch without configuring a project, picking a region, or loading your own data first. In practice you'll do this against your own database instead of the demo:

```bash
halyard project create my-app --import-from <your-connection-string>
halyard branch create --project my-app --name feature/new-signup-flow
```

**Next steps:**
- [Connect your own database](https://halyard.example/docs/import) — bring your existing Postgres in
- [Branch on every pull request](https://halyard.example/docs/ci) — wire branches into CI so every PR gets its own database
- [CLI reference](https://halyard.example/docs/cli) — every command, every flag
- Delete the demo project any time with `halyard project delete halyard-demo` — it doesn't affect your real projects

---

**One more thing, not for the page:** add per-step funnel events (`install_completed`, `auth_completed`, `branch_created`, `connect_completed`) rather than just page-load vs. final-CTA. Right now you only know 62% drop somewhere across four steps — you don't know which one. That number will tell you whether the rewrite actually fixed the structural issue or just moved the drop-off point, and which of the four changes above mattered most if you want to ship them incrementally instead of all at once.