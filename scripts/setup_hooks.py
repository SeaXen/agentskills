#!/usr/bin/env python3
"""
Install git pre-commit and pre-push hooks to automatically:
1. Rebuild Skill.Sea web catalog when skills or categories are committed.
2. Synchronize Skill.Sea master datasets to Cloudflare R2 on git push.
"""
import os
import sys
import stat

if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

PRE_COMMIT_SCRIPT = """#!/bin/sh
# Auto-rebuild Skill.Sea web catalog if skills or categories are staged for commit

STAGED_SKILLS=$(git diff --cached --name-only | grep -E '^(skills|library|category|\\.agent/skills)/')

if [ -n "$STAGED_SKILLS" ]; then
  echo "🔄 Skill changes detected in commit. Auto-rebuilding Skill.Sea catalog..."
  if command -v node >/dev/null 2>&1; then
    node Skill.Sea/scripts/build-catalog.js
    git add Skill.Sea/data/
    echo "✅ Skill.Sea web catalog automatically updated and staged."
  fi
fi

exit 0
"""

PRE_PUSH_SCRIPT = """#!/bin/sh
# Auto-sync Skill.Sea datasets to Cloudflare R2 on push if skills or catalog changed

REMOTE="$1"
URL="$2"

CHANGED=0
while read local_ref local_oid remote_ref remote_oid; do
  if [ "$local_oid" = "0000000000000000000000000000000000000000" ]; then
    continue
  fi
  if [ "$remote_oid" = "0000000000000000000000000000000000000000" ]; then
    DIFF_FILES=$(git diff --name-only HEAD~1 2>/dev/null)
  else
    DIFF_FILES=$(git diff --name-only "$remote_oid" "$local_oid" 2>/dev/null)
  fi

  if echo "$DIFF_FILES" | grep -E -q '^(skills|library|category|\\.agent/skills|Skill\\.Sea/data)/'; then
    CHANGED=1
    break
  fi
done

if [ "$CHANGED" -eq 1 ]; then
  echo ""
  echo "☁️  [Skill.Sea] Skill library updates detected in outgoing push."
  echo "🚀 Synchronizing catalog datasets with Cloudflare R2 (skill-sea-vault)..."
  
  if command -v node >/dev/null 2>&1; then
    # Run sync-r2 with --allow-offline so git push is never blocked if offline
    node Skill.Sea/scripts/sync-r2.js --allow-offline
    echo "✅ Live website data synchronization process complete."
  else
    echo "⚠️  Node.js not found in PATH. Skipping automatic R2 sync."
  fi
  echo ""
fi

exit 0
"""

def setup_git_hooks():
    agents_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    hooks_dir = os.path.join(agents_dir, '.git', 'hooks')
    
    if not os.path.exists(hooks_dir):
        print(f"⚠️ Git hooks directory not found at: {hooks_dir}")
        return False
        
    # 1. Install pre-commit hook
    pre_commit_path = os.path.join(hooks_dir, 'pre-commit')
    with open(pre_commit_path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(PRE_COMMIT_SCRIPT)
    try:
        os.chmod(pre_commit_path, os.stat(pre_commit_path).st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
    except Exception:
        pass
    print(f"✓ Git pre-commit hook installed at: {pre_commit_path}")

    # 2. Install pre-push hook
    pre_push_path = os.path.join(hooks_dir, 'pre-push')
    with open(pre_push_path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(PRE_PUSH_SCRIPT)
    try:
        os.chmod(pre_push_path, os.stat(pre_push_path).st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
    except Exception:
        pass
    print(f"✓ Git pre-push hook installed at: {pre_push_path}")
    
    return True

if __name__ == '__main__':
    setup_git_hooks()

