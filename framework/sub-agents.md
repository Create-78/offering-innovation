# Sub-Agents

Specialized analytical roles invoked throughout the pipeline. These aren't separate tools — they're defined perspectives that can be activated at specific points to challenge, validate, or maintain the analysis.

---

## Why Sub-Agents?

Each phase requires a different cognitive mode. Sub-agents formalize this so that critical perspectives aren't skipped. They can be invoked explicitly ("Run the Assumption Challenger on this output") or automatically at phase gates.

---

## Agent Definitions

### 1. Assumption Challenger

**Purpose:** Pressure-test every claim, classification, and conclusion for hidden assumptions.

**When invoked:**
- After Phase 1 (Move 2 of first principles — are we correctly separating facts from assumptions?)
- After Phase 2 (are stakeholder classifications defensible?)
- After Phase 3 (are outcome statements truly solution-agnostic?)
- After Phase 4 (do performance requirements actually trace to outcomes?)
- Anytime a claim feels "obviously true" — that's when it most needs challenging

**Method:**
1. List every claim in the output
2. For each, ask: "What evidence supports this? What would disprove it?"
3. Apply the Inversion Test: state the opposite. Is it also plausible?
4. Classify: **Verified** (evidence exists), **Testable** (could be verified), **Assumed** (taken on faith)
5. Flag all "Assumed" items — they are risks

**Output format:**

| Claim | Evidence | Inversion Plausible? | Classification | Risk if Wrong |
|-------|----------|---------------------|----------------|---------------|
| [Claim] | [Evidence or "none"] | Yes/No | Verified/Testable/Assumed | [Impact] |

---

### 2. ODI Compliance Checker

**Purpose:** Validate that all JTBD artifacts follow strict ODI methodology.

**When invoked:**
- After writing any job statement
- After completing a job map
- After generating outcome statements
- Before proceeding from Phase 3 to Phase 4

**Checks:**

**Job Statement Validation:**
- [ ] Format: `[Action verb] + [object] + [context]`
- [ ] Solution-agnostic (no products, technologies, methods)
- [ ] Stable over time (would exist without current solutions)
- [ ] Functional first (not emotional or social)
- [ ] Right abstraction level (core functional, not aspirational or micro)

**Job Map Validation:**
- [ ] All 8 steps covered (Define, Locate, Prepare, Confirm, Execute, Monitor, Modify, Conclude)
- [ ] 3-8 sub-activities per step
- [ ] Steps are sequential and non-overlapping
- [ ] No solution-specific language

**Outcome Statement Validation:**
- [ ] Format: `Minimize/Maximize + [measure] + [object of control] + [contextual clarifier]`
- [ ] Uses "minimize" or "maximize" (not "reduce," "improve," "ensure")
- [ ] One metric per statement (no compound outcomes)
- [ ] Solution-agnostic (no features or tools mentioned)
- [ ] Controllable (a solution could affect this)
- [ ] Tied to a specific job step
- [ ] 5-15 outcomes per job step

**Output format:**

| Artifact | Check | Pass/Fail | Issue | Fix |
|----------|-------|-----------|-------|-----|
| [Item] | [Rule] | Pass/Fail | [What's wrong] | [How to fix] |

---

### 3. Cross-Reference Mapper

**Purpose:** Maintain and validate the linkages across all four domains of the three-tier data model.

**When invoked:**
- At the end of each phase (to connect new data to existing data)
- When the data model feels inconsistent
- Before final offering assembly (Phase 4)

**Method:**
1. For each populated cell in the three-tier grid, verify it links to its horizontal neighbors
2. For each vertical relationship (Tier 1 → 2 → 3), verify containment is correct
3. Identify orphans — items that don't connect to anything
4. Identify gaps — cells that should be populated but aren't

**Output format:**

```
LINKAGE MAP
===========

Tier 1:
  Core Job ↔ Problem Statement: [linked / gap / conflict]
  Problem Statement ↔ Offering: [linked / gap / conflict]
  Offering ↔ Work Process: [linked / gap / conflict]

Tier 2:
  [Job Step X] ↔ [Barrier Y]: [linked / gap / conflict]
  [Barrier Y] ↔ [Capability Z]: [linked / gap / conflict]
  ...

Tier 3:
  [Outcome A] ↔ [Unmet Metric B]: [linked / gap / conflict]
  [Unmet Metric B] ↔ [Perf Req C]: [linked / gap / conflict]
  ...

ORPHANS: [Items with no cross-domain link]
GAPS: [Expected links that are missing]
CONFLICTS: [Links that contradict each other]
```

---

### 4. Systems Dynamics Checker

**Purpose:** Identify feedback loops, emergent behaviors, and unintended consequences in the stakeholder system and proposed offering.

**When invoked:**
- After Phase 2 (System Mapping) — are there reinforcing loops we're missing?
- After Phase 4 (Offering Design) — does the offering create new problems?

**Method:**
1. Map causal links between stakeholders and their jobs
2. Look for reinforcing loops (A → B → A, amplifying)
3. Look for balancing loops (A → B → ¬A, stabilizing)
4. For proposed offerings, trace second-order effects: "If we solve X, what happens to Y?"

**Output format:**

| Loop | Type | Stakeholders | Implication |
|------|------|-------------|-------------|
| [A → B → A] | Reinforcing / Balancing | [Who's involved] | [What this means] |

| Second-Order Effect | Trigger | Impact | Severity |
|-------------------|---------|--------|----------|
| [Effect] | [If we do X] | [Then Y happens] | High/Med/Low |

---

### 5. Outcome Research Validator

**Purpose:** Validate that identified outcome statements reflect real, meaningful needs — not analytical artifacts — by finding third-party evidence that the outcome matters to job executors. Also validates Core Job statements and Job Map structure.

**When invoked:**
- After Phase 3, Step 1 — validates Core Job statement (3 sources)
- After Phase 3, Step 2 — validates Job Map structure (3 sources)
- After Phase 3, Step 3c (relevance tagging) — validates all "Relevant" outcomes
- During Phase 4, Step 1 — provides executor-perspective evidence for proxy scoring
- Optionally for "Adjacent" outcomes if time permits

**Method:**
1. For each Relevant outcome statement, search for a minimum of 3 third-party sources
2. Sources must span three categories to triangulate validity:
   - **Industry/expert:** Reports, whitepapers, academic research, professional association publications
   - **Practitioner/trade:** Trade publications, professional forums, conference proceedings, thought leadership
   - **Voice-of-executor:** Reddit, Glassdoor, community posts, Quora, practitioner blogs, interview transcripts
3. For each source, extract the key quote or finding that relates to the outcome
4. Assess whether the source confirms, partially confirms, or contradicts the outcome

**Output format:**

| Outcome | Source | Type | Key Finding | Confirms? |
|---------|--------|------|-------------|-----------|
| [Statement] | [Name + link] | Industry / Practitioner / Voice | [Excerpt] | Yes / Partial / No |

**Validation thresholds:**
- **3 confirming sources (at least 2 types):** Validated — proceed with confidence
- **2 confirming sources:** Validated with caution — note the gap
- **0-1 confirming sources:** Downgrade from Relevant to Adjacent — this outcome may be an analytical artifact
- **Any contradicting source:** Flag for review regardless of other sources — the contradiction may reveal a nuance in the outcome statement

**Why voice-of-executor sources matter:** Industry reports describe what *should* be true. Practitioner sources describe what *professionals think* is true. Voice-of-executor sources describe what *actually hurts*. The gap between these three is often where the real insight lives.

---

## Invocation Schedule

| Phase | Required Agents | Optional Agents |
|-------|----------------|-----------------|
| Phase 1: Problem Decomposition | Assumption Challenger | — |
| Phase 2: System Mapping | Assumption Challenger, Systems Dynamics Checker | — |
| Phase 3: Job Mapping | ODI Compliance Checker, Outcome Research Validator, Cross-Reference Mapper | Assumption Challenger |
| Phase 4: Offering Design | Cross-Reference Mapper, Assumption Challenger | Systems Dynamics Checker |
| Phase 5: Analysis & Executive Summary | Cross-Reference Mapper, Assumption Challenger | All others as needed |

---

## Usage Pattern

When invoking a sub-agent, use this format:

```
> [AGENT: Assumption Challenger]
> Target: [What's being reviewed]
> Phase: [Which phase]
> Specific concern: [If any, or "general review"]
```

The agent produces its output, then control returns to the main analysis.
