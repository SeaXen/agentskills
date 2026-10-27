<!-- Absorbed from the sibling skill 'vercel-react-view-transitions' (D:\Repo\.agents\skills\vercel-react-view-transitions\README.md).
     Kept verbatim so this review skill stays self-contained.
     The sibling skill itself was NOT deleted. -->
# React View Transitions Skill

An agent skill for implementing smooth, native-feeling animations using React's View Transition API.

## What This Skill Covers

- **`<ViewTransition>` component** â€” animation triggers (enter, exit, update, share), placement rules, View Transition Classes
- **`addTransitionType`** â€” tagging transitions for directional or context-specific animations
- **Shared element transitions** â€” morphing elements across different views
- **View Transition Events** â€” imperative JavaScript animations via the Web Animations API
- **CSS pseudo-elements** â€” `::view-transition-old`, `::view-transition-new`, `::view-transition-group`
- **Next.js integration** â€” `transitionTypes` on `next/link` and `useRouter`, App Router patterns
- **Accessibility** â€” `prefers-reduced-motion` handling
- **Ready-to-use CSS recipes** â€” fade, slide, scale, directional navigation

## Skill Structure

```
react-view-transitions/
â”œâ”€â”€ SKILL.md                      # Core skill (always loaded)
â”œâ”€â”€ AGENTS.md                     # Full compiled document (all references expanded)
â””â”€â”€ references/
    â”œâ”€â”€ implementation.md         # Step-by-step implementation workflow
    â”œâ”€â”€ patterns.md               # Real-world patterns and events API
    â”œâ”€â”€ troubleshooting.md        # Symptom-driven debugging
    â”œâ”€â”€ nextjs.md                 # Next.js-specific patterns
    â””â”€â”€ css-recipes.md            # Copy-paste CSS animations
```

## Installation

Install via [skills.sh](https://skills.sh):

```bash
npx skills add https://github.com/vercel-labs/agent-skills --skill vercel-react-view-transitions
```

## Resources

- [React `<ViewTransition>` docs](https://react.dev/reference/react/ViewTransition)
- [React `addTransitionType` docs](https://react.dev/reference/react/addTransitionType)
- [Next.js View Transitions guide](https://nextjs.org/docs/app/guides/view-transitions)
- [Next.js `<Link>` `transitionTypes`](https://nextjs.org/docs/app/api-reference/components/link#transitiontypes)
- [Next.js App Router Playground (view transitions)](https://github.com/vercel/next-app-router-playground/tree/main/app/view-transitions) â€” Vercel's reference implementation

