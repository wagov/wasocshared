#!/usr/bin/env python3
import sys, re
from pathlib import Path

url = sys.argv[1]
advisory_id = re.search(r'(?<=advisories/)\d+(?=-)', url).group(0).strip()
advisory_md = Path(f"docs/advisories").glob(f"{advisory_id}-*.md").__next__().read_text()

sections = advisory_md.split("##")
title, overview = None, None

for section in sections:
    if not title and section.startswith("#"):
        title = section[1:].strip()
    if section.strip().lower().startswith("overview"):
        overview = section[9:].strip()
        break

overview += f"\n\n- [{title}]({url})"

print(overview)