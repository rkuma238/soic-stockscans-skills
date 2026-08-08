---
name: soic-valuation-analyzer
description: "Advanced ATOMIC skill that evaluates Capital Mechanics, Treasury Management (T-bills & Cash deployment), DCF Valuation Model, 3-Year Forward Projections Grid with Guidance Derivation Basis column, Forward P/E, Revenue/PAT CAGR, and PEG Ratio for every year."
type: ATOMIC
version: 2.5.0
inputs:
  - company_data: object
  - financial_outputs: object
outputs:
  - valuation_report_markdown: string
  - treasury_tbill_audit: object
  - target_price: string
  - dcf_valuation: object
  - scenario_analysis: object
---

# SOIC Valuation & Treasury T-Bill Analyzer (ATOMIC)

Evaluates valuation multiples (P/E, EV/EBITDA, P/B, P/FCF, PEG), Treasury Management & T-Bill deployment efficiency, constructs an explicit Discounted Cash Flow (DCF) / Residual Income model with sensitivity grid, and builds a 3-scenario valuation framework.

---

## Treasury Management & T-Bill Investment Deployment Audit (MANDATORY)

Evaluate the productivity of cash & liquid investments held on the balance sheet:

| Treasury Asset Category | Balance Sheet Value (₹ Cr) | Investment Instrument Type | Realized Treasury Yield % | Benchmark T-Bill Yield % (91-Day / 364-Day) | Capital Deployment Efficiency Verdict |
| :--- | :---: | :--- | :---: | :---: | :--- |
| **Government Securities & T-Bills** | `{Gsec_Val}` | Sovereign T-Bills & G-Secs | `{Gsec_Yield}%` | **6.85%** | 🟢 **OPTIMAL RISK-FREE DEPLOYMENT** |
| **Mutual Funds & Liquid Surplus** | `{MF_Val}` | Debt Mutual Funds & Liquid Funds | `{MF_Yield}%` | **6.85%** | 🟢 **EFFICIENT TREASURY YIELD** |
| **Bank Fixed Deposits** | `{FD_Val}` | Scheduled Bank FDs | `{FD_Yield}%` | **6.85%** | 🟢 **STABLE YIELD** |
| **Idle Cash in Current Accounts** | `{Cash_Val}` | Zero-interest Current Accounts | **0.00%** | **6.85%** | 🔴 **IDLE CASH DRAG** (If > 10% of Cash) |

#### Treasury Capital Efficiency Rules:
1. **Idle Cash Drag**: Cash sitting in zero-yield accounts $> 10\%$ of total liquid reserves creates an unnecessary return drag on ROE.
2. **Treasury Yield Benchmarking**: Realized treasury yields should comfortably match or exceed the 91-Day / 364-Day T-Bill benchmark (~6.85–7.00%).

---

## Output
Return `valuation_report_markdown` and `treasury_tbill_audit`.
