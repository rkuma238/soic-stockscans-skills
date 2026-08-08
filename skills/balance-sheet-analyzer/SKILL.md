---
name: balance-sheet-analyzer
description: "Analyzes balance sheet health: capital structure, D/E, ROCE/ROE, Cash Conversion Cycle, and working capital days."
type: ATOMIC
version: 2.0.0
children: []
inputs:
  - company_data: object
  - periods: string[]
outputs:
  - capital_structure: object
  - working_capital: object
  - efficiency_ratios: object
  - leverage_flag: string
---

# Balance Sheet Analyzer

Analyzes balance sheet solvency, capital structure, efficiency ratios, working capital cycles, and asset quality.

---

## Analysis Steps

### 1. Capital Structure & Debt Safety

| Metric | Formula | Risk Benchmark |
|---|---|---|
| Debt-to-Equity (D/E) | Total Debt / Shareholders Equity | < 0.5x ideal, > 1.0x high risk |
| Net Debt | Total Debt – Cash & Liquid Investments | Negative = Net Cash balance sheet |
| Interest Coverage | EBIT / Interest Expense | > 3.0x safe, < 2.0x severe stress |
| Debt Growth vs Sales Growth | Debt YoY % vs Revenue YoY % | Debt growing faster than sales = RED FLAG |

### 2. Capital Efficiency (Return Ratios)

| Metric | Formula | Benchmark |
|---|---|---|
| ROCE | EBIT / (Total Assets – Current Liabilities) | > 15-20% ideal (compare vs WACC ~11%) |
| ROE | Net Profit / Average Shareholders' Equity | > 15% ideal |
| Fixed Asset Turnover | Revenue / Gross Fixed Assets | Declining ratio = asset inefficiency |

### 3. Working Capital & Cash Conversion Cycle (CCC)

| Metric | Formula | Target |
|---|---|---|
| Receivable Days (DSO) | (Avg Receivables / Revenue) × 365 | Stable or declining |
| Inventory Days | (Avg Inventory / COGS or Sales) × 365 | Spiking = demand slowdown / overhang |
| Payable Days | (Avg Payables / COGS or Sales) × 365 | Stretched payables = vendor pressure |
| Cash Conversion Cycle (CCC) | Inventory Days + DSO – Payable Days | Shorter cycle = faster cash generation |

**MANDATORY INVENTORY BREAKDOWN:** Audit Inventory into Raw Materials (RM), Work-In-Progress (WIP), and Finished Goods (FG). Spiking FG alongside falling RM indicates severe end-market demand drop and potential inventory write-downs.

### 4. Asset Quality & CWIP Audit
- **CWIP Retention:** Track Capital Work-in-Progress (CWIP) as % of Net Block and age (>2-3 years without capitalization = fake capitalization risk).
- **Intangibles & Goodwill:** Intangibles as % of Net Worth (flag if >20%).

### 5. Output
Return `leverage_flag` as `GREEN`, `AMBER`, or `RED`. Provide 8-quarter QoQ and 5-year YoY tables for working capital days and return ratios.
