# -*- coding: utf-8 -*-
"""Utilities for the Orion Avto Yandex feed.

The feed URL is fixed and is not modified by this script:
https://raw.githubusercontent.com/dessmond29-star/orion-avto-feed/main/feed.xml
"""

import argparse
from datetime import datetime
from pathlib import Path
from xml.etree import ElementTree as ET

FEED_URL = "https://raw.githubusercontent.com/dessmond29-star/orion-avto-feed/main/feed.xml"
BASE_DIR = Path(__file__).resolve().parent
FEED_PATH = BASE_DIR / "feed.xml"


def check_feed(path: Path = FEED_PATH) -> None:
    if not path.exists():
        raise FileNotFoundError(path)

    root = ET.parse(path).getroot()
    if root.tag != "yml_catalog":
        raise ValueError("Root element must be yml_catalog")

    offers = root.findall("./offers/offer")
    if not offers:
        raise ValueError("Feed contains no offers")

    for offer in offers:
        if not offer.get("id"):
            raise ValueError("Every offer must have an id")

    print(f"OK: {len(offers)} offers")


def refresh_date(path: Path = FEED_PATH) -> None:
    root = ET.parse(path).getroot()
    root.set("date", datetime.now().strftime("%Y-%m-%d %H:%M"))
    ET.indent(root, space="  ")
    tree = ET.ElementTree(root)
    tree.write(path, encoding="utf-8", xml_declaration=True)
    print(f"Updated date: {root.get('date')}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Validate feed.xml")
    parser.add_argument("--refresh-date", action="store_true", help="Update yml_catalog date only")
    args = parser.parse_args()

    if args.check:
        check_feed()
    if args.refresh_date:
        refresh_date()


if __name__ == "__main__":
    main()
