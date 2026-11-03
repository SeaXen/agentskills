---
name: seadash-retro-crt-theme
description: Concrete pattern for retrofitting the SeaDash single-file operator dashboard (or similar monolithic single-file apps) with a complete retro CRT amber-phosphor theme while preserving all JS bindings and the existing body markup.
---

# SeaDash retro CRT amber-phosphor retrofit

When Dr. Sagar asks for the SeaDash UI on `:9090` to look retro / amber CRT / vintage terminal, the goal is a **full visual swap** of the dashboard's design system without touching the 3100+ lines of body markup and JS.

SeaDash is a single-file operator dashboard at `/mnt/tb/1Apps/SeaDash/index.html` served as static content by a Python `http.server.SimpleHTTPRequestHandler` (port 9090, systemd unit `seadash.service`, working dir `/mnt/tb/1Apps/SeaDash`). The current CSS block lives in lines 10–832 (~22 KB of modern glassmorphism), and the body/JS is the remaining ~3 KB+ of inline scripts and DOM. The retro retrofit is a CSS-only surgery.

## When to use

- User says "make SeaDash retro", "amber CRT", "vintage terminal", "phosphor look", or "old VT220".
- A different single-file dashboard needs the same kind of comprehensive theme refresh.
- You need to replace a giant embedded CSS block atomically while leaving all DOM IDs, classes, and JS handlers intact.

## The non-negotiable rule

**Do not touch the body or the JS.** The dashboard binds event handlers to specific class names (`status-led`, `app-card`, `app-name`, `status-text`, `data-status` attributes, `[class*="card"]`, etc.) and relies on universal selectors like `button`, `h1`, `h2`, `h3`, `input`, `table`, `pre`, `code`. The new CSS must keep the **same selector surface** so every JS binding keeps firing.

This means the new stylesheet is a **superseding layer** with the same selector names, not a new class system. Anything that needs a CRT decoration (e.g. `[ + add app ]` brackets around buttons) is added via `::before` / `::after` `content` on universal selectors.

## Atomic CSS block swap recipe

SeaDash serves the file as static content, so the surgery is on `index.html` only. The cleanest path is a Python script that does both edits in one pass:

```python
import re, pathlib

src = pathlib.Path('/mnt/tb/1Apps/SeaDash/index.html')
html = src.read_text(encoding='utf-8')
new_css = pathlib.Path('/tmp/seadash-retro.css').read_text(encoding='utf-8')

# IMPORTANT: use a callable replacement, not a string template.
# A string template treats backslashes in the new CSS (e.g. inside `content: '\\25A0';`)
# as backreference escapes and raises re.error: bad escape \A.
new_html, n = re.subn(
    r'<style>.*?</style>',
    lambda m: '<style>\n' + new_css + '\n</style>',
    html,
    count=1,
    flags=re.DOTALL
)
assert n == 1, "style block not found"

# Inject CRT boot overlay + typewriter script just before </body>
new_html = new_html.replace('</body>', crt_inject_script + '\n</body>', 1)

src.write_text(new_html, encoding='utf-8')
```

Patches of a 822-line block via the `patch` tool are too fragile — fuzzy matchers and re-escaping inline JS inside CSS are a recipe for repeated failures. Use `re.subn` with `count=1` and `re.DOTALL` for the whole block.

Always back up first:
```bash
cp /mnt/tb/1Apps/SeaDash/index.html /mnt/tb/1Apps/SeaDash/index.html.bak.retro.$(date +%s)
```

## The retro CRT design system (verified)

Amber VT220 / DECWriter is the default, with five alternate phosphor colors mapped to the existing `data-theme` attribute names. Phosphor-color choice replaces the original gradient accent system entirely.

| Original theme attribute | Phosphor mapping | Reference hardware |
|---|---|---|
| `data-theme="dark"` (default) | Amber `#ffb000` glow | DEC VT220 |
| `data-theme="light"` | Green phosphor `#00ff41` | Apple ///, IBM 5151 |
| `data-theme="sunset"` | Dim warm amber `#ff8a3a` | DEC VT220 warm |
| `data-theme="ocean"` | White phosphor `#e8e8ff` | IBM 3270 |
| `data-theme="forest"` | Green-amber `#88ff44` | Hazeltine 1500 |
| `data-theme="midnight"` | Blue phosphor `#5b9cff` | Tandy / Wyse 50 |

The original theme variants (sunset / ocean / forest / midnight) preserved their **theme attribute names** but became different phosphor colors instead of different gradient palettes. The user's existing theme switcher keeps working without code changes.

## Color tokens (paste into `:root`)

```css
:root {
  --bg:        #0a0600;
  --bg2:       #120a00;
  --phos:      #ffb000;     /* primary amber */
  --phos-dim:  #aa6600;
  --phos-bright:#ffd060;
  --phos-glow: rgba(255,176,0,0.55);
  --phos-glow-soft: rgba(255,176,0,0.18);
  --caret:     #ffe6a0;
  --text:      var(--phos);
  --text-dim:  var(--phos-dim);
  --text-bright: var(--phos-bright);
  --border:    rgba(255,176,0,0.30);
  --border-dim:rgba(255,176,0,0.12);
  --radius: 0;             /* terminal boxes are square */
  --shadow: 0 0 0 transparent;
  --transition: 0.15s linear;
  --mono: 'VT323', 'IBM Plex Mono', 'JetBrains Mono', 'Fira Code', 'Courier New', monospace;
}
```

For other phosphor themes, override `--phos`, `--phos-dim`, `--phos-bright`, `--phos-glow`, `--phos-glow-soft`, `--text`, `--text-dim`, `--text-bright`, `--border`, `--border-dim` only. Keep `--bg`, `--radius: 0`, and the monospace family the same.

## The CRT effects stack

All effects are CSS-only, with one small JS typewriter for the boot overlay.

1. **Scanlines** — `body::before` with `repeating-linear-gradient` at 1–2 px and a slow drift animation.
   ```css
   body::before {
     content: ''; position: fixed; inset: 0; z-index: 9999; pointer-events: none;
     background: repeating-linear-gradient(
       to bottom,
       rgba(0,0,0,0) 0px, rgba(0,0,0,0) 1px,
       rgba(0,0,0,0.18) 2px, rgba(0,0,0,0) 3px
     );
     mix-blend-mode: multiply;
     animation: scanShift 8s linear infinite;
   }
   @keyframes scanShift { 0% { background-position: 0 0; } 100% { background-position: 0 6px; } }
   ```

2. **CRT vignette + barrel** — `body::after` with multiple radial gradients for edge darkening.
   ```css
   body::after {
     content: ''; position: fixed; inset: 0; z-index: 9998; pointer-events: none;
     background:
       radial-gradient(ellipse 100% 90% at 50% 50%, transparent 55%, rgba(0,0,0,0.55) 100%),
       radial-gradient(ellipse 100% 8% at 50% 0%, rgba(0,0,0,0.5), transparent 80%),
       radial-gradient(ellipse 100% 8% at 50% 100%, rgba(0,0,0,0.5), transparent 80%);
   }
   ```

3. **Phosphor flicker** — subtle 7s opacity animation on the wrapper.
   ```css
   @keyframes crtFlicker {
     0%, 100% { opacity: 1; }
     3% { opacity: 0.96; }
     47% { opacity: 0.98; }
   }
   .crt-wrap { animation: crtFlicker 7s infinite; }
   ```

4. **Caret blink** — used for the main title underscore and any `.blink` element.
   ```css
   @keyframes caretBlink { 0%,49%{opacity:1} 50%,100%{opacity:0} }
   .blink { animation: caretBlink 1.1s steps(1) infinite; }
   ```
   The main title `h1` gets `> SEADASH_` by adding `::before { content: '> ' }` and `::after { content: '_' }`.

5. **Text glow** — every text element gets a `text-shadow: 0 0 4px var(--phos-glow-soft)` minimum. Headers and active elements get stronger glow.

6. **Square corners** — `--radius: 0` on every element. Terminal boxes do not have rounded corners.

7. **ASCII decorations on headings** — `h2::before { content: '══ '; } h2::after { content: ' ══'; }` and `h3::before { content: '── '; }`.

8. **Bracketed buttons** — universal `button::before { content: '['; } button::after { content: ']'; }`. This works because SeaDash already styles all buttons consistently. Brackets are dim-phosphor colored; hover state brightens both brackets and text.

9. **Card corner glyphs** — `.app-card::before { content: '┌'; } .app-card::after { content: '┘'; }` placed at top-left and bottom-right with absolute positioning.

10. **Status LED dots** — `.status-led` is a 8x8 square with `box-shadow: 0 0 6px <color>` and a slow `ledPulse` opacity animation. Green = up, red = down (`.status-led.down`), yellow = warn.

11. **Header status line** — flatten the existing busy header into a single horizontal `HOST: dietpi | LOAD: 3.68 | RAM: 70.9% | DISK: 62.2% | CONTAINERS: 16/29 | CPU: 76°C` style line. Use `sl-key` (dim) and `sl-val` (bright) spans with optional `sl-warn` / `sl-err` modifiers.

12. **Boot overlay** — full-screen `position: fixed; inset: 0; z-index: 99999;` overlay with a typewriter JS that types boot lines (`SEADASH TERMINAL v2.1`, `Initializing phosphor display...`, etc.) one char at a time, then removes the overlay. Each line gets a phosphor-color class (`.boot-ok` green, `.boot-warn` yellow, `.boot-info` dim).

## Boot sequence script (paste before `</body>`)

```html
<div id="crt-boot" aria-hidden="true">
  <div class="boot-inner" id="crt-boot-text"></div>
</div>
<script>
(function(){
  const bootEl = document.getElementById('crt-boot');
  const bootText = document.getElementById('crt-boot-text');
  if (!bootEl || !bootText) return;
  const lines = [
    ['SEADASH TERMINAL v2.1  (Retro CRT Edition)', 'boot-ok'],
    ['Copyright (c) 1981-2026 - All Routes Reserved.', 'boot-info'],
    ['', ''],
    ['Initializing phosphor display..........', 'boot-ok'],
    ['Scanning host bus [I2C/SPI/PCIe].......', 'boot-ok'],
    ['Loading docker.socket..................', 'boot-ok'],
    ['Resolving 29 container endpoints.......', 'boot-warn'],
    ['Querying Cloudflare tunnel status......', 'boot-ok'],
    ['Mounting /mnt/tb/1Apps/SeaDash.........', 'boot-ok'],
    ['Calibrating CRT deflection coils.......', 'boot-ok'],
    ['', ''],
    ['> SYSTEM READY. Display will initialize momentarily...', 'boot-ok'],
  ];
  let i = 0, j = 0, cur = '';
  function render() {
    let out = '';
    for (let k = 0; k < i; k++) {
      const [t, c] = lines[k];
      out += (c ? `<span class="${c}">${t}</span>` : t) + '\n';
    }
    const [t, c] = lines[i];
    out += (c ? `<span class="${c}">${cur}</span>` : cur);
    out += '<span class="boot-cur"></span>';
    bootText.innerHTML = out;
  }
  function typeLine() {
    if (i >= lines.length) {
      setTimeout(() => bootEl.classList.add('gone'), 350);
      setTimeout(() => bootEl.remove(), 900);
      return;
    }
    const [text] = lines[i];
    if (j < text.length) {
      cur += text[j++];
      render();
      setTimeout(typeLine, 8 + Math.random()*10);
    } else {
      i++; j = 0; cur = '';
      setTimeout(typeLine, 35);
    }
  }
  typeLine();
})();
</script>
```

`#crt-boot.gone { opacity: 0; pointer-events: none; }` makes the fade-out clean.

## Verification

SeaDash is served as a static file, so verification is a curl + browser snapshot:

```bash
curl -sS -o /dev/null -w "HTTP %{http_code} | %{size_download} bytes\n" http://localhost:9090/
curl -sS http://localhost:9090/ | grep -E "SEADASH v2.1|boot-cur|var\(--phos\)|scanShift"
```

Then `browser_navigate("http://localhost:9090/")` and look for these in the snapshot:
- Headings show `══ NAME ══` decorations and `── SUBTITLE` decorations
- Title shows `> SEADASH_` with the blinking underscore
- Every button reads as `[ label ]` with brackets
- Section table headers show `> ` prefix
- Alert banner shows `! ALERT: ` prefix
- `h2`, `h3`, `button`, `input`, `table` all use monospace

The `screenshot_path` returned by `browser_vision` is the final visual reference. The amber/green/white phosphor and the scanline overlay are best confirmed by visual check, not by snapshot.

## Pitfalls

- **Re-patching the same 822-line block via `patch`** is fragile and likely to fail 2-3 times. Use `re.subn` with a callable replacement.
- **String replacement with `re.sub` and a string template** raises `re.error: bad escape \A` if the new CSS contains escape sequences. Always use a callable.
- **Universal `button::before` and `button::after`** add brackets to ALL buttons, including any icon-only or label-less ones. Verify visually that this does not produce orphan brackets on icon-only controls.
- **Do not call `setView()` or other existing JS functions from the boot script** — it runs in parallel with the page's own `loadAll()`. The boot overlay is purely visual and removes itself after the typewriter finishes.
- **Do not change `--radius` per theme** to keep the terminal square-corner look consistent. If the user later asks for a glassmorphic variant, make it a separate theme, not an override.
- **Glassmorphism backdrop-filter** has no place in a CRT theme. Remove any `backdrop-filter: blur(...)` rules inherited from the original CSS.
- **Color the main scanline with `mix-blend-mode: multiply`** so it darkens underlying colors regardless of phosphor choice. Using a fixed black overlay with normal blend mode can hide colored backgrounds.
- **Keep `pointer-events: none` on `body::before` and `body::after`** or the scanline and vignette layers will block clicks.
- **Do not commit `index.html` changes** unless the user asks. This is local-only work until pushed.

## File locations

- Source: `/mnt/tb/1Apps/SeaDash/index.html`
- Service: `/etc/systemd/system/seadash.service` → `/usr/bin/python3 /mnt/tb/1Apps/SeaDash/server.py`
- Working dir: `/mnt/tb/1Apps/SeaDash`
- Backups: `index.html.bak.*` in same directory
- Public URL: `https://dash.xuup.top`, local: `http://localhost:9090`

The Python `server.py` does not need to be touched — it serves the file as static content. Restart is not required after editing `index.html`; just refresh the browser.
