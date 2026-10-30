# Email rendering: code, size, dark mode, plain text

Read this before writing any code block or HTML for an issue. Client support shifts as vendors replace rendering engines, so re-check the support tables at caniemail.com when a rule here looks wrong in a test send.

## Contents

1. Client facts
2. Safe code block pattern
3. Dark mode
4. Size and clipping
5. Preview text padding
6. Plain-text part
7. Accessibility floor

## 1. Client facts

| Concern | Fact | Consequence for the issue |
|---|---|---|
| `<pre>` | About 88% support on caniemail; partial in Outlook for Windows 2013-2019 | Safe to use, styled inline |
| `<code>` | About 89%; some clients strip the tag and keep its text | Never let inline code carry meaning by styling alone |
| Web fonts | When a web font leads the font stack, Outlook for Windows may skip the whole stack and render Times New Roman; Gmail does not load web fonts | Lead with a system monospace font |
| `<style>` blocks | Gmail supports them for Gmail accounts, drops them in its apps for non-Gmail accounts, and discards the whole block on a CSS parse error or past its size limit | Inline every property a code block needs |
| `padding` | Classic Outlook for Windows (Word engine) applies padding only on table cells | Put padding, background and border on a `<td>` around the `<pre>` |
| Classic Outlook for Windows | Word engine: ignores flex, grid, border-radius and max-width; may insert page breaks in long emails. The newer Outlook and Outlook.com use a browser engine | Test classic Outlook separately; expect square corners |
| `white-space` | About 93% support on caniemail; partial in Gmail (non-Google accounts), and the `pre` value is unsupported in Gmail, Outlook.com and Yahoo | Wrapping differs per client: short lines are the only reliable fix |
| Images | Blocked by default in some clients until the reader allows them | No information only in an image |

## 2. Safe code block pattern

```html
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="margin:0 0 16px 0;">
  <tr>
    <td style="padding:12px 14px;background-color:#f4f4f5;border:1px solid #d4d4d8;">
      <pre style="margin:0;color:#1f2328;font-family:Consolas,Menlo,Monaco,'Courier New',monospace;font-size:13px;line-height:1.45;white-space:pre-wrap;word-break:break-word;">npm install @example/sdk@4.2.0</pre>
    </td>
  </tr>
</table>
```

- Live text, every property inline, no web font, no syntax highlighting.
- Lines of about 40 characters or fewer. At 13px a monospace character is roughly 7-8px wide, and a phone leaves about 300px for the block after margins and padding.
- For a longer file, show up to 5 lines in this block and link the full file with descriptive link text ("full `config.yaml` on GitHub").
- In a markdown editor, a fenced block usually produces a bare `<pre>`. If the tool accepts raw HTML, paste this pattern; otherwise check the fenced block in the test send.

## 3. Dark mode

- Clients behave three ways:
  - no change;
  - partial inversion: light backgrounds darkened, dark text lightened;
  - full inversion of every colour.
- Which one a reader gets depends on the client, not on the exact colour values. Apple Mail auto-darkens only emails that declare no colours; an email that opts in through `color-scheme` gets its own dark rules applied instead.
- Set the background and text colour of every block inline, as a pair. Clients that transform colours then transform both together, and the contrast survives.
- Opt in where clients honour it: `<meta name="color-scheme" content="light dark">` with `@media (prefers-color-scheme: dark)` rules, plus the attribute selectors some Outlook apps use. Treat these as enhancements; the inline pair is the floor.
- Syntax highlighting themes break here: colours tuned for one background become low-contrast on the other. Highlighted blocks need a test send viewed in both modes.
- Logos and diagrams on transparent backgrounds can vanish on dark backgrounds. Give them a solid background or an outline.

## 4. Size and clipping

- Gmail clips a message whose HTML exceeds 102KB and shows a "[Message clipped] View entire message" link. Images do not count; markup does.
- Readers who do not click see nothing after the cut: usually the footer, its unsubscribe and error-report links, and the open-tracking pixel. Some report spam instead of hunting for the unsubscribe link.
- Per-token syntax highlighting wraps every token in its own `<span>` with inline colour, which multiplies a block's size several times. CSS inlining repeats styles on every element and adds weight to every item.
- Measure the HTML the sending tool exports, not the editor view. Aim under about 90KB to leave margin for tracking rewrites.
- Mobile clients are reported to clip earlier, with unconfirmed figures. Keep issues short rather than relying on any one number.

## 5. Preview text padding

- Hidden preview text placed first in the body sets what the inbox shows. Wide previews (desktop Apple Mail, Gmail on a wide window) keep reading into the body after it.
- Pad after the hidden preview with a run of `&zwnj;&nbsp;` pairs so the next visible line does not leak into the preview.
- Sending tools with a preview-text field usually add this padding themselves. Check the inbox view in the test send.

## 6. Plain-text part

- A multipart email carries a plain-text version next to the HTML. Some tools generate it blank, or full of image placeholders and raw tracking URLs.
- The plain-text part is only visible through a real send from the sending tool, not an HTML preview.
- Write or fix it: headline line, full URL line, code indented four spaces, sponsor label in words, footer links spelled out.

## 7. Accessibility floor

- `lang` set on the `<html>` element.
- One top heading naming the issue, section headings in order, never bold text faking a heading.
- Body text of at least 14px, with 16px preferred on mobile.
- Alt text on every meaningful image; empty `alt=""` on decorative ones; a linked image's alt says where the link goes.
- Link text describes the destination; links underlined, since colour alone fails colour-blind readers.
- Body text contrast of at least 4.5:1, checked again in dark mode.
- Layout tables marked `role="presentation"`.
- A short text label before a long code block ("Example request:") so a screen-reader user knows code follows.
