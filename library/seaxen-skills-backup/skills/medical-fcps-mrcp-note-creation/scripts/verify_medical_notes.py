#!/usr/bin/env python3
"""
Verification script for FCPS/MRCP medical notes.
Usage: python3 verify_medical_notes.py /path/to/chapter/dir
"""

import re
import glob
import sys
from pathlib import Path

REAL_INDICATORS = [
    'GRACE', 'TIMI', 'PARADIGM-HF', 'DAPA-HF', 'EMPEROR', 'EMPEROR-Reduced',
    'EMPEROR-Preserved', 'DELIVER', 'ISCHEMIA', 'COMPLETE', 'EARLY-AF',
    'CASTLE-AF', 'CABANA', 'FIRE AND ICE', 'ADVENT', 'ATTR-ACT',
    'ISAR-REACT 5', 'TWILIGHT', 'AUGUSTUS', 'ENTRUST-AF PCI',
    'REDUCE-IT', 'FOURIER', 'CLEAR Outcomes', 'ESC 202', 'ACC/AHA 202',
    'NICE NG', 'LVEF', 'EF', 'BNP', 'NT-proBNP', 'troponin', 'hs-cTn',
    'CHA2DS2-VASc', 'HAS-BLED', 'SCAI', 'SCD', 'ICD', 'CRT',
    'PCI', 'CABG', 'TAVI', 'TAVR', 'SAVR', 'PMBV', 'TEER', 'MitraClip',
    'FFR', 'iFR', 'RFR', 'SYNTAX', 'MESSA', 'DAPT score', 'PRECISE-DAPT',
    'HFA-PEFF', 'H2FPEF', 'MAGGIC', 'Seattle Heart Failure',
    'Killip', 'INTERMACS', 'Duke criteria', 'REVEAL', 'COMPERA',
    'BMPR2', 'mPAP', 'PAWP', 'PVR', 'Wood units', 'RCM', 'ARVC',
    'LMNA', 'PLN', 'TTN', 'PKP2', 'MYH7', 'MYBPC3'
]

TEMPLATE_PHRASES = [
    'Most common causes | Direct injury',
    'Comprehensive overview of',
    'Most common aetiology based on epidemiology',
    'Underlying mechanism involves multifactorial pathophysiology',
    'Option A / Option B',
    'Option C / Option D / Option E',
    'Based on epidemiology',
    'Based on clinical presentation'
]

def verify_chapter(chapter_path):
    md_files = list(Path(chapter_path).rglob('*.md'))
    
    full_notes = []
    for f in md_files:
        try:
            content = f.read_text()
            if 'status: full-fcps-mrcp-note' in content:
                full_notes.append((f, content))
        except:
            pass
    
    print(f"Found {len(full_notes)} full notes")
    
    real_count = 0
    template_count = 0
    
    for f, content in full_notes:
        has_real = sum(1 for i in REAL_INDICATORS if i in content) >= 3
        is_template = any(p in content for p in TEMPLATE_PHRASES)
        
        if is_template and not has_real:
            template_count += 1
        elif has_real:
            real_count += 1
        else:
            template_count += 1
    
    total = len(full_notes)
    print(f"Real content: {real_count} ({real_count/total*100:.1f}%)")
    print(f"Template/placeholder: {template_count} ({template_count/total*100:.1f}%)")
    
    if real_count / total < 0.95:
        print("❌ FAIL: Real content below 95% threshold")
        return False
    else:
        print("✅ PASS: Real content ≥ 95%")
        return True

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 verify_medical_notes.py /mnt/tb/Medicine/ChapterName")
        sys.exit(1)
    
    success = verify_chapter(sys.argv[1])
    sys.exit(0 if success else 1)