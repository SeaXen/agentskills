#!/usr/bin/env python3
"""Inject anchored review comments into a .docx without touching anything else.

    python3 inject_comments.py manuscript.docx comments.tsv -o reviewed.docx
    python3 inject_comments.py manuscript.docx comments.json -o reviewed.docx --author "D. Lariviere"

Why this exists: Google Docs has no API for anchoring a comment to a text range, and
every convenient docx library flattens `<w:hyperlink>` elements, which destroys live
Paperpile / EndNote / Zotero citations. Round-tripping a .docx through the OpenXML
package is the only channel that gives anchored comments *and* keeps citations live:
upload the output to Drive, open with Google Docs, and each comment appears in the
sidebar attached to its sentence.

Input is one row per comment. TSV with a header, or a JSON list. Columns/keys:

    anchor    required  exact text in the document the comment attaches to
    comment   required  the comment body; in TSV a literal \\n starts a new
                        paragraph, in JSON use a real newline
    author    optional  overrides --author for this row

Nothing in the document body is modified. The only additions are
`w:commentRangeStart` / `w:commentRangeEnd` / `w:commentReference` markers, a new
`word/comments.xml`, and the relationship and content-type entries that declare it.

Derived from the architecture of Giulio Formenti's manuscript-audit-toolkit
(github.com/gf777/manuscript-audit-toolkit), rewritten to fix the namespace loss that
makes its output unopenable in Word, to drop the python-docx and Gemini dependencies,
and to fail loudly on an anchor that does not match exactly once.
"""
import argparse
import csv
import json
import re
import shutil
import sys
import tempfile
import zipfile
from datetime import datetime, timezone
from pathlib import Path
from xml.etree import ElementTree as ET
from xml.sax.saxutils import escape

W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
PKG_R = "http://schemas.openxmlformats.org/package/2006/relationships"
CT = "http://schemas.openxmlformats.org/package/2006/content-types"
COMMENTS_REL = "http://schemas.openxmlformats.org/officeDocument/2006/relationships/comments"
COMMENTS_CT = ("application/vnd.openxmlformats-officedocument."
               "wordprocessingml.comments+xml")

ROOT_TAG = re.compile(r"<w:document\b[^>]*>")
XMLNS = re.compile(r'xmlns:([A-Za-z0-9_.-]+)\s*=\s*"([^"]*)"')
IGNORABLE = re.compile(r'[A-Za-z0-9_.-]+:Ignorable\s*=\s*"([^"]*)"')


def w(tag):
    return f"{{{W}}}{tag}"


def norm(text):
    """Collapse whitespace but keep word boundaries, so offsets stay meaningful."""
    return re.sub(r"\s+", " ", text).strip()


# ---------------------------------------------------------------- input

def load_items(path):
    path = Path(path)
    tsv = path.suffix.lower() != ".json"
    if tsv:
        with path.open(encoding="utf-8", newline="") as fh:
            rows = list(csv.DictReader(fh, delimiter="\t"))
    else:
        rows = json.loads(path.read_text(encoding="utf-8"))
    items = []
    for n, row in enumerate(rows, start=1):
        anchor = (row.get("anchor") or "").strip()
        comment = (row.get("comment") or "").strip()
        if tsv:
            # A TSV cell cannot hold a real newline, so a literal backslash-n is
            # how a multi-paragraph comment is written there.
            comment = comment.replace("\\n", "\n")
        if not anchor or not comment:
            sys.exit(f"row {n}: both 'anchor' and 'comment' are required")
        items.append({"anchor": anchor, "comment": comment,
                      "author": (row.get("author") or "").strip()})
    if not items:
        sys.exit(f"no comments found in {path}")
    return items


# ---------------------------------------------------------------- anchoring

def paragraph_spans(p_elem):
    """[(child_index, start_char, end_char)] over the paragraph's normalised text.

    Offsets index into the string returned alongside, so an anchor found by
    `str.find` maps straight back to the run that holds it.
    """
    spans, text = [], []
    pos = 0
    for i, child in enumerate(p_elem):
        chunk = "".join(child.itertext())
        if not chunk:
            continue
        text.append(chunk)
        spans.append((i, pos, pos + len(chunk)))
        pos += len(chunk)
    return spans, "".join(text)


def locate(paragraphs, anchor):
    """Every (p_index, first_child, last_child) where the anchor occurs."""
    target = norm(anchor)
    hits = []
    for p_idx, p in enumerate(paragraphs):
        spans, raw = paragraph_spans(p)
        if not spans:
            continue
        # normalise while keeping a map back to raw offsets
        flat, back = [], []
        prev_space = True
        for k, ch in enumerate(raw):
            if ch.isspace():
                if prev_space:
                    continue
                flat.append(" ")
                back.append(k)
                prev_space = True
            else:
                flat.append(ch)
                back.append(k)
                prev_space = False
        while flat and flat[-1] == " ":
            flat.pop()
            back.pop()
        hay = "".join(flat)
        at = hay.find(target)
        while at != -1:
            s_raw, e_raw = back[at], back[at + len(target) - 1]
            first = next(i for i, s, e in spans if s <= s_raw < e)
            last = next(i for i, s, e in spans if s <= e_raw < e)
            hits.append((p_idx, first, last))
            at = hay.find(target, at + 1)
    return hits


# ---------------------------------------------------------------- comments.xml

def build_comments_xml(entries, ns_decls):
    """Serialise comments.xml by hand so the namespace set matches document.xml."""
    out = ['<?xml version="1.0" encoding="UTF-8" standalone="yes"?>',
           f"<w:comments {ns_decls}>"]
    for cid, author, initials, when, body in entries:
        out.append(f'<w:comment w:id="{cid}" w:author="{escape(author, {chr(34): "&quot;"})}" '
                   f'w:date="{when}" w:initials="{escape(initials, {chr(34): "&quot;"})}">')
        for para in body.split("\n"):
            out.append('<w:p><w:pPr><w:pStyle w:val="CommentText"/></w:pPr>')
            if para.strip():
                # **bold** runs, everything else plain
                for piece in re.split(r"(\*\*[^*]+\*\*)", para):
                    if not piece:
                        continue
                    if piece.startswith("**") and piece.endswith("**"):
                        out.append("<w:r><w:rPr><w:b/></w:rPr>"
                                   f'<w:t xml:space="preserve">{escape(piece[2:-2])}</w:t></w:r>')
                    else:
                        out.append("<w:r>"
                                   f'<w:t xml:space="preserve">{escape(piece)}</w:t></w:r>')
            out.append("</w:p>")
        out.append("</w:comment>")
    out.append("</w:comments>")
    return "".join(out)


# ---------------------------------------------------------------- package

def patch_rels(path):
    """Add the comments relationship, preserving the default namespace."""
    ET.register_namespace("", PKG_R)
    tree = ET.parse(path)
    root = tree.getroot()
    if any(r.get("Type") == COMMENTS_REL for r in root):
        return
    used = {r.get("Id") for r in root}
    rid = next(f"rId{n}" for n in range(900, 2000) if f"rId{n}" not in used)
    ET.SubElement(root, f"{{{PKG_R}}}Relationship",
                  {"Id": rid, "Type": COMMENTS_REL, "Target": "comments.xml"})
    tree.write(path, xml_declaration=True, encoding="UTF-8")


def patch_content_types(path):
    ET.register_namespace("", CT)
    tree = ET.parse(path)
    root = tree.getroot()
    if any(o.get("PartName") == "/word/comments.xml"
           for o in root.findall(f"{{{CT}}}Override")):
        return
    ET.SubElement(root, f"{{{CT}}}Override",
                  {"PartName": "/word/comments.xml", "ContentType": COMMENTS_CT})
    tree.write(path, xml_declaration=True, encoding="UTF-8")


def repack(src_dir, out_path, order):
    """Rezip, keeping [Content_Types].xml first as readers expect."""
    src_dir = Path(src_dir)
    names = [n for n in order if (src_dir / n).exists()]
    for f in sorted(src_dir.rglob("*")):
        if f.is_file():
            rel = str(f.relative_to(src_dir))
            if rel not in names:
                names.append(rel)
    with zipfile.ZipFile(out_path, "w", zipfile.ZIP_DEFLATED) as z:
        for rel in names:
            z.write(src_dir / rel, rel)


# ---------------------------------------------------------------- verify

def verify(original, output, expected):
    """Refuse to hand back a file that Word would reject. Returns a report."""
    problems, notes = [], []
    with zipfile.ZipFile(output) as z:
        doc = z.read("word/document.xml").decode("utf-8")
        names = set(z.namelist())
        rels = z.read("word/_rels/document.xml.rels").decode("utf-8")
    with zipfile.ZipFile(original) as z:
        src = z.read("word/document.xml").decode("utf-8")
        src_rels = z.read("word/_rels/document.xml.rels").decode("utf-8")

    tag = ROOT_TAG.search(doc)
    if not tag:
        problems.append("document.xml has no <w:document> root")
    else:
        declared = {p for p, _ in XMLNS.findall(tag.group(0))}
        ign = IGNORABLE.search(tag.group(0))
        missing = (set(ign.group(1).split()) - declared) if ign else set()
        if missing:
            problems.append(f"mc:Ignorable names undeclared prefixes {sorted(missing)} "
                            "- Word will report the file as unreadable")
        else:
            notes.append(f"namespace declarations intact ({len(declared)} prefixes)")

    a, b = src.count("<w:hyperlink"), doc.count("<w:hyperlink")
    if a != b:
        problems.append(f"hyperlink count changed {a} -> {b} (live citations damaged)")
    else:
        notes.append(f"hyperlinks preserved ({a})")

    a = src_rels.count("<Relationship")
    b = rels.count("<Relationship")
    if b < a:
        problems.append(f"relationships lost: {a} -> {b}")
    else:
        notes.append(f"relationships preserved ({a} -> {b})")

    a, b = src.count('xml:space="preserve"'), doc.count('xml:space="preserve"')
    if a != b:
        problems.append(f"xml:space=preserve count changed {a} -> {b} (spacing will shift)")
    else:
        notes.append(f"xml:space=preserve retained ({a})")

    for part in ("word/comments.xml", "[Content_Types].xml"):
        if part not in names:
            problems.append(f"missing part {part}")
    for n, label in ((doc.count("commentRangeStart"), "commentRangeStart"),
                     (doc.count("commentRangeEnd"), "commentRangeEnd"),
                     (doc.count("<w:commentReference"), "commentReference")):
        if n != expected:
            problems.append(f"{label} count {n}, expected {expected}")
    if not problems:
        notes.append(f"{expected} anchored comment ranges written")
    return problems, notes


# ---------------------------------------------------------------- main

def inject(docx_path, items, out_path, author, initials):
    docx_path, out_path = Path(docx_path), Path(out_path)
    work = Path(tempfile.mkdtemp(prefix="docxcomments_"))
    try:
        with zipfile.ZipFile(docx_path) as z:
            order = z.namelist()
            z.extractall(work)

        doc_path = work / "word" / "document.xml"
        raw = doc_path.read_text(encoding="utf-8")
        tag = ROOT_TAG.search(raw)
        if not tag:
            sys.exit("word/document.xml has no <w:document> root element")
        original_root = tag.group(0)
        ns_decls = " ".join(f'xmlns:{p}="{u}"' for p, u in XMLNS.findall(original_root))

        # Registering is not enough on its own - ElementTree emits only the
        # namespaces its nodes use - but it keeps the prefixes we DO use stable.
        for prefix, uri in XMLNS.findall(original_root):
            ET.register_namespace(prefix, uri)

        tree = ET.parse(doc_path)
        body = tree.getroot().find(w("body"))
        paragraphs = body.findall(f".//{w('p')}")

        when = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        entries, pending, unmatched, ambiguous = [], [], [], []

        for n, item in enumerate(items):
            hits = locate(paragraphs, item["anchor"])
            if not hits:
                unmatched.append(item["anchor"])
                continue
            if len(hits) > 1:
                ambiguous.append((item["anchor"], len(hits)))
                continue
            cid = str(len(entries) + 1)
            who = item["author"] or author
            entries.append((cid, who,
                            item["author"][:3].upper() if item["author"] else initials,
                            when, item["comment"]))
            pending.append((cid, *hits[0]))

        # Insert back-to-front so earlier indices stay valid.
        for cid, p_idx, first, last in sorted(pending, key=lambda t: (-t[1], -t[2])):
            p = paragraphs[p_idx]
            p.insert(last + 1, ET.Element(w("commentRangeEnd"), {w("id"): cid}))
            ref = ET.Element(w("r"))
            rpr = ET.SubElement(ref, w("rPr"))
            ET.SubElement(rpr, w("rStyle"), {w("val"): "CommentReference"})
            ET.SubElement(ref, w("commentReference"), {w("id"): cid})
            p.insert(last + 2, ref)
            p.insert(first, ET.Element(w("commentRangeStart"), {w("id"): cid}))

        tree.write(doc_path, xml_declaration=True, encoding="UTF-8")

        # The fix for the bug that makes naive injectors produce unopenable files:
        # put the document's own root start-tag back, verbatim, so every namespace
        # declaration and the mc:Ignorable list survive the round trip.
        out = doc_path.read_text(encoding="utf-8")
        doc_path.write_text(ROOT_TAG.sub(lambda _: original_root, out, count=1),
                            encoding="utf-8")

        (work / "word" / "comments.xml").write_text(
            build_comments_xml(entries, ns_decls), encoding="utf-8")
        patch_rels(work / "word" / "_rels" / "document.xml.rels")
        patch_content_types(work / "[Content_Types].xml")
        repack(work, out_path, order)
    finally:
        shutil.rmtree(work, ignore_errors=True)

    return len(entries), unmatched, ambiguous


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("docx", help="source .docx (never modified)")
    ap.add_argument("comments", help="TSV or JSON with anchor/comment columns")
    ap.add_argument("-o", "--output", required=True, help="output .docx")
    ap.add_argument("--author", default="Reviewer", help="comment author name")
    ap.add_argument("--initials", default="REV", help="comment author initials")
    ap.add_argument("--allow-unmatched", action="store_true",
                    help="write the file even if some anchors did not match")
    args = ap.parse_args()

    items = load_items(args.comments)
    n, unmatched, ambiguous = inject(args.docx, items, args.output,
                                     args.author, args.initials)

    print(f"{n} of {len(items)} comments anchored -> {args.output}")
    for a in unmatched:
        print(f"  NOT FOUND   {a[:70]!r}")
    for a, k in ambiguous:
        print(f"  AMBIGUOUS   {k} matches for {a[:60]!r} - lengthen the anchor")

    problems, notes = verify(args.docx, args.output, n)
    for note in notes:
        print(f"  ok  {note}")
    for p in problems:
        print(f"  FAIL  {p}")
    if problems:
        Path(args.output).unlink(missing_ok=True)
        sys.exit("output deleted: it would not have opened correctly")
    if (unmatched or ambiguous) and not args.allow_unmatched:
        sys.exit("some anchors did not match exactly once; "
                 "fix them or pass --allow-unmatched")


if __name__ == "__main__":
    main()
