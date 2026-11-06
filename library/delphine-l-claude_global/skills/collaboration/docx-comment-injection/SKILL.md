---
name: docx-comment-injection
description: Deliver review comments into a co-authored manuscript as native anchored .docx comments - the offline alternative to driving Google Docs through browser automation, preserving live Paperpile/EndNote/Zotero citations
version: 1.0.0
allowed-tools: Read, Write, Edit, Bash, Grep, Glob
---

# DOCX Comment Injection Skill

## Overview

There is a third option between "hand the user a find → replace table" and "drive their live
manuscript through a canvas editor". Round-trip the document as `.docx`, write
`w:commentRangeStart` / `w:commentRangeEnd` markers around the sentences you want to flag,
upload it back, and every point lands as a native sidebar comment anchored to its sentence —
reviewable, repliable, resolvable, and attributable.

This is the **safe channel**. Nothing in the body is modified, so there is no equivalent of
the focus-loss failure documented in `collaboration/live-document-editing`. If the output is
wrong you throw the file away; the live document was never touched.

**The script**: `inject_comments.py`, next to this file. Standard library only.

```bash
python3 inject_comments.py manuscript.docx comments.tsv -o reviewed.docx \
    --author "D. Lariviere" --initials DL
```

## Why not just use a docx library

Two constraints make this harder than it looks, and both are load-bearing.

**1. Google Docs cannot anchor a comment to a text range through any API.**
`Drive.Comments.create` and Apps Script produce *document-level*, unanchored comments. The
only way to get an anchored comment into a Google Doc is to put it in an uploaded `.docx` and
let Drive's importer convert it. The OpenXML round trip is not a workaround — it is the only
route.

**2. Reference-manager citations are hyperlinks, not text.** A Paperpile citation is

```xml
<w:hyperlink r:id="rId10">
  <w:r><w:rPr><w:vertAlign w:val="superscript"/></w:rPr><w:t>2-7</w:t></w:r>
</w:hyperlink>
```

with `rId10` resolving through `word/_rels/document.xml.rels` to a
`https://paperpile.com/c/...` cloud id. EndNote uses `ADDIN EN.CITE` field codes; Zotero uses
bookmarks. `pandoc`, naive `python-docx` scripts and regex converters flatten these to plain
text, and the co-author's bibliography stops being formattable. Editing the package directly
and touching nothing but the comment markers keeps all of it alive.

## The namespace trap — the one thing that breaks everything

**Never `ET.parse()` then `ET.write()` a `word/document.xml` and expect it to open.**

A real Word or Google Docs export declares a dozen namespaces on its root element and then
names some of them in `mc:Ignorable`:

```xml
<w:document xmlns:w="..." xmlns:mc="..." xmlns:w14="..." xmlns:w15="..." xmlns:wp14="..."
            mc:Ignorable="w14 w15 wp14">
```

`xml.etree.ElementTree` emits only the namespaces its *nodes* use. Every declaration nothing
happens to touch is silently dropped, and the rest are renamed `ns0`, `ns1`, … The
`mc:Ignorable` attribute is carried through as an opaque string, so you end up with:

```xml
<w:document xmlns:ns1="...markup-compatibility/2006" ... ns1:Ignorable="w14 w15 wp14">
```

`mc:Ignorable` now names three prefixes that are not declared anywhere. Word reports *"found
unreadable content"* and refuses the file. `python-docx` reopens it happily, so a round-trip
test in Python will tell you everything is fine.

`ET.register_namespace()` does **not** fix this. It stabilises prefixes for namespaces that
are used; it does not make ElementTree emit a declaration for one that is not.

**The fix: capture the root start-tag as a string before parsing, and substitute it back after
serialising.**

```python
ROOT_TAG = re.compile(r"<w:document\b[^>]*>")
raw = doc_path.read_text(encoding="utf-8")
original_root = ROOT_TAG.search(raw).group(0)     # before parsing
...
tree.write(doc_path, xml_declaration=True, encoding="UTF-8")
out = doc_path.read_text(encoding="utf-8")
doc_path.write_text(ROOT_TAG.sub(lambda _: original_root, out, count=1))  # after
```

The same class of problem hits `word/_rels/document.xml.rels` and `[Content_Types].xml`, which
use a *default* namespace. There, `ET.register_namespace("", PKG_R)` before parsing is
sufficient, because the default namespace is always in use.

## What the markup looks like

Three additions to the body, and nothing else:

```xml
<w:p>
  <w:commentRangeStart w:id="1"/>
  <w:r><w:t xml:space="preserve">the sentence being commented on</w:t></w:r>
  <w:hyperlink r:id="rIdPaperpile1">...</w:hyperlink>   <!-- untouched -->
  <w:commentRangeEnd w:id="1"/>
  <w:r><w:rPr><w:rStyle w:val="CommentReference"/></w:rPr>
      <w:commentReference w:id="1"/></w:r>
</w:p>
```

plus a new `word/comments.xml`, one relationship of type `.../relationships/comments`, and one
`[Content_Types].xml` override for `/word/comments.xml`.

**Insert back-to-front.** Inserting at `first` shifts every later child index by one. Sort the
pending insertions by descending paragraph then descending child index, or anchor *n+1* lands
in the wrong place after anchor *n* is written.

**`comments.xml` must carry the same namespace declarations as `document.xml`.** Easiest to
serialise it by hand from the captured declaration string rather than building it with
ElementTree.

## Anchoring: match on offsets, not on a prefix

The tempting approach — strip all non-alphanumerics, take the first 30-40 characters, find the
first paragraph containing it — fails in two ways that are hard to see afterwards:

- stripping spaces as well as punctuation destroys word boundaries, so `"rate in"` matches
  inside `"accurate inference"`
- a repeated phrase anchors to its **first** occurrence, silently, with no warning

Build the paragraph's text by concatenating `itertext()` per child while recording each
child's character span, collapse whitespace while keeping a map back to raw offsets, then
`str.find` the anchor and map the hit's start and end offsets back to child indices. An anchor
spanning several runs — including across a citation hyperlink — resolves correctly.

**Require exactly one match.** Report `NOT FOUND` and `AMBIGUOUS (k matches)` and refuse to
write by default. A comment that silently attached to the wrong paragraph is worse than one
that was never written, because the co-author will act on it.

## Verify before handing the file over

The script refuses to emit a file that fails any of these, and deletes it if one slips through.
Check the same five things in any reimplementation:

| Check | Why |
|---|---|
| every prefix in `mc:Ignorable` is declared | the namespace trap above; Word rejects the file otherwise |
| `<w:hyperlink` count unchanged | live citations survived |
| relationship count not reduced | `rId` targets still resolve |
| `xml:space="preserve"` count unchanged | ElementTree can eat leading and trailing spaces |
| `commentRangeStart` / `End` / `commentReference` counts all equal the comment count | every comment is anchored, none orphaned |

`python-docx` opening the file proves nothing — it is far more tolerant than Word. If
LibreOffice is installed, `soffice --headless --convert-to pdf` is a genuine parse test.

## Input format

TSV with a header, or a JSON list. One row per comment.

| column | | |
|---|---|---|
| `anchor` | required | exact text in the document; must occur exactly once |
| `comment` | required | body; in TSV a literal `\n` starts a new paragraph, in JSON use a real newline |
| `author` | optional | per-row override of `--author` |

`**bold**` in the body becomes a bold run, which is worth using for the label of each field.
A review comment reads better structured than as prose:

```
**CURRENT:** "…the current wording…"
**PROPOSED:** "…the replacement…"
**WHY:** the reason, in one or two sentences.
```

## Workflow for a Google Docs manuscript

1. **File → Download → Microsoft Word (.docx)** from the live document. Note which tab — a
   multi-tab Google Doc downloads only the active tab.
2. Build the TSV. **Anchors must come from the downloaded file**, not from an older PDF
   export; see `collaboration/live-document-editing` on anchor drift.
3. Run the injector. Fix every `NOT FOUND` / `AMBIGUOUS` before continuing.
4. Spot-check: unzip the output and read the anchored paragraph.
5. Upload to Drive, **right-click → Open with → Google Docs**. Comments appear in the sidebar,
   anchored and highlighted.
6. Tell the co-authors it is a *review copy*, not the manuscript. This is the one real cost of
   the approach — see below.

## The cost, stated honestly

A commented `.docx` is a **separate document**. It does not merge back into the live Google
Doc, and any edit a co-author makes in it is stranded there. That is fine for a review pass
and wrong for applying agreed changes.

| | use the .docx channel | use the live document |
|---|---|---|
| raising many points for discussion | ✅ anchored, attributable, repliable | ✗ hours of blind automation |
| a figure legend replaced wholesale | ✅ propose it as a comment | ✓ if the user wants it applied now |
| applying already-agreed substitutions | ✗ lands in the wrong copy | ✅ Editing mode, find & replace |
| document has multiple tabs | ⚠ one tab per download | ✅ all tabs present |

So: **comments through `.docx`, edits in the live document.** Offer the right one rather than
defaulting to whichever is easier to drive.

## Provenance

The architecture — LLM audit → pre/post alignment → non-destructive OpenXML comment injection,
and specifically the insight that an uploaded `.docx` is the only way to get anchored comments
into a Google Doc while keeping Paperpile links live — is Giulio Formenti's
[manuscript-audit-toolkit](https://github.com/gf777/manuscript-audit-toolkit) (MIT).

`inject_comments.py` is a reimplementation of its `commenter.py`, because the original as
published (commit `2e323a6`, 2026-08-28) produces a file Word will not open — verified against
a fixture carrying the full Word namespace set. The differences:

- the root start-tag is restored verbatim, so namespaces and `mc:Ignorable` survive
- offset-based anchoring instead of a normalised 40-character prefix, and anchors that do not
  match exactly once are reported rather than attached to the first hit
- insertions applied back-to-front, so multiple comments in one paragraph land correctly
- self-verification, with the output deleted if a check fails
- no `python-docx`, no `google-genai`, no `GEMINI_API_KEY` — stdlib only
- unpacks to a real temp directory, not the working directory

Its `auditor.py` is not reimplemented. It asks Gemini to find grammar, formatting and
nomenclature problems in isolated lines, which is of little use when you are already the model
reading the manuscript *and* have the underlying data: the errors that matter in a quantitative
paper are numbers contradicting the analysis, which no line-by-line pass without the data can
see. Its `aligner.py` (difflib paragraph then sentence mapping between a pre- and
post-revision `.docx`) is useful on its own terms if you need to show "this is what the
sentence said before".

## References

- Related skills: `collaboration/live-document-editing` (the live channel, and when to prefer
  it), `analysis/scientific-publication`
- ECMA-376 Part 1, §17.13.4 — comments; §17.13.4.4 `commentRangeStart`
- Markup Compatibility (`mc:Ignorable`): ECMA-376 Part 3
