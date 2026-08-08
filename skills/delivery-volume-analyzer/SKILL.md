---
name: delivery-volume-analyzer
description: "Atomic skill that fetches 30-40 trading days of NSE/BSE Delivery Volume, Deliverable Quantity, Delivery %, and Price Change % to classify Institutional Accumulation, Distribution, Fake Moves, and Delivery Breakout Squeezes. Also detects and audits Unusual Volume Spikes (Volume Multiple >= 2.5x 20-Day Average) to classify Institutional Surge Accumulation, Selling Surges, Speculative Pump & Churn, and Bulk/Block Deal Squeezes."
type: ATOMIC
version: 3.0.0
inputs:
  - symbol: string
  - nse_symbol: string
  - lookback_days: integer  # default: 40
outputs:
  - delivery_summary_table: object[]      # rows with REAL DATES (not T-1, T-2 labels)
  - unusual_volume_events: object[]
  - avg_volume_20d: float
  - microstructure_classification: string
  - accumulation_score: float
  - delivery_decryption: string
---

# Delivery & Volume Microstructure + Unusual Volume Spike Analyzer (ATOMIC v3.1.0)

---

## MANDATORY REQUIREMENT: NSE/BSE DELIVERY BHAVCOPY EXTRACTION & DATED MULTI-TABLE ANALYSIS

**ZERO TOLERANCE RULE**: 
1. Delivery and volume data MUST be sourced from official **NSE / BSE Delivery Bhavcopy Archives** or live NSE APIs.
2. Every analysis MUST generate a full **25-35 Dated Trading Session Grid (Sub-Table A)** using real calendar dates (e.g., `06-Aug-2026`, `05-Aug-2026`). Session placeholders ("T-1", "Session X") are STRICTLY FORBIDDEN.
3. Every analysis MUST generate **Sub-Table B: Unusual Volume Spike Events Summary Table** (Vol Multiple >= 2.25x with Tier 1-4 classifications and Bulk/Block Deal cross-checks).
4. Every analysis MUST include verbose 5-point **🔍 Reading Between the Lines & Financial Decryption** commentary matching the IDFC First Bank benchmark standards.

---

## Step 1: Fetch Live NSE/BSE Delivery Bhavcopy Data (MANDATORY)

Use the following data-fetching methods to extract dated session delivery data:

### Primary Source — Live NSE/BSE Delivery Bhavcopy & Security-wise API
Fetch from NSE India's official security-wise delivery position endpoint / Bhavcopy archives:
```
GET https://www.nseindia.com/api/historical/cm/equity?symbol={SYMBOL}&series=EQ&from={FROM_DATE}&to={TO_DATE}
https://archives.nseindia.com/products/content/sec_bhavdata_full.csv
https://www.nseindia.com/api/historical/bulk-deals?symbol={SYMBOL}
```
Extract per session: `Date`, `Total Traded Volume`, `Deliverable Quantity`, `Delivery %`, `Closing Price`, `Price Change %`.


### Priority 4 — Playwright Browser MCP Tool
If API access is unavailable, use the playwright browser MCP tool to navigate to:
```
https://www.nseindia.com/get-quotes/equity?symbol={SYMBOL}
```
Click on the **"Historical Data"** tab → Select **"Deliveries"** radio button → Set date range to last 40 trading days → Capture all rows from the rendered table.

### Priority 5 — Screener `analyze_annual_report` / `get_quarterly_results`
Use screener MCP `get_quarterly_results(symbol)` to cross-verify volume trends.

---

## Step 2: Build the Data Table Schema (REAL DATES — MANDATORY)

From the fetched data, construct the following row schema for each trading session:

```json
{
  "date": "DD-Mon-YYYY",           // REAL DATE — e.g., "05-Aug-2026". NEVER "T-1" or "Session T-X"
  "total_volume": 12450000,        // Total shares traded
  "avg_vol_20d": 4200000,          // 20-Day Simple Moving Average of volume (rolling)
  "vol_multiple": 2.97,            // total_volume / avg_vol_20d
  "deliverable_qty": 8350000,      // Deliverable (non-intraday) quantity
  "delivery_pct": 67.1,            // deliverable_qty / total_volume * 100
  "closing_price": 86.2,           // Closing price on that date
  "prev_close": 83.6,              // Previous day closing price
  "price_change_pct": 3.11,        // (closing - prev_close) / prev_close * 100
  "microstructure_signal": "ACCUMULATION",   // one of: ACCUMULATION | DISTRIBUTION | FAKE_MOVE | BREAKOUT | UNUSUAL_SURGE | PUMP_AND_CHURN
  "unusual_volume_flag": "2.97x",  // null if vol_multiple < 2.5, else the ratio string
  "unusual_volume_tier": 1,        // 1-4 or null
  "institutional_verdict": "FII/DII Block Accumulation"
}
```

---

## Step 3: Compute 20-Day Moving Average Volume

$$\text{20D Avg Volume} = \frac{\sum_{i=1}^{20} \text{Volume}_i}{20}$$

Recompute this rolling for each session row so that the Vol Multiple reflects the correct baseline for that session's lookback window.

---

## Step 4: Microstructure Classifications

### 4A. Standard Delivery % Signal:

| Signal | Delivery % | Price Change | Vol Condition | Classification |
| :--- | :---: | :---: | :---: | :--- |
| 🟢 Institutional Accumulation | $\ge 50\%$ | Flat or positive | Normal | Smart money building long positions |
| 🔴 Institutional Distribution | $\ge 45\%$ | Negative ($< -1.5\%$) | High | Smart money dumping into retail demand |
| ⚠️ Fake Move / Speculative Churn | $< 20\%$ | Any (often +ve) | High | Day-trader intraday frenzy; no real delivery |
| 🚀 Delivery Breakout Squeeze | $\ge 60\%$ | Positive ($> +2\%$) | $> 2\times$ 20D | Institutional-backed breakout with high conviction |

### 4B. Unusual Volume Spike Tier System (Vol Multiple $\ge 2.5\times$):

| Tier | Signal | Vol Multiple | Delivery % | Price Change | Action Verdict |
| :---: | :--- | :---: | :---: | :---: | :--- |
| **1** | ⚡ Institutional Surge Accumulation | $\ge 2.5\times$ | $\ge 50\%$ | $> +1.5\%$ | 🟢 FII/DII block accumulation — confirm on NSE bulk deal board |
| **2** | 🚨 Institutional Dump / Selling Surge | $\ge 2.5\times$ | $\ge 45\%$ | $< -2.0\%$ | 🔴 Institutions liquidating — reduce / exit positions |
| **3** | 🌀 Speculative Pump & Churn | $\ge 3.0\times$ | $< 20\%$ | Any | ⚠️ Retail frenzy / algo pump — do NOT chase |
| **4** | 📦 Bulk / Block Deal Execution | $\ge 4.0\times$ | $\ge 70\%$ | Any | 📦 Check NSE/BSE bulk deal disclosures for identity |

---

## Step 5: Render Output Tables (REAL DATES — MANDATORY)

### Sub-Table A: 30–40 Day Delivery % & Volume Microstructure Grid

**COLUMN ORDER (exact):**

| **Date** | Total Volume | **20D Avg Vol** | **Vol Multiple** | Deliverable Qty | **Delivery %** | Close Price (₹) | Daily Chg % | **Microstructure Signal** | **Unusual Vol Flag** | Institutional Verdict |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- | :---: | :--- |

- **Date column = REAL calendar date** (`DD-Mon-YYYY`). Populated from live NSE/BSE data.
- Sort rows in **reverse chronological order** (most recent date at the top).
- Bold and emoji-prefix any unusual volume session row for visual prominence.
- Last row = **30-Day Rolling Average** row with averages for all numeric columns.

---

### Sub-Table B: Unusual Volume Spike Events Summary Table

Only include sessions where `vol_multiple >= 2.5`. If no such sessions exist in the 30-40 day window, state: *"No Unusual Volume Events Detected in the Last 30–40 Trading Sessions."*

| **Date** | Total Volume | 20D Avg Volume | **Vol Multiple** | **Delivery %** | Daily Price Chg % | **Unusual Volume Tier** | Bulk / Block Deal Cross-Check | Action Verdict |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- | :---: | :--- |

---

## Step 6: Verbose 🔍 Reading Between the Lines Commentary (MANDATORY)

After rendering both sub-tables, write 4–6 verbose paragraphs covering:
1. **Overall 30-Day Smart Money Verdict** — Is the average delivery % showing accumulation or distribution?
2. **Unusual Volume Event Deep Dive** — For each unusual volume event, narrate what the combination of Vol Multiple + Delivery % + Price Change + bulk deal cross-check implies.
3. **Fake Move Identification** — Explicitly call out any sessions with high volume but low delivery % as retail day-trading noise.
4. **Stan Weinstein Stage Implication** — Which of Stage 1 (Accumulation), Stage 2 (Markup), Stage 3 (Distribution), Stage 4 (Capitulation) does the microstructure suggest?
5. **Actionable Investment Signal** — What should a long-term investor interpret from the 30-40 day delivery microstructure pattern?

---

## Output Schema
```json
{
  "delivery_summary_table": [...],  // List of session objects with REAL DATES
  "unusual_volume_events": [...],   // Only sessions with vol_multiple >= 2.5
  "avg_volume_20d": 4200000,
  "microstructure_classification": "INSTITUTIONAL_ACCUMULATION",
  "accumulation_score": 0.74,       // 0.0 (strong distribution) to 1.0 (strong accumulation)
  "delivery_decryption": "..."      // Verbose multi-paragraph narrative
}
```
