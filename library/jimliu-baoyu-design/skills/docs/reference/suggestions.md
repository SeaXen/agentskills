# Suggesting

An update can propose its change instead of making it: the person sees it in the page with the words struck and
added in the text, and accepts or rejects it there. Suggest when the person asks for it ("suggest", "propose", "as
suggestions", "so I can review"); otherwise write directly.

```json
{"tab": "Plan", "suggest": true, "ops": [
  {"op": "replace", "target": {"kind": "find", "text": "$95k"}, "source": {"text": "$90k"}},
  {"op": "insert", "target": {"kind": "blocks", "ids": ["bnb33mnd10h.120"]}, "side": "after",
   "source": {"markdown": "Q3: $80k."}}]}
```

- `"suggest": true` beside the ops makes the whole update one suggestion. The answer adds its `suggestId` (`sg_…`)
  and `members` (how many runs of words and blocks it holds). `"suggest": "<suggestId>"` adds to one of your own
  still open (`not_yours` for anyone else's; one no longer open answers `noop` with the notice `nothing_open`).
- A suggestion inserts, deletes or replaces: words inside one block (`find`, `chars`), whole blocks (`blocks`,
  `root`), or what a table cell holds (`replace` on a `cell` target). Any other op (`format`, `set`, `move`, `wrap`,
  `split`, `join`…), words across two blocks and deleting a cell are refused with `op_not_proposable`. It takes no
  `ifHash` or `force` (`bad_op`); `ifRev` is its only guard.
- The view marks its words `<del s='sg_…'>` and `<ins s='sg_…'>`, and a block it adds or deletes carries
  `suggest='ins'` or `'del'` and `s='sg_…'`. Both end with `<suggestions>`: each open one with `by`, `at`,
  `via='agent'` for an agent's, `mine='1'` for yours, and `asOf`. One without `via` is the person's, made in
  Suggesting mode in the page: leave it to them, and write around it as around any open suggestion. `read <root> <tab> --suggestions` lists the same
  as JSON.
- Until the person accepts it, it is not in the doc as it reads: `--markdown` and `export` keep the struck words and
  leave out the added ones.
- Accepting and rejecting are the person's (`decide_needs_a_person`). Take back your own with `{"op": "decide",
  "suggestId": "sg_…", "verdict": "withdraw", "asOf": "<its asOf from your last read>"}`, the only op in its call.
  `suggestion_changed`: it changed since you read it (the person typed in it), so read again; its `data.asOf` is
  the one now. One already decided answers `noop` with the notice `nothing_open`.
- Plain writes stay out of open suggestions: words one strikes or adds are `in_suggestion`, a block it adds or
  deletes `others_pending` (and so is suggesting into someone else's). Write before or after it, or leave it to the person. A `suggest` mark or attribute in an op is
  refused with `suggest_not_here`: use `"suggest"` on the call.
- What the person types inside words or blocks a suggestion adds joins it, and goes with it when they accept or
  reject it.
- The person can take an accept or reject back (undo in the page): the suggestion is open again with the same
  `suggestId`, except in blocks written since. One you saw decided may be open again, so read before you write
  near it.
