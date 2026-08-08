---
name: sector-kpi-analyzer
description: "Exhaustive sector and sub-sector KPI framework for India and US markets. Covers 30+ sectors and 80+ sub-segments. Triggered after company-type-classifier with sector and sub_sector inputs."
type: ATOMIC
version: 4.0.0
children: []
inputs:
  - company_data: object
  - sector: string
  - sub_sector: string
outputs:
  - sector_kpis: object
  - industry_benchmarks: object
---

# Exhaustive Sector & Sub-Sector KPI Analyzer

Defines the explicit domain KPIs and operational metrics across 30+ sectors and 80+ sub-sectors.

---

## Sector KPI Framework Index

### 1. Healthcare & Pharma
- **APIs & CDMO**: R&D % of sales, FTE headcount, DMF/ANDA filings, USFDA EIR inspection status, active Phase I/II/III molecules, reactor capacity (KL), asset turnover.
- **Hospitals**: ARPOB (Average Revenue Per Occupied Bed), Occupancy Rate %, Bed Count, ALOS (Average Length of Stay), Payor Mix (Self-pay vs Insurance).

### 2. Banking, NBFCs, HFCs & Fintech
- **Banks & NBFCs**: NII, NIM %, GNPA %, NNPA %, PCR %, Slippage Ratio %, CASA %, Cost-to-Income %, ROA %, CRAR %, Stage 3 assets.
- **Payment Infrastructure & Merchant Acquiring**: Gross Payment Volume (GPV), Net Take Rate %, Transaction Failure & Fraud Rate %, API Conversion %, Chargeback Dispute Rate %, Gross Transaction Volume.


### 3. Technology & IT Services
- **IT Services**: Deal Win TCV ($M), Attrition Rate %, Utilization Rate %, Billing Rate ($/hr), Onsite/Offshore Mix, Top 5/10 Client Concentration.
- **SaaS & Software Platforms**: Annual Recurring Revenue (ARR), Net Revenue Retention (NRR %), Customer Lifetime Value (CLTV), Customer Acquisition Cost (CAC), CLTV-to-CAC Ratio, Gross Margin %, Rule of 40 %, Magic Number Growth Metric, Subscription Revenue % of Total, Payback Period in Months.

### 4. Consumer, FMCG & Retail
- **FMCG**: Volume Growth % vs Realisation Growth %, Rural vs Urban Growth %, Gross Margin %, Distribution Reach (Direct Outlets).
- **Retail & QSR**: SSSG (Same Store Sales Growth %), Store Count, ADS (Average Daily Sales per store), Store-level EBITDA Margin %, Footfalls.
- **Footwear Manufacturing & Retail**: Average Selling Price (ASP) Trends, DTC vs Wholesale Mix %, Gross Margin %, Adjusted EBITDA Margin %, In-house Manufacturing %, Core Silhouettes vs Seasonal Styles Ratio, Discount Avoidance Rate.

### 5. Auto & Auto Ancillaries
- **Auto OEMs**: Volume Sales (Units), Realisation Per Vehicle, Order Backlog, EV Mix %, Capacity Utilization %.
- **Auto Ancillaries**: Content Per Vehicle (₹), EV-Agnostic Revenue %, OEM vs Aftermarket vs Export Mix.
- **Electric Vehicles & Clean Energy Solutions**: Vehicle Delivery Volume Growth %, Automotive Gross Margin Ex-Regulatory Credits %, Energy Storage Deployment GWh & Storage Gross Margin %, Autonomous Driving Subscription Take Rate %, CapEx to Free Cash Flow Allocation %.

### 6. Capital Goods, EPC & Industrial Manufacturing
- **Capital Goods / EPC**: Order Book (₹ Cr), Order Intake, Order Book to Bill Ratio (x), Execution Timeline, Working Capital / Sales %.

### 7. Real Estate & Building Materials
- **Real Estate**: Pre-sales (Area & Value), Collections (₹ Cr), Realisation (₹/sqft), Unlaunched Land Bank, Debt/Pre-sales.
- **Tiles / Pipes / Cement**: Freight Cost per Ton, Realisation per Bag/Ton, Fuel Mix (Petcoke vs Coal), Capacity Utilization %.

### 8. Logistics & Aviation
- **Logistics**: Tonnage Volume, Yield per Ton/Km, Network Fleet Count, 3PL vs Express Mix.
- **Aviation**: PLF (Passenger Load Factor %), RASK (Revenue per Available Seat Km), CASK (Cost per Available Seat Km), Yield per Passenger.

### 9. Digital Platforms & Creator Economy
- **Creator Economy & Publishing Platforms**: GMV (Gross Merchandise Volume), Net Platform Revenue Fee %, ARR Growth %, MAU (Monthly Active Users), Free-to-Paid Conversion Rate %, Average Subscriptions per Reader, Creator Earnings Distribution (Top Tier vs Mid Tier), Paid Churn Rate %, Internal Recommendation Network Effects %.

### 10. AI & Compute Infrastructure
- **AI & Semiconductor Compute**: Q4/Q1 Revenue YoY & QoQ Growth %, Forward vs Trailing P/E Multiples, Big Tech CapEx Trends (Hyperscalers), Foundation Model ARR Growth (OpenAI/Anthropic), Compute Scarcity Index, Token Generation Volume, Agentic Workflows (e.g., NeMo-CLAW), Hyperscaler CapEx to FCF Allocation %.

---

### 11. Renewable Energy Storage & Smart Grids
- **Renewable Energy Storage & Smart Grids**: Storage Capacity Deployment MWh, Inverter Efficiency & Microinverter Shipments, Grid Interaction Take-Rate %, System Level Levelized Cost of Storage LCOS.

---

## Output
Return structured `sector_kpis` and `industry_benchmarks` for the evaluated target company.









