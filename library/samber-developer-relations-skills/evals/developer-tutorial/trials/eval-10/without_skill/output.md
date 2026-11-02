# Changes to the Grellan deploy tutorial

## 1. Re-run the pilot without the shortcut

The 95-minute number is not real. It skipped the actual bottleneck: VPN request, SSO group approval, ticket-based namespace provisioning. Re-run the pilot with a genuine new-hire path, ticket to ticket, and record that number separately. Expect it to dwarf the 95 minutes — that's the number that matters for "first week" planning, not the hands-on part.

## 2. Pull provisioning out of the tutorial entirely

VPN, SSO group, namespace ticket are not tutorial steps — they're prerequisites with human/ticket latency. Keep them in the doc.

- Trigger the namespace ticket automatically at offer-acceptance or on the manager's Day-0 checklist, not left for the hire to discover mid-tutorial.
- Put an SLA on it (e.g., namespace ready within 1 business day) so it's done before the hire ever opens the doc.
- Tutorial's prerequisites section states expected wait time and links the checklist. It doesn't try to walk the hire through requesting access interactively — that's a different document, owned by whoever provisions it.

## 3. Add a preflight check as the real step 1

One command that checks VPN connectivity, SSO group membership, namespace existence, registry reachability, before any deploy step runs. On failure it names the specific missing piece and the fix (ticket status link, IT contact) — not a cryptic timeout at step 7.

## 4. Escalate the registry-unreachable problem as infra, not doc

Half the commands failing off-office-network is a platform bug, not something a rewrite fixes. File it with the network/platform team: registry should be reachable over the VPN that's already a listed requirement, not gated to physical presence.

Until fixed:
- Document the constraint explicitly, with the exact symptom (timeout on `docker pull`/`grellan push`, whichever it is).
- Workaround: a bastion/jump host inside the office network, reachable over VPN, that remote or hybrid hires can use for the registry-touching steps.
- Or: schedule the hands-on half of the tutorial for an in-office day during week one for hires who aren't office-based by default.

Don't ship a "must complete in week one" gate that quietly fails for anyone not physically in the building.

## 5. Cut the 95 minutes and the 11 steps

- Wrap repeated boilerplate CLI incantations into one bootstrap script (**`grellan onboarding bootstrap`**, or whatever's idiomatic here) — still prints each underlying command, doesn't hide what's happening.
- Add a checkpoint every 3–4 steps ("service responds at `https://...`, expect `200`"), not just at the end. Failures should surface at minute 20, not minute 90.
- Publish two numbers, not one blended figure: provisioning wait (async, ~1 business day) and hands-on time (~45–60 min, after trimming).

## 6. Replace self-reported completion with a real signal

Grellan already knows who deployed what, when, into which namespace — that's the source of truth, not the hire's word to their manager.

- Last successful deploy in the tutorial auto-posts to an onboarding Slack channel or stamps the HR/onboarding tracker with hire, manager, timestamp, deployed service URL.
- Manager checks a channel or dashboard, doesn't take it on faith or chase a screenshot.

## 7. Add troubleshooting for the failure modes the shortcut account hid

Each with the literal error text the hire will see, not "contact IT":
- VPN connected, SSO group not yet synced (propagation delay after ticket approval).
- Namespace ticket approved but provisioning not yet complete.
- Registry timeout while off-VPN or off-office network.

These four are what a real first-week hire hits and the pre-provisioned test run never could.