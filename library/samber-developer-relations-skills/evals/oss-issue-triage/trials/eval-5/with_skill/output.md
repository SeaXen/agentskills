## 0. Do this in the next 5 minutes — before anything else

You have a live emergency, not a triage backlog problem: a working auth-bypass PoC has been sitting on a **public** tracker for ~40 minutes. Per this skill's security path (`issue-intake-and-routing.md`): *"A vulnerability reported publicly by mistake is an emergency: route it to the private channel immediately rather than triaging in the open."* A `security` label does nothing for this — the issue is exploitable by anyone reading it right now, label or not. In order:

1. **Enable GitHub Private Vulnerability Reporting** on otterlink if it isn't already (Settings → Security → "Private vulnerability reporting"). This gives you a private draft security advisory + private fork with zero setup cost — it's the correct default when, as you said, there's no security list.
2. **Minimize the public issue immediately**: edit the issue body to strip the PoC and technical detail (GitHub keeps edit history, so also ask GitHub Support to purge it if this repo is public and search-indexed), lock the conversation, and post one line: *"Thanks — moving this to a private security report, we'll follow up there."* Then open a private security advisory and continue the conversation with the reporter there.
3. **Do not "handle it fast" by publicly acknowledging severity or fix status** in the open issue — that itself is disclosure.
4. Once it's moved, apply a `security` label to the *private* advisory/issue for your own tracking (see §3) — this is the first legitimate use of the label you asked for.

I'm not running any of this against the repo myself — it's a visible, hard-to-reverse action on a live security matter and you should confirm the account/permissions first. Say the word and I'll run the `gh` commands.

---

## Going forward: the security path, the label, and the template

A label + template alone doesn't satisfy "spotted and handled fast" — a label is bookkeeping *after* a report is already off the public tracker. Every mature project runs the same three-piece pipeline behind the label (`issue-intake-and-routing.md`):

1. **A private intake channel** — never the public tracker. Default: GitHub's private vulnerability reporting (already covered in §0).
2. **A named, size-capped response team**, separate from general triage. Kubernetes caps this at ten, acknowledges within three business days. For otterlink, name at minimum yourself + one backup now — an unowned inbox is not a pipeline, and today's incident shows a single point of failure isn't hypothetical.
3. **An embargo mechanism** — a plain statement that you'll coordinate a disclosure date with the reporter before going public, so a fix doesn't ship with a changelog line that's itself the advisory.

### 1. The public-facing entry: a redirect, not a form

Apache's own instruction to committers is to never put vulnerability details in a public tracker. So the thing a reporter sees in your issue chooser is a **contact link**, not a data-collecting template — otherwise you've just built a nicer public disclosure form.

`.github/ISSUE_TEMPLATE/config.yml`:
```yaml
blank_issues_enabled: false
contact_links:
  - name: 🔐 Report a security vulnerability
    url: https://github.com/<org>/otterlink/security/advisories/new
    about: Do not open a public issue for security reports. Use this private form instead.
```
This is what actually gets these "spotted and handled fast" — it intercepts the reporter *before* they type into a public box, which is the highest-leverage point in the whole system.

### 2. The `security` label

- **Axis**: it doesn't fit type/state/priority/area cleanly — treat it as a cross-cutting flag, applied only by a maintainer, never by automation, never guessed. This is the PyTorch rule for the top-consequence axis: *"Never let automation apply the top priority level. Route every candidate for it to human confirmation instead."* Security is exactly that axis for otterlink.
- **Where it lives**: applied to the private security advisory (for your own audit trail and search later), and — per the closing policy — explicitly **exempted from any staleness sweep** you add later, alongside `confirmed`/`blocked`/`pinned`.
- **One-sentence definition** (put this in the repo, not just the label description): *"Confirmed or suspected security vulnerability; handled via private advisory, never in the public tracker regardless of how it was originally reported."*

### 3. What the private report form should ask for

This is the actual "template" — it lives inside the private advisory, not the public tracker, so it's safe to ask for real technical detail. Every field earns its place by avoiding a round-trip; nothing decorative:

| Field | Required | Why |
|---|---|---|
| Summary (one line) | yes | Triage-at-a-glance |
| Affected component (e.g. "header parsing", "TLS termination") | yes | Routes to the right owner immediately |
| Affected version(s) / commit | yes, dropdown against tags where possible | Free text arrives as "latest" |
| Vulnerability type (dropdown: auth bypass, injection, DoS, info disclosure, RCE, SSRF, other) | yes | Gives you a rough severity band before you read a line of PoC |
| Impact — what an attacker can actually do | yes | "Auth bypass" alone doesn't say if it's read access or full admin |
| Minimal reproduction / PoC | yes | Same rule as any bug report — self-contained, no third-party wrapper |
| Preconditions for exploitation (network position, required auth, specific config flags) | yes | Decides real-world severity, not theoretical |
| **Already disclosed anywhere else (yes/no + where)** | yes | Load-bearing — tells you instantly whether embargo is still possible. This is the field that would have flagged today's incident on submission. |
| Suggested severity / CVSS | optional, marked non-authoritative | Reporter's estimate; your team re-scores |
| Suggested fix or patch | optional | |
| Reporter contact + credit/CVE attribution preference | optional | Needed for coordinated disclosure and advisory publishing |

Keep it to this list. Anything more (e.g. asking for full environment dumps up front) trains reporters to skim it, which is the opposite of what you want from a channel whose entire job is to catch the one report that matters.

---

**Open items I don't have answers to and shouldn't guess**: who's the named backup on the response team, whether otterlink has any existing SECURITY.md to fold this into, and what disclosure-timeline norm you want to publish (e.g. 90-day default before public disclosure regardless of fix status, common in OSS). Tell me and I'll fill those into the SECURITY.md text directly.