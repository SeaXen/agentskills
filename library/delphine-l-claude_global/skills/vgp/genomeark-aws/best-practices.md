# GenomeArk Best Practices and Reference

## Best Practices

### Path Construction

1. **Always normalize case**: `hic` -> `HiC` before fetching
2. **Try multiple patterns**: Implement all filename variations
3. **Use timeouts**: 10-30s per fetch to avoid hanging
4. **Add rate limiting**: 0.2s delay between requests (respectful to AWS)
5. **Handle failures gracefully**: Continue on errors, report successes

### Data Validation

1. **Validate GenomeScope ranges**: Reject values with >50% range or max >95%
2. **Check for empty results**: Verify data before parsing
3. **Verify file existence**: S3 returns 0 bytes for non-existent files
4. **Skip failed QC runs**: Filter out unrealistic values

### AWS CLI vs boto3

For **public buckets** like GenomeArk:
- **Prefer**: `subprocess` + `aws s3` CLI with `--no-sign-request`
- **Avoid**: `boto3` (requires credential config even for public access)

```python
# Simple and works
cmd = ['aws', 's3', 'cp', s3_path, '-', '--no-sign-request']
result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)

# More complex, requires config (avoid)
import boto3
from botocore import UNSIGNED
from botocore.config import Config
s3 = boto3.client('s3', config=Config(signature_version=UNSIGNED))
```

## Batch Processing

```python
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

def batch_fetch_qc_data(species_list, max_workers=5):
    """Fetch QC data for multiple species with rate limiting"""
    results = []

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {
            executor.submit(fetch_all_qc, species, tolid): (species, tolid)
            for species, tolid in species_list
        }

        for future in as_completed(futures):
            species, tolid = futures[future]
            try:
                data = future.result()
                results.append({
                    'species': species,
                    'tolid': tolid,
                    **data
                })
            except Exception as e:
                print(f"Error fetching {species} ({tolid}): {e}")

            time.sleep(0.2)  # Rate limiting

    return results

def fetch_all_qc(species, tolid):
    """Fetch all QC metrics for a species"""
    data = {}

    # GenomeScope
    genomescope = fetch_genomescope_data(species, tolid)
    if genomescope:
        data.update(genomescope)

    # BUSCO
    busco = fetch_busco_data(species, tolid)
    if busco:
        data['busco_completeness'] = busco['completeness']

    # Merqury
    merqury = fetch_merqury_data(species, tolid)
    if merqury:
        data['qv'] = merqury['qv']

    return data
```

## Common Pitfalls

1. **Case sensitivity**: `assembly_vgp_hic_2.0` (table) -> `assembly_vgp_HiC_2.0` (S3)
2. **Missing pattern C**: Single underscore GenomeScope files often missed
3. **Directory evolution**: Merqury structure changed 2022 -> 2024
4. **Failed QC runs**: Always validate GenomeScope ranges before use
5. **Subdirectory variations**: BUSCO/Merqury use different subdir names
6. **File format variations**: Merqury may/may not have header line
7. **Downloading full meryl databases**: Use `.hist` files only!
8. **Timeout issues**: Set reasonable timeouts for S3 operations
9. **Rate limiting**: Add delays between requests to avoid throttling

## Testing Examples

Confirmed working paths (as of 2026-02-26):

```bash
# GenomeScope - Pattern A (double underscore)
aws s3 cp s3://genomeark/species/Gastrophryne_carolinensis/aGasCar1/assembly_vgp_HiC_2.0/evaluation/genomescope/aGasCar1_genomescope__Summary.txt - --no-sign-request

# GenomeScope - Pattern C (single underscore)
aws s3 cp s3://genomeark/species/Platysternon_megacephalum/rPlaMeg1/assembly_vgp_HiC_2.0/evaluation/genomescope/rPlaMeg1_genomescope_Summary.txt - --no-sign-request

# GenomeScope - Pattern B (no prefix)
aws s3 cp s3://genomeark/species/Spea_bombifrons/aSpeBom1/assembly_vgp_standard_2.0/evaluation/genomescope/aSpeBom1_Summary.txt - --no-sign-request

# BUSCO
aws s3 cp s3://genomeark/species/Gastrophryne_carolinensis/aGasCar1/assembly_vgp_HiC_2.0/evaluation/busco/c/aGasCar1_HiC__busco_hap1_busco_short_summary.txt - --no-sign-request

# Merqury - Direct path (2024+)
aws s3 cp s3://genomeark/species/Ia_io/mIaxIox2/assembly_vgp_HiC_2.0/evaluation/merqury/mIaxIox2_qv/output_merqury.tabular - --no-sign-request

# Merqury - Nested path (2022)
aws s3 cp s3://genomeark/species/Gastrophryne_carolinensis/aGasCar1/assembly_vgp_HiC_2.0/evaluation/merqury/c/aGasCar1_qv/output_merqury.tabular - --no-sign-request

# Meryl histogram
aws s3 cp s3://genomeark/species/Rhinolophus_ferrumequinum/mRhiFer1/assembly_vgp_standard_1.0/intermediates/meryl/mRhiFer1.cut.meryl.hist - --no-sign-request
```

## Integration with VGP Workflows

This skill integrates with:
- **vgp-pipeline**: Fetching GenomeScope summaries for workflow analysis
- **bioinformatics-fundamentals**: General S3 access patterns
- **galaxy-automation**: Meryl histogram URLs for Galaxy import

See `vgp-pipeline` skill for species-specific workflow integration patterns.

## References

- GenomeArk Homepage: https://www.genomeark.org/
- VGP Project: https://vertebrategenomesproject.org/
- AWS S3 CLI Documentation: https://docs.aws.amazon.com/cli/latest/reference/s3/

## Version History

- **1.1** (2026-02-26): Assembly date extraction patterns added
  - **NEW**: Comprehensive assembly directory patterns (30+ patterns)
  - **NEW**: Legacy versions (1.6, 1.0, 1.4) for Pri/alt assemblies
  - **NEW**: Verkko assembly patterns (diploid assemblies)
  - **NEW**: Clade-specific directories (primate_v*, etc.)
  - **NEW**: Institution-specific patterns (rockefeller, cambridge, milan)
  - **NEW**: Patterns without "assembly_" prefix
  - **NEW**: Assembly date extraction strategy
  - **NEW**: Date validation results (1.1 year average delay)
  - Updated: Coverage improvement: 47-62% vs 27% with basic patterns

- **1.0** (2026-02-26): Initial skill creation, consolidated from fundamentals and vgp-pipeline skills
  - Comprehensive S3 structure documentation
  - All three GenomeScope filename patterns
  - GenomeScope validation logic
  - Meryl histogram access patterns
  - Best practices and common pitfalls

## Bulk Sweeps: Stream, Don't Stage

Genome FASTAs are 0.4-10 GB each. Download → measure → **delete before the next file**,
so peak disk is one haplotype rather than the whole sweep. This is what made a 266 GB
sweep possible on 123 GB of free disk — not an optimisation, a precondition.

```python
def measure(key, workdir):
    local = workdir / Path(key).name
    try:
        sh(f'aws s3 cp --no-sign-request --only-show-errors "s3://genomeark/{key}" "{local}"')
        return run_tool(local)
    finally:
        if local.exists():
            local.unlink()          # always, including on error
```

Append results per row as you go and skip already-present keys on startup, so an
interrupted multi-hour run resumes instead of restarting:

```python
done = {(f[1], f[2], f[3]) for f in (l.split('\t') for l in out.read_text().splitlines()[1:])}
```

Check free disk against the largest single file, not the sweep total, before starting.

### Parallel listing gotcha

`xargs -P N` processes writing to one shared stdout interleave mid-line and corrupt the
output. Write one file per item, then concatenate:

```bash
# WRONG - silently corrupts rows
cut -f1 species.tsv | xargs -P 8 -I{} ./inv.sh {} > all.tsv

# RIGHT
mkdir -p invd
cut -f1 species.tsv | xargs -P 8 -I{} sh -c './inv.sh "$1" > "invd/$1.tsv"' _ {}
cat invd/*.tsv > all.tsv
```

The corruption is easy to miss — it surfaces as impossible values in a column, e.g. more
distinct species in the output than you queried. Sanity-check counts after any parallel
listing.

## Two Silent Failure Modes

Both of these produce *plausible-looking wrong answers* rather than errors.

### Double-gzipped FASTAs

Some GenomeArk files are gzip-compressed twice. Tools that decompress one layer see binary,
parse no records, and report **0** — which a pipeline will happily record as data.

```python
import gzip
with gzip.open(path, 'rb') as fh:
    if fh.read(2) == b'\x1f\x8b':      # still gzip after one layer
        ...                            # unwrap another layer
```

Known case: `mRucEld1.HiC.hap{1,2}.decontam.20250604.fasta.gz` (real values 83.69 / 102.52 Mb,
reported as 0.00).

**Always reject implausible zeros as measurements**, independently of the cause:

```python
if not vals.get("scaffold_n50") or not vals.get("total_length"):
    return None, "implausible result — file likely unreadable"
```

A zero N50 flows into a percent-change calculation as a division by zero or an infinite
improvement. Guard at the point of measurement, not downstream.

### Trinomial vs binomial species names

VGP freeze files carry trinomials; GenomeArk directories use binomials:

| Freeze | GenomeArk |
|---|---|
| `Peromyscus_gossypinus_allapaticola` | `Peromyscus_gossypinus` |
| `Rucervus_eldii_thamin` | `Rucervus_eldii` |
| `Zapus_hudsonius_preblei` | `Zapus_hudsonius` |

A target list built from freeze names reports "no objects on GenomeArk" for these, which
reads as *absent data* rather than *wrong key*. Always fall back to the binomial (drop the
third token) before concluding a species is missing, and prefer ToLID matching where
available.
