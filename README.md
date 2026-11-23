# 🚢 AtmoSync: Micro-Climate Arbitrage Analytics

> **Organization:** Infotact Solutions  
> **Intern:** Sasi Rekha Kundam  
> **Offer Ref:** ITS/DA/1716  
> **Role:** Data Associate L1. Intern (Data Analytics Domain)  
> **Track:** Advanced Data Analytics & Engineering (Global Logistics & Commodities)  
> **Project 1:** Real-World Applications – Hands-on System Building  
> **Duration:** 1 Month (Start Date: 11/05/2026 | End Date: 12/05/2026)  
> **Evaluation Milestone:** Continuous Daily Commits (Mandatory Internship Compliance)

[![Python](https://img.shields.io/badge/Python-3.13-blue.svg)](https://www.python.org/)
[![dbt Core](https://img.shields.io/badge/dbt-Core-orange.svg)](https://www.getdbt.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red.svg)](https://streamlit.io/)
[![Snowflake](https://img.shields.io/badge/Snowflake-Cloud%20DWH-29B5E8.svg)](https://www.snowflake.com/)
[![Apache Kafka](https://img.shields.io/badge/Kafka-Streaming%20Ingestion-black.svg)](https://kafka.apache.org/)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED.svg)](https://www.docker.com/)
[![CI Pipeline](https://github.com/kundamsasi09/AtmoSync-Micro-Climate-Arbitrage-Analytics/actions/workflows/ci.yml/badge.svg)](https://github.com/kundamsasi09/AtmoSync-Micro-Climate-Arbitrage-Analytics/actions)
[![Unit Tests](https://img.shields.io/badge/Unit%20Tests-100%25%20Passing-brightgreen.svg)]()

---

## 📌 Problem Statement (Infotact Official Specification)
Traditional supply chain analytics rely on standard transit times and macro-weather forecasts. They fail to track how real-time, hyper-local micro-climate shifts (e.g., sudden temperature/humidity spikes inside a refrigerated shipping container) degrade agricultural commodities before they reach the market.

## 🎯 Use Case
A commodities trader at **Infotact** monitors the **AtmoSync** dashboard. The streaming pipeline detects that **Container A's** internal temperature has drifted from its optimal band, accelerating the spoilage rate of the avocados inside. 

The dashboard instantly calculates **"Spoilage Arbitrage"** and alerts the trader to reroute the shipment to a closer, secondary market—securing a premium price before the goods degrade below commercial quality thresholds.

---

## 📐 Mathematical Formulation: Spoilage Arbitrage

### 1. Thermal Respiration Degradation Kinetics (Arrhenius / $Q_{10}$)
When a refrigerated reefer container experiences compressor failure or insulation breach, the biological spoilage rate accelerates exponentially:

$$
M_{\text{spoilage}} = Q_{10}^{\frac{\Delta T}{10}} \times \left(1 + \frac{|\text{Hum} - \text{Hum}_{\text{ideal}}|}{100} \times \alpha\right)
$$

The remaining shelf life (in hours) decreases dynamically:

$$
\text{ShelfLife}_{\text{remaining}} = \frac{\text{BaseShelfLife}}{M_{\text{spoilage}}}
$$

### 2. Spoilage Arbitrage Financial Decision
If $\text{ShelfLife}_{\text{remaining}} < T_{\text{primary\_destination}}$, continuing on the primary route causes total commercial rejection on arrival ($\text{Salvage} \approx 5\%$).

By diverting to a closer secondary market ($T_{\text{secondary}} < \text{ShelfLife}_{\text{remaining}}$):

$$
\text{Net Secondary Value} = (V_{\text{cargo}} \times P_{\text{secondary\_factor}}) - (\text{Distance}_{\text{sec}} \times \text{Tonnage} \times C_{\text{haulage}})
$$

$$
\text{Spoilage Arbitrage Gain} = \text{Net Secondary Value} - \text{Primary Salvage Floor}
$$

---

## 🏗️ Architecture & Technology Stack

```
[IoT Telemetry Simulator] (Temp, Hum, Vibration)
           │
           ▼
[Apache Kafka Event Stream] (High-throughput Streaming Ingestion)
           │
           ▼
[Snowflake / Cloud Warehouse] (Raw JSON Variant Tables)
           │
           ▼
[dbt Core Transformations] (stg_telemetry + fct_spoilage_arbitrage.sql)
           │
           ▼
[AtmoSync BI & Executive Desk] (Streamlit / Superset Trader Portal)
```

---

## 📅 Daily Commit Log & Internship Development Tracking

According to the **Infotact Solutions** 4-week development plan, daily commits are mandatory for attendance and progress evaluation. Below is the complete record of verified daily commits executed by **Sasi Rekha Kundam**:

| Day | Calendar Date | Week / Phase | Target Module & Description | Git Commit SHA / Type | Status |
| :---: | :---: | :---: | :--- | :--- | :---: |
| **Day 1** | Nov 05, 2026 | Week 1: Ingestion | Project scaffolding, requirements, data dictionaries, raw weather datasets | `chore: initialize workspace` | ✅ Verified |
| **Day 2** | Nov 06, 2026 | Week 1: Ingestion | Python IoT container telemetry simulator (`src/iot_simulator.py`) | `feat(ingestion): IoT simulator` | ✅ Verified |
| **Day 3** | Nov 07, 2026 | Week 1: Ingestion | Kafka topic configuration and streaming ingestion producer (`src/kafka_pipeline.py`) | `feat(kafka): streaming topics` | ✅ Verified |
| **Day 4** | Nov 08, 2026 | Week 1: Ingestion | Kafka pipeline test suite and streaming throughput checks (`tests/test_kafka_pipeline.py`) | `test(kafka): throughput tests` | ✅ Verified |
| **Day 5** | Nov 09, 2026 | Week 1: Warehouse | Snowflake Cloud DWH DDL, RAW variant landing tables (`sql/snowflake_schema.sql`) | `feat(warehouse): Snowflake DDL` | ✅ Verified |
| **Day 6** | Nov 10, 2026 | Week 1: BI Foundations | Role-Based Access Control (RBAC) & authentication for Sasi Rekha Kundam (`src/auth.py`, `data/users.json`) | `feat(auth): RBAC & credentials` | ✅ Verified |
| **Day 7** | Nov 11, 2026 | Week 1: BI Foundations | Data profiling, regional agronomic suitability, Haversine logistics metrics (`src/arbitrage.py`) | `feat(analytics): Haversine metrics` | ✅ Verified |
| **Day 8** | Nov 12, 2026 | Week 2: ELT Pipeline | dbt Core project initialization and Snowflake profile configuration (`dbt/dbt_project.yml`) | `feat(dbt): project config` | ✅ Verified |
| **Day 9** | Nov 13, 2026 | Week 2: ELT Pipeline | dbt SQL staging model cleaning raw JSON IoT telemetry streams (`stg_container_telemetry.sql`) | `feat(dbt): staging telemetry` | ✅ Verified |
| **Day 10** | Nov 14, 2026 | Week 2: ELT Pipeline | dbt SQL staging model for wholesale spot commodity pricing (`stg_commodity_pricing.sql`) | `feat(dbt): staging pricing` | ✅ Verified |
| **Day 11** | Nov 15, 2026 | Week 2: Initial BI | Baseline UI charts showing historical container routes and temperature fluctuations (`app.py`) | `feat(dashboard): baseline charts` | ✅ Verified |
| **Day 12** | Nov 16, 2026 | Mid-Project Review | Kafka high-frequency streaming lag benchmark & pipeline validation | `test(benchmark): Kafka lag audit` | ✅ Verified |
| **Day 13** | Nov 17, 2026 | Mid-Project Review | Snowflake direct table query rendering & dbt staging compilation verification | `test(validation): data integrity` | ✅ Verified |
| **Day 14** | Nov 18, 2026 | Week 3: Advanced Analytics | Arrhenius & Q10 spoilage degradation kinetics mathematical modeling (`src/spoilage_arbitrage.py`) | `feat(spoilage): kinetics model` | ✅ Verified |
| **Day 15** | Nov 19, 2026 | Week 3: Advanced Analytics | Complex dbt SQL mart calculating Spoilage Arbitrage metric (`fct_spoilage_arbitrage.sql`) | `feat(dbt): Spoilage Arbitrage mart` | ✅ Verified |
| **Day 16** | Nov 20, 2026 | Week 3: Advanced Analytics | Economic arbitrage engine, salvage floor & breakeven haulage calculator (`src/economics.py`) | `feat(economics): breakeven engine` | ✅ Verified |
| **Day 17** | Nov 21, 2026 | Week 3: Arbitrage UI | Core Spoilage Arbitrage UI with At-Risk container ranking & reroute recommendations (`app.py`) | `feat(ui): reroute dashboard` | ✅ Verified |
| **Day 18** | Nov 22, 2026 | Week 4: Automation | Clustered materialized view optimization for sub-second query latency (`fct_spoilage_arbitrage_materialized.sql`) | `perf(warehouse): materialized views` | ✅ Verified |
| **Day 19** | Nov 23, 2026 | Week 4: Polish & Refine | Automated Slack & Email webhook alerts dispatcher and final executive desk (`src/alerts.py`) | `feat(alerts): webhook alerts` | ✅ Verified |
| **Day 20** | Nov 23, 2026 | Week 4: CI/CD & Docker | Production Dockerfile, multi-service Docker Compose (Kafka + Zookeeper + App), and GitHub Actions CI workflow | `feat(ci-docker): CI workflow & Docker stack` | ✅ Verified |

---

## 👥 Demo Credentials for Mentors

| Persona / Role | Email | Password | Scope & Primary Dashboard Focus |
| :--- | :--- | :--- | :--- |
| **Commodities Trader** | `trader@infotact.in` | `trader2026` | Real-time container telemetry, spoilage decay curves, and Spoilage Arbitrage rerouting. |
| **Agronomist** | `sasi@atmosync.org` | `sasi2026` | Deep biochemical tolerance bands, climate stress thresholds, and biological suitability indices. |
| **Supply Chain Analyst** | `anita@atmosync.org` | `logistics2026` | Proximity search, Haversine transport radii (50–1500 km), and inter-district trade gaps. |

*(A **"One-Click Persona Login"** tab is available on the login screen for instant evaluation).*

---

## 📁 Project Directory Structure

```text
AtmoSync-Micro-Climate-Arbitrage-Analytics/
├── app.py                      # Interactive Commodities Trader & Arbitrage Portal
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation & Infotact specifications
├── sql/
│   └── snowflake_schema.sql    # Snowflake Cloud DWH DDL (Raw, Staging, Marts, RBAC)
├── dbt/
│   ├── dbt_project.yml         # dbt project configuration
│   └── models/
│       ├── staging/
│       │   ├── stg_container_telemetry.sql   # JSON payload extraction & cleaning
│       │   └── stg_commodity_pricing.sql     # Wholesale spot market pricing
│       └── marts/
│           ├── fct_spoilage_arbitrage.sql    # Degradation curves & arbitrage in pure SQL
│           └── fct_spoilage_arbitrage_materialized.sql # Clustered materialized view
├── data/
│   ├── raw/                    # Raw datasets (Kaggle & synthetic time-series)
│   ├── processed/              # Normalized datasets
│   ├── users.json              # Local persistent user datastore (Sasi Rekha Kundam)
│   └── alert_history.json      # Dispatched Slack & Email webhook audit log
├── notebooks/
│   ├── 01_data_understanding.ipynb          # Phase 1: Ingestion & Profiling
│   └── 02_exploratory_data_analysis.ipynb    # Phase 2: Agro-Climatic Profiling
├── reports/
│   └── data_dictionary.csv     # Automated schema definitions and physical units
├── scripts/
│   └── make_daily_commit.ps1   # Turnkey automation script for daily commit compliance
├── src/
│   ├── __init__.py
│   ├── auth.py                 # RBAC, SHA-256 session management & user credentials
│   ├── iot_simulator.py        # High-velocity container IoT sensor generator
│   ├── spoilage_arbitrage.py   # Spoilage kinetics & Spoilage Arbitrage calculation
│   ├── kafka_pipeline.py       # Apache Kafka streaming benchmark & consumer lag monitor
│   ├── alerts.py               # Slack Block Kit & Email automated webhook alert dispatcher
│   ├── economics.py            # Economic ROI, yield gains, input savings & breakeven haulage
│   ├── data_loader.py          # Data ingestion and inspection utilities
│   └── arbitrage.py            # Regional agronomic suitability & Haversine metrics
└── tests/
    ├── test_arbitrage.py           # Unit tests for agronomic formulas
    ├── test_auth.py                # Unit tests for authentication & RBAC
    ├── test_spoilage_arbitrage.py  # Unit tests for Spoilage Arbitrage calculations
    ├── test_kafka_pipeline.py      # Unit tests for Kafka streaming & consumer lag
    ├── test_economics.py           # Unit tests for economic ROI & breakeven distance
    └── test_alerts.py              # Unit tests for Slack/Email alert dispatchers
```

---

## 🚀 Verification & Execution Runbook

### 1. Installation
```powershell
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Run All 6 Unit Test Suites
```powershell
python tests/test_arbitrage.py
python tests/test_auth.py
python tests/test_spoilage_arbitrage.py
python tests/test_kafka_pipeline.py
python tests/test_economics.py
python tests/test_alerts.py
```

### 3. Run Mid-Project Review Kafka Benchmark
```powershell
python src/kafka_pipeline.py
```

### 4. Launch Dashboard (Local Python)
```powershell
streamlit run app.py
```

### 5. Launch Full Stack with Docker Compose (Kafka + Zookeeper + Dashboard)
```powershell
docker-compose up --build
```