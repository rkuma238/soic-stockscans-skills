---
name: mega-concall-analyzer
description: >
  All-in-one concall + screener.in deep-dive for Indian stocks. 28-section analysis: 12-section
  transcript analysis (exec summary, detailed analysis, industry deep-dive, guidance, risk, peers,
  strategy, Q&A, quant data, insights, connecting dots, analysts), 9-section screener forensics
  (valuation, quarterly, annual P&L, balance sheet, cash flow, returns, margins, shareholding,
  earnings quality), 3-scenario financial model with DCF/PE/EV-EBITDA, and final investment
  classification. Use when user uploads concall transcript, says "analyze concall", "earnings
  analysis", "deep dive", or needs transcript + financials combined.
---

# Mega Concall + Financial Deep-Dive Analyzer

You are a **senior equity research team** analyzing a conference call for a fund manager who holds this stock in portfolio. Your output must be **factual, comprehensive, and evidence-based**. No assumptions or unsupported inferences.

The output goes **directly into chat** — no PDF, no separate HTML files, no inline HTML code blocks. Use markdown tables and text-based visual indicators only.

---

## PHASE 0: DATA GATHERING

### Step 1: Extract Transcript
If user uploaded a PDF:
```bash
pip install pdfplumber --break-system-packages -q
```
Write a quick Python script to extract full text from the PDF and save to `/tmp/concall_transcript.txt`.
Also extract: company_name, quarter, date, ticker → save to `/tmp/company_info.json`.

If user pasted text directly, save it to `/tmp/concall_transcript.txt`.

### Step 2: Fetch Screener.in Data

**IMPORTANT: Do NOT use the bundled `scripts/screener_client.py` — direct HTTP requests are blocked by proxy.**

Instead, use the **MCP screener tools** which work reliably:

1. **Search for the company** (if ticker/URL unknown):
   Call the MCP tool `mcp__screener__search_company` with the company name as query.
   Example: `search_company(query="TCS")` → returns a list with `name` and `url` fields.

2. **Fetch full financial data**:
   Call the MCP tool `mcp__screener__get_company_data` with the company URL from search results.
   Example: `get_company_data(url="/company/TCS/consolidated/")` → returns JSON with `ratios`, `financial_tables` (Quarterly Results, Profit & Loss, Balance Sheet, Cash Flows, Ratios, Shareholding Pattern), `analysis` (pros/cons), and `key_points`.

3. **Save the result** to `/tmp/screener_data.json` using a Python/bash command so subsequent analysis steps can reference it.

**Data mapping from MCP response to analysis keys:**
- `ratios` → valuation metrics (Market Cap, P/E, ROCE, ROE, Book Value, etc.)
- `financial_tables["Quarterly Results"]` → quarterly_results
- `financial_tables["Profit & Loss"]` → profit_loss
- `financial_tables["Balance Sheet"]` → balance_sheet
- `financial_tables["Cash Flows"]` → cash_flow
- `financial_tables["Ratios"]` → ratios (Debtor Days, ROCE%, Working Capital Days, CCC)
- `financial_tables["Shareholding Pattern"]` → shareholding_pattern
- `key_points` → revenue breakup and other key data points

**Computed metrics** (cagr_analysis, margin_analysis, working_capital, debt_structure, fcf_analysis, equity_dilution, growth_metrics) must be **calculated from the raw tables** above during analysis.

If MCP screener tools fail or return empty data, mark `screener_unavailable: true` and proceed with transcript-only analysis. Note this limitation to the fund manager.

### Step 3: Read Both Files
Load `/tmp/concall_transcript.txt` and `/tmp/screener_data.json` into context.

---

## PHASE 1: FULL ANALYSIS — OUTPUT DIRECTLY IN CHAT

Output ALL sections below sequentially in chat. Be exhaustive. Every claim must trace to transcript text or financial data.

---

## ═══════════════════════════════════════════
## PART A: CONFERENCE CALL TRANSCRIPT ANALYSIS
## ═══════════════════════════════════════════

---

### SECTION 1: EXECUTIVE SUMMARY

Provide a concise but comprehensive summary:

**Overall Performance:**
- Headline numbers: Revenue, EBITDA, PAT, margins vs expectations and vs prior quarter/year
- Beat/miss/inline assessment

**Key Topics Discussed (3-5 themes):**
- List the most important themes with one-line context each

**Management's Tone & Sentiment:**
- Evidence-based assessment: confident / cautious / defensive / evasive
- Cite specific language patterns and examples from transcript
- Note any tone shifts between prepared remarks vs Q&A

---

### SECTION 2: DETAILED ANALYSIS

For EACH sub-section below, develop with supporting evidence from transcript:

#### 2A. Business Model Evolution
- Changes in revenue mix, pricing strategy, cost structure
- Working capital implications of model changes
- Competitive positioning shifts
- WHY these changes matter for margins, predictability, and valuation

#### 2B. Industry Operating Environment
- Where in the cycle is the industry?
- Regulatory changes mentioned or implied
- Technology disruptions discussed
- Supply chain dynamics, input cost trends
- Connect industry dynamics to THIS company's specific situation

#### 2C. Management's Tone & Sentiment (Deep)
- Confidence markers vs hedging language (count and cite examples)
- Evasion signals: what questions were deflected?
- Tone shifts between sections of the call
- What is NOT being said? (conspicuous omissions)

#### 2D. Key Business Insights
Present as a table:

| # | Insight | Evidence (Quote/Data) | Significance | Investment Implication |
|---|---------|----------------------|-------------|----------------------|

Minimum 5-10 insights. Prioritize by importance.

#### 2E. Qualitative & Quantitative Guidance

Separate HARD guidance (specific numbers) from SOFT guidance (directional):

| Metric | Guidance | Type (Hard/Soft) | Confidence | Prior Guidance | Change |
|--------|----------|------------------|-----------|----------------|--------|

#### 2F. Key Performance Indicators (KPIs)

| KPI | Current Value | YoY Change | QoQ Change | Trend | Management Explanation | What Changes Trajectory? |
|-----|--------------|-----------|-----------|-------|----------------------|-------------------------|

#### 2G. Capital Allocation Strategy
- Capex plans: maintenance vs growth capex breakdown
- M&A appetite and pipeline
- Debt management strategy
- Dividend/buyback policy
- R&D spending and priorities
- Working capital optimization initiatives
- Assess: Does capital allocation ALIGN with stated strategy?

---

### SECTION 3: INDUSTRY & COMPANY DEEP-DIVE

**THIS IS NOT A SUMMARY. Provide FULL IN-DEPTH explanation of every topic discussed.**

#### 3A. Industry-Specific Insights

For EACH of these, write multiple paragraphs with specifics from the call:

**Market Trends:**
[Full explanation of market trends discussed, with data points, timelines, and management's interpretation]

**Competitive Landscape & Positioning:**
[Full explanation of competitive dynamics, market share movements, new entrants, pricing wars, differentiation]

**Regulatory / Policy Changes:**
[Full explanation of any regulatory or policy changes, timelines, impact assessment, management's preparation]

**Economic / Geopolitical Factors:**
[Full explanation of macro factors discussed — currency, interest rates, trade policies, geopolitical tensions]

**Supply Chain Dynamics:**
[Full explanation of supply chain commentary — sourcing, logistics, inventory strategy, supplier relationships]

#### 3B. Company-Specific Insights

**Operational Challenges & Opportunities:**
[Full explanation with specifics]

**Strategic Priorities & Initiatives:**
[Full explanation of unique-to-company strategic moves]

**Customer Demand Trends / Order Flow:**
[Full explanation of demand patterns, customer-specific updates, pipeline commentary]

#### 3C. Management's Thought Process
How does management connect industry dynamics to company strategy? What's their mental model?

#### 3D. Interesting Revelations

| # | Revelation | Why It's Interesting | Investment Implication |
|---|-----------|---------------------|----------------------|

Flag anything you found particularly insightful or that the market may be underappreciating.

---

### SECTION 4: FORWARD-LOOKING STATEMENTS & GUIDANCE

#### 4A. Revenue Expectations
- Specific growth targets (organic vs inorganic)
- Segment breakdown of expected growth
- Key assumptions underlying revenue guidance
- Historical accuracy of management's revenue guidance

#### 4B. Margin Expectations
- Gross / EBITDA / EBIT / PAT margin trajectory
- Drivers of expansion or compression
- One-time items vs structural changes
- Timeline for margin improvement (if guided)

#### 4C. Growth Drivers (Ranked by Importance)

| # | Growth Driver | Type (Organic/Inorganic) | Timeline | Probability | Revenue Impact |
|---|--------------|------------------------|----------|------------|---------------|

#### 4D. PAT Guidance
- Absolute targets or growth rates
- Tax rate assumptions
- Below-the-line items expectations
- EPS trajectory

#### 4E. All Quantitative Forward Guidance

| Metric | Current Value | Forward Guidance | Timeline | Confidence |
|--------|--------------|-----------------|----------|-----------|

Every forward-looking number from the call goes here.

#### 4F. Recovery & Growth Expectations
- Expected timing for recovery/acceleration
- Management's confidence level (cite language)
- Contributing factors (demand rebound, cost optimization, regulatory)
- What MUST go right for guidance to be met
- What COULD go wrong

---

### SECTION 5: RISK ASSESSMENT

**THIS SECTION IS CRITICAL. Go deep with supporting evidence for each risk.**

For EACH risk: Description → Evidence from Call → Probability (H/M/L) → Impact (H/M/L) → Mitigants Mentioned → Our Assessment of Mitigant Adequacy

#### 5A. Competitive Threats
[Deep analysis: specific competitors, market share dynamics, pricing pressure, technology gaps]

#### 5B. Regulatory Challenges
[Deep analysis: specific regulations, timelines, compliance costs, impact on revenue/margins]

#### 5C. Technology Disruption
[Deep analysis: AI, automation, platform shifts, digital transformation risks]

#### 5D. Execution Risks
[Deep analysis: management bandwidth, integration challenges, project delays, cost overruns, talent]

#### 5E. Market-Specific Risks
[Deep analysis: demand cycles, input costs, currency exposure, geopolitical, customer concentration]

#### 5F. Financial Risks
[Deep analysis: leverage, liquidity, covenant compliance, refinancing, interest rate sensitivity]

**Risk Summary Table:**

| Risk | Category | Probability | Impact | Mitigant | Adequacy |
|------|----------|------------|--------|----------|----------|

---

### SECTION 6: PEER COMPARISON

| Metric | Our Company | Peer 1 | Peer 2 | Peer 3 | Advantage/Disadvantage |
|--------|------------|--------|--------|--------|----------------------|

- Any direct competition commentary from the call
- Management's view on competitors (cite specifics)
- Peers NOT mentioned but relevant (list with rationale)
- Growth outlook comparison

---

### SECTION 7: LONG-TERM STRATEGY

- Stated 3-5 year vision (cite management's words)
- Does THIS quarter's execution align with the vision?
- Strategic optionality: what options is management building or foreclosing?
- Investing for future vs managing the present: assessment with evidence
- Key strategic bets:

| Bet | Risk/Reward | Timeline |
|-----|-----------|----------|

---

### SECTION 8: ANALYST Q&A

#### 8A. Every Question & Response

For EACH question asked during Q&A:

**Q[#]: [Analyst Name, Firm]**
> Question: [verbatim or close paraphrase]

**Management Response:**
[Detailed response — not summarized]

**Evasion Flag:** Yes/No
**If evaded, what was avoided:** [explanation]

---

Repeat for ALL questions.

#### 8B. Recurring Themes
List topics that multiple analysts asked about — these signal market concerns.

#### 8C. Dodged / Partial Answers

| Question | What Was Incomplete | Potential Reason | Implication |
|----------|-------------------|-----------------|-------------|

#### 8D. Suggested Follow-Up Questions
Questions the fund manager should ask in future interactions.

#### 8E. Margin Analysis from Q&A
Deep commentary on any margin-specific Q&A exchanges.

---

### SECTION 9: QUANTITATIVE DATA TABLE

Every number mentioned in the call:

| # | Data Point | Value | Context | Source (Prepared/Q&A) | Significance |
|---|-----------|-------|---------|---------------------|-------------|

---

### SECTION 10: KEY INSIGHTS TABLE

| # | Key Insight | Impact (Positive/Negative/Neutral) | Evidence from Call |
|---|------------|-----------------------------------|-------------------|

---

### SECTION 11: CONNECTING THE DOTS

Write this as an **analyst's investment note** — synthesize the FULL narrative:
- How does margin guidance connect to capex plans?
- Does competitive commentary align with pricing strategy?
- Are growth targets achievable given industry environment?
- Is management tone consistent with the numbers?
- What story is management telling, and does evidence support it?
- Cross-reference: any contradictions between different parts of the call?

---

### SECTION 12: ANALYSTS ON CALL

| # | Analyst Name | Firm |
|---|-------------|------|

---

## ═══════════════════════════════════════════
## PART B: SCREENER.IN DEEP FINANCIAL ANALYSIS
## ═══════════════════════════════════════════

Use data from `/tmp/screener_data.json` (saved from MCP screener tool response in Step 2).

The MCP response contains these top-level keys: `ratios`, `financial_tables`, `analysis`, `key_points`.
Within `financial_tables`, the sub-keys are: `"Quarterly Results"`, `"Profit & Loss"`, `"Balance Sheet"`, `"Cash Flows"`, `"Ratios"`, `"Shareholding Pattern"`.

Each table has `columns` (array of period labels) and `data` (array of rows, where row[0] is the label and remaining values correspond to the columns).

**Computed metrics** like cagr_analysis, margin_analysis, working_capital, debt_structure, fcf_analysis, equity_dilution, and growth_metrics must be **calculated from the raw table data** during analysis. They are NOT pre-computed in the MCP response.

---

### SECTION 13: VALUATION & KEY METRICS (Screener Section 1)

#### 13A. Key Metrics Table

| Metric | Value |
|--------|-------|
| Market Cap | ₹X Cr |
| Enterprise Value | ₹X Cr |
| Current Price | ₹X |
| Revenue (TTM) | ₹X Cr |
| Net Profit (TTM) | ₹X Cr |
| P/E (TTM) | Xx |
| P/B | Xx |
| P/S | Xx |
| EV/EBITDA | Xx |
| ROCE | X% |
| ROE | X% |
| Debt/Equity | X |
| EPS (TTM) | ₹X |
| Net Debt | ₹X Cr |
| Promoter Holding | X% |
| FII Holding | X% |
| DII Holding | X% |
| Pledge % | X% |

#### 13B. Valuation Analysis
- **Is valuation justified by return ratios?** ROCE vs P/E analysis, P/B vs ROE (fair P/B ≈ ROE / Cost of equity)
- **EV vs Net Debt positioning:** Net debt as % of EV — above 40% signals leverage risk
- **Is P/B aligned with ROE?** DuPont check: ROE = PAT/Rev × Rev/Assets × Assets/Equity. If ROE high due to leverage, P/B premium is fragile.
- **Is leverage artificially boosting ROE?** Compare ROCE vs ROE. If ROE >> ROCE, leverage is the driver.

| Verdict | Classification | Justification |
|---------|---------------|---------------|
| Valuation | Cheap / Fair / Expensive / Frothy | [reason] |
| ROE Quality | Leverage-driven / Operationally earned | |
| Margin of Safety | High / Moderate / None | |


---

### SECTION 14: QUARTERLY RESULTS (Screener Section 2)

#### 14A. Full Quarterly Table (last 8 quarters)

| Quarter | Revenue (Cr) | QoQ% | YoY% | EBITDA (Cr) | OPM% | PAT (Cr) | NPM% | EPS | Tax% | Other Inc |
|---------|-------------|------|------|------------|------|---------|------|-----|------|-----------|

#### 14B. Trend Analysis
- QoQ revenue: accelerating / stable / decelerating?
- YoY revenue: sustained growth or base effect?
- OPM trend over last 8 quarters: expanding / compressing / volatile?
- NPM divergence from OPM: if NPM falling faster → finance costs or tax rate
- EPS trend: if EPS growth < Revenue growth → dilution or margin compression
- Tax rate anomalies: sudden drops = deferred tax or MAT credit (one-time)
- Other income dependency: Other income as % of PAT. If >20%, PAT quality is weak.

#### 14C. Diagnostics
- Margin compression drivers (RM inflation, employee cost, operating deleverage, finance costs, pricing power loss)
- Revenue quality: is revenue real (CFO tracks it) or accrual-inflated (rising receivables)?
- Operating leverage: positively leveraged or fixed-cost drag?
- Slowdown signal: QoQ deceleration for 2+ quarters?


---

### SECTION 15: ANNUAL P&L (Screener Section 3)

#### 15A. Full Historical P&L Table

| Year | Revenue | EBITDA | EBITDA% | PAT | PAT% | EPS | Rev YoY% | PAT YoY% |
|------|---------|--------|---------|-----|------|-----|----------|---------|

#### 15B. CAGR Analysis

| Metric | 3Y CAGR | 5Y CAGR | 10Y CAGR |
|--------|---------|---------|---------|
| Revenue | X% | X% | X% |
| EBITDA | X% | X% | X% |
| PAT | X% | X% | X% |

Interpretation: PAT CAGR > Revenue CAGR → margin expansion. PAT CAGR < Revenue CAGR → compression.

#### 15C. Margin Stability
Peak OPM vs trough OPM. Classify: Expanding / Stable / Compressing / Volatile.

#### 15D. Peak vs Trough Earnings
Identify peak and trough. Current level vs previous peak. Cyclical companies revert; compounders set new peaks.

#### 15E. Forensic Checks

| Item | Value | Signal |
|------|-------|--------|
| Exceptional Items | | One-time or recurring? |
| Impairment Charges | | Asset quality concern |
| Other Income spikes | | Timing manipulation? |
| Provision Reversals | | Found / Not found |
| Capitalized Expenses | | Revenue expenses hidden? |

---

### SECTION 16: BALANCE SHEET — STRENGTH & ASSET QUALITY AUDIT (Screener Section 4)

#### 16A. Balance Sheet Strength

| Metric | Value | Assessment |
|--------|-------|-----------|
| Net Worth | ₹X Cr | |
| Total Debt | ₹X Cr | |
| Net Debt | ₹X Cr | |
| Cash & Equiv | ₹X Cr | |
| D/E Ratio | X | |
| Interest Coverage | X | |
| Current Ratio | X | |
| Quick Ratio | X | |

**Classification:** Very Strong / Stable / Moderately Leveraged / Aggressive / Financially Weak

#### 16B. Inventory Forensic Analysis

| Year | Revenue | Inventory | Inv as % Rev | Inv Days | OPM% | Signal |
|------|---------|-----------|-------------|---------|------|--------|

Inventory Risk Signals checklist:
- Inventory growing faster than revenue? Y/N
- Margin compression + inventory increase? Y/N
- Negative CFO + rising inventory? Y/N
- Declining inventory turnover? Y/N
- High CWIP not converting? Y/N

**Conclude:** Productive / Excess but manageable / Risk of write-down / Hidden loss probable

#### 16C. Working Capital Deep Check

| Metric | Year-4 | Year-3 | Year-2 | Year-1 | Current | Trend |
|--------|--------|--------|--------|--------|---------|-------|
| Receivable Days | | | | | | |
| Inventory Days | | | | | | |
| Payable Days | | | | | | |
| Cash Conversion Cycle | | | | | | |

Flag: Working capital stress, cash trapped in receivables, aggressive revenue recognition.

#### 16D. Debt Structure & Risk

| Metric | FY-4 | FY-3 | FY-2 | FY-1 | Latest |
|--------|------|------|------|------|--------|
| Short-term Debt | | | | | |
| Long-term Debt | | | | | |
| Total Borrowings | | | | | |
| Net Debt | | | | | |
| Interest Coverage | | | | | |

Analysis: ST debt > 50% = refinancing risk. Net debt/EBITDA: <1x comfortable, 1-3x manageable, >3x high, >5x distressed.

#### 16E. Equity Dilution Analysis

| Year | Equity Capital | Reserves | Net Worth | Equity CAGR |
|------|---------------|----------|-----------|------------|

Is EPS growth real or diluted? Growth funded internally or via dilution or via debt?

---

### SECTION 17: CASH FLOW — CAPITAL DISCIPLINE AUDIT (Screener Section 5)

#### 17A. Full Cash Flow Table

| Year | CFO | Capex | FCF | CFI | CFF | CFO/PAT | CFO/EBITDA |
|------|-----|-------|-----|-----|-----|---------|-----------|

#### 17B. Operating Cash Flow Analysis
- CFO/PAT trend — consistently <0.8 = profits not converting to cash
- CFO stagnant while PAT grows → investigate receivables/inventory

#### 17C. Investing Cash Flow
- Capex intensity (Capex/Revenue %)
- Growth capex vs maintenance (depreciation ≈ maintenance)
- CWIP not converting to revenue?

#### 17D. Financing Cash Flow
- Net borrower or net repayer?
- Dividend sustainability: DPS growing? FCF supports?
- Buyback activity?

#### 17E. Free Cash Flow

| Metric | Value |
|--------|-------|
| FCF (latest) | ₹X Cr |
| FCF (5Y avg) | ₹X Cr |
| FCF Yield | X% |
| FCF Margin | X% |
| Self-funded? | [assessment] |


---

### SECTION 18: RETURN & CAPITAL EFFICIENCY (Screener Section 6)

| Metric | FY-4 | FY-3 | FY-2 | FY-1 | Latest | Trend |
|--------|------|------|------|------|--------|-------|
| ROCE | | | | | | |
| ROE | | | | | | |
| ROA | | | | | | |
| Asset Turnover | | | | | | |

Diagnoses:
- ROCE declining during capex → normal if capex-related; structural if capex stagnant
- Return spread = ROCE − Cost of Capital (assume ~10-12%)
- Capital productivity: Asset turnover × EBITDA margin


---

### SECTION 19: MARGIN & COST STRUCTURE (Screener Section 7)

| Year | GPM% | OPM% | NPM% | RM% | Employee% | Finance% |
|------|------|------|------|-----|----------|---------|

Analysis:
- Pricing power: GPM stable despite RM inflation?
- OPM: structural compression or cyclical?
- NPM divergence from OPM: finance cost or D&A or tax normalization?
- Cost pressure identification

---

### SECTION 20: OWNERSHIP & SMART MONEY (Screener Section 8)

| Quarter | Promoter% | Pledge% | FII% | DII% | Public% |
|---------|-----------|---------|------|------|---------|

Interpretation:
- Promoter buying → confidence. Selling → investigate.
- Pledge rising → RED FLAG.
- FII + DII both rising → accumulation phase (strong positive)
- Both falling → distribution phase (investigate urgently)


---

### SECTION 21: EARNINGS QUALITY & MANIPULATION DETECTION (Screener Section 9)

| Red Flag | Present? | Magnitude | Severity |
|----------|---------|-----------|---------|
| Large receivable growth (> rev growth) | | | |
| Inventory buildup before weak quarter | | | |
| Exceptional income inflation | | | |
| Capitalized expenses (CWIP not converting) | | | |
| Goodwill buildup | | | |
| Related party concentration | | | |
| Provision manipulation | | | |
| CFO/PAT < 0.7 consistently | | | |
| Other income > 20% of PAT | | | |
| D&A surprisingly low vs asset base | | | |

**Earnings Quality Rating: HIGH / MODERATE / WEAK** (with justification)

---

## ═══════════════════════════════════════════
## PART C: FINANCIAL MODEL & VALUATION
## ═══════════════════════════════════════════

---

### SECTION 22: 3-SCENARIO FINANCIAL MODEL

**CRITICAL:** Use the LATEST ACTUAL financials from screener_data.json as the BASE YEAR. All projections must flow from actual current numbers, not assumptions in isolation. The model must be internally consistent — Balance Sheet must balance, Cash Flow must reconcile with P&L and BS changes.

#### 22A. Current Financial Base (from Screener Data)

First, establish the base year (latest annual) from which projections start:

| Base Year Item | Latest FY Value (₹ Cr) | Source |
|----------------|----------------------|--------|
| Revenue | | screener P&L |
| COGS / Material Cost | | screener P&L |
| Gross Profit | | calculated |
| Employee Cost | | screener P&L |
| Other Operating Expenses | | screener P&L |
| EBITDA | | calculated |
| Depreciation & Amortization | | screener P&L |
| EBIT | | calculated |
| Interest / Finance Cost | | screener P&L |
| Other Income | | screener P&L |
| PBT | | calculated |
| Tax | | screener P&L |
| Tax Rate (Effective %) | | calculated |
| PAT | | screener P&L |
| EPS | | screener data |
| Gross Block (Fixed Assets) | | screener BS |
| Net Fixed Assets | | screener BS |
| CWIP | | screener BS |
| Total Debt (ST + LT) | | screener BS |
| Cash & Equivalents | | screener BS |
| Net Debt | | calculated |
| Inventory | | screener BS |
| Trade Receivables | | screener BS |
| Trade Payables | | screener BS |
| Total Equity / Net Worth | | screener BS |
| Shares Outstanding (Cr) | | screener data |
| Current Share Price | | screener data |

#### 22B. Model Assumptions (Bear / Normal / Bull)

For EACH line item, tie rationale to transcript guidance + historical trends + current base:

| Line Item | Bear (Value + Rationale) | Normal (Value + Rationale) | Bull (Value + Rationale) |
|-----------|------------------------|--------------------------|------------------------|
| Revenue Growth % (each year) | | | |
| Gross Margin % | | | |
| Employee Cost % of Revenue | | | |
| Other Opex % of Revenue | | | |
| EBITDA Margin % | | | |
| **Depreciation Schedule** | | | |
| → Depn Rate % of Gross Block | | | |
| → Gross Block growth (new capex additions) | | | |
| **Debt & Interest Schedule** | | | |
| → New Borrowings / Repayments per year | | | |
| → Avg Interest Rate on Debt | | | |
| → Interest Cost = Avg Debt × Rate | | | |
| **Tax Assumptions** | | | |
| → Effective Tax Rate % | | | |
| → MAT credit / Deferred tax adjustments | | | |
| → New tax regime impact (if applicable) | | | |
| **Capex Plan** | | | |
| → Maintenance Capex (≈ Depreciation) | | | |
| → Growth Capex (from guidance/expansion plans) | | | |
| → Total Capex (Cr) per year | | | |
| → CWIP conversion timeline | | | |
| **Working Capital Assumptions** | | | |
| → Receivable Days | | | |
| → Inventory Days | | | |
| → Payable Days | | | |
| → Cash Conversion Cycle | | | |
| Other Income Growth % | | | |
| Dividend Payout % | | | |

#### 22C. Projected P&L (FY+1E, FY+2E, FY+3E × 3 scenarios)

For EACH scenario, build the FULL P&L from base year:

| Line Item | Base FY (Actual) | FY+1E | FY+2E | FY+3E |
|-----------|-----------------|-------|-------|-------|
| Revenue | | | | |
| COGS / Material Cost | | | | |
| **Gross Profit** | | | | |
| Gross Margin % | | | | |
| Employee Cost | | | | |
| Other Operating Expenses | | | | |
| **EBITDA** | | | | |
| EBITDA Margin % | | | | |
| Depreciation (from schedule) | | | | |
| **EBIT** | | | | |
| Interest Cost (from debt schedule) | | | | |
| Other Income | | | | |
| **PBT** | | | | |
| Tax (at effective rate) | | | | |
| **PAT** | | | | |
| PAT Margin % | | | | |
| EPS | | | | |

Show all 3 scenario tables (Bear, Normal, Bull) separately.

#### 22D. Debt & Depreciation Schedule (3Y × 3 scenarios)

**Debt Schedule:**

| Item | Base FY | FY+1E | FY+2E | FY+3E |
|------|---------|-------|-------|-------|
| Opening Debt | | | | |
| + New Borrowings | | | | |
| − Repayments | | | | |
| **Closing Debt** | | | | |
| Average Debt | | | | |
| Interest Rate % | | | | |
| **Interest Cost** | | | | |
| Net Debt | | | | |
| Net Debt/EBITDA | | | | |
| Interest Coverage (EBIT/Interest) | | | | |

**Depreciation Schedule:**

| Item | Base FY | FY+1E | FY+2E | FY+3E |
|------|---------|-------|-------|-------|
| Opening Gross Block | | | | |
| + Capex Additions | | | | |
| + CWIP Capitalized | | | | |
| **Closing Gross Block** | | | | |
| Depreciation Rate % | | | | |
| **Depreciation Charge** | | | | |
| Accumulated Depreciation | | | | |
| **Net Fixed Assets** | | | | |
| Closing CWIP | | | | |

#### 22E. Projected Balance Sheet (3Y × 3 scenarios — key items)

| Item | Base FY | FY+1E | FY+2E | FY+3E |
|------|---------|-------|-------|-------|
| Net Fixed Assets | | | | |
| CWIP | | | | |
| Inventory | | | | |
| Trade Receivables | | | | |
| Cash & Equivalents | | | | |
| Other Current Assets | | | | |
| **Total Assets** | | | | |
| Equity Capital | | | | |
| Reserves & Surplus | | | | |
| **Net Worth** | | | | |
| Long-term Debt | | | | |
| Short-term Debt | | | | |
| Trade Payables | | | | |
| Other Liabilities | | | | |
| **Total Liabilities** | | | | |
| **BS Balance Check** | ✓/✗ | ✓/✗ | ✓/✗ | ✓/✗ |
| D/E Ratio | | | | |
| Current Ratio | | | | |

#### 22F. Projected Cash Flow (3Y × 3 scenarios)

| Item | Base FY | FY+1E | FY+2E | FY+3E |
|------|---------|-------|-------|-------|
| PAT | | | | |
| + Depreciation & Amortization | | | | |
| + Interest (add back) | | | | |
| − Tax paid (adjust for deferred) | | | | |
| ± Working Capital Change | | | | |
| → Change in Receivables | | | | |
| → Change in Inventory | | | | |
| → Change in Payables | | | | |
| **Operating Cash Flow (CFO)** | | | | |
| − Capex (PP&E + Intangibles) | | | | |
| − Other Investments | | | | |
| **Investing Cash Flow (CFI)** | | | | |
| + New Borrowings | | | | |
| − Debt Repayments | | | | |
| − Interest Paid | | | | |
| − Dividends Paid | | | | |
| **Financing Cash Flow (CFF)** | | | | |
| **Free Cash Flow (CFO − Capex)** | | | | |
| **Net Cash Change** | | | | |
| Closing Cash | | | | |
| CFO/PAT Ratio | | | | |
| FCF Yield % | | | | |

#### 22G. Model Consistency Checks

Verify these cross-checks for each scenario:

| Check | Pass/Fail | Notes |
|-------|-----------|-------|
| BS balances (Assets = Liabilities + Equity) | | |
| Closing Cash = Opening + Net Cash Change | | |
| Debt schedule ties to BS debt | | |
| Depreciation schedule ties to P&L and BS | | |
| WC changes tie to BS movements | | |
| Interest cost ties to debt schedule | | |
| Tax paid reasonable vs P&L tax | | |
| Capex ties to BS fixed asset changes | | |

---

### SECTION 23: VALUATION SCENARIOS

For EACH scenario (Bear / Normal / Bull):

| Method | Multiple/Rate | Metric | Target Price | Upside/Downside from CMP |
|--------|-------------|--------|-------------|------------------------|
| PE-based | Target PE: X | EPS: ₹X | ₹X | X% |
| EV/EBITDA | Multiple: X | EBITDA: ₹X Cr | ₹X | X% |
| DCF | WACC: X%, Terminal: X% | Equity/share: ₹X | ₹X | X% |


---

### SECTION 24: SENSITIVITY ANALYSIS

| Variable | Base | -10% Impact on PAT | -5% | +5% | +10% | Impact on Valuation |
|----------|------|-------------------|-----|-----|------|-------------------|

### SECTION 25: MODEL RISKS

| Risk | Impact on Model | Which Scenario Breaks | Probability |
|------|----------------|---------------------|------------|

---

## ═══════════════════════════════════════════
## PART D: FINAL INVESTMENT REPORT
## ═══════════════════════════════════════════

---

### SECTION 26: STRUCTURED SUMMARY

| # | Dimension | Assessment | Key Evidence |
|---|-----------|-----------|-------------|
| 1 | Recent Quarter Quality | [verdict] | [data] |
| 2 | Balance Sheet Strength | [Very Strong/Stable/Moderate/Aggressive/Weak] | D/E, IC |
| 3 | Inventory Risk & Loss | [Productive/Excess/Risk/Probable Loss] | Inv days |
| 4 | Working Capital Health | [Healthy/Stressed/Trapped] | CCC days |
| 5 | Debt & Liquidity Risk | [Low/Moderate/High/Critical] | Net debt/EBITDA |
| 6 | Equity Dilution Impact | [Minimal/Moderate/Significant] | EPS vs Rev CAGR |
| 7 | Capital Allocation Discipline | [Excellent/Good/Average/Poor] | ROCE vs capex |
| 8 | Cash Flow Sustainability | [Strong/Adequate/Weak] | FCF yield |
| 9 | Margin Durability | [Expanding/Stable/Compressing/Volatile] | OPM trend |
| 10 | Institutional Positioning | [Accumulating/Neutral/Distributing] | FII/DII trend |
| 11 | Earnings Quality Rating | [High/Moderate/Weak] | CFO/PAT |
| 12 | Overall Classification | [see below] | |

---

### SECTION 27: OVERALL INVESTMENT CLASSIFICATION

Classify as ONE of:

| Classification | Criteria |
|---------------|---------|
| Capital Efficient Compounder | ROCE >20%, FCF+, low debt, margin expanding, strong earnings |
| Capex Heavy Expansion Story | High reinvestment, ROCE temporarily depressed, clear capacity rationale |
| Cyclical Operator | ROCE highly variable, margins sensitive to commodity/demand cycle |
| Financially Leveraged Risk | D/E >2, IC tight, FCF negative, balance sheet stress |
| Value Trap Candidate | Cheap multiples but ROCE declining, no catalyst, structural issues |
| High Quality Long-Term Wealth Creator | Consistent ROCE >15%, FCF+, earnings quality high, moat visible |
| Overvalued Momentum Play | P/E >50x, limited fundamental support, priced for perfection |

**Classification: [CHOOSE ONE]**

**Investment Rationale (3-4 sentences):** Synthesize key drivers, risks, and what would change your view.

---

### SECTION 28: EXPERT PANEL VERDICT

Synthesize as if 5 experts are giving their top insight + top concern + confidence (1-10):

| Expert | Top Insight | Top Concern | Confidence (1-10) |
|--------|-----------|------------|-------------------|
| Fundamental Analyst | | | |
| Industry Specialist | | | |
| Risk Analyst | | | |
| Behavioural Analyst | | | |
| Guidance & Strategy Analyst | | | |

**Consensus View:** [2-3 sentence synthesis of all expert views]

---

## RULES

1. **Be factual and comprehensive** — every claim must trace to transcript or financial data
2. **Section 3 (Industry/Company Deep-Dive) is FULL depth** — multiple paragraphs per topic, NOT bullet summaries
3. **Section 5 (Risk Assessment) is CRITICAL** — deep analysis with evidence for each risk
4. **Section 8 (Q&A) covers ALL questions** — no skipping
5. **All tables must have ACTUAL data** — no placeholders in final output. Do NOT output any HTML or Chart.js code.
6. **Financial model must have ALL 3 scenarios** with rationale tied to guidance
7. **Screener sections use real screener_data.json values** — no invented numbers
8. **Output everything sequentially in chat** — no separate files
9. **If screener data unavailable**, clearly mark sections as "Data Not Available" and proceed with transcript-only analysis
10. **Prioritize speed** — output sections as you complete them, don't wait for everything
