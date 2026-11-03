#!/bin/bash
set -euo pipefail
chmod +x "$(dirname "$0")/auth.py" "$(dirname "$0")/download_course.py"
command -v yt-dlp >/dev/null || { echo "install yt-dlp"; exit 1; }
command -v ffmpeg >/dev/null || { echo "install ffmpeg"; exit 1; }
mkdir -p ~/.hermes/secrets/drbeen-accounts
echo "DrBeen downloader ready. Set DRBEEN_EMAIL + creds file, then auth.py && download_course.py"