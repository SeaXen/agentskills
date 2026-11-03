#!/usr/bin/env python3
"""
Validate all wiki-links in medical exam notes resolve to existing files.
Run from the chapter root directory.
"""

import os
import re
import sys
from pathlib import Path

def find_wiki_links(content):
    """Extract all wiki-style links from markdown content."""
    # Pattern: [[link]] or [[link|display]]
    pattern = r'\[\[([^\]]+)\]\]'
    return re.findall(pattern, content)

def resolve_link(link, base_dir):
    """Resolve wiki-link to actual file path."""
    # Remove display text if present: [[link|display]] -> link
    if '|' in link:
        link = link.split('|')[0]
    
    # Handle relative paths
    if link.startswith('../'):
        return base_dir / link
    elif link.startswith('./'):
        return base_dir / link[2:]
    else:
        # Assume same directory or subdirectory
        return base_dir / link / f"{link}.md"

def validate_links_in_file(filepath, errors):
    """Check all wiki-links in a file resolve to existing files."""
    try:
        content = filepath.read_text(encoding='utf-8')
    except Exception as e:
        errors.append(f"{filepath}: Failed to read - {e}")
        return
    
    links = find_wiki_links(content)
    base_dir = filepath.parent
    
    for link in links:
        # Skip external links
        if link.startswith('http://') or link.startswith('https://'):
            continue
        # Skip pure anchor links
        if link.startswith('#'):
            continue
        # Skip file references with .md extension
        if link.endswith('.md'):
            continue
            
        target_path = resolve_link(link, base_dir)
        
        # Try multiple extensions
        found = False
        for ext in ['.md', '.MD']:
            if (target_path.parent / (target_path.name + ext)).exists():
                found = True
                break
            if (target_path.parent / target_path.name / f"index{ext}").exists():
                found = True
                break
        
        if not found:
            errors.append(f"{filepath}: Broken link -> [[{link}]] (resolved to {target_path})")

def main():
    if len(sys.argv) > 1:
        root = Path(sys.argv[1])
    else:
        root = Path.cwd()
    
    md_files = list(root.rglob("*.md"))
    
    if not md_files:
        print(f"No markdown files found in {root}")
        return 1
    
    errors = []
    
    print(f"Validating {len(md_files)} markdown files in {root}...")
    
    for md_file in md_files:
        validate_links_in_file(md_file, errors)
    
    if errors:
        print(f"\n❌ Found {len(errors)} broken links:")
        for error in errors:
            print(f"  {error}")
        return 1
    else:
        print("✅ All wiki-links resolve successfully!")
        return 0

if __name__ == "__main__":
    sys.exit(main())