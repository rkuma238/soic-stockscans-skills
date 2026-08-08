---
name: cyclicality-analyzer
description: "End-of-analysis atomic skill: evaluates business cycle sensitivity, quarterly seasonality (dull quarter vs peak quarter), commodity linkages, interest rate dependencies, and earnings volatility."
type: ATOMIC
version: 2.0.0
children: []
inputs:
  - company_data: object
  - sector: string
  - cyclicality: string
  - financial_outputs: object
  - periods: string[]
outputs:
  - cyclicality_report: object
  - cycle_position: string
  - seasonality_pattern: object
  - entry_strategy: string
---

# Cyclicality & Seasonality Analyzer

Evaluates business cycle position, quarterly seasonality (identifying the **Dull Quarter** vs **Peak Quarter**), and entry timing strategy based on historical 8-quarter financial trends.

---

## Step 1 — Quarterly Seasonality Audit (Dull Quarter vs Peak Quarter Pattern)
Identify and document the explicit quarterly historical pattern:

| Quarter | Historical Trend & Operational Reality | Seasonal Classification |
| :--- | :--- | :---: |
| **Q1 (Apr – Jun)** | Annual maintenance shutdowns, client budget resets, summer slowdown | 🔴 **DULL QUARTER** (Seasonal Trough) |
| **Q2 (Jul – Sep)** | Monsoon impact, gradual recovery, R&D trial momentum | 🟡 **MODERATE RECOVERY** |
| **Q3 (Oct – Dec)** | Festive season, global innovator budgeting push | 🟢 **STRONG QUARTER** |
| **Q4 (Jan – Mar)** | Fiscal year-end budget utilization, commercial batch dispatches | 🟢 **PEAK QUARTER** (Seasonal High) |

#### Seasonality Analysis Requirements:
- State explicitly which quarter is historically the **Dull Quarter** (lowest OPM/Revenue) and why.
- State explicitly which quarter is historically the **Peak Quarter** (highest OPM/Revenue) and why.
- Prevent false panic during Dull Quarters by comparing performance strictly YoY rather than QoQ.

---

## Step 2 — Cyclicality Classification

| Label | Definition | Sectors |
|---|---|---|
| `highly-cyclical` | Earnings 2x-3x volatile vs GDP cycle, commodity price-driven | Commodity, Capital Goods, Real Estate, Infra |
| `moderately-cyclical` | GDP-correlated with 1-2 quarter lag, partial pricing power | Auto, Cement, Electrical, IT |
| `defensive` | Demand inelastic, earnings stable across cycles, pricing power | FMCG, Pharma, Hospital |
| `secular-growth` | Structural long-term penetration story, cycle-agnostic demand | Retail, Gold, NBFC, CRDMO/CDMO |
| `rate-sensitive` | Margin and demand directly tied to RBI repo rate cycle | Bank, NBFC |

---

## Step 3 — Current Cycle Position Assessment

| Position | Operational & Financial Signal | Entry Strategy |
|---|---|---|
| **Trough** | Margins at multi-year lows, capex deferred | `aggressive-entry` (Buy when ugly) |
| **Early Recovery** | Volume revival, pricing flat, margins expanding | `strong-buy` (Best risk/reward) |
| **Mid Cycle** | Strong volumes + expanding margins, capex ramp | `accumulate` (Momentum phase) |
| **Peak** | Margins at highs, capex peak, rich valuations | `reduce-or-exit` (Risk of mean reversion) |
| **Downturn** | Volume slowdown, inventory build-up, margin compression | `avoid-or-sell` |

---

## Output
Return `cyclicality_report` with detailed `seasonality_pattern` (Dull Quarter vs Peak Quarter), `cycle_position`, and `entry_strategy` label.
