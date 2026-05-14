# Phase 1 — Problem Decomposition

Transform a problem statement into an atomic understanding of root causes and fundamental assumptions.

---

## Input

A problem statement (can be rough, vague, or assumption-laden).

## Output

- Validated problem statement (Tier 1)
- Execution barriers (Tier 2)
- Unmet metrics (Tier 3)
- Preliminary actors surfaced (carried forward to Phase 2 for classification)
- Fundamental assumptions surfaced

---

## Process

### Step 1: State the Problem

Capture the problem as given. Don't refine yet.

**Prompt:** "What's the problem? State it however it comes to mind."

### Step 2: First Principles Decomposition

Break the problem into its constituent parts. For each claim in the problem statement, ask:

1. **What is actually true here?** (vs. assumed)
2. **What are the underlying components?** (decompose)
3. **What would remain if we removed all assumptions?** (irreducible core)

**Goal:** Separate facts from assumptions, identify the atomic elements.

### Step 3: 5 Whys

Starting from the stated problem, ask "Why?" iteratively:

| Level | Question | Answer |
|-------|----------|--------|
| Why 1 | Why does [problem] exist? | [Because...] |
| Why 2 | Why does [that] happen? | [Because...] |
| Why 3 | Why does [that] occur? | [Because...] |
| Why 4 | Why is [that] the case? | [Because...] |
| Why 5 | Why is [that] fundamental? | [Root cause] |

**Rules:**
- Each "why" must be answerable with evidence or logic, not opinion
- If a "why" branches (multiple causes), follow each branch
- Stop when you reach something that is a law, constraint, or structural truth
- The root cause should feel *irreducible* — you can't decompose it further

#### Step 3b: Root Cause Citation (per Terminal Why)

Each terminal node in the 5 Whys must cite at least one source confirming it is structurally true — not just logically derived from the branch above it. "Because [X]" needs evidence that X is actually the case in the real world.

**Why this matters:** Without external validation, the 5 Whys becomes a logic chain that sounds right but is actually an analytical artifact — each "because" follows from the one above it without any of them being independently verified.

| Terminal Why | Source | Type | Key Evidence | Confirmed? |
|-------------|--------|------|-------------|------------|
| [Root cause statement] | [Source + link] | Industry report / Practitioner account / Research / Regulatory | [Quote or finding confirming this is structurally true] | Yes / Partially / No |

**Rules:**
- Every terminal node needs at least one source — not every intermediate node
- Sources must confirm the claim is structurally true in the real world, not just logically possible
- If a terminal why can't be sourced, flag it as "unvalidated — analytical inference only" and note the confidence level
- Unvalidated terminal whys don't block progress but must be carried forward as assumptions (Step 6)

### Step 4: Surface Actors

The causal tree from Step 3 will naturally reveal people and roles involved in the problem. Capture them here as a preliminary list — **do not classify or prioritize them yet.** Phase 2 handles stakeholder classification.

For each actor that appears in the root cause tree, note:

| Actor | Where They Appeared | Role in the Causal Chain |
|-------|-------------------|-------------------------|
| [Role/person] | [Which branch of the 5 Whys] | [Experiences / Causes / Is affected by] |

**Rules:**
- List every actor that shows up, even if their role isn't clear yet
- Use role names, not departments ("AP Specialist" not "Finance")
- Don't force a single "job executor" — that decision belongs to Phase 2
- It's fine if this list is messy; Phase 2 will organize it

### Step 5: Construct the Problem Domain Data

Map findings to the three-tier structure:

**Tier 1 — Problem Statement:**
`[Job executor] struggles to [do what] because [root cause from 5 Whys]`

**Tier 2 — Execution Barriers:**
For each branch of the 5 Whys that reveals a structural failure:
`At [step/moment], the executor cannot [do what] because [why]`

**Tier 3 — Unmet Metrics:**
For each barrier, identify the measurable gap:
`Current [measure] is [current state]; desired is [target state]`

### Step 5b: Validate Problem Statement with Citations

The constructed problem statement must be validated with **3 credible cited sources** confirming the problem is real and recognized — not just internally coherent. This mirrors Phase 3's core job validation.

| Source | Type | Key Evidence | Confirms Problem? |
|--------|------|-------------|-------------------|
| [Source + link] | Industry/expert | [Quote or finding confirming the problem exists at a structural level] | Yes / Partially / No |
| [Source + link] | Practitioner/trade | [Quote or finding from professionals who describe this problem] | Yes / Partially / No |
| [Source + link] | Voice-of-executor | [Quote or finding from people experiencing the problem] | Yes / Partially / No |

**Source types (need all 3 categories):**
- **Industry/expert source** — confirms the problem exists at a structural level (reports, whitepapers, research, regulatory documents)
- **Practitioner/trade source** — confirms professionals describe this problem (trade publications, conference talks, LinkedIn thought leadership)
- **Voice-of-executor source** — confirms the people experiencing it recognize it (Reddit, forums, practitioner blogs, Glassdoor)

**Gate:** If the problem statement can't be validated by at least 2 of 3 source types, reconsider whether the problem as stated is real or whether it needs reframing.

#### Unmet Metric Precision Note

Phase 1 unmet metrics operate at **Level 1 precision** — source-backed current state with directional gaps. Each unmet metric should cite at least one source confirming the current state is real (not just analytically inferred).

| Unmet Metric | Current State Source | Confidence | Notes |
|-------------|---------------------|------------|-------|
| [Metric] | [Source confirming current state] | High / Medium / Low | [Any caveats] |

Metrics that can't meet Level 1 (no source for current state) are flagged as "directional with no anchor" and carried forward as assumptions. Phase 4 upgrades scoring to Level 3 (executor-grounded proxy or quantitative ODI scoring) when it prioritizes outcomes.

### Step 6: Surface Assumptions

List every assumption embedded in the analysis:

| # | Assumption | Confidence | How to Validate |
|---|-----------|------------|-----------------|
| 1 | [Assumption] | High/Med/Low | [Method] |

---

## Quality Checks

- [ ] Root cause feels irreducible (can't ask "why" again productively)
- [ ] Every terminal why is cited with at least one external source (or flagged as unvalidated)
- [ ] Job executor is a person, not an organization or abstraction
- [ ] Problem statement is solution-agnostic
- [ ] Problem statement validated with 3 cited sources (industry, practitioner, voice-of-executor)
- [ ] Every execution barrier maps to a specific failure point
- [ ] Unmet metrics are measurable (even if directionally)
- [ ] Unmet metrics cite at least one source for current state (Level 1 precision)
- [ ] Metrics without sources are flagged as "directional with no anchor"
- [ ] Assumptions are stated explicitly, not hidden in the analysis
