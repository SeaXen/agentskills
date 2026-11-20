# Tabs, the doc and dropdown lists

Tabs are `file`s in a batch, the doc is `project`, a tab's body is its `node`, and a dropdown list is an `enum`.
`$lid:<alias>` names what an earlier member of the same call made (`"$lid": "<alias>"` on that member); `$lid:p` is
the doc, and in a birth `$lid:f` is its first tab and `$lid:n` that tab's body. The answer's `lids` maps each alias
to the id it got, and `acks` holds one answer per member.

## In the birth

A birth with a second tab, the first one named, a link to the second, and a dropdown:

```json
{"name": "Hiring plan 2027",
 "doc": {"markdown": "# Hiring plan 2027\n\nHow we interview: <?oa block loop?>. Status: <?oa block st?>",
         "blocks": {"loop": {"type": "mention", "ref": "file/$lid:t"},
                    "st": {"type": "dropdown", "enum": "$lid:status", "index": 1}}},
 "batch": [
  {"$lid": "status", "verb": "create", "object": "enum",
   "payload": {"name": "Status", "options": [{"name": "Open"}, {"name": "Interviewing"}, {"name": "Filled"}]}},
  {"$lid": "t", "verb": "create", "object": "file", "payload": {"name": "Interview loop"}},
  {"verb": "create", "object": "node", "payload": {"parent": {"object": "file", "id": "$lid:t"},
    "markdown": "## Interview loop\n\nFour rounds: screen, craft, systems, team."}},
  {"verb": "update", "ref": {"object": "project", "id": "$lid:p"}, "payload": {"kind": "patch", "patch": [
    {"op": "set", "path": ["tabs", "$lid:f", "name"], "value": "Plan"}]}}]}
```

## On a doc that exists

`open-artifact batch <root> <call>` takes the same members, as a list (or `{"batch": [...]}`): here a parent tab and
one nested under it.

```json
[{"$lid": "w", "verb": "create", "object": "file", "payload": {"name": "Candidates"}},
 {"$lid": "a", "verb": "create", "object": "file", "payload": {"name": "Ana Ruiz"}},
 {"verb": "create", "object": "node", "payload": {"parent": {"object": "file", "id": "$lid:a"},
   "markdown": "## Ana Ruiz\n\nStrong systems round."}},
 {"verb": "update", "ref": {"object": "project", "id": "$lid:p"}, "payload": {"kind": "patch", "patch": [
   {"op": "set", "path": ["tabs", "$lid:a", "subtabOf"], "value": "$lid:w"}]}}]
```

## Tabs

- The first tab is born as `Tab 1`. Once a doc has a second tab, name the first for what it holds (`Plan`,
  `Overview`), not the doc's title.
- `create file`'s `name` is a file name: no `/`, no spaces at the ends (`bad_name`). A tab shown with a slash
  ("Sources / raw data") is made with a plain name, then renamed by the patch.
- A new tab goes after the last one, with an empty body, so tabs made in reading order need no `order`; `create
  node` with `parent` (the tab) and `markdown` (and `blocks` for chips) gives it its first content. Link to a tab
  with a `mention` chip, `ref: "file/<tab id>"`, or with a link on words, `[words](#<tab id>)`.
- `open-artifact delete <root> '{"ref": {"object": "file", "id": "<tab>"}}'` removes a tab; links and
  mention chips to it then lead nowhere, so mend them. It takes the tab (its `file`), never its body as a `node` (`tab_body`), and the last tab
  stays (`last_tab`): to start a tab over, replace what it holds. When open comment threads hang on the tab the
  delete is refused (`anchors_affected`, naming the threads): resolve or move them, or send `"payload":
  {"allowDetach": true}` to delete it anyway.
- A deleted tab comes back with its name, body, history, comments and the subtabs deleted with it. `open-artifact
  batch <root> '[{"verb": "read", "ref": {"object": "project", "id": "<doc id>"}, "payload": {"kind": "deleted"}}]'`
  lists them; `open-artifact batch <root> '[{"verb": "create", "object": "file", "payload": {"undelete": "<tab id>"}}]'`
  restores one at its old place (`returnedTo`), or after the last tab when that place is gone. When that is refused
  (`unreadable` and the like), `{"copyOf": "<tab id>"}` in place of `undelete` adds its words as a new last tab with
  the same name, without its comments or history; the deleted tab stays in the list.

## The doc's patch

`{"verb": "update", "ref": {"object": "project", "id": "<doc id>"}, "payload": {"kind": "patch", "patch": [...]}}`,
each entry `{"op": "set", "path": [...], "value": …}` or `{"op": "delete", "path": [...]}`. The doc's id is `id`
in `read <root>` (or `$lid:p`).

- `["name"]` renames the doc.
- `["tabs", <tab>, "name"]` renames a tab; `["tabs", <tab>, "subtabOf"]` nests it under another (`delete` that
  path, or set `null`, to un-nest); `["tabs", <tab>, "order"]` moves it. Tabs sort by `order` as strings, and an
  order is letters and digits that does not end in `0`: to put a tab between two others, pick a key that sorts
  between theirs (between `V` and `k`: `a`; after `k`: `kV`).
- `["display", "tabsLocation"]` set to `"left"` lists the tabs beside the text, as "Show on page" in the page's
  tabs menu does (`delete` it to put them back in the menu). The page's font and page-width controls write
  `headingFont`, `textFont` and `pageWidth` there too; `read <root>` shows the record as `display`.
- `["locked"]` set (to `{}`, or `{"note": "<why>"}`) locks the doc, and `delete` unlocks it. Only an owner may:
  you act for the owner; a page whose person isn't one is refused with `not_owner`. While it is locked, a patch of
  `["locked"]` alone is the only write that lands; anything else, a lock patch mixed with other entries included,
  is refused with `locked`. Every open page hears the lock at once and stops taking edits. Lock or unlock only when
  the person asks.

## Dropdown lists

- `create enum` adds one: `{"name", "options": [{"name"}, …]}`. `read <root>`'s `enums` lists each with its `id`
  and its options' names.
- `{"verb": "read", "ref": {"object": "enum", "id": "<list id>"}}` (in a batch, or as `open-artifact read <root>
  '<that ref as {"ref": …}>'`) gives a list whole: each option's `name`, `order`, `disabled` and `color`.
- `{"verb": "update", "ref": {"object": "enum", "id": "<list id>"}, "payload": {"kind": "value", "value": {"name",
  "options"}}}` writes it whole. A dropdown chip names its option by position, so leave each option where it is:
  rename it in place, `"disabled": true` hides it from the picker (chips on it stay), and new ones go at the end;
  fewer options is refused (`enum_shrinks`). `order` sets where an option shows in the picker; `color` is one of
  `gray`, `sky`, `mineral`, `olive`, `pencil`, `poppy`, `fig`, `plum`. People add and edit options from a chip's
  picker too, so read the list right before you write it.
