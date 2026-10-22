# Versioning and Research Preservation

This repository versions **manuscripts** separately from **experimental implementations**.

## Manuscript versions

Manuscripts are stored in immutable, numbered directories:

- `paper/v0.1.0/` — first public working draft (October 2026).
- `paper/v0.2.0/`, etc. — future research expansions or substantial revisions.
- `paper/v1.0.0/` — a future author-designated full version, if issued. Version numbers do not imply peer review.

The version number follows MAJOR.MINOR.PATCH:
- **PATCH**: typographic, layout, or reference corrections without changing the argument or evidence.
- **MINOR**: additional experiments, interpretation, evidence, sections, or substantive clarification while the manuscript remains in development.
- **MAJOR**: the author declares a new foundational manuscript or a major revision to the argument.

**Never overwrite** a previously published versioned manuscript. Publish a new numbered folder. `paper/LATEST.md` is a pointer, not the archival record.

## Experiment versions

Experiment `v1` to `v5` identify historical implementations, **not** manuscript versions:

| Version | Development | Run represented |
|---|---|---|
| v1 | 2D square, collision-generated balls, growth, persistent/fading trails | 17 s |
| v2 | One observer tracks original c and records encounters | 17 s |
| v3 | Projected 3D cube with X/Y/Z motion | 17 s |
| v4 | Three observer identities, separate encounter records | 17 s |
| v5 | Adjustable duration and speed; three-observer 3D cube | 60 s, half-speed sample |

Preserve each implementation and its recorded logs as a dated snapshot. Bug fixes or new features belong in a new experiment version; commentary about a historical mistake belongs in documentation that does not silently rewrite the original.

## Evidence boundaries

Distinguish **implemented mechanisms** from **theoretical interpretations**. The original generated c is an object and a traceable product of an A–B collision. The proposal that c represents question potential is an interpretation. In the archived simulation, growth is triggered by ordinary-ball collisions. D–c events record encounters, not actual linguistic questions.

## Reproducibility and integrity

Provide for each run: source code, dependencies, seed, frame rate, duration, speed control, event log, screenshots/video where available, and SHA-256 checksums. A repeated run that matches event output is computational reproducibility, not independent empirical validation.

## Public release and licensing

Public repository visibility permits reading the files. Reuse/distribution permissions depend on an explicitly chosen license. No license has been selected for this repository at the time of initial publication.
