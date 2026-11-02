**Do this first (5 min):** export the HTML your ESP actually sends for last week's issue and run `wc -c` on it. If it is over about 102,000 bytes, you have your cause.

## Diagnosis

The cause is almost certainly Gmail clipping, not a spam filter. I haven't seen your HTML, so the size check above confirms it.

- Gmail cuts any message whose HTML is over 102KB. It shows "[Message clipped] View entire message".
- The cut removes the end of the message: the last 3 sections, the footer and the unsubscribe link. That matches your reports.
- A spam filter does not cut a message at a size boundary. It rejects the message or moves it to spam.
- Readers who click "View entire message", and readers on clients that don't clip, see everything. That is your "others see everything" group.
- Prism puts every token in its own `<span>`. 14 samples means thousands of spans.
- juice then copies the inline style onto every one of those spans, so the markup grows several times over.
- Images don't count toward the 102KB. Markup does.
- Some clipped readers report spam instead of hunting for the unsubscribe link. That hurts your sender reputation, so fix this before next week.

## What to change for next week

1. **Remove Prism from the build for email.** Keep it for the web archive if you want it there.
   - Highlighted blocks are the lowest-ranked option for email: they add HTML weight and the colours invert in dark mode.
2. **Cut 14 samples to what the issue needs.** Use the highest row that fits each snippet:
   - A command, flag or identifier under one line: inline code in the sentence.
   - Up to about 10 lines: a short plain block.
   - Anything longer: an excerpt of 5 lines or fewer, plus a link to the full file, gist or playground. The full file must be hosted before send.
   - Python, JSON and YAML can't be re-wrapped. Use excerpt plus link for those, never reflowed code.
   - Don't write security-sensitive snippets (auth, signature checks, crypto) yourself. Use your tested code verbatim, or link to the docs page.
3. **Use this block for every plain sample.**
   - Live text, no `<span>`s.
   - Every property inline.
   - Padding on a `<td>` around the `<pre>`, because classic Outlook only applies padding on table cells.
   - Lines of about 40 characters or fewer.
   - No web font.

   ```html
   <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="margin:0 0 16px 0;">
     <tr>
       <td style="padding:12px 14px;background-color:#f4f4f5;border:1px solid #d4d4d8;">
         <pre style="margin:0;color:#1f2328;font-family:Consolas,Menlo,Monaco,'Courier New',monospace;font-size:13px;line-height:1.45;white-space:pre-wrap;word-break:break-word;">npm install @example/sdk@4.2.0</pre>
       </td>
     </tr>
   </table>
   ```

   - Wrap shell commands with `\`. Never wrap mid-token.
   - Label each sample as runnable or as an excerpt.
4. **Add a size gate to the build.** Fail the build if the juice output is over 90,000 bytes. That leaves margin for your ESP's click-tracking rewrites.
   - Measure the HTML your ESP exports, not your local file.
   - If you're still over, trim the longest items first. Shorter issues beat relying on any one clip number, because mobile clients may clip earlier.
5. **Keep juice, but restrict it.** After step 3 the only inlined markup is your layout plus the block pattern above, so it stays small.
   - Skip the blanket inlining of a `<style>` sheet over every element.
   - Don't rely on `<style>` for the code blocks. Gmail drops it for some accounts, and drops all of it on one CSS error.
6. **Check dark mode.** Each block sets background and text colour as an inline pair, so clients that invert colours transform both together.
7. **Do a test send before the real send.**
   - Send it from the ESP to a Gmail account.
   - Confirm there is no "Message clipped" link and the footer and unsubscribe link are visible.
   - Check light and dark mode in Gmail, Apple Mail on a phone, and classic Outlook for Windows (or a rendering-preview screenshot of it).
   - Check the plain-text part. Sample indentation: code at four spaces, full URLs.

## Open items for you

- ⚠️ **Blocked on you:** I haven't measured the byte size of last week's HTML. Run the `wc -c` check above.
- ⚠️ **Blocked on you:** I haven't checked whether any of the 14 samples is security-sensitive code. Use your tested code verbatim, or link to the docs.
- ℹ️ **Ask the deliverability person when back.** Have them review the unsubscribe headers and authentication. Clipping doesn't touch these, but a missing in-body unsubscribe link raises complaint rates. Those belong to the deliverability skill (`devrel-newsletter-deliverability`), not this issue.
- ℹ️ **Last week's issue.** Fix the web archive page so it shows everything. A resend of the whole issue is not needed. If the clipped footer hid a correction or a dated call to action, send a short correction email.

## Pre-send report for next week's issue

| Check | Status |
|---|---|
| Code blocks: live text, inline-styled, lines ≤ ~40 chars | Pass once step 3 is applied |
| HTML under ~90KB | Blocked until you export and measure |
| Test send in Gmail, Apple Mail, classic Outlook | Blocked until you send one |
| Plain-text part readable, full URLs | Blocked until you send one |

**Next:** run `wc -c` on last week's exported HTML and paste the number here.