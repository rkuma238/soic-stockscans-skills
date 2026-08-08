---
name: forensic-analyzer
description: Deep forensic analysis of earnings quality, cash conversion, auditor KAMs, subsidiary guarantees, database audit trail compliance, and accounting red flags. Use when assessing earnings quality, detecting accounting manipulation, inspecting annual report footnotes, or auditing management credibility.
version: 3.5.0
---

# Forensic Analyzer - Independent Institutional Forensic Accounting Detective (v3.5.0)

Specialized independent forensic analysis of financial statements, annual report footnotes, statutory auditor reports, and conference call transcripts to detect accounting manipulation, audit trail flaws, and assess true earnings quality.

---

## Independent Deep Forensic Audit Framework (6 Mandatory Pillars)

Even when external pre-packaged report cards are unavailable, the agent MUST independently perform the following 6-point deep forensic audit directly from annual report disclosures, notes to accounts, and auditor reports:

### Pillar 1: Auditor Key Audit Matters (KAM) & Delayed Impairment Audit
1. **Multi-Year KAM Footnote Inspection**: Search statutory auditor reports across 3–5 consecutive annual reports for Key Audit Matters (KAMs).
2. **Impairment Provision Lag Detection**: Check if investments in subsidiaries, joint ventures, goodwill, ROU assets, or CWIP were listed as KAMs for multiple years (e.g. 2–4 years) before management recorded an impairment provision on P&L.
3. **Valuation Model Assumptions**: Audit discount rates (e.g. WACC/DCF discount rate), cash flow projections, and terminal growth rates used in impairment calculations.

### Pillar 2: Subsidiary Financial Exposure & Guarantee Audit
1. **Parent Entity Total Exposure**: Extract and sum all 4 forms of parent financial commitment to loss-making subsidiaries from Notes to Accounts (Related Party Transactions & Contingent Liabilities notes):
   - Equity Share Capital invested (₹ Cr)
   - Preference Share Capital invested (₹ Cr)
   - Inter-Corporate Unsecured Loans & Advances + Interest Rates (₹ Cr)
   - Outstanding Corporate & Performance Guarantees (₹ Cr)
2. **Shareholder Voting Governance Pushback**: Search AGM/EGM voting results on Postal Ballot resolutions for inter-corporate loan approvals. Identify if >10% of minority shareholders voted against extending further loans.

### Pillar 3: Software & Database Audit Trail Compliance (Companies Act Rule 11(g))
1. **Auditor Report Rule 11(g) Section**: Inspect the Statutory Auditor's Report under *"Report on Other Legal and Regulatory Requirements"* for Rule 11(g) audit trail disclosures.
2. **Database-Level Audit Trail Verification**: Check if auditors reported non-compliance regarding disabled audit trail features at the database level for accounting software or POS systems across consecutive years.

### Pillar 4: Trade Receivables & Customer Concentration Risk Audit
1. **Customer / Aggregator Concentration**: Calculate the percentage of total trade receivables concentrated in the top 2–3 customers or food delivery aggregators (e.g. Zomato, Swiggy) from Financial Notes.
2. **Provisioning Policy Audit**: Verify if collective impairment allowances were recorded against concentrated balances.

### Pillar 5: Unrecognized Deferred Tax Assets (DTA) & Loss Expiry Audit
1. **Tax Notes Extraction**: Inspect Note on Income Taxes / Deferred Tax Assets in the Annual Report.
2. **Unrecorded DTA Quantum**: Extract unrecorded DTA on carried-forward business losses and unabsorbed depreciation for parent and operating subsidiaries (signaling lack of reasonable certainty of future taxable profits).
3. **Loss Expiry Schedule**: Identify tax losses expiring within 5 years.

### Pillar 6: Accounting Policy Shifts & Exceptional Item Abuse Audit
1. **Accounting Policy Note Inspection**: Inspect Note 1 (Summary of Significant Accounting Policies) for changes in inventory valuation methods (e.g. FIFO to Weighted Average), revenue recognition, or depreciation methods.
2. **Exceptional Non-Operating PAT Impact**: Audit non-recurring franchisee fee waivers, labor code provisions, or one-off asset sales that mask core operating losses.

---

## Core Forensic Scorecard Framework

### 1. Earnings Quality Assessment (Score 1-10)

#### Cash Conversion Analysis
- **OCF/Net Profit Ratio**: Healthy >0.8, Warning <0.7, Red Flag <0.5
- **Free Cash Flow Quality**: FCF vs reported earnings consistency
- **Cash Flow Timing**: Seasonal patterns vs one-time boosts

#### Accrual Quality Analysis  
- **Total Accruals**: (Net Income - OCF) / Total Assets
- **Working Capital Accruals**: Changes in receivables, inventory, payables
- **Discretionary Accruals**: Management's accounting choices impact

---

### 2. Dr. Vijay Malik 7-Point Fraud Risk Scorecard Breakdown

| Malik Forensic Test # | Forensic Check Name | Benchmark & Target Criteria | Test Verdict | Score Weight |
| :---: | :--- | :--- | :---: | :---: |
| **Test 1** | **Sales vs. Cash Flow from Operations (CFO)** | 5-Yr Cumulative CFO $>$ Cumulative PAT | 🟢 **PASS** / 🔴 **FAIL** | 1 Point |
| **Test 2** | **Capital Work-in-Progress (CWIP) vs Net Assets**| CWIP $< 15\%$ of Net Fixed Assets | 🟢 **PASS** / 🔴 **FAIL** | 1 Point |
| **Test 3** | **Receivables & DSO Growth vs Sales Growth** | Receivables Growth $\le$ Sales Growth | 🟢 **PASS** / 🔴 **FAIL** | 1 Point |
| **Test 4** | **Other Income as % of Profit Before Tax (PBT)**| Other Income $< 15\%$ of PBT | 🟢 **PASS** / 🔴 **FAIL** | 1 Point |
| **Test 5** | **Auditor Qualifications & Key Audit Matters**| Unqualified Audit Opinion from Big 4 / Top Tier | 🟢 **PASS** / 🔴 **FAIL** | 1 Point |
| **Test 6** | **Promoter Share Pledging & Encumbrance** | Promoter Pledged Shares $< 20\%$ | 🟢 **PASS** / 🔴 **FAIL** | 1 Point |
| **Test 7** | **Related Party Transactions (RPT) & Loans** | RPTs $< 10\%$ of Net Worth (Arm's Length) | 🟢 **PASS** / 🔴 **FAIL** | 1 Point |
| **SUMMARY** | **FINAL MALIK FRAUD RISK SCORECARD** | **Target: 6 - 7 Points = GREEN (LOW RISK)** | 🟢 **GREEN** | **LOW RISK** |

---

## Forensic Analysis Output

### Forensic Scorecard Summary
| Component | Score (1-10) | Weight | Key Evidence & Footnote Observations |
| :---| :---: | :---: | :--- |
| **Earnings Quality** | 7/10 | 25% | OCF/Profit ratio >0.9; clean cash conversion. |
| **Balance Sheet Integrity** | 5/10 | 25% | Subsidiary loan/guarantee exposure & delayed impairment flags. |
| **Governance & RPT** | 6/10 | 25% | Zero promoter pledging; minor shareholder pushback on loans. |
| **Audit & Disclosure** | 9/10 | 25% | Big 4 audit opinion; database audit trail Rule 11(g) note. |
| **Overall Score** | **6.7/10** | **100%** | **MODERATE FORENSIC QUALITY** |

---

## Integration & Execution Protocol

- **Execution**: Must be run independently across all corporate stock research pipelines (`normal-company-pipeline` and `equity-research-orchestrator`).
- **Inputs**: Annual report PDF / text extractions, statutory auditor reports, financial footnotes, BSE/NSE filings, screener.in financials.
- **Outputs**: Independent 6-Pillar Deep Forensic Audit Table, Dr. Vijay Malik 7-Point Scorecard, and Overall Forensic Score (1-10).