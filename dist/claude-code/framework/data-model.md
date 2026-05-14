# Three-Tier Data Model

The backbone of the Job-Problem-Offering framework. Each tier maps across four domains.

---

## The Grid

| Tier | JTBD Domain | Problem Domain | Offering Domain | Process Domain |
|------|-------------|----------------|-----------------|----------------|
| **Tier 1 — Job** | Core Job | Problem Statement | Offering | Work Process |
| **Tier 2 — Step** | Job Step | Execution Barrier | Capability | Process Step |
| **Tier 3 — Outcome** | Outcome Statement | Unmet Metric | Performance Requirement | Proof Point |

---

## Tier Definitions

### Tier 1 — Job Level (Strategic)

The highest level of abstraction. Defines *what* and *for whom*.

| Domain | Definition | Format |
|--------|-----------|--------|
| **Core Job** | The functional job the executor is trying to accomplish | `[Action verb] + [object] + [context]` |
| **Problem Statement** | The situation creating friction or failure in accomplishing the job | `[Who] struggles to [do what] because [root cause]` |
| **Offering** | The market-facing solution designed to get the job done | `[Name]: [What it does for the executor]` |
| **Work Process** | The end-to-end process the offering enables | `[Process name]: [Input] → [Output]` |

### Tier 2 — Step Level (Tactical)

The middle layer. Defines *how* — the structure of execution.

| Domain | Definition | Format |
|--------|-----------|--------|
| **Job Step** | One of the 8 universal job map steps | Per ODI: Define, Locate, Prepare, Confirm, Execute, Monitor, Modify, Conclude |
| **Execution Barrier** | What prevents or degrades successful completion of a job step | `[At step X], the executor cannot [do what] because [why]` |
| **Capability** | A functional ability the offering must have to remove a barrier | `Ability to [do what] [under what conditions]` |
| **Process Step** | A discrete step in the offering's workflow | `[Step number]: [Action] → [Output]` |

### Tier 3 — Outcome Level (Operational)

The atomic layer. Defines *how well* — measurable success criteria.

| Domain | Definition | Format |
|--------|-----------|--------|
| **Outcome Statement** | How the executor measures success at a job step | `Minimize/Maximize + [measure] + [object] + [context]` (ODI format) |
| **Unmet Metric** | The satisfaction gap on a specific outcome statement — the ODI opportunity score applied to this outcome | `[Outcome statement] — Importance: [1-10], Satisfaction: [1-10], Opportunity: [score]` |
| **Performance Requirement** | What must be true for the capability to satisfy the outcome | `Must [achieve what] to [what standard] [under what conditions]` |
| **Proof Point** | Evidence that the requirement is met | `[Metric/test]: [Pass criteria]` |

**Clarification — Unmet Metric vs. Outcome Statement:**
The outcome statement defines *what the executor wants* (the metric of success). The unmet metric quantifies *how far current solutions fall short* on that outcome. Together they form the ODI opportunity score: `Importance + (Importance - Satisfaction)`. A high-opportunity pair (score > 12) signals a need worth addressing. The unmet metric is not a separate data type — it's the satisfaction gap measured against the outcome statement.

---

## Relationships

### Vertical (within a domain)

```
Tier 1 (Job)
  └── contains 1:many → Tier 2 (Step)
       └── contains 1:many → Tier 3 (Outcome)
```

- A Core Job contains multiple Job Steps
- Each Job Step contains multiple Outcome Statements
- A Problem Statement contains multiple Execution Barriers
- Each Execution Barrier contains multiple Unmet Metrics
- An Offering contains multiple Capabilities
- Each Capability contains multiple Performance Requirements

### Horizontal (across domains at same tier)

```
JTBD Domain ←→ Problem Domain ←→ Offering Domain ←→ Process Domain
```

At each tier, the four domains describe the same reality from different perspectives:
- **Tier 1:** "What's the job?" ↔ "What's broken?" ↔ "What do we build?" ↔ "How does it work?"
- **Tier 2:** "What are the steps?" ↔ "Where does it fail?" ↔ "What abilities are needed?" ↔ "What does the process do?"
- **Tier 3:** "What does success look like?" ↔ "What's specifically unmet?" ↔ "What must be true?" ↔ "How do we prove it?"

---

## Layer Usage

| Layer | Uses Tiers | Purpose |
|-------|-----------|---------|
| **Engagement Layer** | Tier 1 | Understanding intent — what job, what problem, what offering |
| **Execution Layer** | Tiers 2-3 | Doing the work — steps, barriers, capabilities, requirements |
| **Assurance Layer** | Tier 3 | Validating output — outcomes met, metrics satisfied, proof delivered |

---

## Process Domain Scope

The Process Domain describes **how the executor experiences and uses the offering** — not how the offering works internally. This aligns with ODI's consumption chain jobs (learn, install, use, maintain, dispose).

| Tier | Describes | Not |
|------|----------|-----|
| Work Process | The executor's end-to-end workflow with the offering | Internal system architecture |
| Process Step | A discrete step the executor takes | Backend implementation detail |
| Proof Point | Evidence the executor can observe that the requirement is met | Internal test suite |

If you need to describe internal implementation, that belongs in a separate engineering spec — not in this data model.

---

## Pipeline Flow

The data model is populated across four phases:

```
Phase 1: Problem Decomposition
  → Populates: Problem Domain (all 3 tiers)
  → Method: First principles decomposition + 5 Whys
  → Skills: first-principles-decomposition, five-whys
  → Gate: Assumption Challenger validates output

Phase 2: System Mapping
  → Populates: Stakeholder map, executor identification, cross-dependencies
  → Method: Stakeholder enumeration, classification, job hypothesis
  → Gate: Assumption Challenger + Systems Dynamics Checker
  → Decision: Which executors proceed to Phase 3?

Phase 3: Job Mapping (per executor)
  → Populates: JTBD Domain (all 3 tiers) — one set per executor
  → Method: ODI job mapping (core job → job map → outcome statements)
  → Includes: Citation validation of Core Job (3 sources), Job Map (3 sources), and Relevant outcomes (3 sources each)
  → Includes: Mutual exclusivity check on outcome statements
  → Includes: Relevance tagging (Relevant / Adjacent / Out of scope)
  → Skills: jtbd-mapping
  → Gate: ODI Compliance Checker + Outcome Research Validator + Cross-Reference Mapper
  → Note: Runs as a loop for each executor identified in Phase 2

Phase 4: Offering Design (Diverge → Converge)
  → Populates: Offering Domain + Process Domain (all 3 tiers)
  → STAGE A (Diverge): Executor-grounded proxy scoring → performance requirements → unconstrained solution ideation (bell curve: conservative / expected / novel per requirement)
  → STAGE B (Converge): Competitive landscape analysis → approach selection (unmet needs × white space) → capability clustering → offering composition → degraded-mode design → "So What?" test
  → Includes: Proof points as falsifiable experiments (not just metrics)
  → Gate: Cross-Reference Mapper + Assumption Challenger
  → Optional: Systems Dynamics Checker for second-order effects

Phase 5: Analysis & Executive Summary
  → Synthesizes all four phases into a decision-ready document
  → Step 1: Executive Overview (orient the reader)
  → Step 2: Chain of Logic (explicit, evidence-backed links from problem → offering)
  → Step 3: Deep Offering Description (plain language, evidence trail, competitive positioning)
  → Step 4: Validation & Next Steps (prioritized experiments, sequenced actions)
  → Step 5: Data Model Completeness (12-cell grid verification)
  → Step 6: Honest Limitations (scope exclusions, unvalidated assumptions, evidence gaps)
  → Step 7: Net Assessment (defensibility, core risk, recommended next action)
  → Gate: Chain of logic complete, limitations documented, next steps sequenced
  → Output: executive-summary.md in run folder
```

### Decision Gates

Each phase ends with a decision gate before proceeding:

| Gate | Question | Proceed If | Recycle If |
|------|----------|-----------|------------|
| Phase 1 → 2 | Is the problem decomposed to atomic, evidence-backed elements? | Root causes identified, assumptions surfaced | Assumptions remain hidden, root cause feels premature |
| Phase 2 → 3 | Do we know who the job executors are and how they relate? | Executors classified, dependencies mapped | Stakeholders unclear, executor/influencer distinction shaky |
| Phase 3 → 4 | Are outcome statements complete, research-validated, and cross-referenced? | ODI-compliant, Relevant outcomes have 2+ sources, barriers mapped to outcomes | Outcomes unvalidated by research, feel solution-specific, gaps in job map |
| Phase 4 → 5 | Does the offering trace cleanly from outcomes through capabilities? | All 12 grid cells populated, no orphans | Capabilities that don't trace to outcomes, missing proof points |
| Phase 5 → Done | Is the analysis synthesized, honest, and actionable? | Chain of logic explicit, limitations documented, next steps sequenced | Weak links unacknowledged, flat next steps, missing limitations |
