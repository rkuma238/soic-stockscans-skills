---
name: nbfc-analyzer
description: "Analyzes NBFCs, HFCs, and MFIs: AUM growth, Yield/Spread/NIM, Stage 3 asset quality, Gearing, borrowing mix, and ROA."
type: ATOMIC
version: 1.0.0
children: []
inputs:
  - company_data: object
  - periods: string[]
outputs:
  - aum_summary: object
  - spread_margin: object
  - asset_quality: object
  - liability_profile: object
  - nbfc_health_flag: string
---

# NBFC / HFC / MFI Analyzer

Use for **Non-Banking Financial Companies, Housing Finance Companies, Microfinance Institutions** (Bajaj Finance, Cholamandalam, Shriram, LIC Housing, Muthoot, etc.).

> Ind AS classification uses Stage 1/2/3, NOT traditional NPA terminology used for banks.

---

## Analysis Steps

### 1. AUM & Disbursement Growth

| Metric | YoY | QoQ | MoM |
|---|---|---|---|
| AUM | > 20% target | Sequential momentum | Where reported |
| Disbursements | Volume + value | Seasonal patterns | Where reported |
| AUM Mix: Secured vs Unsecured | > 60% secured preferred | | |

### 2. Yield, Spread & NIM

| Metric | Formula | Benchmark |
|---|---|---|
| Yield on Advances | Interest Income / Avg Loan Book | MFI: 20-24%, HFC: 9-11% |
| Cost of Borrowing (CoB) | Interest Expended / Avg Borrowings | 7-9% |
| Interest Spread | Yield – CoB | > 3.5-4% |
| NIM | NII / Avg AUM | Retail NBFC: 6-10% |

### 3. Asset Quality (Ind AS Stage Classification)

| Stage | Definition | Benchmark |
|---|---|---|
| Gross Stage 3 | > 90 DPD | < 3% Retail, < 5% MFI |
| Net Stage 3 | After provisions | < 2% |
| PCR | Provisions / Gross Stage 3 | > 50-60% |
| Write-off Rate | Annualized write-offs / Avg AUM | < 2% |

### 4. Liability Profile & Gearing

- **Gearing**: `Total Borrowings / Net Worth` — Comfortable < 4x Retail, < 7x HFC.
- Borrowing Mix: Banks vs NCDs vs ECB vs CP — High CP dependency = liquidity risk.
- Co-lending / Off-balance-sheet exposure.
- Liquidity Buffer: Cash + Undrawn lines vs next 3-month repayments.

### 5. Returns

- **ROA**: > 2.5-3% Retail, > 1.5% HFC, **> 3.5%-4% MFI**.
- **ROE**: > 18-20%.

### 6. Microfinance (MFI) Specific KPIs
*(If sub-sector is `nbfc-microfinance`)*

| KPI | Description | Benchmark / Signal |
|---|---|---|
| GLP (Gross Loan Portfolio) Growth | Core growth rate | > 25% YoY |
| Active Borrower Base | Growth in unique customers | Key penetration metric |
| States/Districts Concentration | Top-3 states % of GLP | High concentration = political/climate risk |
| Collection Efficiency (CE) % | Cash collected vs demanded | Must be > 98-99% |
| 0+ DPD / 30+ DPD (Days Past Due) | Early warning bucket | Rising early buckets = future NPA |
| JLGs (Joint Liability Groups) vs Individual | Portfolio model | JLG = typical group guarantee |
| Operating Expense / GLP | Cost efficiency metric | Target < 6% |
| Cost-to-Income Ratio | Operational drag | Target < 35-40% |
| Microfinance Regulatory Cap & Margin | RBI MFI margin cap compliance | NIM usually ~10-12% |

### 7. Output
Return `nbfc_health_flag` as `GREEN`, `AMBER`, or `RED`. Produce 8Q QoQ and 4Y YoY tables.
