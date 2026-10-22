# Reproducing the computational demonstrations

## Requirements

The archived programs are Python scripts. The environment used for the October 2026 demonstrations included Python 3.13.5, NumPy 2.3.5, OpenCV 4.13.0 and FFmpeg 7.1.5. Results on other versions may need confirmation.

Install:

```bash
python -m pip install numpy==2.3.5 opencv-python==4.13.0.92
```

FFmpeg is optional for some scripts, but is used to produce H.264 MP4 output.

## Runs

Use each archived script without changing its source. The programs generally accept a random seed, an output filename and a duration. Consult each script's `--help` for the exact controls available.

**V1:** 2D square, 17 seconds; initial A/B collision, generated balls, growth and trails.

**V2:** single D observer, 17 seconds, seed 14; generates a structured JSON event log.

**V3:** projected 3D cube, 17 seconds, seed 14.

**V4:** projected 3D cube with D1/D2/D3, 17 seconds, seed 14.

**V5:** 60-second half-speed sample was rendered at **12 FPS**, not at the V5 source default of 30 FPS. Use the companion [12 FPS reproduction wrapper](experiments/v5/reproduce_60s_12fps.py) from the same directory (or consult its source). It loads the original V5 script, applies `FPS=12` for this sample and calls the unmodified `generate` function with duration=60, speed_scale=0.5 and seed=14.

Run from `experiments/v5/`:

```bash
python reproduce_60s_12fps.py
```

## Recorded results

See [data/run_summary.csv](data/run_summary.csv). The table reports single recorded executions, not averages over multiple trials. Source scripts, input conditions, contact cooldown and population limit determine the motion and event logs.

The experiment records D–c **encounters**. Those event records do not show an actual question being asked. A later conceptual interpretation of c as potential question-state is kept separate from the computational output.

## Data publication status

The full original JSON logs (V2–V5), simulation MP4s, screenshot figures and illustrated PDF are in the supplementary deposition bundle prepared with this release. Their file bytes and SHA-256 checksums are not yet published directly in this repository. Do not infer their publication from the directory descriptions.
