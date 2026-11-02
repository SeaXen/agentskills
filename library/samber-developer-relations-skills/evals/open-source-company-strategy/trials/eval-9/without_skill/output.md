## Feature move: audit-log export + SSO → paid tier

**This is the open-core "rug pull" pattern, even without a license change.** License staying MIT doesn't neutralize the trust hit — you're taking away something that's been free for ~2 years, not withholding something new. The community reacts to what's removed, not to what's technically permitted.

- **SSO is low-risk.** Gating SSO is the industry-standard enterprise line (GitLab CE/EE, most open-core plays) — expected, defensible, barely worth an announcement.
- **Audit-log export is the riskier one.** If any self-hosted community users lean on it for their own SOC2/compliance evidence, pulling it isn't an inconvenience — it's a compliance regression. Check who's actually using it in CE before deciding it's purely an "enterprise nice-to-have."
- **MIT means the code doesn't disappear — someone can fork the last version that has it.** Unlike HashiCorp/Redis/Elastic relicensing to BSL/SSPL (which blocked forking), your core stays MIT. Anyone can fork the last commit with SSO + audit-log intact and keep shipping it as a fully-featured community edition — potentially becoming the "real" community project while yours looks stripped. This is the single biggest practical risk here, bigger than PR backlash.
- **Existing self-hosted deployments break on upgrade, not just new users.** Decide now: does the *next release* silently drop these features for people already running them, or do you grandfather anyone on a current version? Removing something already running in someone's production stack is a different severity than gating it for new signups.
- **Check contribution history before you touch this code.** If any of the SSO/audit-log implementation came from external contributors (not employees), moving their PRs into a proprietary tier is a real problem — they contributed under the assumption it'd stay open. Verify your CLA covers this, or rewrite the enterprise version from scratch rather than relicense contributed code.
- **Give real notice, don't ship-and-changelog it.** A 60-90 day public heads-up with a migration path lands very differently than someone noticing it in a diff. Silence here reads as "hoping nobody checks," which is worse than the change itself.
- **Softer alternative worth considering:** keep basic audit logging in CE (who did what, when) and gate only the *export/retention/SIEM-integration* layer. That's a narrower cut that's easier to defend as "enterprise scale," not "enterprise permission to see your own logs."

## Repo rename: solventlabs/solvent → solventflow/solventflow

"Cosmetic, no code removed" undersells the blast radius. Concrete things that break or need active work:

- **Renaming org AND repo at once is flakier than either alone.** GitHub redirects repo renames and org renames separately, but a combined move has more reported edge cases (git remotes, CI, package managers). Do a dry run on a low-traffic repo first, or sequence org rename → verify → repo rename.
- **One-hop redirect limit.** If `solventflow/solventflow` ever gets renamed again later, the `solventlabs/solvent` redirect breaks entirely. Treat this as your final name.
- **If this is a Go module** (import path = repo path), renaming isn't cosmetic for consumers — `go get` and the module proxy tie versions to the old path. New releases under the new path are a breaking change requiring a major version bump under Go's semantic import versioning, not a silent swap. Same logic if it's published to npm/PyPI/crates under a name tied to the old repo.
- **Old org name becomes squattable.** Once you move off `solventlabs`, that namespace is up for grabs. This is a known supply-chain attack (repo-jacking): someone reclaims the old org, and any stale links, build scripts, or `raw.githubusercontent.com` references pointing at the old path can be hijacked. Either keep `solventlabs` claimed-but-dormant, or make the migration announcement loud and fast enough that nothing keeps pointing there.
- **`raw.githubusercontent.com` links don't redirect as reliably as repo pages.** Anything pulling a badge, script, or config directly from a raw file URL (common in docs, CI templates, other people's READMEs) will 404, not redirect.
- **Two years of backlinks/SEO/Stack Overflow answers/awesome-list entries point at the old name.** GitHub's own redirect covers most of it, but awesome-list PRs, blog posts, and tutorials referencing `solventlabs/solvent` won't self-update — expect a long tail of stale links.
- **Verify the new name is actually clear** before it's public: package registries, trademark, domain, social handles — squatting risk goes up the moment the rename leaks pre-launch.

## The real risk is doing both in the same quarter

Bundling a trust-eroding packaging change with a rebrand invites the community to fuse them into one narrative: "they renamed everything and started charging for stuff that used to be free." Either could be managed individually; together they read as a company in flux, and that's when fork threats and HN pile-ons happen.

**Recommendation:** separate the announcements by a few weeks, lead with whichever one is unambiguously positive (the rebrand), and give the audit-log/SSO change its own dedicated, transparent post with a real notice window — not a line item buried in rebrand-week changelog noise. Burying it there, if noticed, reads as intentional concealment, which costs more trust than the paywall change itself.