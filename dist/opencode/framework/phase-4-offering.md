# Phase 4 — Offering Design (Bottom-Up)

Construct a market offering from the ground up, starting with unmet outcomes and building upward through performance requirements and capabilities. Uses a **diverge-then-converge** structure following design thinking best practices: first expand thinking unconstrained, then select the best path informed by competitive reality.

---

## Input

- Outcome statements with unmet metrics per executor (from Phase 3)
- Stakeholder system map and cross-dependencies (from Phase 2)
- Job executor profiles and hypothesized core jobs (from Phase 2)
- Root cause analysis and execution barriers (from Phase 1)

## Output

- Performance Requirements (Tier 3)
- Capabilities (Tier 2)
- Offering definition (Tier 1)
- Process domain (all 3 tiers)

---

## Process

### Step 1: Prioritize Unmet Outcomes

From the Phase 3 cross-reference, rank outcome/unmet metric pairs. Use quantitative scoring if data is available, or executor-resource-grounded proxy scoring when it's not.

#### When Quantitative Data Is Available (ODI Opportunity Score)

Survey job executors on importance (1-10) and satisfaction (1-10) per outcome. Calculate:

```
Opportunity = Importance + (Importance - Satisfaction)
```

| Score | Interpretation |
|-------|---------------|
| > 15 | Extreme — major unmet need |
| 12-15 | High — strong innovation potential |
| 10-12 | Moderate — worth exploring |
| < 10 | Low — well-served |

#### When Quantitative Data Is NOT Available (Executor-Grounded Proxy Scoring)

Use a severity-based proxy **grounded in executor resources** — not analytical inference alone. Every severity and importance judgment must cite at least one executor-perspective source.

| Outcome Statement | Severity | Executor Evidence | Research Strength | Cross-Ref Density | Proxy Priority |
|-------------------|----------|-------------------|-------------------|-------------------|----------------|
| [Outcome] | Critical / High / Medium / Low | [Source: quote/finding from executor perspective] | Strong (3 sources) / Moderate (2) / Weak (0-1) | # of root causes it maps to | 1-N |

**Severity criteria:**
- **Critical:** Executor cannot complete the job step at all
- **High:** Executor completes but with significant friction/failure rate
- **Medium:** Executor completes but sub-optimally
- **Low:** Minor inconvenience; executor has workable alternatives

**Executor evidence sources** (at least one per outcome):
- Published surveys of the job executor population (e.g., industry salary/satisfaction surveys, professional association research)
- Practitioner forums and communities where executors describe their own pain (Reddit, Glassdoor, professional Slack/Discord, LinkedIn discussions)
- Job descriptions and performance criteria that reveal what executors are measured on
- Industry benchmarks that quantify the friction (e.g., "average time to X is Y hours")
- Interviews, case studies, or testimonials from executors in published sources

**Proxy priority formula:** Rank by severity first (must be executor-evidenced), then break ties by research strength, then by cross-reference density (how many root causes point to this outcome).

**Honesty note:** Proxy scoring is not ODI opportunity scoring. It serves the same prioritization function but is grounded in executor-perspective evidence rather than customer survey data. Flag this in the output. If the offering proceeds to validation, quantitative scoring should replace the proxy.

### Step 2: Define Performance Requirements

For each prioritized outcome, ask: **"What would need to be true for this outcome to be satisfied?"**

**Format:** `Must [achieve what] to [what standard] [under what conditions]`

**Examples:**
- "Must reduce search time to under 2 minutes for datasets over 10,000 records"
- "Must eliminate manual re-entry across systems with 99.9% accuracy"
- "Must provide decision-ready output within the same working session"

**Rules:**
- Each performance requirement maps to exactly one outcome statement
- Requirements are measurable (even if the measure is directional)
- Requirements are solution-agnostic at this stage — describe *what must be true*, not *how*

#### Step 2b: PR Feasibility Flags

Each performance requirement gets a quick feasibility assessment at creation. This prevents the ideation stage from generating ideas for requirements that may not be achievable.

| PR# | Outcome | Performance Requirement | Feasibility | Notes |
|-----|---------|------------------------|-------------|-------|
| PR1 | [Outcome] | [Requirement] | Achievable / Stretch / Uncertain | [Brief rationale] |

**Definitions:**
- **Achievable** — Known methods exist to meet this standard. Low technical risk.
- **Stretch** — Possible but requires significant effort or novel integration. Medium risk.
- **Uncertain** — No clear path to meeting this standard with current methods. High risk. Ideas generated for this PR should be noted as speculative.

**Rule:** Uncertain PRs don't block ideation, but ideas generated against them must carry a "feasibility risk" flag through selection.

---

## STAGE A: DIVERGE — Solution Ideation

**Purpose:** Expand the solution space. Generate maximum creative range without constraining to current market reality, competitive landscape, or structural assumptions. Ideas should be judged only on whether they could satisfy the performance requirement — not on whether someone else is already doing it.

**Mindset:** "What's possible?" not "What exists?"

### Step 3: Solution Ideation (Distribution Approach)

Generate candidate solution approaches for each performance requirement. Use a **bell curve distribution** to ensure creative range without runaway speculation.

**The principle:** For each requirement, generate three ideas — one from the middle of the distribution (conventional/expected), one from each tail (more novel, but within 2 standard deviations of the mean). This prevents both "obvious only" thinking and "science fiction" thinking.

**For each performance requirement, generate:**

| Position | Description | Guideline |
|----------|------------|-----------|
| **Conservative (−1σ)** | The simplest, most proven approach. "What would most people do?" | Uses existing technology, established patterns, minimal change. Low risk, potentially low differentiation. |
| **Expected (mean)** | The reasonable, modern approach. "What would a thoughtful team do?" | Uses current best practices, available tools, moderate integration effort. Balanced risk/reward. |
| **Novel (+1σ to +2σ)** | The creative approach. "What's possible if we rethink assumptions?" | Challenges one or two conventional constraints. Higher risk, potentially higher differentiation. Must still be technically feasible — no magic. |

**Boundary rule:** Ideas must stay within ±2σ of the mean. The mean is "what a competent team with current technology would do." Anything beyond +2σ requires technology or behavior change that can't be assumed. Discard those.

**Output per requirement:**

| PR# | Conservative (−1σ) | Expected (mean) | Novel (+1σ to +2σ) |
|-----|-------------------|-----------------|---------------------|
| PR1 | [Approach] | [Approach] | [Approach] |

#### Step 3b: Ideation Distinctness Check

After generating 3 ideas per PR, verify they use **different mechanisms** — not just different degrees of the same mechanism.

**Test:** Do conservative and novel differ in *kind* (different approach entirely) or just in *degree* (same approach, more/less of it)? If they differ only in degree, add a fourth idea from a genuinely different approach.

| PR# | Conservative Mechanism | Expected Mechanism | Novel Mechanism | Distinct? | 4th Idea Needed? |
|-----|----------------------|-------------------|-----------------|-----------|-----------------|
| PR1 | [Mechanism type] | [Mechanism type] | [Mechanism type] | Yes / No | If No → [4th idea from different mechanism] |

**Example of degree-only difference (bad):**
- Conservative: "Manual review with checklist" / Novel: "Manual review with better checklist" — same mechanism, different intensity.

**Example of kind difference (good):**
- Conservative: "Manual review with checklist" / Novel: "Pattern-matching algorithm flags anomalies" — different mechanism entirely.

**Important:** Do NOT evaluate, rank, or eliminate ideas during this step. The diverge stage is generative only. All ideas carry forward to Stage B.

---

## STAGE B: CONVERGE — Selection and Competitive Positioning

**Purpose:** Contract the solution space. Select the best approach per requirement using three lenses: (1) which serves the executor's unmet needs best, (2) which occupies the least competitive market space, and (3) which composes into a coherent, differentiated offering.

**Mindset:** "What should we build, given what exists and what's needed?"

### Step 4: Competitive Landscape Analysis

Before selecting approaches, map the competitive reality. For the top 5-7 prioritized outcomes, identify existing solutions and assess their coverage.

**4a. Identify competitors:**
Search for existing products, services, tools, and approaches that address the same core job or adjacent jobs for the same executor.

**Minimum coverage requirement:** The competitive landscape must include at least:
- **2 direct product competitors** (tools/platforms built for this executor's job)
- **2 service competitors** (consulting, outsourcing, or managed services addressing the same job)
- **1 adjacent/workaround** (how executors cobble together a solution today — spreadsheets, manual processes, repurposed tools)
- **1 "do nothing" baseline** (what happens if the executor continues with the status quo)

Each competitor must cite a source (product page, industry report, practitioner account).

| # | Competitor / Solution | Type | Source | Description |
|---|----------------------|------|--------|-------------|
| 1 | [Name] | Product / Service / Workaround / Do Nothing | [Source + link] | [What it does] |

**4b. Score competitor coverage per outcome:**

| Outcome | Competitor 1 | Competitor 2 | Competitor 3 | ... |
|---------|-------------|-------------|-------------|-----|
| [Outcome] | Fully / Partially / Unaddressed | ... | ... | ... |

**Coverage definitions (with evidence requirements):**
- **Fully Addressed:** The competitor's core value proposition directly solves this outcome. The executor would say "yes, [product] handles this." **Cite:** product page, documentation, or analyst report confirming this capability.
- **Partially Addressed:** The competitor touches this outcome but incompletely — wrong level, wrong executor, requires workarounds, or is a secondary feature. **Explain:** what's covered and what isn't.
- **Unaddressed:** No existing competitor meaningfully serves this outcome for this executor. **Confirm absence:** searched product page, documentation, and analyst reports — not found. Note what was searched.

**4c. Identify white space:**
Which outcomes are Unaddressed or only Partially Addressed across all competitors? These represent the highest-value differentiation opportunities.

| Outcome | Competitive Coverage | White Space? |
|---------|---------------------|-------------|
| [Outcome] | Fully (2), Partially (1), Unaddressed (0) | No |
| [Outcome] | Partially (1), Unaddressed (2) | **Yes** |

### Step 5: Select Best Approach per Requirement

Now select from the diverge-stage ideas using both executor-need and competitive-positioning criteria:

| Criterion | Weight | Question |
|-----------|--------|----------|
| **Constraint compliance** | Must-have | Does it satisfy all hard constraints identified in Phase 2? (If no → eliminate) |
| **Outcome coverage** | High | How fully does it satisfy the performance requirement? |
| **Competitive white space** | High | Does it address an outcome in a space where competitors are weak or absent? |
| **Combinability** | High | Does it compose well with selected approaches for adjacent requirements? (Solutions that share mechanisms are stronger together) |
| **Feasibility** | Medium | Can it be built/implemented with known methods? |
| **Differentiation** | Medium | Does it address the need in a way current alternatives don't? |

**Selection process:**
1. Eliminate any approach that violates a hard constraint
2. For each requirement, score remaining approaches on the criteria above
3. **Prefer approaches that cluster in competitive white space** — solving well-served outcomes better is harder than solving unserved outcomes first
4. Look across requirements for approaches that share mechanisms — these will cluster naturally into capabilities
5. Default to the Expected approach unless a Novel approach scores higher on differentiation + white space without sacrificing feasibility

**Document the selection:**

| PR# | Selected Approach | Position | Why Selected | Competitive Rationale | Why Others Rejected |
|-----|------------------|----------|-------------|----------------------|-------------------|
| PR1 | [Approach] | Conservative / Expected / Novel | [Rationale] | [Which white space this occupies] | [Brief reason for each rejected] |

#### Step 5b: Post-Selection Stress Test

Before clustering, run the **Assumption Challenger** on the selection table. For each selected approach, ask: "What's the strongest argument for one of the rejected approaches instead?"

| PR# | Selected Approach | Strongest Counter-Argument | Rejected Alternative | Response |
|-----|------------------|---------------------------|---------------------|----------|
| PR1 | [Selected] | [Best case for a rejected approach] | [Which rejected approach] | [Why the selection still holds — or flag if it doesn't] |

**Purpose:** Catches confirmation bias in selection. If the strongest counter-argument is compelling, reconsider before locking in the selection. Better to catch a weak selection here than after clustering.

**Rule:** This is a required step, not optional. Run it before Step 6.

### Step 6: Cluster into Capabilities

Group related performance requirements (with their selected solution approaches) into capabilities.

**Format:** `Ability to [do what] [under what conditions]`

**Clustering criteria:**
- Requirements that address the same job step
- Requirements that share underlying mechanisms
- Requirements that would naturally be delivered together

**Each capability should:**
- Address 2-7 performance requirements
- Map to one or two job steps
- Be describable as a coherent functional ability

### Step 7: Compose the Offering

Assemble capabilities into a coherent market offering. **Default to one offering** unless there's affirmative evidence to split.

#### One Offering or Multiple? (Decision Rule)

**Default: One offering.** Capabilities that share a core job and a primary executor are one offering with multiple capabilities — not multiple micro-offerings.

**Split only when ALL of the following are true:**

| Criterion | Test |
|-----------|------|
| **Different buyers** | The capabilities would be purchased by different budget holders with different decision processes |
| **Different value propositions** | One capability saves money while another reduces risk, and the executor would evaluate them independently |
| **Independent adoption** | One capability is useful without the other (not just "Phase 2" of the same thing) |

**If only 1-2 criteria are met:** It's still one offering, but may have tiers, modules, or a phased rollout. Document this in the offering definition.

**The executor test:** Would the job executor describe these capabilities as "two different things I need" or as "two parts of the same thing I need"? If the latter, it's one offering.

**Offering definition includes:**

| Element | Description |
|---------|-------------|
| **Name** | What it's called |
| **Job Executor** | Who it's for (primary + secondary if multi-executor) |
| **Core Job Addressed** | What job it helps them do |
| **Value Proposition** | Why it's better than current alternatives |
| **Capabilities** | What it can do (list from Step 6) |
| **Key Differentiator** | Which unmet outcomes it uniquely addresses — with competitive white space rationale |
| **Composition** | Single offering / Tiered / Phased — with rationale |

#### Degraded-Mode Design (for Existential Assumptions)

If the Assumption Challenger has flagged any existential assumptions (assumptions that, if false, would make core capabilities impossible), document a degraded-mode offering:

| Element | Full Offering | Degraded Mode (if [assumption] fails) |
|---------|--------------|---------------------------------------|
| **Capabilities removed** | — | [Which capabilities depend on the assumption] |
| **Remaining capabilities** | [All] | [What survives] |
| **Revised value proposition** | [Full value prop] | [What value remains] |
| **Viability assessment** | — | Is the degraded offering still worth building? Yes/No with rationale |

**Purpose:** Ensures the offering isn't all-or-nothing. A reader sees both the full vision and the fallback if the riskiest assumption fails.

### Step 8: Design the Process Domain

Map how the offering actually works:

**Tier 1 — Work Process:**
`[Process name]: [Input] → [Output]`

**Tier 2 — Process Steps:**
For each capability, define the process steps that deliver it:
`[Step number]: [Action] → [Output]`

**Tier 3 — Proof Points (Falsifiable Experiments):**
For each performance requirement, design a **falsifiable experiment** — not just a metric.

**Format:**
```
Experiment: [Specific test methodology]
Sample: [Who/what is tested, sample size, selection method]
Procedure: [Step-by-step test protocol]
Pass criteria: [Specific threshold that constitutes success]
Fail criteria: [What outcome would disprove the capability works]
```

**Examples:**
- "Take 50 historical alerts. Have 3 analysts review them with current tools (measure time). Have 3 analysts review them with auto-assembled investigation briefs (measure time). Pass: second group is 50%+ faster on average."
- "Classify 200 MRO transactions manually by end-use. Run the inference engine on the same 200. Pass: ≥90% agreement with manual classification."
- "Present 20 auto-generated disposition narratives to 5 analysts. Pass: analysts approve or make only minor edits to ≥80% of narratives."

**Rules:**
- Every proof point must be runnable before the full offering is built (prototype-testable)
- Each must have explicit pass AND fail criteria
- Sample sizes must be stated (even if small for early validation)
- The experiment must be designed to disprove the capability, not just confirm it

---

## Validation

### Does the Offering Hold Together?

- [ ] Every capability traces back to specific unmet outcomes
- [ ] Every performance requirement has a feasibility flag (Achievable / Stretch / Uncertain)
- [ ] Ideation produced mechanistically distinct ideas (not just degree variations)
- [ ] Competitive landscape meets minimum coverage (2 product, 2 service, 1 workaround, 1 do-nothing)
- [ ] Each competitor cites a source; each coverage rating is evidence-backed
- [ ] Post-selection stress test completed before clustering
- [ ] Every performance requirement has a falsifiable proof point experiment
- [ ] The offering addresses the core job, not just individual pain points
- [ ] The value proposition is defensible against current alternatives
- [ ] The job executor would recognize this as solving *their* problem
- [ ] Competitive white space is identified and the offering is positioned in it

### "So What?" Test

Before declaring Phase 4 complete, answer three questions. If any answer is weak, the offering needs revision.

| Question | Answer Required |
|----------|----------------|
| **"Would the executor switch from their current approach to this?"** | Name the current approach. Identify the switching cost. Explain why the value exceeds it. If the switching cost is high and the value is incremental, the offering won't get adopted. |
| **"Could someone else build this faster?"** | Name any competitor who is already close. If multiple well-funded competitors already offer 80%+ of this, the offering is a late category entry — acknowledge this and identify what's different, or pivot. |
| **"What's the one thing this offering does that nothing else does?"** | State it in one sentence. If you can't, the offering is a category description, not a product. That's honest and useful — but it means the next step is finding a wedge, not building the whole thing. |

**Output:** Document the three answers explicitly. Weak answers are acceptable — they're honest signals about what the offering still needs. Fake strong answers are not acceptable.

### Does the Data Model Complete?

Verify all 12 cells of the grid are populated:

| Tier | JTBD | Problem | Offering | Process |
|------|------|---------|----------|---------|
| Job | ✓ | ✓ | ✓ | ✓ |
| Step | ✓ | ✓ | ✓ | ✓ |
| Outcome | ✓ | ✓ | ✓ | ✓ |

---

## Anti-Patterns

- **Solution-first:** Designing the offering before understanding the outcomes
- **Capability bloat:** Adding capabilities that don't trace to unmet outcomes
- **Missing the executor:** Building for the buyer instead of the job executor
- **Premature specificity:** Over-specifying the process before validating capabilities
- **Orphan requirements:** Performance requirements that don't connect to an outcome
- **Converging too early:** Eliminating ideas during the diverge stage based on competitive or feasibility concerns
- **Ignoring the landscape:** Designing capabilities without checking if competitors already serve those outcomes
- **Category description:** Arriving at a valid market category rather than a differentiated product — and not acknowledging it

**Note:** After Phase 4 passes its gate, proceed to **Phase 5 — Analysis & Executive Summary** for final synthesis.
