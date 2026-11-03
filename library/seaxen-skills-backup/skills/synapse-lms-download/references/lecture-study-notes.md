# Lecture study notes — "learn from video" workflow

The user asks to **"note all important things"** from a downloaded Synapse lecture. Here's the honest workflow.

## The hard truth: no subtitles

Synapse/Vidinfra MP4 files have **no subtitle track**. There is **no closed-caption data** embedded. You cannot extract a transcript programmatically without a separate ASR pass.

## What you CAN do

### Option A: Vault-aligned high-yield (what we did in session)

Map the video title to the user's existing Davidson Medicine notes in `/mnt/tb/Medicine/<topic>/`. Produce a structured high-yield note covering the standard FCPS/MRCP sections. **This is not the lecturer's words** — it's Davidson curriculum content aligned to the topic.

**Use when:** user wants exam prep, not lecturer-specific content.

### Option B: Audio extraction + Whisper transcription

```bash
# 1. Extract audio
ffmpeg -i "/mnt/tb/synapse_26/Lecture.mp4" -vn -ac 1 -ar 16000 /tmp/lecture.wav

# 2. Transcribe (requires faster-whisper install)
# pip install faster-whisper
python3 -c "
 import WhisperModel
model = WhisperModel('large-v3', device='cpu', compute_type='int8')
segments, info = model.transcribe('/tmp/lecture.wav', language='en', beam_size=5)
with open('/tmp/lecture.txt', 'w') as f:
    for seg in segments:
        f.write(f'[{seg.start:.1f}-{seg.end:.1f}] {seg.text}\n')
print('Done:', len(segments), 'segments')
"

# 3. Summarize the transcript into a note
# (feed the .txt to the agent for summarization into FCPS format)
```

**⚠ CPU cost:** Whisper-large-v3 on CPU = ~10-20 min per 2h lecture. Run as background task with `notify_on_complete=true`. On a busy host, pace with `sleep` gaps.

**Use when:** user wants the **actual lecturer** content, emphasis, case vignettes.

### Option C: Quick extraction (word-level, smaller model)

```bash
# Use small/base model for speed over accuracy
python3 -c "
from faster_whisper import WhisperModel
model = WhisperModel('small', device='cpu', compute_type='int8')
segments, _ = model.transcribe('/tmp/lecture.wav', beam_size=5, vad_filter=True)
with open('/tmp/lecture.txt', 'w') as f:
    for s in segments: f.write(s.text + '\n')
"
# ~3-5 min per 2h lecture
```

## Decision flowchart

```
User says "learn from this video" or "note all important things"
│
├── Do we have time for Whisper? (user asked for detail)
│   ├── YES → Option B (full transcription)
│   └── NO → Option A (vault-aligned high-yield)
│
├── Does the user have /mnt/tb/Medicine notes for this topic?
│   ├── YES → produce vault-aligned note (cross-reference existing files)
│   └── NO → produce generic FCPS high-yield from Davidson 24th Ed structure
```

## Honesty boundary

**Do not** claim to have captured lecture content from the MP4 alone. If you only have the title, say: *"The MP4 has no subtitles. Here's a Davidson-aligned high-yield note based on the title. If you want the actual lecturer's words, I can set up a Whisper transcription pipeline (10-20 min CPU, background)."*

This boundary protects: the user will verify against the video and catches AI-invented "lecture content" immediately.