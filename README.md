# Offering Innovation

A structured prototyping tool that transforms a problem statement into a market offering design.

Uses first principles decomposition, systems thinking, ODI Jobs Theory, and bottom-up offering construction to move from "here's a problem" to "here's what to build and for whom."

---

## Quick Start

1. **Clone this repo** and open the folder in Claude Code
2. **Start a new run:** Copy `runs/_template/` to `runs/run_001_[your-topic]/`
3. **Begin:** Tell Claude your problem: `"Run Phase 1 on this problem: [your problem statement]"`

---

## How It Works

The tool follows a five-phase pipeline. Each phase ends with a decision gate before you proceed.

| Phase | What It Does | Key Output |
|-------|-------------|-----------|
| **1. Problem Decomposition** | Strip the problem to irreducible root causes using first principles and 5 Whys | Atomic problem statement + execution barriers + unmet metrics |
| **2. System Mapping** | Identify all stakeholders, classify job executors, map cross-dependencies | Stakeholder map + ranked executors for Phase 3 |
| **3. Job Mapping** | Build an ODI-compliant job map per executor — core job, 8-step map, outcome statements | Job map + validated outcome statements with importance signals |
| **4. Offering Design** | Diverge (unconstrained ideation) then Converge (competitive selection) | Offering definition + capabilities + falsifiable proof points |
| **5. Analysis & Executive Summary** | Synthesize the full pipeline into a decision-ready document | Executive summary with chain of logic, validation plan, net assessment |

---

## What You Need to Bring

- A problem statement (rough is fine — the process refines it)
- Willingness to find external sources (the framework requires citation at each gate)
- ~4-8 hours across the full pipeline for a first-time run

---

## What the Tool Produces

By the end of a full run, you'll have:

| Artifact | File | Description |
|----------|------|-------------|
| Atomic problem statement | `phase-1-output.md` | Root-cause-grounded, evidence-backed, solution-agnostic |
| Stakeholder system map | `phase-2-output.md` | All actors classified, cross-dependencies mapped |
| ODI job map(s) | `phase-3-output.md` | Core job + 8-step map + validated outcome statements |
| Offering design | `phase-4-output.md` | Capabilities, value proposition, competitive positioning, proof points |
| Executive summary | `executive-summary.md` | Chain of logic + deep offering description + validation plan + net assessment |

---

## File Structure

```
offering-innovation-plugin/
├── README.md                  # This file
├── CLAUDE.md                  # AI context and instructions
├── framework/                 # Methodology documentation
│   ├── data-model.md          # Three-tier x four-domain data structure
│   ├── phase-1-problem.md     # Phase 1 detailed process
│   ├── phase-2-system-mapping.md
│   ├── phase-3-job-map.md
│   ├── phase-4-offering.md
│   └── phase-5-analysis.md
├── runs/                      # Your prototype runs (one folder per problem)
│   └── _template/             # Blank run template — copy this to start
├── tests/                     # Deterministic validation suite
│   └── validate.py
└── .claude/                   # Claude Code configuration
    ├── commands/              # Slash commands (/init, /status, /decision)
    ├── rules/                 # Auto-loaded guidelines
    ├── skills/                # Specialized capabilities
    └── templates/             # Document templates
```

---

## Methodology

The framework combines four approaches:

| Approach | Where Used | Why |
|----------|-----------|-----|
| **First Principles Decomposition** | Phase 1 | Separates structural truths from inherited assumptions |
| **5 Whys** | Phase 1 | Reaches terminal root causes with citation requirements |
| **ODI (Outcome-Driven Innovation)** | Phases 3-4 | Most rigorous Jobs Theory methodology; maps directly to measurable outcomes |
| **Design Thinking (Diverge/Converge)** | Phase 4 | Unconstrained ideation first; competitive analysis informs selection |

### The Data Model

All outputs map to a **3-tier x 4-domain grid:**

|  | JTBD Domain | Problem Domain | Offering Domain | Process Domain |
|--|-------------|---------------|-----------------|----------------|
| **Tier 1 (Job/Problem/Offering/Process)** | Core Job | Problem Statement | Offering Name | Work Process |
| **Tier 2 (Step)** | Job Map Steps | Execution Barriers | Capabilities | Process Steps |
| **Tier 3 (Outcome)** | Outcome Statements | Unmet Metrics | Performance Requirements | Proof Points |

---

## Analytical Sub-Agents

Five analytical perspectives are invoked at key moments:

| Sub-Agent | Purpose | Triggered |
|-----------|---------|-----------|
| **Assumption Challenger** | Pressure-tests claims for hidden assumptions | Phases 1, 2, 4 |
| **ODI Compliance Checker** | Validates JTBD artifacts against strict ODI rules | Phase 3 |
| **Outcome Research Validator** | Finds 3+ third-party sources per outcome | Phase 3 |
| **Cross-Reference Mapper** | Maintains linkages across four domains | Phases 3-4 |
| **Systems Dynamics Checker** | Identifies feedback loops and second-order effects | Phases 2, 4 |

---

## Validation Suite

Run deterministic checks after each phase:

```bash
python tests/validate.py runs/your-run/ --phase 1
python tests/validate.py runs/your-run/ --phase 2
# etc.
```

Results:
- **PASS** — check met
- **WARN** — potential issue, review before proceeding
- **FAIL** — gate criterion not met, fix required
- **SKIP** — check not applicable (phase not started)

---

## Tips

- **Don't skip Phase 2.** The stakeholder system map is what prevents you from mapping the wrong executor's job in Phase 3.
- **Citations are not optional.** The 3-source requirement at each gate exists because analytically constructed problems/jobs produce phantom offerings. Evidence grounds the work.
- **The "So What?" test is the hardest part.** If you can't name a competitor and explain what you do that they don't, the offering isn't differentiated yet.
- **Proxy scoring is honest.** The framework flags when quantitative ODI opportunity scoring isn't available. Proxy scores serve the prioritization function but should be replaced with survey data if the offering moves forward.
- **Phase 5 is synthesis, not summary.** Don't retell each phase — make the logical chain from problem to offering explicit and evidence-backed.
