#!/usr/bin/env python3

"""
DecisionOS
archive_campaign.py

Archives the current campaign into campaigns/archive/
and creates a fresh current.md from the campaign template.

Author: DecisionOS
"""

from __future__ import annotations

import shutil
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent

CURRENT_CAMPAIGN = ROOT / "campaigns" / "current.md"
ARCHIVE_DIR = ROOT / "campaigns" / "archive"
CAMPAIGN_TEMPLATE = ROOT / "templates" / "campaign.md"


class CampaignArchiver:

    def __init__(self):

        ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)

    def archive(self):

        if not CURRENT_CAMPAIGN.exists():
            raise FileNotFoundError(
                "Current campaign does not exist."
            )

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        destination = (
            ARCHIVE_DIR /
            f"campaign_{timestamp}.md"
        )

        shutil.copy2(
            CURRENT_CAMPAIGN,
            destination
        )

        print(f"Archived campaign -> {destination.name}")

    def reset_current_campaign(self):

        shutil.copy2(
            CAMPAIGN_TEMPLATE,
            CURRENT_CAMPAIGN
        )

        print("Created fresh current campaign.")

    def run(self):

        self.archive()

        self.reset_current_campaign()


def main():

    archiver = CampaignArchiver()

    archiver.run()

    print("Campaign archive complete.")


if __name__ == "__main__":
    main()