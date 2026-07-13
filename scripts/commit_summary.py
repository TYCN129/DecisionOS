#!/usr/bin/env python3

"""
DecisionOS
commit_summary.py

Generates a standardized Git commit message from the
current runtime state.

Example:

Week 03 | Authentication Complete

Mission:
Finish Authentication

Artifact:
Authentication Flow

Observation:
Research exceeded implementation

Recommendation:
Research only after implementation

Author: DecisionOS
"""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent

STATE_FILE = ROOT / "state" / "state.json"


class CommitSummary:

    def __init__(self):

        with open(
            STATE_FILE,
            "r",
            encoding="utf-8"
        ) as f:

            self.state = json.load(f)

    def generate_title(self):

        week = self.state["campaign"]["week"]

        artifact = self.state["today"]["artifact"]

        if artifact.strip() == "":
            artifact = "Daily Update"

        return f"Week {week:02d} | {artifact}"

    def generate_body(self):

        today = self.state["today"]

        autopilot = self.state["autopilot"]

        lines = []

        lines.append("")
        lines.append(f"Mission:")
        lines.append(f"{today['mission']}")
        lines.append("")

        lines.append("Success Definition:")
        lines.append(today["success_definition"])
        lines.append("")

        lines.append("Artifact:")
        lines.append(today["artifact"])
        lines.append("")

        lines.append("Observation:")
        lines.append(
            autopilot["last_observation"]
        )
        lines.append("")

        lines.append("Root Cause:")
        lines.append(
            autopilot["root_cause"]
        )
        lines.append("")

        lines.append("Recommendation:")
        lines.append(
            autopilot["recommendation"]
        )

        return "\n".join(lines)

    def print(self):

        print(self.generate_title())
        print(self.generate_body())


def main():

    CommitSummary().print()


if __name__ == "__main__":
    main()