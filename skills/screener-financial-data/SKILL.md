---
name: screener-financial-data
description: Fetch comprehensive financial data from screener.in for Indian companies. Use when analyzing Indian stocks, getting company financials, quarterly results, balance sheets, cash flows, or when the user mentions screener.in, Indian companies, or financial analysis.
---

# Screener Financial Data

Fetch comprehensive financial data from screener.in for Indian listed companies including company search, detailed financials, quarterly results, balance sheets, cash flows, ratios, and shareholding patterns.

## Quick Start

Use the Python script to fetch data:

```bash
python scripts/screener_client.py search "TCS"
python scripts/screener_client.py company TCS
python scripts/screener_client.py ratios TCS
python scripts/screener_client.py quarterly TCS
```

## Available Commands

### 1. Company Search
Search for companies by name or ticker:

```bash
python scripts/screener_client.py search "Tata Consultancy"
python scripts/screener_client.py search "Reliance"
```

### 2. Company Overview
Get basic company information and key metrics:

```bash
python scripts/screener_client.py company TCS
python scripts/screener_client.py company RELIANCE --standalone
```

### 3. Financial Ratios
Get key financial ratios and metrics:

```bash
python scripts/screener_client.py ratios TCS
```

### 4. Quarterly Results
Get quarterly financial statements:

```bash
python scripts/screener_client.py quarterly TCS
python scripts/screener_client.py quarterly RELIANCE --standalone
```

### 5. Complete Analysis
Get comprehensive financial analysis:

```bash
python scripts/screener_client.py complete TCS
```

## Output Format

All commands return structured JSON data that can be:
- Displayed in formatted tables
- Saved to files for further analysis
- Used in financial models or reports

## Data Coverage

- **Company Search**: Name, ticker, sector, URL
- **Financial Metrics**: ROE, ROCE, P/E, Market Cap, Book Value
- **Quarterly Results**: Sales, expenses, profit, margins, EPS
- **Annual Data**: P&L, Balance Sheet, Cash Flow (10+ years)
- **Growth Metrics**: Sales/Profit CAGR, Stock price returns
- **Ratios**: Working capital, debt, efficiency ratios
- **Shareholding**: Promoter, FII, DII, public holdings

## Error Handling

The script handles common issues:
- Invalid ticker symbols
- Network connectivity problems
- Data parsing errors
- Rate limiting from screener.in

## Requirements

Install dependencies:

```bash
pip install requests beautifulsoup4 lxml pandas
```

## Usage Examples

**Find IT companies:**
```bash
python scripts/screener_client.py search "Information Technology"
```

**Compare two companies:**
```bash
python scripts/screener_client.py company TCS > tcs_data.json
python scripts/screener_client.py company INFY > infy_data.json
```

**Get quarterly trends:**
```bash
python scripts/screener_client.py quarterly TCS --format table
```

## Data Source

All data is fetched from [screener.in](https://www.screener.in), a comprehensive platform for Indian stock market analysis and fundamental research.

## Limitations

- Data is limited to Indian listed companies
- Real-time prices may have slight delays
- Some premium features require screener.in login
- Rate limiting may apply for bulk requests