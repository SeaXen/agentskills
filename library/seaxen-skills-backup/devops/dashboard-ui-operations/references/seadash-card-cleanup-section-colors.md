# SeaDash card cleanup + section color controls

Use this after a compact SeaDash rewrite when the user asks for faster app cleanup, clearer separation between sections, or “some color” to distinguish groups.

## UX semantics

- **Close** means hide the app from the normal dashboard view.
  - Works for every app type: host/core, Docker/auto-discovered, and manual apps.
  - Persist by adding the app key to `config.hidden_apps`.
  - Recover from the `Hidden` tab with Unhide/bulk unhide.
- **Delete** means permanently remove a manual/custom app entry.
  - Only show `Delete` for `section === 'custom'` / manual apps.
  - Never delete auto-discovered Docker/host/public-route entries from config; those should only be closable/hidden.
  - Keep a confirmation prompt for Delete even if Close is one-click.
- Keep both controls visible on cards and table rows:
  - `Open`
  - `Close` / `Unhide`
  - `Delete` only for manual apps
  - `Edit`
  - `Move`

## Section color pattern

Add section-level color state instead of relying only on card accent colors:

```js
const sectionPalette = ['cyan','blue','purple','green','orange','pink','red','slate'];
const sectionDefaultColors = {
  core:'cyan', ai:'purple', media:'pink', download:'orange',
  admin:'blue', docker:'cyan', custom:'green', danger:'red'
};
function sectionColor(id){
  return (cfg().section_colors||{})[id] || sectionDefaultColors[id] || 'cyan';
}
```

CSS shape:

```css
.appSection{--sec:#38bdf8}
.sec-cyan{--sec:#38bdf8}.sec-blue{--sec:#60a5fa}.sec-purple{--sec:#a855f7}
.sec-green{--sec:#10b981}.sec-orange{--sec:#f59e0b}.sec-pink{--sec:#f472b6}
.sec-red{--sec:#ef4444}.sec-slate{--sec:#94a3b8}
.sectionHead{position:relative}
.sectionHead:before{content:'';position:absolute;left:0;top:0;bottom:0;width:4px;background:var(--sec)}
```

Controls:
- Add a compact `Color` button in each section header that cycles through `sectionPalette`.
- Add a color `<select data-sec-color>` in the Sections modal for direct selection.
- Include `section_colors` in layout-only export/import keys.
- Add default `section_colors` to `seadash-config.example.json`.

## Verification checklist

Run after patching:

```bash
python3 -m py_compile server.py
python3 - <<'PY'
from pathlib import Path
from html.parser import HTMLParser
html = Path('index.html').read_text()
HTMLParser().feed(html)
script = html.split('<script>',1)[1].split('</script>',1)[0]
Path('/tmp/seadash-script.js').write_text(script)
print('html parse ok')
PY
node --check /tmp/seadash-script.js
curl -sS -m 5 http://127.0.0.1:9090/api/health
```

For live UI verification, browser tools are ideal, but headless Chromium is a useful fallback when browser automation gets stuck behind a `confirm()` dialog:

```bash
chromium --headless --no-sandbox --disable-gpu \
  --virtual-time-budget=5000 --window-size=1440,1000 \
  --screenshot=/tmp/seadash.png http://127.0.0.1:9090/?v=verify
chromium --headless --no-sandbox --disable-gpu \
  --virtual-time-budget=5000 --dump-dom \
  http://127.0.0.1:9090/?v=verify > /tmp/seadash-dom.html
python3 - <<'PY'
from pathlib import Path
html = Path('/tmp/seadash-dom.html').read_text(errors='ignore')
for needle in ['Close','Delete','Color','sec-red','sec-green','44 apps']:
    print(needle, needle in html)
print('appCard count', html.count('appCard'))
print('section count', html.count('appSection'))
PY
```

Expected live assertions:
- Close buttons exist on all cards/table rows.
- Delete buttons exist only for manual/custom apps.
- Section headers show visibly different colored left strips.
- Sections modal has one color dropdown per section.
- `section_colors` persists in `/api/dashboard` config and survives reload.
- No JS console errors.

## Pitfalls

- Do not label the hide action as Delete. The user wants quick cleanup without losing auto-discovered apps.
- Do not expose Delete for Docker/host entries. They will reappear from discovery and deletion semantics become confusing.
- Do not rely on card border colors alone; section-level color strips are faster to scan.
- If a confirm dialog blocks browser automation, navigate may also stay blocked. Use headless Chromium dump/screenshot or manually accept/dismiss before retrying browser-console probes.
