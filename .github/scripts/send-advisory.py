#!/usr/bin/env python3
import sys, re, os
from sendgrid import SendGridAPIClient
from pathlib import Path
from markdown import markdown
from string import Template
from subprocess import check_output

added_files = check_output(["git", "diff", "--name-only", "-r", "--diff-filter=A", "HEAD^"]).decode("utf8").split("\n")
latest_advisory = max(Path("docs/advisories").glob("*.md"))
advisory_uid = latest_advisory.name[:11]
advisory_mds = {}
base_url = "https://soc.cyber.wa.gov.au/advisories/"

def email_campaign (uid, title, overview, url, content):

    sg = SendGridAPIClient(os.environ.get('sendgrid_api'))

    data = {
    "name":f"{uid} - TLP CLEAR - {title}",
    "categories": ["wasoc-advisory"],
    "send_to": {
        "list_ids": [
            "fdeb76e9-0895-4b5e-b929-4022f71cb16d"
        ],
        "segment_ids": [],
        "all": False
    },
    "email_config": {
        "subject": f"Cyber Security Advisory - TLP CLEAR - {title}",
        "html_content": f"{content}",
        #"plain_content": f"{title}\n\n*Ref: {uid}*\n\nOverview\n\n{overview}\n\n{url}\n\nReporting\n\nAgencies whose cyber security teams have enrolled in the DGov Incident Reporting Portal (IRP) should raise an incident within the portal.\n\nThe Cyber Security Unit will liaise with the Australian Cyber Security Centre and other States and Territories in support of nation-wide incident coordination.\n\nFurther Information\n\nFor more information relating to this advisory, or for further information on connecting to the WA SOC, please contact the Office of Digital Government - Cyber Security Unit at cybersecurity@dpc.wa.gov.au\n\n© 2023 Office of the Digital Government - Cyber Security Unit. All rights reserved.\nDumas House, 2 Havelock Street, WEST PERTH, WA 6005",
        "generate_plain_content": True,
        "editor": "design",
        "suppression_group_id": -1,
        "custom_unsubscribe_url": None,
        "sender_id": 5228194
    }
}
    # For Troubleshooting SendGrid Data
    #print(data)

    response = sg.client.marketing.singlesends.post(
        request_body=data
    )

    # For Troubleshooting Send Grid API
    #print(response.status_code)
    #print(response.body)
    #print(response.headers)


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
        if file.startswith(f"docs/advisories/{advisory_uid}"):
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
            title = section[1:].strip()[:-14]
        if section.strip().lower().startswith("overview"):
            overview = section[9:].strip()
            break
    
    html_overview = markdown(overview)
    html_filled = Template(Path("templates/tlp-clear-email-template.html").read_text()).substitute(title=title, overview=html_overview, url=url, uid=advisory_uid)

    email_campaign(advisory_uid, title, html_overview, url, html_filled)

    #print()