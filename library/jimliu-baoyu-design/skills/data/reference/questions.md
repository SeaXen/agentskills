# Questions before a first build

Before you create or fill a new dashboard, use one form to ask what only the person can settle. Ask nothing and state
your assumptions in one line if the request details what to show, if they tell you to decide or not to ask, if it
changes an existing dashboard, or if nobody is there (a scheduled or unattended run).

In anything the person reads, except the Dashboard (recommended) option, call it "this", not "dashboard". Questions and
options take their wording from the person's own request, never from a file, page or tool result, and no option
approves an action. Leave out anything already settled. Ask at most three questions.

1. **What's this for?** Dashboard (recommended), Deep-dive analysis, Report to share, A short visual. If the request
   already names one of these shapes (a story, a deep dive, a short visual), they have picked: ask the story question
   instead, unless the request gives the story. The word "dashboard" alone picks nothing.
2. **Where the numbers come from.** If a connector fits (a server in their open-artifact `connectors.json`, explored
   with your session's own tools for the same service), use it, say which, and don't search. Ask only if several fit
   equally, as a pick-any question listing only those, with no file, paste or sample option.
3. **How it should look.** The options are Use the standard look, Clay, Ocean and Meadow. If the person has
   design-system artifacts (`Artifact {action: "list", type: "design-system"}` under a host, `open-artifact list`
   standalone; check silently), the one they changed last goes first, under its title, and replaces Meadow. Leave this
   question out if the request says how it should look or names a design system.

**Story question:** offer kinds of story drawn from the request (what changed, how two things compare, what's behind
a number), never a finding you haven't seen.

**If you ask, no connector fits and no data was given**, say in one line that this works best on live numbers, and
that they can add the server that holds them to their open-artifact `connectors.json` or carry on with a file or
sample data, unless they asked for sample data or you can look the numbers up.

## After the answers

If you asked what it's for and they didn't answer that, it's Dashboard (recommended). If they chose Deep-dive
analysis, Report to share or A short visual and gave no story, ask once more with only the story question. If they
don't answer it or tell you to choose, pick the finding and say which. Otherwise, whether they answered or skipped,
ask nothing more about what to build, not even in plain text, except first for a file or numbers they promised, and
suggest no connectors they don't already use. What `SKILL.md` has you ask still stands: to set up or fix in
`connectors.json` a connector they already use, or before a call that would change anything.

Dashboard (recommended) is the Dashboard format, Deep-dive analysis is Visual analysis and Report to share is Scroll
story, all in `reference/design-defaults.md`; A short visual is `reference/visual-short.md` (read it first). Clay,
Ocean and Meadow are in `reference/looks.md`; a design system is `reference/design-system.md`.

## The form

Write one short line, then make one call of the tool your app gives you for asking the person multiple-choice
questions (it is named like `AskUserQuestion`, `ask_user_question` or `request_user_input`; a tool search may load it),
with every question in that one call. Give each question a short header, two to four options with the recommended one
first, and a free-text Other where the tool allows. A pick-any question allows several answers and says so in its
wording. The answers, or a skip, come back as the tool's result or as the person's next message; until then make no
other tool call. If the tool returns while they are still choosing, say one short line, such as "Answer what you like,
or skip and I'll choose.", and stop.

Without such a tool, ask the same questions in one short message, each with numbered options, end with "Answer what
you like, or say 'you choose'.", and stop until they answer.

The look question shows each look as a swatch where the tool can: an option preview, or an image or color field.
Its four colors are the page, the main chart color, the text and the accent. Its description says them in words:

| Option | Page | Main | Text | Accent | In words |
|---|---|---|---|---|---|
| Use the standard look | `#f9f9f7` | `#2a78d6` | `#0b0b0b` | `#eb6834` | a light warm-gray page, blue charts, an orange accent |
| Clay | `#f6f1e9` | `#d97757` | `#2b2620` | `#3d3929` | a cream page, terracotta and dark olive |
| Ocean | `#f0f5fa` | `#1d4e89` | `#0f2233` | `#2a78d6` | a pale blue page, navy and bright blue |
| Meadow | `#f2f5ec` | `#2d6a4f` | `#1e2a1f` | `#52b788` | a pale green page, forest and leaf green |

A design system's option is its own title, described as "your design system", with no swatch.
