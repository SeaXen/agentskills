---
type: regex
weight: 1
target: {source: file, path: "letter.html"}
match: not_contains
pattern: '<body\b[\s\S]*?(?:mailto:|[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+\.[A-Za-z]|(?<!\d)0\d{1,2}[-.)\s]\d{3,4}[-.\s]\d{4}(?!\d))'
---
