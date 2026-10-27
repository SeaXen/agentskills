# 🧠 Agent Lessons

> This file is a self-optimizing loop. When an AI agent makes a mistake and you correct it, tell the agent to document the pattern here so it mathematically never repeats the mistake.

## 📋 Lessons
- Ensure all variables are typed before pushing.
- **Skill Scalability**: Never activate >70 skills simultaneously in `.agent/skills/` to prevent prompt bloat. Use the `.agent/library/` catalog and promote on-demand via `/library`.
- **Windows CLI Scripts**: Always enforce `sys.stdout.reconfigure(encoding='utf-8')` on win32 to prevent `cp1252` `UnicodeEncodeError` on emojis or special characters.
- **Skill YAML Frontmatter**: Always quote descriptions containing colons (`"..."`) or use block scalars (`>-`) to prevent YAML parsing crashes.
- **Resource Monitoring**: Use `/usage` or `/quota` to check real-time TPM and token consumption when planning extensive agent workflows.
- **Memory Persistence**: Store architectural decisions, team conventions, and error resolutions in `.agent/lessons.md` as the repository's self-optimizing memory loop.
- **1:1 Theme Fidelity in Tailwind Codebases**: When implementing a design reference, do not rely solely on CSS variables. Build a complete `[data-theme="..."]` cascading override engine in CSS that overrides hardcoded Tailwind utilities (`bg-slate-900`, `border-slate-800`, button gradients, badges, scrollbars, and opaque popovers), inject pre-hydration scripts in `layout.jsx` to prevent FOUC, and synchronize all presets in both the quick header and settings drawer.
- **Alert Cooldown & Recharge Invalidation**: In telemetry monitoring cron jobs, always invalidate alert suppression flags and cooldown timers when a meter balance increases (recharge event) or transitions above the threshold, preventing hourly duplicate notification spam.
- **Domain-Specific Theme Styling & Purple Ban**: Curate theme palettes directly relevant to the project domain (e.g., electricity meters -> SCADA high-voltage amber & obsidian carbon) while strictly adhering to the Purple Ban (zero violet/purple/indigo hues).

