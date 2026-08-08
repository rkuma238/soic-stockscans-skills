---
name: concall-orchestrator
description: Master orchestrator for comprehensive conference call analysis using specialized skills. Use when you need complete earnings call analysis combining forensic analysis, guidance tracking, inflection point detection, red flag scanning, and financial modeling. Coordinates 5 specialized skills to provide institutional-grade investment analysis with Bull/Bear/Normal scenarios, inflection timing, and risk-adjusted valuations.
---

# Conference Call Orchestrator - Master Analysis Coordinator

Coordinates 5 specialized skills to provide comprehensive conference call analysis for investment decision-making with inflection point timing.

## Orchestration Framework

### Phase 1: Data Preparation (Parallel)
Run simultaneously using Task tool:

**Task A - Extract Transcript:**
```
Extract full transcript from uploaded PDF or text.
Save to /tmp/transcript.txt with company info to /tmp/company_info.json
```

**Task B - Fetch Financial Context:**
```
Use screener-financial-data skill to get comprehensive financials including current share price.
Save to /tmp/financials.json with current market data
```

### Phase 2: Specialized Analysis (Parallel)
Launch 5 specialized analyses simultaneously:

**Task C - Forensic Analysis:**
```
Use forensic-analyzer skill to assess:
- Earnings quality (OCF vs profit, accruals)
- Cash conversion patterns
- Working capital deterioration  
- Management credibility
Output: /tmp/forensic_analysis.json with quality scores
```

**Task D - Guidance Tracking:**
```
Use guidance-tracker skill to analyze:
- Forward-looking statements extraction
- Confidence level assessment
- Achievability vs track record
- Quarter-over-quarter changes
Output: /tmp/guidance_analysis.json with credibility scores
```

**Task E - Red Flag Detection:**
```
Use red-flag-scanner skill to identify:
- Management evasion patterns
- Competitive threats
- Execution risks
- Strategic concerns
Output: /tmp/red_flags.json with risk scores
```

**Task F - Inflection Point Detection:**
```
Use inflection-detector skill to identify:
- Business trajectory changes
- Growth/margin inflection signals
- Competitive position shifts
- Strategic turning points
Output: /tmp/inflection_analysis.json with trajectory assessment
```

**Task G - Financial Modeling:**
```
Use financial-modeler skill to create:
- Bull/Bear/Normal scenarios (incorporating inflection insights)
- Multiple valuation methods (PE, EV/EBITDA, DCF)
- Current price integration
- Risk-adjusted price targets
Output: /tmp/financial_model.json with valuations
```

### Phase 3: Integration & Final Analysis
Synthesize all analyses into comprehensive investment report.

## Master Analysis Output

### Executive Summary
```
COMPREHENSIVE CONCALL ANALYSIS
=============================

Company: TCS | Current Price: ₹2,558 | Date: Q3 FY26

INVESTMENT THESIS:
- Earnings Quality: 6.2/10 (Moderate - cash conversion concerns)
- Guidance Credibility: 6.6/10 (Moderate - some downgrades)  
- Red Flag Score: 70/100 (High - execution and competitive risks)
- Fair Value Range: ₹2,000 - ₹3,190 (Bear to Bull scenarios)

RISK-ADJUSTED TARGET: ₹2,180 (-15% from current)
RECOMMENDATION: HOLD (Limited upside, moderate risks)
```

### Integrated Risk Assessment
| Risk Category | Score | Key Issues | Valuation Impact |
|---------------|-------|------------|------------------|
| **Forensic** | 6.2/10 | Cash conversion 0.72, DSO +8 days | -10% discount |
| **Guidance** | 6.6/10 | Revenue guidance cut, margin pressure | -5% discount |
| **Red Flags** | 70/100 | Management evasion, competitive threats | -15% discount |
| **Inflection** | 75% confidence | Early acceleration phase detected | +20% premium |
| **Net Impact** | **MEDIUM** | **Risks offset by inflection potential** | **-10% total** |

### Financial Model Summary
| Scenario | Revenue Growth | EBITDA Margin | EPS | PE | Target | Probability |
|----------|----------------|---------------|-----|----|---------|-----------| 
| **Bull** | 15% | 29% | ₹145 | 22x | ₹3,190 | 20% |
| **Normal** | 9% | 27% | ₹135 | 19x | ₹2,565 | 45% |
| **Bear** | 5% | 25% | ₹125 | 16x | ₹2,000 | 35% |

**Probability-Weighted Fair Value:** ₹2,581  
**Risk-Adjusted Target:** ₹2,180 (-15% discount)  
**Current Price:** ₹2,558  
**Implied Return:** -15% (Downside risk)

### Key Investment Insights

#### Strengths Identified
- Strong market position in IT services
- Healthy cash generation despite quality concerns
- Diversified revenue streams across geographies
- Management has reasonable track record (70% accuracy)

#### Critical Concerns  
- **Earnings Quality**: Cash conversion deteriorating (0.72 vs >0.8 healthy)
- **Working Capital**: DSO increased 8 days, inventory growth outpacing revenue
- **Guidance Cuts**: Revenue expectations lowered from 12-15% to 8-10%
- **Management Evasion**: Dodged key questions on margin pressure

#### Inflection Point Analysis
**Detected Inflection**: Early Revenue Acceleration (75% confidence)
- **Timeline**: 2-3 quarters for full realization
- **Drivers**: New product traction, market share gains, pricing power recovery
- **Stock Impact**: Potential +40-60% if inflection materializes

**Positive Catalysts:**
- New product launches exceeding expectations
- Operating leverage from volume growth  
- Technology leadership in AI/automation
- Market consolidation opportunities

**Key Risks:**  
- Execution risk on new product rollout
- Competitive response to market share gains
- Timeline extension reducing investor patience
- False signal risk if fundamentals deteriorate

### Action Plan & Monitoring

#### Immediate Actions
1. **Investigate Further**: Receivables aging and collection patterns
2. **Monitor Closely**: Working capital trends and cash conversion  
3. **Reassess Valuation**: Apply 15% discount for quality/execution concerns
4. **Position Size**: Reduce to underweight given risk-reward profile

#### Key Monitoring Metrics
- **Quarterly**: Cash conversion ratio, DSO trends, guidance accuracy
- **Monthly**: Competitive positioning, management commentary tone
- **Weekly**: Stock price vs risk-adjusted target range

#### Decision Framework
- **Buy Signal**: Risk score <40, earnings quality >7, price <₹2,000
- **Hold Range**: Current position, monitor for improvement/deterioration  
- **Sell Signal**: Risk score >80, earnings quality <5, execution failures

## Orchestration Workflow

### Step 1: Trigger Detection
Automatically activates when user:
- Uploads conference call transcript
- Asks for "complete concall analysis"
- Requests "comprehensive earnings analysis"
- Mentions "Bull/Bear scenarios with red flags"

### Step 2: Parallel Execution
```bash
# Launch all 4 specialized skills simultaneously
Task forensic-analyzer: Assess earnings quality and cash conversion
Task guidance-tracker: Analyze management credibility and guidance changes  
Task red-flag-scanner: Detect operational and strategic risks
Task financial-modeler: Build scenarios and calculate valuations
```

### Step 3: Integration Logic
```python
# Combine all analyses with weighted scoring
forensic_weight = 0.3  # Earnings quality critical
guidance_weight = 0.25 # Management credibility important  
red_flags_weight = 0.25 # Risk assessment crucial
valuation_weight = 0.2  # Price target calculation

# Calculate risk-adjusted fair value
base_valuation = financial_model.probability_weighted_value
risk_discount = calculate_total_discount(forensic, guidance, red_flags)
final_target = base_valuation * (1 - risk_discount)
```

### Step 4: Investment Recommendation
Generate final buy/hold/sell recommendation with:
- Clear price target with upside/downside
- Key risks and catalysts highlighted
- Monitoring plan and decision triggers
- Position sizing recommendations

## Integration Benefits

### Comprehensive Coverage
- **Forensic**: Accounting quality and manipulation detection
- **Guidance**: Management credibility and promise tracking
- **Red Flags**: Operational and strategic risk identification
- **Inflection**: Business trajectory changes and turning points
- **Financial**: Scenario-based valuation with current price integration

### Risk-Adjusted Approach
- Each skill contributes risk assessment
- Total discount applied based on severity
- Probability-weighted scenarios account for uncertainty
- Clear decision framework with objective triggers

### Institutional Quality
- Multi-dimensional analysis like professional research
- Quantified risk scores and confidence levels
- Systematic approach reducing analyst bias
- Comprehensive documentation for investment committee

This orchestrator provides fund-manager quality analysis by coordinating specialized skills for complete conference call evaluation.