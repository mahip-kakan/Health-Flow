# Workflow Studio — Internal EX Platform (Interview Brief)

**Prepared at Impact Analytics** · Phase 0 product discovery prototype  
**Live demo:** [mahip-kakan.github.io/Work-Flow/](https://mahip-kakan.github.io/Work-Flow/)  
**Status:** Front-end prototype complete · Target backend architecture defined · Eval framework specified

---

## Executive summary

Workflow Studio is an **internal Employee Experience (EX) automation initiative** at Impact Analytics. It prototypes a governed platform where HR and Marketing teams can:

1. **Compose** multi-step automations (trigger → actions) in a low-code Agent Studio  
2. **Serve** employees through a conversational EX assistant with domain glossaries  
3. **Measure** AI quality through a PM/Admin Testing Dashboard (evals, drift, load, observability)

The current repository ships a **Phase 0 React SPA** with no backend. Architecture, API contracts, and rollout phases are documented for productionization.

---

## Document map

| Doc | Contents |
|-----|----------|
| [01 — Problem & Vision](./01-problem-and-vision.md) | Why we built this, personas, scope |
| [02 — Product Surfaces](./02-product-surfaces.md) | Every screen, vertical, and role |
| [03 — HR Flow Catalog](./03-flow-catalog-hr.md) | **Primary** — curated HR automations |
| [04 — Marketing Flow Catalog](./04-flow-catalog-marketing.md) | Campaign, content, experimentation flows |
| [05 — Healthcare & IT Appendix](./05-flow-catalog-healthcare-it.md) | Additional vertical breadth |
| [06 — Backend Architecture](./06-backend-architecture.md) | Production services, APIs, data stores |
| [07 — Eval & Governance](./07-eval-and-governance.md) | Quality gates, guardrails, observability |
| [08 — Demo Script](./08-demo-script.md) | 5-minute live walkthrough + talk track |
| [09 — Roadmap Phases](./09-roadmap-phases.md) | Phase 0 → Phase 5 delivery plan |

### Architecture diagrams (Excalidraw)

Open in [excalidraw.com](https://excalidraw.com) → *Open* → select file.

| Diagram | File |
|---------|------|
| Platform overview (4 layers) | [diagrams/01-platform-overview.excalidraw](./diagrams/01-platform-overview.excalidraw) |
| HR onboarding runtime sequence | [diagrams/02-hr-onboarding-sequence.excalidraw](./diagrams/02-hr-onboarding-sequence.excalidraw) |
| Target backend architecture | [diagrams/03-backend-architecture.excalidraw](./diagrams/03-backend-architecture.excalidraw) |
| AI evaluation pipeline | [diagrams/04-eval-pipeline.excalidraw](./diagrams/04-eval-pipeline.excalidraw) |
| 5-minute demo path | [diagrams/05-interview-demo-flow.excalidraw](./diagrams/05-interview-demo-flow.excalidraw) |

Legacy healthcare architecture: [../architecture/healthcare-automation-architecture.excalidraw](../architecture/healthcare-automation-architecture.excalidraw)

---

## Recommended demo path (5 min)

1. Open live demo → switch vertical to **HR**
2. **My Agents** → *New hire onboarding runbook* → show trigger + action pipeline
3. **AI Chat** → ask a policy question or *"create onboarding workflow when start date is set"*
4. Header role switch → **PM** → **Testing Dashboard** → show eval failure + drift review
5. Reference [06 — Backend Architecture](./06-backend-architecture.md) for production plan

Full script: [08 — Demo Script](./08-demo-script.md)

---

## What is real vs simulated

| Capability | Phase 0 (today) | Production target |
|------------|-----------------|-------------------|
| Flow editor & templates | ✅ UI + in-memory state | Flow API + Postgres + versioning |
| Activate / test run | ✅ UI toggle + mock panel | Orchestrator + connector execution |
| AI chat | ⚠️ Keyword / glossary matching | RAG + LLM + tool planner |
| Testing dashboard | ⚠️ Seeded mock metrics | Eval service + telemetry pipeline |
| Integrations | ⚠️ Copy & config panels only | Connector hub (Slack, Teams, HRIS, Jira) |

---

## Repository structure

```
src/
├── App.jsx                 # Orchestrator: views, flows, roles, verticals
├── components/             # Editor, discovery, glossaries, AI chat
├── data/                   # Vertical catalogs (triggers, actions, templates)
└── testing-dashboard/      # PM/Admin eval & observability UI
docs/
├── interview/              # ← This package
└── architecture/           # Legacy healthcare diagram
```

---

## Contact & context

Built as an internal EX platform exploration for **HR process automation** (primary) and **Marketing operations** (secondary). Intended for product discovery, stakeholder alignment, and architecture review—not production PHI or live HRIS data.
