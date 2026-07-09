#!/usr/bin/env python3

from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))

from planning.task_planner import TaskPlanner
from planning.tasks.tasks import PickTask

planner = TaskPlanner()

planner.solve(PickTask("e2"))
