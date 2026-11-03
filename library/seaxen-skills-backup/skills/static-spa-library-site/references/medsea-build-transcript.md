# Concrete examples from the MedSea static site build

Reference transcript from the v1→v2→v3 build cycle. Use these patterns when building similar sites.

## Site structure (verified at `/mnt/tb/Sea-knowledge/#MedSea/`)

```
#MedSea/
├── Dockerfile                           # nginx:alpine, port 80 internal, port 8855 mapped
├── docker/nginx.conf                    # gzip + 7-day PNG cache + SPA fallback
├── vercel.json                          # cleanUrls + Cache-Control headers
├── scripts/site/build_site.py           # ~1100 lines, regenerates site/ from chapters/
├── chapters/                            # source content (also git-tracked at repo root)
│   ├── 15-nephrology-urology/diseases/<topic>/{topic.png,topic.md}
│   ├── 16-cardiology/diseases/<topic>/{topic.png,topic.md}
│   ├── 17-respiratory-medicine/diseases/<topic>/{topic.png,topic.md}
│   ├── 18-endocrinology/diseases/<topic>/{topic.png,topic.md}
│   └── 21-gastroenterology/diseases/<topic>/{topic.png,topic.md}
└── site/                                # generated (PNGs in .gitignore)
    ├── index.html                       # landing, chapter grid
    ├── README.md                        # preserved across build via _README_MD template
    ├── 15-nephrology-urology/index.html # SPA shell + sidebar JS
    ├── 15-nephrology-urology/topics.json
    ├── 15-nephrology-urology/diseases/  # copied PNGs (gitignored) + MDs
    └── ... (same for each chapter)
```

## The 32-chapter Davidson 25th Ed mapping (DAVIDSON_25TH)

```python
DAVIDSON_25TH = [
    (1,  "Clinical decision-making",                None),
    (2,  "Clinical therapeutics and good prescribing", None),
    ...
    (16, "Cardiology",                              "16-cardiology"),         # LIVE
    (17, "Respiratory medicine",                    "17-respiratory-medicine"),  # LIVE
    (18, "Nephrology and urology",                  "15-nephrology-urology"), # LIVE (MedSea slug differs)
    ...
    (20, "Endocrinology",                           "18-endocrinology"),      # LIVE
    ...
    (22, "Gastroenterology",                        "21-gastroenterology"),   # LIVE
    ...
]
```

**Critical detail:** Davidson Ch 18 = Nephrology, but MedSea slug is `15-nephrology-urology`. Show **Davidson number** in dropdown (18), not slug number (15), to match the canonical chapter list the user provided.

## Build script gotchas

### `shutil.rmtree(SITE)` also deletes README and build script

If the build script lives at `site/scripts/build.py` and SITE = `site/`, then `rmtree(SITE)` deletes the script mid-execution. Two fixes:

1. **Move build script OUTSITE SITE**: `scripts/site/build_site.py` with `SITE = REPO_ROOT / "site"`.
2. **Re-create site/README.md from a template constant** after rmtree:

```python
_README_MD = """# MedSea Static Site
..."""

def main():
    if SITE.exists():
        shutil.rmtree(SITE)
    SITE.mkdir(parents=True)
    (SITE / "README.md").write_text(_README_MD)   # re-create immediately
```

### f-string `{{` `}}` doubling for embedded JS

Inside an f-string block, JS template literals with `{` and `}` collide with f-string interpolation. Double them:

```python
html += f"""
<script>
async function loadManifest() {{
  const res = await fetch(MANIFEST_URL);
  MANIFEST = await res.json();
  const params = new URLSearchParams(location.search);
  const t = params.get("topic");
  if (t) showTopic(t);
}}
function showTopic(localPrefix) {{
  // ...
  const activeEl = document.querySelector(`.topic-item[data-topic="${{localPrefix}}"]`);
  if (activeEl) {{
    activeEl.classList.add("active");
    activeEl.scrollIntoView({{ block: "nearest", behavior: "smooth" }});
  }}
}}
</script>
"""
```

A missing `{{` causes `SyntaxError: f-string: invalid syntax` at build time.

### PNG paths differ across chapters

Two patterns in source data:
- **Folder-based** (Cardiology, Nephrology): `diseases/16.1.25-atherosclerosis-pathogenesis/topic.png`
- **Flat** (Respiratory, Endo, Gastro): `diseases/17.1.01-a-a-gradient-and-oxygenation-failure.png`

Detect both in `find_files()`:

```python
for sub in sorted(diseases_dir.iterdir()):
    if not sub.is_dir(): continue
    m = re.match(r"^(\d+\.\d+)\.(\d+)-(.+)$", sub.name)
    if not m: continue
    md_f = sub / "topic.md"
    png_f = sub / "topic.png"
    if not md_f.exists(): md_f = sub / f"{slug}.md"
    if not png_f.exists(): png_f = sub / f"{slug}.png"
    topics.append({...})

for f in sorted(diseases_dir.iterdir()):
    if not f.is_file(): continue
    m = re.match(r"^(\d+\.\d+)\.(\d+)-(.+)\.(md|png)$", f.name)
    if not m: continue
    # attach to existing topic or create new
```

## The SPA sidebar JS

The chapter page boots like this:

```javascript
const CHAPTER_SLUG = "16-cardiology";
const MANIFEST_URL = "/16-cardiology/topics.json";
let MANIFEST = null;
let CURRENT_TOPIC = null;

async function loadManifest() {
  const res = await fetch(MANIFEST_URL);
  MANIFEST = await res.json();
  const t = new URLSearchParams(location.search).get("topic");
  if (t) showTopic(t);
}

function showTopic(localPrefix) {
  const t = MANIFEST.topics.find(x => x.local_prefix === localPrefix);
  if (!t) return;                              // silent fail → fallback to placeholder
  CURRENT_TOPIC = t;

  // Update sidebar active state
  document.querySelectorAll(".topic-item").forEach(el => el.classList.remove("active"));
  const activeEl = document.querySelector(`.topic-item[data-topic="${localPrefix}"]`);
  if (activeEl) {
    activeEl.classList.add("active");
    activeEl.scrollIntoView({ block: "nearest", behavior: "smooth" });
  }

  // Update URL without reload
  const url = new URL(location.href);
  url.searchParams.set("topic", localPrefix);
  history.replaceState(null, "", url);

  // Render: text BEFORE image (user preference)
  const container = document.getElementById("topicContainer");
  container.className = "topic-detail";
  const imgHtml = t.png ? `<div class="topic-image"><img src="/${CHAPTER_SLUG}/${t.png}" alt="${t.title}"></div>` : "";

  container.innerHTML = `
    <div class="crumbs"><a href="/">Home</a> · <a href="/${CHAPTER_SLUG}/">${MANIFEST.chapter_name}</a> · <span>${t.hub_num} · ${t.hub_name}</span></div>
    <div class="topic-header">
      <div>
        <h1>${t.title}</h1>
        <p class="meta">${t.hub_num} · ${t.local_prefix} · ${t.slug}</p>
      </div>
      <div class="topic-actions">
        ${t.png ? `<a href="/${CHAPTER_SLUG}/${t.png}" download>Download PNG</a>` : ""}
        ${t.md  ? `<a href="/${CHAPTER_SLUG}/${t.md}"  download>Download MD</a>`  : ""}
        <button onclick="navigateTopic(-1)">← Prev</button>
        <button onclick="navigateTopic(1)">Next →</button>
      </div>
    </div>
    <div class="topic-content">${t.html}</div>
    ${imgHtml}
  `;
}

function navigateTopic(dir) {
  if (!MANIFEST || !CURRENT_TOPIC) return;
  const i = MANIFEST.topics.findIndex(x => x.local_prefix === CURRENT_TOPIC.local_prefix);
  const ni = i + dir;
  if (ni < 0 || ni >= MANIFEST.topics.length) return;
  showTopic(MANIFEST.topics[ni].local_prefix);
}

// Sidebar search filter — hides entire hub groups when empty
document.getElementById("topicSearch").addEventListener("input", function(e) {
  const q = e.target.value.toLowerCase();
  let visible = 0;
  document.querySelectorAll(".topic-item").forEach(el => {
    const show = !q || el.textContent.toLowerCase().includes(q);
    el.style.display = show ? "" : "none";
    if (show) visible++;
  });
  document.querySelectorAll(".hub-group").forEach(g => {
    const anyVisible = Array.from(g.querySelectorAll(".topic-item")).some(el => el.style.display !== "none");
    g.style.display = anyVisible ? "" : "none";
  });
  document.getElementById("noResults").classList.toggle("show", visible === 0);
});

loadManifest();
```

## Verification probes (use browser_console when vision is down)

```javascript
// Header compactness
document.querySelector('header.site').getBoundingClientRect().height
// → 48 (good), 80+ (too tall)

// Stats visible
document.querySelector('.stats')?.offsetWidth
// → > 0 means rendered and visible

// Dropdown has all 32 chapters
document.querySelectorAll('.drop-menu .item').length
document.querySelectorAll('.drop-menu .item:not(.soon)').length
document.querySelectorAll('.drop-menu .item.soon').length

// Sidebar topic counts
document.querySelectorAll('.hub-group').length
document.querySelectorAll('.topic-item').length

// Active topic
document.querySelector('.topic-item.active')?.textContent

// Topic content rendered (image below text)
Array.from(document.getElementById('topicContainer').children)
  .map(x => x.className || x.tagName).join(' | ')
// → "crumbs | topic-header | topic-content | topic-image" (image last)
```

## Docker compose port pattern (DON'T do this)

```dockerfile
# WRONG — listens on 8855 inside container
CMD sed -i 's/listen 80;/listen 8855;/' /etc/nginx.conf && nginx

# RIGHT — listen on 80, map host port to 8855
EXPOSE 80
# host runs: docker run -p 0.0.0.0:8855:80 <image>
```

## What's NOT a static SPA library site

If the user wants ANY of these, this skill does not apply — pick a different architecture:

- Server-side filtering/search → need a backend
- Per-user bookmarks/notes → need auth + DB
- Editing content from the web → need a CMS
- >1000 topics with full-text search → need client-side search index (lunr.js / flexsearch)
- Content that updates without rebuild → need API + frontend hydration
