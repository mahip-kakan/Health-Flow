# 03 — HR Flow Catalog

Primary interview vertical. All flows documented here exist in the prototype (`src/data/`, `App.jsx` seeds, HR product pillars).

## HR pillars (Discover → Product Flows)

| Pillar | Module ID | Agent count | Focus |
|--------|-----------|-------------|-------|
| HRBP & Employee Lifecycle | `HRBP & Employee Lifecycle` | 3 | Policy QA, manager triage, lifecycle changes |
| Talent Acquisition | `Talent Acquisition` | 5 | JD, debrief, req kickoff, feedback SLA, offer handoff |
| People Ops & Systems | `People Ops & Systems` | 3 | Onboarding runbook, T-minus scheduling, HRIS remediation |

---

## Featured flows (flagship — demo these first)

### 1. JD generator

| Field | Value |
|-------|-------|
| **ID** | `hr-flow-jd-generator` |
| **Module** | Talent Acquisition |
| **Status** | Active |
| **Business outcome** | Structured JD ready for TA review and Jira/HCM posting |

**Trigger:** `hiring-request-raised` — When hiring request is raised (headcount/backfill approved)

| Step | Action | Integration |
|------|--------|-------------|
| 1 | Run Claude — JD draft | LLM tool (requisition notes → structured JD) |
| 2 | Create TA review task | Internal task system |
| 3 | Post draft to Slack | Slack `#recruiting` |

**Human-in-the-loop:** Recruiter validates tone, DEI language before external posting.

---

### 2. Interview debrief

| Field | Value |
|-------|-------|
| **ID** | `hr-flow-interview-debrief` |
| **Module** | Talent Acquisition |
| **Status** | Inactive (template) |

**Trigger:** `interview-session-completed` — Calendar ended; panel notes and transcript available

| Step | Action | Integration |
|------|--------|-------------|
| 1 | Run Claude — scorecard draft | Calendar + rubric + notes → structured scorecard |
| 2 | Create hiring manager review task | Internal task system |
| 3 | Send Teams update | Teams hiring thread / Notion link |

---

### 3. Onboarding plan

| Field | Value |
|-------|-------|
| **ID** | `hr-flow-onboarding-plan` |
| **Module** | People Ops & Systems |
| **Status** | Inactive (template) |

**Trigger:** `offer-accepted` — Candidate signed offer

| Step | Action | Integration |
|------|--------|-------------|
| 1 | Run Claude — 30-60-90 + kit | Role-specific plan, handbook, benefits, IT checklist |
| 2 | Assign manager onboarding tasks | Internal task system |
| 3 | Notify Slack + Drive kit | Slack `#onboarding` + shared Drive folder |

---

### 4. Policy QA bot

| Field | Value |
|-------|-------|
| **ID** | `hr-flow-policy-qa` |
| **Module** | HRBP & Employee Lifecycle |
| **Status** | Inactive (template) |

**Trigger:** `employee-policy-question` — Question in HR portal, Teams, or email

| Step | Action | Integration |
|------|--------|-------------|
| 1 | Run Claude — HR docs RAG | Vector retrieval over handbook; citations required |
| 2 | Send answer email | Email with source links and effective dates |
| 3 | Log interaction in HR portal | Audit trail; optional HRBP handoff |

**Guardrail:** No legal advice; escalate edge cases to HRBP.

---

## Seeded flows (My Agents — default library)

### 5. New hire onboarding runbook

| Field | Value |
|-------|-------|
| **ID** | `hr-1` |
| **Status** | Active |
| **Best for demo** | ✅ Primary demo flow |

**Trigger:** `start-date-set` — Confirmed start date in HRIS

| Step | Action |
|------|--------|
| 1 | Create onboarding checklist (IT, facilities, hiring manager) |
| 2 | Send Teams message to onboarding channel |
| 3 | Send welcome email (first-day logistics, paperwork) |

**Production event:** `employee.start_date_set` → HRIS webhook

---

### 6. Offer approval chain

| Field | Value |
|-------|-------|
| **ID** | `hr-2` |
| **Status** | Inactive |

**Trigger:** `requisition-approved` — Open headcount approved

| Step | Action |
|------|--------|
| 1 | Create approval tasks (Comp, HRBP, Finance) |
| 2 | Send Teams message to approvers |
| 3 | Push in-app notification in HR portal |

---

### 7. HRIS duplicate record remediation

| Field | Value |
|-------|-------|
| **ID** | `hr-3` |
| **Status** | Inactive |

**Trigger:** `hris-data-exception` — Duplicate profile, missing manager, invalid job code

| Step | Action |
|------|--------|
| 1 | Run HRIS data quality check |
| 2 | Export exception list (CSV) |
| 3 | Assign remediation owner (People ops analyst) |

---

## Product pillar agents (additional curated)

### HRBP & Employee Lifecycle

| ID | Name | Trigger | Actions (summary) |
|----|------|---------|---------------------|
| `hr-flow-policy-qa` | Policy QA bot | Employee policy question | RAG → email → audit log |
| `hrbp-1` | Manager policy question triage | Manager request submitted | HRBP task → Teams → in-app notify |
| `hrbp-2` | Lifecycle change — manager briefing | Lifecycle change in HRIS | Email manager → checklist tasks |

### Talent Acquisition

| ID | Name | Trigger | Actions (summary) |
|----|------|---------|---------------------|
| `hr-flow-jd-generator` | JD generator | Hiring request raised | Claude JD → TA task → Slack |
| `hr-flow-interview-debrief` | Interview debrief | Interview completed | Claude scorecard → HM task → Teams |
| `ta-1` | Req opened to kickoff recruiting | Requisition approved | Slack → recruiter task → email HM |
| `ta-2` | Interview feedback SLA nudge | Interview round completed | Reminder → Teams ping HM |
| `ta-3` | Offer accepted — handoff to People ops | Offer accepted | Welcome email → onboarding task → IT Teams |

### People Ops & Systems

| ID | Name | Trigger | Actions (summary) |
|----|------|---------|---------------------|
| `hr-flow-onboarding-plan` | Onboarding plan | Offer accepted | Claude plan → manager tasks → Slack |
| `po-1` | T-minus onboarding runbook | T-minus before start date | Sub-tasks by offset → Teams status |
| `po-2` | HRIS duplicate record remediation | HRIS data exception | DQ check → CSV export → assign owner |

---

## HR trigger catalog (available in Agent Studio)

| Category | Example triggers |
|----------|------------------|
| Schedule | On a schedule · T-minus before start date · Quarterly access review |
| Employee lifecycle | HR case opened · Lifecycle change in HRIS · Manager request · Policy question |
| Talent | Hiring request raised · Requisition approved · Interview completed · Offer accepted |
| Data & systems | HRIS data exception · Integration sync failure |

Source: `src/data/triggersHr.js`

---

## HR action catalog (available in Agent Studio)

| Category | Example actions |
|----------|-----------------|
| Notifications | Slack · Teams · Email · In-app notification |
| Tasks & workflows | Create onboarding task · Export CSV · HRIS data quality check |
| Talent automation | Interview reminder · JD generator (Claude) · Debrief (Claude) · Policy RAG (Claude) |

Source: `src/data/actionsHr.js`

---

## AI chat intent routing (HR)

The EX assistant maps natural language to templates:

| User intent keywords | Routed template |
|---------------------|-----------------|
| jd, job description, jira, hcm | JD generator |
| debrief, scorecard, panel notes | Interview debrief |
| 30-60-90, onboarding plan | Onboarding plan |
| policy, handbook question | Policy QA bot |
| onboard, new hire, start date | New hire onboarding runbook |

Source: `src/components/AIChatPanel.jsx`

---

## Diagrams

- [HR onboarding runtime sequence](./diagrams/02-hr-onboarding-sequence.excalidraw)  
- [Backend architecture](./06-backend-architecture.md)
