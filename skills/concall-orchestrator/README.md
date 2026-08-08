# Conference Call Analysis Suite - 5 Specialized Skills

A comprehensive suite of specialized skills for institutional-grade conference call analysis, providing forensic accounting analysis, guidance tracking, financial modeling, and operational risk detection.

## Skill Architecture

### 🎯 **Master Orchestrator**
**`concall-orchestrator`** - Coordinates all specialized skills for complete analysis
- Manages parallel execution of 4 specialized analyses
- Integrates results into comprehensive investment recommendation
- Provides risk-adjusted valuations and decision framework

### 🔍 **Specialized Analysis Skills**

#### 1. **`forensic-analyzer`** - Earnings Quality Detective
- **Focus**: Accounting manipulation detection, earnings quality assessment
- **Key Outputs**: Cash conversion analysis, accrual quality, working capital forensics
- **Triggers**: "Forensic analysis", "earnings quality", "cash flow analysis"

#### 2. **`guidance-tracker`** - Management Promise Analyzer  
- **Focus**: Forward guidance extraction, credibility assessment, achievability analysis
- **Key Outputs**: Guidance changes, confidence scores, track record analysis
- **Triggers**: "Guidance analysis", "management credibility", "track record"

#### 3. **`financial-modeler`** - Scenario & Valuation Engine
- **Focus**: Bull/Bear/Normal scenarios, multiple valuations, price targets
- **Key Outputs**: 3-scenario models, PE/EV/DCF valuations, risk-adjusted targets
- **Triggers**: "Financial model", "valuation", "price target", "scenarios"

#### 4. **`red-flag-scanner`** - Operational Risk Detector
- **Focus**: Management evasion, competitive threats, execution risks
- **Key Outputs**: Risk scores, threat assessment, management quality analysis  
- **Triggers**: "Red flags", "risk assessment", "competitive analysis"

## Complete Analysis Workflow

### Phase 1: Data Preparation (Parallel)
```
📄 Extract transcript → /tmp/transcript.txt
💰 Fetch financials → /tmp/financials.json (with current price)
```

### Phase 2: Specialized Analysis (Parallel)
```
🔍 Forensic Analysis → Earnings quality score, cash conversion issues
📊 Guidance Tracking → Credibility assessment, achievability analysis  
🚨 Red Flag Scanning → Risk scores, competitive/operational threats
📈 Financial Modeling → Bull/Bear/Normal scenarios with valuations
```

### Phase 3: Integration & Decision
```
🎯 Master Analysis → Risk-adjusted price target, investment recommendation
```

## Sample Complete Output

```
COMPREHENSIVE CONCALL ANALYSIS - TCS Q3 FY26
===========================================

Current Price: ₹2,558 | Analysis Date: Mar 8, 2026

EXECUTIVE SUMMARY:
Moderate earnings quality with guidance downgrades and execution risks.
Multiple red flags warrant cautious approach despite reasonable valuation.

INTEGRATED RISK ASSESSMENT:
- Forensic Score: 6.2/10 (Cash conversion 0.72, working capital deterioration)
- Guidance Credibility: 6.6/10 (Revenue guidance cut, margin pressure)  
- Red Flag Score: 70/100 (Management evasion, competitive threats)
- Overall Risk: MEDIUM-HIGH (Multiple concerns across areas)

FINANCIAL MODEL & VALUATION:
┌──────────┬────────────┬─────────────┬─────┬────┬─────────┬─────────────┐
│ Scenario │ Rev Growth │ EBITDA Marg │ EPS │ PE │ Target  │ Probability │
├──────────┼────────────┼─────────────┼─────┼────┼─────────┼─────────────┤
│ Bull     │ 15%        │ 29%         │ ₹145│ 22x│ ₹3,190  │ 20%         │
│ Normal   │ 9%         │ 27%         │ ₹135│ 19x│ ₹2,565  │ 45%         │
│ Bear     │ 5%         │ 25%         │ ₹125│ 16x│ ₹2,000  │ 35%         │
└──────────┴────────────┴─────────────┴─────┴────┴─────────┴─────────────┘

RISK-ADJUSTED VALUATION:
- Probability-Weighted Fair Value: ₹2,581
- Risk Discount (25%): -₹401  
- Risk-Adjusted Target: ₹2,180
- Downside from Current: -15%

RECOMMENDATION: HOLD
- Limited upside potential with significant risk factors
- Monitor working capital trends and competitive position
- Reassess if risk score improves below 50 or price drops below ₹2,000
```

## Usage Examples

### Complete Analysis
```
"Analyze this TCS earnings call with Bull/Bear scenarios and red flags"
→ Triggers concall-orchestrator → Runs all 4 skills → Integrated report
```

### Specialized Analysis  
```
"Check earnings quality for this transcript" → forensic-analyzer
"Track guidance changes vs last quarter" → guidance-tracker  
"Build financial model with scenarios" → financial-modeler
"Scan for management and competitive red flags" → red-flag-scanner
```

## Key Benefits

### 🎯 **Comprehensive Coverage**
- **Forensic**: Detects accounting manipulation and quality issues
- **Guidance**: Assesses management credibility and promise delivery
- **Modeling**: Provides scenario-based valuations with current price
- **Red Flags**: Identifies operational and strategic risks

### ⚡ **Token Efficiency**  
- Each skill specialized for specific analysis type
- Parallel execution reduces total processing time
- Focused outputs avoid redundant analysis
- Structured data integration vs lengthy reports

### 🏛️ **Institutional Grade**
- Multi-dimensional risk assessment
- Quantified scores and confidence levels  
- Systematic approach reducing bias
- Professional-quality investment recommendations

### 🔄 **Flexible Usage**
- Use individual skills for focused analysis
- Use orchestrator for comprehensive evaluation
- Modular design allows skill improvements
- Integration with screener-financial-data for context

## Installation & Setup

All skills are ready to use in `~/.cursor/skills/`:
- `concall-orchestrator/` - Master coordinator
- `forensic-analyzer/` - Earnings quality analysis
- `guidance-tracker/` - Management credibility assessment  
- `financial-modeler/` - Scenario modeling & valuation
- `red-flag-scanner/` - Operational risk detection

Each skill automatically activates based on user prompts and provides specialized analysis for comprehensive conference call evaluation.