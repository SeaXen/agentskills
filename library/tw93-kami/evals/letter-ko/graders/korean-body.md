---
type: regex
weight: 1
target: {source: file, path: "letter.html"}
match: not_contains
pattern: '<body\b[\s\S]*?(?:>[^<]*[一-鿿ぁ-ヿ]|Best regards|Sincerely)'
---
