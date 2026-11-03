# HTML Drag-and-Drop + Click Pattern

## Problem

When an `<a>` tag has `draggable="true"`, clicking it starts a drag operation instead of navigating. This breaks `target="_blank"` links inside draggable cards.

## The Grid-Breaking Mistake

Changing the card from `<a class="card">` to `<div class="card">` with an inner `<a class="card-link">` overlay:

```html
<!-- WRONG: breaks grid layout -->
<div class="card" ondragstart="...">
  <a href="..." target="_blank" class="card-link" style="position:absolute;...">
    ...card content...
  </a>
</div>
```

The `position: absolute` on the inner `<a>` removes it from normal document flow, breaking the CSS grid. Cards lose their grid cell sizing and the layout collapses.

## Correct Pattern

Keep the card as a simple `<a>` tag. The grid works because `<a>` is a normal flow element:

```html
<!-- CORRECT: <a> is a grid item -->
<a href="http://host:port" class="card" target="_blank" rel="noopener"
   data-name="..." data-section="..." data-idx="..."
   ondragstart="dragStart(event)" ondragend="dragEnd(event)">
  <div class="card-header">...</div>
  <div class="card-desc">...</div>
  <button class="card-edit" onclick="event.preventDefault();event.stopPropagation();openEditModal(...)">✏️</button>
</a>
```

## CSS

```css
.grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
  gap: 0.75rem;
}
.card {
  display: block;  /* <a> needs this */
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: 10px;
  padding: 1rem;
  text-decoration: none;
  color: var(--text);
  position: relative;  /* for absolute-positioned children like badge/edit */
}
.card-edit {
  position: absolute;
  bottom: 0.5rem;
  right: 0.5rem;
  display: none;
  z-index: 2;
}
.card:hover .card-edit { display: block; }
```

## Key Rules

1. **Card = `<a>` tag** (not `<div>`) — needed for grid layout
2. **`target="_blank"` + `rel="noopener"`** on the `<a>` — opens in new tab
3. **Edit button** uses `event.preventDefault()` + `event.stopPropagation()` — prevents link navigation
4. **URLs** = explicit `http://host:port` (not protocol-relative `//host:port`)
5. **Drag** works on `<a>` tags — the `draggable` attribute is inherited

## URL Pattern

```javascript
// WRONG: protocol-relative can fail in new tabs
function url(app) { return `//${HOST}:${app.port}`; }

// CORRECT: explicit protocol
function url(app) { return `http://${HOST}:${app.port}${app.path || ''}`; }
```

## localStorage Overrides for Auto-Detected Apps

For Docker/Core apps that are auto-detected, user edits are stored as overrides:

```javascript
// Apply overrides before rendering
function applyOverrides(arr, section) {
  const overrides = JSON.parse(localStorage.getItem('dash-overrides') || '{}');
  return arr.map((app, idx) => {
    const ov = overrides[section + ':' + idx];
    if (ov) return { ...app, ...ov };
    return app;
  });
}

// Save override on edit
localStorage.setItem('dash-overrides', JSON.stringify({
  "docker:2": { icon: "👁️", name: "Glances", port: 61208, desc: "System monitor" }
}));
```
