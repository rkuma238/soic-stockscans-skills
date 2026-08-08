---
name: soic-intrinsic-analyzer
description: "Specialized ATOMIC skill that takes a base quantitative RA report and transforms it using the profound 5-point SOIC Intrinsic Compounding framework (Moats, ROCE, Optionality)."
type: ATOMIC
version: 2.0.0
inputs:
  - base_report_markdown: string
outputs:
  - soic_report_markdown: string
  - optionality_matrix: object
tool_dependencies: []
---

# SOIC Intrinsic & Optionality Analyzer (ATOMIC)

Applies the deep-dive qualitative framework of the School of Intrinsic Compounding to the quantitative data extracted by `sector-kpi-analyzer` and `ra-report-synthesizer`.

---

## The Mandatory Business & Growth Optionality Framework (MANDATORY)

Deconstruct and evaluate the non-linear, asymmetric **Growth Optionality** across 5 distinct dimensions:

### 1. Molecule / Product Pipeline Optionality
- **Phase III / Late-Stage Clinical Candidates**: Number of molecules in Phase III trials transitioning to commercial supply contracts ($30–80M+ revenue potential per commercialized molecule).
- **High-Niche Platforms**: Peptide synthesis, GLP-1 intermediates, ADC (Antibody-Drug Conjugates), continuous flow chemistry.

### 2. Capacity & Infrastructure Land Bank Optionality
- **Unallocated Land Reserves**: Greenfield land bank availability for unannounced Phase V/VI modular expansions.
- **Pilot Plant Scalability**: Multipurpose pilot plant blocks ready to convert to commercial scale upon client FDA approval without waiting for greenfield approval cycles.

### 3. Geographic & Supply Chain Diversification Optionality (China+1)
- **Global Innovator Dual-Sourcing**: Contracts won as Western innovators shift supply chain dependencies away from Chinese CDMO vendors.
- **Non-US Innovator Expansion**: Penetration into European, Japanese, and South Korean pharmaceutical innovator networks.

### 4. Technology Platform & M&A Optionality
- **Proprietary Process Tech**: Flow chemistry, biocatalysis, high-potency API (HPAPI) isolation platforms.
- **Accretive Bolt-on M&A**: Balance sheet capacity (low D/E < 0.2x) to execute opportunistic bolt-on acquisitions funded by strong operating cash flows.

### 5. Quantified Optionality Matrix & Valuation Kicker

| Optionality Dimension | Current Baseline Status | Unlocked Potential Event | Timeline | Revenue / Margin Kicker Impact | Implied Target Price Impact |
| :--- | :--- | :--- | :---: | :---: | :---: |
| **Pipeline Commercialization** | 12 Phase III Molecules | 2 Molecules FDA Commercialized | FY27E–FY28E | +₹150–250 Cr Revenue (32% OPM) | +₹250 / Share |
| **Bidar Unit-IV Land Bank** | Construction phase | 200 KL Capacity Ramp-up | Q3FY27 | +₹400 Cr Revenue potential | +₹300 / Share |
| **China+1 Dual Sourcing** | 15% European Share | European Big Pharma contract win | FY28E | +₹200 Cr High-margin CDMO | +₹180 / Share |
| **Combined Optionality Kicker**| Base Fair Value: **₹1,850** | All 3 Optionalities Triggered | FY28E | Total PAT expansion to ₹750+ Cr | **Optionality Target: ₹2,400** |

---

## Agent Execution Prompt

```text
You are acting as the lead analyst for the School of Intrinsic Compounding (SOIC).
You must evaluate:
1. Business Moats (Switching Costs, Cost Leadership, Chemistry Integration).
2. Capital Allocation & ROCE Trajectory.
3. Full 5-Pillar Business & Growth Optionality Framework.
4. Promoter Forensics & Walk The Talk Guidance Scorecard.
```
