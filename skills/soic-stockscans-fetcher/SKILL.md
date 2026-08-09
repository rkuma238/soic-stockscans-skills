---
name: soic-stockscans-fetcher
description: MANDATORY step for equity analysis. Automatically logs into StockScans.in, extracts all 6 SOIC x StockScans reports (Business Overview, Growth Catalysts, Guidance Report, Forensic Report, Financial Model, Deep Dive Report) for any stock symbol, and synthesizes them including exhaustive 6-pillar SOIC Intelligence & Guidance Track Record Analysis into plain-English equity research insights.
version: 2.5.0
---

# SOIC x StockScans Report Card Extractor & Track Record Synthesis (v2.5.0)

This skill logs into StockScans.in, extracts all 6 official SOIC report cards, and synthesizes them into Section 23 `### SOIC x StockScans Intelligence & Synthesis` of every equity research report.

---

## Mandatory 6-Pillar Sub-Section Structure for Section 23 `### SOIC x StockScans Intelligence & Synthesis`

Every equity research report MUST format Section 23 into the following 6 explicit sub-sections:

* **23.1 Business Overview & Segment Deep-Dive**: Exhaustive breakdown of core business segments, product portfolios, brand licensing terms, and operational engines.
* **23.2 Growth Catalysts & Forward Triggers**: Detailed analysis of capacity expansions, capital infusions, margin drivers, and operational tailwinds.
* **23.3 Management Guidance vs Historical Outcomes Scorecard**: Full dated multi-item table classifying guidance into Delivered, On Track, Pending, Partial, and Missed/Delayed with exact metrics and credibility score.
* **23.4 SOIC Forensic Audit & Accounting Quality Scorecard Table**:
  - MUST format into an **Exhaustive SOIC Forensic Audit Scorecard Table** classifying ALL SOIC forensic findings into Severity (🔴 **MAJOR**, 🟡 **MINOR**, 🟢 **CLEAN**).
  - Must cover 100% of SOIC forensic findings: Delayed subsidiary impairments, subsidiary loan/guarantee exposures, database audit trail non-compliance, unrecognized DTAs, aggregator receivable concentration, and auditor rotation history.
  - MUST include dedicated `🔍 Reading Between the Lines & Analytical Takeaways (Forensic Audit)`.
* **23.5 Financial Model & Unit Economics**: Comprehensive review of revenue drivers, plant-level/store-level vs company-level EBITDA, lease/interest/depreciation impacts, and FCF roadmap.
* **23.6 Strategic Moats & Operational Risk Audit**: Detailed narrative on competitive moats, pricing power, and operational risk mitigation.





---

## Execution Workflow

1. **Run Extractor Script**:
   Execute the automated Playwright script passing the stock symbol (e.g., `NSE:RBA`, `RBA`, `HDFCBANK`):
   ```bash
   python3 /Users/rakeshkumarr/.gemini/config/skills/soic-stockscans-fetcher/scripts/fetch_soic_reports.py NSE:RBA
   ```

2. **Extracted Reports Coverage**:
   - **Business Overview**: What the company does, business segments, key product offerings, and franchisee/ownership structure in plain English.
   - **Growth Catalysts**: Forward capacity expansions, store additions, new product launches, financial infusions, and macro tailwinds.
   - **Guidance Report**: Management guidance vs historical actual outcomes (ADS, EBITDA margin targets, store count targets, Capex guidance).
   - **Forensic Report**: Accounting quality, related-party transaction red flags, statutory auditor qualifications, and audit scorecards.
   - **Financial Model**: Revenue breakdown, margin trajectories, capital deployment efficiency, and historical financial metrics.
   - **Deep Dive Report**: In-depth competitive moats and strategic positioning.

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

