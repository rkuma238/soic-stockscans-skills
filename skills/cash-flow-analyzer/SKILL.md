---
name: cash-flow-analyzer
description: "Evaluates cash flow quality: CFO vs PAT ratio, Free Cash Flow (FCF), Capex efficiency, and CFO-to-EBITDA conversion."
type: ATOMIC
version: 2.0.0
children: []
inputs:
  - company_data: object
  - periods: string[]
outputs:
  - cfo_quality: object
  - fcf_summary: object
  - capex_analysis: object
  - cash_quality_flag: string
---

# Cash Flow Analyzer

Evaluates cash generation quality, free cash flow (FCF), capex efficiency, and capital allocation strategy.

---

## Analysis Steps

### 1. CFO Quality & Earnings Conversion

| Metric | Formula | Benchmark |
|---|---|---|
| CFO to EBITDA | Operating Cash Flow / EBITDA | > 75–80% |
| CFO to Net Profit | Operating Cash Flow / PAT | > 1.0x rolling 3–5 years |

⚠ **Red Flag Trigger:** If PAT grows while CFO stagnates or turns negative over multiple years $\rightarrow$ `cash_quality_flag = RED` (indicates paper profits locked in working capital or aggressive revenue recognition).

### 2. Free Cash Flow (FCF) & Cumulative Convergence
- **Free Cash Flow Formula:** `FCF = Operating Cash Flow (CFO) – Capital Expenditure (Capex)`
- **FCF Yield:** `FCF / Market Cap (%)` — Higher yield provides a stronger valuation margin of safety.
- **Multi-Year Cumulative Test:** Compare 5-Year Cumulative PAT vs 5-Year Cumulative CFO vs 5-Year Cumulative FCF.
  - Cumulative CFO must equal or exceed Cumulative PAT.
  - Persistent negative multi-year FCF indicates high capital intensity or uncommissioned capex drag.

### 3. Capex Efficiency & Funding Audit

| Metric / Indicator | Interpretation |
|---|---|
| Capex / Depreciation > 1.0x | Growth phase (building new capacity) |
| Capex / Depreciation $\approx$ 1.0x | Maintenance phase |
| Capex Funding Source | Is Capex funded by Operating Cash Flow (CFO) or Debt/Financing Cash Flow (CFF)? |

### 4. Capital Allocation & Dividend Safety
- **Dividend Coverage Ratio:** `FCF / Total Dividend Outflow` (If <1.0x, dividend is funded by debt or cash reserves).
- Audit priority: Reinvestment in high-ROCE core business vs Debt reduction vs Dividend payout vs Share Buybacks.

### 5. Output
Return `cash_quality_flag` as `GREEN`, `AMBER`, or `RED`. Include 5-year FCF trend and CFO/PAT conversion metrics.
