---
# ⚠️ ZERO TOLERANCE — NO FAKE OR ESTIMATED DATA RULE (MANDATORY — READ FIRST)
# ALL figures in every table MUST come from actual MCP tool calls (screener, nse-bse-mcp,
# playwright, concall-analysis, substack-analyzer) or official published filings.
# PROHIBITED: Inventing, hallucinating, or estimating any factual number.
# REQUIRED: Every table header must cite [Source: screener MCP | NSE-BSE MCP | Annual Report | Concall Transcript]
# If a data point cannot be sourced, write [DATA UNAVAILABLE — CHECK SOURCE] — NEVER a made-up number.
# Forward projections (DCF, 3-year grid) ARE permitted as analyst estimates but MUST be
# labeled PROJECTED ESTIMATE and show derivation basis explicitly.
---
name: ra-report-synthesizer
description: "Synthesizes all atomic skill outputs into a complete institutional-grade equity research report."
type: ATOMIC
version: 5.2.0
inputs:
  - company_type: string
  - sector: string
  - financial_outputs: object
  - sector_kpis: object
  - governance_outputs: object
  - cyclicality_report: object
outputs:
  - report_markdown: string
  - recommendation: string
  - target_price: string
  - risk_rating: string
---

# RA Report Synthesizer

Synthesizes outputs from all atomic analysis skills into a complete institutional equity research report.

---

## MANDATORY RULE: VERBOSE "READ BETWEEN THE LINES" COMMENTARY AFTER EVERY SINGLE TABLE
**CRITICAL REQUIREMENT:** EVERY SINGLE TABLE rendered in the report **MUST be immediately followed by a verbose, multi-paragraph forensic commentary block titled `🔍 Reading Between the Lines & Financial Decryption`**. ZERO EXCEPTIONS.

---

## Required Report Structure & Sections

### Section 1 — Investment Summary & Rating Matrix + Decryption
### Section 1.5 — The 5 to 10 GOOD POINTS vs 5 to 10 BAD POINTS (MANDATORY SCORECARD)
### Section 2 — Multi-Year Historical Financial Statements (5-Year Grids with Verbose Commentary)
### Section 2.3 — 8-Quarter Sequential (QoQ) Financial Analysis & Decryption
### Section 2.4 — Quarterly Cyclicality & Seasonality Pattern (Dull vs Peak Quarter) + Decryption
### Section 2.5 — Segmental Breakdown (Push vs Pull) & Margin vs Volume Growth Story + Decryption
### Section 2.6 — Pre-Provision Operating Profit (PPOP) Trajectory & Margin Story + Decryption *(Finance Companies)*

### Section 2.7 — 30-Day Delivery % & Institutional Accumulation/Distribution + Unusual Volume Spike Analysis (MANDATORY)

This section MUST render **TWO SUB-TABLES** side-by-side:

#### Sub-Table A: 30-Day Delivery % & Volume Microstructure Table
Columns: Session | Total Volume | **20D Avg Volume** | **Vol Multiple** | Deliverable Qty | **Delivery %** | Daily Px Chg % | **Microstructure Signal** | **Unusual Volume Flag** | Institutional Verdict

#### Sub-Table B: Unusual Volume Spike Events Summary Table *(MANDATORY — even if zero events, state "No Unusual Volume Events Detected")*
Columns: Event Date | Total Volume | 20D Avg Volume | **Vol Multiple** | **Delivery %** | Daily Price Chg % | **Unusual Volume Tier Classification** | Cross-Check vs. Bulk / Block Deal | Action Verdict

Tier Classification must follow the 4-tier system:
- ⚡ **Institutional Surge Accumulation** (Vol $\ge 2.5\times$ + Delivery $\ge 50\%$ + Price $> +1.5\%$)
- 🚨 **Institutional Dump / Selling Surge** (Vol $\ge 2.5\times$ + Delivery $\ge 45\%$ + Price $< -2.0\%$)
- 🌀 **Speculative Pump & Churn** (Vol $\ge 3.0\times$ + Delivery $< 20\%$)
- 📦 **Bulk / Block Deal Execution** (Vol $\ge 4.0\times$ + Delivery $\ge 70\%$)

*Must include `🔍 Reading Between the Lines: Delivery Microstructure, Unusual Volume & Smart Money Decryption`*

### Section 3 — Standardized 3-Year Forward Financial Projections Grid (WITH GUIDANCE DERIVATION BASIS) + Decryption
### Section 4 — Concall Crucial Highlights & Management Guidance Timeline (EXHAUSTIVE) + Decryption
### Section 5 — Substack Qualitative Narrative: Business Moat & Value Chain Mechanics
### Section 5.5 — Comprehensive Business & Growth Optionality Matrix (MANDATORY) + Decryption
### Section 6 — Retail Investor Scuttlebutt (ValuePickr Forum — Last 1–4 Quarters) + Decryption
### Section 7 — Sector KPIs (Chemical / Pharma / Banking / Specific Sector) + Decryption
### Section 8 — Forensic Accounting & Red Flag Audit (Dr. Vijay Malik Framework & Walk The Talk Scorecard) + Decryption
### Section 8.5 — Annual Report Governance, KMP Remuneration, Subsidiary & RPT Deep-Dive Table + Decryption
### Section 8.6 — Treasury Management & T-Bill Investment Deployment Audit Table + Decryption
### Section 8.7 — KMP & Board Resignation Audit & RBI Regulatory Circulars Audit Table + Decryption
### Section 8.8 — Write-Offs, Exceptional One-Offs & Unclaimed Liabilities Audit Table + Decryption
### Section 9 — Saurabh Mukherjea's Coffee Can & "Diamonds in the Dust" Framework (MANDATORY) + Decryption
### Section 10 — Peer Benchmarking & Multiples Matrix (P/E & P/B) + Decryption
### Section 11 — Explicit Upside Catalysts/Triggers & Downside Risks
### Section 12 — Valuation Models (DCF for Corporates / Residual Income DDM for Banks) & Sensitivity Matrix + Decryption
### Section 13 — Valuation Scenarios & 12-Month Target Prices (Bull, Base, Bear, Optionality Unlocked) + Decryption
### Section 14 — What to Track (Key Monitorables Grid) + Decryption
