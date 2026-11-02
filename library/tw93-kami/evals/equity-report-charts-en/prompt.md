---
plugins: ["../../plugins/kami"]
tags: [equity-report, en, charts]
max_turns: 150
timeout_seconds: 2400
allowed_tools: [Read, Glob, Grep, Skill, Bash, Write, Edit, TodoWrite]
---

Write an equity research note as a PDF in the current directory. The company is Northgate Robotics, a made-up name for an internal training case, so use only the numbers below and add no outside data. Don't ask me questions, just finish it. Name the source file report.html and the PDF report.pdf.

- Business: warehouse picking robots sold with a software subscription.
- Revenue: FY2023 $412M, FY2024 $538M, FY2025 $701M. Show this as a bar or line chart.
- FY2025 revenue mix: robot hardware 61%, software subscriptions 27%, services 12%. Show this as a donut chart.
- Gross margin: FY2023 34.0%, FY2024 36.5%, FY2025 39.2%.
- Share price $46, 180M shares outstanding.
- Our view: FY2026 revenue $880M, rating Overweight, 12-month target price $58.
- Risks: two customers make up 38% of revenue; a chip supply shortage could delay deliveries.
