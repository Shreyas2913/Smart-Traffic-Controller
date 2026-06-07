# Smart Traffic Controller
### AI-Driven Real-Time Optimisation · Data Pipelines · Automated Decision Logic

> A data-driven system that ingests real-time traffic data, applies business rules, and takes automated action to optimise signal timings.
> Result: ~20% reduction in average vehicle waiting time.

---

## 🎯 The Problem

Static traffic signal timings cause unnecessary congestion — signals stay red even when roads are clear.
Real-time data exists but isn't being used to make dynamic decisions.

## 💡 The Solution

An AI system that reads live sensor data, evaluates traffic KPIs, applies optimisation logic, and adjusts signal timings automatically — with a live dashboard showing performance.

---

## 🏗️ What I Built

```
Real-Time Sensor Data (traffic volume, wait times, flow rates)
      │
      ▼
Data Pipeline (Python · SQL-style querying · cleaning · transformation)
      │
      ▼
Business Rule Engine (thresholds · timing constraints · priority logic)
      │
      ▼
Automated Signal Adjustment (decision output)
      │
      ▼
Live Operational Dashboard (KPIs · before/after · flow patterns)
```

---

## 🔧 Tech Stack

| Component | Tech |
|-----------|------|
| Language | Python |
| Data processing | Pandas, NumPy, SQL-style querying |
| Decision logic | Custom rule engine |
| Visualisation | Matplotlib dashboard |
| Data | Real-time traffic sensor simulation |

---

## 📊 Results

- ✅ ~20% reduction in average vehicle waiting time
- ✅ Full end-to-end automation — no manual intervention needed
- ✅ Dashboard gave clear before/after view of system performance
- ✅ System adapted dynamically to changing traffic conditions

---

## 💡 Why this maps to AI agent engineering

This project is structurally identical to building an AI agent:
- **Context awareness** — reads real-time data (like an agent reads conversation/system state)
- **Business rules** — follows constraints (like agent guardrails)
- **Tool use** — takes action by adjusting outputs (like an agent calling a tool)
- **Validation** — checks outputs match expected behaviour before applying them
