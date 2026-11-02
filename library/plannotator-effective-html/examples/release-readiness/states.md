# Release-readiness states

| State | Trigger | Visible result | Available action |
| --- | --- | --- | --- |
| Blocked | The iOS smoke test failed | The failed check and release decision show why the candidate is blocked | Record a rerun |
| Saving | A reviewer submits a rerun | The form and trigger are disabled while progress is announced | Wait |
| Save error | The simulated evidence service rejects the update | The dialog keeps its values, explains the failure, and offers retry | Retry or cancel |
| Ready | All four checks pass | The summary changes to 4 of 4 and the release action becomes available | Request production release |
| Release requested | A reviewer selects the enabled release action | The prototype explains where the real release system would take over | Close the explanation |
| Empty notes | A reviewer clears the sample notes | The notes area explains that no reviewer notes have been added | Add a note |

The prototype also defines a responsive mobile composition and reduced-motion behavior. Authentication, live data, persistence, authorization, and rollback remain outside the prototype.
