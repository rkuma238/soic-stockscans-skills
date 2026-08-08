---
name: forensic-analyzer
description: Deep forensic analysis of earnings quality, cash conversion, and accounting red flags. Use when you need to assess earnings quality, detect accounting manipulation, analyze cash flow patterns, or investigate financial statement anomalies. Focuses on OCF vs profit, accrual quality, working capital analysis, and management credibility assessment.
---

# Forensic Analyzer - Earnings Quality Detective

Specialized forensic analysis of financial statements and earnings calls to detect accounting manipulation and assess earnings quality.

## Core Forensic Framework

### 1. Earnings Quality Assessment (Score 1-10)

#### Cash Conversion Analysis
- **OCF/Net Profit Ratio**: Healthy >0.8, Warning <0.7, Red Flag <0.5
- **Free Cash Flow Quality**: FCF vs reported earnings consistency
- **Cash Flow Timing**: Seasonal patterns vs one-time boosts

#### Accrual Quality Analysis  
- **Total Accruals**: (Net Income - OCF) / Total Assets
- **Working Capital Accruals**: Changes in receivables, inventory, payables
- **Discretionary Accruals**: Management's accounting choices impact

### 2. Balance Sheet Forensics

#### Working Capital Red Flags
- **Days Sales Outstanding (DSO)**: (Receivables / Daily Sales) trend
- **Inventory Days**: (Inventory / Daily COGS) vs revenue growth
- **Days Payable Outstanding (DPO)**: Payment timing manipulation
- **Cash Conversion Cycle**: DSO + Inventory Days - DPO

#### Asset Quality Checks
- **Receivables Growth vs Revenue**: Divergence indicates collection issues
- **Inventory Buildup**: Growth >Revenue growth = demand weakness
- **Capex vs Depreciation**: Maintenance vs growth capex analysis
- **Goodwill/Intangibles**: Write-down risks and impairment history

### 3. Revenue Quality Forensics

#### Revenue Recognition Red Flags
- **Channel Stuffing**: Unusual Q4 spikes, distributor inventory buildup
- **Bill and Hold**: Revenue without delivery
- **Related Party Sales**: Transactions with subsidiaries/promoters
- **Barter Transactions**: Non-cash revenue recognition

#### One-Time Items Analysis
- **Non-Recurring Revenue**: Asset sales, insurance claims, reversals
- **Exceptional Items**: Frequency of "one-time" charges
- **Reclassification**: Moving expenses between categories

### 4. Management Credibility Assessment

#### Track Record Analysis
- **Guidance Accuracy**: Historical promises vs delivery (8 quarters)
- **Earnings Surprises**: Beat/miss pattern and magnitude
- **Restatements History**: Past accounting corrections
- **Auditor Changes**: Frequency and reasons for switches

#### Language Pattern Analysis
- **Hedging Language**: Uncertainty indicators in guidance
- **Evasion Patterns**: Questions dodged in analyst calls
- **Tone Shifts**: Confidence changes between quarters
- **Blame Attribution**: External factors vs internal execution

## Forensic Analysis Output

### Earnings Quality Scorecard
| Component | Score (1-10) | Weight | Evidence |
|-----------|--------------|---------|----------|
| Cash Conversion | 6/10 | 30% | OCF/Profit: 0.72 |
| Accrual Quality | 7/10 | 25% | Total accruals: 3% of assets |
| Working Capital | 5/10 | 20% | DSO increased 8 days |
| Revenue Quality | 8/10 | 15% | No major red flags |
| Management Credibility | 6/10 | 10% | 70% guidance accuracy |
| **Overall Score** | **6.2/10** | **100%** | **MODERATE QUALITY** |

### Red Flag Summary
| Red Flag | Severity | Evidence | Impact |
|----------|----------|----------|---------|
| Working Capital Deterioration | HIGH | DSO +8 days, Inventory +25% | Potential collection issues |
| Cash Conversion Decline | MEDIUM | OCF/Profit 0.72 vs 0.85 last year | Earnings quality concern |
| Management Evasion | MEDIUM | Dodged 3/8 margin questions | Credibility gap |

### Forensic Recommendations
- **Monitor Closely**: Working capital trends and cash conversion
- **Investigate Further**: Receivables aging and collection patterns  
- **Discount Valuation**: Apply 10-15% discount for quality concerns
- **Key Questions**: Ask management about DSO increase drivers

## Analysis Workflow

### Phase 1: Data Extraction
```bash
# Extract financial data from transcript and screener.in
python scripts/extract_forensic_data.py transcript.txt financials.json
```

### Phase 2: Forensic Analysis
```bash
# Run comprehensive forensic analysis
python scripts/forensic_analysis.py --earnings-quality --cash-flow --working-capital
```

### Phase 3: Credibility Assessment
```bash
# Analyze management credibility patterns
python scripts/credibility_analyzer.py transcript.txt --historical-data
```

## Key Forensic Ratios

### Cash Flow Quality
- **Cash Conversion Ratio**: OCF / Net Income (Target: >0.8)
- **Cash Flow Margin**: OCF / Revenue (Compare to net margin)
- **Free Cash Flow Yield**: FCF / Market Cap (Investment attractiveness)

### Working Capital Efficiency  
- **Asset Turnover**: Revenue / Total Assets (Efficiency trend)
- **Receivables Turnover**: Revenue / Avg Receivables (Collection speed)
- **Inventory Turnover**: COGS / Avg Inventory (Demand strength)

### Earnings Persistence
- **Core Earnings**: Adjusted for one-time items
- **Earnings Smoothing**: Variance in quarterly results
- **Accrual Reversals**: Multi-period accrual patterns

## Integration Points

- **Input**: Conference call transcripts, financial statements from screener.in
- **Output**: Earnings quality score, red flag alerts, credibility assessment
- **Triggers**: "Forensic analysis", "earnings quality", "cash flow analysis"
- **Complements**: Works with other specialized skills for complete analysis

This skill provides institutional-grade forensic analysis to detect accounting manipulation and assess true earnings quality.