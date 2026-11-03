# Canonical Davidson Chapter 16 Cardiology Topics — TEMPLATE
#
# Copy this file, rename to topics.py in the same directory as notion_upload.py,
# and edit the entries for your chapter.
#
# Fields:
#   num        — display number on the hub (1, 2, 3, ...)
#   slug       — URL-safe folder name; must match the local archive folder name
#   title      — display name on the Notion sub-page and hub
#   source_dir — where the user's source notes live (read-only)
#   subdir     — optional, the local archive subfolder (defaults to slug)

topics = [
    {
        "num": 1,
        "slug": "cardiac-investigations",
        "title": "Cardiac Investigations",
        "source_dir": "/mnt/tb/Medicine/Cardiology/01_Cardiac_Investigations",
    },
    {
        "num": 2,
        "slug": "acute-coronary-syndromes",
        "title": "Acute Coronary Syndromes",
        "source_dir": "/mnt/tb/Medicine/Cardiology/02_Acute_Coronary_Syndromes",
    },
    # ... add one entry per topic
]
