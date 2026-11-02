# Recommendation

Don't offer $200, and don't hand this to CERT/CC yet. Reclassify the severity, split the fix, and send the reporter a dated plan.

## Why

1. **A heap overflow in an image decoder is not "just a DoS."** It parses untrusted input, and your bindings are probably behind upload endpoints. "It crashes" means memory is already corrupted. Whether it is exploitable depends on the write primitive and the allocator. Treat it as high or critical until the ASAN trace shows otherwise.
2. **Money for a longer deadline is a bad trade.** It looks like paying for delay or silence. It also sets a precedent and doesn't buy you any hours. Offer credit instead: a CVE, a named acknowledgement in the advisory, and quick answers to their questions.
3. **CERT/CC doesn't fix anything.** It adds a second disclosure clock (45 days by default, which I'm recalling from memory, so verify). The reporter chose a private channel, so ask them before looping anyone in. The people who need to hear about this are the two distros packaging 3.x, since they ship the patch to users.
4. **The 12-hour rewrite is the wrong thing to do before the deadline.** The security fix is a bounds and overflow check on the chunk length. Ship that on all three lines and do the rewrite in a later feature release. That is how you fit the work into your 10 hours.

## Your ~10 hours (my estimates, adjust to your code)

| Task | Hours |
|---|---|
| Minimal check on 5.x, plus regression test from the reporter's PoC | 2 |
| Same on 4.x | 1.5 |
| Same on 3.x (different allocator, so re-verify the overflow path) | 2.5 |
| Fuzz the PNG chunk reader on each line (ASAN, run in background) | 1 attended, more unattended |
| Draft GitHub advisory, request CVE, notify distros | 1.5 |
| Buffer | 1.5 |

That is about 10 hours. A 7-day deadline still leaves no time for release engineering or for distros to ship, so you need a short extension.

## Do these today

1. Ask the reporter for the ASAN trace. You need to know whether it's a read or a write, and whether the length is attacker-controlled.
2. Raise the advisory to High, with CVSS pending the trace.
3. Email the security contacts of the two 3.x distros under embargo. Give them the release date and ask them to confirm their patch lead time. Set the embargo and disclosure date after you have their answer. The `linux-distros` list is the usual route, and I believe it caps embargoes at 14 days, so check its current rules before you post.
4. Use the GitHub advisory's private fork to attach the patches. You can add the reporter and distro maintainers as collaborators.
5. Ask whether the reporter or a distro maintainer will review or write the 3.x patch. You are the only maintainer, so this is the cheapest way to get hours.
6. Find a workaround to publish (for example, rejecting PNGs above a size limit, or a decoder flag) if one exists.

## Message to the reporter (private report thread)

> Hi [name],
>
> Thank you for the report and for the clear reproduction. I've confirmed it on 5.x, 4.x and 3.x.
>
> I don't think this is only a DoS. A heap overflow in the chunk reader may be exploitable, so I'm treating it as High pending your analysis. Could you share the ASAN output, or tell me whether you saw an out-of-bounds read or write and whether you control the length value?
>
> I'm the sole maintainer, and 3.x is shipped by two Linux distributions that need lead time. My plan:
>
> - **By [2026-10-27]:** fix for the overflow merged privately on all three lines, with your PoC as a regression test.
> - **By [2026-11-06]:** patched releases of 5.x, 4.x and 3.x. Distributions are notified under embargo.
> - **By [2026-11-13]:** public advisory with a CVE.
>
> The first fix is a targeted bounds check. The larger rewrite of the chunk-length handling will follow in a later release. This is a 14-day patch timeline against your 7-day deadline, so I'm asking for your agreement to it. If you can't agree to it, tell me what you need. I'd rather give you a firm date I can keep than promise 7 days and miss it.
>
> I'll credit you in the advisory and the CVE (tell me the name or handle you want). I'm happy to add you to the private fork to review the patches. If you can review the 3.x one, that would help a lot.
>
> [name]

## Open questions

- Is it a heap overflow write or a read? That decides the severity and how urgent this is.
- Does the 3.x allocator change what an attacker can do with the overflow?
- If the reporter refuses 14 days, what do you do? I'd ship the minimal fix on 5.x and 4.x at day 7, publish the advisory with the 3.x workaround, and push the 3.x patch to the distros the same day. Tell me if you'd prefer a different fallback.