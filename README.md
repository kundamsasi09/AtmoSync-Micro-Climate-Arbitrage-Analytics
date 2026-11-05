# 🚢 AtmoSync: Micro-Climate Arbitrage Analytics

> **Organization:** Infotact Solutions  
> **Intern:** Sasi Rekha Kundam  
> **Offer Ref:** ITS/DA/1716  
> **Role:** Data Associate L1. Intern (Data Analytics)  
> **Track:** Advanced Data Analytics & Engineering (Global Logistics & Commodities)  
> **Project 1:** Real-World Applications – Hands-on System Building

---

## 📌 Problem Statement (Infotact Official Specification)
Traditional supply chain analytics rely on standard transit times and macro-weather forecasts. They fail to track how real-time, hyper-local micro-climate shifts (e.g., sudden temperature/humidity spikes inside a refrigerated shipping container) degrade agricultural commodities before they reach the market.

## 🎯 Use Case
A commodities trader at **Infotact** monitors the **AtmoSync** dashboard. The streaming pipeline detects that **Container A's** internal temperature has drifted from its optimal band, accelerating the spoilage rate of the avocados inside.

The dashboard instantly calculates **"Spoilage Arbitrage"** and alerts the trader to reroute the shipment to a closer, secondary market—securing a premium price before the goods degrade below commercial quality thresholds.

---

## 🏗️ Architecture & Technology Stack
* **Streaming Ingestion:** Apache Kafka (high-throughput event streaming)
* **Cloud Data Warehouse:** Snowflake (raw JSON variant tables & dimensional marts)
* **Data Transformation:** dbt Core (ELT modeling & degradation curves)
* **Visualization Layer:** Apache Superset & Streamlit Trader Portal