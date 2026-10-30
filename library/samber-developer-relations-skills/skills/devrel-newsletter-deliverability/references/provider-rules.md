# Provider rules and corporate gateways

Read this when checking compliance, reading a rejection code, or explaining a corporate Junk placement. Providers update these pages; re-check the linked page before a large send or a migration.

## Contents

1. Mailbox-provider rules
2. Rejection codes
3. Monitoring sources
4. Corporate gateways

## 1. Mailbox-provider rules

| Rule | Gmail | Yahoo | Outlook.com consumer |
|---|---|---|---|
| Who is "bulk" | Close to 5,000+ messages a day to personal Gmail accounts, counted across the primary domain and its subdomains; permanent once reached | "Significant volume", no number | Domains sending 5,000+ a day to outlook.com, hotmail.com, live.com |
| Every sender | SPF or DKIM, valid forward and reverse DNS, TLS, RFC 5322, spam rate below 0.3% | SPF or DKIM, valid reverse DNS, RFC 5321/5322, spam rate below 0.3% | - |
| Bulk authentication | SPF and DKIM, DMARC at least `p=none`, `From:` aligned with SPF or DKIM | SPF and DKIM, DMARC at least `p=none` that passes | SPF pass, DKIM pass, DMARC at least `p=none` aligned |
| One-click unsubscribe | Required for marketing and subscribed mail, plus a visible body link; honour within 48 hours | Required for marketing and subscribed mail; honour within 2 days | Recommended |
| Spam rate | Keep below 0.1%, never reach 0.3%; calculated and updated daily | Below 0.3%; evaluated continuously, no published formula | Not published |
| When you fail | Since November 2025: temporary and permanent rejections or spam folder; no mitigation help above 0.3% until 7 consecutive days below it | Bounce or spam folder | `550 5.7.515` rejection since May 2025 |
| Out of scope | Google Workspace recipients | - | Microsoft 365 business tenants |

- A newsletter on `news.example.com` adds to product, transactional and employee mail on `example.com` for Gmail's count.
- A "new domain" at Gmail (never above 5,000 a day since 1 January 2024) faces an accelerated enforcement timetable.
- Gmail mitigation (the only escalation path) is open only to bulk senders meeting every rule, including one-click and the 48-hour unsubscribe. Google accepts no allow-list requests from sending platforms.
- Gmail's guidelines also ask senders to confirm each address before subscribing it, to send subscription mail from a different address than other mail, and to increase volume gradually.

## 2. Rejection codes

4xx = temporary, retry later. 5xx = permanent, do not retry. The text after the code says whether the address or the sender is the problem.

| Code | Provider | Meaning | Action |
|---|---|---|---|
| `5.1.1` | any | Mailbox does not exist | Suppress the address |
| `4.7.23` / `5.7.25` | Gmail | Reverse DNS (PTR) missing or mismatched | Platform issue; raise a ticket |
| `4.7.27` / `5.7.27` | Gmail | SPF fails | Fix the return-path records |
| `4.7.30` / `5.7.30` | Gmail | DKIM fails | Fix DKIM records or signing |
| `4.7.31` (sender-rules FAQ), `4.7.40` / `5.7.40` (SMTP error page) | Gmail | DMARC record missing or has no policy | Publish `p=none` with `rua` |
| `4.7.26` / `5.7.26` | Gmail | Unauthenticated (neither SPF nor DKIM passes), SPF `-all` failure, or rejected by the domain's DMARC policy | Fix authentication; keep the address |
| `4.7.32` | Gmail | `From:` not aligned | Custom DKIM on your domain |
| `4.7.29` / `5.7.29` | Gmail | No TLS | Platform issue |
| `4.7.28` | Gmail | Unusual rate of (unsolicited) email from your IP, domain or link domain; temporarily rate limited | Google: wait at least 10 minutes, resume on one connection. Then open triage steps 4 and 5: the trigger is reputation as much as speed |
| `5.7.28` | Gmail | Blocked for an unusual rate of unsolicited email | Stop the stream; complaints and list events first |
| `4.2.1` | Gmail | That one recipient is receiving mail too fast | Retry later; not a sender problem |
| `550 5.7.1` | Gmail | Meaning depends on the text: low IP reputation, low domain reputation, "likely unsolicited", or a header fault (missing or duplicate `From:`, missing `Message-ID`) | IP reputation: platform ticket. Domain reputation or unsolicited: triage step 4. Header fault: template fix. Never act on the code alone |
| `550 5.7.515` | Outlook.com | Domain does not meet the authentication level | SPF, DKIM, DMARC on the sending domain |
| `554 5.7.9` | Yahoo | Rejected for policy reasons | Read the text; often DMARC |
| `421 4.7.0 [TSS04]` | Yahoo | Deferred for unexpected volume or user complaints (commonly seen text) | Read complaint-loop data, slow the ramp |
| `550 5.7.1 ... (S3150)` and similar S-codes | Outlook.com | Sending network on Microsoft's block list (commonly seen text) | Platform ticket; after fixing the cause, the Microsoft sender support request |

Never suppress an address on a sender-side code: the reader is real, and the next send after the fix reaches them.

## 3. Monitoring sources

For blocklist lookups, use Spamhaus's own lookup page: Spamhaus refuses DNS queries relayed through large public resolvers and answers with error codes that naive checks misread as listed or clean.


| Source | What it shows | Limits |
|---|---|---|
| Gmail Postmaster Tools (v2 Compliance status) | Spam rate, authentication, compliance with the bulk rules | Aggregate only; no per-complaint data; updated daily |
| Gmail feedback loop by `Feedback-ID` header | Spam rate per identifier the sender sets (campaign, segment, stream) | Only where you can set the header fields and the mail is signed with your own DKIM domain verified in Postmaster Tools; flags only identifiers with an unusual spam rate, above a daily volume minimum, so small lists often see no data |
| Yahoo Complaint Feedback Loop | Per-complaint reports, keyed to the DKIM domain | Needs DKIM; platform usually wires it in |
| Microsoft SNDS and JMRP | IP data and per-complaint reports | IP-keyed; on a shared pool the platform holds it |
| DMARC aggregate reports | Every source sending as the domain, pass or fail | Volume and alignment, not placement |
| Platform bounce log | Raw SMTP replies per recipient | Some platforms show only hard/soft buckets; ask for raw text |
| Seed or placement tests | A directional snapshot | Seed inboxes have no engagement history; never proof of placement for real readers |

Platform complaint rates under-count Gmail, which sends no per-message reports. Read Postmaster Tools for Gmail.

## 4. Corporate gateways

Developer newsletters reach many readers at work, behind filters the sender cannot see:

- **Microsoft Defender for Office 365** gives each message a Bulk Complaint Level from 0 (not bulk) to 9. The default policy threshold, 7, moves bulk mail to Junk. The Standard preset uses 6 (Junk); the Strict preset uses 5 and quarantines. Admins can also set their own threshold and action. Microsoft's own false-positive guide lists legitimate newsletters at BCL 7-9 and tells admins to verify SPF, DKIM and DMARC before allowing the domain.
- **Safe Links** rewrites URLs and can scan them before delivery. Scanning clicks every link, so click tracking records clicks nobody made.
- **Mimecast, Proofpoint, Barracuda** also rewrite links, check them at click time and hold suspected bulk mail in quarantine digests.
- **Google Workspace** recipients sit outside Gmail's sender rules; their admins' policies decide.

What a sender can do:

1. Keep one branded HTTPS tracking domain that resolves to your own site, or send without tracking.
2. Filter scanner clicks before using clicks for anything: clicks within seconds of delivery, from cloud IP ranges, or on every link of one copy.
3. Keep unsubscribe POST-only (see the authentication reference).
4. Publish a short allow-listing note for readers' IT teams: the sending domain and DKIM `d=` (more durable than shared IPs), and the Microsoft 365 options to allow the domain or adjust the bulk threshold.
5. Offer a feed or archive link for readers whose company junks bulk mail regardless.
