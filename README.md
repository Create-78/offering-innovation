# Offering Innovation

A Claude Code plugin that transforms a problem statement into a market offering design — grounded in jobs theory, first principles decomposition, and competitive positioning.

```
Run Phase 1 on this problem: [your problem statement]
```

---

## The Problem It Solves

Most offering development starts too late. Teams jump from "here's a problem" to "here's a solution" without understanding who actually has the problem, what they're fundamentally trying to accomplish, or why existing solutions fall short. The result is an offering that solves a symptom, targets the wrong buyer, or lands in a competitive space with no differentiation.

This plugin forces the work that gets skipped: atomic root cause analysis, stakeholder system mapping, ODI-validated job mapping, and a diverge-then-converge offering design with explicit competitive positioning. Every claim requires evidence. Every capability traces to an unmet outcome.

---

## How It Works

Five phases run in sequence. Each phase ends with a gate before you proceed.

| Phase | What It Does | Key Output |
|-------|-------------|-----------|
| **1. Problem Decomposition** | Strip the problem to irreducible root causes via first principles and 5 Whys | Atomic problem statement + execution barriers + unmet metrics |
| **2. System Mapping** | Identify all stakeholders, classify job executors, map cross-dependencies | Stakeholder map + ranked executors |
| **3. Job Mapping** | Build an ODI-compliant job map per executor | Core job + 8-step map + validated outcome statements |
| **4. Offering Design** | Diverge (unconstrained ideation) then converge (competitive analysis) | Offering definition + capabilities + proof points |
| **5. Analysis & Executive Summary** | Synthesize the full pipeline into a decision-ready document | Chain-of-logic executive summary + validation plan |

---

## Installation

**Requirements:** [Claude Code](https://claude.ai/code), Node.js

```bash
npx offering-innovation-plugin
```

Run outputs save to `runs/` in the current folder. Open that folder in Claude Code and tell Claude your problem.

**Global install** (commands and skills available in all projects):
```bash
npx offering-innovation-plugin --global
```

### OpenCode

```bash
cp -r dist/opencode/. your-project/
```

### GitHub Copilot

```bash
cp -r dist/github/.github your-project/
```

### Gemini CLI

```bash
cp -r dist/gemini/.gemini your-project/
```

### Codex CLI

```bash
cp -r dist/codex/.agents your-project/
mkdir -p your-project/.codex
cp -r dist/codex/.codex/agents your-project/.codex/
```

### Trae

```bash
cp -r dist/trae/.trae/skills/* ~/.trae/skills/
```

### Rovo Dev

```bash
# Project-specific
cp -r dist/rovo-dev/.rovodev your-project/

# Or global
cp -r dist/rovo-dev/.rovodev/skills/* ~/.rovodev/skills/
```

### Qoder

```bash
# Project-specific
cp -r dist/qoder/.qoder your-project/

# Or global
cp -r dist/qoder/.qoder/skills/* ~/.qoder/skills/
```

### Pi

```bash
cp -r dist/pi/.pi your-project/
```

---

## Usage

Copy `runs/_template/` to start a new run:

```bash
cp -r runs/_template/ runs/run_001_your-topic/
```

Then tell Claude your problem:

```
Run Phase 1 on this problem: [your problem statement]
```

Or with an existing run folder open, use `/init` to be guided through setup.

---

## What One Run Produces

| Artifact | What It Contains |
|----------|-----------------|
| `phase-1-output.md` | Root-cause-grounded problem statement, evidence-backed, solution-agnostic |
| `phase-2-output.md` | All actors classified, cross-dependencies mapped, executors ranked |
| `phase-3-output.md` | Core job, 8-step job map, validated outcome statements with importance signals |
| `phase-4-output.md` | Offering definition, capabilities, competitive positioning, falsifiable proof points |
| `executive-summary.md` | Chain of logic, deep offering description, validation plan, net assessment |

---

## Methodology

| Approach | Where Used | Why |
|----------|-----------|-----|
| **First Principles Decomposition** | Phase 1 | Separates structural truths from inherited assumptions |
| **5 Whys** | Phase 1 | Reaches terminal root causes; citation required at each Why |
| **ODI (Outcome-Driven Innovation)** | Phases 3–4 | Maps directly to measurable executor outcomes; prevents solution-shaped job descriptions |
| **Design Thinking (Diverge/Converge)** | Phase 4 | Unconstrained ideation first; competitive analysis informs selection |

**The data model:** All outputs map to a 3-tier × 4-domain grid (Job/Problem/Offering/Process at the tier level; JTBD/Problem/Offering/Process at the domain level). This structure ensures every capability traces to an unmet outcome and every outcome traces to a root-cause problem.

**Five analytical sub-agents** activate at key moments: Assumption Challenger, ODI Compliance Checker, Outcome Research Validator, Cross-Reference Mapper, and Systems Dynamics Checker. These run automatically — you don't invoke them manually.

---

## Validation

Run deterministic checks after each phase:

```bash
python tests/validate.py runs/your-run/ --phase 1
python tests/validate.py runs/your-run/ --phase 3
python tests/validate.py runs/your-run/
```

Results: `PASS` / `WARN` / `FAIL` / `SKIP` per check. Checks include citation counts, ODI outcome format compliance, solution-agnostic language detection, required sections, and placeholder detection.

---

## Guardrails

- **Citations are not optional.** The 3-source requirement at each gate exists because analytically constructed problems and jobs produce phantom offerings. Evidence grounds the work.
- **One offering by default.** Splitting into multiple offerings requires affirmative evidence: different buyers, different value props, or independent adoption paths. The burden of proof is on the split.
- **Gate failures block, not warn.** A failed gate criterion must be corrected before proceeding — it can't be noted and bypassed.
- **The "So What?" test.** If you can't name a competitor and explain specifically what you do that they don't, the offering isn't differentiated yet.

---

## License

MIT
