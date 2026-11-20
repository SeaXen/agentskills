# A call that needs an earlier answer

When one call needs another's answer (the latest date in the data, an id), one call may still do it: in SQL a subquery often can, with nothing for a viewer to vary. Where it can't, make each one a dataset: the page's code reads the first and sets the second's filter. Sources then shows both calls, and the rules guard both.

Only what comes from the first answer becomes a `{{name}}`, with a rule, and quoted if it sits in text ("Filters" in `reference/features.md`). Whatever must not vary stays written out in `args`:

```
datasets/latest  source: {kind: "call", connector: "Cube", tool: "semantic_query", args: {concept: "latest_day"}}
datasets/daily   source: {kind: "call", connector: "Cube", tool: "semantic_query",
    args: {concept: "arr", filters: [{member: "day", values: ["{{day}}"]}]},
    rules: {day: {pattern: "^[0-9]{4}-[0-9]{2}-[0-9]{2}$"}}}
dash/params      {day: "2026-10-28"}
files/index.html
  <section class="lx-daily" hidden>…the marks and drawings of daily…</section>
  <script>
    dash.onData(() => {
      const day = dash.data('latest').data[0]?.day;
      if (day == null) return;
      if (dash.params().day !== day) return dash.setParams({ day });
      for (const el of document.querySelectorAll('.lx-daily')) el.hidden = false;
    });
  </script>
```

It's the rule, not the first answer, that limits what a viewer can ask for: the page sends the value, and the call runs with the access the owner gave the connector. No screen shows the rule to the person, so tell them in words what it lets a viewer ask for. A `pattern` rejects a number, so fit the rule to what the first answer actually returns. The default in `dash/params` is the value the first call returned when you ran it.

On a one-writer page a mark under `hidden` loads nothing until it is shown, so the second call waits for its value. A list goes as the whole argument (`values: "{{days}}"`), and its rule holds each item. Compare it as text (`String(a) === String(b)`): `===` on two lists is never true, and `setParams` with equal values does nothing, so the page would wait forever.

A loader that calls again, to wait on a job or fetch a next page, can do so with `call` ("A loader" in `reference/sources.md`), but Sources shows only the dataset's own call. Where a reader would want to check the further call, make it a dataset of its own, which the page needn't draw. Write it exactly as the loader, or a parser of `read`, makes it, with each argument that varies a whole `{{name}}` under a rule: `args: {team: "a", cursor: "{{cursor}}"}`. The rule on its id also lets a viewer fetch any other the connector can reach, so tell the person.
