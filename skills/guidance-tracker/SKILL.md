---
name: guidance-tracker
description: Track and analyze management guidance changes, confidence levels, and achievability assessment. Use when analyzing forward-looking statements, comparing guidance across quarters, assessing management credibility, or evaluating guidance realism vs industry benchmarks. Specializes in guidance extraction, confidence analysis, and track record assessment.
---

# Guidance Tracker - Management Promise Analyzer

Specialized analysis of management guidance, forward-looking statements, and credibility assessment based on historical delivery track record.

## Core Guidance Framework

### 1. Guidance Extraction & Classification

#### Hard Guidance (Specific Numbers)
- **Revenue Growth**: "We expect 12-15% revenue growth"
- **Margin Targets**: "EBITDA margin will be 27-29%"  
- **Capex Plans**: "Capex of ₹5,000-6,000 crores"
- **Timeline Specific**: "By Q4 FY26" or "Next 12 months"

#### Soft Guidance (Directional Statements)
- **Qualitative Trends**: "Margins will improve", "Growth will accelerate"
- **Conditional Statements**: "If market conditions remain favorable"
- **Relative Positioning**: "Better than industry", "Outperform peers"

#### Guidance Changes Analysis
- **Upgrades**: Raised from previous quarter
- **Downgrades**: Lowered from previous quarter  
- **New Guidance**: First-time metrics provided
- **Withdrawn**: Previously given, now removed

### 2. Confidence Level Assessment

#### Language Pattern Analysis
**High Confidence Indicators:**
- "Committed to", "Confident of achieving", "Will deliver"
- Specific numbers without hedging
- Shorter timelines with precision

**Medium Confidence Indicators:**  
- "Expect to", "Anticipate", "Believe we can"
- Range guidance (8-10% vs specific 9%)
- Qualified statements with conditions

**Low Confidence Indicators:**
- "Hope to", "May achieve", "Depending on"
- Wide ranges or vague timelines
- Heavy hedging with multiple conditions

#### Confidence Scoring Matrix
| Guidance Type | Language Strength | Timeline Clarity | Confidence Score |
|---------------|-------------------|------------------|------------------|
| Revenue 12-15% | "Committed to" | "FY26" | 8/10 (High) |
| Margin improvement | "Expect" | "Over time" | 5/10 (Medium) |
| Market share gains | "Hope to" | "Eventually" | 3/10 (Low) |

### 3. Achievability Assessment

#### Historical Track Record
- **Guidance Accuracy**: % of guidance met over last 8 quarters
- **Miss Magnitude**: Average deviation when guidance missed
- **Bias Analysis**: Tendency to over-promise or under-promise
- **Seasonal Patterns**: Q4 vs other quarters accuracy

#### Industry Benchmark Comparison
- **Peer Performance**: How guidance compares to industry leaders
- **Market Growth**: Company guidance vs overall market trends
- **Competitive Position**: Market share required for guidance achievement

#### Reality Check Framework
| Guidance Item | Management Target | Industry Benchmark | Achievability |
|---------------|-------------------|-------------------|---------------|
| Revenue Growth | 15% | Industry: 8% | Requires market share gains |
| EBITDA Margin | 29% | Peer avg: 25% | Aggressive, needs cost control |
| Capex | ₹5,000 Cr | Historical: ₹6,500 Cr | Likely underestimated |

### 4. Guidance Evolution Tracking

#### Quarter-over-Quarter Changes
```
Q2 FY26: Revenue growth 12-15%, EBITDA margin 27-29%
Q3 FY26: Revenue growth 8-10%, EBITDA margin 25-27%
Change: Revenue ↓4-5%, Margin ↓2%
Reason: "Market headwinds and cost inflation"
```

#### Confidence Trajectory
- **Increasing Confidence**: Language becoming more assertive
- **Decreasing Confidence**: More hedging and conditions added
- **Consistency**: Stable confidence levels across quarters

## Guidance Analysis Output

### Guidance Comparison Table
| Metric | Previous Quarter | Current Quarter | Change | Confidence | Achievability |
|--------|------------------|-----------------|---------|------------|---------------|
| Revenue Growth | 12-15% | 8-10% | ↓ 4-5% | Medium | Realistic |
| EBITDA Margin | 27-29% | 25-27% | ↓ 2% | Low | Challenging |
| Capex | ₹5,000 Cr | ₹6,000 Cr | ↑ 20% | High | Likely |

### Management Credibility Score
| Component | Score | Weight | Evidence |
|-----------|-------|---------|----------|
| Historical Accuracy | 7/10 | 40% | 70% guidance met (8 quarters) |
| Language Confidence | 6/10 | 25% | Moderate hedging patterns |
| Guidance Stability | 5/10 | 20% | 2 downgrades in 4 quarters |
| External Validation | 8/10 | 15% | Industry trends support |
| **Overall Credibility** | **6.6/10** | **100%** | **MODERATE** |

### Probability Assessment
- **Bull Case** (Guidance exceeded): 20%
- **Base Case** (Guidance achieved): 45%  
- **Bear Case** (Guidance missed): 35%

**Recommended Modeling**: Use 80% of management guidance for conservative estimates

## Analysis Workflow

### Phase 1: Guidance Extraction
```bash
# Extract all forward-looking statements
python scripts/extract_guidance.py transcript.txt --classify-confidence
```

### Phase 2: Historical Comparison  
```bash
# Compare with previous quarters
python scripts/compare_guidance.py current.txt previous.txt --track-changes
```

### Phase 3: Reality Check
```bash
# Assess achievability vs benchmarks  
python scripts/reality_check.py guidance.json financials.json --industry-data
```

## Key Guidance Metrics

### Guidance Quality Indicators
- **Specificity**: Precise numbers vs vague directions
- **Timeline Clarity**: Specific periods vs "over time"
- **Conditionality**: Unconditional vs heavily qualified
- **Consistency**: Stable messaging vs frequent changes

### Track Record Analysis
- **Beat Rate**: % of quarters guidance exceeded
- **Miss Severity**: Average magnitude of misses
- **Revision Frequency**: How often guidance changes
- **Seasonal Bias**: Q4 vs other quarters performance

### Confidence Calibration
- **Language-Performance Correlation**: Do confident statements deliver?
- **Hedging Effectiveness**: Do cautious statements protect?
- **Surprise Patterns**: Consistent beats/misses indicate sandbagging/optimism

## Integration Points

- **Input**: Conference call transcripts, historical guidance data
- **Output**: Guidance changes, confidence scores, achievability assessment
- **Triggers**: "Guidance analysis", "track management promises", "credibility check"
- **Complements**: Feeds into financial modeling and valuation analysis

This skill provides systematic tracking of management guidance to assess credibility and set realistic expectations for financial modeling.