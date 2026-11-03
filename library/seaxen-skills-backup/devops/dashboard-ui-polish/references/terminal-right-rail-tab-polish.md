# Terminal right-rail tab polish

Use this when a dashboard side rail already works functionally, but the user asks for a prettier tab bar, smaller icons, cleaner preset rows, or less messy accordion behavior.

## Durable pattern

### 1. Tab bar
- Treat it like a segmented control, not three plain buttons.
- Add small contextual icons to improve scanning.
- Put counts in compact badges instead of concatenating them into the label.
- Give the active tab stronger contrast, border, and pill treatment.

### 2. Preset rows
- Reduce dead padding and bulky chrome.
- Use a summary row with:
  - chevron
  - title
  - count badge
  - edit action
- Make command rows compact, with consistent copy/pin button shells.
- If pin state matters, visually differentiate pinned rows/buttons more clearly.

### 3. Single-open accordion behavior
- For cleaner scanning, manage accordion state explicitly instead of trusting uncontrolled `<details>` behavior.
- Keep one `openSectionId` state.
- Opening one section should close the previous one.
- When a section enters edit mode, force it open.
- Persist the open section id in localStorage if the UI is a persistent operator surface.

## Verification shape
- Build passes.
- Browser DOM confirms only one section is open at a time.
- Live visual pass confirms tabs actually look better and rows are denser/cleaner, not just structurally different.

## Good trigger phrases
- "make tab bar prettier"
- "add small icon"
- "preset row cleaner"
- "make only 1 preset open at a time"
- "looks messy / bulky / ugly"
