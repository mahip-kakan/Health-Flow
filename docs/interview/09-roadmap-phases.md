# 09 — Roadmap Phases

Phased delivery plan from Phase 0 prototype to production EX platform.

---

## Overview

| Phase | Name | Duration (est.) | Backend | Primary value |
|-------|------|-----------------|--------|---------------|
| **0** | UX Prototype | ✅ Complete | None | Stakeholder alignment, workflow validation |
| **1** | Flow Platform MVP | 8–10 weeks | Flow API + Postgres | Persistent flows, draft/publish, sandbox test runs |
| **2** | HR Production Pilot | 10–12 weeks | Orchestrator + HRIS + RAG | Onboarding + policy QA live for HR ops |
| **3** | Marketing Expansion | 8 weeks | Campaign events + LLM tools | Debrief + repurposing automations |
| **4** | Eval & Governance | 6–8 weeks | Eval service + admin console | Publish gates, drift, cost controls |
| **5** | Employee Channels | 8–10 weeks | Slack/Teams bots | EX assistant in flow of work |

**Total to Phase 5:** ~12–15 months with a small platform team (2 backend, 1 ML, 1 PM, 1 design)

---

## Phase 0 — UX Prototype ✅ (current)

### Delivered

- React SPA with Agent Studio, EX chat, Testing Dashboard  
- HR, Marketing, Healthcare, IT/SaaS vertical catalogs  
- Role-based personas (Developer, PM, Admin)  
- GitHub Pages deployment  
- Interview documentation package (`docs/interview/`)

### Limitations

- In-memory flow storage  
- Simulated AI (keyword / glossary matching)  
- Mock eval metrics  
- No external integrations  

### Exit criteria

- [x] HR and Marketing stakeholders validate top 10 flows  
- [x] Architecture reviewed by engineering  
- [x] Eval framework requirements documented  

---

## Phase 1 — Flow Platform MVP

### Build

- Flow / Agent API (CRUD, versioning, draft/publish)  
- PostgreSQL schema for flows, versions, audit log  
- API Gateway with SSO + RBAC  
- Front-end wired to API (replace `useState(savedFlows)`)  
- Sandbox test run endpoint (mock connector responses)  

### APIs

```
POST /api/v1/flows
POST /api/v1/flows/{id}/publish
POST /api/v1/runs/test
GET  /api/v1/runs/{id}
```

### Exit criteria

- Process owner creates, saves, and publishes flow without code deploy  
- Sandbox test run returns step-by-step mock results in UI  
- Flow versions auditable  

---

## Phase 2 — HR Production Pilot

### Build

- Event Ingest Service + HRIS webhook (`employee.start_date_set`, `offer.accepted`)  
- Workflow Orchestrator (Temporal) with retry + idempotency  
- Connectors: internal tasks, Teams, email  
- RAG Service over HR handbook (pgvector)  
- Chat API v1: glossary + policy Q&A with citations  

### Pilot flows (go-live)

1. New hire onboarding runbook  
2. Policy QA bot  
3. T-minus onboarding runbook  

### Exit criteria

- 3 flows running in production for HR ops pilot group  
- Policy answers include citations; OOS refusal rate < 5% false positives  
- Run audit log queryable by HR admin  

---

## Phase 3 — Marketing Expansion

### Build

- CMS + analytics event ingest (`content.published`, `campaign.ended`)  
- LLM tools: debrief summarizer, copy generator  
- Connectors: Slack, email, CSV export  
- Marketing golden eval dataset  

### Pilot flows

1. Post-campaign debrief  
2. Content repurposing  
3. A/B test readout  

### Exit criteria

- Marketing ops publishes 3 recipes without engineering  
- Debrief cycle time < 24h from campaign end  

---

## Phase 4 — Eval & Governance

### Build

- Eval Service: golden datasets, offline runner, CI gate on publish  
- Drift monitoring jobs + alert to PM dashboard  
- Load test pipeline (k6 in staging)  
- Admin control plane (extend IT/SaaS AI Governance to all verticals)  
- Model Gateway: multi-provider routing, token cost tracking  

### Exit criteria

- 100% of flow publishes run eval gate; failures block publish  
- Drift alerts fire within 24h of baseline breach  
- IT admin can disable AI features per vertical  

---

## Phase 5 — Employee Channels

### Build

- Slack / Teams bot integration for EX assistant  
- Employee SSO context (role, location) in every chat request  
- Proactive nudges (T-minus reminders, pending approvals)  
- Self-service task completion via tool use (PTO, policy, onboarding status)  

### Exit criteria

- ≥ 50% of HR pilot employees use EX assistant monthly  
- Task completion rate ≥ 70% without ticket creation  
- p95 chat latency < 2s  

---

## Team & dependencies

| Role | Phase 1–2 | Phase 3–5 |
|------|-----------|-----------|
| PM (you) | Requirements, eval criteria, pilot success | Adoption, roadmap, governance policy |
| Backend engineer | Flow API, orchestrator, connectors | Event ingest, scaling |
| ML / AI engineer | RAG, prompt registry | Eval service, model gateway |
| Front-end engineer | API integration | Channel bots, dashboard |
| HR / Marketing sponsor | Pilot users, golden dataset curation | Feedback, change management |

### External dependencies

- HRIS webhook access (IT + HR)  
- SSO / Okta integration (IT)  
- LLM enterprise agreement (Legal + Finance)  
- Confluence / handbook export for RAG (HR)  

---

## Risk register

| Risk | Mitigation |
|------|------------|
| HRIS integration delay | Phase 1 manual trigger + CSV import fallback |
| LLM hallucination on policy | RAG-only answers + citation gate + human escalation |
| Low employee adoption | Embed in Slack/Teams (Phase 5); don't rely on new portal |
| Eval suite false positives | Human review queue; tune thresholds per suite |
| Scope creep across verticals | Shared engine; vertical catalogs owned by domain PMs |

---

## Diagram reference

- [Platform overview](./diagrams/01-platform-overview.excalidraw)  
- [Backend architecture](./diagrams/03-backend-architecture.excalidraw)  
- [Eval pipeline](./diagrams/04-eval-pipeline.excalidraw)
