---
name: nbfc-pipeline
description: "COMPOSITE pipeline for NBFCs, HFCs, and MFIs: nbfc-analyzer, tax-analysis, corporate-actions-analyzer, fraud-detection-forensics, cyclicality-analyzer."
type: COMPOSITE
version: 2.0.0
children:
  - nbfc-analyzer
  - tax-analysis
  - corporate-actions-analyzer
  - fraud-detection-forensics
  - cyclicality-analyzer
inputs:
  - company_data: object
  - cyclicality: string
  - periods: string[]
outputs:
  - aum_summary: object
  - asset_quality: object
  - effective_tax_rate: object
  - governance_signal: string
  - fraud_risk_score: string
  - cyclicality_report: object
  - cycle_position: string
---

# NBFC Analysis Pipeline (COMPOSITE)

```mermaid
graph TD
  Entry --> nbfc-analyzer
  nbfc-analyzer -->|status == PASS| tax-analysis
  nbfc-analyzer -->|status == FAILED| Failed

  tax-analysis -->|status == PASS| corporate-actions-analyzer
  tax-analysis -->|status == FAILED| Failed

  corporate-actions-analyzer -->|status == PASS| fraud-detection-forensics
  corporate-actions-analyzer -->|status == FAILED| Failed

  fraud-detection-forensics -->|status == PASS| cyclicality-analyzer
  fraud-detection-forensics -->|status == FAILED| Failed

  cyclicality-analyzer -->|status == PASS| Completed
  cyclicality-analyzer -->|status == FAILED| Failed
```
