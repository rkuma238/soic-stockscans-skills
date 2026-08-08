# Screener Financial Data - Usage Examples

## Basic Usage Examples

### 1. Company Search
Find companies by name or partial name:

```bash
# Search for Tata companies
python scripts/screener_client.py search "Tata"

# Search for IT companies
python scripts/screener_client.py search "Information Technology"

# Search by partial ticker
python scripts/screener_client.py search "REL"
```

**Sample Output:**
```json
{
  "results": [
    {
      "name": "Tata Consultancy Services Ltd",
      "ticker": "TCS",
      "url": "https://www.screener.in/company/TCS/consolidated/",
      "sector": "Information Technology"
    }
  ]
}
```

### 2. Company Overview
Get comprehensive company data:

```bash
# Get TCS consolidated data
python scripts/screener_client.py company TCS

# Get standalone data
python scripts/screener_client.py company TCS --standalone

# Format as table
python scripts/screener_client.py company TCS --format table
```

### 3. Financial Ratios
Get key financial ratios:

```bash
python scripts/screener_client.py ratios TCS
python scripts/screener_client.py ratios RELIANCE
```

### 4. Quarterly Results
Get quarterly financial statements:

```bash
python scripts/screener_client.py quarterly TCS
python scripts/screener_client.py quarterly INFY --standalone
```

## Advanced Usage Patterns

### Comparative Analysis
Compare multiple companies:

```bash
# Save data for multiple companies
python scripts/screener_client.py company TCS > tcs_data.json
python scripts/screener_client.py company INFY > infy_data.json
python scripts/screener_client.py company WIPRO > wipro_data.json

# Compare ratios
python scripts/screener_client.py ratios TCS --format table
python scripts/screener_client.py ratios INFY --format table
```

### Sector Analysis
Analyze companies in a specific sector:

```bash
# Find IT companies
python scripts/screener_client.py search "Software" > it_companies.json

# Get data for top IT companies
for ticker in TCS INFY WIPRO HCLTECH TECHM; do
    python scripts/screener_client.py complete $ticker > ${ticker}_analysis.json
done
```

### Time Series Analysis
Track quarterly performance:

```bash
# Get quarterly data
python scripts/screener_client.py quarterly TCS > tcs_quarterly.json

# Extract specific metrics for trend analysis
# (You can process the JSON output with jq or Python scripts)
```

## Integration Examples

### With Python Scripts
```python
import subprocess
import json

def get_company_data(ticker):
    """Get company data using the screener client"""
    result = subprocess.run([
        'python', 'scripts/screener_client.py', 'company', ticker
    ], capture_output=True, text=True)
    
    if result.returncode == 0:
        return json.loads(result.stdout)
    else:
        print(f"Error: {result.stderr}")
        return None

# Usage
tcs_data = get_company_data('TCS')
if tcs_data:
    print(f"TCS Market Cap: {tcs_data['key_metrics'].get('Market Cap', 'N/A')}")
```

### With Shell Scripts
```bash
#!/bin/bash
# analyze_portfolio.sh

PORTFOLIO_TICKERS="TCS INFY RELIANCE HDFCBANK ICICIBANK"

echo "Portfolio Analysis Report"
echo "========================"

for ticker in $PORTFOLIO_TICKERS; do
    echo "Analyzing $ticker..."
    python scripts/screener_client.py ratios $ticker --format table
    echo ""
done
```

## Error Handling Examples

### Network Issues
```bash
# The script handles network timeouts gracefully
python scripts/screener_client.py company INVALID_TICKER
# Output: Error message to stderr, empty JSON to stdout
```

### Invalid Tickers
```bash
# Invalid ticker handling
python scripts/screener_client.py company XYZ123
# Returns empty result with error message
```

## Output Processing Examples

### Using jq for JSON Processing
```bash
# Extract just the current price
python scripts/screener_client.py company TCS | jq -r '.current_price'

# Get key metrics only
python scripts/screener_client.py company TCS | jq '.key_metrics'

# Extract quarterly sales data
python scripts/screener_client.py quarterly TCS | jq '.quarterly_results[] | select(.metric == "Sales")'
```

### Using Python for Data Processing
```python
import json
import subprocess

def analyze_pe_ratios(tickers):
    """Compare P/E ratios across multiple companies"""
    pe_data = {}
    
    for ticker in tickers:
        result = subprocess.run([
            'python', 'scripts/screener_client.py', 'ratios', ticker
        ], capture_output=True, text=True)
        
        if result.returncode == 0:
            data = json.loads(result.stdout)
            pe_ratio = data.get('key_metrics', {}).get('Stock P/E', 'N/A')
            pe_data[ticker] = pe_ratio
    
    return pe_data

# Usage
it_stocks = ['TCS', 'INFY', 'WIPRO', 'HCLTECH']
pe_comparison = analyze_pe_ratios(it_stocks)
print("P/E Ratio Comparison:")
for ticker, pe in pe_comparison.items():
    print(f"{ticker}: {pe}")
```

## Performance Tips

1. **Batch Processing**: Add small delays between requests to avoid rate limiting
2. **Caching**: Save results to files for repeated analysis
3. **Error Handling**: Always check return codes and handle network errors
4. **Data Validation**: Verify ticker symbols before making requests

## Common Use Cases

### Investment Research
```bash
# Research a potential investment
python scripts/screener_client.py search "Adani"
python scripts/screener_client.py complete ADANIPORTS
python scripts/screener_client.py ratios ADANIPORTS --format table
```

### Portfolio Monitoring
```bash
# Monitor existing holdings
for ticker in $(cat my_portfolio.txt); do
    echo "=== $ticker ==="
    python scripts/screener_client.py ratios $ticker --format table
done
```

### Sector Comparison
```bash
# Compare banking stocks
BANKS="HDFCBANK ICICIBANK SBIN AXISBANK KOTAKBANK"
for bank in $BANKS; do
    python scripts/screener_client.py ratios $bank > ${bank}_ratios.json
done
```