#!/usr/bin/env python3
from subprocess import run, check_output
from datetime import datetime, timedelta
run("az config set extension.use_dynamic_install=yes_without_prompt", shell=True)
expiry = (datetime.utcnow() + timedelta(days=45)).isoformat().split("T")[0]
sas = check_output(f"az storage container generate-sas --connection-string $AZURE_STORAGE_CONNSTRING --permissions lr --expiry {expiry} --name tlp-green -o tsv", shell=True).decode("utf-8").strip()

for path in ["tlp-green/sas_link.txt", "tlp-green/reportcontent/soc-update.md"]:
    content = open(path, "r").read()
    with open(path, "w") as f:
        f.write(content.replace("{sas}", sas))

run("az storage blob sync -c tlp-green -s . --exclude-path .git", shell=True)
