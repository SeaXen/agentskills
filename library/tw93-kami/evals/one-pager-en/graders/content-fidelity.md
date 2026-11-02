---
type: regex
weight: 2
target: {source: file, path: "tidewell.html"}
match: contains
pattern: '<body\b(?=[\s\S]*?(?:\$1\.2(?:\s|&nbsp;|<[^>]*>)*M))(?=[\s\S]*?(?:\$310(?:\s|&nbsp;|<[^>]*>)*K))(?=[\s\S]*?(?:\b38(?!\d)))(?=[\s\S]*?(?:\b214(?!\d)))(?=[\s\S]*?(?:\$31(?:\s|&nbsp;|<[^>]*>)*K))(?=[\s\S]*?(?:\b14(?:\s|&nbsp;|<[^>]*>)*%))(?=[\s\S]*?(?:\b6(?:\s|&nbsp;|<[^>]*>)*%))(?=[\s\S]*?(?:\b120(?!\d)))(?=[\s\S]*?(?:\$6(?:\s|&nbsp;|<[^>]*>)*M))(?=[\s\S]*?(?:Ireland))(?=[\s\S]*?(?:Netherlands))(?=[\s\S]*?(?:Leeds))(?=[\s\S]*?(?:\b2023(?!\d)))'
---
