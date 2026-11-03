---
name: creative-diagrams
description: "Create architecture, infrastructure, flow, and sequence diagrams as SVG/HTML (architecture-diagram) or hand-drawn Excalidraw JSON (excalidraw)."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [diagrams, architecture, infrastructure, visualization, svg, html, excalidraw, flowchart, sequence]
    related_skills: [architecture-diagram, excalidraw, design-md, claude-design, popular-web-designs]
---

# Creative Diagrams — Unified Diagram Creation

Two complementary diagram approaches in one skill:

| Approach | Tool | Output | Best For |
|----------|------|--------|----------|
| **Technical Architecture** | SVG/HTML generator | Standalone `.html` with inline SVG | Cloud infra, microservices, system architecture, deployment diagrams |
| **Hand-Drawn Sketches** | Excalidraw JSON | `.excalidraw` files (open at excalidraw.com) | Flowcharts, sequence diagrams, concept maps, whiteboard-style |

Use **architecture-diagram** for polished, dark-themed technical diagrams. Use **excalidraw** for quick hand-drawn diagrams, collaborative editing, or when you need editable source.

---

## Architecture Diagram (SVG/HTML)

### When to Use
- Software system architecture (frontend/backend/database layers)
- Cloud infrastructure (VPC, regions, subnets, managed services)
- Microservice/service-mesh topology
- Database + API maps, deployment diagrams
- Anything needing a dark, grid-backed tech aesthetic

### Scope
**Best suited for:** Tech/infra subjects fitting a dark aesthetic.
**Look elsewhere for:** Scientific subjects, physical objects, floor plans, hand-drawn sketches (use Excalidraw), animated explainers.

Based on [Cocoon AI's architecture-diagram-generator](https://github.com/Cocoon-AI/architecture-diagram-generator) (MIT).

### Workflow
1. User describes system (components, connections, technologies)
2. Generate HTML file following the design system below
3. Save with `write_file` to `.html` (e.g., `~/architecture-diagram.html`)
4. User opens in browser — works offline, no dependencies

### Design System & Visual Language

#### Color Palette (Semantic Mapping)

| Component Type | Fill (rgba) | Stroke (Hex) |
|----------------|-------------|--------------|
| **Frontend** | `rgba(8, 51, 68, 0.4)` | `#22d3ee` (cyan-400) |
| **Backend** | `rgba(6, 78, 59, 0.4)` | `#34d399` (emerald-400) |
| **Database** | `rgba(76, 29, 149, 0.4)` | `#a78bfa` (violet-400) |
| **AWS/Cloud** | `rgba(120, 53, 15, 0.3)` | `#fbbf24` (amber-400) |
| **Security** | `rgba(136, 19, 55, 0.4)` | `#fb7185` (rose-400) |
| **Message Bus** | `rgba(251, 146, 60, 0.3)` | `#fb923c` (orange-400) |
| **External** | `rgba(30, 41, 59, 0.5)` | `#94a3b8` (slate-400) |

#### Typography & Background
- **Font:** JetBrains Mono (Google Fonts)
- **Sizes:** 12px (Names), 9px (Sublabels), 8px (Annotations), 7px (Tiny)
- **Background:** Slate-950 (`#020617`) with 40px grid pattern

#### Technical Implementation
- **Double-rect masking:** Opaque `#0f172a` rect + semi-transparent styled rect (prevents arrow bleed-through)
- **Z-order:** Arrows early (behind components)
- **Security flows:** Dashed rose lines
- **Boundaries:** Security groups (dashed rose), Regions (large dashed amber, rx=12)
- **Legend placement:** CRITICAL — outside all boundaries, ≥20px below lowest boundary

### Document Structure
1. **Header:** Title with pulsing dot + subtitle
2. **Main SVG:** Diagram in rounded border card
3. **Summary Cards:** 3-card grid for high-level details
4. **Footer:** Minimal metadata

### Template Reference
```
skill_view(name="creative-diagrams", file_path="templates/architecture-template.html")
```

---

## Excalidraw Diagram (Hand-Drawn JSON)

### When to Use
- Architecture diagrams, flowcharts, sequence diagrams, concept maps
- Need editable source (open at excalidraw.com)
- Collaborative editing via shareable links
- Quick whiteboard-style sketches

### Workflow
1. Write elements JSON (array of Excalidraw element objects)
2. Wrap in standard envelope and save as `.excalidraw` with `write_file`
3. Optionally upload for shareable link via `scripts/upload.py`

### Saving a Diagram
```json
{
  "type": "excalidraw",
  "version": 2,
  "source": "hermes-agent",
  "elements": [ ...elements... ],
  "appState": { "viewBackgroundColor": "#ffffff" }
}
```

### Upload for Shareable Link
```bash
python scripts/upload.py ~/diagrams/my_diagram.excalidraw
```
Requires `cryptography` (`pip install cryptography`). Uploads to excalidraw.com (no account).

### Element Format Reference

#### Required Fields (all elements)
`type`, `id` (unique string), `x`, `y`, `width`, `height`

#### Element Types

**Rectangle:**
```json
{ "type": "rectangle", "id": "r1", "x": 100, "y": 100, "width": 200, "height": 100 }
```
- `roundness: { "type": 3 }` for rounded corners
- `backgroundColor: "#a5d8ff"`, `fillStyle: "solid"` for filled

**Labeled Shape (container binding — REQUIRED approach):**
```json
{ "type": "rectangle", "id": "r1", "x": 100, "y": 100, "width": 200, "height": 80,
  "roundness": { "type": 3 }, "backgroundColor": "#a5d8ff", "fillStyle": "solid",
  "boundElements": [{ "id": "t_r1", "type": "text" }] },
{ "type": "text", "id": "t_r1", "x": 105, "y": 110, "width": 190, "height": 25,
  "text": "Hello", "fontSize": 20, "fontFamily": 1, "strokeColor": "#1e1e1e",
  "textAlign": "center", "verticalAlign": "middle",
  "containerId": "r1", "originalText": "Hello", "autoResize": true }
```
⚠️ **NEVER** use `"label": { "text": "..." }` on shapes — silently ignored!

**Labeled Arrow** — same container binding approach.

**Arrow with Bindings:**
```json
{ "type": "arrow", "id": "a1", "x": 300, "y": 150, "width": 150, "height": 0,
  "points": [[0,0],[150,0]], "endArrowhead": "arrow",
  "startBinding": { "elementId": "r1", "fixedPoint": [1, 0.5] },
  "endBinding": { "elementId": "r2", "fixedPoint": [0, 0.5] } }
```
`fixedPoint`: top=[0.5,0], bottom=[0.5,1], left=[0,0.5], right=[1,0.5]

#### Drawing Order (Z-Order)
Array order = z-order (first = back, last = front)
- **GOOD:** bg_zone → shape1 → text_for_shape1 → arrow1 → arrow_label → shape2 → ...
- **BAD:** all rectangles, then all texts, then all arrows
- Always place bound text immediately after its container shape

#### Sizing Guidelines
- **Font sizes:** Min 16 (body), 20 (titles), 14 (secondary only) — NEVER below 14
- **Element sizes:** Min 120x60 for labeled shapes; 20-30px gaps between elements
- Prefer fewer, larger elements over many tiny ones

#### Color Palette
| Use | Fill Color | Hex |
|-----|-----------|-----|
| Primary / Input | Light Blue | `#a5d8ff` |
| Success / Output | Light Green | `#b2f2bb` |
| Warning / External | Light Orange | `#ffd8a8` |
| Processing / Special | Light Purple | `#d0bfff` |
| Error / Critical | Light Red | `#ffc9c9` |
| Notes / Decisions | Light Yellow | `#fff3bf` |
| Storage / Data | Light Teal | `#c3fae8` |

**Text contrast is CRITICAL** — never light gray on white. Min text on white: `#757575`.

### References & Scripts
- `references/colors.md` — Full color tables
- `references/dark-mode.md` — Dark mode diagrams
- `references/examples.md` — Larger examples
- `scripts/upload.py` — Upload to excalidraw.com for shareable link