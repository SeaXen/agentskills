No. This plan breaks the verification protocol on nearly every axis (`skills/developer-tutorial/references/verification-protocol.md`). Ship decision from it would be meaningless.

**5 violations, stacked:**

1. **Wrong runner.** Marcus wrote the tutorial AND the SDK. Protocol: "Never the author, and ideally not the author's team." He's both.
2. **Wrong skill level.** Tutorial declared beginner; Marcus is your most senior engineer. Protocol: "A senior engineer breezing through a beginner tutorial proves nothing — they patch the gaps unconsciously and report success."
3. **Wrong artefact + environment.** Protocol: "Install from the published artefact (registry package, released image), not from the working tree." Main-branch build on his own laptop is neither the release nor a clean machine — no cached credentials, no preinstalled toolchain, is the bar. Catching unreleased breakage is a real goal, but it belongs in the CI checkpoint job against main (see "Keeping it verified"), not in the human learner test.
4. **Wrong observation method.** "Sit next to him, answer questions" directly violates: "Hand over the tutorial link and nothing else... The runner narrates aloud; the observer stays silent... Answering a question destroys the data point you came for." Every question he asks you is a defect you'll never log.
5. **Wrong pass bar.** "Under an hour → ship" checks 1 of 6 pass-threshold criteria (time). Missing: checkpoints pass unaided, zero hidden prerequisites, and criterion 5 — the transfer test, "the one that separates a tutorial from a long quickstart." Skip it and you can't tell if Marcus learned the concept or just executed a script he half-wrote.

**Fix:**

1. Pick a runner who's actually never used the product (or used it once via quickstart) — not Marcus, not his team. Two runners if you can: one novice, one ecosystem-fluent, different walls.
2. Fresh container/clean machine, install the published package (registry/released image), not main.
3. Hand over the link, nothing else. You take silent notes, log each snag as defect / hidden prerequisite / concept gap / friction.
4. 10 minutes after the last checkpoint, run the transfer test: a variation you never demonstrated, reference docs only, no help.
5. Ship only if all 6 pass-threshold criteria hold — not on elapsed time alone.

Separately: if you want main-branch regressions caught, wire that as a scheduled CI job per checkpoint branch against the published package — that's the protocol's actual answer to "catch anything unreleased," not folding it into the human test.

Next: pick tomorrow's actual runner (not Marcus) and decide clean-machine vs container before scheduling the session.