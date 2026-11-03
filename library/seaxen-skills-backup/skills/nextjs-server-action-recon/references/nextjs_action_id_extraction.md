# Next.js Server Action ID Extraction — exact commands

## 1. Fetch page + list chunks
```bash
curl -s -L "https://SITE/PATH" -o page.html
# count of 40-hex candidates in static HTML (usually 0 — IDs are in JS, not HTML)
grep -oE '[0-9a-f]{40}' page.html | sort -u
# list all chunk URLs
grep -oE '/_next/static/chunks/[A-Za-z0-9_/.-]+\.js' page.html | sort -u > chunks.txt
```

## 2. Download every chunk
```bash
mkdir -p chunks && cd chunks
while read c; do
  fn=$(echo "$c" | sed 's#/_next/static/chunks/##')
  curl -s -L "https://SITE$c" -o "$fn"
done < chunks.txt
echo "downloaded: $(ls -1 | wc -l) files"
```

## 3. Extract action IDs (minified pattern, 42-hex)
```bash
python3 - <<'PY'
import re,glob
seen={}
for f in glob.glob('*.js'):
    t=open(f,encoding='utf-8',errors='replace').read()
    for m in re.finditer(r'createServerReference\)\("([0-9a-f]+)"', t):
        aid=m.group(1)
        tail=t[m.end():m.end()+120]
        nm=re.search(r'"([^"]+)"\s*\)\s*;', tail)
        seen[aid]=nm.group(1) if nm else '(unnamed)'
for a,n in sorted(seen.items()):
    print(f"{a}  |  {n}")
print("total action IDs:", len(seen))
PY
```

## Notes
- The RSC payload (`curl -L "https://SITE/PATH" -H "RSC: 1"`) usually does NOT contain these IDs for static pages.
- The static HTML returned 0 candidates; the IDs only surfaced in the downloaded `.js` chunks.
- Real IDs observed: **42 hex chars**, not 40. Don't anchor the regex on `{40}`.
- `createServerReference` in the bundle is the call site; the first quoted arg is the action ID, the trailing quoted arg (if present) is a friendly name (e.g. `"socialLogin"`, `"registration"`).
