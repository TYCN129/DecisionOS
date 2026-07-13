#!/usr/bin/env python3

"""
DecisionOS
generate_dashboard.py

Generates the dashboard state used by GitHub Pages.

This script copies the canonical runtime state
(state/state.json) into docs/state.json after validating it.

Author: DecisionOS
"""

from __future__ import annotations

import json
import shutil
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent

MASTER_STATE = ROOT / "state" / "state.json"

DASHBOARD_STATE = ROOT / "docs" / "state.json"


REQUIRED_TOP_LEVEL_KEYS = [
    "system",
    "user",
    "north_star",
    "campaign",
    "week",
    "today",
    "execution",
    "health",
    "oracle",
    "personal_brand",
    "business",
    "career",
    "finance",
    "relationships",
    "metrics",
    "compass",
    "autopilot",
    "recovery",
    "dashboard"
]


class DashboardGenerator:

    def __init__(self):

        self.state = self.load_state()

    def load_state(self):

        if not MASTER_STATE.exists():
            raise FileNotFoundError(
                f"Missing runtime state: {MASTER_STATE}"
            )

        with open(
            MASTER_STATE,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)

    def validate(self):

        missing = []

        for key in REQUIRED_TOP_LEVEL_KEYS:

            if key not in self.state:
                missing.append(key)

        if missing:

            raise ValueError(
                f"Missing required keys: {missing}"
            )

    def prepare_dashboard(self):

        self.state["system"]["last_updated"] = (
            datetime.now().isoformat()
        )

    def publish(self):

        with open(
            DASHBOARD_STATE,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                self.state,
                f,
                indent=4,
                ensure_ascii=False
            )

    def run(self):

        self.validate()

        self.prepare_dashboard()

        self.publish()


def copy_master_state():

    shutil.copy2(
        MASTER_STATE,
        DASHBOARD_STATE
    )


def main():

    generator = DashboardGenerator()

    generator.run()

    print("Dashboard successfully generated.")

    print(f"Output: {DASHBOARD_STATE}")


if __name__ == "__main__":

    main()