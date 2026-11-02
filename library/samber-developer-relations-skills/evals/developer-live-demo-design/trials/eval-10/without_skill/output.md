Good list of what's already covered. Here's what's still open, grouped by leak surface — worth going through in order, since #1 removes most of the risk from everything below it.

## 0. Highest-leverage move
- **Create a dedicated macOS user account (or a fresh guest profile) just for the demo.** Log into nothing personal there — no Mail, no Messages, no personal iCloud, no password manager unlocked, no other client repos. This alone kills 80% of the risks below, because a security-conference audience will pause the YouTube recording and zoom into corners of the screen looking for exactly this stuff.

## 1. Messaging & notifications (Slack ≠ everything)
- **Quit, don't just background:** Teams, Discord, WhatsApp/Signal/Telegram desktop, Mail client, Messages (iMessage/SMS).
- **Turn off Handoff/Continuity** (System Settings → General → AirDrop & Handoff) — otherwise an iPhone text can surface as a macOS notification even mid-demo.
- Check your conferencing app's **own** "hide notifications while screen sharing" toggle (Zoom/Meet/Teams) — some in-app banners bypass macOS-level DND.
- Quit Dropbox/Google Drive/OneDrive — their custom overlay toasts (showing synced filenames) often ignore system DND.

## 2. Browser
- Use a **separate browser profile** built just for this, with a clean bookmarks bar (no internal tool names), no browsing history, no saved passwords/autofill.
- **Log out of or remove extensions that show org names on click**: password manager (1Password/Bitwarden vault name), VPN client extension, any internal admin-tool extension icon.
- Close every tab that isn't part of the demo — including background tabs on other displays if you're extending, not mirroring.
- Disable address-bar autocomplete suggestions (they can surface internal URLs as you type, even in a fresh profile if browser history sync is on).

## 3. Terminal / shell
- Use a **clean shell profile** for the demo (fresh `.zsh_history`, no up-arrow recall into anything sensitive).
- Check `PS1`/prompt doesn't leak hostname if your machine name reveals the company (`whoami`/`hostname` too, if you run either live).
- If the demo touches any cloud CLI (`gcloud`, `aws`, `kubectl`, `az`), run `gcloud config list` / `aws sts get-caller-identity` / `kubectl config current-context` **beforehand** and scrub — these routinely print real account IDs, org names, or cluster names.
- Double-check `.env` files, dotfiles, and any real secrets aren't in `history` or shell-visible env vars (`env`, `printenv`) if you run those commands live.

## 4. OS chrome (small stuff YouTube viewers pause on)
- **Rename the Mac itself** (System Settings → General → Sharing → "Local hostname"/computer name) to something generic — this string surfaces in AirDrop sheets, Finder network browsing, and some screen-recording title bars.
- Clean desktop: no icons, no personal wallpaper, no visible file names.
- Empty/curate the Dock — a pinned internal tool icon lighting up with a notification badge is still visible even with DND on.
- Disable software-update prompts and Time Machine/disk-space popups for the session (System Settings → General → Software Update → pause).
- If Bluetooth device picker or AirPlay/screen-mirror picker could appear on camera, check device names aren't "Samuel's iPhone" etc.

## 5. Conferencing app specifics
- Display name shown to the room/stream: set to what you actually want public.
- Meeting/webinar title, waiting-room branding, and any co-host's visible name — check who else could appear in a screen-share thumbnail.
- If you'll use a virtual background or camera at all, sanity-check what's behind you too (recorded + YouTube = permanent).

## 6. Files / IDE
- Check the IDE's "recent projects/files" list and sidebar tree don't show other client repos or folders with real names, even the ones not open.
- Confirm the seed-data repo has no `.env`, credentials file, or internal ticket/Slack links in comments or README that you already fixed names in but forgot elsewhere — worth one `grep -ri` pass for the client names you replaced, in case one instance was missed (commit messages, git history, config files, not just the seed data itself).
- If you'll show `git log`, skim it once for any commit message that references a real customer or internal system.

## 7. Dry run (do this last, in order)
1. Start the actual recording/screen-share tool exactly as you will on the day.
2. Trigger a test notification from each app you didn't quit, to confirm DND actually suppresses it in that specific tool.
3. Open every window/tab you'll touch during the demo once, watching for anything unexpected in title bars, autofill dropdowns, or sidebars.
4. Have a second person watch the shared screen live (not just you) — a fresh set of eyes catches things you're now blind to from familiarity.

Given the audience and the permanence of YouTube, treat "would a security researcher pause-and-zoom this frame" as the bar, not "would a live audience notice in real time."