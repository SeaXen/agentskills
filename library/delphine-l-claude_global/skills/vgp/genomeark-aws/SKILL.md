---
name: genomeark-aws
description: Access and navigate GenomeArk AWS S3 bucket - VGP assemblies, QC data, and species directory structure
allowed-tools: Read, Grep, Glob, Bash
---

# GenomeArk AWS S3 Data Repository

Comprehensive guide for accessing and navigating the GenomeArk AWS S3 public bucket containing Vertebrate Genomes Project (VGP) assemblies and quality control data.

**Supporting files** (read as needed for detailed code and strategies):
- [assembly-date-extraction.md](./assembly-date-extraction.md) - Extract assembly dates from FASTA filenames, validation rules
- [qc-data-fetching.md](./qc-data-fetching.md) - GenomeScope, BUSCO, Merqury, Meryl fetching code and parsing
- [best-practices.md](./best-practices.md) - AWS CLI patterns, batch processing, common pitfalls, testing examples, version history

## When to Use This Skill

Use this skill when:
- Accessing VGP genome assemblies from GenomeArk AWS S3
- Fetching QC metrics (GenomeScope, BUSCO, Merqury) for genomic analyses
- Downloading genome evaluation data for comparative studies
- Accessing meryl k-mer histograms for GenomeScope analysis
- Building automated pipelines that fetch VGP data
- Troubleshooting S3 path issues or missing data
- Working with species-specific genome data from VGP

## Repository Overview

**GenomeArk** is a public AWS S3 bucket (`s3://genomeark/`) hosting:
- VGP genome assemblies (primary, alternate, trio)
- Quality control metrics (GenomeScope, BUSCO, Merqury)
- Intermediate files (meryl databases, k-mer histograms)
- Assembly evaluation reports
- Haplotype-resolved assemblies

**Access Method**: Public bucket requiring **no AWS credentials** when using `--no-sign-request`

**Critical Discovery**: GenomeArk structure has evolved over time (2022 -> 2024+). Always implement fallback path patterns for reliability.

## Directory Structure

### Base Structure

```
s3://genomeark/
└── species/
    └── {Genus_species}/          # e.g., Rhinolophus_ferrumequinum
        └── {ToLID}/               # e.g., mRhiFer1 (VGP specimen ID)
            ├── assembly_vgp_{type}_{version}/
            │   ├── evaluation/     # QC metrics (MAIN ACCESS POINT)
            │   │   ├── genomescope/
            │   │   ├── busco/
            │   │   ├── merqury/
            │   │   └── ...
            │   └── intermediates/  # K-mer databases, temp files
            │       └── meryl/
            └── genomic_data/      # Raw sequencing data folders
```

### Assembly Directory Variations

**assembly_vgp_{type}_{version}** - Standard VGP Patterns:
- `assembly_vgp_HiC_2.0` - Hi-C phased assembly (case-sensitive!)
- `assembly_vgp_standard_2.0` - Standard assembly without Hi-C
- `assembly_vgp_hic_2.0` - Alternative Hi-C naming
- `assembly_vgp_trio_2.0` - Trio-binned assembly

**Legacy Versions** (2019-2021 assemblies):
- `assembly_vgp_standard_1.6` - Version 1.6 (common in fish, birds)
- `assembly_vgp_standard_1.0` - Version 1.0 (early assemblies)
- `assembly_vgp_HiC_1.6` - Hi-C version 1.6
- `assembly_vgp_HiC_1.0` - Hi-C version 1.0
- `assembly_vgp_HiC_1.4` - Hi-C version 1.4

**Verkko Assemblies** (diploid assemblies):
- `assembly_verkko_1.4/` - Verkko version 1.4
- `assembly_verkko_1.1-0.1/` - Verkko version 1.1-0.1
- `assembly_verkko_1.1-0.1-freeze/` - Frozen version
- `assembly_verkko_1.1-0.2/` - Version 1.1-0.2
- `assembly_verkko_1.4.1r/` - Revised version 1.4.1

**Clade-Specific Directories** (2023+ specialized assemblies):
- `assembly_primate_v1.4.2/` - Primate-specific pipeline
- `assembly_fish_*` - Fish-specific (potential)
- `assembly_bird_*` - Bird-specific (potential)

**Institution-Specific Directories**:
- `assembly_rockefeller/` - Rockefeller University assemblies
- `assembly_cambridge/` - Cambridge assemblies
- `assembly_MT_rockefeller/` - Case variation
- `assembly_mt_rockefeller/` - Lowercase variation
- `assembly_mt_milan/` - Milan institute

**Directories Without "assembly_" Prefix** (rare):
- `vgp_standard_1.6/` - Standard v1.6 without prefix
- `vgp_standard_1.0/` - Standard v1.0 without prefix
- `vgp_HiC_1.6/` - Hi-C v1.6 without prefix

**Curated Assemblies** (post-manual curation):
- `assembly_curated/` - **Exclude for date extraction** (post-curation dates)

**CRITICAL CASE SENSITIVITY**:
- Metadata may store: `assembly_vgp_hic_2.0` (lowercase)
- S3 requires: `assembly_vgp_HiC_2.0` (mixed case!)
- **Always normalize** before fetching

**COMPREHENSIVE PATTERN MATCHING**:
- **Don't stop at first match**: Try ALL valid paths
- **Pri/alt assemblies** often use legacy versions (1.6, 1.0)
- **Phased assemblies** typically use version 2.0
- **Verkko assemblies** are diploid, use different naming
- **Coverage improvement**: Using all patterns -> 47-62% vs 27% with basic patterns

## Pre/Post Curation Assembly FASTAs

Both curation stages live under `assembly_curated/`. This is the only route to pre/post
curation metrics when precomputed gfastats tables are absent.

```
PRE   assembly_curated/intermediates/*hap{1,2}*decontam*.fasta[.gz]   # scaffolder output
POST  assembly_curated/<ToLID>.hap{1,2}.cur.<YYYYMMDD>.fasta.gz       # curated deposit
```

- **Multiple dated files per stage are normal** — take the newest. `mSagOed1` had both
  `.cur.20251218` and `.cur.20260105`. Sort on the embedded date, not lexically on the key.
- `evaluation/gfastats/c/` is **contigging, not curated** — never use it as "post".
- Curated AGPs do **not** always end in `.agp`. Real names include `.agp_20250311`,
  `.agp_Oct11`, `.agp_NB_Feb6`. A `\.agp$` filter silently drops ~5% of them; use
  `\.agp(_\w+)?$`.
- Not every ToLID has both stages. Inventory first (one recursive listing per species)
  and count how many have pre *and* post before planning a sweep — expect ~65-80%.

**Validation**: running `gfastats` on these FASTAs reproduced GenomeArk's own precomputed
tables byte-exactly for `bZonAlb1` — 11/12 fields, every scaffold and contig N50 across
both haplotypes and both stages. The single difference was a scaffold *count* off by one
(174 vs 173), consistent with an extra record such as MT in the published table.

**Always validate a new extraction against a ToLID whose values you already have before
launching a full sweep.** See [best-practices.md](best-practices.md) for the streaming
sweep pattern.

### Two-Block gfastats Files Carry Pre AND Post in One Small File

Newer curated gfastats reports contain **two stat blocks** (~500 bytes total), so pre/post
can be read without downloading any FASTA. Verified against an existing pre/post table on
`fAbrBra2` (pre 43,288,790 / post 42,794,514, exact):

```
block 1  = PRE-curation    (first `Scaffold N50` in the file)
block 2  = POST-curation   (after the first `# paths` line)
```

Split on `^# paths\t[\d,]+$`. Single-block files are **post only** — older assemblies
predate the format, so a sweep recovers far less than the file count suggests: 369 species
swept -> 216 gfastats found -> **0** usable pre/post pairs, all single-block.

### Filename Variants That Silently Drop Species

A `hap[12]` + `.fasta.gz` filter misses a large fraction of the archive:

```
hap1 / hap2          modern phased naming
pri  / alt           older pri/alt assemblies  -> map to hap1 / hap2
.fasta.gz / .fa.gz   both extensions occur
.gfastats.tsv        uncompressed as well as .gz
```

One sweep recovered contig N50 for 79/97 VGL species but only **1/261** Sanger, purely
from naming assumptions. Always report per-institution recovery rates — a near-zero rate
for one institution is a parser bug, not a data gap.

Fetch gzipped members as **bytes**: `subprocess(..., text=True)` raises
`UnicodeDecodeError` on `.gz` content before you can inspect it.

### `aws s3 ls --recursive` on a Species Prefix Can Exceed 3 Minutes

Species with large `intermediates/` trees (e.g. `mTamTet1`) time out and, if the exception
is not caught per-species, kill a whole threaded sweep. List the top level, then only the
`assembly_*` directories:

```bash
aws s3 ls --no-sign-request "s3://genomeark/species/<Sp>/<ToLID>/"
# then per assembly_* dir, non-recursive
```

Wrap every per-species probe in `try/except subprocess.TimeoutExpired` returning an empty
result, so one slow species degrades to a miss instead of an aborted run.

### Not Every Institution Deposits to GenomeArk

**Genoscope species are absent entirely** — 86/87 had no prefix at all, not a naming
problem. Inventory presence before planning a sweep, and expect whole institutions to be
unrecoverable. Curated assemblies are on NCBI regardless, so post-curation metrics can
come from there; it is the **pre**-curation stage that only GenomeArk holds.

### Directory Naming Is an Institutional Convention, NOT the Pipeline That Ran

`assembly_cambridge/` vs `assembly_vgp_HiC_2.0/` does **not** identify the assembler. The
recorded `Assembly tech` was the same on both sides of that split, and the naming tracked
release year (a convention change ~2024), not software. Do not infer methodology from
paths — check the recorded assembler field instead.

## Data Access Summary

For detailed fetching code and parsing logic, see [qc-data-fetching.md](./qc-data-fetching.md).

| Data Type | Location | Key Notes |
|-----------|----------|-----------|
| **GenomeScope** | `evaluation/genomescope/` | 3 filename patterns (double/single/no underscore); validate heterozygosity ranges |
| **BUSCO** | `evaluation/busco/{subdir}/` | Dynamic subdir search (c/, p/, c1/, p1/); parse `C:XX.X%` |
| **Merqury** | `evaluation/merqury/` | Two path layouts (direct vs nested); QV in column 4 |
| **Meryl hist** | `intermediates/meryl/` | Use `.hist` file only (~700KB), not full database (~10GB) |
| **Assembly dates** | FASTA filenames | YYYYMMDD stamps; see [assembly-date-extraction.md](./assembly-date-extraction.md) |
| **Technology** | `genomic_data/` subfolders | `pacbio_hifi/` -> HiFi, `ont/` -> ONT, etc. |

### Path Normalization (used by all fetching functions)

```python
def normalize_s3_path(s3_path):
    """Normalize path for GenomeArk (case sensitivity!)"""
    if not s3_path:
        return None
    s3_path = s3_path.replace('/assembly_vgp_hic_2.0/', '/assembly_vgp_HiC_2.0/')
    if not s3_path.endswith('/'):
        s3_path += '/'
    return s3_path
```

### GenomeScope Filename Patterns (TRY ALL THREE!)

- Pattern A: `{ToLID}_genomescope__Summary.txt` (double underscore, most common)
- Pattern C: `{ToLID}_genomescope_Summary.txt` (single underscore, easily missed)
- Pattern B: `{ToLID}_Summary.txt` (no prefix, older assemblies)

Checking only A and B causes ~30-40% of data to be missed.

### GenomeScope Validation

Reject failed runs where heterozygosity range > 50% or max > 95%. A range of 0%-100% indicates complete model failure.

### Meryl Histograms - Direct HTTPS URLs (for Galaxy import)

```
https://genomeark.s3.amazonaws.com/species/{species}/{tolid}/assembly_vgp_standard_1.0/intermediates/meryl/{tolid}.cut.meryl.hist
```

## Quick Reference

**AWS CLI pattern** (prefer over boto3 for public buckets):
```python
cmd = ['aws', 's3', 'cp', s3_path, '-', '--no-sign-request']
result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
```

**Rate limiting**: 0.2s delay between requests.

**Common pitfalls**: Case sensitivity (`hic` vs `HiC`), directory evolution (2022 vs 2024 layouts), downloading full meryl databases instead of `.hist` files. See [best-practices.md](./best-practices.md) for full list.

## Where decontaminated (pre-curation) assemblies live, and from when

Two unrelated naming families exist, and only the first is produced by the Galaxy export
workflows in `iwc` (branch `exports`, `workflows/VGP-assembly-v2/Export-*`):

```
# 1. Galaxy, Export-pre-curation/Export_PretextMap.ga -- from 2025-05-23 ONLY
species/<Species>/<ToLID>/assembly_curated/intermediates/
    <ToLID>.HiC.combined.decontam.<YYYYMMDD>.fasta.gz
    <ToLID>.HiC.hap1.decontam.<YYYYMMDD>.fasta.gz
    <ToLID>.HiC.hap2.decontam.<YYYYMMDD>.fasta.gz

# 2. Other centres / manual -- directly in assembly_curated/, real haplotype labels
species/<Species>/<ToLID>/assembly_curated/<ToLID>.{mat,pat,hap1,hap2,pri,alt}.decon[tam].<DATE>.fasta.gz
```

**`.HiC.`, `hap1` and `hap2` are hardcoded literals** in the Galaxy workflow - it has six
parameters and no assembly-method or haplotype parameter, and all three fasta inputs are
`optional: false` in every version. So a primary/alternate assembly gets no distinct path and
the export cannot run on a single haplotype at all. `Export-WF1-3` (the pri/alt branch)
exports no decontaminated file, and VGP9 (decontamination) has no export step anywhere.

**Dates that matter**: decontaminated fastas first exported **2025-05-23** (`a584fc720`) and
the path has not changed since; before that the pre-curation export carried only
`pretextmap/PretextMap_with_tracks.pretext`. Repo-wide, the root changed from `/species/` to
`species/` on 2024-05-16, and a `//`-when-no-haplotype bug was fixed on 2024-05-23 - so
`evaluation//gfastats/` in a key dates it before that.

**The scaffolded (pre-decontamination) assembly** is elsewhere again, written by
`Export-WF8`: `assembly_vgp_{standard|HiC|trio}_2.0/<ToLID>.<method>.<hap>.<YYYYMMDD>.fasta.gz`,
`hap` in {hap1, hap2, pri, mat, pat}.

**Practical consequence**: for most curated assemblies there is NO separate pre-curation file.
The pre-curation statistics are block 1 of the two-block
`assembly_curated/<ToLID>.<hap>.cur.<DATE>.gfastats.tsv[.gz]`, and GenomeArk publishes no
decontaminated gfastats at all - so the stage of that block cannot be read from any path and
must be established by measuring the FASTA, or inferred from whether the **diploid** total
scaffold length was preserved across curation.

Beware the ToLID: some assemblies' files are published under a sibling ToLID of the same
species (bFalPer1 -> bFalPer5, mBalPhy1 -> mBalPhy2). Pre and post then come from the
substitute consistently, so the *change* is valid, but it is a different assembly from the one
the metadata names.
