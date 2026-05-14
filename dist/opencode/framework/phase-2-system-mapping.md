# Phase 2 — System Mapping

Understand the system of stakeholders around the problem and identify which are job executors whose jobs should be mapped.

---

## Why This Phase Exists

Problems don't exist in isolation — they're embedded in systems of actors with interdependent goals, constraints, and jobs. Phase 1 gives you the atomic problem. Phase 2 answers: **"Who's in this system, and whose jobs matter?"**

Without this phase, you risk:
- Mapping a single executor's job while ignoring the system that constrains them
- Building an offering for the wrong stakeholder
- Missing interdependencies where one executor's outcome is another's input

---

## Input

- Atomic problem statement (from Phase 1)
- Root cause analysis with classified causes (from Phase 1)
- Preliminary actor list surfaced during causal analysis (from Phase 1, Step 4)
- Identified assumptions (from Phase 1)

## Output

- Stakeholder map with roles, relationships, and influence
- Classified stakeholders: job executors vs. influencers vs. constraints
- Preliminary job hypotheses per executor
- Cross-executor dependencies identified
- Decision: which executors proceed to Phase 3 (Job Mapping)

---

## Process

### Step 1: Organize and Complete the Stakeholder List

Phase 1's causal analysis will have already surfaced most actors. This step's job is to **organize** what Phase 1 found and **identify anyone missing** — not to start from scratch.

Start with the preliminary actor list from Phase 1, Step 4. Then check for gaps:
- Are there actors **upstream** of the earliest actor in the causal chain? (who feeds them?)
- Are there actors **downstream** of the consequences? (who bears the impact?)
- Are there **invisible actors** not in the causal chain but who control systems, policies, or resources that shape the problem? (IT, compliance, procurement, legal)
- Are there **external actors** who set the rules or constraints? (regulators, auditors, standards bodies)

**Format:**

| # | Stakeholder | Source | Relationship to Problem | Why They're in the System |
|---|------------|--------|------------------------|--------------------------|
| 1 | [Role/person] | Phase 1 / New | Experiences / Contributes / Affected / Would be affected | [Specific reason] |

**Rule:** List roles, not departments. "Marketing analyst who builds campaign reports" not "Marketing."

#### Step 1b: Validate Stakeholder Completeness

Cite **2-3 sources** confirming the stakeholder system for this problem domain. Sources should describe who is typically involved when this type of problem occurs — ensuring the list isn't limited to the analyst's imagination.

| Source | Type | Stakeholders Confirmed | Stakeholders Missing from Our List |
|--------|------|----------------------|-----------------------------------|
| [Source + link] | Org research / Process documentation / Industry workflow description | [Which of our stakeholders appear] | [Any roles described in the source we missed] |

**Gate:** If sources consistently describe stakeholders not on the list, add them before proceeding. If our list includes stakeholders that no source mentions, flag them as "analytical inference — low confidence."

### Step 2: Map Relationships

For each pair of stakeholders, identify:
- **Information flows** — who provides what to whom?
- **Decision authority** — who approves, blocks, or enables?
- **Dependency chains** — whose output is another's input?
- **Incentive alignment** — do they want the same outcomes?

**Format (adjacency list):**

```
[Stakeholder A] → [Stakeholder B]
  Flow: [What passes between them]
  Direction: [A→B / B→A / Bidirectional]
  Dependency: [A depends on B for X / mutual / none]
  Alignment: [Aligned / Misaligned / Neutral]
```

**Look for:**
- **Bottlenecks** — stakeholders that many others depend on
- **Misalignment** — stakeholders with conflicting incentives
- **Invisible actors** — roles that aren't obvious but influence the system (IT, compliance, procurement)

#### Step 2b: Validate Critical Dependencies

At least the **critical dependencies** (bottlenecks, misalignments) must cite a source — not all relationships, just the ones that drive downstream decisions.

| Critical Dependency | Source | Type | Key Evidence |
|--------------------|--------|------|-------------|
| [Stakeholder A → B: bottleneck/misalignment] | [Source + link] | Process documentation / Workflow guide / Practitioner account | [Evidence this dependency exists in practice] |

**Note:** This is a light validation. Not every relationship needs a citation — focus on the ones that will influence executor selection or offering design.

### Step 3: Classify Stakeholders

Assign each stakeholder one primary classification:

| Classification | Definition | Criteria | Proceeds to Phase 3? |
|---------------|-----------|----------|----------------------|
| **Job Executor** | Has a functional job-to-be-done that the problem prevents or degrades | They are *trying to accomplish something* and the problem gets in the way | Yes — gets a full ODI job map |
| **Influencer** | Affects the executor's ability to do the job but doesn't have their own job in this context | They make decisions, set policy, or provide inputs | No — but their constraints inform the job map |
| **Constraint** | A structural role that imposes requirements (compliance, legal, IT policy) | They don't choose to be involved; their role creates boundaries | No — but their requirements become boundary conditions |
| **Beneficiary** | Benefits from the problem being solved but doesn't experience it directly | They receive downstream value | No — but they validate the offering's value proposition |

**Decision rule:** If you're unsure whether someone is an executor or influencer, ask: "Are they trying to make progress on a functional job, or are they reacting to someone else's job?" Executors initiate; influencers respond.

#### Step 3b: Validate Executor Classifications

Each **Job Executor** classification must cite at least one source showing this role initiates a functional job — not just participates in the problem system.

| Executor | Source | Type | Evidence of Functional Job |
|----------|--------|------|---------------------------|
| [Role] | [Source + link] | Job description / Role definition / Professional association | [Evidence this role's primary function involves initiating a job relevant to the problem] |

**Acceptable source types:** Job postings (Indeed, LinkedIn, BLS), professional association role definitions, certification body descriptions, company role documentation.

#### Defining a Job Executor (Not a Title)

A job executor is described by **what they do**, not what they're called. Titles vary across organizations; the functional role is stable.

**Format:** `The person who [primary functional activity] in [context]`

**Examples:**
- "The person who classifies transactions for tax compliance in a corporate AP department"
- "The person who reviews and approves vendor invoices before payment release"

**Then list possible titles:** After defining the executor functionally, list 3-5 titles this person might hold across organizations. This helps with research and source finding.

| Executor (Functional) | Possible Titles |
|-----------------------|----------------|
| The person who [does X] in [context] | Title A, Title B, Title C |

### Step 4: Hypothesize Jobs per Executor

For each identified job executor, draft a preliminary core job hypothesis.

**Format:**

| Executor | Hypothesized Core Job | Confidence | Key Assumption |
|----------|----------------------|------------|----------------|
| [Role] | [Action verb] + [object] + [context] | High/Med/Low | [What we're assuming] |

**Rules:**
- Follow ODI format (solution-agnostic, stable, functional)
- These are *hypotheses* — Phase 3 will validate and refine
- Multiple executors may share the same core job (they become segments, not separate jobs)
- One executor may have multiple relevant jobs (flag this — Phase 3 may need to prioritize)

### Step 5: Map Cross-Executor Dependencies

Where one executor's job step produces an output that another executor needs:

```
[Executor A] — [Job Step X] → produces → [Output]
                                              ↓
[Executor B] — [Job Step Y] → requires → [that Output]
```

**This reveals:**
- Where the system creates bottlenecks (Executor B is blocked by Executor A)
- Where the offering might need to serve multiple executors simultaneously
- Where a single-executor offering would fail because it ignores upstream/downstream dependencies

#### Step 5b: Validate Critical Handoffs

Cite at least one source per **critical handoff** — where one executor's output becomes another's input.

| Handoff | Source | Type | Key Evidence |
|---------|--------|------|-------------|
| [Executor A Step X] → [Executor B Step Y] | [Source + link] | Process documentation / Workflow guide / Practitioner account | [Evidence this handoff exists and matters] |

**Note:** Focus on handoffs that, if broken, would block downstream executors. Not every dependency needs a citation.

### Step 6: Decide Who Gets Mapped

Not every executor gets a full ODI job map in Phase 3. Select based on:

| Criterion | Weight |
|-----------|--------|
| **Proximity to the problem** — how directly does their job relate to the root cause? | High |
| **Leverage** — would solving their job have cascading benefits for other stakeholders? | High |
| **Feasibility** — can we realistically build an offering for this executor? | Medium |
| **Access** — can we learn enough about their job to map it well? | Medium |

**Output:** A ranked list of executors to map in Phase 3, with rationale for inclusion/exclusion.

#### Step 6b: Ground Executor Selection in Evidence

Proximity and leverage scores must reference **specific evidence from Phase 1 root causes** — not just analytical intuition.

| Executor | Proximity Score | Proximity Evidence | Leverage Score | Leverage Evidence |
|----------|----------------|-------------------|----------------|-------------------|
| [Role] | High / Medium / Low | [Which Phase 1 root cause(s) directly involve this executor] | High / Medium / Low | [Which downstream stakeholders would benefit if this executor's job improved] |

**Rule:** "Feels close to the problem" is not evidence. Each proximity claim must point to a specific terminal why or execution barrier from Phase 1. Each leverage claim must point to specific cross-executor dependencies from Step 5.

---

## Decision Gate

Before proceeding to Phase 3, validate:

- [ ] Stakeholder list validated with 2-3 external sources (no obvious gaps)
- [ ] Classifications are defensible (executor vs. influencer distinctions hold up)
- [ ] Each executor classification cites at least one source showing the role initiates a functional job
- [ ] Executors are defined functionally (not by title) with possible titles listed
- [ ] At least one job executor has been identified with a plausible core job
- [ ] Critical dependencies (bottlenecks, misalignments) cite at least one source each
- [ ] Critical handoffs cite at least one source each
- [ ] Cross-dependencies are mapped (we know where executor jobs interact)
- [ ] Executor selection scores reference specific Phase 1 evidence (not just intuition)
- [ ] The subset selected for Phase 3 mapping is justified

**If no clear job executors emerge:** The problem may be systemic rather than job-based. Consider whether the ODI framework is the right tool, or whether the problem needs to be reframed.

---

## Anti-Patterns

### The Org Chart Trap
Mapping stakeholders by organizational structure instead of by their role in the problem system.

**Fix:** Two people in the same department may play completely different roles in the system. Two people in different departments may play the same role.

### The Single-Hero Assumption
Assuming one executor is "the" user and everyone else is peripheral.

**Fix:** The system mapping exists precisely because problems usually involve multiple executors. Resist the urge to simplify prematurely.

### The Consensus Fallacy
Assuming all stakeholders want the same outcome.

**Fix:** Explicitly map incentive alignment. Misaligned incentives are often the root cause of persistent problems.

### Skipping to Job Mapping
Eager to get to ODI and skipping the system analysis.

**Fix:** Phase 2 exists because Phase 3 (job mapping) is expensive. Better to spend time here choosing the *right* executors to map than to map the wrong ones thoroughly.

---

## Quick Reference

### Stakeholder Classifications
- **Executor** — has a job; the problem degrades it → map in Phase 3
- **Influencer** — affects executors but doesn't have their own job here → informs the map
- **Constraint** — imposes structural boundaries → becomes boundary conditions
- **Beneficiary** — benefits downstream → validates value proposition

### Key Questions
1. Who experiences this problem?
2. Who contributes to it?
3. Who's affected by consequences?
4. Whose output is someone else's input?
5. Who has misaligned incentives?

### Decision Rule for Executors
> "Are they trying to make progress on a functional job, or reacting to someone else's?"
> Executors initiate. Influencers respond.
