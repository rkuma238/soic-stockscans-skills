# Screener Financial Data Skill

A comprehensive Cursor skill for fetching financial data from screener.in for Indian listed companies.

## Installation

1. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Verify installation:**
   ```bash
   python scripts/screener_client.py search "TCS"
   ```

## Quick Start

### Search for Companies
```bash
python scripts/screener_client.py search "Tata Consultancy"
python scripts/screener_client.py search "Reliance"
```

### Get Company Data
```bash
python scripts/screener_client.py company TCS
python scripts/screener_client.py ratios TCS
python scripts/screener_client.py quarterly TCS
```

### Format Output
```bash
python scripts/screener_client.py company TCS --format table
python scripts/screener_client.py ratios TCS --format json
```

## Available Commands

| Command | Description | Example |
|---------|-------------|---------|
| `search` | Find companies by name/ticker | `search "Tata"` |
| `company` | Get comprehensive company data | `company TCS` |
| `ratios` | Get financial ratios | `ratios TCS` |
| `quarterly` | Get quarterly results | `quarterly TCS` |
| `complete` | Get all available data | `complete TCS` |

## Options

| Option | Description | Example |
|--------|-------------|---------|
| `--standalone` | Use standalone instead of consolidated data | `company TCS --standalone` |
| `--format table` | Format output as table | `ratios TCS --format table` |
| `--format json` | Format output as JSON (default) | `company TCS --format json` |

## Data Coverage

- **Company Search**: Name, ticker, sector, URL
- **Key Metrics**: ROE, ROCE, P/E ratio, Market Cap, Book Value, Dividend Yield
- **Financial Ratios**: Debt ratios, efficiency metrics, profitability ratios
- **Quarterly Results**: Sales, expenses, profit margins, EPS trends
- **Growth Metrics**: Sales CAGR, profit CAGR, stock price returns
- **Shareholding Pattern**: Promoter, FII, DII, public holdings

## Integration with Cursor

This skill is automatically available in Cursor when you:
1. Ask about Indian company financials
2. Mention screener.in
3. Request financial analysis for Indian stocks
4. Need quarterly results or balance sheet data

### Example Prompts

- "Get financial data for TCS from screener.in"
- "Compare the ratios of TCS and Infosys"
- "Show me quarterly results for Reliance"
- "Search for Adani companies and get their key metrics"

## Error Handling

The script gracefully handles:
- Network connectivity issues
- Invalid ticker symbols
- Rate limiting from screener.in
- Data parsing errors
- Missing data fields

## Limitations

- Data is limited to Indian listed companies
- Some advanced metrics require screener.in premium access
- Real-time prices may have slight delays
- Rate limiting may apply for bulk requests

## Contributing

To improve the data extraction:
1. Enhance the HTML parsing in `screener_client.py`
2. Add more financial metrics extraction
3. Improve error handling and retry logic
4. Add data validation and cleaning

## License

This skill is provided as-is for educational and research purposes. Please respect screener.in's terms of service and rate limits.