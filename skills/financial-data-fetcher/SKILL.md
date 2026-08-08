---
# ⚠️ ZERO TOLERANCE — NO FAKE OR ESTIMATED DATA RULE (MANDATORY — READ FIRST)
# ALL financial data, KMP salaries, NPA figures, shareholding %, GNPA/NNPA,
# treasury balances, subsidiary revenues, RPT values, write-offs, and any
# numerical fact MUST be fetched from a real MCP tool or official source.
# NEVER invent, estimate, or hallucinate any factual figure.
# Every data point in every table MUST include a [Source: ...] citation.
# If data is unavailable from MCP tools, mark the field as "[DATA UNAVAILABLE — CHECK SOURCE]"
# rather than inserting a model estimate. This rule has NO exceptions.
---
name: financial-data-fetcher
description: "Initial ATOMIC skill that operates as the data ingestion engine. Autonomously fetches 5-6 quarters of financial data (Screener/NSE), latest concall transcripts, Substack moats/value chain, ValuePickr scuttlebutt, Annual Report disclosures (Auditor report, KMP remuneration, Subsidiary details, RPTs, T-bills, Write-offs, Exceptional items, Unclaimed bills), and scrapes corporate web pages."
type: ATOMIC
version: 3.2.0
inputs:
  - company_name: string
  - periods: string[]
outputs:
  - financial_data: object
  - concall_transcripts: object[]
  - substack_narrative: object
  - valuepickr_scuttlebutt: object[]
  - annual_report_disclosures: object
---

# Financial Data Fetcher (ATOMIC)

Data ingestion engine for listed companies. Autonomously scours Screener MCP and NSE/BSE MCP, extracts Concall transcripts, ingests Substack moat/value chain research, harvests ValuePickr scuttlebutt, and extracts **Annual Report Disclosures & Financial Footnotes** (Auditor Reports, KMP Remuneration, Subsidiary Breakdown, Related Party Transactions, Treasury T-Bill Deployment, Bad Debt Write-Offs, Exceptional One-Off Items, Unclaimed Bills, and Trade Payable Write-Backs).

## Mandatory Screener Concall & Three-Way Data Verification (MANDATORY)

1. **Screener Concall & Transcript Extraction**:
   - Use `screener.analyze_earnings_call` and `screener.get_document_list` / `screener.get_company_announcements` to extract transcript notes, key management commentary, capex timelines, NIM/margin guidance, and management Q&A highlights for recent quarters.

2. **Three-Way Data Cross-Verification**:
   - MUST cross-verify (1) **Screener API dataset**, (2) **Exchange Result Announcements (NSE/BSE Filings)**, and (3) **Audited Annual Report disclosures & footnotes** before generating the final report.
   - Any numerical discrepancies between Screener data and official exchange filings / annual reports MUST be explicitly flagged in a **Data Provenance & Discrepancy Table**.

3. **Exceptional One-Off Items & Non-Recurring Income Audit**:
   - Isolate non-operating gains/losses, land sale proceeds, tax refund interest, debt restructuring write-offs, and DTA adjustments from core operating profits.

---

## Mandatory Annual Report Disclosures Extraction

Harvest and structure the following 6 annual report sections:

1. **Auditor's Report & Key Audit Matters (KAMs)**: Statutory Auditor Name, Audit Firm Tier (Big 4 check), Audit Opinion (`UNQUALIFIED` / `QUALIFIED`), Key Audit Matters (KAMs).
2. **Key Managerial Personnel (KMP) Remuneration**: CEO / MD / Executive Directors salary, commission, and stock options (₹ Cr and % of PAT).
3. **Subsidiary & Joint Venture (JV) Breakdown**: List of active direct & indirect subsidiaries, step-down entities, and JVs with financial contributions.
4. **Related Party Transactions (RPT)**: Total RPT value as % of Sales / Expenses / Net Worth.
5. **Treasury Management & T-Bill Investment Deployment**: Cash, G-Secs, T-Bills, Mutual Funds, Fixed Deposits breakdown & realized yields.
6. **Bad Debt Write-Offs, Exceptional Items, Unclaimed Bills & Write-Backs**:
   - Technical & Bad Debt Write-Offs (₹ Cr written off during the fiscal year).
   - Recovery against Written-off Assets (bad debt recoveries credited to P&L).
   - Exceptional One-Off Items (non-recurring gains/losses, restructuring costs, DTA one-offs).
   - Unclaimed Liabilities, Trade Payable Write-backs & Unbilled Revenue Write-downs.

---

## Output
Return consolidated `financial_data`, `concall_transcripts`, `substack_narrative`, `valuepickr_scuttlebutt`, `annual_report_disclosures`, and `three_way_verification_audit`.

