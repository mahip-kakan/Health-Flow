# Runtime Sequences

End-to-end execution flows for Workflow Studio. Diagrams render directly on GitHub (Mermaid).

**Related:** [Backend services](./backend-services.md) · [HR flow catalog](../flows/hr.md)

---

## HR onboarding runbook

**Flow ID:** `hr-1` · **Trigger:** `employee.start_date_set` (HRIS webhook)

When a start date is confirmed in HRIS, the orchestrator executes a linear action pipeline.

```mermaid
sequenceDiagram
    autonumber
    participant HRIS as HRIS<br/>(Workday / BambooHR)
    participant Bus as Event Bus
    participant Orch as Orchestrator
    participant Tasks as Internal Tasks
    participant Teams as Microsoft Teams
    participant Email as Email Service
    participant UI as Workflow Studio

    HRIS->>Bus: employee.start_date_set
    Bus->>Orch: Match flow "Onboarding runbook"
    Orch->>Orch: Create run #8842 · audit log

    Orch->>Tasks: Step 1 · Create onboarding checklist
    Tasks-->>Orch: task_ids

    Orch->>Teams: Step 2 · Post to #onboarding
    Teams-->>Orch: message_id

    Orch->>Email: Step 3 · Send welcome email
    Email-->>Orch: delivery_id

    Orch->>UI: Run status · COMPLETED
    Note over Orch,UI: Phase 0: simulated in TestDataPanel<br/>Production: SSE / webhook to Observability
```

### Action pipeline

| Step | Action | Connector |
|------|--------|-----------|
| 1 | Create onboarding checklist (IT, facilities, hiring manager) | `internal_tasks` |
| 2 | Send Teams message to onboarding channel | `microsoft_teams` |
| 3 | Send welcome email (logistics, paperwork) | `email` |

---

## Policy Q&A (EX Assistant)

**Flow ID:** `hr-flow-policy-qa` · **Trigger:** employee policy question

```mermaid
sequenceDiagram
    autonumber
    participant Emp as Employee
    participant Chat as EX Chat API
    participant Guard as Guardrails
    participant RAG as RAG Service
    participant VDB as Vector DB
    participant LLM as Model Gateway
    participant Email as Email
    participant Portal as HR Portal

    Emp->>Chat: "What is our parental leave policy?"
    Chat->>Guard: Input screening
    Guard->>RAG: Query with employee context (location, role)
    RAG->>VDB: Hybrid search + ACL filter
    VDB-->>RAG: Policy chunks + citations
    RAG->>LLM: Generate answer (grounded only)
    LLM-->>Chat: Answer + citations + confidence

    alt confidence >= threshold
        Chat->>Email: Send answer with source links
        Chat->>Portal: Log interaction · audit trail
        Chat-->>Emp: Answer displayed
    else low confidence or edge case
        Chat->>Portal: Escalate to HRBP queue
        Chat-->>Emp: "Connecting you with HR..."
    end
```

---

## JD generator (human-in-the-loop)

**Flow ID:** `hr-flow-jd-generator` · **Trigger:** hiring request raised

```mermaid
sequenceDiagram
    autonumber
    participant Jira as Jira / HCM
    participant Orch as Orchestrator
    participant LLM as Claude · JD tool
    participant Tasks as Internal Tasks
    participant Slack as Slack #recruiting
    participant TA as Recruiter

    Jira->>Orch: hiring_request.approved
    Orch->>LLM: Generate JD from requisition notes
    LLM-->>Orch: Draft JD (structured)
    Orch->>Tasks: Create TA review task
    Orch->>Slack: Post draft link + Jira ticket
    Note over TA,Slack: Human gate · recruiter approves<br/>DEI language · comp band · posting
    TA->>Jira: Approve → publish to HCM
```

---

## Marketing post-campaign debrief

**Flow ID:** `mkt-post-campaign-debrief` · **Trigger:** campaign ended

```mermaid
sequenceDiagram
    autonumber
    participant Analytics as Analytics
    participant Orch as Orchestrator
    participant Export as CSV Export
    participant Email as Email
    participant Teams as Marketing Teams

    Analytics->>Orch: campaign.ended
    Orch->>Export: Pull channel + conversion metrics
    Export-->>Orch: metrics CSV
    Orch->>Email: Debrief outline to channel owners
    Orch->>Teams: Post recap + next test ideas
```

See [Marketing flows](../flows/marketing.md).

---

## Chat intent routing (Phase 0 vs production)

### Phase 0 (prototype)

```mermaid
flowchart TD
    Msg[User message] --> Match{Keyword / glossary match?}
    Match -->|Glossary term| Glossary[Return definition]
    Match -->|Template keywords| Template[Propose flow draft]
    Match -->|No match| Fallback[Generic assistant response]
    Template --> Editor[Open in Agent Studio]
```

### Production target

```mermaid
flowchart TD
    Msg[User message] --> Auth[Auth + context]
    Auth --> Intent[Intent classifier]
    Intent -->|Question| RAG[RAG + citations]
    Intent -->|Create workflow| TMatch[Template retrieval]
    Intent -->|In-flight run| Tools[Tool execution]
    Intent -->|Out of scope| Escalate[Escalation / refusal]
    TMatch --> Draft[Flow draft → Agent Studio]
```

---

## Sandbox test run

Phase 1 adds `POST /api/v1/runs/test` — executes pipeline without external side effects.

```mermaid
sequenceDiagram
    participant Builder as Process owner
    participant API as Execution API
    participant Orch as Orchestrator
    participant Mock as Mock connectors

    Builder->>API: POST /runs/test { flow_id }
    API->>Orch: Sandbox run (no external writes)
    Orch->>Mock: Simulate each action step
    Mock-->>Orch: Step results + latency
    Orch-->>API: Run trace
    API-->>Builder: Step-by-step results in UI
```
