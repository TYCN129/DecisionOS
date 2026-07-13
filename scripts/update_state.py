#!/usr/bin/env python3

"""
DecisionOS
update_state.py

Updates the master runtime state after a DecisionOS protocol
(Daily Review, Weekly Review, Campaign Review or Recovery).

Author: DecisionOS
"""

from __future__ import annotations

import json
import shutil
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent

STATE_FILE = ROOT / "state" / "state.json"

DASHBOARD_STATE = ROOT / "docs" / "state.json"


class StateManager:

    def __init__(self):

        self.state = self.load()

    def load(self):

        with open(STATE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)

    def save(self):

        self.state["system"]["last_updated"] = datetime.now().isoformat()

        with open(
            STATE_FILE,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                self.state,
                f,
                indent=4,
                ensure_ascii=False
            )

    def publish_dashboard(self):

        shutil.copy2(
            STATE_FILE,
            DASHBOARD_STATE
        )

    def set_today(self,
                  mission=None,
                  artifact=None,
                  success_definition=None):

        if mission is not None:
            self.state["today"]["mission"] = mission

        if artifact is not None:
            self.state["today"]["artifact"] = artifact

        if success_definition is not None:
            self.state["today"]["success_definition"] = success_definition

    def complete_mission(self):

        self.state["execution"]["mission_completed"] = True

    def complete_artifact(self):

        self.state["execution"]["artifact_created"] = True

        self.state["metrics"]["artifacts_this_week"] += 1

        self.state["metrics"]["artifacts_this_campaign"] += 1

    def log_sleep(self, hours):

        self.state["health"]["sleep_hours"] = hours

    def complete_gym(self):

        self.state["health"]["gym_completed"] = True

    def set_energy(self, energy):

        self.state["health"]["energy"] = energy

    def set_nutrition(self, nutrition):

        self.state["health"]["nutrition"] = nutrition

    def set_attention(self, attention_dict):

        self.state["compass"]["attention"] = attention_dict

    def autopilot(self,
                  observation,
                  root_cause,
                  recommendation):

        self.state["autopilot"]["last_observation"] = observation

        self.state["autopilot"]["root_cause"] = root_cause

        self.state["autopilot"]["recommendation"] = recommendation

    def activate_recovery(self,
                          level,
                          reason):

        self.state["system"]["mode"] = "RECOVERY"

        self.state["recovery"]["active"] = True

        self.state["recovery"]["level"] = level

        self.state["recovery"]["reason"] = reason

        self.state["recovery"]["started_on"] = datetime.now().strftime(
            "%Y-%m-%d"
        )

        self.state["metrics"]["recovery_days"] += 1

    def deactivate_recovery(self):

        self.state["system"]["mode"] = "NORMAL"

        self.state["recovery"]["active"] = False

        self.state["recovery"]["level"] = 0

        self.state["recovery"]["reason"] = ""

        self.state["recovery"]["started_on"] = None

    def initialize(self):

        self.state["system"]["initialized"] = True


def main():

    manager = StateManager()

    manager.initialize()

    manager.save()

    manager.publish_dashboard()

    print("DecisionOS state updated successfully.")


if __name__ == "__main__":

    main()