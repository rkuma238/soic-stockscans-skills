---
name: financial-modeler
description: Build comprehensive Bull/Bear/Normal financial scenarios with DCF, PE, and EV/EBITDA valuations. Use when creating financial projections, calculating fair value, building scenario analysis, or generating price targets. Integrates current share price from screener.in with guidance-based modeling to produce risk-adjusted valuations.
---

# Financial Modeler - Scenario & Valuation Engine

Comprehensive financial modeling with Bull/Bear/Normal scenarios, multiple valuation methods, and risk-adjusted price targets based on current market price.

## Core Modeling Framework

### 1. Scenario Construction

#### Bull Case (Optimistic Scenario)
- **Revenue Growth**: Upper end of guidance + market share gains
- **Margin Expansion**: Operational leverage + cost optimization success
- **Multiple Expansion**: Premium valuation for growth/quality
- **Probability**: 20-25% (favorable conditions align)

#### Normal Case (Base Scenario)  
- **Revenue Growth**: Midpoint of management guidance
- **Margin Maintenance**: Current levels with modest improvement
- **Multiple Stability**: Historical average multiples
- **Probability**: 50-60% (guidance achieved as stated)

#### Bear Case (Conservative Scenario)
- **Revenue Growth**: Lower end of guidance or miss
- **Margin Compression**: Cost pressures, competitive headwinds  
- **Multiple Contraction**: Discount for execution/quality concerns
- **Probability**: 20-30% (challenges exceed expectations)

### 2. Financial Projections (3-Year Model)

#### Revenue Modeling
```
Bull Case:
- FY26E: ₹2,75,000 Cr (+15% vs guidance 8-10%)
- FY27E: ₹3,16,250 Cr (+15% sustained growth)
- FY28E: ₹3,63,688 Cr (+15% market leadership)

Normal Case:  
- FY26E: ₹2,60,000 Cr (+9% midpoint guidance)
- FY27E: ₹2,83,400 Cr (+9% steady execution)
- FY28E: ₹3,08,906 Cr (+9% consistent delivery)

Bear Case:
- FY26E: ₹2,50,000 Cr (+5% below guidance)
- FY27E: ₹2,62,500 Cr (+5% market headwinds)
- FY28E: ₹2,75,625 Cr (+5% competitive pressure)
```

#### Profitability Modeling
- **EBITDA Margins**: Bull 29%, Normal 27%, Bear 25%
- **Depreciation**: % of gross block based on capex cycle
- **Interest**: Debt levels and prevailing rates
- **Tax Rate**: Effective rate considering incentives
- **PAT Margins**: Bottom-line impact of scenarios

### 3. Multiple Valuation Methods

#### PE-Based Valuation
```
Current Market Data (from screener.in):
- Share Price: ₹2,558
- TTM EPS: ₹131.88  
- Current PE: 19.4x

Scenario PE Multiples:
- Bull Case: 22x (growth premium)
- Normal Case: 19x (historical average)
- Bear Case: 16x (quality discount)

Price Targets:
- Bull: ₹145 EPS × 22x = ₹3,190 (+25%)
- Normal: ₹135 EPS × 19x = ₹2,565 (0%)  
- Bear: ₹125 EPS × 16x = ₹2,000 (-22%)
```

#### EV/EBITDA Valuation
- **Enterprise Value**: Market cap + net debt
- **EBITDA Multiples**: Industry benchmarks adjusted for scenarios
- **Equity Value**: EV minus net debt
- **Per Share Value**: Equity value / shares outstanding

#### DCF Valuation  
- **Free Cash Flow**: EBIT(1-Tax) + Depreciation - Capex - Working Capital
- **Terminal Growth**: 3-4% based on GDP growth
- **WACC**: Cost of equity and debt weighted by capital structure
- **Present Value**: Discounted cash flows + terminal value

### 4. Risk-Adjusted Valuation

#### Risk Assessment Integration
- **Earnings Quality**: Discount for poor cash conversion
- **Management Credibility**: Discount for poor track record  
- **Business Model**: Discount for competitive threats
- **Financial Health**: Discount for leverage/liquidity concerns

#### Risk Adjustment Matrix
| Risk Factor | Impact | Discount Applied |
|-------------|--------|------------------|
| Earnings Quality Issues | High | -15% |
| Management Credibility Gap | Medium | -10% |
| Competitive Pressure | Medium | -8% |
| Working Capital Deterioration | Low | -5% |
| **Total Risk Discount** | | **-25%** |

#### Final Price Target Calculation
```
Base Case Valuation: ₹2,565
Risk Adjustment: -15% (moderate concerns)
Risk-Adjusted Target: ₹2,180
Current Price: ₹2,558
Downside Risk: -15%
Recommendation: HOLD (limited upside, moderate risk)
```

## Valuation Output Framework

### Scenario Summary Table
| Scenario | Revenue CAGR | EBITDA Margin | EPS FY28E | PE Multiple | Price Target | Probability |
|----------|--------------|---------------|-----------|-------------|--------------|-------------|
| **Bull** | 15% | 29% | ₹145 | 22x | ₹3,190 | 25% |
| **Normal** | 9% | 27% | ₹135 | 19x | ₹2,565 | 50% |
| **Bear** | 5% | 25% | ₹125 | 16x | ₹2,000 | 25% |

### Probability-Weighted Fair Value
```
Expected Value = (25% × ₹3,190) + (50% × ₹2,565) + (25% × ₹2,000)
Expected Value = ₹798 + ₹1,283 + ₹500 = ₹2,581
Risk-Adjusted Fair Value = ₹2,581 × (1 - 15%) = ₹2,194
```

### Sensitivity Analysis
| Variable | -10% | -5% | Base | +5% | +10% |
|----------|------|-----|------|-----|------|
| Revenue Growth | ₹2,200 | ₹2,380 | ₹2,565 | ₹2,750 | ₹2,940 |
| EBITDA Margin | ₹2,310 | ₹2,440 | ₹2,565 | ₹2,695 | ₹2,820 |
| PE Multiple | ₹2,180 | ₹2,370 | ₹2,565 | ₹2,760 | ₹2,950 |

## Modeling Workflow

### Phase 1: Data Integration
```bash
# Get current price and financial data
python scripts/fetch_market_data.py TICKER --source screener.in
```

### Phase 2: Scenario Building
```bash  
# Build 3 scenarios from guidance
python scripts/build_scenarios.py guidance.json financials.json
```

### Phase 3: Valuation Analysis
```bash
# Calculate multiple-based valuations
python scripts/calculate_valuations.py scenarios.json --methods PE,EV_EBITDA,DCF
```

### Phase 4: Risk Adjustment
```bash
# Apply risk discounts from other analyses  
python scripts/risk_adjust.py valuations.json red_flags.json credibility.json
```

## Key Modeling Assumptions

### Revenue Drivers
- **Organic Growth**: Market expansion, pricing power
- **Market Share**: Competitive positioning changes
- **New Products**: Innovation pipeline contribution
- **Geographic Mix**: Emerging vs developed markets

### Margin Drivers  
- **Operating Leverage**: Fixed cost absorption
- **Cost Inflation**: Input cost pressures
- **Pricing Power**: Ability to pass through costs
- **Mix Shift**: High-margin vs low-margin business

### Multiple Justification
- **Growth Rate**: Higher growth commands premium
- **Profitability**: Sustainable margins support multiples
- **Quality**: Predictable earnings deserve premium
- **Competitive Moat**: Defensibility supports valuation

## Integration Points

- **Input**: Management guidance, current share price, financial statements
- **Output**: Scenario-based price targets, probability-weighted fair value
- **Triggers**: "Financial model", "valuation analysis", "price target", "scenario analysis"  
- **Complements**: Uses guidance credibility and risk assessments from other skills

This skill provides institutional-grade financial modeling with comprehensive scenario analysis and risk-adjusted valuations for investment decision-making.