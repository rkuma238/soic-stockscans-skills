---
name: soic-stage-analyzer
description: "Analyzes technical and fundamental alignment using SOIC's (Stan Weinstein) 4-Stage framework to detect accumulation, momentum, distribution, and value traps using 30-40 day delivery % tracking."
type: ATOMIC
version: 2.0.0
inputs:
  - symbol: string
  - price_data: object
outputs:
  - stage_rating: string
  - delivery_microstructure: object
  - Weinstein_stage: string
---

# SOIC 4-Stage & Delivery Microstructure Analyzer

Combines Stan Weinstein's 4-Stage Technical Framework (Stage 1 Accumulation, Stage 2 Markup, Stage 3 Distribution, Stage 4 Capitulation) with **30-40 Day Delivery Percentage % Microstructure Analysis** from `delivery-volume-analyzer`.

---

## Delivery % Confirmation Rules for Stan Weinstein Stages

1. **Stage 1 (Base Accumulation)**: Average Delivery $\% \ge 48\%$. High delivery on quiet, narrow-range days indicates smart money accumulation.
2. **Stage 2 (Markup / Breakout)**: Breakout above resistance accompanied by Delivery $\% \ge 55\%$ and $2\times$ volume expansion confirms genuine Stage 2 markup.
3. **Stage 3 (Distribution Top)**: High volume, wide price swings, and falling Delivery $\% < 25\%$ signal institutional distribution and retail churn.
4. **Stage 4 (Capitulation / Markdown)**: High delivery percentage on down days confirms institutional liquidation.

---

## Output
Return `stage_rating`, `delivery_microstructure`, and `Weinstein_stage`.
