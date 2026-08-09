---
name: soic-stockscans-fetcher
description: MANDATORY step for equity analysis. Automatically logs into StockScans.in, extracts all 6 SOIC x StockScans reports (Business Overview, Growth Catalysts, Guidance Report, Forensic Report, Financial Model, Deep Dive Report) for any stock symbol, and synthesizes 100% of forensic flags and guidance items into plain-English equity research insights without omission.
version: 3.0.0
---

# SOIC x StockScans Report Card Extractor & Track Record Synthesis (v3.0.0)

This skill logs into StockScans.in, extracts all 6 official SOIC report cards, and synthesizes 100% of their raw contents into Section 23 `### SOIC x StockScans Intelligence & Synthesis` of every equity research report.

---

## Mandatory 6-Pillar Sub-Section Structure for Section 23 `### SOIC x StockScans Intelligence & Synthesis`

Every equity research report MUST format Section 23 into the following 6 explicit sub-sections:

* **23.1 Business Overview & Segment Deep-Dive**: Exhaustive breakdown of core business segments, product portfolios, brand licensing terms, and operational engines.
* **23.2 Growth Catalysts & Forward Triggers**: Detailed analysis of capacity expansions, capital infusions, margin drivers, and operational tailwinds.
* **23.3 Management Guidance vs Historical Outcomes Scorecard**: Full dated multi-item table classifying guidance into Delivered, On Track, Pending, Partial, and Missed/Delayed with exact metrics and credibility score.
* **23.4 SOIC Forensic Audit & Accounting Quality Scorecard Table (MANDATORY 100% EXTRACTION)**:
  - **NON-NEGOTIABLE RULE**: You MUST parse 100% of the raw text inside `soic_Forensic_Report.txt`. Every single audit observation, impairment timeline, loan/guarantee disclosure, database audit trail non-compliance, unbooked DTA, and receivable concentration MUST be extracted and listed in a structured table.
  - **ZERO GENERIC SUMMARIES**: You are STRICTLY FORBIDDEN from replacing specific SOIC forensic observations with generic summaries (e.g. "Clean audit history").
  - **MANDATORY TABLE FORMAT**:
    - Parameter Name
    - Severity Level: 🔴 **MAJOR**, 🟡 **MINOR**, or 🟢 **CLEAN**
    - Exact Financial Metric & Audit Finding (e.g. ₹120 Cr provision post 4-yr KAM flags, ₹239 Cr guarantees, 3-yr database audit trail non-compliance, >₹212 Cr unbooked DTAs, 66.6% aggregator concentration)
    - Governance & Strategic Takeaway
  - MUST include dedicated `🔍 Reading Between the Lines & Analytical Takeaways (Forensic Audit)` directly beneath the table.
* **23.5 Financial Model & Unit Economics**: Comprehensive review of revenue drivers, plant-level/store-level vs company-level EBITDA, lease/interest/depreciation impacts, and FCF roadmap.
* **23.6 Strategic Moats & Operational Risk Audit**: Detailed narrative on competitive moats, pricing power, and operational risk mitigation.

---

## Execution Workflow

1. **Run Extractor Script**:
   Execute the automated Playwright script passing the stock symbol (e.g., `NSE:RBA`, `RBA`, `AARTIPHARM`):
   ```bash
   python3 /Users/rakeshkumarr/.gemini/config/skills/soic-stockscans-fetcher/scripts/fetch_soic_reports.py NSE:<SYMBOL>
   ```

2. **Extracted Reports Coverage & Parsing Mandate**:
   - **Business Overview**: Extract segment split, manufacturing/store footprints, brand licenses.
   - **Growth Catalysts**: Extract capacity expansions, capital infusions, margin drivers.
   - **Guidance Report**: Extract ALL historical management guidance statements into an exhaustive scorecard table.
   - **Forensic Report**: Extract ALL 8+ forensic checkpoints (impairment delays, subsidiary loans/guarantees, database audit trail non-compliance, unbooked DTAs, receivable concentrations, auditor rotations) into Section 23.4.
   - **Financial Model**: Extract quarterly/annual margin trends, capital deployment efficiency.
   - **Deep Dive Report**: Extract competitive moats and industry dynamics.


3. **Mandatory Exhaustive Synthesis Output Requirements (Section 18)**:
   Always incorporate the extracted SOIC StockScans findings into the final equity research report under a dedicated, highly detailed section titled:
   `### SOIC x StockScans Intelligence & Synthesis`
   
   Section 18 MUST include the following 6 detailed subsections:
   - **18.1 Business Overview & Segment Deep-Dive**: Exhaustive breakdown of core business segments, menu ladders, brand licensing terms, and operational engines.
   - **18.2 Growth Catalysts & Forward Triggers**: Detailed analysis of capacity expansions, capital infusions, margin drivers, and operational tailwinds.
   - **18.3 Management Guidance vs Historical Outcomes Scorecard**: Full dated multi-item table classifying guidance into *Delivered*, *On Track*, *Pending*, and *Missed/Delayed* with exact metrics.
   - **18.4 Forensic Audit, Accounting Quality & Dr. Vijay Malik Fraud Risk Scorecard**: Full 7-point checklist covering CFO vs Sales, CWIP ratio, Receivables, Other Income dependency, Auditor Qualifications, Promoter Pledging, and RPTs.
   - **18.5 Financial Model & Unit Economics**: Comprehensive review of revenue drivers, store-level vs company-level EBITDA, Ind AS lease interest/depreciation impacts, and FCF roadmap.
   - **18.6 Strategic Moats & Operational Risk Audit**: Detailed narrative on competitive moats, pricing power, and operational risk mitigation.

