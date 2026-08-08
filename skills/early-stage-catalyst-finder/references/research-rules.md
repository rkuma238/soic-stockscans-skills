# Research Rules — Strict Compliance Required

These rules are NON-NEGOTIABLE. Any output that violates these rules must be revised before delivery.

---

## Rule 1: DATE EVERYTHING

Every catalyst, event, order win, or announcement MUST include a specific date or at minimum month+year.

REJECTED examples:
- "Recently won a large order"
- "The company announced expansion plans"
- "Management guided for strong growth"

ACCEPTED examples:
- "Won ₹450 Cr order from Adani Green on 22-Jan-2026"
- "Board approved ₹600 Cr capex on 15-Mar-2026 (BSE Filing)"
- "In the Q3 FY26 concall (held 28-Jan-2026), MD stated revenue target of ₹5,000 Cr by FY28"

If you cannot find a date for a claim, either:
- Search harder with different query terms, OR
- State: "Date not confirmed via available sources"

---

## Rule 2: NO STALE TRIGGERS

The trigger must be from the LAST 6 MONTHS relative to today's date.

- If the most recent identifiable catalyst is older than 6 months → classify as:
  "NO RECENT FUNDAMENTAL TRIGGER — Technical/Liquidity Setup Only"
- Do NOT stretch old news to make it seem current.
- If a Q2 concall mentioned a catalyst but nothing new has happened since, note:
  "Last known trigger from [date]. No recent update found."

---

## Rule 3: QUANTIFY OR DELETE

Every financial or business claim MUST have a number attached.

REJECTED:
- "Strong order book"
- "Improving margins"
- "Good revenue growth"
- "Healthy balance sheet"

ACCEPTED:
- "Order book of ₹3,200 Cr (up 42% YoY from ₹2,250 Cr)"
- "OPM improved from 12.3% in Q1 FY25 to 18.1% in Q3 FY26"
- "Revenue grew 28% YoY to ₹1,450 Cr in Q3 FY26"
- "Debt/Equity reduced from 0.8 to 0.3 over last 8 quarters"

---

## Rule 4: ANNOUNCED vs EXECUTED

Clearly label the status of any capex, expansion, or strategic initiative:

- **ANNOUNCED**: Board approval or management statement. No construction started.
- **UNDER CONSTRUCTION**: Capex sanctioned, land acquired, construction in progress. Cite expected commissioning date.
- **COMMISSIONED**: Plant/line operational. Cite when it went live.
- **RAMP-UP**: Operational but not at full utilization. Cite current vs target utilization.

Never conflate "planning" with "commissioned." Example:
- WRONG: "The company has expanded capacity to 50,000 MT"
- RIGHT: "Board approved 50,000 MT expansion (BSE filing 10-Dec-2025). Expected commissioning: Q2 FY27. Current capacity: 30,000 MT. [STATUS: UNDER CONSTRUCTION]"

---

## Rule 5: SKEPTICISM ON GENERIC NARRATIVES

These narratives are NOT triggers by themselves:
- "China+1 beneficiary"
- "PLI scheme beneficiary"
- "Import substitution play"
- "Digital India / Smart City beneficiary"
- "EV transition play"

To use ANY of these narratives, you MUST back them with at least ONE of:
- A specific order win from a named customer attributable to the trend
- A named customer addition (with date) due to the shift
- Actual PLI disbursement received (with ₹ amount and date)
- Measurable export revenue increase (with % and destination)

---

## Rule 6: CITE SOURCES

Every factual claim MUST have a source tag at the end:

Format: [Source: description]

Accepted sources:
- [Source: Q3 FY26 Concall Transcript]
- [Source: BSE Filing dated 14-Feb-2026]
- [Source: Screener.in]
- [Source: Company Investor Presentation, Jan 2026]
- [Source: Economic Times, 20-Mar-2026]
- [Source: MoneyControl, 15-Feb-2026]

Unaccepted:
- [Source: Internet] ← too vague
- [Source: Various] ← not a source
- No source tag at all

---

## Rule 7: ACKNOWLEDGE GAPS

If web search returns no meaningful recent news for a stock:

DO NOT:
- Invent a catalyst
- Rehash old news as if it's recent
- Fill the template with generic statements

DO:
- State clearly: "Limited recent newsflow — no specific fundamental trigger identified via web search"
- Still complete the Screener.in financial snapshot (this data is always available)
- Note if the technical breakout might be driven by liquidity, sector rotation, or index rebalancing
- Suggest what to monitor: "Watch for upcoming Q4 results / order announcements / capacity commissioning"

---

## Rule 8: WEB SEARCH STRATEGY

For each stock, run AT LEAST 4 distinct web searches before concluding "no data found":

1. "[Company Name] latest quarterly results"
2. "[Company Name] order win announcement [current year]"
3. "[Company Name] expansion capex news"
4. "[Company Name] [Sector] outlook"

If initial searches return nothing useful:
5. Try BSE/NSE specific: "[Company Name] BSE corporate announcement"
6. Try news sites: "[Company Name] site:economictimes.com OR site:moneycontrol.com"
7. Try the full company name (not just ticker) if ticker-based searches fail

---

## Rule 9: SCREENER DATA IS MANDATORY

Even if web search finds no news, the Screener.in financial snapshot section MUST be completed for every stock. Use MCP tools `mcp__screener__search_company` and `mcp__screener__get_company_data`.

If Screener MCP is unavailable, note: "[Screener.in data unavailable — MCP tool error]" and proceed with web-sourced financial data.

---

## Rule 10: NO OPINIONS WITHOUT DATA

Do not write subjective assessments like:
- "Management seems confident"
- "The company appears well-positioned"
- "This looks like a good setup"

Instead, let the data speak:
- "Management guided for 25% revenue growth in FY27 (Q3 concall). If achieved, this implies ₹X Cr revenue vs current TTM of ₹Y Cr."
- "ROCE at 22% is above sector median of 15%, with improving trend over 3 years."
