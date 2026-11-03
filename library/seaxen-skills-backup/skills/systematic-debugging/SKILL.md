---
name: systematic-debugging
description: "4-phase root cause debugging: understand bugs before fixing."
version: 1.1.0
author: Hermes Agent (adapted from obra/superpowers)
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [debugging, troubleshooting, problem-solving, root-cause, investigation]
    related_skills: [test-driven-development, writing-plans, subagent-driven-development]
---

# Systematic Debugging

## Overview

Random fixes waste time and create new bugs. Quick patches mask underlying issues.

**Core principle:** ALWAYS find root cause before attempting fixes. Symptom fixes are failure.

**Violating the letter of this process is violating the spirit of debugging.**

## The Iron Law

```
NO FIXES WITHOUT ROOT CAUSE INVESTIGATION FIRST
```

If you haven't completed Phase 1, you cannot propose fixes.

## When to Use

Use for ANY technical issue:
- Test failures
- Bugs in production
- Unexpected behavior
- Performance problems
- Build failures
- Integration issues

**Use this ESPECIALLY when:**
- Under time pressure (emergencies make guessing tempting)
- "Just one quick fix" seems obvious
- You've already tried multiple fixes
- Previous fix didn't work
- You don't fully understand the issue

**Don't skip when:**
- Issue seems simple (simple bugs have root causes too)
- You're in a hurry (rushing guarantees rework)
- Someone wants it fixed NOW (systematic is faster than thrashing)

## The Four Phases

You MUST complete each phase before proceeding to the next.

---

## Phase 1: Root Cause Investigation

**BEFORE attempting ANY fix:**

### 1. Read Error Messages Carefully

- Don't skip past errors or warnings
- They often contain the exact solution
- Read stack traces completely
- Note line numbers, file paths, error codes

**Action:** Use `read_file` on the relevant source files. Use `search_files` to find the error string in the codebase.

### 2. Reproduce Consistently

- Can you trigger it reliably?
- What are the exact steps?
- Does it happen every time?
- If not reproducible → gather more data, don't guess

**For browser/UI bugs:** build success is NOT verification. Interact with the live page.
- Click the real buttons/inputs in the browser tool
- Verify DOM/state changes after interaction
- Confirm live data actually appears, not just placeholders
- Check console errors and network-backed behavior before claiming success
- If the UI still looks static after a claimed fix, assume the fix is not verified yet

**Action:** Use the `terminal` tool to run the failing test or trigger the bug:

```bash
# Run specific failing test
pytest tests/test_module.py::test_name -v

# Run with verbose output
pytest tests/test_module.py -v --tb=long
```

### 3. Check Recent Changes

- What changed that could cause this?
- Git diff, recent commits
- New dependencies, config changes

**Action:**

```bash
# Recent commits
git log --oneline -10

# Uncommitted changes
git diff

# Changes in specific file
git log -p --follow src/problematic_file.py | head -100
```

### 4. Gather Evidence in Multi-Component Systems

**WHEN system has multiple components (API → service → database, CI → build → deploy):**

### 4b. For React/TypeScript refactors: audit contracts before touching logic

**WHEN a build breaks after splitting a large hook/component into tabs, pages, or helpers:**

Treat the compile errors as a contract audit, not as independent bugs.

Check these first:
- Prop names and callback signatures on both sides of every extracted component
- Return shape of shared hooks (`useX()` object keys, renamed fields, missing derived state)
- Type/schema drift after refactor (`SavedView.columns` → `SavedView.sessionColumns`, etc.)
- Renamed domain fields that survived in old code (`source_platform` vs `source`)
- Enum/union drift (`SortMode` still allows only `recent | messages | tools` while code checks `tokens | priority`)

Operational rule:
1. Run the build once and collect the full TypeScript error set
2. Group errors by contract surface, not by file count
3. Fix shape/signature mismatches first
4. Rebuild
5. Only after build is green decide whether to continue refactoring

This avoids thrashing on downstream errors created by a single stale interface.

Reference: `references/react-typescript-refactor-triage.md`

**BEFORE proposing fixes, add diagnostic instrumentation:**

For EACH component boundary:
- Log what data enters the component
- Log what data exits the component
- Verify environment/config propagation
- Check state at each layer

Run once to gather evidence showing WHERE it breaks.
THEN analyze evidence to identify the failing component.
THEN investigate that specific component.

### 5. Trace Data Flow

**WHEN error is deep in the call stack:**

### 5a. For Dockerized Node apps with native modules: check runtime alignment before changing code

**WHEN the app works on the host but fails in Docker with 500s, unhealthy status, restart loops, or missing `.node` bindings:**

Do not treat it as an application-logic bug first. Check runtime alignment across these three axes:
- **Node ABI** — host-built native addon vs container Node major
- **libc family/version** — glibc vs musl, or older glibc in the container than on the host
- **artifact completeness** — whether packaged standalone output actually includes required runtime modules

Typical indicators:
- `Could not locate the bindings file`
- `ERR_DLOPEN_FAILED`
- `GLIBC_x.xx not found`
- `Cannot find module 'next'` after packaging a supposedly complete standalone build

Operational rule:
1. Inspect container logs first
2. Confirm whether failure is JS dependency vs native binding vs libc mismatch
3. Align runtime image to the built artifact before changing app code
4. Re-verify with health endpoint + page 200 + no restart loop

Reference: `references/native-module-runtime-alignment.md`


- Where does the bad value originate?
- What called this function with the bad value?
- Keep tracing upstream until you find the source
- Fix at the source, not at the symptom

**Action:** Use `search_files` to trace references:

```python
# Find where the function is called
search_files("function_name(", path="src/", file_glob="*.py")

# Find where the variable is set
search_files("variable_name\\s*=", path="src/", file_glob="*.py")
```

### 5b. For sudden power-offs / overnight machine deaths: separate policy from hardware

### 5c. For high Docker daemon CPU: separate control-plane churn from container workload

**WHEN `dockerd` / `containerd` look hot:**

Do not assume one application container is doing the work. First determine whether the CPU is coming from **Docker control-plane activity** rather than sustained workload inside a container.

Investigate in this order:
- Measure the live shape: `pidstat -p <dockerd_pid>,<containerd_pid> 1 8` or equivalent. Bursty spikes with low idle intervals often indicate polling / healthchecks / metadata churn.
- Check whether load is actually severe: compare load average to CPU core count, and check iowait / pressure so you do not misdiagnose moderate background activity as saturation.
- List containers with restart counts and health state. A restart storm and a healthcheck storm are different failure modes.
- Sample Docker events and look specifically for repeated `exec_create`, `exec_start`, and `exec_die` on the same containers. Repeated short exec events usually mean healthchecks.
- Inspect container healthcheck config directly with `docker inspect`; image-defined healthchecks may exist even when the compose file does not show any `healthcheck:` block.
- Quantify which containers are generating the exec churn, not just that churn exists.
- Check monitoring clients such as Glances / dashboards / app managers separately; they can keep Docker busy even when containers themselves are idle.

Interpretation rules:
- If the same container shows repeated `exec_*` events every ~30s, suspect a healthcheck interval that is too aggressive for the host.
- If the compose file has no healthcheck but `docker inspect` shows one, the healthcheck is coming from the image and must be overridden explicitly.
- If `dockerd` and `containerd` spike in sync while app containers stay low, suspect control-plane polling rather than application compute.
- If restart counts stay near zero, do not call it a restart loop.

Low-risk remediation pattern:
- Back up the compose file first.
- For non-critical apps with image-defined healthchecks, override in compose with:

```yaml
healthcheck:
  disable: true
```

- Recreate only the affected containers.
- Verify with `docker inspect` that health becomes `["NONE"]`.
- Re-sample Docker events and daemon CPU after the change; do not claim success until the event churn and daemon CPU actually drop.

Scope rule:
- Prefer disabling or relaxing healthchecks on low-risk accessory apps first (dashboards, convenience UIs, download helpers) before touching core services.
- If an app is safety-critical, prefer increasing interval rather than disabling the healthcheck entirely.

Special case — `cloudflared` parallel tunnel reconnect: cloudflared opens 4 parallel QUIC tunnels to different Cloudflare edge IPs and retries each independently on failure. When the network drops you see 4 simultaneous "Failed to dial quic ... Retrying in up to 1s" lines in the docker log and `containerd` sits at 15–25% CPU for no visible reason. `docker restart cloudflared-web` is the standard first move; persistent cases need the tunnel token re-issued or the container removed.

### 5d. For thermal shutdowns at 80–95°C: separate kernel protection from BIOS emergency

**WHEN a laptop or small host keeps hard-cutting at a specific, repeatable temperature (typically 80–95°C):**

The Linux kernel's own `thermal_zone*/trip_point_*_temp` critical thresholds are almost always **100–115°C**. If the machine cuts at 85–90°C, the kernel's protection did not fire — your laptop's **BIOS/UEFI emergency protection** (Intel/AMD Tjmax firmware cutoff, embedded controller) did. Raising Linux trip points will not help; the fix is *reducing the CPU load* that pushes the package sensor to the cutoff.

Use a minute-level `power_watch.sh`-style thermal logger to confirm the cutoff temperature is stable across incidents. The crash signature in the log is unmistakable: last entry shows the package sensor at 86–90°C, then a 1–15 minute gap with **no entries at all**, then a new `boot_id`. A clean shutdown writes final journal entries; a BIOS cutoff does not.

After confirming thermal cutoff, find the runaway process. The most common laptop trap is **dockerd + containerd eating 30–40% CPU on control-plane churn** (reconnect loops, healthcheck loops) while `docker stats` shows each container near 0% — because the burn is in the daemon, not the container. Use `docker inspect <name> --format '{{.State.Health.FailingStreak}}'` to surface image-defined healthcheck failure loops, and `journalctl -u docker` to surface cloudflared-style reconnect storms.

Cheapest immediate relief: `echo 2000000 > /sys/devices/system/cpu/cpu*/cpufreq/scaling_max_freq` (cap frequency, no install). For long-term fix, stop or remove the runaway container, then install `thermald` + `tlp` so the CPU throttles before reaching the firmware cutoff.

Reference: `references/thermal-shutdown-triage.md` — full triage order, instrumentation script, the "dockerd hot but container stats show 0%" pattern, cloudflared-specific investigation, and a worked example on this host (DietPi laptop, kula + Hermes + 7 Docker containers, 88°C cutoff driven by cloudflared-web + medsea healthcheck).


**WHEN a laptop or small host powers off unexpectedly (especially overnight):**

Check for *configured* shutdown/sleep behavior before blaming random hardware, then verify the physical power path.

Investigate in this order:
- Check scheduled actions: `systemctl list-timers --all`, user/root `crontab -l`
- Check power-management config: `logind.conf`, `sleep.conf`, UPower critical power action
- Check boot history and prior-boot tail: `journalctl --list-boots`, `journalctl -b -1 -e`
- Check whether your own periodic logs show a hard timestamp gap across the suspected event window
- Check live battery health with `upower -i /org/freedesktop/UPower/devices/battery_BAT0`
- Check whether lid-close actions are disabled before assuming suspend from lid events
- Check thermals, but do not over-attribute ordinary 55–70 C laptop temps to emergency thermal shutdown without corroborating logs
- Run SMART on internal disks; a passing health result does **not** rule out transport issues like SATA CRC errors

Interpretation rules:
- A severely degraded battery (for example single-digit percent of design capacity) means tiny AC drops can kill the machine immediately
- `CriticalPowerAction=` can explain a *clean* power-management action, but not an abrupt external power cut
- SMART `CRC_Error_Count` points more toward cable/connector/path instability than media failure
- If no shutdown timer exists and there is a clean log gap ending with a new boot, power path problems become the lead suspect

After investigation, install cheap instrumentation before concluding "random":
- minute-level power/thermal logger
- `@reboot` boot marker
- persistent journald retention
- daily SMART summary

Reference: `references/sudden-poweroff-triage.md`

### Phase 1 Completion Checklist

- [ ] Error messages fully read and understood
- [ ] Issue reproduced consistently
- [ ] Recent changes identified and reviewed
- [ ] Evidence gathered (logs, state, data flow)
- [ ] Problem isolated to specific component/code
- [ ] Root cause hypothesis formed

**STOP:** Do not proceed to Phase 2 until you understand WHY it's happening.

---

## Phase 2: Pattern Analysis

**Find the pattern before fixing:**

### 1. Find Working Examples

- Locate similar working code in the same codebase
- What works that's similar to what's broken?

**Action:** Use `search_files` to find comparable patterns:

```python
search_files("similar_pattern", path="src/", file_glob="*.py")
```

### 2. Compare Against References

- If implementing a pattern, read the reference implementation COMPLETELY
- Don't skim — read every line
- Understand the pattern fully before applying

### 3. Identify Differences

- What's different between working and broken?
- List every difference, however small
- Don't assume "that can't matter"

### 4. Understand Dependencies

- What other components does this need?
- What settings, config, environment?
- What assumptions does it make?

---

## Phase 3: Hypothesis and Testing

**Scientific method:**

### 1. Form a Single Hypothesis

- State clearly: "I think X is the root cause because Y"
- Write it down
- Be specific, not vague

### 2. Test Minimally

- Make the SMALLEST possible change to test the hypothesis
- One variable at a time
- Don't fix multiple things at once

### 3. Verify Before Continuing

- Did it work? → Phase 4
- Didn't work? → Form NEW hypothesis
- DON'T add more fixes on top

### 4. When You Don't Know

- Say "I don't understand X"
- Don't pretend to know
- Ask the user for help
- Research more

---

## Phase 4: Implementation

**Fix the root cause, not the symptom:**

### 1. Create Failing Test Case

- Simplest possible reproduction
- Automated test if possible
- MUST have before fixing
- Use the `test-driven-development` skill

### 2. Implement Single Fix

- Address the root cause identified
- ONE change at a time
- No "while I'm here" improvements
- No bundled refactoring

### 3. Verify Fix

```bash
# Run the specific regression test
pytest tests/test_module.py::test_regression -v

# Run full suite — no regressions
pytest tests/ -q
```

### 4. If Fix Doesn't Work — The Rule of Three

- **STOP.**
- Count: How many fixes have you tried?
- If < 3: Return to Phase 1, re-analyze with new information
- **If ≥ 3: STOP and question the architecture (step 5 below)**
- DON'T attempt Fix #4 without architectural discussion

### 5. If 3+ Fixes Failed: Question Architecture

**Pattern indicating an architectural problem:**
- Each fix reveals new shared state/coupling in a different place
- Fixes require "massive refactoring" to implement
- Each fix creates new symptoms elsewhere

**STOP and question fundamentals:**
- Is this pattern fundamentally sound?
- Are we "sticking with it through sheer inertia"?
- Should we refactor the architecture vs. continue fixing symptoms?

**Discuss with the user before attempting more fixes.**

This is NOT a failed hypothesis — this is a wrong architecture.

---

## Red Flags — STOP and Follow Process

If you catch yourself thinking:
- "Quick fix for now, investigate later"
- "Just try changing X and see if it works"
- "Add multiple changes, run tests"
- "Skip the test, I'll manually verify"
- "It's probably X, let me fix that"
- "I don't fully understand but this might work"
- "Pattern says X but I'll adapt it differently"
- "Here are the main problems: [lists fixes without investigation]"
- Proposing solutions before tracing data flow
- **"One more fix attempt" (when already tried 2+)**
- **Each fix reveals a new problem in a different place**

**ALL of these mean: STOP. Return to Phase 1.**

**If 3+ fixes failed:** Question the architecture (Phase 4 step 5).

## Common Rationalizations

| Excuse | Reality |
|--------|---------|
| "Issue is simple, don't need process" | Simple issues have root causes too. Process is fast for simple bugs. |
| "Emergency, no time for process" | Systematic debugging is FASTER than guess-and-check thrashing. |
| "Just try this first, then investigate" | First fix sets the pattern. Do it right from the start. |
| "I'll write test after confirming fix works" | Untested fixes don't stick. Test first proves it. |
| "Multiple fixes at once saves time" | Can't isolate what worked. Causes new bugs. |
| "Reference too long, I'll adapt the pattern" | Partial understanding guarantees bugs. Read it completely. |
| "I see the problem, let me fix it" | Seeing symptoms ≠ understanding root cause. |
| "One more fix attempt" (after 2+ failures) | 3+ failures = architectural problem. Question the pattern, don't fix again. |

## Quick Reference

| Phase | Key Activities | Success Criteria |
|-------|---------------|------------------|
| **1. Root Cause** | Read errors, reproduce, check changes, gather evidence, trace data flow | Understand WHAT and WHY |
| **2. Pattern** | Find working examples, compare, identify differences | Know what's different |
| **3. Hypothesis** | Form theory, test minimally, one variable at a time | Confirmed or new hypothesis |
| **4. Implementation** | Create regression test, fix root cause, verify | Bug resolved, all tests pass |

## Hermes Agent Integration

### Investigation Tools

Use these Hermes tools during Phase 1:

- **`search_files`** — Find error strings, trace function calls, locate patterns
- **`read_file`** — Read source code with line numbers for precise analysis
- **`terminal`** — Run tests, check git history, reproduce bugs
- **`web_search`/`web_extract`** — Research error messages, library docs

### With delegate_task

For complex multi-component debugging, dispatch investigation subagents:

```python
delegate_task(
    goal="Investigate why [specific test/behavior] fails",
    context="""
    Follow systematic-debugging skill:
    1. Read the error message carefully
    2. Reproduce the issue
    3. Trace the data flow to find root cause
    4. Report findings — do NOT fix yet

    Error: [paste full error]
    File: [path to failing code]
    Test command: [exact command]
    """,
    toolsets=['terminal', 'file']
)
```

### With test-driven-development

When fixing bugs:
1. Write a test that reproduces the bug (RED)
2. Debug systematically to find root cause
3. Fix the root cause (GREEN)
4. The test proves the fix and prevents regression

## Real-World Impact

From debugging sessions:
- Systematic approach: 15-30 minutes to fix
- Random fixes approach: 2-3 hours of thrashing
- First-time fix rate: 95% vs 40%
- New bugs introduced: Near zero vs common

**No shortcuts. No guessing. Systematic always wins.**
