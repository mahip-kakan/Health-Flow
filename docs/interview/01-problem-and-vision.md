# 01 — Problem & Vision

## Problem statement

Impact Analytics HR and Marketing teams repeatedly execute the same multi-step handoffs:

- **HR:** onboarding checklists, JD drafting, interview debriefs, policy Q&A, HRIS exception remediation  
- **Marketing:** post-campaign debriefs, content repurposing, experiment readouts, event follow-up

Today these processes span Slack, Teams, email, Jira, HRIS, and ad-hoc documents. There is no unified **employee-facing action layer** or **low-code builder** for process owners to compose, govern, and measure automations.

## Vision

Build an internal **Workflow Studio** — a governed EX automation platform with three pillars:

| Pillar | Description |
|--------|-------------|
| **Agent Studio** | Low-code composer: trigger → ordered actions, versioned and publishable |
| **EX Assistant** | Conversational interface for employees: policy answers, workflow creation, glossary |
| **Quality Platform** | Eval suites, drift monitoring, load testing, and governance controls |

## Strategic goals

1. **Reduce manual handoffs** in HR onboarding and TA workflows by 40%+ (target TBD with HR ops)
2. **Accelerate Marketing ops** debrief and repurposing cycles from days to hours
3. **Establish AI quality gates** before any agent or flow reaches employees
4. **Reuse one platform engine** across verticals (HR, Marketing) with different catalogs and knowledge bases

## Personas

| Persona | Role in system | Primary surfaces |
|---------|----------------|----------------|
| **Process owner** (HR ops, Marketing ops) | Builds and publishes flows | Agent Studio, Discover, My Agents |
| **Employee** | Self-service questions and tasks | AI Chat, Glossary |
| **PM / Platform admin** | Eval quality, thresholds, drift | Testing Dashboard |
| **Developer** | Extends connectors and catalogs | Flow editor (Developer role) |
| **IT / Security** | Governance, model routing, audit | AI Governance (IT/SaaS vertical preview) |

## Scope

### In scope (Phase 0 prototype)

- Visual flow editor with trigger + action pipeline  
- Vertical workspaces: HR (primary), Marketing (secondary), Healthcare & IT/SaaS (breadth)  
- AI chat with glossary lookup and template routing (simulated intelligence)  
- Testing Dashboard with eval, load, drift, and observability mock data  
- Architecture and API design for production backend  

### Out of scope (Phase 0)

- Live HRIS, Jira, or Slack integrations  
- Production LLM/RAG pipeline  
- Persistent flow storage across browser sessions (in-memory only today)  
- PHI, clinical data, or regulated healthcare production use  

## Positioning for stakeholders

> "We are not building a chatbot. We are prototyping the **EX automation platform** — how process owners compose governed workflows, how employees self-serve, and how platform teams measure AI quality before anything ships."

## Success metrics (production targets)

| Metric | Definition | Initial target |
|--------|------------|----------------|
| Task completion rate | % of EX agent requests fully resolved without ticket | ≥ 70% |
| Time to first workflow | Process owner publishes first automation | < 2 hours |
| Eval pass rate at publish | Flows blocked if eval suite fails | 100% gate |
| HR onboarding cycle time | Start date set → all tasks assigned | −30% vs baseline |
| Marketing debrief latency | Campaign end → debrief posted | < 24 hours |

## Related diagrams

- [Platform overview](./diagrams/01-platform-overview.excalidraw)  
- [Roadmap phases](./09-roadmap-phases.md)
