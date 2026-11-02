---
type: regex
target: {source: file, path: "portfolio.html"}
match: not_contains
pattern: '>[^<]*\{\{[^}\n]{1,60}\}\}'
---
