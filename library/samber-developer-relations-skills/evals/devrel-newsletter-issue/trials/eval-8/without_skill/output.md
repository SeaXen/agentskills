# Fix for next week's issue: Gmail is clipping your email, and a spam filter isn't involved

I haven't seen the HTML, so this is a diagnosis from the symptoms. The test below will confirm or rule it out.

## Likely cause

Gmail clips any message whose HTML source is larger than about 102 KB. It cuts the HTML at that point and shows "[Message clipped] View entire message." Everything past the cut disappears, including the footer and unsubscribe link, so the missing content is always the bottom of the email. That matches what your readers report.

A spam filter doesn't behave this way. It blocks or junks the whole message, or rewrites links. It doesn't remove the last 3 sections at a byte offset. Readers who see everything are probably on clients without this limit, or they opened the web version.

Your build is a good way to produce this. Prism wraps every token in its own `<span class="token ...">`, so a 14-sample issue has thousands of spans. Juice then copies the matching CSS declarations onto every one of them as an inline `style="..."`. A full Prism theme puts several properties on each token, so each span carries a lot of repeated text. Your ESP also adds weight after you upload: it rewrites links for tracking and adds an open pixel. The size Gmail sees is larger than the size you upload.

## Confirm it first (5 minutes)

1. Check the size of the HTML you sent. If you only have the pre-upload file, send a test through the ESP to a Gmail address and look for the clipped banner.
2. Ask two or three affected readers whether they're on Gmail. If they are, and the sent HTML is over about 100 KB, that is the cause.
3. If the HTML is well under 100 KB, drop this theory. The next suspects would be malformed HTML, such as an unclosed tag or unescaped `<` in a code sample, or the ESP stripping content.

## Changes for next week

Do these in order. The first two matter most.

1. **Cut the code highlighting weight.**
   - Replace the stock Prism theme with a minimal one that sets only `color`, plus `font-weight` for keywords. Use 4–5 colors in total.
   - Put the `pre` and `code` block styling (font, background, padding, `white-space`) on the wrapper only, not on the token spans.
   - Merge adjacent spans that have the same class after highlighting.
   - Or skip highlighting in the email and keep it on the web version. 14 samples is a lot for an inbox, so consider keeping 3–5 inline and linking to the web issue for the rest.

2. **Move the unsubscribe link to the top.** Put "View in browser · Unsubscribe" in the header or preheader, and keep the footer link as well. A clipped footer should never again remove the unsubscribe path. Also confirm your ESP sends the `List-Unsubscribe` header, which gives Gmail its native unsubscribe button.

3. **Minify the HTML before upload.** Use `html-minifier-terser` with whitespace collapsing, but leave `pre` and `code` alone so code formatting survives. Strip comments. In juice, drop the `<style>` blocks once inlined. Keep a `<style>` only for media queries.

4. **Add a size check to the build script.**
   - Fail the build if the final HTML exceeds about 80 KB, measured in bytes (`Buffer.byteLength`), not characters. This leaves headroom for the ESP's link rewriting and tracking pixel.
   - Print the size contributed by each code sample, so you see which one blows the budget.

5. **Test before sending.** Send the final issue to a Gmail account and confirm there is no clipped banner and that the footer is visible. Do this every week.

## For the issue already sent

Publish the web version and send a short follow-up, or add a line to next week's issue. Gmail readers can't unsubscribe from a clipped message, so a missing link is also a compliance risk (CAN-SPAM and GDPR). That's one more reason to fix the unsubscribe link first.