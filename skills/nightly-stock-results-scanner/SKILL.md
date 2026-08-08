---
name: nightly-stock-results-scanner
description: Scrape stockscans.in for latest quarterly results, filter for companies with 15%+ revenue growth, 15%+ OPM, and 15%+ EBITDA growth, then add them to Notion Results database.
---

You are running a nightly stock results scanner. Follow these steps precisely:

## Step 1: Scrape stockscans.in for latest results

Use the Chrome browser tools (Claude in Chrome) to:
1. First get browser tab context using tabs_context_mcp (createIfEmpty: true)
2. Navigate to https://www.stockscans.in/result-scans
3. Wait for the page to load, then run the following JavaScript extractor to get structured data from ALL visible result cards:

```javascript
(() => {
    const results = [];
    const tables = document.querySelectorAll('table');
    for (const table of tables) {
        try {
            let element = table;
            let companyName = null, dateStr = null, mcap = null;
            let revenueYoY = null, revenueQoQ = null;
            let opProfitYoY = null, opProfitQoQ = null;
            let opm = null;
            let patYoY = null, patQoQ = null;
            for (let i = 0; i < 15; i++) {
                element = element.previousElementSibling || element.parentElement;
                if (!element) break;
                const text = element.textContent || '';
                if (!companyName && (text.includes('Ltd') || text.includes('Limited'))) {
                    const match = text.match(/([A-Z][^\n]{3,}(?:Ltd|Limited))/);
                    if (match) companyName = match[1].trim();
                }
                if (!dateStr) {
                    const dateMatch = text.match(/(\d{1,2}\s+(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+\d{4})/);
                    if (dateMatch) dateStr = dateMatch[1];
                }
                if (companyName && dateStr) break;
            }
            if (!companyName) continue;
            const rows = table.querySelectorAll('tr');
            for (const row of rows) {
                const cells = Array.from(row.querySelectorAll('td, th'));
                if (cells.length < 3) continue;
                const cellTexts = cells.map(c => c.textContent.trim());
                const metric = cellTexts[0].toLowerCase();
                if (metric.includes('revenue')) {
                    revenueYoY = parseFloat(cellTexts[1]?.replace('%','').replace(',','')) || null;
                    revenueQoQ = parseFloat(cellTexts[2]?.replace('%','').replace(',','')) || null;
                }
                if (metric.includes('operating profit') && !metric.includes('opm')) {
                    opProfitYoY = parseFloat(cellTexts[1]?.replace('%','').replace(',','')) || null;
                    opProfitQoQ = parseFloat(cellTexts[2]?.replace('%','').replace(',','')) || null;
                }
                if (metric.includes('opm')) {
                    opm = parseFloat(cellTexts[3]?.replace('%','').replace(',','')) || null;
                }
                if (metric === 'pat' || (metric.includes('pat') && !metric.includes('operating'))) {
                    patYoY = parseFloat(cellTexts[1]?.replace('%','').replace(',','')) || null;
                    patQoQ = parseFloat(cellTexts[2]?.replace('%','').replace(',','')) || null;
                }
            }
            let afterEl = table;
            for (let i = 0; i < 10; i++) {
                afterEl = afterEl.nextElementSibling || afterEl.parentElement?.nextElementSibling;
                if (!afterEl) break;
                const text = afterEl.textContent || '';
                const mcapMatch = text.match(/MCap:\s*₹?\s*([\d,]+)/);
                if (mcapMatch) { mcap = mcapMatch[1]; break; }
            }
            results.push({ company: companyName, date: dateStr, revenueYoY, revenueQoQ, opProfitYoY, opProfitQoQ, opm, patYoY, patQoQ, mcap });
        } catch(e) {}
    }
    const seen = new Set();
    return results.filter(r => { if (seen.has(r.company)) return false; seen.add(r.company); return true; });
})()
```

## Step 2: Filter results

From the extracted results, keep ONLY companies that meet ALL of these criteria:
- Result published date is within the last 24 hours (compare against today's date)
- Revenue YoY growth >= 15%
- OPM (Operating Profit Margin) >= 15%
- Operating Profit YoY growth >= 15% (this is the EBITDA proxy)

Also note the QoQ values for each metric.

## Step 3: Determine the quarter

The page shows the current quarter (e.g., "Dec 2025" = Q3 FY26, "Mar 2026" = Q4 FY26, "Jun 2026" = Q1 FY27, "Sep 2026" = Q2 FY27). Map the quarter accordingly:
- Oct-Dec = Q3 of that fiscal year (FY runs Apr-Mar)
- Jan-Mar = Q4
- Apr-Jun = Q1 of next FY
- Jul-Sep = Q2

Use the quarter tag like "FY26Q4" when adding to Notion.

## Step 4: Add to Notion

For each filtered company, use the Notion MCP tool `notion_create_database_item` to add an entry to the "Results" database (ID: 328925d1-0745-8173-a488-ce7be498e5a5).

The database has these properties:
- Name (title) — company name
- Quarter (select) — e.g. "FY26Q3" or "FY26Q4"
- Revenue YoY % (number, percent format) — divide by 100, e.g. 81.6% → 0.816
- Revenue QoQ % (number, percent format) — divide by 100
- OPM % (number, percent format) — divide by 100
- Op Profit YoY % (number, percent format) — divide by 100
- Op Profit QoQ % (number, percent format) — divide by 100
- PAT YoY % (number, percent format) — divide by 100
- PAT QoQ % (number, percent format) — divide by 100
- MCap Cr (number) — remove commas, e.g. "9,913" → 9913
- Date Published (date) — ISO format of the result publication date
- Date Added (date) — today's date in ISO format

IMPORTANT: Before adding, search the Notion database using notion_query_database to check if the company already exists for this quarter to avoid duplicates.

## Step 5: Cookie handling

If the stockscans.in page shows a login screen or no results, the cookie may be expired. In that case:
- Inform the user that the cookie needs to be refreshed
- Suggest running /Users/rakeshkumarr/stockscan/stock_scan_cookie_update.py manually (it requires a visible browser for Google OAuth)

## Step 6: Report

Summarize what was found: how many total results were on the page, how many matched all criteria, and which companies were added to Notion. If no companies matched, say so.