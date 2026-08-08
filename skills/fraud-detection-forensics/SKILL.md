---
name: fraud-detection-forensics
description: "Forensic accounting skill: detects earnings manipulation, Related Party Transaction (RPT) risks, KMP salary anomalies, KMP/Board resignations, auditor report KAMs, subsidiary guarantees, bad debt write-offs, exceptional one-off items, unclaimed liabilities, and includes a mandatory Walk The Talk Management Guidance Scorecard."
type: ATOMIC
version: 3.2.0
children: []
inputs:
  - company_data: object
  - annual_report_disclosures: object
  - periods: string[]
outputs:
  - forensic_flags: object[]
  - walk_the_talk_scorecard: object
  - auditor_report_audit: object
  - kmp_resignation_audit: object
  - writeoff_exceptional_audit: object
  - fraud_risk_score: string
---

# Fraud Detection & Forensics Analyzer (v3.3.0)

Applies to all corporate companies, banks, and NBFCs. Implements Dr. Vijay Malik's 7-point Forensic Triangulation, **Three-Way Data Cross-Verification Accounting Fraud Triangulation**, the **Walk The Talk Guidance Scorecard**, **Auditor Report KAM Audit**, **KMP & Board Resignation Audit**, **KMP Remuneration Audit**, **Subsidiary Performance Breakdown**, **Related Party Transactions (RPT) Audit**, and **Write-Offs, Exceptional One-Offs & Unclaimed Liabilities Audit**.

---

## 0. Three-Way Data Comparison & Accounting Fraud Audit (MANDATORY FOR EVERY COMPANY)

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

## 1. Write-Offs, Exceptional One-Offs & Unclaimed Liabilities Audit Table (MANDATORY FOR EVERY COMPANY)

Evaluate bad debt write-offs, technical write-offs, non-recurring exceptional items, and unclaimed trade payable write-backs:

| Item Category | Extracted Financial / Footnote Details | Value (₹ Cr) | % of Net Profit / Sales | Forensic Risk Rating & Audit Verdict |
| :--- | :--- | :---: | :---: | :---: |
| **Bad Debt & Technical Write-Offs** | NPA / Bad debt write-offs utilized against provisions | `{WO_Val}` | `{WO_PAT_%}%` | 🟢 **NORMAL BALANCE SHEET CLEANUP** / 🔴 **HIGH LOSS DRAG** |
| **Bad Debt Recoveries** | Recovery credited back to P&L from written-off accounts | `{Rec_Val}` | `{Rec_PAT_%}%` | 🟢 **CORE CASH RECOVERY** |
| **Exceptional / One-off Gains/Losses**| Non-recurring gains, merger restructuring, tax one-offs | `{Exc_Val}` | `{Exc_PAT_%}%` | 🟢 **PAR** / 🟡 **NON-OPERATIONAL PAT KICKER** |
| **Unclaimed Bills & Payable Write-backs**| Write-back of unclaimed liabilities & trade payables (>3Y) | `{WB_Val}` | `{WB_PAT_%}%` | 🟢 **CLEAN** / 🔴 **EARNINGS INFLATION RISK** |

#### Forensic Write-Off & One-Off Rules:
- 🔴 **HIGH FORENSIC RED FLAG**: Core PAT growth driven primarily by write-back of unclaimed trade payables, unbilled revenue write-downs $>5\%$ of Sales, or persistent unrecorded bad debt write-offs.
- 🟢 **CLEAN / LOW RISK**: Technical write-offs fully covered by existing provisions, zero earnings reliance on trade payable write-backs.

---

## 2. KMP & Board Resignation Audit Table
Audit CFO, CEO, CRO, Company Secretary, and Independent Director resignations over past 3-5 years.

---

## 3. Auditor's Report & Governance Audit Table
Statutory Auditor Name, Audit Firm Tier (Big 4 check), Audit Opinion (`UNQUALIFIED` / `QUALIFIED`), Key Audit Matters (KAMs).

---

## 4. KMP Remuneration & Executive Compensation Alignment Audit Table (MANDATORY RATIONALE)

Every analysis MUST explicitly justify **WHY** KMP compensation is rated `GREEN`, `AMBER`, or `RED`:

| KMP Name & Designation | Total Remuneration (₹ Cr) | Remuneration % of Sales / PAT / EBITDA | YoY Pay Growth vs Employee Cost Growth | SEBI Section 197 & Peer Benchmark | Forensic Rating | Explicit Justification & Rationale for Rating |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **MD / CEO** | `{CEO_Pay}` | `{CEO_PAT_%}%` | `{Pay_vs_EmpCost}` | `{Peer_Benchmark}` | 🟢 **GREEN** / 🔴 **RED** | **MANDATORY EXPLICIT WHY RATIONALE**: Explain why pay is aligned or inflated. |

#### KMP Remuneration Forensic Rating Rules:
- 🟢 **GREEN (LOW RISK)**: CEO pay $< 2\%$ of Net Profit ($< 0.5\%$ of Sales for loss-making growth companies), pay growth $\le$ employee cost growth, compliant with SEBI Section 197 ceiling or RBI Section 35B approval, zero unapproved profit commissions.
- 🟡 **AMBER (MODERATE RISK)**: CEO pay $2\% - 5\%$ of Net Profit, pay growth significantly outstripping employee salary growth ($>15\%$ divergence).
- 🔴 **RED (HIGH RISK)**: CEO pay $> 5\%$ of Net Profit, or CEO pay increasing $>20\%$ during a year when Net Profit / EBITDA declined $>20\%$, or unapproved related party managerial payouts.

---

## 5. Dr. Vijay Malik 7-Point Fraud Risk Scorecard Breakdown (MANDATORY FOR EVERY COMPANY)

Calculate the final **MALIK FRAUD RISK SCORE** (`GREEN (LOW RISK)`, `AMBER (MODERATE RISK)`, or `RED (HIGH RISK)`) by evaluating all 7 Dr. Vijay Malik forensic tests:

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

## 6. Subsidiary & Related Party Transactions (RPT) Audit Table

---

## 7. The 'Walk The Talk' Management Guidance Scorecard

---

## Output
Return `fraud_risk_score` as `GREEN`, `AMBER`, or `RED`, accompanied by `malik_scorecard_breakdown`, `accounting_fraud_audit`, `writeoff_exceptional_audit`, `kmp_resignation_audit`, `auditor_report_audit`, `kmp_remuneration_audit_with_rationale`, `subsidiary_rpt_audit`, and `walk_the_talk_scorecard`.


