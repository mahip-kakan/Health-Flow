# 02 — Product Surfaces

Every navigable surface in Workflow Studio, mapped to product purpose and persona.

## Global controls

| Control | Values | Behavior |
|---------|--------|----------|
| **Vertical** | Healthcare · HR · Marketing · IT/SaaS | Swaps trigger/action catalogs, glossaries, templates, testing seed data. Persisted in `localStorage`. |
| **Role** | Developer · PM · Admin | PM/Admin auto-navigate to Testing Dashboard. Developer sees builder surfaces. |

## Navigation surfaces

| View key | Sidebar label | Persona | Purpose |
|----------|-----------------|---------|---------|
| `home` | Home | All | AI landing: featured templates, product pillars, quick-create |
| `analytics` | Analytics | Leadership | Engagement and automation metrics dashboard |
| `discover` | Discover | Process owners | Browse templates by category and product module |
| `my-flows` | My Agents | Builders | Saved flows for active vertical; edit, activate |
| `product-flows` | — | Builders | Module-specific agent library (from Discover → product) |
| `editor` | — | Builders | Visual flow canvas + trigger/action/config panels |
| `glossary` | Glossary | All | Domain terminology (vertical-specific) |
| `connectors` | Connect Apps | IT/SaaS only | SaaS connector catalog |
| `ai-governance` | AI Surfaces | IT/SaaS only | AI governance dashboard preview |
| `testing-dashboard` | Testing | PM / Admin | Eval, orchestration, load, observability |

## Editor layout

When `activeView === 'editor'`:

```
┌─────────────────────────────────────────────────────────┐
│ FlowHeader — name, back, help                           │
├──────────────────────────────┬──────────────────────────┤
│ FlowCanvas                   │ Editor panel (slide-in)  │
│  · Starter (trigger)         │  · TriggerPanel          │
│  · Actions (ordered)         │  · ActionPanel           │
│  · Test run / Activate       │  · TriggerConfigPanel    │
│                              │  · ActionConfigPanel     │
└──────────────────────────────┴──────────────────────────┘
```

**Flow model:**

```json
{
  "id": "string",
  "vertical": "hr | marketing | healthcare | it-saas",
  "name": "string",
  "trigger": { "id", "name", "description", "icon", "color" } | null,
  "actions": [ /* same shape */ ],
  "isActive": boolean
}
```

## Overlay panels (global)

| Panel | Trigger | Purpose |
|-------|---------|---------|
| **AIChatPanel** | Chat assistant button | Conversational EX agent; glossary + template routing |
| **FlowHelpPanel** | Help in editor | Contextual flow documentation |
| **TestDataPanel** | Test run in canvas | Simulated execution with mock results |

## Vertical-specific content

| Vertical | Glossary source | Product flows | Special surfaces |
|----------|-----------------|---------------|------------------|
| Healthcare | `healthcareChatGlossary.js` | Clinical care, patient experience pillars | Original demo vertical |
| **HR** | `glossaryHr.js` | HRBP, TA, People Ops pillars | **Interview primary** |
| **Marketing** | `marketingTemplates.js` | Campaign, content, brand pillars | **Interview secondary** |
| IT/SaaS | `glossaryItSaas.js` | Integration builder pillars | Connectors + AI Governance |

## Testing Dashboard screens

Embedded sub-app at `src/testing-dashboard/`:

| Screen | Component | Purpose |
|--------|-----------|---------|
| Dashboard | `DashboardScreen` | Overview metrics |
| Orchestration | `OrchestrationScreen` | Test run definitions, CI-style gates |
| AI Model Testing | `AIModelScreen` | Eval suites, prompt regression |
| Load & Performance | `LoadScreen` | Concurrent chat / routing load scenarios |
| Observability | `ObservabilityScreen` | Run traces, drift checks |
| Settings | `SettingsScreen` | Thresholds, model config |

Overlay panels: New Eval, Define Workflow, Add Rule, Add Load Scenario, Add Drift Check, Add Prompt Test, Run/Eval Detail.

## Data layer (front-end catalogs)

| File pattern | Contents |
|--------------|----------|
| `triggers*.js` | Categorized trigger picklists per vertical |
| `actions*.js` | Categorized action picklists per vertical |
| `*ProductFlows.js` | Pillar-organized agent libraries |
| `hrFeaturedCopilotFlows.js` | Four flagship HR + Claude flows |
| `marketingTemplates.js` | Six marketing recipe templates |
| `saasConnectorCatalog.js` | IT/SaaS integration catalog |

## Diagram reference

- [05 — Interview demo flow](./diagrams/05-interview-demo-flow.excalidraw)
