---
name: obsidian-publisher
description: "Takes analyzed equity research outputs and formats them iteratively into an Obsidian Vault markdown file. Injects YAML frontmatter for QoQ/YoY historical querying via Dataview."
type: ATOMIC
version: 1.0.0
children: []
inputs:
  - company_name: string
  - quarter: string
  - year: string
  - sector: string
  - analysis_output: string
outputs:
  - vault_path_created: string
---

# Obsidian Publisher (Vault Sync)

This skill takes the final output of the `ra-report-synthesizer` or `knowledge_extractor` and pushes it into the user's localized Obsidian Vault for permanent, linked retention.

## Execution Rules
1. Target Vault: `~/OpenClaw_Research_Vault/`
2. Create folder structure: `<Target Vault>/<sector>/<company_name>/` (make directory if it doesn't exist).
3. Generate Filename: `<year>_<quarter>_Results.md`
4. Inject standard YAML frontmatter exactly as:
```yaml
---
company: "{company_name}"
quarter: "{quarter}"
year: "{year}"
sector: "{sector}"
tags: ["equity-research", "financial-results", "{year}", "{quarter}", "{sector}"]
---
```
5. Append `analysis_output` body below frontmatter.
6. Return `vault_path_created` on success.
7. Log success to `.cursor/execution_dag.json`.
