---
name: soic-variant-perception
description: "Specialized ATOMIC skill that identifies the variant perception (how our view differs from the market consensus) for any company under analysis. Focuses on identifying structural re-rating/de-rating triggers such as operating leverage, capacity inflections, product-mix premiumization, or segmental de-mergers."
type: ATOMIC
version: 1.0.0
inputs:
  - company_symbol: string
  - market_consensus: string
  - variant_triggers: array
outputs:
  - variant_perception_matrix: object
  - analysis_narrative: string
tool_dependencies: []
---

# SOIC Variant Perception Framework (ATOMIC)

This skill evaluates the mismatch between **Market Consensus** (what the crowd believes and is currently priced in) and **Operational Realities** (what the numbers and business developments indicate is about to happen). 

---

## 1. Core Framework Principles
Variant perception exists when your view of a company's future trajectory differs significantly from the consensus, and you have identified a specific, verifiable catalyst (trigger) that will force the market to re-rating or de-rating the stock.

### Common Variant Perception Triggers:
1. **Operating Leverage (The Opex Lag)**:
   - *Consensus*: High cost-to-income or low operating margins are structural.
   - *Variant View*: High expenses are front-loaded investments (e.g., new branches, marketing, R&D) that will flatten, while revenues scale exponentially, expanding the operating profit margin.
2. **Product Mix Shift (The Margin Kicker)**:
   - *Consensus*: Low-margin commodity player.
   - *Variant View*: The company is rapidly scaling high-margin specialty chemicals, CDMO products, premium retail banking services, or value-added segments, driving margin expansion.
3. **Asset Turn & Capacity Inflection**:
   - *Consensus*: Excessive capex is depressing return ratios (ROA/ROCE).
   - *Variant View*: Large capex phase is ending; asset turn is about to double as commercial supply begins, unlocking non-linear revenue growth.
4. **De-mergers & Conglomerate Discount Unlocking**:
   - *Consensus*: Complex structure depresses corporate valuation.
   - *Variant View*: Spinning off a fast-growing specialty subsidiary will list it at pure-play multiples, unlocking hidden value.
5. **Regulatory / Industry Cycle Arbitrage**:
   - *Consensus*: Industry is in down-cycle; company is structural value trap.
   - *Variant View*: Lower-cost producers are gaining market share, or regulatory changes (e.g. risk weight increases) have already been fully absorbed.

---

## 2. Standardized SOIC Variant Perception Matrix

Every analysis report must include a dedicated Variant Perception section containing this structured grid:

| Analysis Dimension | Market Consensus View (Priced In) | Our Variant Perception (Operational Reality) | Specific Re-rating Catalyst / Trigger | Verification Metric |
| :--- | :--- | :--- | :--- | :--- |
| **Growth & Scaling** | Flat or linear growth based on historical trends. | Non-linear inflection due to past capital deployment. | Capacity commercialization / Branch vintage maturation. | Revenue CAGR vs. Capex CAGR |
| **Margins & Profitability**| Depressed margins due to high overheads / raw materials. | Outsized margin expansion as fixed costs are absorbed. | Raw material cooling / Product-mix shift to value-added. | Gross Margins & EBITDA Margins |
| **Return Ratios (ROCE/ROE)**| Subdued return ratios below peer group averages. | Rapid expansion towards top-quartile status. | Leverage normalization / Asset turnover doubling. | ROCE/ROE expansion trajectory |
| **Risk Factors & Forensic** | Elevated risks from control issues or cycle downturns. | Risks are short-term, contained, and fully provisioned. | External audits, independent reviews, or cash recovery. | Provision Coverage Ratio (PCR) / Forensic Scorecard |

---

## 3. Agent Instructions for Report Synthesis

When writing or updating an equity research report:
1. **Explicitly Label**: Create a dedicated `## SOIC Variant Perception Analysis` section.
2. **Contrast Views**: Clearly delineate the consensus view from our proprietary variant view. Do not use generic summaries; utilize specific numerical data (e.g., "Market expects 12% ROE, but branch maturation path implies 15.5% ROE by FY28E").
3. **Identify Triggers**: State the exact catalyst and its timeline (e.g., "Q1FY27 provisions normalization," "Bidar modular block commercialization").
4. **Cite Sources**: Ensure all underlying numbers in the Variant Perception arguments are cross-referenced with live MCP tool outputs (Screener, NSE-BSE, or official annual reports).
