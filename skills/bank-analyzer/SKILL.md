---
name: bank-analyzer
description: "Analyzes Scheduled Commercial Banks (PSU & Private): NII, NIM, GNPA/NNPA/PCR, CASA, Slippage Rate, Cost-to-Income, ROA, and CRAR."
type: ATOMIC
version: 1.0.0
children: []
inputs:
  - company_data: object
  - periods: string[]
outputs:
  - income_summary: object
  - asset_quality: object
  - deposit_advances: object
  - capital_returns: object
  - bank_health_flag: string
---

# Bank Analyzer

Use **only for Scheduled Commercial Banks** (SBI, HDFC Bank, ICICI, Kotak, Axis, etc.).

> Traditional EBITDA / Working Capital / Capex metrics do NOT apply to banks.

---

## Analysis Steps

### 1. P&L Equivalents

| Metric | Formula | Benchmark |
|---|---|---|
| NII Growth | YoY / QoQ NII% | > 12-15% YoY |
| NIM | NII / Avg Earning Assets | Private: 3.5-4.5%, PSU: 2.5-3.5% |
| Other Income | Fee + Trading + FX | Higher mix = quality |
| PPOP | Net Revenue – OpEx | Core earnings proxy |
| Cost-to-Income | OpEx / Net Income | < 50% target |

### 2. Asset Quality (8Q Trend)

| Metric | Formula | Benchmark |
|---|---|---|
| GNPA % | Gross NPAs / Gross Advances | < 2% Private, < 5% PSU |
| NNPA % | Net NPAs / Net Advances | < 1% |
| PCR | Provisions / Gross NPAs | > 75% |
| Slippage Rate | Fresh NPAs / Avg Loan Book | < 1.5% per quarter |
| Credit Cost | Provisions / Avg Loan Book | < 1% annualized |

### 3. Deposit & Advance Franchise

- **CASA Ratio**: `(Current + Savings) / Total Deposits` — Target > 40%.
- **CD Ratio**: `Advances / Deposits` — Ideal 72-80%.
- Loan Mix: Retail vs Corporate vs SME — Retail preferred.
- Deposit Growth QoQ/YoY vs Advance Growth QoQ/YoY.

### 4. Capital Adequacy & Returns

- **Tier-1 CRAR**: > 9.5% regulatory minimum; leaders sustain > 15%.
- **ROA**: > 1.5% target.
- **ROE**: > 15% target.

### 5. MoM Inputs (if available)
- Monthly MSME disbursements, home loan sanctions, NPA recovery amounts.

### 6. Output
Return `bank_health_flag` as `GREEN`, `AMBER`, or `RED`. Produce 8Q comparison table.
