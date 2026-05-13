#!/usr/bin/env python3
"""
Offering Innovation — Validation Suite

Runs deterministic checks against phase outputs in a run folder.

Usage:
    python tests/validate.py runs/your-run-folder/ --phase N
    python tests/validate.py runs/your-run-folder/ --all

Results:
    PASS  — check met
    WARN  — potential issue, review before proceeding
    FAIL  — gate criterion not met, fix required
    SKIP  — check not applicable (phase not started or file empty)
"""

import argparse
import os
import re
import sys
from pathlib import Path


# ─── Result helpers ───────────────────────────────────────────────────────────

def result(status, check, detail=""):
    color = {"PASS": "\033[92m", "WARN": "\033[93m", "FAIL": "\033[91m", "SKIP": "\033[90m"}
    reset = "\033[0m"
    prefix = color.get(status, "") + f"[{status}]" + reset
    msg = f"  {prefix} {check}"
    if detail:
        msg += f"\n         {detail}"
    print(msg)
    return status


def load_file(run_dir, filename):
    path = Path(run_dir) / filename
    if not path.exists():
        return None
    content = path.read_text()
    # Treat files that only contain template placeholders as not started
    if content.strip() == "" or "{{RUN_NAME}}" in content and "{{PROBLEM_STATEMENT}}" in content:
        return None
    return content


# ─── Phase checks ─────────────────────────────────────────────────────────────

def check_phase_1(run_dir):
    print("\nPhase 1: Problem Decomposition")
    content = load_file(run_dir, "phase-1-output.md")
    if content is None:
        result("SKIP", "Phase 1 output not found or not started")
        return

    results = []

    # Check for root cause section
    has_root_cause = "Root Cause" in content or "5 Whys" in content
    results.append(result(
        "PASS" if has_root_cause else "FAIL",
        "5 Whys section present",
        "" if has_root_cause else "Missing '5 Whys' or 'Root Cause' section"
    ))

    # Check for problem statement
    has_problem_statement = "Problem Statement" in content
    results.append(result(
        "PASS" if has_problem_statement else "FAIL",
        "Problem statement section present"
    ))

    # Check for citations (look for URLs or source references)
    citation_count = len(re.findall(r'https?://', content))
    results.append(result(
        "PASS" if citation_count >= 3 else ("WARN" if citation_count > 0 else "FAIL"),
        f"Citations present ({citation_count} URLs found)",
        "Need at least 3 cited sources for problem statement validation" if citation_count < 3 else ""
    ))

    # Check for assumptions section
    has_assumptions = "Assumption" in content
    results.append(result(
        "PASS" if has_assumptions else "WARN",
        "Assumptions section present",
        "Step 6 (Surface Assumptions) may be missing" if not has_assumptions else ""
    ))

    # Check for execution barriers
    has_barriers = "Barrier" in content or "Execution Barrier" in content
    results.append(result(
        "PASS" if has_barriers else "WARN",
        "Execution barriers documented"
    ))

    # Check for unmet metrics
    has_metrics = "Unmet Metric" in content or "Metric" in content
    results.append(result(
        "PASS" if has_metrics else "WARN",
        "Unmet metrics documented"
    ))

    # Check quality checklist completion
    checked_items = content.count("- [x]") + content.count("- [X]")
    total_items = content.count("- [ ]") + checked_items
    if total_items > 0:
        results.append(result(
            "PASS" if checked_items == total_items else "WARN",
            f"Quality checklist: {checked_items}/{total_items} items checked"
        ))

    fails = results.count("FAIL")
    warns = results.count("WARN")
    print(f"\n  Phase 1 summary: {results.count('PASS')} PASS, {warns} WARN, {fails} FAIL")
    return fails == 0


def check_phase_2(run_dir):
    print("\nPhase 2: System Mapping")
    content = load_file(run_dir, "phase-2-output.md")
    if content is None:
        result("SKIP", "Phase 2 output not found or not started")
        return

    results = []

    # Stakeholder list
    has_stakeholders = "Stakeholder" in content
    results.append(result(
        "PASS" if has_stakeholders else "FAIL",
        "Stakeholder list present"
    ))

    # Classifications
    has_classifications = "Executor" in content and "Classification" in content
    results.append(result(
        "PASS" if has_classifications else "FAIL",
        "Stakeholder classifications present"
    ))

    # Functional executor definitions
    has_functional = "Functional" in content or "The person who" in content
    results.append(result(
        "PASS" if has_functional else "WARN",
        "Executors defined functionally (not just by title)"
    ))

    # Citations
    citation_count = len(re.findall(r'https?://', content))
    results.append(result(
        "PASS" if citation_count >= 2 else ("WARN" if citation_count > 0 else "FAIL"),
        f"Citations present ({citation_count} URLs found)",
        "Need 2-3 sources for stakeholder completeness validation" if citation_count < 2 else ""
    ))

    # Cross-dependencies
    has_deps = "Dependency" in content or "Cross-Executor" in content or "Handoff" in content
    results.append(result(
        "PASS" if has_deps else "WARN",
        "Cross-executor dependencies documented"
    ))

    fails = results.count("FAIL")
    warns = results.count("WARN")
    print(f"\n  Phase 2 summary: {results.count('PASS')} PASS, {warns} WARN, {fails} FAIL")
    return fails == 0


def check_phase_3(run_dir):
    print("\nPhase 3: Job Mapping (ODI)")
    content = load_file(run_dir, "phase-3-output.md")
    if content is None:
        result("SKIP", "Phase 3 output not found or not started")
        return

    results = []

    # Core job statement
    has_core_job = "Core Job" in content
    results.append(result(
        "PASS" if has_core_job else "FAIL",
        "Core job statement present"
    ))

    # All 8 job map steps
    required_steps = ["Define", "Locate", "Prepare", "Confirm", "Execute", "Monitor", "Modify", "Conclude"]
    missing_steps = [s for s in required_steps if s not in content]
    results.append(result(
        "PASS" if not missing_steps else "FAIL",
        f"All 8 job map steps present",
        f"Missing: {', '.join(missing_steps)}" if missing_steps else ""
    ))

    # ODI outcome format check (minimize/maximize)
    outcome_lines = [l for l in content.split('\n') if 'Minimize' in l or 'Maximize' in l]
    results.append(result(
        "PASS" if len(outcome_lines) >= 5 else ("WARN" if len(outcome_lines) > 0 else "FAIL"),
        f"ODI outcome statements present ({len(outcome_lines)} found)",
        "Outcomes should use 'Minimize' or 'Maximize' format" if len(outcome_lines) < 5 else ""
    ))

    # Check for solution-specific language in outcomes (common violations)
    solution_words = ["software", "platform", "tool", "app", "system", "dashboard", "API", "database"]
    violations = []
    for line in outcome_lines:
        for word in solution_words:
            if word.lower() in line.lower():
                violations.append(f"'{word}' in: {line.strip()[:80]}")
    results.append(result(
        "PASS" if not violations else "WARN",
        "Outcome statements are solution-agnostic",
        f"Possible violations: {violations[0]}" if violations else ""
    ))

    # Relevance tags
    has_relevance = "Relevant" in content or "Adjacent" in content
    results.append(result(
        "PASS" if has_relevance else "WARN",
        "Outcome relevance tags present (Relevant/Adjacent/Out of scope)"
    ))

    # Citations for relevant outcomes
    citation_count = len(re.findall(r'https?://', content))
    results.append(result(
        "PASS" if citation_count >= 6 else ("WARN" if citation_count >= 3 else "FAIL"),
        f"Citations present ({citation_count} URLs found)",
        "Relevant outcomes need 3 sources each (core job + job map + outcomes)" if citation_count < 6 else ""
    ))

    # Importance signals
    has_signals = "Critical" in content or "Common" in content or "Minor" in content
    results.append(result(
        "PASS" if has_signals else "WARN",
        "Importance signals captured (Critical/Common/Minor)"
    ))

    fails = results.count("FAIL")
    warns = results.count("WARN")
    print(f"\n  Phase 3 summary: {results.count('PASS')} PASS, {warns} WARN, {fails} FAIL")
    return fails == 0


def check_phase_4(run_dir):
    print("\nPhase 4: Offering Design")
    content = load_file(run_dir, "phase-4-output.md")
    if content is None:
        result("SKIP", "Phase 4 output not found or not started")
        return

    results = []

    # Performance requirements
    has_prs = "Performance Requirement" in content or "PR1" in content or "PR#" in content
    results.append(result(
        "PASS" if has_prs else "FAIL",
        "Performance requirements present"
    ))

    # Feasibility flags
    has_feasibility = "Achievable" in content or "Stretch" in content or "Uncertain" in content
    results.append(result(
        "PASS" if has_feasibility else "WARN",
        "Feasibility flags on performance requirements"
    ))

    # Diverge stage
    has_diverge = "Conservative" in content and "Expected" in content and "Novel" in content
    results.append(result(
        "PASS" if has_diverge else "FAIL",
        "Diverge stage: Conservative/Expected/Novel ideas generated"
    ))

    # Competitive landscape
    has_competitive = "Competitor" in content or "Competitive" in content
    results.append(result(
        "PASS" if has_competitive else "FAIL",
        "Competitive landscape present"
    ))

    # Minimum competitive coverage
    competitor_count = len(re.findall(r'\|\s*\d+\s*\|', content))
    results.append(result(
        "PASS" if competitor_count >= 4 else "WARN",
        f"Competitive coverage ({competitor_count} rows found in competitor table)",
        "Minimum: 2 product competitors + 2 service competitors + 1 workaround + 1 do-nothing" if competitor_count < 4 else ""
    ))

    # Post-selection stress test
    has_stress = "Stress Test" in content or "Counter-Argument" in content
    results.append(result(
        "PASS" if has_stress else "FAIL",
        "Post-selection stress test completed"
    ))

    # Capabilities
    has_capabilities = "Capability" in content or "Capabilities" in content
    results.append(result(
        "PASS" if has_capabilities else "FAIL",
        "Capabilities section present"
    ))

    # Proof points / falsifiable experiments
    has_proof = "Experiment" in content or "Proof Point" in content or "Pass criteria" in content
    results.append(result(
        "PASS" if has_proof else "FAIL",
        "Falsifiable proof point experiments present"
    ))

    # "So What?" test
    has_so_what = "So What" in content or "switch" in content.lower()
    results.append(result(
        "PASS" if has_so_what else "FAIL",
        '"So What?" test answered'
    ))

    # Data model completeness (12 cells)
    has_data_model = "Data Model" in content and "JTBD" in content
    results.append(result(
        "PASS" if has_data_model else "WARN",
        "Data model completeness grid present"
    ))

    fails = results.count("FAIL")
    warns = results.count("WARN")
    print(f"\n  Phase 4 summary: {results.count('PASS')} PASS, {warns} WARN, {fails} FAIL")
    return fails == 0


def check_phase_5(run_dir):
    print("\nPhase 5: Analysis & Executive Summary")
    content = load_file(run_dir, "executive-summary.md")
    if content is None:
        result("SKIP", "Executive summary not found or not started")
        return

    results = []

    # Chain of logic
    has_chain = "Chain of Logic" in content
    results.append(result(
        "PASS" if has_chain else "FAIL",
        "Chain of Logic section present"
    ))

    # Deep offering description
    has_offering = "Deep Offering" in content or ("What It Is" in content and "Who It's For" in content)
    results.append(result(
        "PASS" if has_offering else "FAIL",
        "Deep offering description present"
    ))

    # Competitors named
    citation_count = len(re.findall(r'https?://', content))
    results.append(result(
        "PASS" if citation_count >= 3 else "WARN",
        f"Evidence cited ({citation_count} URLs found)"
    ))

    # Validation plan
    has_validation = "Validation" in content and ("Experiment" in content or "Pass Criteria" in content)
    results.append(result(
        "PASS" if has_validation else "FAIL",
        "Validation plan with experiments present"
    ))

    # Next steps
    has_next_steps = "Next Steps" in content or "Recommended" in content
    results.append(result(
        "PASS" if has_next_steps else "FAIL",
        "Recommended next steps present"
    ))

    # Limitations
    has_limitations = "Limitation" in content or "Limitations" in content
    results.append(result(
        "PASS" if has_limitations else "FAIL",
        "Honest limitations documented"
    ))

    # Net assessment
    has_net = "Net Assessment" in content
    results.append(result(
        "PASS" if has_net else "FAIL",
        "Net assessment present"
    ))

    # Still contains placeholder text
    has_placeholders = "{{RUN_NAME}}" in content or "*(3-5 paragraphs" in content
    results.append(result(
        "FAIL" if has_placeholders else "PASS",
        "Placeholder text replaced with real content",
        "Template placeholders found — document may not be filled out" if has_placeholders else ""
    ))

    fails = results.count("FAIL")
    warns = results.count("WARN")
    print(f"\n  Phase 5 summary: {results.count('PASS')} PASS, {warns} WARN, {fails} FAIL")
    return fails == 0


# ─── Main ─────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Validate phase outputs for an Offering Innovation run"
    )
    parser.add_argument("run_dir", help="Path to the run folder (e.g., runs/run_001_my-problem/)")
    parser.add_argument("--phase", type=int, choices=[1, 2, 3, 4, 5],
                        help="Check a specific phase only")
    parser.add_argument("--all", action="store_true", help="Check all phases")

    args = parser.parse_args()

    run_dir = Path(args.run_dir)
    if not run_dir.exists():
        print(f"Error: Run folder not found: {run_dir}")
        sys.exit(1)

    print(f"\nOffering Innovation — Validation Suite")
    print(f"Run folder: {run_dir}")
    print("=" * 60)

    phase_checks = {
        1: check_phase_1,
        2: check_phase_2,
        3: check_phase_3,
        4: check_phase_4,
        5: check_phase_5,
    }

    if args.phase:
        phases_to_check = [args.phase]
    else:
        phases_to_check = [1, 2, 3, 4, 5]

    all_passed = True
    for phase_num in phases_to_check:
        passed = phase_checks[phase_num](run_dir)
        if passed is False:
            all_passed = False

    print("\n" + "=" * 60)
    if all_passed:
        print("\033[92mAll checks passed.\033[0m")
    else:
        print("\033[91mSome checks failed. Fix FAIL results before proceeding.\033[0m")

    sys.exit(0 if all_passed else 1)


if __name__ == "__main__":
    main()
