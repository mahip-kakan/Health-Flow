#!/usr/bin/env python3
"""Generate Excalidraw architecture diagrams for Workflow Studio interview docs."""

import json
import random
from pathlib import Path

OUT = Path(__file__).parent
TS = 1710000000000


def seed(base):
    return base + random.randint(0, 9999)


def text(el_id, x, y, content, font_size=14, color="#1e40af", width=800, height=24):
    return {
        "type": "text",
        "version": 1,
        "versionNonce": seed(1000),
        "isDeleted": False,
        "id": el_id,
        "fillStyle": "solid",
        "strokeWidth": 1,
        "strokeStyle": "solid",
        "roughness": 0,
        "opacity": 100,
        "angle": 0,
        "x": x,
        "y": y,
        "strokeColor": color,
        "backgroundColor": "transparent",
        "width": width,
        "height": height,
        "seed": seed(2000),
        "groupIds": [],
        "frameId": None,
        "roundness": None,
        "boundElements": None,
        "updated": TS,
        "link": None,
        "locked": False,
        "fontSize": font_size,
        "fontFamily": 2,
        "text": content,
        "textAlign": "left",
        "verticalAlign": "top",
        "containerId": None,
        "originalText": content,
        "lineHeight": 1.25,
    }


def rect(el_id, x, y, w, h, fill, stroke, bound=None):
    return {
        "type": "rectangle",
        "version": 1,
        "versionNonce": seed(3000),
        "isDeleted": False,
        "id": el_id,
        "fillStyle": "solid",
        "strokeWidth": 2,
        "strokeStyle": "solid",
        "roughness": 1,
        "opacity": 100,
        "angle": 0,
        "x": x,
        "y": y,
        "strokeColor": stroke,
        "backgroundColor": fill,
        "width": w,
        "height": h,
        "seed": seed(4000),
        "groupIds": [],
        "frameId": None,
        "roundness": {"type": 3},
        "boundElements": bound or [],
        "updated": TS,
        "link": None,
        "locked": False,
    }


def arrow(el_id, x, y, dx, dy, stroke="#1e3a5f", start_bind=None, end_bind=None):
    binds = []
    if start_bind:
        binds.append({"id": start_bind, "type": "rectangle"})
    if end_bind:
        binds.append({"id": end_bind, "type": "rectangle"})
    return {
        "type": "arrow",
        "version": 1,
        "versionNonce": seed(5000),
        "isDeleted": False,
        "id": el_id,
        "fillStyle": "solid",
        "strokeWidth": 2,
        "strokeStyle": "solid",
        "roughness": 1,
        "opacity": 100,
        "angle": 0,
        "x": x,
        "y": y,
        "strokeColor": stroke,
        "backgroundColor": "transparent",
        "width": dx,
        "height": dy,
        "seed": seed(6000),
        "groupIds": [],
        "frameId": None,
        "roundness": {"type": 2},
        "boundElements": None,
        "updated": TS,
        "link": None,
        "locked": False,
        "points": [[0, 0], [dx, dy]],
        "lastCommittedPoint": None,
        "startBinding": {"elementId": start_bind, "focus": 0, "gap": 4} if start_bind else None,
        "endBinding": {"elementId": end_bind, "focus": 0, "gap": 4} if end_bind else None,
        "startArrowhead": None,
        "endArrowhead": "arrow",
    }


def save(name, elements):
    doc = {
        "type": "excalidraw",
        "version": 2,
        "source": "https://excalidraw.com",
        "elements": elements,
        "appState": {
            "gridSize": None,
            "viewBackgroundColor": "#ffffff",
        },
        "files": {},
    }
    path = OUT / name
    path.write_text(json.dumps(doc, indent=2))
    print(f"Wrote {path}")


def platform_overview():
    els = [
        text("t-title", 120, 20, "Workflow Studio — Platform Overview (Internal EX)", 24, "#1a1a2e", 960, 36),
        text("t-sub", 120, 52, "Four-layer architecture: Experience → Orchestration → AI Platform → Data & Integrations", 13, "#64748b", 960, 20),
    ]
    layers = [
        ("lane-exp", 80, 90, "#e3f2fd", "#1565c0", "1 · Experience Layer", "React SPA: Agent Studio · EX Chat · Testing Dashboard · Glossaries\nPersonas: Builder · Employee · PM/Admin · Verticals: HR · Marketing"),
        ("lane-orch", 80, 230, "#fff3e0", "#c2410c", "2 · Orchestration Layer", "API Gateway · Flow/Agent API · Execution API · Workflow Orchestrator\nEvent Ingest (HRIS, Jira, Scheduler) · Connector Hub · Run Audit Log"),
        ("lane-ai", 80, 370, "#ede9fe", "#6d28d9", "3 · AI Platform Layer", "Model Gateway · RAG Retrieval · Intent Planner · Prompt Registry\nGuardrails · Tool Router (MCP-compatible) · Eval Service"),
        ("lane-data", 80, 510, "#ecfdf5", "#047857", "4 · Data & Integrations Layer", "PostgreSQL (flows, runs, evals) · Vector DB (handbooks, playbooks)\nRedis · Object Storage · Event Bus · Slack · Teams · HRIS · Jira"),
    ]
    y = 90
    prev = None
    for lid, x, _, fill, stroke, label, body in layers:
        els.append(rect(lid, x, y, 1120, 120, fill, stroke))
        els.append(text(f"{lid}-lbl", x + 16, y + 8, label, 15, stroke))
        els.append(text(f"{lid}-body", x + 16, y + 36, body, 13, "#374151", 1080, 70))
        if prev:
            els.append(arrow(f"a-{prev}-{lid}", x + 560, y - 18, 0, 18, stroke, prev, lid))
        prev = lid
        y += 140
    save("01-platform-overview.excalidraw", els)


def hr_onboarding_sequence():
    els = [
        text("t-title", 80, 20, "HR Flow — New Hire Onboarding Runbook (Runtime Sequence)", 22, "#1a1a2e", 1000, 32),
        text("t-sub", 80, 50, "Trigger: employee.start_date_set (HRIS webhook) → linear action pipeline with async orchestration", 13, "#64748b", 1000, 20),
    ]
    boxes = [
        ("b-hris", 40, 120, 160, 72, "#fed7aa", "#c2410c", "HRIS\n(BambooHR /\nWorkday)"),
        ("b-bus", 240, 120, 140, 72, "#dbeafe", "#1e40af", "Event Bus\n(Kafka / SQS)"),
        ("b-orch", 420, 120, 160, 72, "#fff3e0", "#c2410c", "Orchestrator\n(run #8842)"),
        ("b-task", 620, 120, 150, 72, "#a7f3d0", "#047857", "Step 1\nCreate onboarding\nchecklist tasks"),
        ("b-teams", 820, 120, 150, 72, "#a7f3d0", "#047857", "Step 2\nNotify Teams\n#onboarding"),
        ("b-email", 1020, 120, 150, 72, "#a7f3d0", "#047857", "Step 3\nSend welcome\nemail"),
    ]
    ids = []
    for bid, x, y, w, h, fill, stroke, label in boxes:
        els.append(rect(bid, x, y, w, h, fill, stroke))
        els.append(text(f"{bid}-t", x + 10, y + 12, label, 12, "#374151", w - 20, h - 20))
        ids.append(bid)
    for i in range(len(ids) - 1):
        a = ids[i]
        b = ids[i + 1]
        els.append(arrow(f"arr-{i}", boxes[i][1] + boxes[i][3], boxes[i][2] + 36, boxes[i + 1][1] - (boxes[i][1] + boxes[i][3]), 0, "#1e3a5f", a, b))
    els.append(rect("b-studio", 420, 240, 520, 100, "#e3f2fd", "#1565c0"))
    els.append(text("b-studio-t", 440, 258, "Workflow Studio UI (Phase 0 prototype)\nFlow definition stored → published → matched on event → run status streamed to Observability dashboard", 13, "#374151", 480, 70))
    els.append(arrow("a-orch-studio", 500, 192, 0, 48, "#1565c0", "b-orch", "b-studio"))
    save("02-hr-onboarding-sequence.excalidraw", els)


def backend_architecture():
    els = [
        text("t-title", 60, 16, "Target Backend Architecture — Workflow Studio Production", 22, "#1a1a2e", 1100, 32),
        text("t-sub", 60, 46, "Services, APIs, and stores required to productionize the Phase 0 front-end prototype", 13, "#64748b", 1100, 20),
    ]
    # Client
    els.append(rect("client", 60, 80, 200, 80, "#e3f2fd", "#1565c0"))
    els.append(text("client-t", 75, 100, "React SPA\n(Workflow Studio)", 13, "#374151", 170, 50))
    # Gateway
    els.append(rect("gw", 320, 80, 180, 80, "#dbeafe", "#1e40af"))
    els.append(text("gw-t", 335, 100, "API Gateway\nAuth · RBAC · Rate limit", 13, "#374151", 150, 50))
    els.append(arrow("a-c-gw", 260, 120, 60, 0, "#1e3a5f", "client", "gw"))
    services = [
        ("svc-flow", 540, 60, "Flow API\nPOST /flows · publish · version"),
        ("svc-run", 540, 160, "Execution API\nPOST /runs · test · status"),
        ("svc-chat", 760, 60, "Chat API\nPOST /chat · RAG · tools"),
        ("svc-eval", 760, 160, "Eval API\nsuites · regression · drift"),
    ]
    for sid, x, y, label in services:
        els.append(rect(sid, x, y, 180, 70, "#fff3e0", "#c2410c"))
        els.append(text(f"{sid}-t", x + 12, y + 14, label, 12, "#374151", 156, 50))
        els.append(arrow(f"a-gw-{sid}", 500, 120, 40 if x < 700 else 260, y - 80 if y < 120 else 60, "#1e3a5f", "gw", sid))
    # Orchestrator + AI
    els.append(rect("orch", 540, 280, 200, 90, "#fed7aa", "#c2410c"))
    els.append(text("orch-t", 555, 298, "Workflow Orchestrator\n(Temporal / Step Functions)\nRetries · idempotency · audit", 12, "#374151", 170, 60))
    els.append(rect("ai", 780, 280, 200, 90, "#ddd6fe", "#6d28d9"))
    els.append(text("ai-t", 795, 298, "AI Platform\nModel Gateway · RAG · Planner\nPrompt Registry · Guardrails", 12, "#374151", 170, 60))
    els.append(arrow("a-run-orch", 630, 230, 0, 50, "#c2410c", "svc-run", "orch"))
    els.append(arrow("a-chat-ai", 850, 130, 0, 150, "#6d28d9", "svc-chat", "ai"))
    # Connectors
    els.append(rect("conn", 540, 420, 440, 80, "#ecfdf5", "#047857"))
    els.append(text("conn-t", 555, 440, "Connector Hub (MCP-compatible tools): Slack · Teams · Email · Jira · HRIS · LLM tools · Internal Tasks", 13, "#374151", 410, 40))
    els.append(arrow("a-orch-conn", 640, 370, 0, 50, "#047857", "orch", "conn"))
    # Data stores
    stores = [
        ("pg", 60, 420, "PostgreSQL\nflows · runs · evals · audit"),
        ("vec", 60, 520, "Vector DB\nHR handbook · marketing playbooks"),
        ("queue", 280, 420, "Event Bus + Queue\nwebhooks · async jobs"),
        ("obs", 280, 520, "Observability\nDatadog · traces · token cost"),
    ]
    for sid, x, y, label in stores:
        els.append(rect(sid, x, y, 200, 70, "#f1f5f9", "#64748b"))
        els.append(text(f"{sid}-t", x + 12, y + 16, label, 12, "#374151", 176, 40))
    els.append(arrow("a-orch-pg", 540, 330, -280, 120, "#64748b", "orch", "pg"))
    els.append(arrow("a-ai-vec", 780, 370, -520, 180, "#64748b", "ai", "vec"))
    save("03-backend-architecture.excalidraw", els)


def eval_pipeline():
    els = [
        text("t-title", 80, 20, "AI Evaluation Pipeline — Quality Gate Before Publish", 22, "#1a1a2e", 900, 32),
        text("t-sub", 80, 50, "Maps to Testing Dashboard screens: AI Model Testing · Orchestration · Observability", 13, "#64748b", 900, 20),
    ]
    steps = [
        ("s1", 60, 100, "Golden Dataset\n(HR: 36 Q&A · Mkt: 32 · policy + routing)", "#fed7aa", "#c2410c"),
        ("s2", 300, 100, "Offline Eval Run\nRAG accuracy · template routing · refusal tests", "#dbeafe", "#1e40af"),
        ("s3", 540, 100, "Score vs Threshold\nglossary ≥95% · routing ≥90%", "#fef3c7", "#b45309"),
        ("s4", 780, 100, "Gate Decision\nPASS → publish flow\nFAIL → block + alert PM", "#fee2e2", "#dc2626"),
        ("s5", 1020, 100, "Testing Dashboard\nPM/Admin observability UI", "#a7f3d0", "#047857"),
    ]
    for i, (sid, x, y, label, fill, stroke) in enumerate(steps):
        els.append(rect(sid, x, y, 200, 80, fill, stroke))
        els.append(text(f"{sid}-t", x + 12, y + 16, label, 12, "#374151", 176, 50))
        if i > 0:
            prev = steps[i - 1][0]
            px = steps[i - 1][1] + 200
            els.append(arrow(f"a-{i}", px, y + 40, x - px, 0, "#1e3a5f", prev, sid))
    els.append(rect("online", 300, 240, 620, 90, "#ede9fe", "#6d28d9"))
    els.append(text("online-t", 320, 258, "Online loop (post-deploy): user feedback · drift checks · prompt regression on model/prompt change\nLLM-as-judge for subjective cases · trajectory scoring for multi-step agent runs", 13, "#374151", 580, 60))
    els.append(arrow("a-dash-online", 1120, 180, -200, 120, "#6d28d9", "s5", "online"))
    save("04-eval-pipeline.excalidraw", els)


def demo_flow():
    els = [
        text("t-title", 80, 20, "5-Minute Interview Demo Path", 22, "#1a1a2e", 700, 32),
        text("t-sub", 80, 50, "Live: mahip-kakan.github.io/Work-Flow/ — switch to HR vertical · then PM role", 13, "#64748b", 900, 20),
    ]
    steps = [
        ("d1", "0:00", "Open demo · HR vertical", "Home — featured templates"),
        ("d2", "0:45", "My Agents → Onboarding runbook", "Flow editor: trigger + 3 actions"),
        ("d3", "1:45", "AI Chat", "Policy Q or 'create onboarding workflow'"),
        ("d4", "2:45", "Switch role → PM", "Testing Dashboard opens"),
        ("d5", "3:45", "AI Model Testing", "Show eval fail + drift review"),
        ("d6", "4:30", "Close", "Backend architecture + Phase 1 roadmap"),
    ]
    y = 100
    for sid, time, title, detail in steps:
        els.append(rect(sid, 80, y, 1040, 56, "#e3f2fd" if sid != "d6" else "#ecfdf5", "#1565c0" if sid != "d6" else "#047857"))
        els.append(text(f"{sid}-t", 100, y + 10, f"{time}  {title}", 14, "#1e40af", 400, 20))
        els.append(text(f"{sid}-d", 100, y + 30, detail, 12, "#64748b", 1000, 18))
        y += 68
    save("05-interview-demo-flow.excalidraw", els)


if __name__ == "__main__":
    platform_overview()
    hr_onboarding_sequence()
    backend_architecture()
    eval_pipeline()
    demo_flow()
