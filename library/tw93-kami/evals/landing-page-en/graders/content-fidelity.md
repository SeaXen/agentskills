---
type: regex
weight: 2
target: {source: file, path: "index.html"}
match: contains
pattern: '<body\b(?=[\s\S]*?(?:Ledgerly))(?=[\s\S]*?(?:CSV))(?=[\s\S]*?(?:\b40(?:\s|&nbsp;|<[^>]*>)*%))(?=[\s\S]*?(?:\b1,800(?!\d)))(?=[\s\S]*?(?:\$12(?!\d)))(?=[\s\S]*?(?:\b14(?:-|\s|&nbsp;)day))'
---
