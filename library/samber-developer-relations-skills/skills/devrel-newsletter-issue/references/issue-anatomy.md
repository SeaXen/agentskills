# Issue anatomy: default order and specs

Read this when the programme has no section template, or when sizing an item, a sponsor block, a subject or a preview line. Figures come from published issues and media kits of long-running developer newsletters. Treat them as examples to calibrate against, never as targets.

## Contents

1. Default section order
2. Item specs, with real shapes
3. Sponsor block specs
4. Subject and preview text
5. Links per issue

## 1. Default section order

Use this only when no charter or previous issue fixes the order.

| Section | Holds | Items | When empty |
|---|---|---|---|
| Lead | the one item most readers need this cycle | 1 | promote the strongest item from another section |
| Shipped | your own releases: breaking changes and security fixes first, then capabilities | 1-5 | drop the section |
| From the ecosystem | external posts, releases, talks worth reading | 2-6 | drop the section |
| From the community | community-built projects, answers, calls for participation | 1-3 | drop the section |
| In brief | one-line bullets for everything else that qualified | 0-10 | drop the section |
| Events | dated, with location or "online" | 0-3 | drop the section |
| Footer | submit an item, report an error, archive, unsubscribe, sender address | - | never empty |

Put the sponsor slot after the lead item, or wherever the charter fixes it.

## 2. Item specs, with real shapes

- **Full item:** linked headline, 1-3 sentences of roughly 20-45 words, author and organisation line, optional one-line aside. One counted issue of a large JavaScript digest ran 20-41 words per item.
- **Hedged claim:** "Benchmarks claim up to 8x" rather than "8x faster". The editor attributes, never endorses, a number they did not measure.
- **One-sentence item:** can be pure "why it matters", for example why the author's track record makes the piece worth reading.
- **Headline-only item:** the Rust community's weekly digest groups bare linked titles by category. This suits a high-volume issue whose readers scan, and it is the drafting form for a link the editor could not read; that item stays blocked until a person reads it.
- **Review item:** a "We like / We don't like" pair, written as if the editor evaluated the tool for their own use.
- **Vendor release item:** a bold verb-led headline plus one sentence of 12-25 words ("Checkout cancel URL is now optional: the cancel_url parameter is no longer required."), or about 35 words stating capability then availability ("This capability is generally available.").
- **Fixed sections that recur well:** project of the week with nomination credit, calls for testing, calls for participation, a merged-PR count, jobs, quote of the week.

## 3. Sponsor block specs

| Publisher pattern | Slots per issue | Format limits | Label |
|---|---|---|---|
| Large weekly digest family | 1 primary slot, plus sponsored links and classifieds | primary headline up to 60 characters, summary 100-250 characters, small image; sponsored link 70-character headline, 120-character description; classified up to 140 characters, one link | "Together with" masthead, "sponsor" on each placement |
| Daily tech digest | 3: top, middle, quick links | same headline-plus-summary shape as editorial | labelled; critics say identical format blurs the line |
| Tool-review newsletter | 1 text ad | up to 100 characters | "clearly marked"; no sponsored reviews |

- Copy arrives days before send so the editor can review format and tone. Set a copy deadline in the charter.
- A sponsor gets one link. Its tracking parameters are the sponsor's; editorial links carry no added UTM parameters beyond the sending tool's click tracking.

## 4. Subject and preview text

- Subjects in one large digest name the lead story in 33-43 characters, with a concrete hook: a version, a stated multiplier, a named project.
- Preview text: put it first in the body, hidden if the design needs it, at least 90 characters. Otherwise clients fill the preview with alt text, "View in browser" or the first body line.
- Preview widths shown by clients vary with window size and font, and no mail-client vendor publishes them. Approximate vendor-blog measurements: about 35 characters in Outlook for Windows, 55 in Outlook for iOS, 81 in Apple Mail on iPhone portrait, around 90 or more in Gmail, up to 140 on desktop Apple Mail. Hence news in the first 35 characters, length past 90.
- Some inboxes now replace the preview with a generated summary of the message. The first body paragraph has to carry the news as well.
- A "Plus..." deck naming two or three secondary items doubles as preview text for a digest.

## 5. Links per issue

- A large weekly digest counted about 69 content links plus about 6 navigation links in one issue. Release roundups carry several links per line.
- Most programmes measure clicks, so the sending tool rewrites every link through a tracking redirect. Readers who hover then see the tracker, not the destination, and the plain-text part shows the full tracking URL.
- Make the tracking domain a branded subdomain of the newsletter's own domain, over HTTPS, with one redirect. Never use a public URL shortener.
- Leave links untracked only when the charter says so. Some curated digests do this on purpose and measure nothing per link.
