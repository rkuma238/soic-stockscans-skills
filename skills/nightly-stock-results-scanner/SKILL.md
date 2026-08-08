---
name: nightly-stock-results-scanner
description: Nightly pipeline to scrape StockScans 24H quarterly results, filter GREEN (>20% YoY & >20% QoQ) and AMBER (only >20% YoY or QoQ) stocks, run fraud detection forensics v3.5.0, and save classified JSON reports.
version: 2.0.0
---

# Nightly 24H Stock Results & Fraud Scanner (v2.0.0)

Automatically runs nightly (scheduled at 21:00 IST via crontab) to extract all quarterly results declared in the last 24 hours from StockScans (`https://www.stockscans.in/result-scans`), classify growth momentum, run fraud triangulation, and output structured JSON and Markdown reports.

---

## 1. Classification & Filtering Rules

Every declared quarterly result is classified into one of three tiers:

| Tier Category | Quantitative Trigger Condition | Action / Output Protocol |
| :--- | :--- | :--- |
| 🟢 **GREEN (Double Acceleration)** | **Both YoY > 20% AND QoQ > 20%** (Revenue or Op Profit) | Saved to JSON, Markdown & synced to Notion. Runs `fraud-detection-forensics` v3.5.0. |
| 🟡 **AMBER (Single Acceleration)** | **Only YoY > 20% OR QoQ > 20%** | Saved to JSON & Markdown under AMBER watchlist. Runs fraud audit. |
| ❌ **IGNORE (Baseline / Subdued)**| **Neither YoY > 20% nor QoQ > 20%** | **Discarded completely**. Not saved to JSON or Notion. |

---

## 2. Automated Fraud Triangulation Checks (v3.5.0)

For all 🟢 GREEN and 🟡 AMBER stocks, the pipeline automatically evaluates:
1. **PAT-Revenue Divergence**: High sales growth with declining/negative PAT.
2. **Inventory Inflation / Profit Kicker**: Operating profit growth $> 2.5 \times$ Revenue growth.
3. **Tax Expense Anomaly**: PBT $> 0$ but Tax Expense $\le 0$.
4. **Extreme OPM Expansion**: OPM $> 30\%$.

---

## 3. Automated Output Destinations

- **JSON Output**: `/Users/rakeshkumarr/analyse_financial_data/reports/nightly_results_YYYY-MM-DD.json`
- **Markdown Report**: `/Users/rakeshkumarr/analyse_financial_data/reports/nightly_results_YYYY-MM-DD.md`
- **Crontab Schedule**: `0 21 * * *` (Every night at 21:00 IST)