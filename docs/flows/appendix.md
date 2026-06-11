# Healthcare & IT/SaaS — Appendix

Supporting verticals demonstrating platform breadth.

---

## Healthcare (original demo vertical)

### Seeded flows (My Agents)

| ID | Name | Trigger | Actions (summary) | Active |
|----|------|---------|---------------------|--------|
| `cc-1` | Post-Discharge Follow-Up | Patient discharged (ADT) | Care plan → care task → Teams | ✅ |
| `2` | Readmission Risk Alert | Readmission risk flagged (>40%) | In-app notification | — |
| `3` | Appointment Reminder Automation | Appointment scheduled | Reminder → pre-visit instructions | ✅ |

### Use cases

Clinical care coordination, patient experience, and population health automation patterns. Includes healthcare glossary and clinical trigger/action catalogs.

**Note:** Not intended for production PHI. See [architecture overview](../architecture/README.md) for platform design.

Source: `App.jsx` seeds, `src/data/triggers.js`, `src/data/actions.js`

---

## IT/SaaS vertical

Demonstrates **integration builder** and **AI governance** surfaces relevant to platform PM roles.

### Exclusive surfaces

| Surface | Purpose |
|---------|---------|
| **Connect Apps** (`connectors`) | SaaS connector catalog — OAuth, SCIM, rate limits |
| **AI Surfaces** (`ai-governance`) | Model routing, permission scoping, audit preview |

### Product pillars

Source: `src/data/itSaasProductFlows.js`

| Pillar | Focus |
|--------|-------|
| Integration Builder | API connector generation, webhook ingestion |
| Access & Identity | Provisioning, deprovisioning, access reviews |
| ITSM & Support | Ticket routing, incident response |
| Cost & FinOps | SaaS spend alerts, license optimization |

### IT/SaaS trigger categories

Schedule · Integration events · ITSM incidents · Access & identity · Cost & governance

Source: `src/data/triggersItSaas.js`, `src/data/actionsItSaas.js`

### Glossary

IT/SaaS terminology: OAuth, SCIM, MCP, rate limiting, MTTR, SLA, etc.

Source: `src/data/glossaryItSaas.js`

---

## Cross-vertical platform principle

All verticals share:

- Same flow model (`trigger` + `actions[]`)
- Same editor, chat, and testing dashboard shells
- Different **catalogs** (triggers, actions, templates, glossaries, eval seeds)

Production backend implements vertical as a **dimension** on flow definitions, not separate products.

---

## Appendix: full vertical comparison

| Dimension | Healthcare | HR | Marketing | IT/SaaS |
|-----------|------------|-----|-----------|---------|
| Primary persona | Care coordinator | HR ops / TA | Marketing ops | IT / Platform |
| Knowledge layer | Clinical glossary | HR handbook RAG | Brand & campaign glossary | Tech + integration glossary |
| Flagship AI pattern | Care plan automation | Policy QA + JD generator | Campaign debrief | Connector builder |
| Governance surface | Clinical guardrails | HR compliance audit | Brand voice checks | AI Control Center preview |
| Documentation focus | Low | **High** | **Medium** | Medium (governance) |
