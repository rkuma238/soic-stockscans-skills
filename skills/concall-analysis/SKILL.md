---
name: concall-analysis
description: Comprehensive conference call transcript analysis with a multi-expert panel framework. Use this skill whenever the user uploads or pastes a conference call transcript, earnings call transcript, investor call, analyst day transcript, or quarterly results discussion. Also trigger when the user says "analyze this concall", "earnings call analysis", "conference call review", "transcript analysis", or any variation involving analysis of management commentary from public company calls. This skill produces an institutional-grade, fund-manager-ready PDF report with embedded interactive HTML charts and visualizations. Always use this skill for any concall/earnings transcript analysis — it dramatically improves output quality.
---

# Conference Call Analysis — Parallel Multi-Agent Pipeline

You are a senior research team analyzing a conference call for a fund manager who holds this stock in portfolio.
The pipeline runs **4 parallel agents**, then assembles a **PDF report** with **static HTML chart files** at key sections.

## Phase 0: Setup & Data Gathering (Parallel)

Run these **2-3 tasks simultaneously** using the `Task` tool with `subagent_type: "general-purpose"`:

### Task A — Extract Transcript
```
prompt: |
  Extract the full transcript from the uploaded PDF.
  1. pip install pdfplumber --break-system-packages -q
  2. Read every page of: {uploaded_pdf_path}
  3. Write full text to /tmp/concall_transcript.txt
  4. Write /tmp/company_info.json with: company_name, quarter, date, ticker
```

### Task B — Fetch Financial Data from Screener (Python — token efficient)
```
prompt: |
  Fetch financial data for {company_name} from Screener.in.
  1. pip install requests beautifulsoup4 --break-system-packages -q
  2. Copy scripts/screener_client.py from skill directory to /tmp/
  3. Run: python3 /tmp/screener_client.py complete {TICKER} > /tmp/screener_financials.json

  If Python client fails (proxy block), fall back to Chrome browser:
  - Navigate to https://www.screener.in/company/{TICKER}/consolidated/
  - Use get_page_text to extract all data
  - Parse and save as JSON to /tmp/screener_financials.json

  JSON must contain: key_metrics, quarterly_results, annual_data,
  balance_sheet, cash_flow, ratios, growth_metrics, shareholding_pattern.
```

### Task C — Download Concall PDF (only if user didn't upload one)
```
prompt: |
  Download latest concall transcript for {company_name} from Screener.in.
  Use Chrome browser to navigate, find document links, download PDF to /tmp/concall_latest.pdf.
```

**Wait for all Phase 0 tasks to complete before Phase 1.**

---

## Phase 1: Parallel Analysis (4 Agents)

Launch **4 agents simultaneously** using `Task` tool with `subagent_type: "general-purpose"`.
Each agent reads `/tmp/concall_transcript.txt` and `/tmp/screener_financials.json`.
Each agent writes its output as a JSON file.

---

### Agent 1 — TRANSCRIPT DEEP-DIVE ANALYST

**Output:** `/tmp/agent1_transcript.json`

Analyze the transcript exhaustively. Produce JSON with:

**a) executive_summary**
- overall_performance: paragraph on headline numbers (revenue, EBITDA, PAT, margins) vs expectations
- key_topics: list of 3-5 most important themes
- management_tone: evidence-based assessment (confident/cautious/defensive/evasive) with specific language patterns cited

**b) detailed_analysis**
- business_model_evolution: changes in revenue mix, pricing, cost structure, working capital, competitive positioning. Explain WHY changes matter for margins, predictability, valuation.
- industry_operating_environment: cycle position, regulatory changes, tech disruptions, supply chain, input costs. Connect to company's specific situation.
- management_tone_sentiment: confidence markers vs hedging language, evasion signals, tone shifts between prepared remarks and Q&A, what's NOT being said.
- key_business_insights: [{insight, evidence_quote_or_data, significance_high_med_low, investment_implication}] — minimum 5-10 insights
- qualitative_quantitative_guidance: separate hard guidance (specific numbers) from soft guidance (directional). Table: [{metric, guidance, type_hard_soft, confidence, prior_guidance, change}]
- kpis: [{kpi_name, current_value, yoy_change, qoq_change, trend, management_explanation, what_changes_trajectory}]
- capital_allocation: capex plans (maintenance vs growth), M&A appetite, debt management, dividends, R&D, working capital optimization. Assess alignment with strategy.

**c) industry_company_deep_dive**
This is NOT a summary. Provide FULL IN-DEPTH explanation of every industry and company topic discussed:
- industry_insights: {market_trends, competitive_landscape, regulatory_policy_changes, economic_geopolitical_factors, supply_chain_dynamics}. Each must be multiple paragraphs with specifics.
- company_insights: {operational_challenges_opportunities, strategic_priorities, customer_demand_trends, order_flow_updates}. Full explanation, not bullets.
- management_thought_process: how management connects industry dynamics to company strategy
- interesting_revelations: [{revelation, why_its_interesting, investment_implication}] — flag anything particularly insightful

**d) analyst_qa**
For EVERY question asked:
- questions: [{analyst_name, firm, question_verbatim_or_close, management_response_detailed, evasion_flag_yes_no, if_evaded_what_was_avoided}]
- recurring_themes: list of topics multiple analysts asked about (signals market concerns)
- dodged_partial_answers: [{question, what_was_incomplete, potential_reason, implication}]
- suggested_followups: list of questions fund manager should ask
- margin_analysis_from_qa: any margin-specific Q&A with deep commentary

**e) analysts_on_call
- analysts: [{name, firm}] — every analyst who asked a question

---

### Agent 2 — FORENSIC & RISK ANALYST

**Output:** `/tmp/agent2_forensic.json`

**a) earnings_quality** (score /10)
- cash_conversion_ratio: OCF/PAT — flag if < 0.7
- accrual_quality: compare reported vs cash profit
- receivables_vs_revenue_growth: flag divergence
- inventory_flags: unusual buildup
- related_party_flags: transactions mentioned
- revenue_recognition_changes: any policy shifts
- score: 1-10 with detailed explanation

**b) management_credibility** (score /10)
- past_guidance_vs_actual: [{promised, delivered, gap_pct, verdict}]
- language_analysis: {hedging_words_count, assertive_count, evasion_count, examples}
- specific_evasions: [{question, how_evaded, significance}]
- tone_shifts: [{section, tone_before, tone_after, trigger}]
- credibility_score: 1-10

**c) red_flag_scanner**
- flags: [{flag_name, severity_1_10, evidence, implication, action_required}]
  Mandatory checks: revenue recognition, unusual margins, debt covenants, promoter pledges, auditor changes, related-party spikes, capex overruns, working capital bloat, tax anomalies, recurring "one-time" items, inventory write-downs, contingent liabilities

**d) risk_assessment** (CRITICAL SECTION — go deep)
For each risk provide: description, evidence from call, probability (H/M/L), impact (H/M/L), mitigants mentioned, our assessment of mitigant adequacy.
- competitive_threats: specific competitors, market share dynamics
- regulatory_challenges: specific regulations, timelines, impact
- technology_disruption: AI, automation, platform shifts
- execution_risks: management bandwidth, integration, project delays, cost overruns
- market_specific_risks: demand cycles, input costs, currency, geopolitical
- financial_risks: leverage, liquidity, covenant, customer concentration

**e) governance_assessment** (score /10)

---

### Agent 3 — GUIDANCE, STRATEGY & PEER ANALYST

**Output:** `/tmp/agent3_guidance.json`

**a) forward_looking_guidance**
- revenue_expectations: specific growth targets, organic vs inorganic, segment breakdown, key assumptions
- margin_expectations: gross/EBITDA/EBIT/PAT margin trajectory, drivers of expansion/compression, one-time items
- growth_drivers: [{driver, type_organic_inorganic, timeline, probability, revenue_impact}] ranked by importance
- pat_guidance: absolute targets, growth rates, tax rate assumptions, below-line items
- quantitative_guidance_table: [{metric, current_value, forward_guidance, timeline, confidence}] — every forward-looking number
- recovery_growth_expectations: {expected_timing, confidence_level, contributing_factors, what_must_go_right, what_could_go_wrong}

**b) peer_comparison**
- performance_comparison: [{peer, metric, our_value, peer_value, advantage_or_disadvantage}]
- growth_outlook_comparison: any commentary on peers
- competition_mentions: [{competitor, context, management_view}]
- peers_not_mentioned_but_relevant: list with rationale

**c) long_term_strategy**
- stated_vision_3_5_years: paragraph
- alignment_with_current_actions: does this quarter's execution match the vision?
- strategic_optionality: what options is management building or foreclosing?
- investing_for_future_vs_managing_present: assessment with evidence
- key_strategic_bets: [{bet, risk_reward, timeline}]

**d) connecting_the_dots**
Synthesize the FULL narrative — this reads like an analyst's investment note:
- How margin guidance connects to capex plans
- Does competitive commentary align with pricing strategy?
- Are growth targets achievable given industry environment?
- Is management tone consistent with numbers?
- What story is management telling, and does evidence support it?
- Cross-reference: any contradictions between different parts of the call

---

### Agent 4 — FINANCIAL MODELLING ANALYST

**Output:** `/tmp/agent4_modelling.json`

**Build a full 3-scenario financial model. THIS IS THE MOST DETAILED AGENT.**

**a) assumptions**
For EACH line item, provide Bear / Normal / Bull with rationale tied to transcript guidance + historical trends:
```json
[
  {"line_item": "Revenue Growth %", "bear": {"value": "X%", "rationale": "..."}, "normal": {...}, "bull": {...}},
  {"line_item": "EBITDA Margin %", ...},
  {"line_item": "Depreciation as % of Gross Block", ...},
  {"line_item": "Interest Rate on Debt %", ...},
  {"line_item": "Tax Rate %", ...},
  {"line_item": "Capex (Cr or % of Revenue)", ...},
  {"line_item": "Receivable Days", ...},
  {"line_item": "Inventory Days", ...},
  {"line_item": "Payable Days", ...},
  {"line_item": "Debt Repayment / New Borrowing", ...},
  {"line_item": "Other Income Growth %", ...},
  {"line_item": "Employee Cost Growth %", ...}
]
```

**b) projected_pl** (FY27E, FY28E, FY29E × 3 scenarios)
Each year: revenue, cogs, gross_profit, employee_cost, other_expenses, ebitda, depreciation, ebit, interest, other_income, pbt, tax, pat, eps

**c) projected_balance_sheet** (3 years × 3 scenarios)
net_fixed_assets, cwip, inventory, receivables, cash, total_assets, equity, reserves, long_term_debt, short_term_debt, payables, total_liabilities, debt_equity, current_ratio

**d) projected_cash_flow** (3 years × 3 scenarios)
pat, depreciation, working_capital_change, operating_cf, capex, acquisitions, investing_cf, borrowings, repayments, dividends, financing_cf, free_cash_flow, net_cash_change

**e) valuation_scenarios**
Per scenario: PE-based {target_pe, eps, target_price}, EV/EBITDA {multiple, ebitda, ev, equity_value, per_share}, DCF {wacc, terminal_growth, equity_value_per_share}, upside_downside_from_cmp

**f) sensitivity_analysis**
[{variable, base_value, minus_10pct_impact_on_pat, minus_5pct, plus_5pct, plus_10pct, impact_on_valuation}]

**g) model_risks**
[{risk, impact_on_model, which_scenario_breaks, probability}]

---

## Phase 2: Assemble Report

After all 4 agents complete, read all JSON outputs and build the report.

### Output Format: PDF + HTML Charts

The main report is a **reportlab PDF**. At key sections, also generate **standalone HTML chart files** using Chart.js that get referenced in the report. Save charts to the output folder alongside the PDF.

### Install
```bash
pip install reportlab --break-system-packages -q
```

### Report Sections (map to agent outputs)

Write `generate_report.py` in **2 PARTS** to avoid token limits:

**Part 1** — Imports, styles, cover, Sections 1-8:
| Section | Title | Agent Source |
|---------|-------|-------------|
| 1 | Executive Summary | Agent1.a + Agent2.b credibility |
| 2 | Detailed Analysis (Business Model, Industry, Tone, Insights, Guidance, KPIs, CapAlloc) | Agent1.b |
| 3 | Industry & Company Deep-Dive (FULL depth, not summary) | Agent1.c |
| 4 | Forward-Looking Statements & Guidance | Agent3.a |
| 5 | Risk Assessment (CRITICAL — deep with evidence) | Agent2.d |
| 6 | Peer Comparison | Agent3.b |
| 7 | Long-Term Strategy | Agent3.c |
| 8 | Analyst Q&A (every question + themes + dodged + followups + margin) | Agent1.d |

**Part 2** — Append via Edit tool, Sections 9-16 + build:
| Section | Title | Agent Source |
|---------|-------|-------------|
| 9 | Quantitative Data Table (every number from call) | Agent1.b (every_number) |
| 10 | Key Insights Table | Agent1.b (key_insights) |
| 11 | Connecting the Dots | Agent3.d |
| 12 | Analysts on Call | Agent1.e |
| 13 | Forensic Analysis (Earnings Quality + Red Flags + Credibility) | Agent2 full |
| 14 | Financial Model — Assumptions + Projections | Agent4.a-d |
| 15 | Valuation Scenarios + Sensitivity | Agent4.e-g |
| 16 | Expert Panel Verdict | Synthesize all 4 agents |

### HTML Charts to Generate

Create these as standalone `.html` files with Chart.js (CDN: https://cdn.jsdelivr.net/npm/chart.js):

1. **revenue_trend.html** — Bar+line chart: quarterly revenue + YoY growth %
2. **margin_trend.html** — Multi-line: EBITDA margin, PAT margin over quarters
3. **risk_matrix.html** — Scatter plot: probability vs impact for each risk
4. **scenario_valuation.html** — Grouped bar: Bear/Normal/Bull target prices (PE, EV/EBITDA, DCF)
5. **earnings_quality.html** — Radar chart: cash conversion, accruals, receivables quality, governance, credibility
6. **debt_trajectory.html** — Area chart: total debt, net debt over time
7. **shareholding.html** — Doughnut chart: promoter, FII, DII, public holdings

Each HTML file must be self-contained with embedded Chart.js via CDN.

### reportlab Cheat Sheet
```python
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor, white
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer,
    Table, TableStyle, PageBreak, HRFlowable)

P = HexColor("#1a365d"); A = HexColor("#2b6cb0")
G = HexColor("#4a5568"); BD = HexColor("#e2e8f0"); LT = HexColor("#f7fafc")
RED = HexColor("#e53e3e"); GRN = HexColor("#38a169"); YEL = HexColor("#d69e2e")

s = getSampleStyleSheet()
s.add(ParagraphStyle('H', parent=s['Heading1'], fontSize=16, textColor=P, spaceBefore=16, spaceAfter=8))
s.add(ParagraphStyle('SH', parent=s['Heading2'], fontSize=12, textColor=A, spaceBefore=10, spaceAfter=5))
s.add(ParagraphStyle('B', parent=s['Normal'], fontSize=10, leading=14, spaceAfter=6, alignment=TA_JUSTIFY))
s.add(ParagraphStyle('BL', parent=s['Normal'], fontSize=10, leading=13, leftIndent=18, bulletIndent=6, spaceAfter=3))
s.add(ParagraphStyle('Q', parent=s['Normal'], fontSize=10, leading=13, textColor=G, leftIndent=14, fontName='Helvetica-Oblique'))
s.add(ParagraphStyle('TH', parent=s['Normal'], fontSize=9, textColor=white, fontName='Helvetica-Bold', alignment=TA_CENTER))
s.add(ParagraphStyle('TC', parent=s['Normal'], fontSize=9, leading=11))
s.add(ParagraphStyle('BEAR', parent=s['Normal'], fontSize=9, textColor=RED))
s.add(ParagraphStyle('BULL', parent=s['Normal'], fontSize=9, textColor=GRN))
s.add(ParagraphStyle('BASE', parent=s['Normal'], fontSize=9, textColor=YEL))

# Table helper
def make_table(headers, rows, col_widths=None):
    header_row = [Paragraph(h, s['TH']) for h in headers]
    data = [header_row] + [[Paragraph(str(c), s['TC']) for c in r] for r in rows]
    t = Table(data, colWidths=col_widths, repeatRows=1)
    t.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,0),P), ('TEXTCOLOR',(0,0),(-1,0),white),
        ('GRID',(0,0),(-1,-1),0.5,BD), ('ROWBACKGROUNDS',(0,1),(-1,-1),[white,LT]),
        ('VALIGN',(0,0),(-1,-1),'TOP'), ('TOPPADDING',(0,0),(-1,-1),6),
        ('BOTTOMPADDING',(0,0),(-1,-1),6),
    ]))
    return t

# Footer
def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont('Helvetica', 8); canvas.setFillColor(G)
    canvas.drawString(50, 20, f"{company_name} — {quarter} Concall Analysis")
    canvas.drawRightString(A4[0]-50, 20, f"Page {doc.page}")
    canvas.restoreState()

doc = SimpleDocTemplate(output_path, pagesize=A4,
    leftMargin=50, rightMargin=50, topMargin=50, bottomMargin=40)
doc.build(story, onFirstPage=footer, onLaterPages=footer)
```

---

## Rules

1. **Parallel execution is mandatory** — launch all independent agents simultaneously
2. **Be factual and comprehensive** — avoid assumptions or unsupported inferences
3. **Every claim must trace** to transcript text or financial data
4. **Section 3 (Industry/Company Deep-Dive) must be FULL depth** — not a summary. Multiple paragraphs per topic. Flag interesting/helpful insights explicitly.
5. **Section 5 (Risk Assessment) is CRITICAL** — deep analysis with supporting evidence for each risk
6. **Section 8 (Q&A) must cover ALL analyst questions** — no skipping. Include margin analysis from Q&A.
7. **Financial model must have ALL 3 scenarios** with detailed rationale per assumption tied to guidance
8. **Forensic section must flag specific red flags** with evidence and severity scores
9. **Generate 7 HTML chart files** alongside the PDF
10. **Write PDF script in 2 parts** to avoid token limits
11. **Save outputs** (PDF + HTML charts) to the user's output folder
12. **Expert Panel Verdict (Section 16)** must synthesize all agents: FA top insight + concern + confidence 1-10, IS same, RA same, BA same, GSA same, plus consensus view
