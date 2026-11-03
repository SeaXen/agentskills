# Verifying canonical paths

Session note:
- `/mnt/tb/hermes` is a symlink to `/root/.hermes`
- Use the canonical path when writing files
- Mention both paths when the alias matters to the user

Verification pattern:
1. Resolve the path with `readlink -f` or equivalent.
2. Write the file under the canonical root.
3. Read the result back from disk.
4. If the user supplied a symlink path, confirm both names refer to the same location.
