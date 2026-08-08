---
name: normal-company-pipeline
description: "COMPOSITE pipeline for all normal corporate companies: runs income-statement, balance-sheet, cash-flow, sector-kpi, tax-analysis, corporate-actions, delivery-volume-analyzer, fraud-detection, and cyclicality-analyzer."
type: COMPOSITE
version: 3.1.0
children:
  - income-statement-analyzer
  - balance-sheet-analyzer
  - cash-flow-analyzer
  - sector-kpi-analyzer
  - tax-analysis
  - corporate-actions-analyzer
  - delivery-volume-analyzer
  - fraud-detection-forensics
  - cyclicality-analyzer
inputs:
  - company_data: object
  - sector: string
  - cyclicality: string
  - periods: string[]
outputs:
  - pl_summary: object
  - capital_structure: object
  - fcf_summary: object
  - working_capital: object
  - segmental_analysis: object
  - sector_kpis: object
  - effective_tax_rate: object
  - delivery_summary_table: object
  - unusual_volume_events: object
  - governance_signal: string
  - fraud_risk_score: string
  - cyclicality_report: object
  - cycle_position: string
---

# Normal Company Analysis Pipeline (COMPOSITE)

Executes multi-statement quantitative, working capital days, cash flow conversion, segmental push/pull, 30-40 day delivery volume microstructure, and forensic auditing for corporate companies.

```mermaid
graph TD
  Entry --> income-statement-analyzer
  income-statement-analyzer -->|status == PASS| balance-sheet-analyzer
  income-statement-analyzer -->|status == FAILED| Failed

  balance-sheet-analyzer -->|status == PASS| cash-flow-analyzer
  balance-sheet-analyzer -->|status == FAILED| Failed

  cash-flow-analyzer -->|status == PASS| sector-kpi-analyzer
  cash-flow-analyzer -->|status == FAILED| Failed

  sector-kpi-analyzer -->|status == PASS| tax-analysis
  sector-kpi-analyzer -->|status == FAILED| Failed

  tax-analysis -->|status == PASS| corporate-actions-analyzer
  tax-analysis -->|status == FAILED| Failed

  corporate-actions-analyzer -->|status == PASS| delivery-volume-analyzer
  corporate-actions-analyzer -->|status == FAILED| Failed

  delivery-volume-analyzer -->|status == PASS| fraud-detection-forensics
  delivery-volume-analyzer -->|status == FAILED| Failed

  fraud-detection-forensics -->|status == PASS| cyclicality-analyzer
  fraud-detection-forensics -->|status == FAILED| Failed

  cyclicality-analyzer -->|status == PASS| Completed
  cyclicality-analyzer -->|status == FAILED| Failed
```

