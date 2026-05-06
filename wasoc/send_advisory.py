#!/usr/bin/env python3
"""Create SendGrid single-send drafts for WA SOC advisories."""

from __future__ import annotations

import argparse
import sys

from wasoc.advisory import (
    email_delete,
    latest_advisory_paths,
    paths_from_source,
    recent_advisory_paths,
    send_campaign,
    sendgrid_client,
)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument(
        "--auto", "-a", action="store_true", help="create drafts for recent advisories"
    )
    mode.add_argument(
        "--bulk",
        "-b",
        nargs="?",
        const=0,
        type=int,
        metavar="COUNT",
        help="create drafts for the latest COUNT advisories",
    )
    mode.add_argument(
        "source", nargs="?", help="SOC advisory URL or advisory markdown file"
    )
    parser.add_argument(
        "--action",
        "-x",
        choices=("new", "update", "delete"),
        default="new",
        help="operation for a manual source (default: new)",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)

    try:
        client = sendgrid_client()
        if args.auto:
            paths = recent_advisory_paths()
            if not paths:
                print(
                    "NOTE: No recent advisories found for automatic "
                    "SendGrid draft creation"
                )
            send_campaign(client, paths)
            return 0

        if args.bulk is not None:
            count = args.bulk or int(
                input(
                    "To bulk create SendGrid advisories, enter the "
                    "number of latest advisories: "
                )
            )
            send_campaign(client, latest_advisory_paths(count))
            return 0

        paths = paths_from_source(args.source)
        uid = paths[0].name.split("-", 1)[0]
        if args.action in {"delete", "update"}:
            email_delete(client, uid)
        if args.action in {"new", "update"}:
            send_campaign(client, paths)
        return 0
    except (FileNotFoundError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
