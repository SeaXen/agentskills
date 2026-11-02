# Layout for "Deploy a worker"

Tabs fit the choices that swap whole blocks of content. A single flag, a 3% audience and an unsupported path don't need them. Here is the page top to bottom.

## Page outline

1. **Intro**: two sentences on what the reader will have at the end, a running worker that consumes jobs from their queue.
2. **Before you start**: a short list, not tabs.
   - You have a Corvelle account and a queue. Name the queue in one line and reuse that name in every snippet.
   - Pick your SDK language, creation method and runtime. Each choice is a tab group below.
3. **Step 1, Create the worker** (tabs: **Dashboard** | **Terraform**)
   - Dashboard: the five clicks as a numbered list.
   - Terraform: provider block, worker resource, then `terraform plan` and `terraform apply`.
   - Link out for state setup (backend, credentials). Readers who use Terraform already have state. Spelling it out here makes this tab three times longer than its sibling.
   - End the step with an explicit handoff: "You now have a worker ID and token. Step 3 uses them." This is what lets two different tabs lead into the same next step.
4. **Step 2, Write the worker** (tabs: **Python** | **Node** | **Go**)
   - Same steps and same prose outside the tabs. Only the code blocks sit inside.
   - Put the shared explanation above the tabs. Keep the prose short so the tabs contain only syntax.
5. **Step 3, Run the worker** (tabs: **Kubernetes** | **Single VM**)
   - Kubernetes: cluster prerequisite, namespace, Helm chart install, then verify with `kubectl get pods`.
   - VM: systemd unit, enable and start, then verify with `systemctl status`.
   - Each tab ends with its own verify command and the expected output.
6. **Step 4, Confirm in the dashboard** (no tabs): the worker shows as connected, then run a test job. This step is the same for every combination.
7. **Region** (a callout, not a tab group): "Add `--region eu` to [the command]. Default is US." A one-flag difference doesn't justify a tab group, and tabs would hide it from readers who never click them.
8. **Windows** (a short note under Step 3): one or two lines on what's supported and what to do instead, linking to a separate page if that page exists. At 3% of readers, don't add a third tab to the runtime group.
9. **Not supported: bare metal** (a short note at the bottom, linking to an FAQ or support answer)
   - Skip the tutorial. A step-by-step "Advanced" section tells readers it's a supported path, and support will field those tickets.
   - Say plainly that it's unsupported, why, and what to use instead.

## Tab mechanics

- **Synced groups**: use one key per dimension (`language`, `create-method`, `runtime`), so a choice carries across steps and visits.
- **Combinations**: the page has 3 × 2 × 2 = 12 reachable combinations. Open all 12 before publishing and check that nothing reads wrong, such as a step that refers to something shown only in another tab.
- **Defaults**: pick the most common option as the first tab in each group. Your analytics should tell you which that is.
- **Search and anchors**: text inside inactive tabs is hard to find with ctrl-F and may not appear in site search. Make sure your docs platform indexes all tab content.
- **Verify commands**: keep them inside the runtime tab, so each reader sees only the check that applies to them.

## Questions that could change the layout

1. **Language and the runtime step.** Does the language change the Helm chart values or the systemd `ExecStart`? If so, Step 3 needs a language-specific line, and nesting tabs gets messy. The simpler fix is to have Step 2 end with one language-agnostic artifact, such as an image or a single start command, so Step 3 never mentions language.
2. **The region flag.** Which command takes `--region eu`: the CLI, or the Terraform provider block (where it would be an argument, not a flag)? If both, the callout needs one line per creation method.
3. **VM versus bare metal.** A systemd unit on a VM already runs the worker without a container, so what makes bare metal different? If it's only "no container runtime", the VM tab may already cover it. In that case the note should point there instead of saying it's unsupported.
4. **Windows.** Is it supported, supported through WSL2 or containers, or unsupported? The note's wording depends on the answer.