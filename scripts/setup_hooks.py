#!/usr/bin/env python3
"""
Install git pre-commit hook to automatically rebuild Skill.Sea web catalog
whenever skills or categories are committed.
"""
import os
import sys

def setup_git_hooks():
    agents_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    hooks_dir = os.path.join(agents_dir, '.git', 'hooks')
    
    if not os.path.exists(hooks_dir):
        print(f"⚠️ Git hooks directory not found at: {hooks_dir}")
        return False
        
    pre_commit_path = os.path.join(hooks_dir, 'pre-commit')
    
    hook_script = """#!/bin/sh
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
    
    with open(pre_commit_path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(hook_script)
        
    try:
        import stat
        os.chmod(pre_commit_path, os.stat(pre_commit_path).st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
    except Exception:
        pass
        
    print(f"✓ Git pre-commit hook installed successfully at: {pre_commit_path}")
    return True

if __name__ == '__main__':
    setup_git_hooks()
