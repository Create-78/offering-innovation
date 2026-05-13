# Phase 3 — Job Mapping (ODI)

Map each job executor's world using strict ODI methodology. Build from core job through job map to outcome statements. Runs once per executor identified in Phase 2.

---

## Input

- Ranked list of job executors with hypothesized core jobs (from Phase 2)
- Stakeholder relationships and cross-dependencies (from Phase 2)
- Root cause analysis and execution barriers (from Phase 1)
- Fundamental assumptions (from Phase 1)

## Output

- Core Job statement (Tier 1)
- Job Map with all 8 steps (Tier 2)
- Desired Outcome Statements per step (Tier 3)
- Linkage back to Problem Domain

---

## Process

### Step 1: Define the Core Job

Using the job executor from Phase 1, define the core functional job.

**Format:** `[Action verb] + [object of action] + [contextual clarifier]`

**ODI Rules (strict):**
- Solution-agnostic — no products, technologies, or methods
- Stable over time — the job existed before current solutions
- Functional first — emotional/social jobs come after
- Right level of abstraction — core functional, not aspirational or micro

**Validation:** Ask "Would this job exist if [current solutions] didn't?" If yes, it's a real job.

#### Step 1b: Validate Core Job with Citations

The Core Job statement must be validated with **3 credible cited sources** confirming this is how the real world describes this executor's primary function. If the core job can't be validated externally, it may be an analytical construct rather than a real job.

| Source | Type | Key Evidence | Confirms Core Job? |
|--------|------|-------------|-------------------|
| [Source + link] | Job description / Industry report / Professional association / Academic | [Quote or finding showing this is the executor's primary function] | Yes / Partially / No |

**Source types (need at least 2 of these 3 categories):**
- **Job descriptions / role definitions:** How employers describe this role's primary purpose (Indeed, LinkedIn, company postings, BLS descriptions)
- **Industry / professional sources:** How the profession describes its own core function (professional associations, certification bodies, industry standards)
- **Academic / research sources:** How researchers or analysts characterize this role's purpose

**Gate:** If 0-1 sources confirm the core job, **stop and reframe** before proceeding. The job map built on a weak core job will produce unreliable outcomes.

### Step 2: Build the Job Map

Walk the 8 universal steps of the ODI job map:

| Step | Definition | Guiding Question |
|------|-----------|-----------------|
| 1. Define | Determine goals and plan approach | What is the executor trying to achieve? How do they plan? |
| 2. Locate | Gather inputs and information | What do they need to find or collect before starting? |
| 3. Prepare | Set up inputs and environment | How do they get ready? What setup is required? |
| 4. Confirm | Verify readiness to proceed | How do they know they can start? What must be true? |
| 5. Execute | Carry out the core action | What is the main activity? |
| 6. Monitor | Track whether it's working | How do they know it's going well? |
| 7. Modify | Make adjustments | What changes when things deviate? |
| 8. Conclude | Finish and clean up | How do they wrap up and know they're done? |

For each step, document 3-8 sub-activities.

#### Step 2b: Validate Job Steps with Citations

The job map structure must be validated with **3 credible cited sources** confirming the steps are mutually exclusive and reflect how the executor actually works — not how an analyst thinks they should work.

**Validation requirements:**
1. **Mutual exclusivity:** Each step must describe a distinct activity. If two steps overlap in how sources describe the executor's workflow, merge or redefine them.
2. **Real-world reflection:** Sources should describe the executor performing these steps (or equivalent activities) in practice.

| Source | Type | Steps Confirmed | Steps Contradicted or Missing | Notes |
|--------|------|----------------|------------------------------|-------|
| [Source + link] | Process doc / Practitioner account / Training material / Research | [e.g., Steps 1-5 clearly described] | [e.g., Step 7 not evident in practice] | [Relevant context] |

**Source types (need at least 2 of these 3 categories):**
- **Process documentation:** SOPs, training materials, certification curricula, workflow guides published by employers or industry bodies
- **Practitioner accounts:** How executors describe their own workflow (blog posts, conference talks, Reddit/forum posts, interview transcripts)
- **Research / analysis:** Academic studies, consulting reports, or time-motion studies of the executor's work

**Gate:** If sources consistently show the executor skips, merges, or reorders steps compared to the proposed map, revise the map. The map should describe reality, not theory. Steps that can't be validated by any source should be flagged as "unvalidated — low confidence."

### Step 3: Generate Outcome Statements

For each job step, generate 5-15 desired outcome statements.

**Format:** `Minimize/Maximize + [measure] + [object of control] + [contextual clarifier]`

**ODI Rules (strict):**
- Always "minimize time to [object/context] OR minimize likelihood of [object/context]" — creates measurable scale
- One outcome per statement — no compound metrics
- Solution-agnostic — no products or features mentioned
- Controllable — something a solution could actually affect
- Tied to a specific job step

**Common measures:** Express all outcomes using the two forms above; common dimensions (effort, cost, accuracy, completeness, frequency) map to one or the other — e.g. accuracy as 'minimize likelihood of error', cost as 'minimize likelihood of overrun'.

### Step 3b: Validate Outcome Statements are Mutually Exclusive

Before tagging relevance, verify that outcome statements within each step are **mutually exclusive** — each measures a distinct dimension of success. If two outcomes overlap (e.g., both measure speed of the same activity from slightly different angles), merge them.

**Within-step test:** For any two outcomes in the same step, ask: "Could a solution improve one without affecting the other?" If yes, they're distinct. If improving one necessarily improves the other, they overlap — merge or eliminate one.

#### Step 3b-ii: Cross-Step Redundancy Check

After within-step validation, run the mutual exclusivity test **across all steps**. Outcomes in different steps can still overlap if they measure the same underlying dimension from different vantage points.

**Cross-step test:** For any two outcomes in different steps, ask: "Could a solution improve outcome X without affecting outcome Y?" If they're in different steps but the answer is no, either merge them (assign to the step where the root activity occurs) or differentiate them (clarify what makes each distinct).

**Note:** This is a lighter check than within-step validation. Focus on outcomes that use similar language or reference the same object of control.

### Step 3c: Tag Outcome Relevance

After generating and validating the outcome statements, tag each one:

| Tag | Meaning | Carries to Phase 4? |
|-----|---------|---------------------|
| **Relevant** | Directly connected to the problem identified in Phase 1 | Yes — prioritized |
| **Adjacent** | Related to the problem space but not directly caused by the root causes | Yes — lower priority, may reveal expansion opportunities |
| **Out of scope** | Real outcome but unrelated to this problem | No — documented but not carried forward |

**Why tag instead of delete:** ODI says map the whole job because you might find unexpected opportunities. Tagging preserves completeness while focusing the offering design. Out-of-scope outcomes stay in the record for future reference.

#### Step 3c-ii: Validate Relevance Tags with Evidence

Each **"Relevant"** tag must cite the specific Phase 1 root cause or execution barrier it connects to — not just "related to the problem."

| Outcome | Tag | Connected Root Cause / Barrier | Causal Link |
|---------|-----|-------------------------------|-------------|
| [Outcome statement] | Relevant | [Specific Phase 1 terminal why or barrier] | [If this root cause were resolved, would this outcome improve? Yes/No + explanation] |

**Causal test:** Ask: "If this root cause were resolved, would this outcome improve?" If not, the connection is correlational, not causal — downgrade to Adjacent.

**Rule:** "Related to the problem" is not sufficient. The link must be directional: root cause → outcome degradation.

### Step 3d: Validate Outcomes with External Research

For each **Relevant** outcome statement, the Outcome Research Validator (sub-agent) finds a minimum of 3 third-party sources that confirm the outcome is real and meaningful to the job executor.

**Source requirements:**

| Slot | Source Type | Purpose | Examples |
|------|-----------|---------|---------|
| 1 | **Industry/expert source** | Confirms the outcome is recognized in professional practice | Industry reports, consulting whitepapers, professional association publications, academic research |
| 2 | **Practitioner/trade source** | Confirms the outcome is discussed by people who do the job | Trade publications, professional forums, conference proceedings, LinkedIn thought leadership |
| 3 | **Voice-of-executor source** | Contextualizes the pain/importance from the executor's lived experience | Reddit, Glassdoor, professional community posts, Quora, blog posts by practitioners, interview transcripts |

**Output per outcome:**

| Outcome | Source | Type | Key Quote/Finding | Confirms? |
|---------|--------|------|-------------------|-----------|
| [Outcome statement] | [Source name + link] | Industry/Practitioner/Voice | [Relevant excerpt] | Yes / Partially / No |

**Rules:**
- If an outcome can't be validated by at least 2 of 3 sources, flag it — it may be an artifact of the analysis rather than a real executor need
- Voice-of-executor sources are especially valuable because they use the executor's language, not the analyst's
- Sources don't need to use ODI language — they just need to describe the same pain/need in their own terms
- If a source contradicts the outcome, that's important — capture it and reassess

**Gate:** Any "Relevant" outcome that fails validation (0-1 sources) is downgraded to "Adjacent" with a note explaining why. This prevents phantom outcomes from driving offering design.

#### Step 3d-ii: Capture Importance Signals

During the 3-source validation, capture any evidence of **severity or frequency** — not just existence. Tag each validated outcome with a preliminary importance signal based on what sources describe.

| Outcome | Importance Signal | Supporting Evidence |
|---------|------------------|-------------------|
| [Outcome statement] | Critical / Common / Minor | [Source quote describing severity, frequency, or impact] |

**Signal definitions:**
- **Critical** — Sources describe this as a major pain point, career risk, or frequent failure mode
- **Common** — Sources describe this as a regular frustration or widely experienced issue
- **Minor** — Sources mention it but don't emphasize severity or frequency

**Purpose:** Seeds Phase 4 proxy scoring with real evidence gathered during validation, rather than requiring a separate research pass. Not every outcome will have a clear signal — tag what the sources provide.

#### Step 3e: Adjacent Outcome Threshold Check

After validating Relevant outcomes, review **Adjacent** outcomes for upgrade potential. Adjacent outcomes that accumulated 2+ sources *incidentally* during Relevant outcome validation may warrant full validation and upgrade.

| Adjacent Outcome | Sources Found Incidentally | Upgrade? | Rationale |
|-----------------|---------------------------|----------|-----------|
| [Outcome statement] | [# and brief description] | Yes / No | [Why upgrade or keep as Adjacent] |

**Rule:** If 2+ sources were found without actively searching for them (they appeared while validating Relevant outcomes), that's a signal this outcome matters more than initially tagged. Upgrade to Relevant and complete the 3-source validation.

**Purpose:** Prevents important outcomes from being parked as Adjacent when the evidence is already there.

### Step 5: Cross-Reference with Problem Domain

For each execution barrier (Phase 1, Tier 2), identify:
- Which job step does this barrier occur at?
- Which outcome statements does it prevent?

For each unmet metric (Phase 1, Tier 3), identify:
- Which outcome statement does it map to?
- What is the importance/satisfaction gap?

**This creates the bridge to Phase 3** — the outcome/unmet metric pairs that drive offering design.

### Step 6: Outcome Completeness Cross-Check

After generating and validating all outcomes, cross-check against the validated sources from Steps 1b and 2b. Do those sources describe pain points or success criteria that aren't captured in any outcome statement?

| Source (from Steps 1b/2b) | Pain Point or Success Criterion Described | Captured in Outcome? | If No — Action |
|---------------------------|------------------------------------------|---------------------|----------------|
| [Source] | [What the source describes] | Yes → [which outcome] / No | Add outcome / Flag as gap / Out of scope with rationale |

**Purpose:** Validation sources often describe the executor's world in richer terms than the analyst's outcome statements capture. This check ensures the outcome set isn't narrower than what the sources reveal.

**Rule:** Not every pain point described in a source needs its own outcome — some will be captured implicitly. But if a source describes a significant pain point that no outcome addresses, either add an outcome or document why it's excluded.

---

## Quality Checks

- [ ] Core job is solution-agnostic and stable over time
- [ ] Core job validated with 3 cited sources (at least 2 source categories)
- [ ] Job is at core functional level (not aspirational or micro)
- [ ] All 8 job map steps are covered
- [ ] Job map validated with 3 cited sources — steps are mutually exclusive and reflect real workflow
- [ ] Each step has 3-8 sub-activities
- [ ] Outcome statements follow strict ODI format
- [ ] Outcome statements within each step are mutually exclusive
- [ ] Cross-step redundancy check completed (no hidden overlaps across steps)
- [ ] 5-15 outcomes per job step
- [ ] No products, features, or solutions mentioned in outcomes
- [ ] Each "Relevant" tag cites a specific Phase 1 root cause with causal link
- [ ] Relevant outcomes validated with 3 external sources each
- [ ] Importance signals captured during validation (Critical / Common / Minor)
- [ ] Adjacent outcomes reviewed for upgrade (2+ incidental sources triggers upgrade)
- [ ] Outcome completeness cross-checked against Steps 1b/2b sources
- [ ] Every Phase 1 barrier maps to a job step
- [ ] Every Phase 1 unmet metric maps to an outcome statement
