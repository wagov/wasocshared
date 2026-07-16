"""MkDocs macros for the WA SOC shared guidance site."""

from __future__ import annotations

import datetime as dt
from itertools import groupby
from pathlib import Path

from wasoc.common import first_heading_text

macro_cache: dict[str, str] = {}
MITRE_BASE_URL = "https://attack.mitre.org"


def normalise_mitre_id(mitre_id: object) -> str:
    """Return a MITRE ID string, including when Jinja passed an Undefined name."""
    if isinstance(mitre_id, str):
        return mitre_id
    undefined_name = getattr(mitre_id, "_undefined_name", None)
    return str(undefined_name or mitre_id)


def attack_url(mitre_id: str) -> str | None:
    categories = {
        "TA": "tactics",
        "T": "techniques",
        "S": "software",
        "G": "groups",
        "C": "campaigns",
    }
    category = next(
        (
            category
            for prefix, category in categories.items()
            if mitre_id.startswith(prefix)
        ),
        None,
    )
    return (
        None
        if category is None
        else f"{MITRE_BASE_URL}/{category}/{mitre_id.replace('.', '/')}/"
    )


def attack_link(mitre_id: object) -> str:
    """Render a MITRE ATT&CK ID as a deterministic link without network access."""
    mitre_id = normalise_mitre_id(mitre_id)
    url = attack_url(mitre_id)
    if url is None:
        return f"Unknown MITRE ATT&CK ID: {mitre_id}"
    return f"[{mitre_id}]({url})"


def month_heading(month: str) -> str:
    """Return a YYYY Month heading from a YYYYMM filename prefix."""
    return dt.datetime.strptime(month + "01", "%Y%m%d").strftime("%Y %B")


def define_env(env):
    """Register mkdocs-macros macros."""

    @env.macro
    def date_index(folder, prefix="", expand=3, include=None):
        """Insert a month-grouped index for markdown files in a docs folder."""
        glob = f"{folder}/*.md"
        cachekey = f"date_index.{glob}.{prefix}.{expand}.{include}"
        if cachekey in macro_cache:
            return macro_cache[cachekey]

        mdtext = []
        files = sorted(Path(env.project_dir).glob(glob), reverse=True)
        months = groupby(files, key=lambda file: file.name[0:6])

        for month_count, (month, paths) in enumerate(months):
            if month_count < expand:
                indent = ""
                mdtext.append(f"#### {month_heading(month)}")
            else:
                indent = "    "
                mdtext.append(f'??? note "{month_heading(month)}"')
            mdtext.append("")

            for path in paths:
                mdtext.append(
                    f"{indent}- [{first_heading_text(path)}]({prefix}{path.name})"
                )

            if include is not None and month_count + 1 > include:
                break

        macro_cache[cachekey] = "\n".join(mdtext)
        return macro_cache[cachekey]

    @env.macro
    def mitre(mitre_id):
        """Render a MITRE ATT&CK ID as a deterministic link."""
        mitre_id = normalise_mitre_id(mitre_id)
        cachekey = f"mitre.{mitre_id}"
        if cachekey not in macro_cache:
            macro_cache[cachekey] = attack_link(mitre_id)
        return macro_cache[cachekey]
