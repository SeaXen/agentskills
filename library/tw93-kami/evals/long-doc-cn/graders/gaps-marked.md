---
type: regex
target: {source: file, path: "whitepaper.html"}
match: contains
pattern: '<body\b(?=[\s\S]*?(?:多活))(?=[\s\S]*?(?:成本))(?=[\s\S]*?(?:DATA NEEDED|待补|待测|未测|尚未|未整理|待整理))'
---
