# Architecture Overview

Target production architecture for Workflow Studio — an internal EX automation platform at Impact Analytics.

**Related docs:** [Backend services](./backend-services.md) · [Runtime sequences](./runtime-sequences.md) · [Eval & governance](./eval-and-governance.md)

All diagrams on this page use **Mermaid** and render directly on GitHub.

---

## System context

Workflow Studio sits between process owners (HR, Marketing), employees (self-service), and enterprise systems (HRIS, collaboration, LLM providers).

```mermaid
flowchart LR
    subgraph Users
        PO[Process owners]
        EMP[Employees]
        PM[Platform / PM admin]
    end

    subgraph WS["Workflow Studio"]
        Studio[Agent Studio]
        Assistant[EX Assistant]
        Quality[Testing Dashboard]
    end

    subgraph Backend["Target backend"]
        API[API Gateway]
        Orch[Orchestrator]
        AI[AI Platform]
    end

    subgraph External["Enterprise systems"]
        HRIS[HRIS]
        Collab[Slack / Teams]
        LLM[Model providers]
        KB[Handbooks / Confluence]
    end

    PO --> Studio
    EMP --> Assistant
    PM --> Quality
    Studio --> API
    Assistant --> API
    Quality --> API
    API --> Orch
    API --> AI
    Orch --> HRIS
    Orch --> Collab
    AI --> LLM
    AI --> KB
```

---

## Four-layer model

| Layer | Responsibility | Key components |
|-------|----------------|----------------|
| **1 · Experience** | Builder UI, employee chat, observability | React SPA, Testing Dashboard |
| **2 · Orchestration** | Flow lifecycle, event matching, execution | Flow API, Orchestrator, Event Ingest, Connector Hub |
| **3 · AI Platform** | Retrieval, planning, models, quality | Model Gateway, RAG, Prompt Registry, Guardrails, Eval Service |
| **4 · Data & Integrations** | Persistence, events, external systems | PostgreSQL, Vector DB, Event Bus, Job Queue, Connectors |

```mermaid
flowchart TB
    subgraph L1["1 · Experience"]
        direction LR
        E1[Agent Studio]
        E2[EX Chat]
        E3[Testing Dashboard]
    end

    subgraph L2["2 · Orchestration"]
        direction LR
        O1[API Gateway]
        O2[Flow API]
        O3[Orchestrator]
        O4[Event Ingest]
    end

    subgraph L3["3 · AI Platform"]
        direction LR
        A1[Model Gateway]
        A2[RAG]
        A3[Planner]
        A4[Eval Service]
    end

    subgraph L4["4 · Data & Integrations"]
        direction LR
        D1[(PostgreSQL)]
        D2[(Vector DB)]
        D3[Event Bus]
        D4[Connectors]
    end

    L1 --> L2
    L2 --> L3
    L2 --> L4
    L3 --> L4
```

---

## Backend service topology

Detailed API specs: [backend-services.md](./backend-services.md)

```mermaid
flowchart TB
    Client[React SPA]

    Client --> GW[API Gateway<br/>Auth · RBAC · Rate limit]

    GW --> FlowAPI[Flow / Agent API<br/>CRUD · publish · version]
    GW --> RunAPI[Execution API<br/>runs · test · status]
    GW --> ChatAPI[Chat API<br/>RAG · tools · sessions]
    GW --> EvalAPI[Eval API<br/>suites · drift · load]

    RunAPI --> Orch[Workflow Orchestrator<br/>Temporal / Step Functions]
    ChatAPI --> Planner[Intent / Tool Planner]
    Planner --> RAG[RAG Service]
    Planner --> MG[Model Gateway]
    Planner --> Conn[Connector Hub]

    Orch --> Conn
    Orch --> PG[(PostgreSQL)]
    RAG --> VDB[(Vector DB)]
    EvalAPI --> PG

    Ingest[Event Ingest<br/>HRIS · Jira · Scheduler] --> Orch
    Conn --> Slack[Slack]
    Conn --> Teams[Teams]
    Conn --> HRIS[HRIS]
    Conn --> Email[Email]
    Conn --> Tasks[Internal Tasks]
```

---

## AI evaluation pipeline

Publish gate: no flow reaches production without passing offline eval suites.

```mermaid
flowchart LR
    GD[Golden dataset] --> Run[Offline eval run]
    Run --> Score[Score vs threshold]
    Score -->|Pass| Pub[Allow publish]
    Score -->|Fail| Block[Block + alert PM]
    Pub --> Dash[Testing Dashboard]
    Block --> Dash

    Dash --> Online[Online loop]
    Online --> Drift[Drift monitoring]
    Online --> Feedback[User feedback]
    Drift --> Run
```

Full spec: [eval-and-governance.md](./eval-and-governance.md)

---

## Design principles

1. **Async execution** — multi-step runs via job queue; no blocking HTTP chains across connectors  
2. **Versioned flows** — draft → eval gate → publish; production runs pinned versions only  
3. **Permission-aware RAG** — retrieval filtered by employee role and document ACLs  
4. **Human-in-the-loop** — LLM drafts (JD, policy) require approval before external send  
5. **MCP-compatible tools** — connectors expose standardized interfaces for agent planners  
6. **Fail safe** — retries, circuit breakers, graceful degradation, audit on every run  

---

## Phase alignment

| Phase | Architecture milestone |
|-------|------------------------|
| 0 (now) | Front-end prototype only |
| 1 | Flow API + Postgres + sandbox runs |
| 2 | Orchestrator + HRIS webhooks + RAG |
| 3 | Marketing event ingest + LLM tools |
| 4 | Eval service as publish gate + governance console |
| 5 | Slack/Teams employee channels |

See [roadmap](../roadmap.md).
