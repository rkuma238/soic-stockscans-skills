---
name: corporate-actions-analyzer
description: "Monitors and interprets corporate actions: promoter pledging, buybacks, dividends, bonus/splits, rights issues, and bulk/block deals."
type: ATOMIC
version: 1.0.0
children: []
inputs:
  - company_data: object
  - periods: string[]
outputs:
  - promoter_analysis: object
  - capital_events: object[]
  - governance_signal: string
---

# Corporate Actions Analyzer

Applies to **all company types** (Corporate, Bank, NBFC). Tracks insider and structural ownership signals.

---

## Analysis Steps

### 1. Promoter Holding & Pledging

| Signal | Benchmark |
|---|---|
| Promoter Holding trend | Increasing = confidence; Declining = alert |
| Pledging % (Pledged / Total Promoter) | > 20% = AMBER, > 40% = RED |

### 2. Share Buybacks
- Type: Tender Offer vs Open Market (Tender preferred — more committed).
- Buyback Price premium vs CMP at announcement.
- Buyback quantum as % of Net Worth (> 5% = meaningful).

### 3. Qualified Institutional Placements (QIP), Preferential Allotments & Share Dilution Audit (MANDATORY)
- **QIP & Institutional Capital Raises**: Issue date, QIP issue price vs CMP, dilution quantum (% of expanded equity base), and participating marquee institutions.
- **Preferential Allotments & Convertible Warrants**: Allotment price, lock-in terms, and conversion timelines for promoters/insiders/investors.
- **Rights Issues & ESOP Dilution**: Rights ratio, issue price, and cumulative ESOP dilution per annum.
- **5-Year Share Count & Dilution Impact Table**: Track total outstanding share count across 5 years, calculate EPS dilution %, and evaluate capital deployment efficiency (ROE/ROA pre vs post dilution).

### 4. Capital Restructuring & Corporate Actions
- **MANDATORY:** You MUST explicitly describe all recent and historical corporate actions in the report.
- Stock Splits & Bonus ratios (with exact dates).
- Rights Issues & Preferential Allotments → dilution impact and allotment price vs CMP.
- Warrant conversions by promoters/insiders.

### 5. Dividends & Payouts
- Dividend per Share (DPS) CAGR.
- Payout Ratio: `Dividends / PAT` (sustainable if < 40% for growth cos).

### 6. Bulk/Block Deals & Insider/KMP Market Transactions (MANDATORY TABLE SCHEMAS)

Every Bulk & Block Deals Table (Section 4.2) and Insider & KMP Transactions Table (Section 4.3) MUST include the following exact columns:

#### Bulk & Block Deals Table Schema (Section 4.2):
1. `Transaction Date`
2. `Entity Name (Buyer / Seller)`
3. `Transaction Type (BUY / SELL)`
4. `Shares Traded (in Cr / Lakhs)`
5. `Execution Price (₹)`
6. `Total Value (₹ Cr)`
7. **`% of Total Shares (% Equity Transacted)`** (MANDATORY COLUMN: `Shares Traded / Total Outstanding Shares * 100`)
8. `Institutional Context / Strategic Impact`

#### Insider & KMP Transactions Table Schema (Section 4.3):
1. `Date / Period`
2. `Insider Name & Designation`
3. `Transaction Type (Market Buy / Market Sell / ESOP / Preferential)`
4. `Shares Transacted`
5. `Average Price (₹)`
6. **`% of Total Shares (% Equity Transacted)`** (MANDATORY COLUMN: `Shares Transacted / Total Outstanding Shares * 100`)
7. `Post-Transaction Holding`
8. `Regulatory Compliance / Rationale`

### 7. Output
Return `governance_signal` as `GREEN`, `AMBER`, or `RED` with key event timeline and `dilution_impact_summary`.



