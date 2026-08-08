---
name: soic-stockscans-fetcher
description: MANDATORY step for equity analysis. Automatically logs into StockScans.in, extracts all 6 SOIC x StockScans reports (Business Overview, Growth Catalysts, Guidance Report, Forensic Report, Financial Model, Deep Dive Report) for any stock symbol, and synthesizes them into plain-English equity research insights.
---

# SOIC x StockScans Report Fetcher & Synthesizer

## Mandatory Execution Rule
**This skill MUST be executed for every equity analysis task.** 
Before completing any equity research report or company breakdown, you MUST fetch and synthesize the official **SOIC x StockScans Reports**.

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

3. **Synthesis & Plain-English Output Requirement**:
   Always incorporate the extracted SOIC StockScans findings into the final equity research report under a dedicated section titled:
   `### SOIC x StockScans Intelligence & Synthesis`
   Translating complex financial jargon into clear, actionable, simple plain English for investors.
