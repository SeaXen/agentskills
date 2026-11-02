---
type: regex
target: {source: file, path: "tidewell.html"}
match: not_contains
flags: i
pattern: '\b(?:churn|CAC|LTV|NRR|net revenue retention|payback)\b[^<\d]{0,30}\d|\d[^<\d]{0,20}\b(?:churn|CAC|LTV|NRR|payback)\b'
---
