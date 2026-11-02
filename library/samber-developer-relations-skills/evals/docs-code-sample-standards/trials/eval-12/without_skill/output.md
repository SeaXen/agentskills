**No audit findings. I could not find your docs tree, so there is nothing to score.**

- `docs/` in this repo holds an unrelated project's own files. It is not the Marlowe Freight corpus.
- I never saw the key-rotation guide, the security-hardening page, or any Java, Ruby or Go samples.
- The follow-up searches for them were blocked by approval prompts, and so was writing a script to `/tmp`.
- I will not invent counts. Everything below is the audit design and a tool, ready to run on your tree.

**Next action (2 min):** tell me the docs path, or run the script below yourself.

```
python3 -I /tmp/audit.py <docs-dir> --intentional '*key-rotation*' --intentional '*security-hardening*'
```

## Constraint decisions

- **Tiers deleted:** Run and Compile-only are dropped for Java, Ruby and Go. There is no CI, no network and no `javac`, `ruby` or `go` toolchain.
- **Python tier:** Python gets Compile-only through `ast.parse`. Run is only possible for samples that need no network and no credentials.
- **Other languages:** Java, Ruby and Go samples are labelled **unverified**. They get static checks only (bracket balance, credential and TLS patterns).
- **Parity gap:** a one-language toolchain means the parity matrix cannot claim tested cells for three of four languages. Report that as a gap. It is not a pass.
- **First fix-queue item:** a CI job that installs the other three toolchains. This is outside the audit itself.

## Fixing the 63-P0 noise

The cause is that one rule fires on a string's shape and ignores the page's purpose. Skipping those pages entirely would hide a real leak on exactly the pages most likely to hold one. The script applies these rules instead:

1. **Real-format keys stay P0 on every page.** These are vendor prefixes at exact lengths: AWS `AKIA` plus 16 characters, `ghp_` tokens, `sk_live_`, and PEM private-key headers. A rotation guide must show placeholders, so a real-format key there is a leak. Rotate it.
2. **Placeholder-shaped keys on the two named pages drop to INFO.** A string counts as placeholder-shaped if it has `<...>`, `EXAMPLE`, `YOUR_`, `XXXX` or `...`, or if its entropy is below 3.2 bits per character.
3. **`--insecure` demos on the two pages drop to INFO only when both hold:**
   - a warning phrase appears in the block or in the 300 characters above it;
   - the host is reserved: localhost, `127.0.0.1`, `*.example`, `*.test`, or the RFC 5737 ranges.
4. **Unlabelled or non-reserved-host demos stay P0 even on those pages.**
5. **`--insecure` and similar flags (`verify=False`, `InsecureSkipVerify`, `VERIFY_NONE`) outside those pages are P0.**
6. **Report new findings against the old baseline.** Hand-label a random 15 of the 63 old findings first, so the report states the scanner's real precision. Then publish the delta: "N new P0, 63 old reclassified." Readers will trust a P0 list again only once it is short and every entry is real.

## Sampling plan ("sample audit")

1. **Census 100% mechanically.** Count blocks by language, page and last-commit date.
2. **Hand-score about 40 samples (rubric, 20 points each).** Stratify by language × product area × age.
3. **Oversample the adoption path:** quickstart, auth, first call.
4. **Always score both exempt pages by hand.**
5. **Do not read only the top pages.** The skill names that as the failure mode.

## Pass thresholds (baselines from the skill, not industry standards)

- Zero P0.
- Compile/run pass ≥90%.
- No deprecated-API rate above 43%. This is the only gate with a measured comparator (Zhou and Walker, FSE 2016).
- ≥80% of samples executed by CI. This is unreachable today without toolchains. Cut samples before lowering the bar.

## Report template (fill from the script's output)

```
## Sample audit - Marlowe Freight docs, 2026-10-30
Corpus: <N> blocks, <L> languages, <P> pages.
Census: python compile pass <x>%; java/ruby/go unverified (no toolchain).
Secret scan: <n> real-format P0; <m> INFO on key-rotation, security-hardening.
Rubric: <40> scored, mean <_>/20.
Findings: P0 <_>, P1 <_>, P2 <_>.
Fix queue: 1 P0 rotate/replace, 2 toolchain CI, 3 quickstart to Run tier.
```

## The script (stdlib only, run with `python3 -I`)

This is **untested**. I could not write or run it here. Save it as `/tmp/audit.py` and run it on a copy of one small page first.

```python
#!/usr/bin/env python3
import ast, collections, fnmatch, math, os, re, sys

FENCE = re.compile(r"^(\s*)(```+|~~~+)\s*([\w+-]*)[^\n]*\n(.*?)^\1\2\s*$", re.S | re.M)
VENDOR_KEY = [
    ("aws-access-key", re.compile(r"\b(AKIA|ASIA)[0-9A-Z]{16}\b")),
    ("github-token", re.compile(r"\bgh[pousr]_[A-Za-z0-9]{36,}\b")),
    ("stripe-live", re.compile(r"\bsk_live_[A-Za-z0-9]{24,}\b")),
    ("private-key-block", re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----")),
]
GENERIC = re.compile(r"""(?i)(api[_-]?key|secret|token|passwd|password)\s*[=:]\s*["']?([A-Za-z0-9+/_\-]{24,})""")
PLACEHOLDER = re.compile(r"(?i)<[^>]+>|EXAMPLE|YOUR[_-]|XXXX|\.\.\.|placeholder|changeme|dummy")
INSECURE = re.compile(r"(--insecure\b|\bcurl\b[^\n]*\s-k\b|verify\s*=\s*False|InsecureSkipVerify\s*:\s*true|VERIFY_NONE|trustAll|NODE_TLS_REJECT_UNAUTHORIZED\s*=\s*0)")
RESERVED_HOST = re.compile(r"(localhost|127\.0\.0\.1|\[::1\]|\.example(\.\w+)?\b|\.test\b|\b192\.0\.2\.|\b198\.51\.100\.|\b203\.0\.113\.)")
WARNING = re.compile(r"(?i)(do not|never|only for|insecure|unsafe|development|test(ing)? only|not for production)")
LANGS = {"python": "python", "py": "python", "java": "java", "ruby": "ruby", "rb": "ruby", "go": "go", "golang": "go"}

def entropy(s):
    c = collections.Counter(s)
    return -sum(n / len(s) * math.log2(n / len(s)) for n in c.values())

def check(lang, body, before, intentional):
    out = []
    if lang == "python":
        try:
            ast.parse(body)
        except SyntaxError as e:
            out.append(("P1", "python-syntax", f"{e.msg} (block line {e.lineno})"))
    elif lang in ("java", "go"):
        for o, c in ("()", "{}", "[]"):
            if body.count(o) != body.count(c):
                out.append(("P1", "unbalanced-brackets", f"{o}{c} count differs"))
    for name, rx in VENDOR_KEY:
        for m in rx.finditer(body):
            if not PLACEHOLDER.search(m.group(0)):
                out.append(("P0", "credential-real-format", f"{name}; rotate if live"))
    for m in GENERIC.finditer(body):
        val = m.group(2)
        if PLACEHOLDER.search(m.group(0)) or entropy(val) < 3.2:
            out.append(("INFO" if intentional else "P2", "key-shaped-placeholder", val[:8] + "..."))
        else:
            out.append(("P1" if intentional else "P0", "high-entropy-literal", val[:4] + "...redacted"))
    for m in INSECURE.finditer(body):
        eol = body.find("\n", m.end())
        line = body[body.rfind("\n", 0, m.start()) + 1: eol if eol != -1 else len(body)]
        labelled = bool(WARNING.search(before) or WARNING.search(body))
        reserved = bool(RESERVED_HOST.search(line))
        if intentional and labelled and reserved:
            out.append(("INFO", "insecure-demo-ok", m.group(0)))
        elif intentional:
            out.append(("P0", "insecure-demo-unguarded",
                        f"{m.group(0)}: needs {'a warning label' if not labelled else 'a reserved host'}"))
        else:
            out.append(("P0", "insecure-default", m.group(0)))
    return out

def main():
    argv = sys.argv[1:]
    root = argv[0]
    globs = [argv[i + 1] for i, a in enumerate(argv) if a == "--intentional"]
    census, findings, total = collections.Counter(), [], 0
    for d, _, files in os.walk(root):
        for f in files:
            if not f.endswith((".md", ".mdx")):
                continue
            p = os.path.join(d, f)
            rel = os.path.relpath(p, root)
            intentional = any(fnmatch.fnmatch(rel, g) for g in globs)
            text = open(p, encoding="utf-8", errors="replace").read()
            for m in FENCE.finditer(text):
                lang = LANGS.get(m.group(3).lower(), m.group(3).lower() or "untagged")
                line = text.count("\n", 0, m.start()) + 1
                before = text[max(0, m.start() - 300): m.start()]
                total += 1
                census[lang] += 1
                for sev, rule, detail in check(lang, m.group(4), before, intentional):
                    findings.append((sev, f"{rel}:{line}", lang, rule, detail))
    print(f"Census: {total} blocks. " + ", ".join(f"{k}={v}" for k, v in census.most_common()))
    sevs = collections.Counter(s for s, *_ in findings)
    print("Findings: " + ", ".join(f"{k}={sevs[k]}" for k in ("P0", "P1", "P2", "INFO")))
    for f in sorted(findings):
        print("\t".join(f))

main()
```

Known limits:
- Ruby blocks get no static check at all, because heredocs defeat bracket counting.
- The warning check is a keyword match, so the hand-score pass must confirm each INFO.
- A script is only a census. The 40 hand-scored samples are where P1 and P2 findings come from.

**Step 1 of 3:** I need the docs path, or the script's output pasted back. Steps 2 and 3 are then the hand-scoring and the filled report.