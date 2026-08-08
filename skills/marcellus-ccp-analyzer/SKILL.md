---
name: marcellus-ccp-analyzer
description: "Quantitative ATOMIC skill that runs Saurabh Mukherjea's 'Diamonds in the Dust' & Coffee Can Investing Framework: 10-Yr Twin Filter (Sales >10% & ROCE >15%), Accounting Purity Audit, Incremental ROCE (iROCE), and Reinvestment Efficiency."
type: ATOMIC
version: 3.0.0
inputs:
  - company_data: object
outputs:
  - ccp_qualified: boolean
  - ccp_analysis_markdown: string
  - coffee_can_rating: string
  - iroce_percentage: string
tool_dependencies: []
---

# Marcellus Coffee Can & "Diamonds in the Dust" Analyzer

Rigorously applies Saurabh Mukherjea's "Diamonds in the Dust" and Coffee Can Investing framework to evaluate 10-year quantitative compounding consistency, accounting purity, pricing power, and incremental return on capital (iROCE).

---

## 1. The 10-Year Twin Filter Test (MANDATORY HURDLE MATRIX)

Evaluate historical multi-year records to determine if the company has met **BOTH** conditions consistently for 10 consecutive years (or all available listed years):
- **Revenue Growth Filter:** $> 10\%$ YoY growth every single fiscal year.
- **Return on Capital Employed (ROCE / ROE):** $> 15\%$ absolute ROCE every single fiscal year.

#### Twin Filter Audit Table:

| Fiscal Year | Gross Sales (₹ Cr) | Sales YoY % ($\ge 10\%$) | ROCE / ROE % ($\ge 15\%$) | Twin Filter Status |
| :--- | :---: | :---: | :---: | :---: |
| **Year T-9** | `{Sales_9}` | `{Sales_YoY_9}%` | `{ROCE_9}%` | 🟢 PASS / 🔴 FAIL |
| **Year T-8** | `{Sales_8}` | `{Sales_YoY_8}%` | `{ROCE_8}%` | 🟢 PASS / 🔴 FAIL |
| **Year T-7** | `{Sales_7}` | `{Sales_YoY_7}%` | `{ROCE_7}%` | 🟢 PASS / 🔴 FAIL |
| **Year T-6** | `{Sales_6}` | `{Sales_YoY_6}%` | `{ROCE_6}%` | 🟢 PASS / 🔴 FAIL |
| **Year T-5** | `{Sales_5}` | `{Sales_YoY_5}%` | `{ROCE_5}%` | 🟢 PASS / 🔴 FAIL |
| **Year T-4** | `{Sales_4}` | `{Sales_YoY_4}%` | `{ROCE_4}%` | 🟢 PASS / 🔴 FAIL |
| **Year T-3** | `{Sales_3}` | `{Sales_YoY_3}%` | `{ROCE_3}%` | 🟢 PASS / 🔴 FAIL |
| **Year T-2** | `{Sales_2}` | `{Sales_YoY_2}%` | `{ROCE_2}%` | 🟢 PASS / 🔴 FAIL |
| **Year T-1** | `{Sales_1}` | `{Sales_YoY_1}%` | `{ROCE_1}%` | 🟢 PASS / 🔴 FAIL |
| **Current Year** | `{Sales_0}` | `{Sales_YoY_0}%` | `{ROCE_0}%` | 🟢 PASS / 🔴 FAIL |

---

## 2. Accounting Purity & Capital Allocation Audit (Diamonds in the Dust)

1. **Cash Conversion Efficiency**: 10-Year Cumulative CFO to EBITDA Ratio $> 75\%$ (Proves earnings represent real cash).
2. **Capital Misallocation Check**: Zero investments in unrelated real estate, subsidizing promoter entities, or speculative treasury bets.
3. **Promoter Remuneration & Pledging**: Promoter salary $< 5\%$ of Net Profit; Zero promoter share pledging.

---

## 3. Incremental ROCE (iROCE) & Reinvestment Runway

$$\text{Incremental ROCE (iROCE)} = \frac{\text{Change in EBIT over 5 Years}}{\text{Cumulative Capital Reinvested over 5 Years}}$$

- **iROCE $> 20\%$**: Ultra-high compounding engine (creates massive economic value).
- **iROCE $15–20\%$**: High quality compounder.
- **iROCE $< 15\%$**: Capital destruction / commoditized growth.

---

## 4. Coffee Can Classification Verdict

- **`COFFEE CAN COMPOUNDER`**: Passes 10-Yr Twin Filter + Clean Forensic Score + iROCE $> 20\%$.
- **`EMERGING COMPOUNDER`**: Passes 5-Yr Filter with expanding ROCE & clean forensics.
- **`COMMODITIZED / CYCLICAL TRAP`**: Fails ROCE or Sales growth filter.

---

## Output
Return `ccp_qualified` (boolean), `coffee_can_rating`, `iroce_percentage`, and detailed `ccp_analysis_markdown`.
