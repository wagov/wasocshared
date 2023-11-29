#!/usr/bin/env python3
import sys, re
from pathlib import Path
from markdown import markdown
from string import Template
from subprocess import check_output

added_files = check_output(["git", "diff", "--name-only", "-r", "--diff-filter=A", "HEAD^"]).decode("utf8").split("\n")
latest_advisory = max(Path("docs/advisories").glob("*.md"))
base_template = Template(Path("email-template.html").read_text())
today = latest_advisory.name[:8]
advisory_mds = {}
base_url = "https://soc.cyber.wa.gov.au/advisories/"

if sys.argv[1].startswith(base_url):
    # If a url is provided, find the relevant advisory and send it
    input_url = sys.argv[1]
    advisory_id = re.search(r'(?<=advisories/)\d+(?=-)', input_url).group(0).strip()
    advisory_mds[input_url] = max(Path(f"docs/advisories").glob(f"{advisory_id}-*.md")).read_text()
else:
    print(f"input {sys.argv[1]} doesn't start with {base_url}")
    # Figure out if file is in latest set of added files, and send if so
    for file in added_files:
        print(file)
        if file.startswith(f"docs/advisories/{today}"):
            file = Path(file)
            url = base_url + file.stem
            advisory_mds[url] = file.read_text()

print("Preparing to send below advisories: ")

for url, advisory_md in advisory_mds.items():
    print(url)
    sections = advisory_md.split("##")
    title, overview = None, None

    for section in sections:
        if not title and section.startswith("#"):
            title = section[1:].strip()
        if section.strip().lower().startswith("overview"):
            overview = section[9:].strip()
            break

    overview += f"\n\n- [{title}]({url})"
    html_overview = markdown(overview)

    print(f"Title: {title}")
    print("--- Overview Below ---")
    print(overview)
    print("---")