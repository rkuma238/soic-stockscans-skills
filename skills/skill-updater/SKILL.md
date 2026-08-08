---
name: skill-updater
description: "Takes novel learnings extracted from the Telegram Knowledge Pipeline and injects them structurally into the appropriate ATOMIC skill (like sector-kpi-analyzer). Enforces MDC rules."
type: ATOMIC
version: 1.0.0
children: []
inputs:
  - learnings_json: object
  - target_skill: string
outputs:
  - patch_applied: boolean
  - diff_summary: string
---

# Skill Updater (Knowledge Injection Agent)

This skill safely modifies other OpenClaw `SKILL.md` files structurally based on new insights downloaded from the Telegram `"Research Reports"` channel pipeline.

## Execution Rules
1. Read the `new_kpis` and `new_subsectors_identified` from the `learnings_json`.
2. Locate the `target_skill` (e.g., `sector-kpi-analyzer`).
3. Using MDC-compliant markdown, append the new KPIs under the correct section (e.g. `### NEW_SECTOR`).
4. Ensure the modified file does **not** break YAML frontmatter.
5. Log the update to `.cursor/execution_dag.json` as `{"node": "skill-updater", "status": "COMPLETED", "patch": "..." }`.

## Validation
* Cannot rewrite `type: COMPOSITE` frontmatter.
* Must preserve acyclic requirements.
