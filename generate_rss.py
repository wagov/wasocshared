# # Generate an RSS feed of last 90 days of markdown files changed in the repository
# Using git, find last 90 days of changed files, exclude some noisy ones and publish as an RSS/ATOM feed

from pathlib import Path
from subprocess import run
from feedgen.feed import FeedGenerator

# +
base_url = "https://soc.cyber.wa.gov.au"

def get_meta(path):
    doc = path.read_text().split("\n\n")
    updated = run(["git", "log", "-1", '--pretty=format:%ci', path], capture_output=True).stdout.decode("utf8").strip()
    title = doc[0].replace("#", "").strip()
    for i, row in enumerate(doc):
        if row.startswith("##"):
            overview_index = i + 1
            break
    else:
        raise ValueError("Can't find overview")
    overview = doc[overview_index]
    url_path = path.relative_to("docs").with_suffix("")
    category = url_path.parts[0]
    url = f"{base_url}/{url_path}"
    return { "title": title, "url": url, "overview": overview, "updated": updated, "category": category }


# -

recent = run(["git", "whatchanged", "@{180 days ago}", "--oneline", "--name-only", "--pretty=format:"], capture_output=True).stdout.decode("utf8").split("\n")
# Exclude ADS form updates
recent = [Path(p) for p in recent if p.find("/ADS_forms/") < 0 and Path(p).suffix == ".md" and Path(p).is_file()]
recent = list(dict.fromkeys(recent))
latest_updated = run(["git", "log", "-1", '--pretty=format:%ci', recent[0]], capture_output=True).stdout.decode("utf8").strip()

# +
fg = FeedGenerator()
fg.id(base_url)
fg.title('WA SOC Alerts & Updates')
fg.description('This site contains technical information to support WA Government Cyber Security activities. Please propose updates directly via the edit link on each page or email cybersecurity@dpc.wa.gov.au with any feedback.')
fg.author( {'name':'WA SOC','email':'cybersecurity@dpc.wa.gov.au'} )
fg.updated(latest_updated)
fg.link( href=base_url, rel='alternate' )
fg.language('en')

for path in reversed(recent):
    try:
        doc_meta = get_meta(path)
    except ValueError:
        continue
    fe = fg.add_entry()
    fe.id(doc_meta["url"])
    fe.title(doc_meta["title"])
    fe.author( {'name':'WA SOC','email':'cybersecurity@dpc.wa.gov.au'} )
    fe.description(doc_meta["overview"])
    fe.category(term=doc_meta["category"])
    fe.updated(doc_meta["updated"])
    fe.link(href=doc_meta["url"])
# -

fg.atom_file("site/atom.xml")
fg.rss_file("site/rss.xml")
