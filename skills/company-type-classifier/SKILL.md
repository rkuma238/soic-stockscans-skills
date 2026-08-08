---
name: company-type-classifier
description: "Classifies a company into entity type, sector, sub-sector, and cyclicality. Covers India and US markets across 30+ sectors and 80+ sub-sectors."
type: ATOMIC
version: 4.2.0
children: []
inputs:
  - company_data: object
  - company_name: string
  - market: string
outputs:
  - company_type: string
  - sector: string
  - sub_sector: string
  - cyclicality: string
  - market: string
  - classification_confidence: string
  - classification_reason: string
---

# Company Type, Sector & Sub-Sector Classifier (India + US)

Three-level classification: **entity type → sector → sub-sector**.

> `market` input accepts `"india"`, `"us"`, or `"auto"` (default — inferred from data).

---

## Level 1 — Entity Type → `company_type`

| Type | Key Signals |
|---|---|
| `bank` | NII, Gross Advances, Deposits, GNPA, CASA, CRR/SLR, RBI Banking License / US Fed Member |
| `nbfc` | AUM, Disbursements, Stage 1/2/3, Gearing, Co-lending, RBI-NBFC / US non-bank finance |
| `insurance` | Gross Written Premium (GWP), Claims Ratio, Combined Ratio, Solvency Ratio; IRDAI / NAIC regulated |
| `corporate` | All others — default |

---

## Level 2 + 3 — Sector & Sub-Sector

---

### INDIA — Financial Sectors

#### `insurance`
| Sub-Sector | Examples |
|---|---|
| `insurance-life` | LIC, HDFC Life, SBI Life, Max Life, ICICI Pru Life |
| `insurance-general` | New India, ICICI Lombard, Star Health, Go Digit |
| `insurance-health` | Niva Bupa, Star Health (standalone health insurer) |
| `insurance-reinsurance` | GIC Re, New India (re-insurance book) |

#### `fintech-exchange` (India)
| Sub-Sector | Examples |
|---|---|
| `exchange-stock` | NSE, BSE |
| `exchange-commodity` | MCX, NCDEX |
| `depository` | CDSL, NSDL |
| `fintech-payments` | One97 (Paytm), PhonePe (unlisted), Infibeam, PayU |
| `fintech-insurance-broker` | PB Fintech (PolicyBazaar), Coverfox |
| `fintech-lending` | Lendingkart, Aye Finance (unlisted) |

#### `nbfc`
| Sub-Sector | Key Players |
|---|---|
| `nbfc-microfinance` | CreditAccess Grameen, Spandana Sphoorty, Ujjivan, Fusion |
| `nbfc-housing-hfc` | LIC Housing, PNB Housing, Can Fin Homes, Aavas, Home First |
| `nbfc-vehicle-finance` | Cholamandalam, Shriram Finance, M&M Financial |
| `nbfc-gold-loan` | Muthoot Finance, Manappuram |
| `nbfc-consumer-diversified` | Bajaj Finance |

---

### INDIA — Energy & Industrial

#### `oil-gas`
| Sub-Sector | Key Players |
|---|---|
| `oil-upstream` | ONGC, Oil India |
| `oil-downstream-refining` | Reliance Industries (refining), BPCL, HPCL, IOC |
| `oil-cgd` | City Gas Distribution: IGL, MGL, Gujarat Gas, Mahanagar Gas |
| `oil-lng` | PLNG (Petronet LNG), GSPL |
| `oil-oilfield-services` | Hindustan Oil Exploration, HOEC |

#### `power-utilities`
| Sub-Sector | Key Players |
|---|---|
| `power-thermal-generation` | NTPC, CESC, Tata Power (thermal book) |
| `power-renewable` | Adani Green, Tata Power Renewable, NTPC Renewable, SJVN |
| `power-transmission` | Power Grid Corporation, IndiGrid InvIT |
| `power-distribution` | Tata Power Delhi, CESC, BSES (unlisted) |
| `power-regulatories-invit` | IndiGrid InvIT, PowerGrid InvIT |

#### `specialty-chemicals`
| Sub-Sector | Key Players |
|---|---|
| `spec-chem-agrochemicals` | PI Industries, Coromandel, UPL, Bayer CropScience |
| `spec-chem-fluorochemicals` | Gujarat Fluorochemicals (GFL), Navin Fluorine, SRF Ltd |
| `spec-chem-pigments-dyes` | Sudarshan Chemical, Kiri Industries, Atul Ltd |
| `spec-chem-adhesives-polymers` | Pidilite, Astral (adhesives), Apcotex |
| `spec-chem-performance-chem` | Aarti Industries, Alkyl Amines, Fine Organics |
| `spec-chem-explosives-mining` | Solar Industries, Premier Explosives, NMDC |

#### `defence`
| Sub-Sector | Key Players |
|---|---|
| `defence-systems-platforms` | HAL, BEL, BEML, Mazagon Dock |
| `defence-electronics-comm` | BEL, Data Patterns, MTAR Technologies, Paras Defence |
| `defence-shipbuilding` | Mazagon Dock, CSL (Cochin Shipyard), Garden Reach |
| `defence-ammunition-explosives` | Solar Industries (defence), Premier Explosives |

---

### INDIA — Infrastructure & Logistics

#### `telecom`
| Sub-Sector | Key Players |
|---|---|
| `telecom-integrated` | Reliance Jio, Airtel, Vodafone Idea |
| `telecom-tower-infra` | Indus Towers, American Tower India |
| `telecom-enterprise` | Tata Communications, BSNL (unlisted) |
| `telecom-submarine-satellite` | Tata Communications, ISRO-linked |

#### `aviation`
| Sub-Sector | Key Players |
|---|---|
| `aviation-airline` | IndiGo (InterGlobe), SpiceJet, Air India (unlisted) |
| `aviation-airport` | GMR Airports, Adani Airports, AAI (unlisted) |
| `aviation-mro-ground` | Air Works, GMR Aero Technic |

#### `logistics`
| Sub-Sector | Key Players |
|---|---|
| `logistics-3pl-surface` | VRL Logistics, TCI Express, Mahindra Logistics |
| `logistics-express-parcel` | Blue Dart, Delhivery, Ecom Express |
| `logistics-ports-marine` | APSEZ (Adani Ports), JSW Infrastructure, Gujarat Pipavav |
| `logistics-rail-freight` | CONCOR, IRCTC, Rail Vikas Nigam |
| `logistics-shipping` | GE Shipping, SCI (Shipping Corporation) |
| `logistics-cold-chain` | Snowman Logistics, ColdEX |

#### `media-entertainment`
| Sub-Sector | Key Players |
|---|---|
| `media-tv-broadcast` | Zee Entertainment, Sun TV, TV18, Star (unlisted) |
| `media-ott-streaming` | ZEE5, JioCinema, SonyLIV (unlisted) |
| `media-film-production` | PVR INOX (exhibition), Eros STX, Saregama |
| `media-digital-outdoor` | Hoardings, HMV, Laqshya Media |
| `media-music-rights` | Tips Industries, Saregama, T-Series (unlisted) |
| `media-gaming` | Nazara Technologies, Mobile Premier League |
| `media-news` | NDTV, TV Today, D.B. Corp, HT Media |

---

### INDIA — Consumer & Agri

#### `agri`
| Sub-Sector | Key Players |
|---|---|
| `agri-inputs-fertiliser` | Coromandel, Chambal Fertilisers, GSFC |
| `agri-inputs-seeds-pesticides` | PI Industries, Rallis, Sumitomo (India) |
| `agri-tractor-farm-equipment` | Mahindra & Mahindra (Farm), Escorts Kubota |
| `agri-food-processing` | ITC (FMCG+Agri), HUL (food), Heritage Foods |
| `agri-sugar` | Balrampur Chini, Dhampur Sugar, EID Parry |
| `agri-cotton-textiles` | Ambika Cotton, Vardhman Textiles |

#### `building-materials`
| Sub-Sector | Key Players |
|---|---|
| `bm-paints-coatings` | Asian Paints, Berger Paints, Kansai Nerolac, Indigo Paints |
| `bm-tiles-sanitaryware` | Kajaria Ceramics, Somany, H&R Johnson |
| `bm-plywood-mdf-laminates` | Century Plyboards, Greenply, Greenlam |
| `bm-pipes-fittings` | Astral, Supreme Industries, Prince Pipes |
| `bm-adhesives-sealants` | Pidilite Industries, Sika India |
| `bm-glass-windows` | Asahi India Glass, Gold Plus Glass |
| `bm-steel-structural` | Tata Steel (structural), JSW Steel, SAIL |

#### `textiles`
| Sub-Sector | Key Players |
|---|---|
| `textiles-yarn-spinning` | Vardhman Textiles, Trident Group, Indo Count |
| `textiles-fabric-processing` | Himatsingka, Raymond (Fabric), Arvind |
| `textiles-branded-apparel` | Page Industries (Jockey), Vedant Fashions (Manyavar), Bata |
| `textiles-technical-nonwoven` | SRF (Technical Textiles), Welspun |
| `textiles-home-furnishing` | Welspun India, Trident, Indo Count |

#### `consumer-durables`
| Sub-Sector | Key Players |
|---|---|
| `cd-white-goods-ac` | Voltas, Blue Star, Havells, Daikin India |
| `cd-kitchen-appliances` | TTK Prestige, Butterfly Gandhimathi |
| `cd-tv-consumer-electronics` | Vizio (component player), Dixon Technologies |
| `cd-ems-contract-manufacturing` | Dixon Technologies, Amber Enterprises, Kaynes |
| `cd-led-lighting` | Havells, Crompton Greaves |

#### `education`
| Sub-Sector | Key Players |
|---|---|
| `edu-offline-coaching` | Aakash (NEET/JEE), Allen (unlisted), FIITJEE |
| `edu-edtech` | Byju's (unlisted), Unacademy (unlisted), Vedantu |
| `edu-k12-schools` | Zee Learn, Global Education (NIIT), Delhi Public School |
| `edu-higher-ed` | Manipal (unlisted), Amity (unlisted), Sharda University |
| `edu-vocational-skill-dev` | NIIT Technologies, TeamLease, Teamlease Edtech |

#### `mining`
| Sub-Sector | Key Players |
|---|---|
| `mining-coal` | Coal India, NMDC (iron ore), Singareni (unlisted) |
| `mining-metals-hard-rock` | Hindalco, Vedanta, National Aluminium |
| `mining-sand-quarry` | Nuvoco (aggregates), JK Cement (limestone) |

#### `paper-packaging`
| Sub-Sector | Key Players |
|---|---|
| `paper-writing-printing` | ITC Paperboards, TNPL, JK Paper |
| `paper-packaging-board` | ITC Packaging, TCPL Packaging |
| `flexible-packaging` | Uflex, Huhtamaki, Cosmo Films |

#### `metals-fabrication`
| Sub-Sector | Key Players |
|---|---|
| `metals-castings-forgings` | Bharat Forge, Ramkrishna Forgings |
| `metals-special-alloy` | Mishra Dhatu Nigam (MIDHANI), Mukand |
| `metals-aluminium-rolled` | Hindalco (Novelis), NALCO |

#### `invit`
| Sub-Sector | Key Players |
|---|---|
| `invit-roads` | NAM India InvIT, IRB InvIT |
| `invit-power-transmission` | IndiGrid InvIT, PowerGrid InvIT |
| `invit-telecom-tower` | American Tower India InvIT |

---

### INDIA — Base Key Sectors (Inlined)

#### `auto` (Automotive Value Chain)
| Sub-Sector | Key Players |
|---|---|
| `auto-oem-pv` | Maruti Suzuki, Tata Motors (PV), M&M (PV) |
| `auto-oem-cv` | Ashok Leyland, Tata Motors (CV), Eicher Motors (VECV) |
| `auto-oem-2w` | Hero MotoCorp, Bajaj Auto, TVS Motor, Eicher (Royal Enfield) |
| `auto-oem-tractor` | M&M (Tractors), Escorts Kubota |
| `auto-ancillary-tyres` | MRF, Apollo Tyres, CEAT, JK Tyre |
| `auto-ancillary-batteries` | Exide Industries, Amara Raja |
| `auto-ancillary-components` | Motherson Sumi, Bosch, Endurance, Minda |
| `auto-dealership` | Landmark Cars, Popular Vehicles |

#### `fmcg` (Consumer Value Chain)
| Sub-Sector | Key Players |
|---|---|
| `fmcg-brand-owner` | HUL, Nestlé, Britannia, Dabur, Marico, Godrej Consumer |
| `fmcg-contract-mfg` | Hindustan Foods, Bajaj Consumer |
| `fmcg-qcommerce-retail` | Zomato (Blinkit), Swiggy |

#### `cement` & `infra` (Construction Value Chain)
| Sub-Sector | Key Players |
|---|---|
| `cement-integrated` | UltraTech, Ambuja, Shree Cement, Dalmia (clinker + grinding) |
| `cement-grinding` | Regional grinding units |
| `infra-epc` | L&T (construction), KNR, Ahluwalia Contracts, PNC Infratech |
| `infra-developer-bot` | IRB Infra (BOT/HAM assets) |

#### `retail` & `gold`
| Sub-Sector | Key Players |
|---|---|
| `retail-grocery-hypermarket`| DMart (Avenue Supermarts), Spencer's |
| `retail-apparel-fashion` | Trent, Shopper's Stop, V-Mart, Aditya Birla Fashion |
| `retail-electronics` | Reliance Retail (unlisted), Electronics Mart |
| `gold-jewellery-retail` | Titan, Kalyan Jewellers, Senco Gold, Joyalukkas (unlisted) |

#### Other Base Sectors
| Sector | Key Signals / Examples |
|---|---|
| `it` | TCS, Infosys, Wipro, HCL Tech, Tech Mahindra |
| `capital-goods` | L&T, Siemens, ABB, BHEL |
| `electrical` | Polycab, Havells, KEI Industries |
| `commodity` | Tata Steel, JSW Steel, Hindalco, Vedanta |
| `hospitality-hotels` | Indian Hotels, EIH, Lemon Tree, Chalet, Samhi Hotels |
| `capital-markets-amc` | HDFC AMC, Nippon Life AMC, UTI AMC |
| `recycling-circular` | Gravita India, Eco Recycling |
| `infra-peb` | Pennar Industries, Everest, JSW Severfield |
| `deeptech-drones-aerospace`| Zen Tech, ideaForge, MTAR Tech, Data Patterns |
| `green-energy-bess` | KPI Green, Amara Raja (BESS), Gensol |
| `internet-platform-auto` | Cartrade Tech, Cars24 (unlisted) |
| `auto-ancillary-ev` | Minda Corporation, Sona Comstar |
| `it-healthcare` | Indegene, CitiusTech (unlisted) |
| `specialty-plastics-films` | Garware Hi-Tech Films, Cosmo First |
| `pharma-cdmo` | Sai Life Sciences, Syngene, Divis Labs |
| `cryogenics-gas-equip` | INOX India, Everest Kanto |
| `semicon-equipment-global` | ASML, Applied Materials, Lam Research |
| `retail-apparel` | Trent, DMart, V-Mart, Shoppers Stop |
| `ems-contract-mfg` | Dixon Tech, Amber Enterprises, Kaynes Tech |
| `datacenter-infrastructure`| Netweb Tech, Anant Raj |
| `power-capex` | Hitachi Energy, GE T&D, Apar Industries |
| `fmcg-alco-beverage` | United Spirits, Radico Khaitan, Tilaknagar |
| `infra-ports` | Adani Ports, JSW Infra, Gujarat Pipavav |
| `specialty-chemicals` | SRF, Navin Fluorine, PI Industries |
| `green-energy-solar` | Waaree Renewables, Sterling & Wilson, Tata Power |
| `infra-water-epc` | VA Tech Wabag, Ion Exchange, EMS Ltd |
| `auto-tractors-agri` | M&M, Escorts, Swaraj Engines |
| `sugar-ethanol-distillery` | Triveni Engineering, Balrampur Chini, Praj |
| `fmcg-consumer-brands` | Varun Beverages, Tata Consumer, Nestle India |
| `banks-sfb-microfinance` | AU Small Finance, Equitas, Ujjivan |
| `qsr-food-chains` | Jubilant Foodworks, Westlife, Devyani |
| `quick-commerce` | Zomato (Blinkit), Swiggy Instamart |
| `ev-batteries-chemicals` | Neogen, Aarti, Himadri Speciality |
| `power-exchange-platforms` | IEX, MCX (Commodity) |
| `nbfc-housing-finance` | Aavas, Home First, Aptus, Can Fin |
| `consumer-ed-tech` | NIIT, Aptech (unlisted proxies) |
| `retail-footwear` | Metro Brands, Campus, Relaxo, Bata |
| `retail-knitwear` | Page Industries, Lux, Dollar, Rupa |
| `holdcos` | Bajaj Holdings, Pilani Inv, Tata Investment |
| `wires-cables` | Polycab, KEI Industries, RR Kabel |
| `auto-ancillary-core` | Minda Corp, Sona Comstar, Schaeffler |
| `real-estate-developers` | Macrotech (Lodha), DLF, Godrej Prop |
| `building-materials-cement` | UltraTech, Shree Cement, Ambuja |
| `building-materials-pipes` | Astral, Supreme Industries, Finolex |
| `building-materials-tiles` | Kajaria Ceramics, Somany |
| `healthcare-hospitals` | Apollo Hospitals, Max Health, Narayana |
| `healthcare-diagnostics` | Dr Lal PathLabs, Metropolis, Thyrocare |
| `hospitality-hotels` | Indian Hotels, Lemon Tree, Samhi Hotels |
| `aviation-airlines` | InterGlobe (Indigo), SpiceJet |
| `telecom-services` | Bharti Airtel, Reliance Jio (Unlisted) |

---

### INDIA — Healthcare (already covered — see pharma & hospital above)

---

## US MARKET SECTORS

### `biotech-us`
| Sub-Sector | Examples |
|---|---|
| `biotech-clinical-stage` | Pre-revenue, pipeline-driven (phase II/III data catalysts) |
| `biotech-commercial-stage` | Revenue-generating branded biologic/biosimilar |
| `biotech-genomics-diagnostic` | Exact Sciences, Guardant, Illumina |
| `biotech-cell-gene-therapy` | Bluebird bio, Moderna (mRNA platform) |
| `biotech-cro-cdmo-us` | IQVIA, Charles River, Catalent, Lonza |

### `semicon`
| Sub-Sector | Examples |
|---|---|
| `semicon-fabless-design` | Nvidia, AMD, Qualcomm, Broadcom |
| `semicon-foundry-ido` | TSMC, Intel Foundry, Samsung Semi |
| `semicon-equipment-materials` | ASML, Applied Materials, KLA, Lam Research |
| `semicon-integrated-ido` | Intel, Texas Instruments, Analog Devices |
| `semicon-memory` | Micron, SK Hynix |

### `saas-cloud`
| Sub-Sector | Examples |
|---|---|
| `saas-b2b-enterprise` | Salesforce, ServiceNow, Workday, Adobe |
| `saas-b2b-smb` | HubSpot, Freshworks, Zoho |
| `saas-b2c-consumer-tech` | Spotify, Duolingo, Match Group |
| `cloud-infra-hyperscaler` | AWS (Amazon), Azure (Microsoft), Google Cloud |
| `ai-ml-platform` | Palantir, C3.ai, OpenAI (unlisted), Anthropic (unlisted) |
| `cybersecurity-saas` | CrowdStrike, Palo Alto, SentinelOne, Zscaler |

### `us-healthcare`
| Sub-Sector | Examples |
|---|---|
| `managed-care-hmo` | UnitedHealth, Humana, Elevance Health (Anthem) |
| `hospital-system-us` | HCA Healthcare, Tenet Health, Universal Health |
| `pharma-us-branded` | Pfizer, Eli Lilly, Merck, AbbVie, Johnson & Johnson |
| `medtech-us` | Medtronic, Boston Scientific, Abbott |
| `pharmacy-benefit-manager` | CVS Health (PBM), Cigna (Express Scripts) |
| `health-insurance-exchange` | Oscar Health, Clover Health |

### `us-financials`
| Sub-Sector | Examples |
|---|---|
| `investment-bank` | Goldman Sachs, Morgan Stanley, Lazard |
| `asset-manager` | BlackRock, Vanguard (private), T. Rowe Price |
| `broker-dealer` | Charles Schwab, Interactive Brokers, LPL Financial |
| `payments-us` | Visa, Mastercard, PayPal, Stripe (unlisted) |
| `consumer-finance-us` | American Express, Discover, Capital One |
| `specialty-finance-us` | Apollo Global, KKR, Blackstone (alt asset managers) |

### `us-energy`
| Sub-Sector | Examples |
|---|---|
| `energy-e-and-p` | ExxonMobil (upstream), ConocoPhillips, Pioneer |
| `energy-midstream-mlp` | Enterprise Products, Kinder Morgan, Energy Transfer |
| `energy-downstream-refining` | Valero, Marathon Petroleum, Phillips 66 |
| `energy-renewable-us` | NextEra, First Solar, Enphase, SunPower |
| `energy-utilities-regulated` | Duke Energy, American Electric Power, Southern Company |

### `us-reits`
| Sub-Sector | Examples |
|---|---|
| `reit-data-center` | Equinix, Digital Realty, Iron Mountain |
| `reit-healthcare-us` | Ventas, Welltower, Healthcare Trust |
| `reit-industrial-logistics-us` | Prologis, Duke Realty, Rexford Industrial |
| `reit-office-us` | Boston Properties, Vornado, SL Green |
| `reit-retail-us` | Simon Property Group, Regency Centers |
| `reit-triple-net-lease` | Realty Income (O), STORE Capital, NNN REIT |
| `reit-residential-multifamily` | AvalonBay, Equity Residential, Camden Property |
| `reit-self-storage` | Public Storage, Extra Space Storage |

### `us-defence`
| Sub-Sector | Examples |
|---|---|
| `us-defence-prime-contractor` | Lockheed Martin, RTX (Raytheon), Boeing Defense |
| `us-defence-electronics-systems` | Northrop Grumman, L3Harris, BAE Systems (UK) |
| `us-defence-cybersec` | Booz Allen Hamilton, SAIC, Leidos |

### `us-consumer`
| Sub-Sector | Examples |
|---|---|
| `us-luxury-goods` | Ralph Lauren, Tapestry, Capri Holdings; LVMH, Hermès (France) |
| `us-qsr-foodservice` | McDonald's, Yum! Brands, Restaurant Brands (Burger King) |
| `us-auto-oem` | GM, Ford, Tesla, Rivian |
| `us-auto-dealer` | AutoNation, CarMax, Carvana |
| `us-e-commerce` | Amazon (marketplace), Shopify (platform), Etsy |

### `us-industrials`
| Sub-Sector | Examples |
|---|---|
| `us-capital-goods-industrial` | Caterpillar, Deere, Honeywell, Parker Hannifin |
| `us-aero-commercial` | Boeing (commercial), Spirit AeroSystems |
| `us-chemical-specialty` | Albemarle (lithium), Cabot, RPM International |
| `us-packaging` | Sealed Air, Ball Corp, Graphic Packaging |

---

## Cyclicality Classification → `cyclicality`

| Label | Sectors / Sub-Sectors |
|---|---|
| `highly-cyclical` | `commodity`, `capital-goods`, `realty-residential-*`, `realty-commercial-*`, `infra`, `oil-upstream`, `shipping`, `aviation-airline`, `agri-sugar`, `semicon-memory`, `us-defence-prime`, `energy-e-and-p`, `energy-midstream-mlp` |
| `moderately-cyclical` | `auto`, `electrical`, `cement`, `it`, `realty-retail-mall`, `power-thermal`, `telecom-integrated`, `us-industrials`, `us-auto-oem`, `saas-b2b-enterprise`, `biotech-commercial-stage` |
| `defensive` | `fmcg`, `pharma-domestic-branded`, `hospital-multispecialty-chain`, `hospital-diagnostic-lab`, `insurance-life`, `insurance-health`, `oil-cgd`, `power-distribution`, `energy-utilities-regulated`, `managed-care-hmo`, `telecom-tower-infra` |
| `secular-growth` | `retail`, `gold`, `pharma-cdmo`, `pharma-diagnostics`, `hospital-health-tech`, `realty-warehousing-industrial`, `saas-b2b-enterprise`, `cybersecurity-saas`, `ai-ml-platform`, `semicon-fabless-design`, `cloud-infra-hyperscaler`, `reit-data-center`, `logistics-express-parcel`, `edu-edtech` |
| `rate-sensitive` | `bank`, `nbfc`, `insurance-life`, `reit-*`, `energy-utilities-regulated`, `realty-reit` |
| `export-cycle` | `pharma-api`, `pharma-export-us-generics`, `it` (USD-INR driven), `spec-chem-agrochemicals` (global pricing), `textiles-branded-apparel` |
| `policy-driven` | `defence`, `oil-downstream-refining` (OMC subsidy), `power-renewable` (RPO mandates), `agri-inputs-fertiliser` (subsidy), `us-defence-prime` |
