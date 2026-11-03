# Organize new Sagar Synapse downloads immediately after download

For Dr. Sagar's Synapse workflow, flat downloads in `/mnt/tb/synapse_26` are only an intermediate landing area. **After every incremental download session, immediately organize new files into the chapter-wise tree** at `/mnt/tb/synapse_26_by_chapter`.

## When to do this

Run the organizer after any of these:
- `download_sagar_one.py ...`
- `download_notes.py sagar ...`
- `download_all.py sagar` (full or partial sync)

Do it in the **same session** as the download, not later. The user expects the chapter-wise tree to stay current.

## Command

Preferred (organize + auto-normalize):

```bash
bash /root/.hermes/skills/synapse-lms-download/scripts/organize_sagar_after_sync.sh
```

Or:

```bash
/root/.venvs/synapse-env/bin/python /root/.hermes/skills/synapse-lms-download/scripts/organize_by_chapter.py \
  /mnt/tb/synapse_26 \
  /mnt/tb/synapse_26_by_chapter
```

(`organize_by_chapter.py` invokes `normalize_chapter_filenames.py` at the end.)

## Expected behavior

- New `.mp4` and `.pdf` files are moved from the flat source into chapter folders.
- Existing duplicates already present in the organized tree are removed from the flat source.
- Source root should end up clean after a successful organize pass.

## Current chapter targets used on this host

- `Ch20_Endocrinology`
- `Ch22_Gastroenterology_Hepatology`
- `Ch08_Oncology_Palliative_Environmental_Ageing`
- `Ch14_Infectious_Disease`
- `Ch15_STIs`
- `Ch25_Rheumatology`
- `Ch27_Neurology`
- `Ch24_Haematology`
- `Ch18_Nephrology`
- `Ch29_Psychiatry`
- `Ch32_Geriatrics`
- `Ch00_Orientation`
- fallback: `Ch00_Unsorted`

## Verification

Check that the expected files landed in the chapter tree and that the flat root is clean.

Example verification pattern:

```bash
find /mnt/tb/synapse_26_by_chapter/Ch20_Endocrinology -maxdepth 1 -type f -printf '%f\n' | sort
find /mnt/tb/synapse_26 -maxdepth 1 -type f -printf '%f\n' | sort
```

## Pitfall

The organizer script itself is part of the skill and should be treated as a real maintained asset, not a throwaway helper. If it fails, fix it before finishing the Synapse task; otherwise future "check and download" sessions will keep leaving the organized tree stale.
