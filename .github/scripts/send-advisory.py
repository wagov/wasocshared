#!/usr/bin/env python3
import json, sys, re, os, datetime
from sendgrid import SendGridAPIClient
from pathlib import Path
from markdown import markdown
from string import Template
from subprocess import check_output

added_files = check_output(["git", "diff", "--name-only", "-r", "--diff-filter=A", "HEAD^"]).decode("utf8").split("\n")
latest_advisory = max(Path("docs/advisories").glob("*.md"))
latest_advisory_uid = latest_advisory.name[:11]
advisory_uid = {}
advisory_mds = {}
base_url = "https://soc.cyber.wa.gov.au/advisories/"


def email_lookup (advisory_uid):

    sg = SendGridAPIClient(os.environ.get('sendgrid_api'))

    response = sg.client.marketing.singlesends.search.post(
        request_body={"name":advisory_uid}
    )
    response_output = json.loads(response.body)
    results = response_output["result"]
    #print(results)
    
    if len(results) > 0:
        result_name = results[0]["name"]
        result_send_time = results[0]["send_at"]
        result_status = results[0]["status"]
        result_id = results[0]["id"]
        print(f"\nNOTE: The advisory '{result_name}' already exists and was sent at '{result_send_time}' with '{result_status}' status. Sendgrid ID: {result_id}")
        return True, result_name
    else:
        print("NOTE: No existing advisory found")
        return False, ''

def email_delete (advisory_uid):

    lookup = email_lookup(advisory_uid)
    if lookup[0] is True:
        #sg.client.marketing.singlesends._(result_id).delete() #Off by default
        print(f"NOTE: The advisory {lookup[1]} was deleted")
    else:
        print(f"No existing advisory found. Cannot delete advisory {advisory_uid}")
        sys.exit()

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
        #"plain_content": f"{title}\n\n*Ref: {uid}*\n\nOverview\n\n{overview}\n\n{url}\n\nReporting\n\nAgencies whose cyber security teams have enrolled in the DGov Incident Reporting Portal (IRP) should raise an incident within the portal.\n\nThe Cyber Security Unit will liaise with the Australian Cyber Security Centre and other States and Territories in support of nation-wide incident coordination.\n\nFurther Information\n\nFor more information relating to this advisory, or for further information on connecting to the WASOC, please contact the Office of Digital Government - Cyber Security Unit at cybersecurity@dpc.wa.gov.au\n\n© 2023 Office of the Digital Government - Cyber Security Unit. All rights reserved.\nDumas House, 2 Havelock Street, WEST PERTH, WA 6005",
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

    print(f"\nAdvisory: {uid} - TLP CLEAR - {title} was uploaded to Sendgrid for review")
    # For Troubleshooting Send Grid API
    #print(response.status_code)
    #print(response.body)
    #print(response.headers)

def send_campaign (advisory_content):


    for source, advisory_md in advisory_content.items():
        if source.startswith(base_url):
            url = source
            print(f"\nCollecting advisory data from source: {source}")
        if source.endswith(".md"):
            url = base_url + source[:-3] + "/"
            print(f"\nCollecting advisory data from source: {source}")
        sections = advisory_md.split("##")
        title, overview = None, None

        for section in sections:
            if not title and section.startswith("#"):
                title = section[1:].strip()[:-14]
                    #raise ValueError(f"Advsisory {advisory_uid} - {title}: Title character count is longer than or equal to 100 Characters. Reduce the title length.")
            if section.strip().lower().startswith("overview"):
                overview = section[9:].strip()
                break
        if len(title) >= 100:
            print(f"\nERROR: Advisory '{advisory_uid} - {title}': The title character count is longer than or equal to 100 Characters. Reduce the Title Length.")
            print("\n-------------------------")
            break
        lookup = email_lookup(advisory_uid)
        if lookup[0] is True:
            # An Advisory already exists with this UID
            print("\nERROR: Advisory already exists. Requested advisory will be skipped.")
            print("\n-------------------------")
        else:
            html_overview = markdown(overview)
            html_filled = Template(Path("templates/tlp-clear-email-template.html").read_text()).substitute(title=title, overview=html_overview, url=url, uid=advisory_uid)
            #print(html_filled) # Reviewing the filled email template for sendgrid
            email_campaign(advisory_uid, title, html_overview, url, html_filled)
    

arguments = sys.argv[1:]

options = sys.argv[2:]

if len(arguments) < 1:
    print(f"Error: at least 1 argument expected, {len(arguments)} arguments given. Add a SOC Advisory URL, Advisory Markdown file or type '-b', '--bulk'")
    sys.exit()
if len(options) < 1 and arguments[0] not in ['-b', '--bulk', '-a', '--auto']: #or arguments[0] != '--auto':
    print(f"Error: at least 1 option expected, {len(arguments)} options given. Choose the following options: ('-n', '--new', '-d', '--delete', '-u', '--update')")
    sys.exit()



if sys.argv[1].startswith(base_url):
    # If a url is provided, find the relevant advisory and send it
    input_url = sys.argv[1]
    advisory_uid = re.search(r'(?<=advisories/)\d+(?=-)', input_url).group(0).strip()
    advisory_mds[input_url] = max(Path(f"docs/advisories").glob(f"{advisory_uid}-*.md")).read_text()
elif sys.argv[1].endswith(".md"):
    # If a markdown is provided, find the relevant content and send it
    markdown_file = sys.argv[1]
    advisory_uid = markdown_file[:11]
    advisory_mds[markdown_file] = max(Path(f"docs/advisories").glob(f"{advisory_uid}-*.md")).read_text()
elif sys.argv[1] == '-b' or sys.argv[1] == '--bulk':
    number_of_file = input("To bulk create sendgrid advisories, please enter the 'number' of latest advisories: ")
    all_files = Path("docs/advisories").glob("*.md")
    sorted_files = sorted(all_files, key=lambda item: item.name)
    requested_files = (sorted_files)[-int(number_of_file):]
    for file in requested_files:
        #print(f"{file}")
        advisory_uid = file.name[:11]
        content = {file.name:max(Path(f"docs/advisories").glob(f"{file.name}")).read_text()}
        send_campaign(content)
elif sys.argv[1] == '-a' or sys.argv[1] == '--auto':
    #look_back_time = time.strftime("%Y%m%d") #Current day lookback for advisories
    all_files = Path("docs/advisories").glob("*.md")
    sorted_files = sorted(all_files, key=lambda item: item.name)
    for i in range(0, 5):#Look back on the last 5 days worth of Advisories
        look_back_date = datetime.date.today() - datetime.timedelta(i)
        for file in sorted_files:
            if file.name[:8] == look_back_date.strftime("%Y%m%d"):
                advisory_uid = file.name[:11]
                content = {file.name:max(Path(f"docs/advisories").glob(f"{file.name}")).read_text()}
                send_campaign(content)
else:
    print(f"ERROR: Input {sys.argv[1]} doesn't start with {base_url} or is a markdown file or is contains type '-a', '--auto'")
    sys.exit()

if options:
    for option in options:
        if option not in ('-n', '--new', '-d', '--delete', '-u', '--update'):
            print(f"ERROR: {option} not available! Exiting Program")
            sys.exit()
    for option in options:
        if option == '-n' or option == '--new':
            print(f"New Option Selected - Manually creating advisory {advisory_uid}")
            send_campaign(advisory_mds)
        if option == '-u' or option == '--update':
            print(f"Update Option Selected - Deleting old advisory {advisory_uid} and then creating new {advisory_uid}")
            email_delete(advisory_uid)
            send_campaign(advisory_mds)
        if option == '-d' or option == '--delete':
            print(f"Delete Option selected - Deleting advisory {advisory_uid}")
            email_delete(advisory_uid)