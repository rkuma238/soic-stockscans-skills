---
name: bank-pipeline
description: "COMPOSITE pipeline for Scheduled Commercial Banks: bank-analyzer, tax-analysis, corporate-actions-analyzer, fraud-detection-forensics, cyclicality-analyzer."
type: COMPOSITE
version: 2.0.0
children:
  - bank-analyzer
  - tax-analysis
  - corporate-actions-analyzer
  - fraud-detection-forensics
  - cyclicality-analyzer
inputs:
  - company_data: object
  - cyclicality: string
  - periods: string[]
outputs:
  - income_summary: object
  - asset_quality: object
  - effective_tax_rate: object
  - governance_signal: string
  - fraud_risk_score: string
  - cyclicality_report: object
  - cycle_position: string
---

# Bank Analysis Pipeline (COMPOSITE)

```mermaid
graph TD
  Entry --> bank-analyzer
  bank-analyzer -->|status == PASS| tax-analysis
  bank-analyzer -->|status == FAILED| Failed

  tax-analysis -->|status == PASS| corporate-actions-analyzer
  tax-analysis -->|status == FAILED| Failed

  corporate-actions-analyzer -->|status == PASS| fraud-detection-forensics
  corporate-actions-analyzer -->|status == FAILED| Failed

  fraud-detection-forensics -->|status == PASS| cyclicality-analyzer
  fraud-detection-forensics -->|status == FAILED| Failed

  cyclicality-analyzer -->|status == PASS| Completed
  cyclicality-analyzer -->|status == FAILED| Failed
```
