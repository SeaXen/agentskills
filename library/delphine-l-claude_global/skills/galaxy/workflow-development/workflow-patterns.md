# Workflow Patterns and Tool Management

Common workflow patterns, tool version migration, ToolShed API usage, and writing methods sections for publications.

## Common Workflow Patterns

### Pattern 1: Data Fetching
```
Input: Accession list
|
Tool: Fetch data (e.g., fasterq-dump)
|
Tool: Quality control (e.g., FastQC)
|
Output: Raw reads + QC report
```

### Pattern 2: Read Processing
```
Input: FASTQ files
|
Tool: Quality trimming
|
Tool: Alignment/Mapping
|
Tool: Post-processing
|
Output: Processed data + statistics
```

### Pattern 3: Analysis Pipeline
```
Input: Processed data + reference
|
Tool: Primary analysis (e.g., variant calling, quantification)
|
Tool: Filtering/Normalization
|
Tool: Visualization
|
Output: Results + plots + reports
```

---

## Tool Version Migration in .ga Files

When updating a tool to a newer version in an existing .ga workflow, ALL of these fields must be updated for each affected step:

1. **`content_id`**: Full toolshed path including version (e.g., `toolshed.g2.bx.psu.edu/repos/owner/tool/tool_id/1.4.2+galaxy0`)
2. **`tool_id`**: Same as content_id for toolshed tools
3. **`tool_version`**: Version string (e.g., `1.4.2+galaxy0`)
4. **`tool_shed_repository.changeset_revision`**: Galaxy wrapper revision hash -- look up via `get_tool_details(tool_id)` on the Galaxy MCP
5. **`tool_state`**: JSON dict of parameters -- MUST match the new tool's parameter schema exactly

Use `replace_all` when a field (e.g., `changeset_revision`) appears identically in multiple steps using the same tool.

**Always validate JSON after editing:**
```bash
python3 -c "import json; json.load(open('workflow.ga'))"
```

### Check for an open planemo-autoupdate PR first

Before hand-editing tool versions, look for a bot PR against that workflow:

```bash
gh pr list --search "Updating workflows/<path>" --state open
gh pr view <N> --json title,headRefName,headRefOid,headRepositoryOwner,files
```

The bot opens one PR per workflow and bumps **everything** at once, so a manual
bump often duplicates work -- and both land on the same next release number, so
the two versions collide rather than stack.

**Fold rather than re-edit.** Take the bot's `.ga` as the base and re-apply your
manual fixes on top:

```bash
gh api "repos/planemo-autoupdate/galaxyproject_iwc/contents/<path>/<wf>.ga?ref=<headRefOid>" \
  --jq '.content' | base64 -d > bot.ga
```

#### Audit the bot's output -- it is not authoritative

Two real defects in one PR:

- **A removed parameter was left behind.** It bumped compleasm `0.2.6+galaxy3 ->
  0.2.9+galaxy0` but kept `"mode": "busco"` in `tool_state`, although `mode` was
  dropped upstream in 0.2.8. The bot updates versions; it does not re-derive
  `tool_state` against the new schema.
- **Its CHANGELOG was incomplete.** Two changeset-only updates
  (`map_param_value`, `datamash_ops` -- same version, new revision) were in the
  `.ga` but absent from the CHANGELOG it wrote.

So diff structurally rather than reading its CHANGELOG. Compare
`(tool_id, tool_version, changeset_revision, tool_state)` per step, recursing into
subworkflows, between your file and the bot's. Anything that differs is either a
fix of yours to preserve or a bot change to accept -- decide each one:

```
VER  15     minimap2   2.28+galaxy2 (539de907fd99) -> 2.31+galaxy1 (7a6382582d76)
STATE33     +['mode']                   <- bot re-added a removed param: keep yours
STATE44/3   ~['components']             <- your awk fix: keep yours
STATE32     ~['mode_condition']         <- gfastats relocation: take the bot's
```

After folding, re-run the same diff **against the bot's file**: the only
differences should be your deliberate fixes. Anything else leaked in.

The bot does handle schema relocations well -- it moved gfastats `discover_paths`
from `mode_condition.output_condition` back up to `mode_condition` across all 7
steps, including adding it where it had been absent. Do not assume it needs help
with those.

### Common tool_state Migration Patterns

**Flat parameter -> Conditional:**
```json
// Old: flat dropdown
"assembler": "spades"

// New: conditional with sub-options
"assembler_type": {"assembler": "spades", "__current_case__": 3, "plasmid": false}
```

**Removed parameters:** Delete from tool_state entirely. Do NOT leave old keys.

**New parameters:** Add with their default values. Check defaults via `get_tool_details(tool_id, io_details=True)`.

**Changed output types:** Update the step's `outputs` list (e.g., `"type": "txt"` -> `"type": "gfa1"` for Flye's assembly graph).

**Removed outputs:** Remove from both `outputs` and `workflow_outputs` arrays.

**Input type changes** (e.g., `data_collection` -> `data` with `multiple:true`): Collections still work as input at runtime but the schema is different in tool_state.

### Parameter Location Changes Between Wrapper Versions

When a wrapper update moves a parameter from one level to another in the tool XML, the `tool_state` in the .ga file retains the old location. Reverting the tool version then causes "No value found" warnings because the parameter is in a location the older wrapper doesn't expect.

**Example**: gfastats `1.3.11+galaxy1` moved `discover_paths` from `mode_condition` (top-level) into `output_condition` (GFA-only conditional). Reverting to `galaxy0` requires manually moving the parameter back:

```json
// galaxy1 format (wrong for galaxy0):
"output_condition": {"out_format": "gfa", "discover_paths": false}

// galaxy0 format (correct):
"mode_condition": {"discover_paths": true, "output_condition": {"out_format": "gfa"}}
```

**Always check**: After reverting a tool version, compare `tool_state` against the older wrapper's XML schema. Parameters may need to be relocated or added.

### When NOT to Update In-Place

Do NOT attempt in-place .ga file edits when:
- The tool has been **replaced by a completely different tool** (e.g., JBrowse 1.x -> JBrowse2 has different owner, ID, and interface)
- The tool has been **split into multiple tools** (e.g., monolithic Meryl -> 7 separate Meryl tools)

These require rebuilding the affected workflow steps from scratch.

---

## Galaxy Tool Version Audit with MCP

To check whether a workflow's tools are up to date on a Galaxy server:

1. **Extract tool IDs** from the .ga file (look for `tool_id` fields in each step)
2. **Search for current versions**: `search_tools_by_name("tool_name")` returns the latest installed version
3. **Compare versions**: Classify as same / wrapper-only / minor / major
4. **For major changes**: `get_tool_details(tool_id, io_details=True)` returns the full parameter schema. Compare against the `tool_state` in the .ga file to identify:
   - Parameters renamed or restructured
   - New required parameters
   - Removed outputs
   - Changed default values
5. **Get changeset_revision**: The `tool_shed_repository` section in `get_tool_details()` output provides the exact `changeset_revision` hash needed for the .ga file

---

### Empirical version triage from job history

Before assuming a version bump fixes a tool failure, ask the instance what actually happens:

```bash
for v in 0.2.6+galaxy3 0.2.9+galaxy0; do
  echo "=== $v ==="
  curl -s -H "x-api-key: $KEY" --get "$URL/api/jobs" \
    --data-urlencode "tool_id=toolshed.g2.bx.psu.edu/repos/iuc/compleasm/compleasm/$v" \
    --data-urlencode "limit=200" \
  | python3 -c "import json,sys,collections; print(collections.Counter(j['state'] for j in json.load(sys.stdin)))"
done
```

```
=== 0.2.6+galaxy3 ===  Counter({'error': 100, 'skipped': 75, 'ok': 1})
=== 0.2.9+galaxy0 ===  Counter({'ok': 154, 'error': 23})
```

That contrast settles it in one call. Especially valuable for failures caused by **upstream data
drift** rather than the workflow -- e.g. compleasm 0.2.6 crashing in `download_placement` because
BUSCO's `file_versions.tsv` gained entries its `strain.split(".")` can't parse. Such a pin is
permanently broken; no workflow edit helps.

Requires admin rights to see other users' jobs. Also check `versions` on the tool to see what the
instance actually has installed:
```bash
curl -s -H "x-api-key: $KEY" "$URL/api/tools/<url-encoded-tool-id>?io_details=true"
```
and diff the input schema before bumping -- parameters get removed (compleasm dropped `mode` in
0.2.8) and must be deleted from `tool_state`.

---

### Version currency and revision validity are different questions

A pin can name the newest version and still carry a changeset that the tool shed
no longer advertises as installable. A currency check (`pinned == latest`) reports
it as fine; IWC lint rejects it:

```
ERROR: The tool .../map_param_value/0.2.0 references changeset_revision
5ac8a4bf7a8d, which is not an installable revision of the repository.
```

This happened with `map_param_value 0.2.0` and `datamash_ops 1.9+galaxy0` -- both at
the latest version, both with superseded revisions, three failing occurrences in CI.
A version sweep printed `(pinned rev not in TS metadata)` for both and the rows were
still read as "current, no action". **That parenthetical was the defect.**

Never report a tool as OK on version match alone. Run the dedicated checker, which
validates consistency, installability, and that the revision ships the declared
version:

```bash
python3 .claude/skills/workflow-development/scripts/check_changesets.py WORKFLOW.ga
```

---

## ToolShed API for Tool Version Discovery

To find the latest version of a tool directly on the ToolShed (without needing a Galaxy server):

### 1. Get repository ID
```bash
curl -s "https://toolshed.g2.bx.psu.edu/api/repositories?name={tool_name}&owner={owner}"
# Returns JSON array, use [0]["id"] for the repo ID
```

### 2. Get all revisions with tool versions
```bash
curl -s "https://toolshed.g2.bx.psu.edu/api/repositories/{repo_id}/metadata"
# Keys are "N:changeset_hash" (e.g., "0:5799092ffdff", "1:2b8b4cacb83d")
# The LAST entry contains the latest version
# Each entry has: tools[].version, changeset_revision
```

### 3. Extract latest version info
```python
keys = list(metadata.keys())
latest = metadata[keys[-1]]
tool_version = latest["tools"][0]["version"]  # e.g., "1.3.11+galaxy1"
changeset = latest["changeset_revision"]       # e.g., "0fe699ced54f"
```

**Note**: The ToolShed metadata endpoint does NOT include tool input definitions. Use Galaxy MCP `get_tool_details(tool_id, io_details=True)` to compare inputs between versions.

---

## Tool Update Verification Checklist

After updating tool versions in a workflow, verify these potential issues:

1. **Default value contradictions**: New defaults may override explicit workflow settings (boolean flips, changed numeric values)
2. **Lost text/value inputs**: Enum options may have been removed; check `tool_state` values against new schema
3. **New required params without defaults**: Will cause tool failure if not configured
4. **Removed params still referenced**: Check both `tool_state` and `input_connections`
5. **Conditional/section restructuring**: Parameter paths may change (e.g., `param` -> `section|param`)
6. **Output changes**: Removed/renamed outputs break downstream step connections and `post_job_actions`

Use Galaxy MCP `get_tool_details(tool_id, io_details=True)` for both old and new versions to compare schemas systematically.

---

## Writing Methods Sections for Publications

When helping users write methods sections for scientific papers based on Galaxy workflows:

### 1. Workflow Analysis Strategy

**Quick metadata check:**
```bash
python3 -c "import json; wf=json.load(open('workflow.ga')); print(wf['name']); print(wf.get('annotation','')[:300])"
```

**For extracting complete tool inventories (including subworkflows):**

grep-based extraction misses tools inside nested subworkflows. Use Python's
recursive approach to capture the full dependency tree:

```python
import json

with open('workflow.ga') as f:
    wf = json.load(f)

seen = set()

def extract_tools(steps, indent=0):
    for step_id, step in sorted(steps.items(), key=lambda x: int(x[0])):
        if step.get('tool_id') and step['type'] == 'tool':
            tid = step['tool_id']
            ver = step.get('tool_version', '')
            key = f'{tid}:{ver}'
            if key not in seen:
                seen.add(key)
                print(f'{"  "*indent}{tid}  v{ver}')
        elif step.get('type') == 'subworkflow':
            swf = step.get('subworkflow', {})
            name = swf.get('name', step.get('label', ''))
            print(f'{"  "*indent}[SUBWORKFLOW] {name}')
            extract_tools(swf.get('steps', {}), indent+1)

extract_tools(wf['steps'])
```

**Why this matters**: Galaxy `.ga` files nest subworkflow definitions inline.
A `grep` for `tool_id` at the top level misses tools embedded 2-3 levels deep
in subworkflow JSON. VGP curation workflows typically have 5+ subworkflows
containing >20 additional tools not visible at the top level.

**For large workflows (>25000 tokens):**
- Don't read entire files - they'll exceed token limits
- Use the Python extraction above instead of reading the full file
- Read only first 100 lines for metadata: `head -100 workflow.ga`
- Search for tool patterns rather than reading everything

### 2. VGP Workflow Documentation Pattern

For VGP pipeline workflows, document in this order:

1. **Platform and pipeline**: "implemented in Galaxy (cite) using VGP workflows (cite)"
2. **Data-specific approach**: Distinguish trio vs non-trio methods
3. **Sequential workflow steps**:
   - K-mer profiling (Meryl, GenomeScope2)
   - Assembly (HiFiasm with appropriate mode)
   - Scaffolding (RagTag with reference)
   - Quality assessment (BUSCO/Compleasm, Merqury, gfastats)
4. **Tool versions**: Always include version numbers
5. **Specific parameters**: Reference genomes, accessions used

### 3. Methods Section Template

```markdown
Genome assemblies were generated using the [Pipeline Name] workflows (Citation)
implemented in Galaxy (Galaxy Community, 2024). For [condition A], we employed
[approach A]: first, [step 1] using [Tool v.X] (Citation), followed by [step 2]
using [Tool v.Y] (Citation). For [condition B], we performed [approach B]
using [Tool v.Z] (Citation). All assemblies were [post-processing step] using
[Tool] with [specific parameter/reference]. Assembly quality was assessed using
multiple metrics including [Tool A] for [metric type], [Tool B] for [metric type],
and [Tool C] for [metric type]. [Annotation or downstream analysis] was performed
using [Tool/Pipeline] (Citation), which [brief description]. [Specific data sources
with accessions].
```

### 4. Common VGP Workflow Tool Citations Needed

**Core tools to cite:**
- Galaxy platform: The Galaxy Community (2024)
- VGP workflows: Lariviere et al. (2024) Nature Biotechnology
- HiFiasm: Cheng et al. (2021) Nature Methods
- Meryl: Rhie et al. (2020) Genome Biology
- GenomeScope2: Ranallo-Benavidez et al. (2020) Nature Communications
- Merqury: Rhie et al. (2020) Genome Biology
- BUSCO: Manni et al. (2021) MBE
- Compleasm: Huang & Li (2023) Bioinformatics
- RagTag: Alonge et al. (2022) Genome Biology
- gfastats: Formenti et al. (2022) Bioinformatics
- EGApX: Thibaud-Nissen et al. (2013) NCBI Handbook

**Curation-specific tools to cite:**
- PretextMap/PretextView: Harry (2022) - Hi-C contact map visualization
- PretextGraph: Harry (2022) - Annotation track overlay
- Pretext Snapshot: Harry (2022) - Static map image generation
- BWA-MEM2: Vasimuddin et al. (2019) IPDPS - Hi-C read alignment
- pairtools: Open2C et al. (2024) PLoS Computational Biology - Hi-C contact parsing
- Teloscope: Formenti et al. (2024) - Telomere detection
- minimap2: Li (2018) Bioinformatics - Long-read alignment
- deepTools: Ramirez et al. (2016) NAR - Coverage analysis
- BEDTools: Quinlan & Hall (2010) Bioinformatics - Interval operations
- MashMap: Jain et al. (2018) Bioinformatics - Whole-genome alignment
- Cutadapt: Martin (2011) EMBnet.journal - Adapter trimming
- Samtools: Danecek et al. (2021) GigaScience - BAM/SAM manipulation
- MultiQC: Ewels et al. (2016) Bioinformatics - QC aggregation
- JBrowse2: Diesh et al. (2023) Genome Biology - Genome browser
- ImageMagick: ImageMagick Studio LLC

### 5. Key Information to Extract from Workflows

**From workflow annotation field:**
- Purpose and description
- Pipeline position (e.g., "Part of VGP suite, run after VGP1")

**From tool_id fields:**
- Primary assembler (hifiasm, flye, etc.)
- Scaffolding tool (ragtag, yahs, etc.)
- QC tools (busco, merqury, etc.)

**From inputs:**
- Data types required (HiFi, Hi-C, Illumina, trio data)
- Reference genome requirements
- RNA-seq accessions for annotation

**From parameters:**
- K-mer lengths
- Ploidy settings
- BUSCO lineages
- Coverage thresholds

### 6. Curation Workflow Methods Template

For VGP curation workflows, document in three phases:

1. **Pre-curation**: Hi-C map generation with annotation tracks
   - Hi-C alignment (BWA-MEM2, pairtools, dedup)
   - Long-read alignment and coverage (minimap2, deepTools)
   - Telomere detection (Teloscope)
   - Assembly statistics and gaps (gfastats)
   - Gene completeness (Compleasm, optional)
   - Pretext map generation with tracks (PretextMap, PretextGraph)

2. **Manual curation**: Brief description of PretextView usage
   - Distinguish dual vs single curation for phased assemblies
   - AGP export format

3. **Post-curation**: QC and haplotype processing
   - AGP application and haplotype splitting (VGP custom tools: vgp_split_agp, vgp_chromosome_assignment, vgp_sak_generation)
   - Haplotype reorientation (MashMap)
   - Per-haplotype re-evaluation (same modules as pre-curation)
   - Visualization (ImageMagick montages, JBrowse2)

4. **Reproducibility**: Workflow availability statement (Galaxy, IWC)

**Key distinction from assembly methods**: Curation methods describe the
same analytical modules applied twice (before and after curation) with
the curation step in between. Emphasize that post-curation uses identical
tools for direct comparability.

### 7. Workflow File Size Considerations

**Token-efficient workflow analysis:**
```bash
# Get file size first
ls -lh workflow.ga

# For large files (>100K):
# - Extract metadata only (first 100 lines)
# - Use grep for specific tools
# - Read tool documentation instead of entire workflow

# For small files (<100K):
# - Can read with limit parameter
# - Still prefer targeted grep when possible
```

## Galaxy Tag System in Workflows

### Tag Types in .ga Files

Galaxy has three tag types, but they use different syntax in `.ga` JSON vs the Galaxy UI:

| Galaxy UI | .ga JSON syntax | Behavior |
|-----------|----------------|----------|
| `#tagname` (inheritable) | `name:tagname` | Propagates to ALL downstream datasets |
| `name:tagname` (name tag) | `name:tagname` | Same syntax — `name:` in .ga = `#` in UI |
| `tagname` (regular) | `tagname` | Does NOT propagate |

**Critical**: In `.ga` files, `name:hap1` is the inheritable `#hap1` tag, not a regular tag.

### Post-Job Actions for Tags

```json
"TagDatasetAction": adds tags
"RemoveTagDatasetAction": removes inherited tags from a specific output
```

Example removal:
```json
"RemoveTagDatasetActionout_file1": {
    "action_arguments": { "tags": "name:hap1" },
    "action_type": "RemoveTagDatasetAction",
    "output_name": "out_file1"
}
```

### Tag Propagation Debugging

When an output has an unexpected inheritable tag:
1. Trace the data flow backward through `input_connections`
2. Find where `TagDatasetAction` with `name:tagname` is set
3. Follow ALL paths forward — the tag propagates through every tool that consumes the tagged dataset
4. Add `RemoveTagDatasetAction` on the step where the tag should stop propagating

Common pitfall: a tool that takes inputs from both haplotypes (e.g., mashmap comparing hap1 vs hap2) will inherit tags from BOTH inputs. Downstream datasets get both `#hap1` and `#hap2`.

### Dynamic Output Naming with Parameters

`RenameDatasetAction` supports `${parameter_name}` template syntax:
```json
"RenameDatasetActionout_file1": {
    "action_arguments": { "newname": "${Haplotype} Genes track" },
    "action_type": "RenameDatasetAction",
    "output_name": "out_file1"
}
```

This is useful for subworkflows that run on different haplotypes — pass a "Haplotype" parameter ("Hap1" or "Hap2") and use `${Haplotype}` in rename actions to prefix all output names. `TagDatasetAction` does NOT support this template syntax.

**Syntax distinction**: `${parameter_name}` references a workflow **text parameter** value. `#{input_name}` references an **input dataset** name. Using the wrong syntax silently produces empty strings. The `#{}` syntax was seen in the Scaffolding-HiC workflow for dataset names (`#{input}: (Sorted)`).

### Output Label Quality Audit

When workflows use `${Haplotype}` template renaming in subworkflows, the outer workflow's `workflow_outputs` labels are static strings that can drift from the intended naming. Common issues:

| Issue | Example | Fix |
|-------|---------|-----|
| Trailing whitespace | `"Mashmap Chrom level "` | Trim |
| Mixed hap in non-comparison output | `"Hap1 Pairtools...: Hap2"` | Should be `": Plots"` |
| Missing hap number | `"Hap Pairtools..."` | Should be `"Hap2 Pairtools..."` |

**Programmatic detection** (run during `/prepare-for-iwc`):
```python
for wo in step.get('workflow_outputs', []):
    label = wo.get('label', '')
    if label != label.strip():
        flag("trailing whitespace")
    if 'Hap1' in label and 'Hap2' in label and 'orientation' not in label.lower():
        flag("mixed hap labels")
    if label.startswith('Hap ') and not label.startswith('Hap1') and not label.startswith('Hap2'):
        flag("missing hap number")
```

## Tool Wrapper Quirks

### `tp_find_and_replace`: literal apostrophes get sanitized to `X`

The Galaxy wrapper for `toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_find_and_replace` substitutes literal `'` characters in the `replace_pattern` with `X` before invoking perl — apparently for shell-safety. The actual command line shows e.g. `'X,X'` where the workflow `tool_state` had `"','"`.

Symptom: a step intended to wrap CSV values in quotes (e.g. converting user input `Mammalia,Aves` into `Mammalia','Aves`) instead emits `MammaliaX,XAves`, breaking downstream filter expressions like `c6 in ['MammaliaX,XAves']`.

**Workaround**: set `is_regex: true` and use the hex escape `\x27` for apostrophes in the replacement. The wrapper sees no literal `'` so it passes the string through; perl in regex mode interprets `\x27` as the apostrophe character at runtime.

In `.ga` `tool_state`:

```json
{"find_pattern": ",", "replace_pattern": "\\x27,\\x27", "is_regex": true}
```


### `compose_text_param` -> `tp_awk_tool`: unbalanced quotes break only at runtime

When an awk program is built by `compose_text_param` and fed to `tp_awk_tool`'s `code` input,
nothing validates the assembled string. A misplaced quote in one static component yields a
program that fails at execution with no lint or editor warning.

**Real example** (VGP6 `Rename and unify fasta`). Components were:

| # | value |
|---|---|
| 0 | `{print $1"\t` |
| 1 | *(connected: "Type of Sequence")* |
| 2 | `"_"NR".`  <- stray leading `"` |
| 3 | *(connected: "Haplotype")* |
| 4 | `"}` |

With `contig` / `H2` that composes `{print $1"\tcontig"_"NR".H2"}` -- `"\tcontig"` closes the
string early, leaving a bare `.`:

```
awk: {print $1"\tcontig"_"NR".H2"}
awk:                         ^ syntax error
```

Component 2 should be `_"NR".`, giving `{print $1"\tcontig_"NR".H2"}`.

#### The test-masking trap

This bug shipped and stayed green in CI because the test YAML compensated **in the input value**:

```yaml
"What sequences are you purging?": contig"     # <-- stray quote balances the broken program
```

`contig"` makes the malformed program parse. Real users pass `contig` and the workflow dies.

> **Rule**: a test parameter value containing stray punctuation -- especially an unmatched quote --
> is a red flag, not a quirk. It usually means the test is bending the input to fit a broken
> workflow. Fix the workflow; make the test value natural.

When you fix such a program, **the test YAML must be fixed in the same commit** or the test starts
failing on the corrected workflow.

#### Detector

Syntax-check every awk program, reconstructing composed ones. Quote-parity alone works
(odd count of `"` in the static parts => a connected value must be supplying one), but
actually parsing is stronger:

```python
# For each tp_awk_tool step: if `code` is a ConnectedValue, follow input_connections['code']
# to the compose_text_param step, concatenate its static component_values, substitute a plain
# placeholder (e.g. "PARAMVALUE") for each ConnectedValue, then:
r = subprocess.run(['awk', prog], stdin=subprocess.DEVNULL, capture_output=True, text=True)
broken = 'syntax error' in r.stderr
```

Recurse into `subworkflow.steps` -- composed awk usually lives inside a subworkflow.
Validate the detector against a known-bad `.ga` (`git show HEAD:path`) before trusting a clean run.

Across the IWC repo this found 33 awk programs in 9 VGP workflows (only VGP6 and Post_Curation
compose from parameters at all) plus 8 genuinely broken ones in the amplicon MGnify workflows,
where the program is stored wrapped in literal single quotes.
