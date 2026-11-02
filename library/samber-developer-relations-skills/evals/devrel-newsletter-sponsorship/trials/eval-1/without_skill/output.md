# Pulse Weekly sponsor block for the Quillstack issue

I changed Quillstack's wording in three places, and each change is to the wording that would have hidden the payment from readers.

## Changes to Quillstack's wording

| Their ask | What I used | Why |
|---|---|---|
| Header "Presented by Quillstack" | "Sponsored by Quillstack", with a "Sponsored / Anzeige" tag | "Presented by" can read as Quillstack co-producing or editing the issue. "Sponsored" is the standard word and is understood in the US, UK and Germany. The German tag covers your ~40% German readers, since German advertising law expects "Anzeige" or "Werbung". |
| "Thanks to our friends at Quillstack for supporting the community" | "Thanks to Quillstack for sponsoring this issue and supporting the community." | "Friends" hides a paid relationship. The US FTC, the UK ASA and the German UWG all expect a clear disclosure of a paid placement. The thanks still reads warmly. |
| Subject: "Quillstack x Pulse Weekly" | "Pulse Weekly #[N]: [topic] (sponsored by Quillstack)" | "x" signals a collaboration, not an ad. A subject line that hides sponsorship is the riskiest place to do it, under CAN-SPAM, the UK CAP Code and German law. |

If Quillstack pushes back on the subject, offer them "Quillstack x Pulse Weekly" only with "Sponsored:" in front. Don't send it bare.

I'm not a lawyer. With 40% of readers in Germany, it's worth a quick check with one, because German advertising law is the strictest of the three.

## Final sponsor block (HTML email)

```
[small grey tag, above the logo]
SPONSORED · ANZEIGE

[Quillstack logo, linked to https://[quillstack-url]?utm_source=pulse-weekly&utm_medium=newsletter&utm_campaign=[issue]
 alt text: "Quillstack logo"]

Sponsored by Quillstack

[Quillstack's 2–3 sentence pitch and CTA button, as supplied by them]

Thanks to Quillstack for sponsoring this issue and supporting the community.
Sponsors pay for placement. They do not review or influence Pulse Weekly's editorial content.
```

Confirm the last sentence is true for Quillstack before you publish it. If they got a preview or any say in editorial content, cut it.

## Where each piece goes

| Piece | Email (HTML) | Plain-text version | Web archive |
|---|---|---|---|
| Subject line | Yes, with "(sponsored by Quillstack)" | Same subject | Page `<title>` and H1 carry the same issue title, including "(sponsored by Quillstack)" |
| "SPONSORED · ANZEIGE" tag | Above the logo, in the same block | First line of the block, plain text | Same, above the logo |
| Logo | Image with alt text, linked | Not possible. Write `Quillstack` and put the link on its own line | Image with alt text, linked |
| "Sponsored by Quillstack" | Directly under the logo | Next line | Same |
| Pitch and CTA | Button | Plain sentence plus full URL on its own line | Button |
| Thanks and independence lines | Under the pitch | Same, plain text | Same |
| Position | Top of the issue, before editorial content | Top, set off with `-----` rules | Top of the page |
| Links | Tracked URL | Same URL, written out in full | Add `rel="sponsored"` to every Quillstack link, so search engines treat them as paid |

**Plain-text version:**

```
-----------------------------------------
SPONSORED · ANZEIGE
Sponsored by Quillstack
[pitch text]
-> https://[quillstack-url]?utm_source=pulse-weekly&utm_medium=newsletter&utm_campaign=[issue]

Thanks to Quillstack for sponsoring this issue and supporting the community.
Sponsors pay for placement. They do not review or influence Pulse Weekly's editorial content.
-----------------------------------------
```

## Before you send

1. Check that the tag and the "Sponsored by" line show with images blocked. Many German corporate mail clients block images, so the disclosure has to be text, not part of the logo.
2. Keep the archive's wording identical to the email's. Don't strip the tag later.
3. Keep Quillstack's sponsorship terms in writing, including that the disclosure wording is yours to set.