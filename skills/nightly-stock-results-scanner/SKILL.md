---
name: nightly-stock-results-scanner
description: Nightly pipeline to scrape StockScans 24H quarterly results, filter >= ₹1,000 Cr MCap companies, classify GREEN (>20% YoY & >20% QoQ) and AMBER (only >20% YoY or QoQ) stocks, update persistent Q<>FY<> cumulative master JSON database (append daily, unique once only, sorted by PAT YoY %), and run fraud detection v3.5.0.
version: 2.4.0
---

# Nightly 24H Stock Results & Fraud Scanner (v2.4.0)

Automatically runs nightly (scheduled at 21:00 IST via crontab) to extract all quarterly results declared in the last 24 hours from StockScans (`https://www.stockscans.in/result-scans`), filter out companies under ₹1,000 Cr Market Cap, classify growth momentum, append newly declared companies to the cumulative `Q<>FY<>` master database, and output sorted Markdown & JSON reports.

---

## 1. Core Mandatory Filtering & Classification Rules

1. **Market Cap Filter**: Pick ONLY companies with **Market Cap $\ge$ ₹1,000 Crore** (`mcap_num >= 1000.0`). Discard all small/micro cap noise below ₹1,000 Cr.
2. **Growth Momentum Classification**:
   - 🟢 **GREEN (Double Acceleration)**: Both **YoY > 20% AND QoQ > 20%** (Revenue, Op Profit, or PAT).
   - 🟡 **AMBER (Single Acceleration)**: Only **YoY > 20% OR QoQ > 20%**.
   - ❌ **IGNORE (Baseline / Subdued)**: Neither YoY > 20% nor QoQ > 20%. **Discarded completely**.
3. **Cumulative Master JSON Database (Append Daily, Unique Once Only)**:
   - Maintained at `/Users/rakeshkumarr/analyse_financial_data/reports/master_quarterly_results.json`
   - Dynamically tagged by fiscal quarter (e.g. `Q1FY27`, `Q4FY26`, `Q3FY26`).
   - Every night, appends newly declared companies without replacing existing results.
   - Each company appears **ONLY ONCE per quarter** (Zero duplicates).
4. **ALWAYS SORTED DESCENDING BY PAT YoY % EVERY NIGHT**:
   - Displays both **PAT YoY %** and **PAT QoQ %** side-by-side.
   - Every night, the entire cumulative master list (`Q1FY27`) is **resorted descending by PAT YoY % (`patYoY_num`)** so the highest net profit compounders appear at the top.

---

## 2. Automated Fraud Triangulation Checks (v3.5.0)

For all 🟢 GREEN and 🟡 AMBER stocks, the pipeline automatically evaluates:
1. **PAT-Revenue Divergence**: High sales growth with declining/negative PAT.
2. **Inventory Inflation / Profit Kicker**: Operating profit growth $> 2.5 \times$ Revenue growth.
3. **Tax Expense Anomaly**: PBT $> 0$ but Tax Expense $\le 0$.
4. **Extreme OPM Expansion**: OPM $> 30\%$.

---

## 3. Persistent Output Files & Crontab Schedule

- **Cumulative Master JSON**: `/Users/rakeshkumarr/analyse_financial_data/reports/master_quarterly_results.json`
- **Cumulative Master Markdown**: `/Users/rakeshkumarr/analyse_financial_data/reports/master_quarterly_results.md`
- **Daily Snapshot Markdown**: `/Users/rakeshkumarr/analyse_financial_data/reports/nightly_results_YYYY-MM-DD.md`
- **Crontab Schedule**: `0 21 * * *` (Every night at 21:00 IST)