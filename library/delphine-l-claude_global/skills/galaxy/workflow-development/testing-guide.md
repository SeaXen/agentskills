# Galaxy Workflow Testing Guide

Complete reference for testing Galaxy workflows with Planemo, including test file structure, assertions, remote testing, troubleshooting, and test data management.

## Test File Structure

### Test File Naming Convention
- Workflow: `workflow-name.ga`
- Test file: `workflow-name-tests.yml` (identical name + `-tests.yml`)

### Test File Structure (YAML)

```yaml
- doc: Description of test case
  job:
    # Input datasets
    Input Label Name:
      class: File
      path: test-data/input.txt
      filetype: txt
      hashes:
      - hash_function: SHA-1
        hash_value: abc123...

    # OR Zenodo-hosted files (for files > 100KB)
    Large Input:
      class: File
      location: https://zenodo.org/records/XXXXXX/files/file.fastq.gz
      filetype: fastqsanger.gz
      hashes:
      - hash_function: SHA-1
        hash_value: def456...

    # Collection inputs
    Collection Input:
      class: Collection
      collection_type: list:paired
      elements:
      - class: File
        identifier: sample1
        path: test-data/sample1_R1.fastq
      - class: File
        identifier: sample1
        path: test-data/sample1_R2.fastq

    # Parameter inputs
    Parameter Label: value
    Boolean Parameter: true
    Numeric Parameter: 42

  outputs:
    # Output assertions
    Output Label:
      file: test-data/expected.txt

    # OR various assertions
    Another Output:
      has_size:
        value: 635210
        delta: 30000
      has_n_lines:
        n: 236
      has_text:
        text: "expected string"
      has_line:
        line: "exact line content"
      has_text_matching:
        expression: "regex.*pattern"

    # Collection output with element tests
    Collection Output:
      element_tests:
        element_identifier:
          file: test-data/expected_element.txt
          decompress: true
          compare: contains
```

---

## Assertion Types

1. **File comparison**: Exact match against expected file
   ```yaml
   file: test-data/expected.txt
   ```

2. **Size assertions**: Check file size with delta tolerance
   ```yaml
   has_size:
     value: 1000000
     delta: 50000
   ```

3. **Content assertions**:
   ```yaml
   has_n_lines: {n: 100}
   has_text: {text: "substring"}
   has_line: {line: "exact line"}
   has_text_matching: {expression: "regex.*"}
   ```

4. **Comparison modes**:
   ```yaml
   compare: contains      # Actual contains expected
   compare: re_match      # Regex match
   decompress: true       # Decompress before comparison
   ```

5. **Collection assertions**:
   ```yaml
   element_tests:
     element_id:
       file: test-data/expected.txt
   ```

### Test Assertion Syntax Requirements

**CRITICAL**: Test assertions in `-tests.yml` files must follow exact formatting to avoid `planemo workflow_lint` errors.

**WRONG** (causes `AttributeError: 'str' object has no attribute 'copy'`):
```yaml
outputs:
  Output Name:
    asserts:
      has_text: "expected text here"
```

**CORRECT**:
```yaml
outputs:
  Output Name:
    asserts:
      has_text:
        text: "expected text here"
```

**Diagnosing Assertion Format Errors**:

When `planemo workflow_lint` crashes with Python traceback containing `AttributeError` or `to_test_assert_list` failures:

```bash
# Find problematic patterns in test file
grep -n 'has_text:.*"' workflow-tests.yml
grep -n 'has_size:.*{' workflow-tests.yml
```

**All assertion types** (`has_text`, `has_size`, `has_line`, `has_n_lines`, etc.) **require nested dict format** with appropriate key:
- `has_text` -> `text: "value"`
- `has_size` -> `value: 1000, delta: 100`
- `has_line` -> `line: "exact line"`
- `has_n_lines` -> `n: 100`

---

## Planemo Verification Limitations

Some Galaxy output types cause planemo's verifier to fail in ways that look like test errors but are actually verifier limitations.

### `expression.json` outputs

Outputs typed `expression.json` (e.g. `Assembly Info` from `compose_text_param`) cannot be verified by any assertion — `has_text`, `has_size`, `has_n_lines` all fail silently with:

```
Expected file properties for output [<name>]
<file content>
None
```

The trailing "None" is the assertion result. The verifier reads the file but never confirms the assertion.

**Workaround**: Omit the output from the `outputs:` block entirely. There is no assertion that succeeds on these files.

### Conditional subworkflow outputs leave null placeholders

When a step (often a subworkflow) is gated by `when:` and the condition evaluates false, its workflow-flagged outputs *still appear* in the invocation:

- **Dataset outputs**: 4-byte `expression.json` files whose content is the literal text `null`
- **Collection outputs**: `populated_state: ok`, `element_count > 0`, but each element is itself a 4-byte null `expression.json` placeholder

A "skipped" collection looks fully populated by metadata alone. `element_count` and `populated_state` are NOT signals that real content was produced.

**Practical consequence**: in multi-config test suites (e.g. test 1 = single-haplotype mode, test 2 = dual-haplotype mode), you can't write a single shared assertion against an output from the inactive branch — the collection "exists" in both invocations but contains only null elements in one.

**How to detect a real-content branch**: fetch the first element's `file_size` and `extension` via the Galaxy API. A populated branch produces real datatypes (e.g. `html`, hundreds+ of bytes); a skipped branch produces 4-byte `expression.json` elements:

```python
coll = get(f"/api/dataset_collections/{cid}?instance_type=history&view=element")
first = coll["elements"][0]["object"]
populated = first["extension"] != "expression.json" or first["file_size"] > 10
```

### Collection elements with empty extension

When a workflow produces a `list` collection whose elements have `extension: ""` (e.g. JBrowse2 output directories), planemo crashes during verification:

```
File ".../_check_output.py", line 52, in _verify_output_file
    path = output_properties["path"]
TypeError: 'NoneType' object is not subscriptable
```

The crash happens because the element has no downloadable single-file path. Any per-element assertion (including `has_size`) triggers it.

**Workaround**: Use empty `element_tests` to verify the collection exists without checking individual elements:

```yaml
outputs:
  My JBrowse2 Collection:
    element_tests: {}
```

**Not supported**: the seemingly-obvious keys `count:` and `element_count:` are silently treated as file assertions, not collection assertions. They produce "No path specified for expected output file" errors.

### No negative tests

Planemo workflow tests do NOT support `expect_failure: true`. The Galaxy *tool* test format supports it, but planemo's workflow test parser (`runnable.py`) reads only `job`, `outputs`, `doc`. When a workflow invocation fails, the test result is always `status="error"` with no way to mark it as expected.

For verifying failure paths (e.g. a validation step rejecting bad input), write an external bioblend script rather than a planemo test.

### Collection element identifiers come from upstream collections

When a workflow output is a collection produced by mapping over an input collection, the output's element identifiers are inherited from the **input** collection's identifiers, not from the workflow logic or the data being processed. Example: a workflow that aligns a haplotype against each "Related Species" produces a JBrowse2 collection where element identifiers are `Related_species_1`, `Related_species_2`, etc. — not `Haplotype_1`/`Haplotype_2` as one might guess.

Always verify identifiers by fetching the actual collection via MCP before writing assertions:

```python
get_collection_details(<output_collection_id>)
```

---

## Configuring Planemo Tests from Galaxy Invocations

When creating Planemo test configurations, you can extract accurate parameter values from successful Galaxy workflow invocations.

### Step 1: Fetch Invocation Data

```bash
# Get invocation ID from Galaxy workflow invocation URL
# Example: https://galaxy.server.org/workflows/invocations/cc989bc4fb645bb5
INVOCATION_ID="cc989bc4fb645bb5"

# Fetch invocation details
curl -X 'GET' "https://galaxy.server.org/api/invocations/$INVOCATION_ID" \
  -H 'accept: application/json' \
  -H 'x-api-key: '$GALAXY_API_KEY > invocation.json
```

### Step 2: Extract Parameters

```python
import json

with open('invocation.json') as f:
    data = json.load(f)

# Get all workflow parameters
params = data.get('input_step_parameters', {})

# Print in YAML-ready format
for label, param_data in params.items():
    value = param_data.get('parameter_value')
    print(f"    {label}: {value}")
```

### Step 3: Structure Test YAML

```yaml
- doc: Test 1 - Description
  job:
    Input_Dataset:
      class: File
      location: https://zenodo.org/records/RECORD_ID/files/filename.ext
      filetype: format
      hashes:
      - hash_function: SHA-1
        hash_value: abc123...

    # Parameters from invocation
    Parameter Name 1: value1
    Parameter Name 2: value2
    Boolean Parameter: true  # or false
    Numeric Parameter: 10

  outputs:
    Output Name:
      asserts:
        has_text:
          text: "expected content"
        has_size:
          value: 60000
          delta: 30000  # +/-50% tolerance
```

### Common Parameter Types and Formats

| Parameter Type | YAML Format | Example |
|----------------|-------------|---------|
| Boolean | `true`/`false` | `Do you want X?: true` |
| String | Plain or quoted | `Species Name: Test_species` |
| Number | Unquoted | `Minimum Quality: 10` |
| List (comma-sep) | Quoted string | `Patterns: "A,B,C"` |

### Trailing whitespace in input labels

Galaxy input labels can include trailing whitespace (e.g. `"Download sequences? "`). Test YAML keys must match exactly, **including the trailing space**. Always extract labels programmatically rather than retyping:

```python
import json
ga = json.load(open('workflow.ga'))
for s in ga['steps'].values():
    if s.get('type', '').startswith('parameter_input') or s.get('type') == 'data_input':
        print(repr(s['label']))   # repr() reveals trailing spaces
```

In YAML, always quote keys with trailing spaces: `"Download sequences? ": true`. Planemo lint catches the mismatch as `ERROR: Non-optional input has no value specified in workflow test job`.

### Validating Test Parameters

Before running tests, verify:

1. **All mandatory parameters present** - Check workflow file for required inputs
2. **Data types match** - Boolean as boolean, not string "true"
3. **File paths correct** - Zenodo URLs, local paths, or collection structures
4. **Output names match workflow** - Use exact labels from workflow outputs

### Testing Strategy for Collections

Create two test cases to validate both single-file and collection inputs:

```yaml
# Test 1: Single dataset per input (minimal)
- doc: Test 1 - Single read set
  job:
    PacBio reads:
      class: Collection
      collection_type: list
      elements:
      - class: File
        identifier: set_1
        location: https://zenodo.org/.../reads_1.fastq.gz

# Test 2: Multiple datasets (collection handling)
- doc: Test 2 - Multiple read sets
  job:
    PacBio reads:
      class: Collection
      collection_type: list
      elements:
      - class: File
        identifier: set_1
        location: https://zenodo.org/.../reads_1.fastq.gz
      - class: File
        identifier: set_2
        location: https://zenodo.org/.../reads_2.fastq.gz
```

This tests both minimal workflow execution and collection merging logic.

---

## Verifying Workflow Output Names

Workflow output names can change between versions. Always verify output names before creating test assertions.

### Extract All Workflow Outputs

```bash
# Get all workflow output labels
grep -A 2 '"workflow_outputs"' workflow.ga | \
  grep -A 1 '"label":' | \
  grep '"label"' | \
  cut -d'"' -f4 | \
  sort -u

# Or use Python for structured extraction
cat workflow.ga | python3 -c "
import json, sys
wf = json.load(sys.stdin)
outputs = set()
for step in wf['steps'].values():
    for out in step.get('workflow_outputs', []):
        if 'label' in out and out['label']:
            outputs.add(out['label'])
for name in sorted(outputs):
    print(name)
"
```

### Common Output Name Patterns

Some tools change output names over versions:

| Old Name | Current Name | Tool |
|----------|--------------|------|
| `Seqtk-telo Output` | `Telomere Report` | seqtk_telo |
| `Telomeres Bedgraph` | `terminal telomeres` | custom scripts |
| `Coverage Track` | `BigWig Coverage` | bamCoverage |

Always verify against the actual `.ga` file, not documentation.

### Updating Test Assertions

When output names change, update test YAML:

```yaml
# OLD (will fail)
outputs:
  Seqtk-telo Output:
    asserts:
      has_text:
        text: "scaffold_10"

# NEW (correct)
outputs:
  Telomere Report:
    asserts:
      has_text:
        text: "scaffold_10"
```

---

## Test Data Organization

For workflows requiring multiple input files (e.g., assemblies + sequencing reads), use this structure:

```
workflow-directory/
├── workflow.ga
├── workflow-tests.yml
├── test_data/
│   ├── README.md              # Quick reference with SHA-1 hashes
│   ├── Haplotype_1.fasta
│   ├── Haplotype_2.fasta
│   ├── PacBio_reads_1.fastq.gz
│   ├── PacBio_reads_2.fastq.gz
│   ├── HiC_forward_1.fastqsanger.gz
│   ├── HiC_reverse_1.fastqsanger.gz
│   ├── HiC_forward_2.fastqsanger.gz
│   └── HiC_reverse_2.fastqsanger.gz
├── TEST_DATA_README.md        # Detailed characteristics
├── TEST_CONFIGURATION_GUIDE.md # Test setup instructions
└── TESTS_SUMMARY.md           # Quick reference guide
```

### Test Data README Template

```markdown
# Test Data Quick Reference

**Total Files**: 8
**Total Size**: ~33.5 MB

| # | File | Type | Size | SHA-1 Hash |
|---|------|------|------|------------|
| 1 | Haplotype_1.fasta | Assembly | 1.11 MB | `a0ee25...` |
| 2 | PacBio_reads_1.fastq.gz | HiFi | 10.20 MB | `84fe8f...` |
...

## Collection Structure

### PacBio: List Collection
- set_1: 739 reads (~5x coverage)
- set_2: 447 reads (~3x coverage)

### Hi-C: List:Paired Collection
- set_1: 30,000 pairs (forward + reverse)
- set_2: 20,000 pairs (forward + reverse)
```

### Collection YAML Syntax (Complete Reference)

**list:paired** (e.g., Hi-C reads):
```yaml
Input Label:
  class: Collection
  collection_type: list:paired
  elements:
  - class: Collection
    type: paired
    identifier: set_name
    elements:
    - identifier: forward
      class: File
      path: test-data/forward.fastqsanger.gz  # or location: URL
      filetype: fastqsanger.gz
    - identifier: reverse
      class: File
      path: test-data/reverse.fastqsanger.gz
      filetype: fastqsanger.gz
```

**list** (e.g., PacBio reads):
```yaml
Input Label:
  class: Collection
  collection_type: list
  elements:
  - class: File
    identifier: set_name
    path: test-data/reads.fastq.gz
    filetype: fastqsanger.gz
```

Note: `path` for local files, `location` for URLs. Include `hashes` with SHA-1 for Zenodo-hosted files.

### Documentation Best Practices

1. **README.md in test_data/**: SHA-1 hashes and file list
2. **TEST_DATA_README.md**: Detailed data characteristics
3. **TEST_CONFIGURATION_GUIDE.md**: How to use the test data
4. **TESTS_SUMMARY.md**: Quick start for developers

This helps reviewers understand test data without downloading/inspecting files.

### Matching Test Configuration to Workflow Paths

Test configurations must accurately reflect workflow behavior, especially for workflows with optional processing steps:

**Example**: Optional duplicate removal affects outputs and assertions:

```yaml
- doc: Test 1 - Single read set (with duplicate removal enabled)
  job:
    Remove duplicated Hi-C reads?: true  # Optional feature enabled
    # ... other parameters

  outputs:
    Markduplicates Summary:  # Only present when duplicates removed
      asserts:
        has_text:
          text: "1042\t217\t3942"

- doc: Test 2 - Single read set (without duplicate removal)
  job:
    Remove duplicated Hi-C reads?: false  # Optional feature disabled
    # ... other parameters

  outputs:
    # Markduplicates Summary not tested - not generated
```

**Key Principles**:
1. **Document feature toggles** in test `doc` field (e.g., "with duplicate removal", "without trimming")
2. **Match assertions to enabled features** - don't assert on outputs that won't be generated
3. **Test different paths** when workflow has significant optional steps
4. **Update parameters together** - changing one optional feature may require updating related assertions

**Common optional workflow features**:
- Quality trimming/filtering
- Duplicate removal
- Adapter trimming
- Optional annotations
- Different algorithm choices

When updating test configurations after workflow changes, review all optional parameters and verify assertions match the enabled features.

---

## Synthetic Test Data Generation

For workflow testing, synthetic data should include realistic biological features while remaining compact.

### Example: Assembly with Telomeres, Gaps, and Genes

```python
import random
random.seed(42)  # Reproducibility

def generate_scaffold(name, length, add_telomeres=False):
    """Generate scaffold with gaps, genes, and optional telomeres"""
    seq = []

    # P-arm telomere (10kb)
    if add_telomeres:
        seq.append("CCCTAA" * 1666)  # ~10kb

    # Main sequence with gaps and genes
    remaining = length
    while remaining > 0:
        # Add random sequence
        chunk = min(50000, remaining)
        seq.append(''.join(random.choices('ACGT', k=chunk)))
        remaining -= chunk

        # Add assembly gap every 150kb
        if remaining > 0 and random.random() < 0.3:
            seq.append('N' * 200)
            remaining -= 200

    # Q-arm telomere (12kb)
    if add_telomeres:
        seq.append("CCCTAA" * 2000)  # ~12kb

    return f">{name}\n" + ''.join(seq)
```

### Key Features to Include

- **Telomeres**: Canonical repeats (TTAGGG/CCCTAA for vertebrates). Must be ≥2kb (≥334 copies × 6bp) for teloscope detection — its default `min_block_length` is 500bp and `window` is 1000bp, so 300bp telomeres will NOT be detected.
- **Assembly gaps**: 200bp N-sequences
- **Gene-like sequences**: ATG start + coding + stop codon (TAA/TAG/TGA)
- **Coverage gaps**: Regions with zero read coverage
- **Duplicates**: For paired-end data (10-15% duplication rate)

### Data Sizes for Testing

| Data Type | Minimal | Typical | Full |
|-----------|---------|---------|------|
| Assembly | 1-2 MB | 5-10 MB | 50+ MB |
| HiFi Reads | 500-1000 reads | 5,000 reads | 50,000+ |
| Hi-C Pairs | 10K pairs | 50K pairs | 1M+ pairs |

Minimal datasets enable fast CI/CD testing (~30-60 min runtime).

#### PretextView AGP v2.1 Format

Used by post-curation workflows. 11 tab-separated columns:

| Cols 1-5 | Standard AGP | object, object_beg, object_end, part_number, component_type |
|----------|-------------|-------------------------------------------------------------|
| Cols 6-9 | Standard AGP | component_id/gap_length, component_beg/gap_type, component_end/linkage, orientation/evidence |
| Col 10 | `Painted` | Literal string "Painted" |
| Col 11 | Haplotype | `Hap_1`, `Hap_2`, `Z`, `W`, `Unloc`, `Haplotig` |

Gap lines also carry all 11 columns.

#### Test Data for Rename/Reorient Workflows

To exercise mashmap-based rename/reorient:
- Hap2 autosomes must be ≥50kb (mashmap seqLength threshold)
- Derive hap2 from hap1 with ~5% SNPs (>90% identity for alignment)
- Make hap2 scaffolds different sizes than hap1 homologs so size-based chromosome assignment produces mismatches
- Reverse complement one hap2 scaffold to trigger inversion detection
- Include sex chromosomes (Z/W) and small scaffolds (Unloc, Haplotig) for label handling

---

## Running Planemo Tests on Remote Galaxy Instances

### Best Practice: Always Prefer Live Instances

**IMPORTANT: Always test against live Galaxy instances** instead of spinning up local Galaxy:

```bash
# PREFERRED: Test against live instance
planemo test --fail_fast \
  --galaxy_url https://vgp.usegalaxy.org \
  --galaxy_user_key "$TESTKEY" \
  workflow.ga

# AVOID: Local Galaxy (slow, dependency issues)
planemo test --fail_fast workflow.ga
```

> **IMPORTANT**: Always use `$TESTKEY` for testing, NOT `$MAINKEY`. `$MAINKEY` is an admin key that can see and modify ALL users' data on the server. Using it for testing risks accidental interference with other users' work.

**Why live instances are superior:**
- **Much faster**: No Galaxy setup time (saves 5-10 minutes per test)
- **More reliable**: Dependencies already installed on production instance
- **Tests real environment**: Validates against actual production setup
- **Less resource intensive**: No local Docker/Galaxy overhead
- **Correct tool versions**: Production servers have the exact versions users will use

**Common live instances for VGP workflows:**
- VGP workflows: `https://vgp.usegalaxy.org` with `$TESTKEY` (use `$MAINKEY` only for admin tasks)
- General workflows: `https://usegalaxy.org` or `https://usegalaxy.eu`

**When to use local Galaxy:**
- Testing unreleased tools not yet on public instances
- Testing tool wrapper changes before deployment
- Debugging Galaxy configuration issues
- Network/connectivity issues prevent remote access

**Test duration expectations:**
- Complex workflows (80+ steps): 30-60 minutes on live server
- Simple workflows (<20 steps): 5-15 minutes on live server
- Local Galaxy: Add 5-10 minutes for setup time

### Command Structure

```bash
planemo test --galaxy_url https://galaxy.instance.org --galaxy_user_key $API_KEY workflow.ga
```

**Key flags**:
- `--galaxy_url`: The remote Galaxy instance URL
- `--galaxy_user_key`: User API key (NOT `--api_key` or `--galaxy_api_key`)
- `--galaxy_admin_key`: Admin key (for admin operations)
- `--timeout`: Optional timeout in milliseconds (default 120000, max 600000)
- `--check_uploads_ok`: Verify uploads succeed (**always use** for workflow tests)
- `--simultaneous_uploads`: Upload test datasets in parallel (**always use** for workflow tests)
- `--no_shed_install`: Skip tool installation when testing on a server that already has the tools
- `--fail_fast`: Stop on first job failure (recommended for workflow updates)
- `--failed`: Re-run only failed tests (requires tool_test_output.json from previous run)

**When to use --fail_fast**:
- **Workflow updates** (existing workflow being modified): Use `--fail_fast` by default to save time
  ```bash
  planemo test --fail_fast --galaxy_url ... --galaxy_user_key $KEY workflow.ga
  ```
- **New workflows** (first time testing): Ask the user if they want to use `--fail_fast`
  - Without `--fail_fast`: All tests run to completion, showing all failures
  - With `--fail_fast`: Stops at first failure, faster feedback but incomplete results

**Re-running failed tests**:
After a test run completes with failures, **ask the user** if they want to re-run only the failed tests:
- **Yes (--failed)**: Re-runs only failed tests, faster iteration
  ```bash
  planemo test --failed --galaxy_url ... --galaxy_user_key $KEY workflow.ga
  ```
- **No**: User may want to fix issues first, review logs, or run all tests again

**Running in background**:
For long-running tests, capture the shell ID and check later:
```bash
planemo test --galaxy_url ... --galaxy_user_key $KEY workflow.ga &
# Note the shell ID, then check with:
# jobs or fg
```

### Monitoring Test Progress

**Best Practice: Don't spam-check test status.** Instead:

1. **Check once** after starting the test
2. **Report last check timestamp** and current status to the user
3. **Recommend specific wait time** based on:
   - Workflow complexity (number of steps/jobs)
   - Test phase (execution vs. output collection)
   - Instance type (live vs. local)

**Example status report**:
```
Last check: 2026-02-16T18:34:25Z
Status: Workflow complete (61/61 jobs), collecting outputs (9 test cases)
Recommendation: Check again in 2-3 minutes

Typical phases and durations:
- Workflow execution: 5-15 minutes (depends on workflow complexity)
- Output collection: 2-5 minutes (depends on file sizes and network)
- Local Galaxy startup: Add 5-10 minutes to total time
```

**Caveat: planemo's rich progress bars don't write to log files.** When planemo's stdout is redirected (`tee /tmp/log` or background bash), the rich `Invocation <id>` progress panels render once and stop updating in the file. The process is still running and polling Galaxy normally — only the log appears stuck.

To monitor live during a long test, query Galaxy's API directly:

1. Find the active history: `GET /api/histories?user_id={me} | sort by update_time desc | head -1`
2. Get the top-level invocation: `GET /api/invocations?history_id={hid}` — the **earliest** create_time is the top-level invocation (planemo creates a fresh history per test, then nested subworkflows produce many sub-invocations sharing the same history).
3. Poll `GET /api/invocations/{id}/jobs_summary` for state counts (`ok`, `error`, `running`, `new`, `queued`, `skipped`).

### Re-testing Against an Existing Invocation

To re-run test assertions against a completed invocation without re-executing the workflow:

```bash
planemo workflow_test_on_invocation \
  --galaxy_url "$GXYVGP" \
  --galaxy_user_key "$TESTKEY" \
  WORKFLOW-tests.yml INVOCATION_ID
```

> **Important**: The first argument is the **test YAML file** (not the .ga workflow file). Using the .ga file causes a confusing error about "file must contain a list of tests".

This is useful when:
- A test fails on output assertions only (all jobs succeeded)
- You've updated the test YAML and want to validate without re-running
- Debugging assertion values (size, text, line counts)

**IMPORTANT:** When a workflow invocation succeeds but test assertions fail, ALWAYS use `workflow_test_on_invocation` to iterate on the test YAML instead of re-running the full `planemo test`. This saves the entire workflow execution time (often 15-30+ minutes). Extract the invocation ID from planemo's progress bar (`Invocation <ID>`).

**Result semantics**: `workflow_test_on_invocation` tries every test in the YAML against the invocation and reports a single combined result (`num_tests: 1` in `tool_test_output.json`). Success = at least one test matched. Failure = **none** matched. The `output_problems` list usually shows assertions from the first/closest test, not necessarily the failing one — to know which test fails, inspect each test's parameter set against the invocation's `input_step_parameters`.

This means the command is best used to validate that an invocation matches a *specific* test's parameters, not as a catch-all check.

**Targeting a specific test in a multi-test YAML** — to validate only one test against the invocation, use `--test_index N` (1-based):

```bash
planemo workflow_test_on_invocation \
  --galaxy_url "$GXYVGP" --galaxy_user_key "$TESTKEY" \
  --test_index 2 \
  WORKFLOW-tests.yml INVOCATION_ID
```

The full `planemo test` log shows two invocation panels in order — match index by position: first panel = `--test_index 1`, second = `--test_index 2`, etc. Test 2 in a typical multi-read workflow has more jobs (e.g., 148 vs 135 in a hi-c run) which also helps identify which invocation maps to which test index.

### Planemo Timeout vs Actual Failure

When planemo exits with "at least one job is in [error] state", the workflow may still be running on Galaxy. Check the actual invocation state via MCP before assuming failure:

```bash
mcp__Galaxy__get_invocations(invocation_id="<ID>", view="element", step_details=True)
```

If the invocation state is `ready` (not `failed`), the workflow is still in progress and planemo simply timed out. Long-running subworkflows (Hi-C mapping, compleasm) commonly exceed planemo's patience.

**Tip:** Extract the invocation ID from planemo's progress bar (`Invocation <ID>`) for direct Galaxy API queries.

#### Recovering assertions when the planemo process dies

Killing planemo (ctrl-C, task stop, local crash) does **not** stop the workflow --
Galaxy keeps scheduling it. The local run collects no outputs and evaluates no
assertions, but none of that needs recomputing.

1. **Find the surviving invocation.** A run creates one invocation per subworkflow
   plus the top-level one, all with near-identical `create_time`. The top-level one
   is the one whose step count matches the workflow:

```bash
curl -s -H "x-api-key: $KEY" "$URL/api/invocations?limit=12" | python3 -c "
import json,sys
for i in json.load(sys.stdin): print(i['id'], i['state'])" | while read id st; do
  printf '  %-18s %-10s ' "$id" "$st"
  curl -s -H "x-api-key: $KEY" "$URL/api/invocations/$id" \
    | python3 -c "import json,sys; print('steps=%d' % len(json.load(sys.stdin).get('steps',[])))"
done
```

```
  9d99aa5b0c1bedc3   scheduled  steps=14     <- subworkflow
  5e922236ed39bd29   completed  steps=8      <- subworkflow
  04cf612c5d8081c4   ready      steps=62     <- top-level (workflow has 62 steps)
```

2. **Let it finish, then evaluate the test YAML against it** -- seconds, no recompute:

```bash
planemo workflow_test_on_invocation --galaxy_url "$URL" --galaxy_user_key "$KEY" \
  --test_index 1 --test_output_json /tmp/result.json \
  WORKFLOW-tests.yml <TOP_LEVEL_INVOCATION_ID>
```

This also recovers the real output values needed to calibrate assertions, which is
usually why the run mattered. Invocations persist for a long time -- one was still
queryable and usable for assertion evaluation nearly a month later.

**Always check for a surviving invocation before re-running a long workflow.**

### "unexpected_failure" Phantom Messages

A subworkflow invocation can return:
- `state: completed`
- `messages: [{"reason": "unexpected_failure", "details": null, "step_id": null}]`

…while every job and dataset is `ok`. Planemo flags this as a failed test even though the workflow produced correct outputs. Verify by checking actual dataset states:

```python
mcp__Galaxy__get_history_contents(history_id, visible=False)
# Filter for state != "ok" or job_state_summary.error/failed/paused > 0
```

If everything is clean, this is a Galaxy scheduler glitch — re-running usually clears it. Don't chase the workflow as if it has a real bug.

### Planemo Installation Fallbacks

If `planemo` is not found directly or in a conda env, try:
```bash
pipx run planemo <command>
```
This uses the pipx cache and doesn't require a dedicated environment.

### Verifying Tests via MCP When Planemo Fails

If `planemo workflow_test_on_invocation` gets stuck, use MCP to manually verify test assertions:

1. Connect to Galaxy: `mcp__Galaxy__connect(url, api_key)`
2. Get invocation details: `mcp__Galaxy__get_invocations(invocation_id, view="element", step_details=True)`
3. For each test output assertion, fetch the dataset:
   - `mcp__Galaxy__get_dataset_details(dataset_id, preview_lines=N)` for content checks
   - Check `metadata_data_lines` for `has_n_lines` assertions
   - Check `file_size` for `has_size` assertions
   - Check preview content for `has_text` assertions
4. Compare against the test YAML assertions manually

**How to check status** (when using background execution):
```bash
# For background jobs
BashOutput --bash_id <shell_id>

# Status will show one of:
# - running: Test still executing
# - success: All tests passed
# - failed: One or more tests failed
```

**Exit codes**:
- Exit 1: Linting warnings (workflow still structurally valid if "CHECK: Tests appear structurally correct")
- Exit 2: Command syntax error (wrong flags)
- Exit 0: All tests pass

---

## Common Planemo Lint Errors and Fixes

When running `planemo workflow_lint` or `planemo test`, errors are often related to test file configuration, not the workflow itself.

**IMPORTANT**: Never modify the workflow file (`.ga`) to fix test errors - only modify the test file (`.yml`).

### Input Parameter Name Mismatches

**Error Pattern**:
```
ERROR: Non-optional input has no value specified in workflow test job [Input Name]
WARNING: Unknown workflow input in test job definition [Input Name], workflow inputs are [['Other Name ', ...]]
```

**Cause**: The workflow input has a trailing space (or other whitespace) that doesn't match the test file key.

**Fix**: Quote the key name in the test YAML file to preserve exact spacing:
```yaml
# Instead of:
Remove adapters from HiFi reads?: false

# Use (note the space before closing quote):
"Remove adapters from HiFi reads? ": false
```

**How to identify**: Look carefully at the error message - it shows both what you provided and what the workflow expects. Compare character-by-character including spaces.

### Test File Syntax Errors

**Error Pattern**: YAML parsing errors or unexpected behavior

**Common typos**:
- `ppath` instead of `path`
- Missing colons or incorrect indentation
- Unquoted strings with special characters

**Fix**: Carefully review the test file line-by-line. Use a YAML validator if needed.

### Output Label Mismatches Between Workflow and Test File

**Error Pattern**:
```
ERROR: Test found for unknown workflow output [Old Label], workflow outputs [['New Label', ...]]
```

**Cause**: A workflow output was renamed (e.g., during tool replacement or restructuring) but the test file still uses the old label.

**Fix**: Update the output key in the `-tests.yml` file to match the new workflow output label exactly:
```yaml
# Old (broken):
    Hi-C alignments stats multiqc:
      asserts:
        - has_text: ...

# New (fixed):
    Hi-C alignments on Scaffolds stats multiqc:
      asserts:
        - has_text: ...
```

**When this happens**: Commonly after replacing tools (e.g., MarkDuplicates -> samtools markdup) which changes output labels, or after renaming outputs for clarity.

**Detection**: Always run `planemo workflow_lint --iwc .` after workflow changes and before testing.

### Re-exported Workflows Reset IWC Transformations

**Problem**: When a workflow is modified in Galaxy and re-exported to a `.ga` file, the following IWC transformations are lost:
- `"release"` field is removed
- Runtime parameter descriptions (`"description": "runtime parameter..."`) reappear
- The `"readme"` field may be cleared or outdated

**Solution**: Always re-run `/prepare-for-iwc` after re-exporting a workflow from Galaxy. The command will re-apply all transformations and detect any new inputs/outputs that need documenting in README and CHANGELOG.

**Tip**: If the workflow was modified during testing (e.g., adding a new optional input), the re-exported `.ga` may also have renumbered steps. This is normal -- the preparation command handles it.

**Tip**: During an active debug-fix-test loop on a workflow, expect to run `/prepare-for-iwc` *multiple times* — once after each Galaxy re-export. The transformations are cosmetic for IWC submission and don't affect workflow behavior, so they don't need to be in place during testing — only at submission time.

**Watch for input *type* changes (not just label changes)**: a re-export can keep an input's label the same but change its `type` (e.g., `data_input` ↔ `data_collection_input`, or `collection_type: list` ↔ `list:paired`). Label-only diffing misses this. When comparing against `main`, also compare `step['type']` and `tool_state['collection_type']`/`tool_state['format']` — a type change requires updating both `-tests.yml` (`class: File` ↔ `class: Collection`) and the README description.

---

### Release / CHANGELOG mismatch

```
.. ERROR: The release of workflow ./NAME.ga does not match the version in the CHANGELOG.
```

`workflow_lint --iwc` compares the `.ga` `release` field against the topmost `## [x.y.z]` heading
in `CHANGELOG.md`. Bumping one without the other fails the lint. Add the entry as:

```markdown
## [0.10.6] - 2026-09-21

### Fixes
- <what changed and why>
```

Note this error is easy to miss: `workflow_lint` prints dozens of `WARNING: step has no label`
lines, so filter before reading -- `planemo workflow_lint --iwc . 2>&1 | grep -E 'ERROR|CHECK:'`.

---

## Interpreting Planemo Lint Output

Planemo lint shows three categories of messages:

**WARNINGS** (exit code 1):
- Missing annotations, labels on workflow steps
- Disconnected inputs (conditional inputs that may not be used)
- These are quality-of-life issues, not blocking errors
- Workflow is still valid if final checks pass

**ERRORS** (exit code 1):
- Test file configuration issues
- Missing required inputs in test jobs
- Input name mismatches
- Must be fixed before tests will run

**CHECKS** (exit code depends on context):
```
.. CHECK: Tests appear structurally correct for workflow.ga
.. CHECK: All tool ids appear to be valid.
```
- These indicate the workflow structure is valid
- If you see both CHECKs after warnings/errors, the workflow file itself is fine
- Focus on fixing ERROR messages in the test file

**Workflow is ready to test when**:
- Both CHECK messages appear
- No ERROR messages (or all errors fixed)
- Warnings about annotations/labels are acceptable

### Baseline lint against main

To check whether a warning is new, lint the `main` version in a scratch directory.
Copy all of these files, otherwise the lint reports missing-file ERRORs:

```bash
D=<scratchpad>/mainlint; mkdir -p $D
for f in Wf.ga Wf-tests.yml README.md CHANGELOG.md .dockstore.yml; do
  git show main:<workflow-dir>/$f > $D/$f
done
planemo workflow_lint --iwc $D 2>&1 | grep -E 'ERROR|disconnected'
```

`Input X of workflow step <annotation text> is disconnected` can appear for inputs
that are wired. If the same warning shows up on `main`, it was already there and is
not a regression.

---

## Writing Behavioral Assertions

Test assertions should verify that the workflow performs its intended biological logic, not just that outputs exist with the right size. Structure assertions in tiers:

### Tier 1: Verify core logic happened
- **Rename/reorient**: Check for `RENAME` and `RVCP` in instruction outputs
- **Chromosome assignment**: Verify correct count (`has_n_lines`) and sex chromosomes (`SUPER_Z`, `SUPER_W`)
- **Alignment**: Check for `cis` contacts in Hi-C stats
- **Empty-is-good**: `has_size: value: 0` for outputs like "sequences missing in mashmap"

### Tier 2: Verify biological features detected
- **Telomeres**: Check `Total telomeres:` count, `Two telomeres:` and `One telomere:` counts
- **Orientation**: Check for `+` and `-` in orientation mapping (detects inversions)
- **Gaps**: Verify gap count matches test data design

### Tier 3: Sanity checks
- **File sizes**: Use generous deltas (+/-50%) for FASTA/BAM/binary files
- **Text markers**: `has_text` for scaffold names, chromosome labels

### Test Data Design for Behavioral Testing

Design test data so that specific features are guaranteed to be exercised:
- Include at least one reverse-complemented scaffold to trigger inversion detection
- Make hap2 scaffold sizes differ from hap1 to force chromosome renaming
- Include telomeric repeats ≥2kb for teloscope detection (`min_block_length: 500bp` default)
- Include ~10% duplicate Hi-C reads for dedup testing
- Leave a coverage gap for coverage track testing

### Testing functional parameter changes

When a workflow changes a tool parameter that alters output behavior (not just version bumps), add an assertion that verifies the **effect** of the change, not just that the step completed.

Example: Changing samtools markdup from `remove: false` to `remove: true`:
- **Weak test**: Assert markdup stats show duplicates detected (`total_dups: 1327`) — this passes with BOTH settings
- **Strong test**: Assert the output BAM file size decreased, confirming reads were actually removed

Always trace the workflow connections to understand which output reflects the change:
1. Find the step with the parameter change
2. Identify which downstream outputs are affected
3. Add assertions on those specific outputs

**Pattern: regex backreferences for relational assertions**

When the regression criterion is a *relationship* between two numbers in a stats file (rather than absolute values), `has_text_matching` with a backreference is robust and read-count agnostic:

```yaml
# Assert duplicates were KEPT (samtools markdup ran without -r):
Hi-C duplication stats on Scaffolds:
  asserts:
    - has_text_matching:
        expression: "READ: (\\d+)\\nWRITTEN: \\1\\b"   # WRITTEN == READ

# Assert duplicates were REMOVED (samtools markdup ran with -r):
Hi-C duplication stats on Scaffolds:
  asserts:
    - has_text_matching:
        expression: "READ: (\\d+)\\nWRITTEN: (?!\\1\\b)\\d+"   # WRITTEN ≠ READ
```

The backreference `\1` captures READ's value; the negative lookahead `(?!\1\b)` requires a different number. This survives changes in test data size — only the boolean behavior is locked in. Use this pattern for any "X was/wasn't applied" regression where stats expose before/after counts.

---

## Placeholder Assertions for New Outputs

When adding test assertions for **new** workflow outputs (outputs you haven't yet seen real values for), use a placeholder that is **guaranteed to fail** on the first test run. This forces you to come back and replace it with a real assertion once the test has produced actual output — silent passes on weak assertions hide real bugs.

**Pattern**: `has_text` with an actual short Terry Pratchett quote as the search string. A real quote will (almost certainly) not appear in real bioinformatics output, so the assertion fails loudly, and the unusual prose makes the placeholder easy to grep for later. Prefer a genuine quote over the bare `"GNU Terry Pratchett"` tag — it reads better in the test file and is just as distinctive.

```yaml
# Placeholder — REPLACE after first test run with a real assertion
New Output:
  asserts:
    has_text:
      text: "Real stupidity beats artificial intelligence every time."  # placeholder, must be replaced
```

Any short Pratchett quote works (e.g. `"Real stupidity beats artificial intelligence every time."`, `"In the beginning there was nothing, which exploded."`). Pick one and stay consistent across the test file so a single `grep -n` for that quote reveals every placeholder still pending.

**Workflow**:
1. Add the new output with the placeholder assertion
2. Run the test — the placeholder assertion fails, but Galaxy produces the real output
3. Inspect the output via the Galaxy UI (size, content, key markers)
4. Replace the placeholder with a real assertion (`has_size`, `has_text` for a real marker, etc.)
5. Run `workflow_test_on_invocation` against the existing invocation to confirm — the workflow hasn't changed, only the tests, so there's no need to re-execute it

**Why not just omit the assertion?** An output with no assertion is silently accepted (planemo only checks output existence), so you may forget it ever needed validation. A failing placeholder is a tripwire that survives until you've actually looked at the data.

**Before merging**: `grep -n '<the quote you chose>' *-tests.yml` should return nothing. Any hit is an un-replaced placeholder.

---

## Adjusting Test Assertions After Initial Runs

After running tests and seeing assertion failures, adjust expectations based on actual outputs:

### File Size Assertions
When `has_size` assertions fail, update based on actual values:

```yaml
# Before (failed):
BigWig Coverage:
  asserts:
    has_size:
      value: 60000
      delta: 30000

# After (adjusted to actual: 9011 bytes):
BigWig Coverage:
  asserts:
    has_size:
      value: 10000
      delta: 5000  # +/-50% tolerance
```

**Guidelines for size assertions**:
- Use **+/-50% delta** for binary files (BAM, BigWig, Pretext) - compression varies
- Use **+/-30% delta** for text files if content may vary slightly
- For multi-collection tests, scale expected sizes proportionally (e.g., 2x data ~ 2x file size)
- **FASTA size vs sequence length:** A FASTA file with 260kb of sequence will be ~270kb on disk due to line wrapping (80 chars/line → extra newlines) plus header lines. Use generous `delta` values or run a first test to calibrate actual sizes. Don't estimate FASTA file sizes from sequence lengths alone.

**Re-baselining after job parameter changes**: When you change a test's `job:` parameters in a way that shifts data flow (e.g., toggling `Will you use a second haplotype?`, `Remove duplicated Hi-C reads?`, `Generate gene annotations`), expect *every* size assertion and many text-count assertions to need new values. Use `workflow_test_on_invocation` against the new run, then mine `tool_test_output.json`'s `output_problems` list for the actual values to plug in. Text-pattern assertions on scaffold names usually still pass; size-based and count-based ones rarely do.

### has_size delta must distinguish behavioral states

When `has_size` is used to verify a behavioral change (e.g., duplicates removed vs. only marked), ensure the delta is **smaller than the difference between the two possible outcomes**. Otherwise the test passes regardless of whether the change is actually applied.

Example: Verifying samtools markdup `remove: true` actually removes reads:
- Merged BAM (before dedup): 4,026,938 bytes
- Deduped BAM (after dedup): 3,759,316 bytes
- Difference: ~267,000 bytes

```yaml
# BAD: delta 500,000 accepts BOTH sizes — test is useless
Deduplicated Hi-C alignments on contigs:
  asserts:
  - has_size:
      value: 3759316
      delta: 500000

# GOOD: delta 100,000 only accepts the deduped size
Deduplicated Hi-C alignments on contigs:
  asserts:
  - has_size:
      value: 3759316
      delta: 100000
```

**Rule of thumb**: delta should be less than half the difference between the expected and incorrect values.

### Text Pattern Assertions
When `has_line` with exact patterns fails, simplify to `has_text`:

```yaml
# Too strict (failed):
Gaps Bed:
  asserts:
    has_text:
      text: "scaffold_10.H1"
    has_line:
      line: "scaffold_10.H1\t"  # Exact tab pattern
      n: 2

# Less strict (better):
Gaps Bed:
  asserts:
    has_text:
      text: "scaffold_10.H1"  # Just check presence
```

**Workflow**: Run test -> Check failures -> Adjust assertions -> Re-run with `--failed`

---

### Reference-database changes invalidate output assertions

Switching a BUSCO/compleasm database or lineage changes the marker set, so any
count-based assertion on its outputs becomes wrong:

```
v5 / vertebrata_odb10          ->  40388 and 40342 lines (hap1, hap2)
all-odb12-.../vertebrata_odb12 ->  72168 and 72168 lines
```

Leave the old values in place for the first run rather than loosening them: the
failure reports the exact new numbers, so you can set them precisely instead of
guessing a delta. Then re-verify with `workflow_test_on_invocation`.

**Watch for an assertion that stops discriminating.** Under odb10 the two
haplotypes gave different counts; under odb12 both are exactly `72168`. The test
still passes, but a value identical for both haplotypes no longer distinguishes
them -- likely counting the full marker set rather than per-assembly hits. A
passing assertion that cannot fail differently for different inputs is weaker than
it looks; prefer a `has_text` on the summary's completeness figures.

---

## Testing with Multiple Read Collections

### MarkDuplicates with Multiple Hi-C Datasets

**Problem**: When testing workflows with multiple Hi-C read sets in a collection (e.g., `list:paired`), Picard MarkDuplicates may fail with:

```
Exception in thread "main" htsjdk.samtools.SAMException:
Value was put into PairInfoMap more than once 3: RGread_3623
```

**Cause**: Test data files contain reads with identical names across different collection elements (e.g., `read_3623` appears in both `Hi-C_set_1` and `Hi-C_set_2`).

**Solution**: For tests with multiple read collections, disable MarkDuplicates:

```yaml
- doc: Test 2 - Multiple read sets with collections
  job:
    Hi-C reads:
      class: Collection
      collection_type: list:paired
      elements:
      - class: Collection
        identifier: Hi-C_set_1
        # ... multiple sets ...
    Remove duplicated Hi-C reads?: false  # Disable for multi-collection tests
```

**Best Practice**:
- **Test 1** (single collection): Enable MarkDuplicates to test the feature
- **Test 2** (multiple collections): Disable MarkDuplicates to avoid duplicate name conflicts

**Alternative**: Rename reads in test data files to ensure globally unique identifiers across all collection elements.

---

## Troubleshooting Tool Failures

When tests fail due to tool errors (not test configuration), the issue may be with the Galaxy tool wrapper itself.

### Workflow `state=failed`: Three Failure Modes

When an invocation's `state` is `failed`, the cause is at one of three levels — each surfaces differently and requires a different fix:

**1. Job-level failure** — a tool job errored
- `jobs_summary.states.error > 0` for the invocation (or any sub-invocation)
- Fetch `/api/jobs/{job_id}?full=true` and read `tool_stderr`
- For workflows with subworkflows, errors are often hidden inside; walk recursively:
  ```python
  inv = get(f'/api/invocations/{inv_id}?step_details=true')
  for s in inv['steps']:
      if s.get('subworkflow_invocation_id'):
          # recurse into sub-invocation's jobs_summary, then jobs API
  ```

**2. Workflow scheduling-level failure** — `messages` field contains the error
- `jobs_summary.states.error == 0` (all jobs green) but the invocation is `failed`
- `GET /api/invocations/{id}` → check the `messages` array
- Common reason: `expression_evaluation_failed` — a `when:` conditional or expression-tool in the workflow couldn't be evaluated. The `workflow_step_id` and `workflow_step_index_path` fields point to the offending step.
- Fix is in workflow design (typically conditional gating or `pick_value` plumbing), not the data.

**3. Invoke-time failure** — workflow never started
- `bioblend.ConnectionError: Unexpected HTTP status code: 400: {"err_msg":"Workflow was not invoked; the following required tools are not installed: <tool_id> (version <X>)..."}`
- The required tool revision isn't installed on the target Galaxy server. Either revert workflow to an installed revision or request the install.
- Visible in planemo's stderr but not in the Galaxy invocation API (no invocation was created).

### Tool Wrapper Argument Errors

**Symptom**: Test fails with error like `Error: Got unexpected extra argument (path/to/file)`

**Common Causes**:
1. **Tool wrapper bug**: The Galaxy tool wrapper is incorrectly constructing command-line arguments
2. **Version mismatch**: Different galaxy versions of the same tool (e.g., `1.1.3+galaxy3` vs `1.1.3+galaxy6`) may have different bugs
3. **Server-side issue**: Tool may work locally but fail on remote Galaxy server

**Diagnosis Steps**:
```bash
# 1. Check the error file for exact command that failed
cat error_tool_*.txt

# 2. Identify which tool version is used in subworkflow
grep -A 5 "tool_id.*tool_name" workflow.ga

# 3. Check if workflow uses multiple versions of same tool
grep "tool_name" workflow.ga | sort | uniq -c
```

**Resolution**:
- Update workflow to use a newer/fixed version of the tool
- Check Galaxy tool shed for changelog or bug reports
- If affecting production server, contact Galaxy administrators
- Consider testing on different Galaxy instance to isolate issue

**Example**: pairtools_parse tool had argument handling bug in galaxy3/galaxy6 versions that was fixed in later releases.

### gfastats Empty FASTA Output from Hifiasm GFA

**Symptom**: gfastats produces 0-byte fasta when converting hifiasm GFA, but GFA-to-GFA conversion works fine. Assembly summary shows `# scaffolds: 0`.

**Cause**: Hifiasm GFA files contain S (segment) and A (alignment) records but no W (walk) or P (path) lines. gfastats produces fasta by iterating over paths -- without `--discover-paths`, the path list is empty.

**Fix**: Ensure `discover_paths: true` is set in the gfastats `tool_state` at the `mode_condition` level (for `galaxy0` wrapper) or in `output_condition` (for `galaxy1` wrapper).

**Note**: gfastats `1.3.11+galaxy1` has a bug where `--discover-paths` was moved inside a GFA-only conditional, making it unavailable for fasta output. Use `1.3.11+galaxy0` until fixed. See [bgruening/galaxytools#1760](https://github.com/bgruening/galaxytools/pull/1760).

## Workflow Reports

Galaxy workflows support embedded reports using special markdown syntax. Add a `"report"` field to the .ga JSON:

```json
"report": {
    "markdown": "# Report Title\n\n```galaxy\nhistory_dataset_as_table(output=\"Output Label\")\n```\n"
}
```

### Report Display Functions

| Function | Use for |
|----------|---------|
| `history_dataset_as_table(output="Label")` | Tabular data (stats, mappings) |
| `history_dataset_as_image(output="Label")` | Images (Pretext snapshots, plots) |
| `history_dataset_embedded(output="Label")` | Text/HTML content (telomere reports, assembly info, **MultiQC HTML reports**) |
| `history_dataset_peek(output="Label")` | Quick preview of dataset |
| `workflow_display()` | Show workflow diagram |
| `invocation_inputs()` | List all inputs |
| `invocation_outputs()` | List all outputs |

The `output=` value must exactly match a workflow output label. Store the report as a separate `.md` file during development, then embed in the `.ga` file for submission.

## Troubleshooting

### Stale stored workflow on live Galaxy

Symptom: `planemo test` keeps returning an old error message (e.g. an old validator message) that doesn't match the current `.ga` file even after editing the workflow.

Cause: each `planemo test` run uploads the workflow under its `name`. If a previously-uploaded workflow with the same name exists on the Galaxy instance, Galaxy may keep using the older stored version. Changing the `uuid` alone does not always force a fresh upload.

Fix: delete the stale stored workflow on Galaxy before re-running:

```bash
# Find the stored workflow
curl -sS -H "x-api-key: $TESTKEY" "$GXY/api/workflows?show_published=false" \
  | python3 -c "import json,sys; [print(w['id'], w['name']) for w in json.load(sys.stdin) if w['name']=='My Workflow Name']"

# Delete it (permanent)
curl -sS -X DELETE -H "x-api-key: $TESTKEY" "$GXY/api/workflows/<id>"
```

Then re-run `planemo test`. The error message that comes back is the authoritative signal — if Galaxy still serves the old message after deletion, suspect tool_state caching at the tool level (a separate problem).

### Stale `tool_test_output.json` after `workflow_test_on_invocation`

`planemo test` writes `tool_test_output.json` into the workflow directory.
`workflow_test_on_invocation` **does not** -- it leaves the old file untouched.

Reading it after a re-verify therefore reports the *previous* run's failures, making a fix look
ineffective. The tell: identical `/var/folders/.../tmpXXXX/` paths across both runs, and an
`mtime` older than the run you just did.

**Always pass an explicit output path when re-verifying:**

```bash
planemo workflow_test_on_invocation \
  --galaxy_url "$GXY" --galaxy_user_key "$KEY" \
  --test_index 1 \
  --test_output_json /tmp/reverify.json \
  WORKFLOW-tests.yml INVOCATION_ID

python3 -c "
import json; d=json.load(open('/tmp/reverify.json'))
for t in d['tests']:
    print(t['data']['status'])
    for p in t['data'].get('output_problems') or []: print(' ', p)"
```

Sanity check before trusting any `tool_test_output.json`:
```bash
stat -f '%Sm %N' -t '%F %T' tool_test_output.json; date '+%F %T  (now)'
```

### Transient network errors are not workflow errors

Both `workflow_lint` and `planemo test` make many ToolShed/Galaxy calls and surface failures as
`ERROR:` lines:

```
.. ERROR: The ToolShed returned an error when searching for the most recent version of
   .../gfastats/1.3.11+galaxy1: ('Connection aborted.', ConnectionResetError(54, ...))
requests.exceptions.ChunkedEncodingError: ('Connection broken: IncompleteRead(442026 bytes read...
```

**Always re-run once before acting.** These clear on retry; a genuine lint error (schema, missing
label, release/CHANGELOG mismatch) reproduces every time.

Distinguishing tell: real lint errors name a workflow property; transient ones name a
`requests`/`bioblend` exception or a host.

An upload-phase `ConnectionResetError` can also mean the API key is wrong for that instance --
if retrying fails identically, confirm the key matches the `--galaxy_url` before assuming network.

### Debugging planemo failures via direct API

When `planemo test` fails with an opaque error and verbose logs aren't enough, bypass planemo and exercise the workflow directly with curl. This isolates whether the bug is in the workflow, in planemo's input mapping, or in Galaxy's caching.

```bash
# 1. Upload the local .ga as a fresh workflow
WFID=$(curl -sS -X POST -H "x-api-key: $TESTKEY" -H "Content-Type: application/json" \
  -d @<(python3 -c "import json; print(json.dumps({'workflow': json.load(open('workflow.ga'))}))") \
  "$GXY/api/workflows" | python3 -c "import json,sys; print(json.load(sys.stdin)['id'])")

# 2. Make a history
HID=$(curl -sS -X POST -H "x-api-key: $TESTKEY" -H "Content-Type: application/json" \
  -d '{"name":"debug"}' "$GXY/api/histories" | python3 -c "import json,sys; print(json.load(sys.stdin)['id'])")

# 3. Invoke with inputs_by=name and only the params you want to control
curl -sS -X POST -H "x-api-key: $TESTKEY" -H "Content-Type: application/json" \
  -d "{\"history_id\":\"$HID\",\"inputs_by\":\"name\",\"inputs\":{\"My Param\":\"value\"}}" \
  "$GXY/api/workflows/$WFID/invocations"
```

How to read the result:
- **HTTP 400 with a parameter-validator message** — Galaxy received your value and rejected it at validation. Fix the value or relax the validator.
- **HTTP 200 followed by `state: failed` on invocation poll** — scheduling succeeded but a tool job died. Inspect the job's stderr via `/api/jobs/<id>?full=True`.
- **HTTP 200 followed by `state: scheduled` for all steps and `messages: [{reason: unexpected_failure, ...}]`** — Galaxy hit an internal error scheduling a specific step. The step that's stuck in state `new` is usually the culprit.

Clean up afterwards: `curl -X DELETE -H "x-api-key: $TESTKEY" "$GXY/api/workflows/$WFID"` and the corresponding history.
