---
name: banking-nbfc-analyzer
description: "Atomic skill specialized for analyzing Banks, NBFCs, and Housing Finance Companies (HFCs), focusing on NII, PPOP story, NIMs, Asset Quality (GNPA/NNPA/PCR), CASA ratio, Cost-to-Income, ROA, RBI regulatory changes, Price-to-Book (P/B) valuation, and Capital Adequacy (CRAR)."
type: ATOMIC
version: 4.0.0
children: []
inputs:
  - company_data: object
  - periods: string[]
outputs:
  - bank_nbfc_summary: object
  - ppop_trajectory_story: object
  - rbi_regulatory_audit: object
  - asset_quality_audit: object
  - pb_valuation_matrix: object
---

# Banking & NBFC Analyzer (ATOMIC)

Specialized atomic skill for evaluating Scheduled Commercial Banks (PSU & Private), NBFCs, Housing Finance Companies (HFCs), and Microfinance Institutions (MFIs).

---

## 1. Pre-Provision Operating Profit (PPOP) Trajectory Story (MANDATORY)

Deconstruct the core operational earning capacity before credit costs/provisions:

$$\text{Pre-Provision Operating Profit (PPOP)} = \text{Net Interest Income (NII)} + \text{Other Fee Income} - \text{Operating Expenses}$$

$$\text{PPOP Margin \%} = \frac{\text{PPOP}}{\text{Total Earning Assets}}$$

#### PPOP Story Requirements:
- Evaluate 5-year and 8-quarter PPOP growth relative to AUM growth.
- Prove whether PPOP expanding faster than AUM confirms operating leverage as Cost-to-Income drops.
- Demonstrate that strong PPOP buffers protect the institution from short-term credit provisioning spikes.

---

## 2. RBI Regulatory Circulars & Mandate Changes Impact Audit (MANDATORY)

Audit the specific financial & capital impact of key RBI regulatory mandates:

| RBI Regulatory Mandate / Circular | RBI Regulatory Requirement | Financial & Capital Impact on Institution | Management Compliance Status |
| :--- | :--- | :--- | :---: |
| **1. Unsecured Retail Risk Weights** | RBI raised risk weights on credit cards & personal loans (100% $\rightarrow$ 125%) | Tier-1 CRAR impacted by 40–80 bps | 🟢 **COMPLIANT** (CRAR > 15%) |
| **2. MFI Household Income & FOIR Cap** | Capping borrower monthly debt service FOIR at $\le 50\%$ of household income | Moderates MFI loan ticket sizes; reduces over-indebtedness default risk | 🟢 **COMPLIANT** |
| **3. Draft LCR Run-off Guidelines** | Higher run-off factor (15%) on internet/mobile retail banking deposits | Requires higher holding of G-Secs/HQLA liquid assets | 🟢 **COMPLIANT** (LCR > 120%) |
| **4. Scale-Based Regulation (SBR)** | Upper / Middle Layer capital & board governance hurdles for NBFCs | Net Worth & regulatory reporting alignment | 🟢 **COMPLIANT** |

---

## 3. Primary Valuation Metric: Price-to-Book (P/B) Multiple
Price-to-Book Value (P/B) and Price-to-Tangible Book Value (P/TBV) are the primary valuation multiples.

---

## 4. Standardized 3-Year Forward Financial Projections Grid for Banks/NBFCs

3-Year Forward Projections Grid (AUM, NII, PPOP, PAT, EPS, BVPS, Forward P/B Multiple, Forward P/E Multiple, PEG, Guidance Basis).

---

## 5. Output
Return `bank_nbfc_summary`, `ppop_trajectory_story`, `rbi_regulatory_audit`, `asset_quality_audit`, and `pb_valuation_matrix`.
