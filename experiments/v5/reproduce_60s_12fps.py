#!/usr/bin/env python3
"""Reproduce the archived Version 5 60-second, half-speed sample at 12 FPS.

This wrapper leaves the historical V5 source file unchanged.
"""
import importlib.util
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SCRIPT = HERE / "question_origination_cube_v5.py"
spec = importlib.util.spec_from_file_location("question_origination_cube_v5", SCRIPT)
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)
module.FPS = 12

result = module.generate(
    output=str(HERE / "question_origination_cube_v5_60s_slow.mp4"),
    seconds=60.0,
    seed=14,
    log_path=str(HERE / "question_origination_cube_v5_60s_slow_events.json"),
    no_video=False,
    capture_times=[10, 30, 50],
    speed_scale=0.5,
)
print(result["final"])
