# Marketing Flow Catalog

Secondary vertical. Six recipe templates plus product-pillar agents for campaign, content, and brand operations.

## Marketing modules

| Module | Icon theme | Focus |
|--------|------------|-------|
| Campaign & lifecycle | Megaphone | Debriefs, experiments, event follow-up |
| Content & distribution | Layers | Repurposing, multi-channel snippets |
| Brand & insights | Lightbulb | Competitor intel, brief-to-copy |

Source: `src/data/marketingTemplates.js` → `MARKETING_MODULES`

---

## Featured templates (home + discover)

### 1. Post-campaign debrief

| Field | Value |
|-------|-------|
| **ID** | `mkt-post-campaign-debrief` |
| **Category** | Campaign performance |
| **Stack** | Analytics + Claude + Slides |
| **Output** | Debrief deck with learnings |

**Trigger:** `campaign-ends` — Paid, lifecycle, or nurture campaign reaches end date

| Step | Action |
|------|--------|
| 1 | Export campaign metrics CSV |
| 2 | Email debrief outline to channel owners |
| 3 | Post recap to Marketing Teams |

---

### 2. Competitor monitoring

| Field | Value |
|-------|-------|
| **ID** | `mkt-competitor-monitoring` |
| **Category** | Market intelligence |
| **Stack** | Web search + Claude + Notion |
| **Output** | Structured intel brief |

**Trigger:** `on-schedule` — Weekly digest

| Step | Action |
|------|--------|
| 1 | Post intel summary to Slack `#competitive-intel` |
| 2 | Email weekly brief to GTM list |
| 3 | Export tracked signals CSV |

---

### 3. Content repurposing

| Field | Value |
|-------|-------|
| **ID** | `mkt-content-repurposing` |
| **Category** | Content engine |
| **Stack** | Claude + Buffer/LinkedIn |
| **Output** | 5 formats from 1 source asset |

**Trigger:** `content-published` — Blog, guide, or pillar page goes live in CMS

| Step | Action |
|------|--------|
| 1 | Notify content pod (email) |
| 2 | Notify editors in CMS (in-app) |
| 3 | Drop snippet pack in Slack |

---

### 4. Brief → copy

| Field | Value |
|-------|-------|
| **ID** | `mkt-brief-to-copy` |
| **Category** | Brand & creative |
| **Stack** | Claude + brand skill |
| **Output** | On-brand copy across formats |

**Trigger:** `brief-uploaded` — Brief doc or form in shared workspace

| Step | Action |
|------|--------|
| 1 | Create copy review task (brand reviewer) |
| 2 | Email draft to stakeholders |
| 3 | Notify brief requestor (in-app) |

---

### 5. A/B test readout

| Field | Value |
|-------|-------|
| **ID** | `mkt-ab-readout` |
| **Category** | Experimentation |
| **Stack** | Analytics + Claude + Docs |
| **Output** | Stat summary + ship/iterate recommendation |

**Trigger** `experiment-concludes` — Test window closed or significance threshold met

| Step | Action |
|------|--------|
| 1 | Validate experiment data (assignment integrity) |
| 2 | Export results CSV (variants, lifts, guardrails) |
| 3 | Post readout to experiment Teams channel |

---

### 6. Event follow-up

| Field | Value |
|-------|-------|
| **ID** | `mkt-event-follow-up` |
| **Category** | Lifecycle |
| **Stack** | CRM + Claude + Email |
| **Output** | Segmented nurture + recap email |

**Trigger:** `webinar-ends` — Webinar or field event session completed

| Step | Action |
|------|--------|
| 1 | Send recap email series (attendee vs no-show branches) |
| 2 | Create SDR follow-up tasks (high-intent accounts) |
| 3 | Optional SMS nudge for booked follow-ups |

---

## AI chat intent routing (Marketing)

| Keywords | Routed template |
|----------|-----------------|
| debrief, campaign | Post-campaign debrief |
| competitor, intel | Competitor monitoring |
| repurpose, linkedin | Content repurposing |
| brief, copy | Brief → copy |
| ab test, experiment | A/B test readout |
| webinar, event | Event follow-up |

Source: `MARKETING_AI_SUGGESTIONS` in `marketingTemplates.js`

---

## Marketing trigger catalog

| Trigger ID | Name | Use case |
|------------|------|----------|
| `campaign-ends` | When campaign ends | Debrief automation |
| `on-schedule` | On a schedule | Weekly intel digest |
| `content-published` | When long-form content is published | Repurposing |
| `brief-uploaded` | When marketing brief is uploaded | Copy generation |
| `experiment-concludes` | When A/B experiment concludes | Readout |
| `webinar-ends` | When webinar or field event ends | Follow-up nurture |

Source: `src/data/triggersMarketing.js`

---

## Production integration map

| System | Role in Marketing flows |
|--------|---------------------------|
| Analytics / BI | Campaign metrics export, experiment validation |
| CMS | Content publish events |
| CRM | Event attendee segmentation, SDR tasks |
| Slack / Teams | Team notifications and recap posts |
| Claude / LLM gateway | Debrief summaries, copy drafts, intel synthesis |
| Email / SMS | Nurture sequences and nudges |

---

## Eval thresholds (Marketing vertical)

From Testing Dashboard seed data (`TESTING_SEED_MARKETING`):

| Suite | Score | Threshold | Status |
|-------|-------|-----------|--------|
| Brand & campaign glossary | 95% | ≥ 93% | Pass |
| Recipe template routing | 93% | ≥ 90% | Pass |
| Copy / CTA prompt regression | 87% | ≥ 90% | **Fail — review required** |

---

## Related documentation

- [Marketing debrief sequence](../architecture/runtime-sequences.md#marketing-post-campaign-debrief)
- [Eval & governance](../architecture/eval-and-governance.md)
- [Architecture overview](../architecture/README.md)
