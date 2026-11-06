# Automation Patterns and Debugging

Common patterns for Galaxy workflow automation and debugging techniques. See [SKILL.md](SKILL.md) for overview.

---

## Common Automation Patterns

### 1. Thread-Safe Galaxy Operations

**Use locks for concurrent API calls:**
```python
import threading

galaxy_lock = threading.Lock()

def thread_safe_invoke_workflow(gi, workflow_id, inputs, history_id):
    """Invoke workflow with thread safety"""
    with galaxy_lock:
        invocation = gi.workflows.invoke_workflow(
            workflow_id,
            inputs=inputs,
            history_id=history_id
        )
        return invocation['id']
```

**Why:** Galaxy API can have issues with concurrent uploads/operations from same API key.

---

### 2. Batch Processing Pattern

```python
def process_samples_batch(gi, workflow_id, samples, max_concurrent=3):
    """
    Process multiple samples with concurrency limit.

    Args:
        gi: GalaxyInstance
        workflow_id: Workflow to run
        samples: List of sample dicts with 'name' and 'files'
        max_concurrent: Max parallel invocations
    """
    from concurrent.futures import ThreadPoolExecutor, as_completed

    def process_one_sample(sample):
        # Create history
        history_id = get_or_find_history_id(gi, sample['name'])

        # Upload files
        dataset_ids = []
        for file_path in sample['files']:
            ds = gi.tools.upload_file(file_path, history_id)
            dataset_ids.append(ds['outputs'][0]['id'])

        # Invoke workflow
        inputs = {'0': {'id': dataset_ids[0], 'src': 'hda'}}
        invocation_id = thread_safe_invoke_workflow(
            gi, workflow_id, inputs, history_id
        )

        # Wait for completion
        state = wait_for_invocation(gi, invocation_id)

        return {
            'sample': sample['name'],
            'invocation_id': invocation_id,
            'state': state
        }

    # Process with limited concurrency
    with ThreadPoolExecutor(max_workers=max_concurrent) as executor:
        futures = {executor.submit(process_one_sample, s): s for s in samples}

        results = []
        for future in as_completed(futures):
            result = future.result()
            results.append(result)
            print(f"Completed: {result['sample']} - {result['state']}")

        return results
```

---

### 3. Resume Capability Pattern

**Track processed samples:**
```python
import json
import os

STATE_FILE = 'processing_state.json'

def load_state():
    """Load processing state"""
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, 'r') as f:
            return json.load(f)
    return {'completed': [], 'failed': []}

def save_state(state):
    """Save processing state"""
    with open(STATE_FILE, 'w') as f:
        json.dump(state, f, indent=2)

def process_with_resume(samples):
    """Process samples with resume capability"""
    state = load_state()

    for sample in samples:
        sample_name = sample['name']

        # Skip if already completed
        if sample_name in state['completed']:
            print(f"Skipping {sample_name} (already completed)")
            continue

        try:
            # Process sample
            result = process_one_sample(sample)

            if result['state'] == 'ok':
                state['completed'].append(sample_name)
            else:
                state['failed'].append(sample_name)

            save_state(state)

        except Exception as e:
            print(f"Error processing {sample_name}: {e}")
            state['failed'].append(sample_name)
            save_state(state)
```

---

## Debugging

### 1. Galaxy History Inspection

```python
def inspect_history(gi, history_id):
    """Print detailed history information"""
    history = gi.histories.show_history(history_id)
    print(f"History: {history['name']} ({history['id']})")
    print(f"State: {history['state']}")

    contents = gi.histories.show_history(history_id, contents=True)

    for item in contents:
        print(f"  [{item['state']}] {item['name']} (type: {item['history_content_type']})")
```

---

### 2. Invocation Step Analysis

```python
def analyze_failed_invocation(gi, invocation_id):
    """Analyze why invocation failed"""
    invocation = gi.invocations.show_invocation(
        invocation_id,
        include_workflow_steps=True
    )

    print(f"Invocation: {invocation_id}")
    print(f"State: {invocation['state']}")

    for step_id, step_data in invocation.get('steps', {}).items():
        step_state = step_data['state']
        job_id = step_data.get('job_id')

        if step_state == 'error':
            print(f"\nFailed Step {step_id}:")

            if job_id:
                job = gi.jobs.show_job(job_id)
                print(f"  Tool: {job.get('tool_id')}")
                print(f"  Exit code: {job.get('exit_code')}")
                print(f"  Stderr:\n{job.get('stderr', 'N/A')}")
```

> **CRITICAL: the function above misses subworkflow failures.** A parent step wrapping a
> subworkflow reports `state: "scheduled"` and `jobs: []` even when a job inside it errored.
> Iterating only top-level steps reports a clean invocation for a workflow that plainly failed.

**Fast triage via the REST API** (fewer round-trips than walking steps):

```bash
# 1. How bad is it?
curl -s -H "x-api-key: $KEY" "$URL/api/invocations/$INV/jobs_summary"
#    -> {"states": {"ok": 40, "paused": 20, "error": 2}, "populated_state": "failed"}

# 2. WHICH jobs errored (includes jobs nested in subworkflows)
curl -s -H "x-api-key: $KEY" "$URL/api/invocations/$INV/step_jobs_summary" \
  | python3 -c "import json,sys
for j in json.load(sys.stdin):
    if 'error' in (j.get('states') or {}): print(j['id'], j['states'])"

# 3. Full detail on one job: command_line, tool_stderr, params
curl -s -H "x-api-key: $KEY" "$URL/api/jobs/$JOB?full=true"
```

`step_jobs_summary` surfaces nested job IDs, but **not** which step they belong to. To locate
one, pull `?step_details=true`, collect every `subworkflow_invocation_id`, and recurse:

```python
def find_failed_jobs(gi_url, key, inv_id, prefix=''):
    """Walk an invocation and all nested subworkflow invocations."""
    inv = get(f'{gi_url}/api/invocations/{inv_id}?step_details=true')
    for s in inv['steps']:
        loc = f"{prefix}{s['order_index']}"
        for j in s.get('jobs', []):
            if j.get('state') == 'error':
                yield loc, s.get('workflow_step_label'), j['id']
        if s.get('subworkflow_invocation_id'):          # <-- the easy thing to miss
            yield from find_failed_jobs(gi_url, key, s['subworkflow_invocation_id'], f'{loc}/')
```

**Worked example**: invocation `ffa43919f2f13c65` showed `error: 2` in `jobs_summary`. Only one
error mapped to a top-level step (33, compleasm). The second lived at step 7 of the subworkflow
invocation behind parent step 44 -- whose own state was `scheduled`, jobs `[]`.

---

## Screen Recording with ffmpeg

For recording browser automation sessions (e.g., tutorial video generation):

```bash
# macOS: device "1" is main screen, "0" is camera
ffmpeg -f avfoundation -framerate 30 -capture_cursor 1 -i "1:none" \
  -vf "scale=1280:720" -c:v libx264 -preset ultrafast -crf 23 \
  -pix_fmt yuv420p -y output.mp4

# Linux: x11grab
ffmpeg -f x11grab -framerate 30 -video_size 1280x720 -i :0.0 \
  -c:v libx264 -preset ultrafast -crf 23 -pix_fmt yuv420p -y output.mp4
```

- Send `q` to ffmpeg's stdin for graceful stop (not SIGTERM)
- Use `ultrafast` preset during capture, re-encode later if needed
- Run as async subprocess; write `q` + drain to stop

---

## Finding Playwright Chromium

Playwright installs Chromium to a cache directory:

```python
import glob
from pathlib import Path

patterns = [
    # macOS ARM
    str(Path.home() / "Library/Caches/ms-playwright/chromium-*/chrome-mac-arm64/"
        "Google Chrome for Testing.app/Contents/MacOS/Google Chrome for Testing"),
    # macOS Intel
    str(Path.home() / "Library/Caches/ms-playwright/chromium-*/chrome-mac/"
        "Google Chrome for Testing.app/Contents/MacOS/Google Chrome for Testing"),
    # Linux
    str(Path.home() / ".cache/ms-playwright/chromium-*/chrome-linux/chrome"),
]
for pattern in patterns:
    matches = sorted(glob.glob(pattern))
    if matches:
        return matches[-1]  # latest version
```

Use this when launching Chromium with `--remote-debugging-port=9222` for browser-use CDP connection.
