---
name: tax-analysis
description: "Common atomic tax analysis skill for all company types: evaluates effective tax rate, deferred tax assets/liabilities, tax incentives (Section 80-IC, 10AA, 115BAA), MAT credit, and tax contingency provisions."
type: ATOMIC
version: 1.0.0
children: []
inputs:
  - company_data: object
  - company_type: string
  - periods: string[]
outputs:
  - effective_tax_rate: object
  - deferred_tax: object
  - tax_incentives: object
  - contingent_liabilities: object
  - tax_quality_flag: string
---

# Tax Analysis Skill (Common — All Entity Types)

Evaluates **tax health, efficiency, and hidden risks** across all companies.

---

## Analysis Steps

### 1. Effective Tax Rate (ETR) Trend

| Metric | Formula | Benchmark |
|---|---|---|
| Effective Tax Rate (ETR) | Tax Paid / PBT × 100 | ~25.17% (115BAA) or 22% (new regime) |
| ETR vs Statutory Rate Gap | Statutory Rate – ETR | Flag if ETR < 15% without explanation |
| Cash Tax vs Book Tax | Tax Paid (Cash Flow) vs Tax Expense (P&L) | Large divergence = deferred tax buildup |

Flag sudden ETR drops — may indicate:
- One-time deferred tax asset recognition.
- MAT credit utilization running out.
- Tax holiday expiry risk ahead.

### 2. Deferred Tax Assets (DTA) & Liabilities (DTL)

- **Net DTA**: `Deferred Tax Asset – Deferred Tax Liability`.
- Rising Net DTA on balance sheet = future tax cash outflow risk.
- `DTA / PBT` > 30% over multiple years = `tax_quality_flag = AMBER`.
- Sudden large DTA creation → verify if underlying timing differences are genuine.

### 3. Tax Incentives & Holiday Zones

| Incentive | Applicable To |
|---|---|
| Section 115BAA | New corporate tax rate 22% (forgo MAT/exemptions) |
| Section 80-IC | Manufacturing in Himachal, Uttarakhand (10-year benefit) |
| Section 10AA | SEZ units — 100% deduction first 5 years, tapering |
| Section 80-IAB | Infra & Power projects tax deduction |
| Hospital Section 35AD | Capital investment deduction for hospitals |

**Expiry Risk Check**: Identify when incentive windows expire and model ETR normalization impact on PAT.

### 4. Minimum Alternate Tax (MAT)
- Is the company paying MAT (18.5% of book profit) vs regular tax?
- **MAT Credit Entitlement** on balance sheet → can be utilized within 15 years.
- Rising MAT credit balance = company consistently in MAT zone = low profitability concern.

### 5. Bank-Specific Tax Considerations
*(if `company_type == bank`)*
- Deferred Tax on NPA Provisions.
- Investment depreciation tax treatment.
- Capital gains tax on AFS portfolio mark-to-market.

### 6. Contingent Tax Liabilities
- Tax disputed and under litigation (note the ₹Cr amount vs annual PAT).
- Disputed demands at CIT(A), ITAT, High Court, Supreme Court levels.
- Flag if `Disputed Tax / PAT > 50%` = `tax_quality_flag = RED`.

---

## Output
- `effective_tax_rate`: trend across 8 quarters.
- `tax_incentives`: active incentives, amounts, and expiry dates.
- `contingent_liabilities`: disputed tax demands with court level.
- `tax_quality_flag`: `GREEN` / `AMBER` / `RED`.
