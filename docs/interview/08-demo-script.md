# 08 — Demo Script

5-minute live walkthrough for interviewers.  
**Live URL:** [mahip-kakan.github.io/Work-Flow/](https://mahip-kakan.github.io/Work-Flow/)

**Diagram:** [diagrams/05-interview-demo-flow.excalidraw](./diagrams/05-interview-demo-flow.excalidraw)

---

## Pre-demo checklist

- [ ] Open demo in Chrome (incognito avoids stale localStorage if needed)  
- [ ] Confirm vertical = **HR** (header dropdown)  
- [ ] Confirm role = **Developer** (to start in builder mode)  
- [ ] Have [03 — HR Flow Catalog](./03-flow-catalog-hr.md) open as reference  
- [ ] Optional: open [03-backend-architecture.excalidraw](./diagrams/03-backend-architecture.excalidraw) in Excalidraw for closing  

---

## Minute 0:00 — Open & frame (45 sec)

**Action:** Load demo. Point to header vertical selector → **HR**.

**Say:**

> "This is Workflow Studio — an internal EX automation platform we're preparing at Impact Analytics. Phase 0 is a front-end prototype; the backend architecture and eval framework are defined in our docs folder. I'll show HR workflows first because that's our primary use case."

**Action:** Briefly scan sidebar (Home, Discover, My Agents, Glossary).

---

## Minute 0:45 — Flow editor (60 sec)

**Action:** Sidebar → **My Agents** → click **New hire onboarding runbook** (or edit from list).

**Action:** Walk through canvas:

1. **Starter:** "When start date is set" (HRIS event)  
2. **Action 1:** Create onboarding checklist  
3. **Action 2:** Send Teams message  
4. **Action 3:** Send welcome email  

**Action:** Click trigger node → show config panel. Click an action → show config panel.

**Say:**

> "The model is intentionally simple: one trigger, ordered actions. Production runs this through an async orchestrator with retries and audit logs. Process owners compose flows here without engineering — same pattern as enterprise Agent Studio products."

**Optional:** Click **Activate** toggle to show publish concept.

---

## Minute 1:45 — EX Assistant (60 sec)

**Action:** Click chat bubble (bottom right) → AI Chat opens.

**Try one of:**

- "What is a requisition?" → glossary answer  
- "Create onboarding workflow when start date is set" → template proposal  

**Say:**

> "Today this uses keyword and glossary matching to simulate routing. Production replaces this with RAG over our HR handbook plus an intent planner that can propose or execute flows. Notice the out-of-scope handling — we test refusal paths in our eval suite."

**Action:** If template matched, show "create flow" path into editor.

---

## Minute 2:45 — Role switch to PM (60 sec)

**Action:** Header → change role from **Developer** to **PM**.

App auto-navigates to **Testing Dashboard**.

**Say:**

> "We designed separate personas deliberately. Builders compose flows; platform PMs own quality. This Testing Dashboard is the observability layer I'd operate before any flow reaches employees."

**Action:** Scan dashboard subtitle: *Test orchestration · AI evals · Load · Observability*

---

## Minute 3:45 — Eval & drift (45 sec)

**Action:** Navigate to **AI Model Testing** screen.

**Point out:**

- HR glossary accuracy: **94%** ✅ (threshold 92%)  
- HR template routing: **91%** ✅  
- TA handoff prompts: **86%** ❌ — **below threshold**

**Say:**

> "This failing eval is intentional in the prototype — it shows our publish gate would block a bad prompt version. We run golden datasets offline, monitor drift online, and require pass before publish."

**Action:** Open **Observability** → show drift check: fallback rate 14% → 19% = **Review**.

---

## Minute 4:30 — Close with architecture (30 sec)

**Say:**

> "Front-end validates UX and workflow patterns. Production adds four layers: orchestration with event ingest and connector hub, AI platform with model gateway and RAG, eval service as publish gate, and Postgres plus vector store for flows and knowledge. We've documented the full API surface and phased rollout in our docs/interview folder."

**Action:** Share GitHub link to `docs/interview/README.md`.

---

## Alternate paths (if interviewer asks)

| Question | Demo path |
|----------|-----------|
| "Show Marketing" | Switch vertical → Discover → Post-campaign debrief template |
| "Show governance" | Switch to IT/SaaS → AI Surfaces |
| "Show architecture" | Open Excalidraw backend diagram |
| "What's not built?" | Reference README "What is real vs simulated" table |

---

## Anticipated Q&A

**Q: Is this connected to your HRIS?**  
A: Not yet — Phase 0 is UX validation. Phase 2 adds HRIS webhooks for triggers like `employee.start_date_set`.

**Q: What LLM do you use?**  
A: Prototype simulates Claude-powered actions (JD, debrief, RAG). Production routes through a model gateway with eval gates per provider.

**Q: How do you prevent bad AI answers on policy questions?**  
A: RAG with citations only from authorized docs, confidence thresholds, human escalation, and offline eval suites — documented in eval doc.

**Q: Why build internally vs buy?**  
A: We're prototyping how Impact Analytics-specific HR and Marketing processes map to a governed agent platform. Buy vs build is a Phase 4 decision informed by this discovery.

---

## After demo

Send interviewer:

1. Link to `docs/interview/README.md`  
2. Link to live demo  
3. Optional: Excalidraw backend diagram file  
