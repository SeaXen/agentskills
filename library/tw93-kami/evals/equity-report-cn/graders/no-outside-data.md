---
type: regex
weight: 1
target: {source: file, path: "report.html"}
match: not_contains
pattern: '<body\b[\s\S]*?(?:宁德时代|阳光电源|比亚迪|派能|海博思创|特斯拉|Tesla|一致预期|可比公司|竞品)'
---
