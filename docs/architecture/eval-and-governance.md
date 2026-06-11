# Eval & Governance

Quality and governance framework mapped from the Testing Dashboard prototype to production platform services.

**Diagram:** [Architecture overview — eval pipeline](./README.md#ai-evaluation-pipeline) (renders on GitHub)

---

## Philosophy

AI-powered EX automations fail in production when teams ship on **demo quality**, not **measured quality**. This platform treats evaluation as a **publish gate**, not a post-mortem.

Three evaluation modes:

| Mode | When | Purpose |
|------|------|---------|
| **Offline eval** | Pre-publish, CI, prompt/model change | Block bad releases |
| **Online eval** | Production sampling | Detect drift and regressions |
| **Human review** | Edge cases, failed evals | Ground truth for suite improvement |

---

## Testing Dashboard → production mapping

| Prototype screen | Production service | Data source |
|------------------|-------------------|-------------|
| Dashboard overview | Metrics aggregator | Eval + run + chat telemetry |
| Test Orchestration | CI/CD gate service | GitHub Actions / internal pipeline |
| AI Model Testing | Eval Service | Golden datasets + scoring jobs |
| Load & Performance | Load test runner | k6 / Locust scheduled runs |
| Observability | Trace + drift analyzer | OpenTelemetry + statistical baselines |
| Settings | Platform config API | Thresholds, model routing, feature flags |
| AI Governance (IT view) | Admin control plane | Org-wide AI policy |

---

## Eval suites (by vertical)

### HR

| Suite | Threshold | Test count | Prototype score |
|-------|-----------|------------|-----------------|
| HR glossary accuracy | ≥ 92% | 36 | 94% ✅ |
| HR template routing | ≥ 88% | 22 | 91% ✅ |
| TA handoff prompts (v1) | ≥ 90% | 40 | 86% ❌ |

### Marketing

| Suite | Threshold | Test count | Prototype score |
|-------|-----------|------------|-----------------|
| Brand & campaign glossary | ≥ 93% | 32 | 95% ✅ |
| Recipe template routing | ≥ 90% | 18 | 93% ✅ |
| Copy / CTA prompt regression | ≥ 90% | 44 | 87% ❌ |

### Healthcare (reference)

| Suite | Threshold | Prototype score |
|-------|-----------|-----------------|
| Glossary accuracy | ≥ 95% | 96% ✅ |
| Template routing | ≥ 90% | 92% ✅ |
| Prompt regression (v2) | ≥ 90% | 88% ❌ |

Source: `src/testing-dashboard/TestingDashboardApp.jsx` seed constants

---

## Prompt test categories

Each vertical includes standardized prompt tests:

| Test type | Example input | Expected behavior |
|-----------|---------------|-------------------|
| **Glossary term** | "What is a requisition?" | Definition from HR glossary with example |
| **Intent — workflow** | "Create onboarding when start date is set" | Route to onboarding template |
| **Out of scope** | "Diagnose my chest pain" / "What's the weather?" | Safe refusal + appropriate redirect |

Production: these become **regression fixtures** in the eval service, run on every prompt or model version change.

---

## Evaluation pipeline (offline)

```
Golden dataset (curated Q&A + intent + routing cases)
        ↓
Eval runner executes full pipeline (RAG + planner + mock tools)
        ↓
Scorers:
  · Exact match (glossary)
  · Citation overlap (RAG)
  · Template ID match (routing)
  · LLM-as-judge (subjective quality)
        ↓
Aggregate score vs threshold per suite
        ↓
Gate: PASS → allow publish  |  FAIL → block + notify PM
        ↓
Results → Testing Dashboard API
```

---

## Drift monitoring (online)

Prototype drift checks (HR example):

| Check | Baseline | Current | Status |
|-------|----------|---------|--------|
| HR glossary term match rate | 94% | 93.6% | OK |
| Template mix (onboarding vs offer vs HRIS) | Onboarding 45% | 42% | OK |
| No-match fallback rate | 14% | 19% | **Review** |

Production implementation:

- Weekly batch comparison vs 30-day rolling baseline  
- Alert when delta exceeds configurable threshold  
- PM dashboard surfaces "review" state (matches prototype UI)  

---

## Load testing

Prototype scenarios (HR):

| Scenario | p95 latency | RPS | Status |
|----------|-------------|-----|--------|
| HR chat send (40 concurrent) | 1.1s | 38 | Pass |
| HRIS glossary lookup (80/s) | 0.09s | 80 | Pass |
| HR template match + create (15/s) | 0.55s | 15 | Pass |

Production: scheduled k6 runs against staging; block releases if p95 exceeds SLO.

---

## Governance controls

### AI Governance dashboard (IT/SaaS vertical preview)

Production control plane capabilities:

| Control | Description |
|---------|-------------|
| Model routing | Select LLM provider per vertical or use case |
| Feature toggles | Enable/disable RAG, tool use, external connectors |
| Permission scoping | Which roles can publish flows; which data sources RAG can access |
| Audit log | Every chat query, flow publish, run execution |
| Cost caps | Token budget per team per month |
| Red teaming | Scheduled adversarial prompt tests |

Maps to enterprise patterns (e.g., centralized AI control consoles in modern EX platforms).

### Human-in-the-loop gates

| Flow | Gate |
|------|------|
| JD generator | TA must approve before Jira/HCM post |
| Policy QA | Edge cases escalate to HRBP; no auto-send below confidence threshold |
| Marketing copy | Brand reviewer task before external publish |

### Guardrails (runtime)

- Input: prompt injection detection, PII scrubbing  
- Retrieval: ACL enforcement on every chunk  
- Output: citation required for policy answers; refusal templates for OOS  
- Action: sandbox mode for test runs; production requires published flow version  

---

## Metrics that matter

| Metric | Type | Target |
|--------|------|--------|
| Glossary accuracy | Offline eval | ≥ threshold per vertical |
| Template routing accuracy | Offline eval | ≥ 90% |
| Task completion rate | Online | ≥ 70% |
| Fallback / no-match rate | Drift | < 15%; alert above |
| p95 chat latency | Load | < 2s |
| Eval pass rate at publish | Gate | 100% (block on fail) |
| User satisfaction (CSAT) | Online | ≥ 4.2 / 5 |

---

## Implementation priority

1. **Golden datasets** for HR glossary + routing (unblocks Phase 2)  
2. **Publish gate** integrated with Flow API  
3. **Drift jobs** on weekly schedule  
4. **LLM-as-judge** for subjective prompt tests  
5. **Governance admin UI** (extend IT/SaaS preview to all verticals)  
