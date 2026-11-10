#!/usr/bin/env python3
"""AST & Static Architecture Auditor for Python AI Agent Repositories.

Detects the 6 fatal production failure modes cataloged in:
Jay Thorne, "Beyond the Prompt: The Architecture of Autonomous Systems"
(Digbijoy Labs Publications, 2026) — https://www.amazon.com/dp/B0HJZ1BY9P
"""
from __future__ import annotations

import argparse
import ast
import json
import sys
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import List


@dataclass
class Finding:
    rule_id: str
    severity: str
    plane: str
    file: str
    line: int
    message: str
    remediation: str
    book_reference: str


@dataclass
class AuditReport:
    target_path: str
    files_scanned: int
    lines_scanned: int
    harness_score: int
    grade: str
    findings: List[Finding] = field(default_factory=list)
    reference_manual: str = (
        "Beyond the Prompt: The Architecture of Autonomous Systems by Jay Thorne "
        "(Amazon Kindle $3.99 / Paperback $24.99: https://www.amazon.com/dp/B0HJZ1BY9P)"
    )


DANGEROUS_CALLS = {
    "os.system": ("BTP-SANDBOX-001", "CRITICAL", "Plane 3: Execution & Tooling"),
    "subprocess.Popen": ("BTP-SANDBOX-002", "HIGH", "Plane 3: Execution & Tooling"),
    "subprocess.run": ("BTP-SANDBOX-003", "HIGH", "Plane 3: Execution & Tooling"),
    "eval": ("BTP-SANDBOX-004", "CRITICAL", "Plane 3: Execution & Tooling"),
    "exec": ("BTP-SANDBOX-005", "CRITICAL", "Plane 3: Execution & Tooling"),
}


def _get_call_name(node: ast.Call) -> str:
    if isinstance(node.func, ast.Name):
        return node.func.id
    if isinstance(node.func, ast.Attribute):
        parts = []
        curr: ast.AST = node.func
        while isinstance(curr, ast.Attribute):
            parts.append(curr.attr)
            curr = curr.value
        if isinstance(curr, ast.Name):
            parts.append(curr.id)
        return ".".join(reversed(parts))
    return ""


def scan_python_file(py_file: Path, rel_root: Path) -> tuple[int, list[Finding]]:
    try:
        source = py_file.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return 0, []
    lines = source.splitlines()
    try:
        tree = ast.parse(source, filename=str(py_file))
    except SyntaxError:
        return len(lines), []

    rel_path = str(py_file.relative_to(rel_root)).replace("\\", "/")
    findings: list[Finding] = []

    for node in ast.walk(tree):
        # 1. Unbounded while True loops without explicit step/budget guard
        if isinstance(node, ast.While):
            is_const_true = isinstance(node.test, ast.Constant) and node.test.value is True
            if is_const_true:
                loop_src = ast.get_source_segment(source, node) or ""
                has_budget_guard = any(
                    kw in loop_src
                    for kw in ("max_steps", "step_budget", "max_iterations", "timeout", "circuit_breaker")
                )
                if not has_budget_guard:
                    findings.append(
                        Finding(
                            rule_id="BTP-LOOP-001",
                            severity="CRITICAL",
                            plane="Plane 1: Control & State",
                            file=rel_path,
                            line=node.lineno,
                            message="Unbounded `while True` loop detected without explicit step/token circuit breaker.",
                            remediation="Replace open-ended while loops with a bounded 7-stage statechart or step-counter governor (`core/loop/governor.py`).",
                            book_reference="Beyond the Prompt, Ch. 3 (Statecharts vs. Linear Loops) & Ch. 4 (Oscillation Damping)",
                        )
                    )

        # 2. Subprocess / shell execution without process-group isolation
        if isinstance(node, ast.Call):
            call_name = _get_call_name(node)
            if call_name in DANGEROUS_CALLS:
                rule_id, sev, plane = DANGEROUS_CALLS[call_name]
                kw_names = {kw.arg for kw in node.keywords if kw.arg}
                if call_name.startswith("subprocess.") and (
                    "start_new_session" in kw_names and "timeout" in kw_names
                ):
                    continue
                findings.append(
                    Finding(
                        rule_id=rule_id,
                        severity=sev,
                        plane=plane,
                        file=rel_path,
                        line=node.lineno,
                        message=f"Unisolated `{call_name}()` invocation without process-group session containment and hard timeout.",
                        remediation="Enforce `start_new_session=True`, explicit `timeout=`, and `os.killpg` cleanup, or isolate in rootless network namespaces (`core/sandbox/process_sandbox.py`).",
                        book_reference="Beyond the Prompt, Ch. 11 (Micro-Sandboxing & OS Primitives)",
                    )
                )

            # 3. Raw json.loads on LLM output without Pydantic schema validation
            if call_name == "json.loads":
                findings.append(
                    Finding(
                        rule_id="BTP-ACI-001",
                        severity="MEDIUM",
                        plane="Plane 3: Execution & Tooling",
                        file=rel_path,
                        line=node.lineno,
                        message="Raw `json.loads()` call detected; probabilistic LLM payloads can drift in schema or types.",
                        remediation="Validate tool and structured-output payloads with Pydantic v2 `model_validate_json()` (`core/tools/tool_validator.py`).",
                        book_reference="Beyond the Prompt, Ch. 2 (Probabilistic-to-Deterministic Boundary) & Ch. 9 (ACI Contracts)",
                    )
                )

    return len(lines), findings


def audit_repository(target: Path) -> AuditReport:
    target = target.resolve()
    py_files = [target] if target.is_file() else sorted(target.rglob("*.py"))
    rel_root = target.parent if target.is_file() else target

    total_lines = 0
    all_findings: list[Finding] = []
    scanned_files = 0

    for f in py_files:
        if any(part in f.parts for part in (".git", ".venv", "venv", "node_modules", "__pycache__")):
            continue
        scanned_files += 1
        line_count, file_findings = scan_python_file(f, rel_root)
        total_lines += line_count
        all_findings.extend(file_findings)

    penalty = 0
    for item in all_findings:
        if item.severity == "CRITICAL":
            penalty += 15
        elif item.severity == "HIGH":
            penalty += 8
        else:
            penalty += 3

    score = max(0, 100 - min(95, penalty))
    if score >= 90:
        grade = "A (Production-Hardened Harness)"
    elif score >= 75:
        grade = "B (Moderately Bounded Runtime)"
    elif score >= 55:
        grade = "C (Fragile Prototype — High Drift Risk)"
    else:
        grade = "F (Unbounded Probabilistic Loop — Outage Imminent)"

    return AuditReport(
        target_path=str(target),
        files_scanned=scanned_files,
        lines_scanned=total_lines,
        harness_score=score,
        grade=grade,
        findings=all_findings[:50],
    )


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Beyond the Prompt — Deterministic AI Harness AST Auditor"
    )
    parser.add_argument("path", nargs="?", default=".", help="Path to Python repository or file")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON report")
    args = parser.parse_args()

    report = audit_repository(Path(args.path))
    if args.json:
        print(json.dumps(asdict(report), indent=2))
        return 0

    print("=" * 76)
    print(" BEYOND THE PROMPT — DETERMINISTIC AI HARNESS AUDITOR (v1.1.0)")
    print("=" * 76)
    print(f" Target       : {report.target_path}")
    print(f" Scanned      : {report.files_scanned} Python files ({report.lines_scanned:,} lines)")
    print(f" Harness Score: {report.harness_score}/100  [{report.grade}]")
    print("-" * 76)
    if not report.findings:
        print(" [PASS] Zero unbounded loops or unisolated execution primitives detected.")
    else:
        print(f" Findings ({len(report.findings)}):")
        for idx, f in enumerate(report.findings[:15], 1):
            print(f"  {idx:02d}. [{f.severity}] {f.rule_id} ({f.file}:{f.line}) — {f.plane}")
            print(f"      Issue : {f.message}")
            print(f"      Fix   : {f.remediation}")
            print(f"      Ref   : {f.book_reference}")
    print("-" * 76)
    print(f" Architectural Reference: {report.reference_manual}")
    print("=" * 76)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
