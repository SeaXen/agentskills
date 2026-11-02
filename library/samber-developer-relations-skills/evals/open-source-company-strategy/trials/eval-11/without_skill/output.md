**CFO number: ~$680K year 1. ~$500K/year steady state (year 2+).**

Below: breakdown, biggest cost driver, operating model, assumptions to confirm.

## 1. Year 1 budget ($680K)

One-time setup + steady-state run rate, first year:

1. OSPO lead, 1.0 FTE loaded — $200K
2. Patch-carry engineering labor (40 patches, current state) — $180K
3. Repo publish readiness, 3 repos (license audit, history scrub, CI, docs, trademark check) — $60K one-time
4. Tooling: SBOM + license scanning (FOSSA/Black Duck/Snyk class), security scan for public repos — $60K
5. Foundation dues (LF Energy Silver tier — fits grid-balancing domain directly) — $40K

Plus: legal/counsel time $30K, policy rollout/training $8K, contingency 12% ($75K). Sum ≈ $680K.

## 2. Steady state, year 2+ ($500K/year)

Same buckets, minus one-time repo setup, minus reduced patch tax (see below):

1. OSPO lead — $200K
2. Patch-carry labor, post-upstreaming investment — $90K (down from $180K)
3. Tooling — $65K
4. Foundation dues — $40K
5. Legal + contingency + maintenance buffer — $105K

## 3. Real cost driver: the 40 patches, not the 3 repos

Publishing repos and joining foundation is cheap. Patch carry is not.

- 40 patches, rebased every release, no upstreaming = recurring tax forever.
- Estimate: 1 dev-day avg per patch per rebase. Quarterly upstream releases = 160 dev-days/year = 0.7 FTE, just conflict resolution + regression test. That number scales with upstream's release cadence — confirm it, it drives everything above.
- Fix: one-time push to upstream 15-20 of the 40 patches (bugfixes, non-differentiating changes). Cost: ~70-100 dev-days one-time (~$70K), cuts ongoing carry roughly in half.
- Board framing: this is not new spend created by "going open source." It is existing hidden spend, now measured. That's worth saying explicitly — CFO's instinct will be "why does open source cost $500K," and the honest answer is most of it was already being spent, invisibly, on patch maintenance.

## 4. Operating model

No new department. Light structure, existing org:

- **OSPO lead** (1 FTE) — owns policy, tooling, intake, foundation liaison. Reports to VP Engineering. Dotted line to Legal for compliance sign-off.
- **Working group**, monthly: OSPO lead + eng director owning scheduler patches + part-time legal counsel + one security rep. No standing committee beyond this.
- **Decision rights, tiered**:
  1. Inbound OSS, pre-approved license (MIT/BSD/Apache-2.0/MPL-2.0) — engineer self-serve, CI-gated, no approval needed.
  2. Inbound OSS, copyleft or unknown license — OSPO lead + legal must approve before merge.
  3. Outbound (new repo, open-sourcing internal code) — OSPO lead + legal sign-off mandatory, VP Eng approves scope.
  4. Foundation seat/vote — OSPO lead runs day-to-day; CTO/VP Eng holds any formal board or TSC seat.
  5. Upstream-first default on patches — eng director's call; OSPO lead tracks upstreaming rate quarterly.
- **Cadence**: quarterly board update, monthly working group, day-to-day enforced by CI (license gate), not by meetings.

## 5. Assumptions to confirm before board (changes the number)

1. Upstream scheduler's release cadence (drives patch-tax math above — quarterly assumed).
2. Company jurisdiction/salary basis (USD loaded-cost figures used — adjust if EU/other).
3. Whether SBOM generation already required by a regulator you serve (NERC CIP / NIS2-class utility customer contracts often mandate this — if yes, tooling line is non-optional, not a nice-to-have).
4. Current OSS tooling state (if license/SBOM scanning already exists, cut $50-65K).
5. Which 3 repos, and whether any require trademark clearance beyond company's own IP — that's the range on line 3 of the year-1 breakdown.

Next: confirm upstream release cadence with eng director owning the scheduler patches — that single number moves the CFO figure by up to $90K either direction.