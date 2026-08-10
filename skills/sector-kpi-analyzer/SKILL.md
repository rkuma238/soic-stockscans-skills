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

---

---

---

---
## 🧠 Dynamically Learned Industry KPIs & Concall Benchmarks

### Capital Goods, Defense & Precision Engineering
- This is where First signs of mean reversion emerged due to: i) Order book increased to a Multi Quarter High.
- Post Q1FY27, order book formed a new high and growth reverted back to mean.
- Precision Wires ran at 89% capacity utilisation in FY25 (up from 86%).
- Precision Wires India (PWIL) is India’s largest winding-wire producer by capacity (~55,000 MT/year as of mid-2025, expanding to ~61,000 MT by June 2026).

### QSR, Consumer & Retail
- Those who saw that the core instrumentation franchise never stopped earning 15%+ margins captured the entire re-rating.
- IDFC FIRST Bank is executing a deposit-led growth strategy, with its high-quality savings franchise reducing funding costs and supporting NIM sustainability.
- These are businesses with structural category growth, operating leverage, premiumisation, and expansion into higher-margin adjacencies: Shaily Engineering Plastics has built a proprietary healthcare franchise with drug delivery platforms for insulin, GLP-1 pens, and auto-injectors, positioning it as a preferred device partner for global generic pharmaceutical companies.
- Defending a mature franchise requires reinvestment that compresses margins, and if the growth it buys is low-single-digits, the stock simply cannot compound the way it did from 2010 to 2020.

### Power T&D, Electricals & Transformers
- India is committing on the order of 9 trillion to build out its transmission grid over FY23-32, at the same moment the world is short of transformers, with US lead times stretching to two-to-four years and imports meeting 80% of US power-transformer supply.
- Yet CTC and specialty winding wire are made at scale by only 3-4 qualified Indian players, whose combined specialty capacity is expanding from roughly 45 kt to 77 kt by FY28 with plants already running near-full, protected by five-to-seven-year end-utility qualification cycles, and pinched further by parallel shortages of insulators, grain-oriented electrical steel and bushings.
- The demand is genuinely structural and five-headed, the T&D capex supercycle, renewables evacuation, data centers, EV/electrification, and an export pull from a global transformer shortage.
- The questions worth watching: who clears the qualification barriers (especially HVDC), who successfully integrates backward into greener/cheaper copper, and who converts announced capacity into *utilised, value-added* tonnes rather than an idle nameplate.

### Recycling, Metals & Industrial Circularity
- India’s 2025 Union Budget eliminated the basic customs duty entirely on copper scrap and waste (down from 5% in 2021, to 2.5%, to nil) explicitly to boost domestic recycling capacity for the EV and electronics sectors, a direct tailwind for the recyclers.
- Also other recyclers seeing this tailwind have announced a big capex in copper recycling like Pondy Oxides and Gravita India.
- Total Supa capex is ~₹340 crore across both phases (₹220 crore Phase 1 + ₹120 crore Phase 2, the latter including a ₹100 million copper-recycling line).
- We recently met the management of Gravita India and here are the key insights from that call on how the future growth would look like for the company 1.

### Auto Components & Commercial Vehicles
- MCX aluminium alloy contract may be structurally blocked by a large OEM.
- This content growth is the tide that lifts sophisticated Tier-1 suppliers like Motherson even when the unit volume tide is not rising.
- Drivers of Growth: The Irillic Acquisition: Motherson bought a company that pioneered India’s first real-time ICG-based fluorescence imaging technology , which is used for micro-vascular and lymphatic visualization during open and laparoscopic surgeries.
- Drivers of Growth: Captive Scalability: They have currently consolidated 60% of Motherson’s internal third-party logistics.

### Specialty & Aroma Chemicals
- Please think independently before taking buying and selling decision Privi is not a commodity aroma-chemical maker that happens to have good margins rather it is a vertically integrated waste-to-wealth platform that buys other industries’ effluent (kraft-pulp turpentine, kerosene side-streams, corn-cob) at near-scrap prices and chemically climbs the value chain on every single stream, main product and by-product.
- Privi has literally presented its growth and EBITDA-margin slides to the #2 in the hierarchy at IFF to a customer whose own EBITDA margin is ~21–22% and said, in effect, “I supply you, and I still make 25%, because I am extremely efficient and I keep rediscovering my own processes.” This is the right way to underwrite the margin durability.
- Privi is a fully integrated, large-volume producer of all three, that integration is the margin.
- Five years ago BASF’s commercial head literally called and asked “why are you doing this?” Today Privi contracts this product with multiple large buyers and has out-competed BASF despite BASF’s backward integration.

### Pharma, API & CDMO
- Theme 5 - Pharma’s CDMO/CRDMO Pivot The contract development and manufacturing organisation (CDMO) segment has emerged as the single most exciting structural growth pocket in Indian pharmaceuticals.
- Several structural forces are converging to make this an unusually durable growth theme: The China+1 diversification in pharma supply chains is accelerating, catalysed by the US BIOSECURE Act (a bipartisan initiative prompting pharmaceutical companies to re-evaluate outsourcing to Chinese CDMOs).
- With EBITDA margins of 25-35% (versus 15-20% for traditional generic pharma), lower marketing costs, and dollar-denominated revenues, CDMOs generate structurally superior RoCE trajectories once initial capacity investments are absorbed.
- Laurus Labs is executing its CDMO pivot after years of investment in capability and capacity.

### Semiconductors & Electronics Manufacturing
- Input cost inflation (crude-linked inputs, packaging, gold prices) can compress margins if premiumisation momentum stalls.
- The MDF (Medium Density Fibreboard) segment, in particular, is seeing robust industry growth of over 20%, driven by substitution of lower-end plywood, new usage in packaging, and increasing modular furniture adoption.
- MDF industry growth continues at over 20%, driven by increasing substitution of lower-end plywood and new usage categories such as boxes, trays, and gift packaging.
- The IML technology provides differentiation and higher margins versus commodity packaging.

### General Industrial & Corporate KPIs
- But what makes this cycle different from previous ones and what’s really driving the re-rating is that the quality of growth has fundamentally changed.
- This isn’t just topline growth anymore.
- Its topline growth is accompanied by a sustained EBITDA margin expansion cycle, something the sector hasn’t seen since the pre-2018 golden era.
- Getting back to the discussion, So Consider a few data points from the companies that reported this quarter to comprehend what I am trying to explain above: Zydus Lifesciences delivered consolidated revenues of 27,150 Cr for FY26, up 17% YoY, with an EBITDA margin of 31.2% which is the highest-ever operating margin in the company’s history.

### Logistics, Shipping & Supply Chain
- Companies that maintained customer relationships, invested in capacity, and kept shipping volumes were running on a treadmill growing units sold but seeing realizations collapse due to Chinese dumping and global oversupply.
- By fully integrating its R&D, manufacturing, and business development teams, Navin acts as an indispensable solution provider, driving process improvements and securing higher volume commitments in its partners’ long-term supply chain roadmaps.
- While Navin has worked hard to de-risk its supply chain by signing long-term contracts with South African miners, China still controls a massive portion of the world’s fluorspar supply.
- This improvement created an efficiency paradox : Faster trips and higher utilisation Fewer trucks needed to move the same cargo Better profitability for surviving fleets Suppressed headline CV volumes This is why CV volumes stayed muted even as freight demand improved.

### Banking, NBFCs & Financial Services
- The positioning is genuinely unique: Hester is the world’s largest supplier of PPR (Peste des Petits Ruminants) vaccine and is the designated supplier to the WOAH (World Organisation for Animal Health) vaccine bank.
- What emerged from this crisis was the RBI’s Malegam Committee, which created the regulated NBFC-MFI category, introduced interest rate caps and borrower-level lending limits, and mandated ethical recovery practices; the regulatory foundation that still governs the sector today.
- Disbursement growth slowed sharply as lenders conserved liquidity.
- In bust years, credit costs spike to 3–5% of AUM, erasing all margin.

### General Industrial & Operational KPIs
- This transformation is anchored in its “3P” framework , which acts as the blueprint for its sustainable business model: Product: Building a diverse, high-value portfolio spanning fluorine-based intermediates, specialty chemicals, inorganic chemicals, and contract research services.
- R32 (The Current Growth Driver): This is the current star product of the division.
- Ultimately, the HPP division utilizes massive, continuous-process industrial plants running at optimal capacity to manufacture these gases and salts, selling them in bulk volumes to domestic and international buyers to capture higher realisations and volume growth.
- If one of these molecules proves to be highly successful and the customer requires massive commercial volumes, the company then transitions its production out of the MPP and builds a massive “dedicated plant” specifically tailored to manufacture that single product.

### Pipes, Fittings & Plastic Products
- This allows them to capture massive, stable volumes from successful drugs while continuously incubating new clinical pipeline projects for future growth.
- As the remaining capacity is validated and filled with new pipeline molecules, this plant will deliver massive incremental top-line growth.

### Ceramics, Tiles & Sanitaryware
- The growth slowed down sharply due to a prolonged inventory correction, weak farmer sentiment, Agri downcycle, volatile commodity prices, & higher interest rates.
- Better Risk-Reward at the Same Point in the Cycle In early-to-mid recovery: OEMs look optically cheap but earnings are volatile Component makers show steady margin expansion and balance sheet strength This asymmetry makes components the cleaner, lower-risk way to play a CV recovery .

### Aerospace, SpaceTech & Satellite Communications
- Capex & Growth Orientation Recent capacity additions and modernisation efforts position Jamna for: Higher payload platforms Export opportunities New-age CVs (including buses and EV platforms) Importantly, Jamna’s growth does not require a boom cycle.
