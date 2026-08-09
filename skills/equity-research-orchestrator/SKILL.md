---
name: equity-research-orchestrator
description: "Master COMPOSITE orchestrator for professional equity Research Analyst (RA) diligence. Classifies company type (bank/nbfc/corporate), routes to the correct analysis pipeline, loops minimum 3 times until convergence (no new details added), enforces side-by-side YoY % and QoQ % analysis, and synthesizes a full RA report with investment rating."
type: COMPOSITE
version: 3.2.0
children:
  - soic-stockscans-fetcher
  - financial-data-fetcher
  - company-type-classifier
  - normal-company-pipeline
  - bank-pipeline
  - nbfc-pipeline
  - ra-report-synthesizer
  - marcellus-ccp-analyzer
  - soic-intrinsic-analyzer
  - soic-valuation-analyzer
  - obsidian-publisher
inputs:
  - company_name: string
  - periods: string[]
outputs:
  - report_markdown: string
  - recommendation: string
  - target_price: string
  - risk_rating: string
---

# Equity Research Master Orchestrator (COMPOSITE v3.2.0)

Master composite skill for listed company equity analysis across ALL DOMAINS (`corporate`, `bank`, `nbfc`). Dispatches the correct pipeline based on `company-type-classifier` output, then synthesizes the full institutional RA report.

---

## 🔄 MANDATORY ITERATIVE RESEARCH LOOP (MINIMUM 3 PASSES)

Every execution of `equity-research-orchestrator` MUST perform an **Iterative Refinement Loop (Minimum 3 Passes)**:

1. **Pass 1 (Primary Data Extraction & Initial Draft)**:
   - Run `soic-stockscans-fetcher` to extract all 6 official StockScans reports (`Business Overview`, `Growth Catalysts`, `Guidance Report`, `Forensic Report`, `Financial Model`, `Deep Dive Report`).
   - Run `screener` MCP tools to fetch full 12-quarter P&L, 7-year annual financials, Balance Sheet, Cash Flows, and Shareholding.
   - Run `tradingview` MCP tools to audit 30-40 day delivery volume & deliverable quantity.
2. **Pass 2 (Granular Deepening & Reading-Between-The-Lines Expansion Pass)**:
   - Audit Pass 1 output against all 25 section requirements.
   - Ensure EVERY SINGLE TABLE contains an explicit `🔍 Reading Between the Lines & Analytical Takeaways` subsection.
   - **MANDATORY DUAL-DELTA NARRATIVE RULE**: Ensure all quarterly narratives and Reading Between the Lines subsections explicitly evaluate BOTH **YoY %** AND **QoQ %** deltas side-by-side! (e.g. `Revenue ₹536 Cr (+38.7% YoY | -8.1% QoQ)`, `PAT ₹76 Cr (+53.8% YoY | +24.6% QoQ)`).
3. **Pass 3 (Cross-Verification & Convergence Loop Pass)**:
   - Perform a full cross-verification pass between Screener API, StockScans report cards, and TradingView data.
   - **Loop Continuation Condition**: If Pass 3 discovers ANY new metric, guidance delta, forensic detail, or table insight that was missing, **CONTINUE THE LOOP (Pass 4, Pass 5, etc.) until a complete pass yields NO NEW ADDITIONS (Complete Convergence)**!


---

## Universal Execution & Report Output Standards (ALL SECTORS & DOMAINS)

Every single execution of `equity-research-orchestrator` MUST automatically and repeatably enforce the following 15 report sections across ALL DOMAINS:


1. **Investment Summary & Rating Matrix**: CMP, 52W range, Market Cap, P/E, P/B, ROCE/ROE (or ROA/CRAR for Banks), Target Price, Rating.
2. **Key Investment Scorecard (Mandatory 5-10 Good Points vs 5-10 Bad Points)**:
   - *Minimum 5 to 10 GOOD POINTS (Key Strengths & Bullish Signals)*
   - *Minimum 5 to 10 BAD POINTS (Key Weaknesses & Red Flags)*
3. **Multi-Year Historical Financial Statements (5-Year Grids)**:
   - P&L / NII Table + Decryption
   - Balance Sheet / Asset-Liabilities Table + Decryption
   - Cash Flow / Capital Adequacy Table + Decryption
   - Working Capital / Asset Quality (GNPA/NNPA) Days Table + Decryption
   - Shareholding Pattern Table (8 Quarters) + Decryption
4. **MANDATORY Company Share Transaction, QIP & Ownership Microstructure Audit**:
   - *QIP, Preferential Allotments & Share Dilution Audit (5-Year share count expansion, QIP issue prices, warrant conversions, rights issues, ESOP dilution impact)*
   - *Bulk & Block Deals Breakdown (Buyer/Seller identities, transaction dates, prices, total value in ₹ Cr, MANDATORY % of Total Shares / % Equity Transacted column)*
   - *Promoter & Insider Share Transactions (Pledging changes, insider buys/sells, buyback participation, MANDATORY % of Total Shares / % Equity Transacted column)*
   - *Institutional (FII / DII) Share Transaction Dynamics (Net quarterly position shifts, index rebalancing flows, retail shareholder base expansion)*
   - *Delivery Volume & Deliverable Quantity Microstructure (30-40 day delivery %, volume multiples, institutional accumulation vs distribution signals)*
5. **8-Quarter Sequential (QoQ) Financial Analysis & Decryption**: Complete 8-Quarter QoQ Table (Sales/NII, EBITDA/PPOP, OPM/NIM %, PAT, EPS, One-Off / Exceptional Items).
6. **Quarterly Cyclicality & Seasonality Pattern**: Explicit identification of **Dull Quarter** (e.g. Q1 annual shutdown/budget reset) vs **Peak Quarter** (e.g. Q4 year-end push).
7. **Segmental Breakdown (Push vs Pull) & Growth Story**: Volume vs Margin growth breakdown (or AUM/Yield vs Cost of Funds for Banks/NBFCs) + Segment Push vs Pull table.
8. **Standardized 3-Year Forward Financial Projections Grid with Guidance Derivation Basis**:
   - Gross Revenue / NII, Operating EBITDA / PPOP, Net Profit (PAT), Projected EPS (₹), Forward P/E or Forward P/B Multiple, Implied PEG Ratio for FY26, FY27E, FY28E, FY29E, and **`Management Guidance & Capex Derivation Basis`** column.
9. **Screener Concall Crucial Highlights & Guidance Timeline**: Chronological management statements extracted via Screener earnings call tools (`screener.analyze_earnings_call`), capex commissioning dates, margin/NIM guidance, debt/borrowing roadmap.
10. **Marcellus Coffee Can & "Diamonds in the Dust" Compounding Framework (MANDATORY SECTION)**:
    - *Multi-Year Twin Filter Audit Table (Sales Growth >10% YoY & ROCE/ROE >15% every year)*
    - *Accounting Purity Audit (10-Yr Cumulative CFO/EBITDA >75%, zero asset misallocation, promoter pledging = 0%)*
    - *Incremental ROCE (iROCE) & Reinvestment Efficiency Table*
    - *Coffee Can Classification Verdict (`COFFEE CAN COMPOUNDER`, `EMERGING COMPOUNDER`, `TURNAROUND / INFLECTION`, or `NOT QUALIFIED`)*.
11. **Substack Qualitative Narrative**: Moats, Uniqueness, Pricing Power, and Industry Value Chain Mapping.
12. **Business & Growth Optionality Matrix (5-Pillar Framework)**: Pipeline/Product Optionality, Capacity/Branch Land Bank Optionality, Geographic/Market Optionality, Tech Platform Optionality, and Quantified Optionality Target Price Impact Table.
13. **Retail Investor Scuttlebutt (ValuePickr Forum — Last 1-4 Quarters)**.
14. **Sector KPIs & Regulatory Audit**: Domain-specific metrics across 30+ sectors.
15. **Three-Way Data Verification, Accounting Fraud & Forensic Audit**:
    - *Three-Way Data Cross-Verification Table (Screener API Data vs BSE/NSE Filings vs Audited Annual Reports)*
    - *MANDATORY Dr. Vijay Malik 7-Point Fraud Risk Scorecard Breakdown Table (Sales vs CFO, CWIP, Receivables, Other Income, Audit Opinion, Pledging, RPTs with exact score/7)*
    - *MANDATORY KMP & Executive Compensation Audit Table with Explicit WHY Rating Justification (Detailed rationale explaining why GREEN/AMBER/RED rating is assigned)*
    - *Walk-The-Talk Guidance Scorecard*.
16. **Valuation Models (DCF / DDM / Residual Income / SOTP Model with Sensitivity Grid)**: MUST be presented as clean **Markdown Tables** and step-by-step plain text arithmetic (DO NOT use raw LaTeX commands like `\frac`, `\text`, `\times` with currency symbols as they fail to render in UI). Include Scenario Target Prices (Bull, Base, Bear, Optionality Unlocked).
17. **MANDATORY VERBOSE "READ BETWEEN THE LINES" COMMENTARY**: Rendered directly beneath **EVERY SINGLE TABLE**.

---

## Execution Routing Rules

| Classifier Output | Pipeline Invoked | Atomic Skills Run |
|---|---|---|
| `company_type == corporate` | `normal-company-pipeline` | income-statement-analyzer → balance-sheet-analyzer → cash-flow-analyzer → corporate-actions-analyzer → delivery-volume-analyzer → fraud-detection-forensics |
| `company_type == bank` | `bank-pipeline` | bank-analyzer → corporate-actions-analyzer → delivery-volume-analyzer → fraud-detection-forensics |
| `company_type == nbfc` | `nbfc-pipeline` | nbfc-analyzer → corporate-actions-analyzer → delivery-volume-analyzer → fraud-detection-forensics |



18. **MANDATORY SOIC x StockScans Intelligence & Synthesis (6-Report Extraction)**:
    - *Automatically fetch and synthesize all 6 SOIC x StockScans Reports from StockScans.in via `soic-stockscans-fetcher`*:
      1. **Business Overview** (What the company does, business segments, key product offerings in plain English)
      2. **Growth Catalysts** (Forward growth drivers, capacity expansions, new product launches, macro triggers)
      3. **Guidance Report** (Management guidance vs actual outcomes, ADS, margin targets, capex delivery)
      4. **Forensic Report** (Accounting quality, auditor qualifications, RPT red flags)
      5. **Financial Model** (Revenue drivers, margin trajectories, capital deployment)
      6. **Deep Dive Report** (Strategic moats, competitive analysis)
    - *Synthesize all 6 reports into simple, clear, actionable plain English commentary for investors.*