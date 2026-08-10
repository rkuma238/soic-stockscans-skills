---
name: fraud-detection-forensics
description: "Forensic accounting skill: detects earnings manipulation, 24H quarterly result fraud signals, Related Party Transaction (RPT) risks, KMP salary anomalies, KMP/Board resignations, auditor report KAMs, subsidiary guarantees, bad debt write-offs, exceptional one-off items, unclaimed liabilities, database audit trail non-compliance, unrecognized DTAs, delayed subsidiary impairments, and includes a mandatory Walk The Talk Management Guidance Scorecard."
type: ATOMIC
version: 3.5.0
children: []
inputs:
  - company_data: object
  - quarterly_result_24h: object
  - annual_report_disclosures: object
  - periods: string[]
outputs:
  - forensic_flags: object[]
  - walk_the_talk_scorecard: object
  - auditor_report_audit: object
  - quarterly_result_triangulation: object
  - kmp_resignation_audit: object
  - writeoff_exceptional_audit: object
  - database_audit_trail_check: object
  - subsidiary_guarantee_exposure: object
  - fraud_risk_score: string
---

# Fraud Detection & Forensics Analyzer (v3.5.0 — SOIC & 24H Result Audit Benchmark)

Applies to all corporate companies, banks, and NBFCs. Implements **24-Hour Quarterly Result Fraud Triangulation**, Dr. Vijay Malik's 7-point Forensic Triangulation, **SOIC-Level 6-Point Deep Forensic Audit**, **Three-Way Data Cross-Verification Accounting Fraud Triangulation**, the **Walk The Talk Guidance Scorecard**, **Auditor Report KAM & Impairment Lag Audit**, **Software & Database Audit Trail Compliance Audit**, **Subsidiary Financial Exposure & Guarantee Audit**, **Trade Receivable Aggregator Concentration Audit**, **KMP & Board Resignation Audit**, **KMP Remuneration Audit**, **Related Party Transactions (RPT) Audit**, and **Write-Offs, Exceptional One-Offs & Unclaimed Liabilities Audit**.

---

## 0. 24-Hour Quarterly Result Fraud Triangulation Rules (NEW v3.5.0)

When evaluating new quarterly results declared in the last 24 hours (from StockScans `result-scans`), automatically apply these 5 automated red flag checks:

| Result Fraud Test | Quantitative Trigger Condition | Forensic Risk Classification | Mandatory Action / Audit Verdict |
| :--- | :--- | :---: | :--- |
| **1. PAT-Revenue Divergence** | Revenue YoY $\ge 15\%$ AND PAT YoY $< 0\%$ | 🔴 **HIGH RED FLAG** | Investigate interest/depreciation drag or margin compression. |
| **2. Inventory Inflation / Profit Kicker** | Op Profit YoY $> 2.5 \times$ Revenue YoY (when Rev YoY $>10\%$) | 🟡 **AMBER WARNING** | Verify if raw material costs were capitalized into inventory. |
| **3. Tax Expense Anomaly** | PBT $> 0$ BUT Tax Expense $\le 0$ | 🟡 **AMBER WARNING** | Check for unrecorded DTA reversals masking core PBT. |
| **4. Extreme OPM Margin Expansion** | OPM $> 30\%$ (for non-financial corporates) | 🟡 **AMBER WARNING** | Verify sustainability vs one-off inventory/raw material tailwinds. |
| **5. Receivable vs Sales Growth Divergence**| Quarterly Receivables Growth $> 2 \times$ Revenue YoY | 🔴 **HIGH RED FLAG** | Inspect uncollected revenue and aggregator concentration. |

---

## 0. StockScans Official Forensic Report Standards & Audit Framework (v3.5.0)

All forensic audits MUST evaluate the 6 official StockScans Forensic Report Pillars:
1. **Delayed Impairments vs KAM Flags**: Track multi-year auditor KAM warnings on subsidiary equity/loans before impairment provisions.
2. **Subsidiary Financial Exposure & Guarantees**: Quantify total parent exposure (Equity + Preference + Unsecured Loans + Guarantees) and shareholder voting pushback (>10% against).
3. **Database Audit Trail Compliance (Rule 11(g))**: Verify consecutive non-compliance or unverifiable POS/software database audit logs.
4. **Customer / Aggregator Concentration**: Audit trade receivables concentrated in top 2-3 customers or aggregators (>60%).
5. **Unrecognized Deferred Tax Assets (DTA)**: Audit unrecorded DTAs on carried-forward losses and loss expiry timelines (<5 years).
6. **Accounting Policy Shifts & Exceptional Items**: Flag inventory valuation changes (FIFO to Weighted Average), depreciation shifts, or one-off fee waivers shaping profit.

---

## 1. SOIC-Level Deep Forensic Audit (MANDATORY FOR EVERY COMPANY)

Every forensic audit MUST analyze and document the following 6 deep forensic audit parameters extracted from annual report footnotes, statutory auditor reports, and Key Audit Matters (KAMs):

### 1. Auditor Key Audit Matters (KAM) & Delayed Impairment Provision Audit
- **Multi-Year KAM Tracking**: Check if investments in subsidiaries, goodwill, ROU assets, or CWIP were flagged as KAMs by statutory auditors across multiple consecutive annual reports (e.g. 2–4 years) BEFORE management recorded an impairment provision.
- **Impairment Timing & Model Assumptions**: Identify delayed impairment provisions (e.g. ₹120 Cr provision after 4 years of auditor warnings) and verify DCF discount rates (e.g. 14%) and terminal growth rates.

### 2. Subsidiary Financial Exposure, Loans & Corporate Guarantee Audit
- **Parent Total Commitment**: Quantify parent entity's total financial commitment to loss-making subsidiaries across:
  1. Equity Share Capital Invested (₹ Cr)
  2. Preference Share Capital (₹ Cr)
  3. Inter-Corporate Unsecured Loans / Advances & Interest Terms (₹ Cr)
  4. Outstanding Corporate & Performance Guarantees (₹ Cr)
- **Shareholder Voting Pushback**: Audit minority shareholder voting % against inter-corporate loan approvals (>10% voting against indicates shareholder governance concern).

### 3. Software & Database-Level Audit Trail Compliance Check (Rule 11(g))
- **Audit Trail Status**: Verify if statutory auditors reported non-compliance with Companies Act Rule 11(g) regarding the database-level audit trail feature in accounting software and POS systems across consecutive years (e.g. FY24, FY25, FY26 non-compliance).
- **Tamper-Proof Audit Trail Verification**: Check if log-editing or database access was independently verifiable by auditors.

### 4. Trade Receivables & Aggregator / Customer Concentration Audit
- **Customer Concentration Ratio**: Quantify % of trade receivables concentrated in top 2–3 customers or food delivery aggregators (e.g. Zomato, Swiggy representing >60% of receivables).
- **Impairs & Provisioning Policy**: Audit whether collective impairment allowances were created for concentrated balances.

### 5. Unrecognized Deferred Tax Assets (DTA) & Loss Expiry Audit
- **Unrecorded DTA Quantum**: Quantify unrecognized DTA on carried-forward business losses and unabsorbed depreciation for parent and operating subsidiaries (indicating lack of reasonable certainty of future taxable profits).
- **Tax Loss Expiry Timeline**: Highlight losses expiring within 5 years.

### 6. Accounting Policy Changes & Exceptional Item Abuse Audit
- **Policy Shifts**: Detect inventory valuation method shifts (e.g. FIFO to Weighted Average), depreciation method changes, or unbilled revenue accounting shifts.
- **Exceptional Non-Operating PAT Impact**: Audit franchisee fee waivers, labor code provisions, or one-off asset sales masking core operating losses.


---

## 1. Three-Way Data Comparison & Accounting Fraud Audit (MANDATORY FOR EVERY COMPANY)

Cross-verify **Screener API Data** vs. **BSE/NSE Result Announcements** vs. **Audited Annual Report Disclosures** to identify accounting fraud signals:

| Accounting Risk Category | Verification Procedure | Extracted Comparison Findings | Forensic Verdict / Risk Level |
| :--- | :--- | :--- | :---: |
| **1. Revenue & Turnover Mismatch** | Compare Revenue in Screener vs BSE Filing vs Annual Report | `{Rev_Compare}` | 🟢 **MATCHED** / 🔴 **DISCREPANCY** |
| **2. CFO vs PAT Divergence** | Cumulative CFO vs Cumulative PAT over 5 years ($CFO < PAT$) | `{CFO_PAT_Ratio}` | 🟢 **HIGH CASH CONVERSION** / 🔴 **EARNINGS MANIPULATION** |
| **3. Expense Capitalization** | CWIP / Fixed Assets growth vs Sales Growth | `{CWIP_Sales_Growth}` | 🟢 **PAR** / 🔴 **CAPEX INFLATION** |
| **4. One-off / Exceptional Item Abuse** | Non-operating gains masking core operating losses | `{Exceptional_PAT_%}` | 🟢 **PAR** / 🟡 **NON-OPERATIONAL PAT KICKER** |
| **5. RPT Siphoning & Circular Loans** | Loans/Advances to related entities vs Net Worth | `{RPT_NetWorth_%}` | 🟢 **ARM'S LENGTH** / 🔴 **MONEY CHURNING RISK** |
| **6. Share Capital Dilution / QIP Audit**| Share count expansion vs Net Worth growth | `{Share_Dilution_%}` | 🟢 **NO DILUTION** / 🟡 **EPS DILUTION** |
| **7. Receivable & DSO Inflation** | Receivables growth % vs Revenue growth % | `{Receivable_Growth_%}` | 🟢 **ALIGNMENT** / 🔴 **FICTITIOUS REVENUE** |

---

## 2. Write-Offs, Exceptional One-Offs & Unclaimed Liabilities Audit Table

| Item Category | Extracted Financial / Footnote Details | Value (₹ Cr) | % of Net Profit / Sales | Forensic Risk Rating & Audit Verdict |
| :--- | :--- | :---: | :---: | :---: |
| **Bad Debt & Technical Write-Offs** | NPA / Bad debt write-offs utilized against provisions | `{WO_Val}` | `{WO_PAT_%}%` | 🟢 **NORMAL BALANCE SHEET CLEANUP** / 🔴 **HIGH LOSS DRAG** |
| **Bad Debt Recoveries** | Recovery credited back to P&L from written-off accounts | `{Rec_Val}` | `{Rec_PAT_%}%` | 🟢 **CORE CASH RECOVERY** |
| **Exceptional / One-off Gains/Losses**| Non-recurring gains, merger restructuring, tax one-offs | `{Exc_Val}` | `{Exc_PAT_%}%` | 🟢 **PAR** / 🟡 **NON-OPERATIONAL PAT KICKER** |
| **Unclaimed Bills & Payable Write-backs**| Write-back of unclaimed liabilities & trade payables (>3Y) | `{WB_Val}` | `{WB_PAT_%}%` | 🟢 **CLEAN** / 🔴 **EARNINGS INFLATION RISK** |

---

## 3. Dr. Vijay Malik 7-Point Fraud Risk Scorecard Breakdown

| Malik Forensic Test # | Forensic Check Name | Benchmark & Target Criteria | Extracted Company Metric | Test Verdict | Score Weight |
| :---: | :--- | :--- | :--- | :---: | :---: |
| **Test 1** | **Sales vs. Cash Flow from Operations (CFO)** | 5-Yr Cumulative CFO $>$ Cumulative PAT | `{CFO_vs_PAT_Val}` | 🟢 **PASS** / 🔴 **FAIL** | 1 Point |
| **Test 2** | **Capital Work-in-Progress (CWIP) vs Net Assets**| CWIP $< 15\%$ of Net Fixed Assets | `{CWIP_Ratio}` | 🟢 **PASS** / 🔴 **FAIL** | 1 Point |
| **Test 3** | **Receivables & DSO Growth vs Sales Growth** | Receivables Growth $\le$ Sales Growth | `{Receivable_Growth}` | 🟢 **PASS** / 🔴 **FAIL** | 1 Point |
| **Test 4** | **Other Income as % of Profit Before Tax (PBT)**| Other Income $< 15\%$ of PBT | `{OtherInc_Ratio}` | 🟢 **PASS** / 🔴 **FAIL** | 1 Point |
| **Test 5** | **Auditor Qualifications & Key Audit Matters**| Unqualified Audit Opinion from Big 4 / Top Tier | `{Audit_Opinion}` | 🟢 **PASS** / 🔴 **FAIL** | 1 Point |
| **Test 6** | **Promoter Share Pledging & Encumbrance** | Promoter Pledged Shares $< 20\%$ | `{Pledge_Ratio}` | 🟢 **PASS** / 🔴 **FAIL** | 1 Point |
| **Test 7** | **Related Party Transactions (RPT) & Loans** | RPTs $< 10\%$ of Net Worth (Arm's Length) | `{RPT_Ratio}` | 🟢 **PASS** / 🔴 **FAIL** | 1 Point |
| **SUMMARY** | **FINAL MALIK FRAUD RISK SCORECARD** | **Target: 6 - 7 Points = GREEN (LOW RISK)** | **Total Points: `{Score}/7`** | 🟢 **GREEN** | **LOW RISK** |

---

## Output Schema
Return `fraud_risk_score` as `GREEN`, `AMBER`, or `RED`, accompanied by `soic_deep_forensic_audit`, `malik_scorecard_breakdown`, `accounting_fraud_audit`, `writeoff_exceptional_audit`, `kmp_resignation_audit`, `auditor_report_audit`, `kmp_remuneration_audit_with_rationale`, `subsidiary_rpt_audit`, and `walk_the_talk_scorecard`.

---

---

## 🧠 Dynamically Learned 24H Result Red Flags & Forensic Patterns
- **Ind-Swift Laboratories Ltd (`INDSWFTLAB`)**: 🟡 Operating Leverage / Inventory Valuation: Operating profit growth 2.5x higher than Revenue growth.
- **Dynamatic Technologies Ltd (`DYNAMATECH`)**: 🟡 Operating Leverage / Inventory Valuation: Operating profit growth 2.5x higher than Revenue growth.
- **Nitin Spinners Ltd (`NITINSPIN`)**: 🟡 Operating Leverage / Inventory Valuation: Operating profit growth 2.5x higher than Revenue growth.
- **Akums Drugs & Pharmaceuticals Ltd (`AKUMS`)**: 🟡 Operating Leverage / Inventory Valuation: Operating profit growth 2.5x higher than Revenue growth.
- **PC Jeweller Ltd (`PCJEWELLER`)**: 🟡 Operating Leverage / Inventory Valuation: Operating profit growth 2.5x higher than Revenue growth.
- **Colab Platforms Ltd (`COLAB`)**: 🟡 Operating Leverage / Inventory Valuation: Operating profit growth 2.5x higher than Revenue growth.
- **Onida Electronics Ltd (`ONIDA`)**: 🔴 PAT-Revenue Divergence: High Sales growth with declining/negative PAT.
- **PNC Infratech Ltd (`PNCINFRA`)**: 🔴 PAT-Revenue Divergence: High Sales growth with declining/negative PAT.
- **Bosch Ltd (`BOSCHLTD`)**: 🔴 PAT-Revenue Divergence: High Sales growth with declining/negative PAT.
- **TVS Supply Chain Solutions Ltd (`TVSSCS`)**: 🔴 PAT-Revenue Divergence: High Sales growth with declining/negative PAT.
- **Rupa & Company Ltd (`RUPA`)**: 🟡 Operating Leverage / Inventory Valuation: Operating profit growth 2.5x higher than Revenue growth.
- **PDS Ltd (`PDSL`)**: 🟡 Operating Leverage / Inventory Valuation: Operating profit growth 2.5x higher than Revenue growth.
- **Sharda Motor Industries Ltd (`SHARDAMOTR`)**: 🔴 PAT-Revenue Divergence: High Sales growth with declining/negative PAT.
- **Delhivery Ltd (`DELHIVERY`)**: 🔴 PAT-Revenue Divergence: High Sales growth with declining/negative PAT.
- **Tarsons Products Ltd (`TARSONS`)**: 🔴 PAT-Revenue Divergence: High Sales growth with declining/negative PAT.

---

---

## 🧠 Master Forensic Fraud Checklist: Dr. Vijay Malik & SOIC Audit Benchmarks

### 🔴 PAT-Revenue Divergence & Margin Compression
- **Source**: Dr. Vijay Malik Case Studies
- **Gist / Mechanism**: Company inflates top-line sales via low-margin uncollectible orders or aggressive credit terms, while high operating/interest costs destroy net profit.
- **Mandatory Audit Rule**: `Compare 3-year Revenue YoY % vs PAT YoY %; flag any divergence >15%.`

### 🔴 Inventory Valuation Inflation & Cost Capitalization
- **Source**: Dr. Vijay Malik Case Studies
- **Gist / Mechanism**: Management shifts raw material expenses out of P&L into Capital Work-in-Progress (CWIP) or changes inventory valuation methods (e.g. FIFO to Weighted Average) to artificially inflate operating margins.
- **Mandatory Audit Rule**: `Audit CWIP additions, inventory growth vs sales growth, and inventory accounting policy disclosures.`

### 🔴 Delayed Impairments & Balance Sheet Carrying Value Masking
- **Source**: Dr. Vijay Malik Case Studies
- **Gist / Mechanism**: Management avoids writing off loss-making subsidiary investments to protect standalone Net Worth, using aggressive DCF assumptions (low WACC, high terminal growth) until forced by auditors.
- **Mandatory Audit Rule**: `Track multi-year Key Audit Matter (KAM) warnings; calculate Total Exposure (Equity + Preference + Unsecured Loans + Guarantees) vs Net Worth.`

### 🔴 Software & Database Audit Trail Disruption (Rule 11(g))
- **Source**: Dr. Vijay Malik Case Studies
- **Gist / Mechanism**: Disabling database-level audit logs allows direct database editing, manual journal entry manipulation, or POS transaction deletion without leaving an automated audit trail.
- **Mandatory Audit Rule**: `Verify statutory auditor's Companies Act Rule 11(g) qualification across consecutive annual reports.`

### 🔴 Aggregator & Trade Receivable Concentration Risk
- **Source**: Dr. Vijay Malik Case Studies
- **Gist / Mechanism**: Fictitious sales or uncollectible receivables are allowed to accumulate without bad debt provisions, masking core credit loss drag.
- **Mandatory Audit Rule**: `Audit top 3 customer concentration % in receivables footnote and check allowance for expected credit loss (ECL).`

### 🔴 Unrecognized Deferred Tax Assets (DTA) & Loss Expiration
- **Source**: Dr. Vijay Malik Case Studies
- **Gist / Mechanism**: Subsidiaries incur heavy tax losses expiring in 5 years with no reasonable certainty of future taxable profit, forcing management to refuse DTA recognition or write off past DTAs.
- **Mandatory Audit Rule**: `Audit tax footnote for unbooked DTAs and tax loss expiration schedules.`

### 🔴 Exceptional One-Off Item Abuse & Non-Operating PAT Kickers
- **Source**: Dr. Vijay Malik Case Studies
- **Gist / Mechanism**: Management uses non-operating write-backs of trade payables (>3Y old) or asset sale gains to mask operating losses.
- **Mandatory Audit Rule**: `Separate Operating PAT from Total PAT; subtract exceptional items and write-backs from net profit.`

### 🔴 Preferential Warrant Arbitrage & Share Dilution
- **Source**: Dr. Vijay Malik Case Studies & SEBI Orders (Varanium Cloud / Promoter Warrants)
- **Gist / Mechanism**: Promoters issue preferential warrants to themselves when stock prices are depressed. They inflate quarterly earnings or announce hyped news to drive the share price up, then convert the warrants at a fraction of market value, diluting minority shareholders and taking risk-free gains.
- **Mandatory Audit Rule**: `Audit warrant issuance price vs current market price; verify 25% upfront money received and check share count dilution %.`

### 🔴 Related Party Asset Mispricing & Cash Siphoning
- **Source**: Dr. Vijay Malik Case Studies (National Peroxide / RPT Asset Mispricing)
- **Gist / Mechanism**: Management transfers valuable company land, patents, or subsidiaries to promoter-owned private entities at dirt-cheap book value, or forces the public company to buy illiquid promoter real estate at inflated valuations, draining cash out of the public firm.
- **Mandatory Audit Rule**: `Inspect Related Party Transactions (RPT) footnote for asset purchase/sale valuations; verify independent valuation reports.`

### 🔴 Interest-Free / Low-Interest Inter-Corporate Loans to Promoter Shells
- **Source**: Dr. Vijay Malik Case Studies (Promoter Money Churning)
- **Gist / Mechanism**: The public company takes high-interest bank debt (12-14%) and simultaneously extends interest-free or low-interest unsecured loans/advances to promoter private entities or loss-making subsidiaries, effectively transferring public credit to promoters.
- **Mandatory Audit Rule**: `Compare interest cost paid on borrowings vs interest income received on inter-corporate deposits (ICDs); flag loans >5% of Net Worth.`

### 🔴 Disproportionate Promoter Remuneration & Royalty Extraction
- **Source**: Dr. Vijay Malik Case Studies (Management Remuneration Audit)
- **Gist / Mechanism**: Promoters structure executive salaries, commissions, and brand royalty payments to private family trusts to extract 5-10% of gross profits, maintaining high pay checks even during years when Net Profit declines or turns negative.
- **Mandatory Audit Rule**: `Calculate Total Promoter Remuneration + Royalty as % of Net Profit; flag if remuneration grows while Net Profit drops.`

### 🔴 Capital Expenditure Inflation via CWIP Capitalization
- **Source**: Dr. Vijay Malik Case Studies (CWIP & Interest Capitalization Shenanigans)
- **Gist / Mechanism**: Management stalls CWIP capitalization for 3-5 years, parking routine operating expenses, raw material costs, and interest payments into CWIP instead of charging them to P&L, artificially inflating operating profit (EBITDA) and net assets.
- **Mandatory Audit Rule**: `Audit CWIP as % of Net Fixed Assets (>15% is high risk); verify multi-year CWIP age analysis and capitalized interest outgo.`

### 🔴 Fictitious Sales & DSO Inflation (Receivables Siphoning)
- **Source**: Dr. Vijay Malik Case Studies (Receivable Days & CFO vs PAT)
- **Gist / Mechanism**: Management books bogus sales to related party distributors or fictitious customers near quarter-end to meet revenue targets. Because no cash is ever collected, Days Sales Outstanding (DSO) explodes and CFO remains far below PAT.
- **Mandatory Audit Rule**: `Compare 5-Year Cumulative CFO vs Cumulative PAT (CFO < PAT indicates bogus earnings); check DSO growth rate vs Revenue growth rate.`

### 🔴 Weak Internal Controls & Senior Management Embezzlement
- **Source**: Dr. Vijay Malik Case Studies (National Peroxide Internal Control Failure)
- **Gist / Mechanism**: Lack of segregation of duties and missing/disabled POS/accounting database audit trails allow senior executives or promoters to siphon funds via fake vendor invoices and unrecorded cash transactions for nearly a decade.
- **Mandatory Audit Rule**: `Audit Companies Act Rule 11(g) database audit trail qualification and internal auditor reports on material weaknesses.`

### 🔴 Non-Operating Other Income Inflation
- **Source**: Dr. Vijay Malik Case Studies (Financial Shenanigans - Other Income)
- **Gist / Mechanism**: Management uses interest income, asset sale gains, or investment revaluations (accounting for >20% of PBT) to hide declining core operating profits and present a false picture of healthy bottom-line growth.
- **Mandatory Audit Rule**: `Calculate Other Income as % of Profit Before Tax (PBT); flag any company where Other Income >15% of PBT.`
