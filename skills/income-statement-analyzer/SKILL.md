---
name: income-statement-analyzer
description: "Analyzes P&L metrics: 8-quarter QoQ trend, revenue growth (YoY/QoQ/MoM), volume vs margin growth breakdown, gross/EBITDA/PAT margins, operating leverage, interest coverage, and earnings quality."
type: ATOMIC
version: 2.2.0
children: []
inputs:
  - company_data: object
  - periods: string[]
outputs:
  - pl_summary: object
  - qoq_summary: object
  - margin_vs_volume: object
  - operating_leverage: string
  - earnings_quality_flag: string
  - segmental_analysis: object
---

# Income Statement Analyzer

Performs deep multi-period P&L analysis for corporate companies, evaluating 8-quarter QoQ trends, top-line volume vs margin growth drivers, operating leverage, interest cost escalation, and segmental performance dynamics.

---

## Analysis Steps

### 1. 8-Quarter Sequential (QoQ) Financial Audit (MANDATORY)
Construct a complete 8-Quarter QoQ Financial Table:

| Metric (₹ Cr) | Q1FY25 | Q2FY25 | Q3FY25 | Q4FY25 | Q1FY26 | Q2FY26 | Q3FY26 | Q4FY26 | QoQ % (Q4) | YoY % (Q4) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Gross Sales** | `{Q1_25}` | `{Q2_25}` | `{Q3_25}` | `{Q4_25}` | `{Q1_26}` | `{Q2_26}` | `{Q3_26}` | `{Q4_26}` | `{QoQ_Rev}%` | `{YoY_Rev}%` |
| **EBITDA** | `{Q1_E}` | `{Q2_E}` | `{Q3_E}` | `{Q4_E}` | `{Q1_E2}` | `{Q2_E2}` | `{Q3_E2}` | `{Q4_E2}` | `{QoQ_E}%` | `{YoY_E}%` |
| **OPM %** | `{Q1_OPM}`| `{Q2_OPM}`| `{Q3_OPM}`| `{Q4_OPM}`| `{Q1_OPM2}`| `{Q2_OPM2}`| `{Q3_OPM2}`| `{Q4_OPM2}`| `{OPM_Change}`| `{YoY_OPM}` |
| **Net Profit**| `{Q1_PAT}`| `{Q2_PAT}`| `{Q3_PAT}`| `{Q4_PAT}`| `{Q1_PAT2}`| `{Q2_PAT2}`| `{Q3_PAT2}`| `{Q4_PAT2}`| `{QoQ_PAT}%`| `{YoY_PAT}%`|
| **EPS (₹)** | `{Q1_EPS}`| `{Q2_EPS}`| `{Q3_EPS}`| `{Q4_EPS}`| `{Q1_EPS2}`| `{Q2_EPS2}`| `{Q3_EPS2}`| `{Q4_EPS2}`| — | — |

### 2. Margin vs Volume Growth Story (MANDATORY BREAKDOWN)
Deconstruct top-line growth into its twin engines:
- **Volume-Driven Growth (%)**: Revenue expanded by new reactor throughput, active batch dispatches, or commercial client count.
- **Margin/Realisation-Driven Growth (%)**: Revenue/EBITDA expanded by product mix shift (high-margin CDMO vs bulk API), pricing power, or raw material cost deflation.
- State explicitly: *"Is the company's growth story driven by Volume Scaling or Margin Expansion?"*

### 3. Mandatory Segmental Performance Audit (Push vs Pull Dynamics)
Construct segment-wise Revenue and EBITDA table detailing:
- **Segment Pulling Performance Down**: Division dragging margin/revenue down.
- **Segment Pushing Growth Up**: Division driving top-line/margin expansion.

### 4. Below-EBITDA Line Items & Solvency Watch
- **Depreciation Trajectory:** Track depreciation growth alongside Gross Block additions.
- **Interest Cost Escalation:** YoY % increase in interest expense relative to debt growth.
- **Interest Coverage Ratio:** `EBIT / Interest Expense` — **RED FLAG** if < 3.0x.

### 5. Output
Return structured `pl_summary`, `qoq_summary`, and `margin_vs_volume` breakdown object. Flag `earnings_quality_flag` as `GREEN`, `AMBER`, or `RED`.
