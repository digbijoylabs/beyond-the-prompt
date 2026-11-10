<p align="center">
  <a href="https://digbijoylabs.com" target="_blank">
    <img src="assets/images/digbijoy_labs_logo.png" alt="Digbijoy Labs" width="280">
  </a>
</p>

<h1 align="center">Beyond the Prompt</h1>
<h3 align="center">The Architecture of Autonomous Systems</h3>
<p align="center">
  <em>Context Engineering, Graph Engineering, Loop Design, and Production AI Harnesses</em>
</p>

<p align="center">
  <strong>Jay Thorne</strong> &nbsp;|&nbsp; Published by <a href="https://digbijoylabs.com" target="_blank"><strong>Digbijoy Labs Publications</strong></a> (2026)
</p>

<p align="center">
  <a href="https://github.com/digbijoy-labs/beyond-the-prompt/actions/workflows/ci.yml"><img src="https://github.com/digbijoy-labs/beyond-the-prompt/actions/workflows/ci.yml/badge.svg" alt="CI Verification"></a>
  <a href="https://www.python.org/downloads/"><img src="https://img.shields.io/badge/python-3.12+-blue.svg" alt="Python 3.12+"></a>
  <a href="https://pydantic.dev"><img src="https://img.shields.io/badge/pydantic-v2.8+-e92063.svg" alt="Pydantic v2"></a>
  <a href="https://modelcontextprotocol.io"><img src="https://img.shields.io/badge/protocol-MCP_JSON--RPC_2.0-orange.svg" alt="Protocol: MCP"></a>
  <a href="https://opentelemetry.io"><img src="https://img.shields.io/badge/telemetry-OTel_GenAI-blueviolet.svg" alt="OpenTelemetry"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT"></a>
  <a href="https://doi.org/10.5281/zenodo.24100423"><img src="https://zenodo.org/badge/DOI/10.5281/zenodo.24100423.svg" alt="DOI: 10.5281/zenodo.24100423"></a>
</p>

<p align="center">
  <img src="assets/images/a_plus_hero_banner.png" alt="Beyond the Prompt Hero Banner" width="100%">
</p>

---

## ⚡ 30-Second Quickstart: Run the AST Agent Codebase Auditor or MCP Server

You can use this repository immediately as a **standalone CLI static auditor** or **Model Context Protocol (MCP) server** in Claude Desktop, Cursor, Windsurf, Cline, or Antigravity to audit any Python AI agent codebase for unbounded loops, unisolated `subprocess` calls, and unvalidated tool schemas:

```bash
# 1. Audit any local Python AI/agent repository from your terminal:
python -m core.auditor.harness_auditor /path/to/your/agent-repo

# 2. Or output a machine-readable JSON security & reliability scorecard:
python -m core.auditor.harness_auditor . --json
```

**Add to your IDE / Claude Desktop `mcp_config.json`:**
```json
{
  "mcpServers": {
    "agent-harness-auditor": {
      "command": "python",
      "args": ["-m", "core.auditor.mcp_server"],
      "cwd": "/path/to/beyond-the-prompt"
    }
  }
}
```
Exposes 3 MCP tools to your coding agent: `audit_agent_repository`, `calculate_loop_cost_ceiling`, and `get_architectural_invariant_kernel`.

---

## 🎯 What Is This Repository?

Reference architecture kernels for building **production AI agents** in Python — context engineering, GraphRAG knowledge-graph traversal, Model Context Protocol (MCP) host wiring, loop-damping governors, sandboxed execution, human-in-the-loop escrow, and OpenTelemetry GenAI tracing. It is the companion code for *Beyond the Prompt: The Architecture of Autonomous Systems* by Jay Thorne.

| | |
|---|---|
| **Who it's for** | Systems, platform and infrastructure engineers taking LLM prototypes into production |
| **What it is** | Small, readable, testable reference kernels — the architectural invariants behind the book |
| **What it is not** | A framework, a wrapper, or turnkey production code |
| **Language / runtime** | Python 3.12+, pydantic v2, OpenTelemetry |
| **Start here** | [Prerequisites](#1-prerequisites) → [Installation](#2-installation) → `pytest` |
| **License** | MIT — copy the patterns into your own architecture |

### Which pattern solves which problem?

| Production problem | Reference pattern | Where |
|---|---|---|
| Probabilistic schema drift, unbounded recursive loops | Deterministic execution harness with oscillation damping, on an explicit state graph | `core/flow/`, `core/loop/` |
| Context windows filling with stale or contradictory content | Context compaction and GraphRAG knowledge-graph traversal | `core/context/`, `core/graph/` |
| Uncontained side effects from tool-calling models | OS-level sandboxing — network namespaces, seccomp, cgroups | `core/sandbox/` |
| Agents taking irreversible actions unattended | Human-in-the-loop escrow and governance gates | `core/hitl/`, `core/governance/` |
| Multi-agent systems that deadlock or duplicate work | MCP host/client plus swarm coordination | `core/protocols/`, `core/multiagent/` |
| No visibility into agent behaviour in production | OpenTelemetry GenAI semantic-convention tracing | `core/` (telemetry) |

---

## 📖 Book Overview & Editorial Showcase

<table>
  <tr>
    <td width="36%" align="center" valign="top">
      <img src="assets/images/book_cover.jpg" alt="Beyond the Prompt Book Cover" width="100%" style="border-radius: 6px; box-shadow: 0 6px 18px rgba(0,0,0,0.18);">
      <br><br>
      <a href="https://digbijoylabs.com" target="_blank">
        <img src="https://img.shields.io/badge/Digbijoy_Labs-Official_Portal-000000?style=for-the-badge&logo=globe&logoColor=white" alt="Digbijoy Labs Portal">
      </a>
      <br><br>
      <sub><strong>Available Editions</strong>:<br>Paperback (7"×10") • Hardcover Case-Laminate • Kindle eBook</sub>
      <br><br>
      <strong>📦 Get Your Copy</strong><br>
      <a href="https://www.amazon.com/dp/B0HJZ1BY9P" target="_blank">
        <img src="https://img.shields.io/badge/Kindle_eBook-Buy_Now-FF9900?style=flat-square&logo=amazon&logoColor=white" alt="Buy Kindle eBook">
      </a><br>
      <a href="https://www.amazon.com/dp/B0HJZ9TGP5" target="_blank">
        <img src="https://img.shields.io/badge/Paperback-Buy_Now-FF9900?style=flat-square&logo=amazon&logoColor=white" alt="Buy Paperback">
      </a><br>
      <a href="https://www.amazon.com/dp/B0HK1CNB5Y" target="_blank">
        <img src="https://img.shields.io/badge/Hardcover-Buy_Now-FF9900?style=flat-square&logo=amazon&logoColor=white" alt="Buy Hardcover">
      </a>
    </td>
    <td width="64%" valign="top">
      <h3>The Definitive Systems Engineering Manual for Autonomous AI Agents</h3>
      <p>
        <strong>Prompt engineering has hit its mathematical ceiling.</strong> When software architects wire unconstrained probabilistic language models directly into production APIs, databases, and financial systems, probabilistic schema drift, unbounded recursive loops, memory rot, and uncontained side-effects compound into catastrophic failures.
      </p>
      <p>
        <strong><em>Beyond the Prompt</em></strong> establishes a rigorous distributed-systems foundation for agentic engineering. Rather than treating foundation models as conversational oracles, this volume treats the large language model as an <strong>untrusted, probabilistic CPU</strong> operating inside a hardened, deterministic runtime system governed by an engineered <strong>AI Harness</strong>.
      </p>
      <ul>
        <li><strong>432 Pages</strong> of rigorous, zero-fluff distributed systems architecture.</li>
        <li><strong>24 In-Depth Chapters</strong> organized into 6 formal architectural parts.</li>
        <li><strong>26 Monochromatic O'Reilly-Style Schematics</strong> illustrating isolation boundaries and topologies.</li>
        <li><strong>178 Production Reference Blueprints</strong> in modern Python 3.12+ and Pydantic v2.</li>
        <li><strong>The 2026 Multipolar AI Landscape</strong>: Fully integrates Anthropic Mythos & Claude 5, OpenAI GPT-6 Astra, DeepMind Gemini 3.8, DeepSeek-V4 Pro/R1, Alibaba Qwen 3.8 Max, Zhipu GLM-5.3, and Mistral Large 3.</li>
      </ul>
      <p>
        🌐 <strong>Publisher Portal & Errata</strong>: <a href="https://digbijoylabs.com" target="_blank">digbijoylabs.com</a>
      </p>
    </td>
  </tr>
</table>

---

## 🌟 Core Architectural Pillars (Amazon A+ Showcase)

<table>
  <tr>
    <td width="33%" align="center" valign="top">
      <img src="assets/images/card_deterministic_loops.png" alt="Deterministic Statecharts & Loops" width="100%">
      <h4>1. Deterministic Loops & Statecharts</h4>
      <p align="left">
        Replace fragile linear ReAct loops with formal 7-stage directed statecharts. Incorporates cryptographically damped sliding windows, oscillation circuit breakers, and bounded evaluator-optimizer reflexion loops.
      </p>
    </td>
    <td width="33%" align="center" valign="top">
      <img src="assets/images/card_graphrag_memory.png" alt="Context Virtual Memory & GraphRAG" width="100%">
      <h4>2. Context as Virtual Memory</h4>
      <p align="left">
        Treat GPU context windows as active RAM hierarchies. Explores RadixAttention prefix caching stabilization, hierarchical compaction cascades, and ontology-driven GraphRAG for multi-hop semantic reasoning.
      </p>
    </td>
    <td width="33%" align="center" valign="top">
      <img src="assets/images/card_enterprise_sandboxing.png" alt="Enterprise Sandboxing & Protocols" width="100%">
      <h4>3. Micro-Sandboxes & Protocol ACIs</h4>
      <p align="left">
        Contain untrusted execution with authentic OS primitives: rootless Linux network namespaces, cgroups v2, process-group isolation, and full compliance with the Model Context Protocol (MCP (JSON-RPC 2.0 / 2025-06-18)) standard.
      </p>
    </td>
  </tr>
</table>

---

## 📐 Interior Schematics & System Topologies

<p align="center">
  <img src="assets/images/a_plus_interior_schematics.png" alt="Interior Architectural Schematics" width="100%">
</p>

Every architectural diagram in the book conforms to the premier monochromatic grayscale standard (exemplified by O'Reilly and Addison-Wesley): high-legibility sans-serif typography, crisp 2px monoline iconography, clean orthogonal connectors, and zero hallucinated tokens.

### The 5-Plane Cognitive Runtime Matrix (Figure 0.1 / Figure 1.1)

<p align="center">
  <img src="assets/images/figure_001_5plane_matrix.png" alt="Figure 0.1: The 5-Plane Engineering Matrix" width="95%">
</p>

<p align="center">
  <img src="assets/images/a_plus_architectural_matrix.png" alt="5-Plane Matrix Architectural Comparison" width="100%">
</p>

| Architectural Plane | Operational Mandate | Key Technologies & Primitives in Companion Code |
| :--- | :--- | :--- |
| **1. Intelligence Plane** | Probabilistic reasoning & candidate action generation | Frontier SLMs/LLMs, TTC search, grammar constraints (`core/intelligence/`) |
| **2. Context Plane** | Virtual memory management & token stream assembly | Prefix KV-cache, compaction cascades, GraphRAG (`core/context/`, `core/graph/`) |
| **3. Execution Plane** | Deterministic actuation & environment interaction | MCP clients/servers, microVM sandboxes, external APIs (`core/protocols/`, `core/sandbox/`) |
| **4. Control Plane** | Invariant enforcement & workflow coordination | Deterministic statecharts, PDP gates, circuit breakers (`core/runtime/`, `core/governance/`) |
| **5. Evidence Plane** | Observability, telemetry & cryptographic auditing | OpenTelemetry GenAI spans, structured logs, audit trails (`core/sre/`, `core/durable/`) |

---

## ⚡ The 7-Stage State Graph Reference Pattern

Rather than naive linear prompt chains, *Beyond the Prompt* formalizes autonomous task execution as a 7-stage directed state graph:

$$\text{Interpret} \longrightarrow \text{Plan} \longrightarrow \text{Act} \longrightarrow \text{Observe} \longrightarrow \text{Verify} \longrightarrow \text{Recover} \longrightarrow \text{Learn}$$

Every stage is governed by strict schema coercion, hardware-timed timeouts, and cryptographic cycle detectors to eliminate infinite loop traps.

---

## 📂 Repository Layout

```
beyond-the-prompt/
├── assets/images/                       # Book cover, A+ content banners, and schematics
├── core/                                # Verified production runtime kernels
│   ├── runtime/harness.py               # Deterministic Execution Harness (Ch 1)
│   ├── intelligence/cognitive_router.py # Budget-Aware Inference Engine (Ch 2)
│   ├── gateway/model_gateway.py         # Multi-Provider Failover Gateway (Ch 3)
│   ├── tools/tool_registry.py           # Grammar-Constrained Tool Coercion (Ch 4)
│   ├── context/prefix_compiler.py       # Static KV Prefix Cache Governor (Ch 5)
│   ├── context/compaction_cascade.py    # Recursive Context Compaction (Ch 6)
│   ├── graph/graph_rag_engine.py        # Knowledge Graph & Multi-Hop Traversal (Ch 7)
│   ├── memory/hybrid_memory_substrate.py# Tiered Working/Episodic/Fact Memory (Ch 8)
│   ├── flow/statechart.py               # Guarded Statechart DAG Engine (Ch 9)
│   ├── reasoning/mcts_planner.py        # Test-Time Compute (TTC) Rollout Search (Ch 10)
│   ├── loop/self_correction.py          # Grounded Evaluator-Optimizer Reflexion (Ch 11)
│   ├── governance/loop_governor.py      # Oscillation Damping & Cycle Arrest (Ch 12)
│   ├── sandbox/process_sandbox.py       # OS Process Group Sandbox (Ch 13)
│   ├── protocols/mcp_server.py          # Model Context Protocol (MCP) Host (Ch 14)
│   ├── aci/workspace_controller.py      # Safe Agent-Computer Interface (Ch 15)
│   ├── durable/temporal_state.py        # Event-Sourced Journal State Store (Ch 16)
│   ├── protocols/a2a_messaging.py       # Agent-to-Agent (A2A) Message Envelope (Ch 17)
│   ├── multiagent/subagent_pool.py      # Ephemeral Subagent Worker Isolation (Ch 18)
│   ├── hitl/authorization_gate.py       # Two-Phase Policy Decision Point (Ch 19)
│   ├── hitl/escrow_gate.py              # Cryptographic Escrow & Anti-Tamper Gate (Ch 19)
│   ├── spec/executable_spec.py          # Spec-Driven Executable Prompt Engine (Ch 20)
│   ├── security/zero_trust_guard.py     # Prompt Injection & Canary Filter (Ch 21)
│   ├── evals/eval_runner.py             # Deterministic Trajectory Benchmarks (Ch 22)
│   ├── sre/telemetry.py                 # OpenTelemetry GenAI Cost/Latency Tracker (Ch 23)
│   └── compound/flywheel.py             # DSPy-style Exemplar Flywheel (Ch 24)
├── chapters/                            # Runnable chapter demonstrations & guides
│   ├── part1_paradigm_shift/            # Chapters 1–4 Walkthroughs
│   ├── part2_context_graph/             # Chapters 5–8 Walkthroughs
│   ├── part3_flow_loops/                # Chapters 9–12 Walkthroughs
│   ├── part4_protocols_runtime/         # Chapters 13–16 Walkthroughs
│   ├── part5_multi_agent_swarms/        # Chapters 17–20 Walkthroughs
│   └── part6_eval_security/             # Chapters 21–24 Walkthroughs
├── tests/                               # Comprehensive automated test suite (14/14 passing)
├── .github/workflows/ci.yml             # GitHub Actions CI for Python 3.12+
├── ERRATA.md                            # Living errata & architecture changelog
├── LICENSE                              # MIT License (Digbijoy Labs)
└── pyproject.toml                       # Python 3.12+ PEP 621 packaging
```

---

## 🚀 Quickstart

### 1. Prerequisites
- Python 3.12 or higher
- Git

### 2. Installation
Clone the repository and install dependencies:

```bash
git clone https://github.com/digbijoy-labs/beyond-the-prompt.git
cd beyond-the-prompt
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 3. Run the Automated Test Suite
Verify that all architectural kernels and invariants execute with zero failures:

```bash
pytest -v tests/
```

### 4. Run Chapter Demonstrations
Execute any chapter reference blueprint directly:

```bash
# Part 1: Deterministic Execution Harness & Oscillation Damping
python -m chapters.part1_paradigm_shift.example_harness

# Part 2: Context Compaction & GraphRAG Knowledge Graph Traversal
python -m chapters.part2_context_graph.example_graphrag

# Part 4: Model Context Protocol (MCP (JSON-RPC 2.0 / 2025-06-18)) Host Server
python -m chapters.part4_protocols_runtime.example_mcp_client
```

---

## 🌐 The 2026 Multipolar AI Landscape

All blueprints and harness architectures in this repository reflect the genuine multipolar frontier of artificial intelligence:

| Category | Premier Foundation Systems | Substrates Supported |
| :--- | :--- | :--- |
| **Frontier Reasoning** | Anthropic Mythos / Claude 5, OpenAI GPT-6 Astra, DeepMind Gemini 3.8 | Public Cloud API & Micro-Sandboxes |
| **Open-Source & Sovereign** | DeepSeek-V4 Pro / R1, Alibaba Qwen 3.8 Max, Zhipu GLM-5.3, Mistral Large 3 | Ascend NPUs, Apple Silicon (MLX), AMD ROCm, NVIDIA CUDA |
| **Protocol Standards** | Model Context Protocol (MCP (JSON-RPC 2.0 / 2025-06-18)), OpenTelemetry GenAI Semantic Conventions | JSON-RPC 2.0 over stdio/SSE, gRPC, REST |

---

## 📖 Book Information & Citation

If you reference this work, utilize the companion code, or cite its architectural frameworks in academic papers or industrial whitepapers:

```bibtex
@book{thorne2026beyondtheprompt,
  author    = {Jay Thorne},
  title     = {Beyond the Prompt: The Architecture of Autonomous Systems},
  subtitle  = {Context Engineering, Graph Engineering, Loop Design, and Production AI Harnesses},
  publisher = {Digbijoy Labs Publications},
  year      = {2026},
  pages     = {446},
  url       = {https://github.com/digbijoy-labs/beyond-the-prompt}
}
```

---

## 🏢 About Digbijoy Labs & the Author

**Digbijoy Labs** is an autonomous research studio and intellectual media lab. Across books and two flagship YouTube channels, it works two frontiers of intelligence — the technical and the human — with forensic depth and visual beauty, unhurried.

### 📺 Watch

| Channel | Focus |
|---------|-------|
| **The Neural Blueprint** | Forensic deep-dives on AI, computation, and deep technology |
| **The Mind Blueprint** | Consciousness, psychology, existential philosophy, self, mind, and life |

### 📚 Read — Digbijoy Labs Publications

**Jay Thorne** *(pen name)* — practitioner-grade books spanning the same ground: AI, computation and the AI-native stack; consciousness, psychology and the examined life.

Current catalogue:

- *Beyond the Prompt* — The Architecture of Autonomous Systems
- *The Legacy Bridge* — *(Coming Soon)*
- *The Connected Machine* — *(Coming Soon)*

---

- **Official Portal**: [https://digbijoylabs.com](https://digbijoylabs.com)
- **Errata Submissions**: Submit discrepancies directly via [GitHub Issues](https://github.com/digbijoy-labs/beyond-the-prompt/issues) or consult [ERRATA.md](ERRATA.md).

> *No hype. No surface-level tutorials. Faceless by design.*

---

## ❓ Frequently Asked Questions

### Is this companion code a framework I can install and depend on?

No. The `core/` modules are **reference architectural kernels** — compact, annotated illustrations of invariants, state transitions and protocol contracts. They are written to be read and copied into your own architecture, not imported as a production dependency. Every kernel is exercised by the test suite so you can see the invariant it enforces.

### What is context engineering, and how is it different from prompt engineering?

Prompt engineering optimises a single instruction. **Context engineering** treats everything the model sees — retrieved documents, tool schemas, conversation history, structured state — as a designed system with a budget, a compaction policy, and a graph of dependencies. In production, the context pipeline rather than the prompt is what determines reliability. See `core/context/` and `core/graph/`.

### Why use an explicit state graph instead of a simple agent loop?

A single `while` loop around a model call has no bound on recursion, no rollback, and no way to distinguish progress from oscillation. An explicit state graph makes every transition inspectable, makes cycles detectable, and makes damping policies (stop, escalate, summarise) a first-class part of the design. See [The 7-Stage State Graph Reference Pattern](#-the-7-stage-state-graph-reference-pattern).

### Which AI models does this code target?

It is deliberately model-agnostic. The reference kernels track the 2026 multipolar landscape — frontier reasoning models from Anthropic, OpenAI and Google DeepMind alongside open-weight and sovereign runtimes (DeepSeek, Qwen, GLM, Mistral) on heterogeneous accelerators (NVIDIA CUDA, Huawei Ascend NPU, Apple MLX, AMD ROCm). See [The 2026 Multipolar AI Landscape](#-the-2026-multipolar-ai-landscape).

### Does it support the Model Context Protocol (MCP)?

Yes. A reference MCP host server over JSON-RPC 2.0 (stdio/SSE) ships under `core/protocols/`, and there is a runnable demonstration in [Run Chapter Demonstrations](#4-run-chapter-demonstrations).

### How do I cite this repository, and how do I report an error?

A `CITATION.cff` is provided for machine-readable citation; the BibTeX block is under [Book Information & Citation](#-book-information--citation). Errata go through [GitHub Issues](https://github.com/digbijoy-labs/beyond-the-prompt/issues) or [ERRATA.md](ERRATA.md).

---

## 📄 License

The code and reference blueprints in this repository are licensed under the [MIT License](LICENSE).  
Copyright (c) 2026 Jay Thorne & Digbijoy Labs Publications.
