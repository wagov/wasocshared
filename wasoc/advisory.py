"""Advisory parsing and SendGrid draft creation."""

from __future__ import annotations

import datetime as dt
import json
import os
import re
from dataclasses import dataclass
from pathlib import Path
from string import Template

from markdown import markdown
from sendgrid import SendGridAPIClient

from .common import (
    ADVISORY_BASE_URL,
    ADVISORY_DIR,
    EMAIL_TEMPLATE_PATH,
    document_title,
    titled_section,
)

SENDGRID_LIST_ID = "fdeb76e9-0895-4b5e-b929-4022f71cb16d"
SENDGRID_SENDER_ID = 5228194
TITLE_MAX_LENGTH = 100
AUTO_LOOKBACK_DAYS = 5


@dataclass(frozen=True)
class Advisory:
    uid: str
    title: str
    overview: str
    path: Path

    @property
    def url(self) -> str:
        return f"{ADVISORY_BASE_URL}{self.path.stem}/"


def sendgrid_client() -> SendGridAPIClient:
    """Return a SendGrid client, failing closed if the API key is missing."""
    api_key = os.environ.get("SENDGRID_API")
    if not api_key:
        raise SystemExit("ERROR: SENDGRID_API environment variable is not set")
    return SendGridAPIClient(api_key)


def advisory_uid_from_name(name: str) -> str:
    match = re.match(r"(?P<uid>\d{11})-", Path(name).name)
    if not match:
        raise ValueError(f"Could not find 11-digit advisory UID in {name}")
    return match.group("uid")


def advisory_uid_from_url(url: str) -> str:
    match = re.search(r"/advisories/(?P<uid>\d{11})-", url)
    if not match:
        raise ValueError(f"Could not find advisory UID in {url}")
    return match.group("uid")


def advisory_path_for_uid(uid: str) -> Path:
    try:
        return next(ADVISORY_DIR.glob(f"{uid}-*.md"))
    except StopIteration as exc:
        raise FileNotFoundError(f"No advisory markdown found for UID {uid}") from exc


def parse_advisory(path: Path) -> Advisory:
    """Return advisory metadata from markdown content."""
    markdown_text = path.read_text(encoding="utf-8-sig")
    title = document_title(markdown_text)
    overview = titled_section(markdown_text, "overview")

    if not title:
        raise ValueError("Advisory title not found")
    title = re.sub(r"\s+-\s+\d{11}$", "", title).strip()
    if not overview:
        raise ValueError(f"Overview section not found for advisory '{title}'")
    if len(title) >= TITLE_MAX_LENGTH:
        raise ValueError(
            f"Advisory '{title}' title length is {len(title)} characters; "
            f"it must be less than {TITLE_MAX_LENGTH} characters"
        )
    return Advisory(advisory_uid_from_name(path.name), title, overview, path)


def render_email(advisory: Advisory) -> str:
    return Template(EMAIL_TEMPLATE_PATH.read_text(encoding="utf-8")).substitute(
        title=advisory.title,
        overview=markdown(advisory.overview),
        url=advisory.url,
        uid=advisory.uid,
    )


def email_lookup(client: SendGridAPIClient, uid: str) -> tuple[bool, str, str | None]:
    response = client.client.marketing.singlesends.search.post(
        request_body={"name": uid}
    )
    results = json.loads(response.body).get("result", [])
    if not results:
        print("NOTE: No existing advisory found")
        return False, "", None

    result = results[0]
    name = result["name"]
    result_id = result.get("id")
    print(
        f"\nNOTE: The advisory '{name}' already exists and was sent at "
        f"'{result.get('send_at', '')}' with '{result.get('status', '')}' status. "
        f"SendGrid ID: {result_id}"
    )
    return True, name, result_id


def email_delete(client: SendGridAPIClient, uid: str) -> None:
    exists, name, result_id = email_lookup(client, uid)
    if not exists or not result_id:
        raise SystemExit(f"No existing advisory found. Cannot delete advisory {uid}")

    client.client.marketing.singlesends._(result_id).delete()
    print(f"NOTE: The advisory {name} was deleted")


def email_campaign(client: SendGridAPIClient, advisory: Advisory) -> None:
    data = {
        "name": f"{advisory.uid} - TLP CLEAR - {advisory.title}",
        "categories": ["wasoc-advisory"],
        "send_to": {"list_ids": [SENDGRID_LIST_ID], "segment_ids": [], "all": False},
        "email_config": {
            "subject": f"Cyber Security Advisory - TLP CLEAR - {advisory.title}",
            "html_content": render_email(advisory),
            "generate_plain_content": True,
            "editor": "design",
            "suppression_group_id": -1,
            "custom_unsubscribe_url": None,
            "sender_id": SENDGRID_SENDER_ID,
        },
    }
    client.client.marketing.singlesends.post(request_body=data)
    print(
        f"\nAdvisory: {advisory.uid} - TLP CLEAR - {advisory.title} "
        "was uploaded to SendGrid for review"
    )


def send_campaign(client: SendGridAPIClient, paths: list[Path]) -> None:
    for path in paths:
        print(f"\nCollecting advisory data from source: {path}")
        advisory = parse_advisory(path)
        exists, _, _ = email_lookup(client, advisory.uid)
        if exists:
            print(
                "\nERROR: Advisory already exists. Requested advisory will be skipped."
            )
            print("\n-------------------------")
            continue
        email_campaign(client, advisory)


def paths_from_source(source: str) -> list[Path]:
    if source.startswith(ADVISORY_BASE_URL):
        return [advisory_path_for_uid(advisory_uid_from_url(source))]

    path = Path(source)
    if path.suffix == ".md":
        return (
            [path]
            if path.is_file()
            else [advisory_path_for_uid(advisory_uid_from_name(path.name))]
        )

    raise ValueError(f"Input {source} is not a SOC advisory URL or markdown file")


def latest_advisory_paths(count: int) -> list[Path]:
    if count < 1:
        raise ValueError("Count must be at least 1")
    return sorted(ADVISORY_DIR.glob("*.md"), key=lambda item: item.name)[-count:]


def recent_advisory_paths(days: int = AUTO_LOOKBACK_DAYS) -> list[Path]:
    lookback_dates = {
        (dt.date.today() - dt.timedelta(days=offset)).strftime("%Y%m%d")
        for offset in range(days)
    }
    return [
        path
        for path in sorted(ADVISORY_DIR.glob("*.md"), key=lambda item: item.name)
        if path.name[:8] in lookback_dates
    ]
