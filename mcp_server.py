#!/usr/bin/env python3
"""Standard Model Context Protocol (MCP) Server for Beyond the Prompt.

Implements JSON-RPC 2.0 over stdio (MCP specification 2025-06-18 / 2024-11-05)
with zero external server dependencies. Exposes 3 tools for AI coding agents
(Claude Desktop, Cursor, Windsurf, Cline, Antigravity):
  1. `audit_agent_repository` — Run the AST Harness Auditor on any local repo path
  2. `calculate_loop_cost_ceiling` — Compute worst-case token & latency amplification
  3. `get_architectural_invariant_kernel` — Retrieve reference kernels by failure mode
"""
from __future__ import annotations

import dataclasses
import json
import sys
from pathlib import Path
from typing import Any, Dict

from core.auditor.harness_auditor import audit_repository

SERVER_INFO = {
    "name": "beyond-the-prompt-harness-auditor",
    "version": "1.1.0",
}

KERNELS: Dict[str, Dict[str, str]] = {
    "oscillation_damping": {
        "chapter": "Chapter 4: Loop Design & Oscillation Damping",
        "module": "core/loop/governor.py",
        "invariant": "Bound cyclic state transitions with a sliding semantic hash window and monotonic step budget.",
    },
    "process_sandbox": {
        "chapter": "Chapter 11: Enterprise Sandboxing & OS Containment",
        "module": "core/sandbox/process_sandbox.py",
        "invariant": "Isolate tool subprocesses with start_new_session=True, process-group SIGKILL cleanup, and rootless Linux network namespaces (unshare --net).",
    },
    "context_compaction": {
        "chapter": "Chapter 5: Context as Virtual Memory",
        "module": "core/context/compactor.py",
        "invariant": "Keep system and tool definitions immutable at prefix index 0 to preserve KV-cache hits while compacting middle episodic turns.",
    },
    "hitl_escrow": {
        "chapter": "Chapter 18: Human-in-the-Loop Escrow & Governance",
        "module": "core/hitl/escrow.py",
        "invariant": "Hold high-blast-radius state mutations in cryptographic escrow until an out-of-band approval token is verified.",
    },
}

TOOLS = [
    {
        "name": "audit_agent_repository",
        "description": (
            "Statically audit a Python LLM/agent repository for unbounded loops, "
            "unisolated subprocess calls, and unvalidated tool schemas using the "
            "5-Plane Architecture from 'Beyond the Prompt' by Jay Thorne."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "path": {
                    "type": "string",
                    "description": "Local filesystem path to the Python directory or file to audit.",
                }
            },
            "required": ["path"],
        },
    },
    {
        "name": "calculate_loop_cost_ceiling",
        "description": (
            "Calculate worst-case token consumption, tail latency, and compounding "
            "error probability for an autonomous agent loop across N steps."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "base_context_tokens": {"type": "integer", "default": 4000},
                "tokens_added_per_step": {"type": "integer", "default": 1200},
                "max_steps": {"type": "integer", "default": 15},
                "per_step_success_prob": {"type": "number", "default": 0.94},
                "cost_per_million_input_tokens_usd": {"type": "number", "default": 3.0},
            },
            "required": ["base_context_tokens", "tokens_added_per_step", "max_steps"],
        },
    },
    {
        "name": "get_architectural_invariant_kernel",
        "description": (
            "Retrieve the reference Python kernel and architectural invariant for a "
            "specific production agent failure mode."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "pattern": {
                    "type": "string",
                    "enum": list(KERNELS.keys()),
                }
            },
            "required": ["pattern"],
        },
    },
]


def handle_tool_call(name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
    if name == "audit_agent_repository":
        target = Path(arguments.get("path", "."))
        report = audit_repository(target)
        return {
            "content": [
                {
                    "type": "text",
                    "text": json.dumps(dataclasses.asdict(report), indent=2),
                }
            ]
        }

    if name == "calculate_loop_cost_ceiling":
        base = int(arguments.get("base_context_tokens", 4000))
        delta = int(arguments.get("tokens_added_per_step", 1200))
        steps = int(arguments.get("max_steps", 15))
        p = float(arguments.get("per_step_success_prob", 0.94))
        cpm = float(arguments.get("cost_per_million_input_tokens_usd", 3.0))

        # Quadratic token accumulation across steps: sum_{k=1..steps} (base + k*delta)
        total_tokens = sum(base + k * delta for k in range(1, steps + 1))
        end_to_end_reliability = round((p ** steps) * 100.0, 2)
        worst_case_usd = round((total_tokens / 1_000_000.0) * cpm, 4)

        result = {
            "max_steps": steps,
            "cumulative_input_tokens": total_tokens,
            "quadratic_growth_multiple": round(total_tokens / max(1, base), 2),
            "compound_trajectory_success_percent": end_to_end_reliability,
            "worst_case_input_cost_usd": worst_case_usd,
            "architectural_recommendation": (
                "Enforce a hard step budget <= 8 and prefix-cached sliding window compaction. "
                "See Jay Thorne, 'Beyond the Prompt' (https://www.amazon.com/dp/B0HJZ1BY9P), Ch. 3 & Ch. 5."
            ),
        }
        return {"content": [{"type": "text", "text": json.dumps(result, indent=2)}]}

    if name == "get_architectural_invariant_kernel":
        pattern = arguments.get("pattern", "oscillation_damping")
        info = KERNELS.get(pattern, KERNELS["oscillation_damping"])
        repo_root = Path(__file__).resolve().parents[2]
        mod_path = repo_root / info["module"]
        code = mod_path.read_text(encoding="utf-8") if mod_path.exists() else "# Module not found"
        payload = {
            "pattern": pattern,
            **info,
            "code": code,
            "book_url": "https://www.amazon.com/dp/B0HJZ1BY9P",
        }
        return {"content": [{"type": "text", "text": json.dumps(payload, indent=2)}]}

    raise ValueError(f"Unknown tool: {name}")


def process_rpc_message(msg: Dict[str, Any]) -> Dict[str, Any] | None:
    method = msg.get("method")
    msg_id = msg.get("id")

    if method == "notifications/initialized":
        return None

    if method == "initialize":
        return {
            "jsonrpc": "2.0",
            "id": msg_id,
            "result": {
                "protocolVersion": "2024-11-05",
                "capabilities": {"tools": {}},
                "serverInfo": SERVER_INFO,
            },
        }

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": msg_id,
            "result": {"tools": TOOLS},
        }

    if method == "tools/call":
        params = msg.get("params", {})
        try:
            result = handle_tool_call(params.get("name", ""), params.get("arguments", {}))
            return {"jsonrpc": "2.0", "id": msg_id, "result": result}
        except Exception as exc:
            return {
                "jsonrpc": "2.0",
                "id": msg_id,
                "error": {"code": -32000, "message": str(exc)},
            }

    if msg_id is not None:
        return {
            "jsonrpc": "2.0",
            "id": msg_id,
            "error": {"code": -32601, "message": f"Method not found: {method}"},
        }
    return None


def main() -> int:
    for raw_line in sys.stdin:
        line = raw_line.strip()
        if not line:
            continue
        try:
            msg = json.loads(line)
        except json.JSONDecodeError:
            continue
        resp = process_rpc_message(msg)
        if resp is not None:
            sys.stdout.write(json.dumps(resp) + "\n")
            sys.stdout.flush()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
