---
name: baoyu-visual-content
description: "Use when turning source material into Baoyu-style visual deliverables: article illustrations, infographics, or educational comics with saved prompts and reproducible output structure."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [creative, baoyu, illustration, infographic, comic, image-generation, prompt-files]
    related_skills: [sketch, popular-web-designs]
---

# Baoyu Visual Content

## Overview

This is the class-level umbrella for Baoyu-derived visual generation workflows in Hermes. Use it when the user wants to convert text, articles, notes, or concepts into a structured visual artifact and you need to choose between illustration, infographic, or comic forms without fragmenting the workflow into multiple tiny skills.

## When to use
- The user wants article illustrations, educational comics, visual summaries, or infographic-style outputs.
- The task starts from source content and ends in one or more generated images.
- You need a reproducible workflow with saved prompt files, output directories, and optional reference-image trait extraction.

## Core rules
1. **Pick the artifact class first**: article illustration, infographic, or comic/narrative.
2. **Prompt files are mandatory reproducibility records** before image generation.
3. **Source-specific facts must survive intact**; do not flatten numbers, labels, or quotations into generic filler.
4. **Reference images are text-extracted guidance**, not direct image inputs to `image_generate`.
5. **Output organization matters**: save analysis, outlines/storyboards, prompts, and downloaded images in a stable directory tree.

## Choose the right subsection

### 1. Article illustration path
Use when the source is primarily an article or essay and the goal is to place supporting visuals at key positions.

Best for:
- explanatory articles
- tutorials
- essays needing section-level illustrations
- mixed type/style/palette planning

Durable lessons:
- illustration position and purpose should be explicit
- prompt labels must use article-specific terms and data
- the final deliverable often includes markdown insertion paths, not just loose images

### 2. Infographic path
Use when the goal is a single high-density visual summary or information graphic.

Best for:
- structured concepts
- timelines, comparisons, dashboards, frameworks
- one-image visual explainers

Durable lessons:
- choose layout from the information structure first, then style
- preserve exact stats and labels
- map custom aspect ideas onto the available `image_generate` aspect enums deliberately

### 3. Comic / narrative path
Use when the source benefits from sequencing, characters, panels, or story beats.

Best for:
- educational comics
- biographies
- tutorials with scenes and recurring characters
- multi-page outputs needing storyboard + character definitions

Durable lessons:
- confirm style/preset choices instead of silently defaulting everything
- character consistency comes from repeated text descriptions embedded in prompts
- for multi-page work, storyboard and prompt sequencing are part of the deliverable, not prep noise

## Shared workflow spine
1. Ingest source material.
2. Analyze audience, structure, language, and visual opportunity.
3. Confirm the artifact class and major style choices.
4. Write analysis / outline / storyboard files.
5. Write final prompt files.
6. Generate images.
7. Download returned URLs to stable local paths.
8. Verify files exist and match the intended output set.

## Common pitfalls
- Skipping the choice of artifact class and jumping straight into prompts.
- Generating images before writing prompt files.
- Treating `image_generate` like an image-to-image model.
- Losing source-specific numbers or terminology in labels.
- Returning URLs without downloading them into the output package.

## When `image_generate` is unavailable or unsuitable
For **text-dense educational infographics** (branded study notes, comparison-heavy cheat sheets, FCPS/MRCP-style one-pagers), AI image generation often mangles small text, breaks tables, and loses section structure. A reliable fallback is to author the artifact as **HTML/CSS** and render it to PNG via headless Chromium — gives byte-perfect typography, an editable source file, and crisp 96-DPI output. See `references/html-fallback-for-text-dense-content.md` for the full workflow, Chromium flags, page-fit pitfalls, and the body-vs-paper-bg detection gotcha.

## Verification checklist
- [ ] Correct visual format chosen (illustration vs infographic vs comic)
- [ ] Output directory structure created intentionally
- [ ] Prompt files saved before generation
- [ ] Generated image URLs downloaded locally
- [ ] Content-specific labels/data preserved
- [ ] Any reference-image influence was converted into text traits
