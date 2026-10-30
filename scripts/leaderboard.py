#!/usr/bin/env python3
import sys, os
target = os.path.join(os.path.dirname(__file__), 'skillleaderboard.py')
if __name__ == '__main__':
    import subprocess
    sys.exit(subprocess.run([sys.executable, target] + sys.argv[1:]).returncode)
