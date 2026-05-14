# Phase 5 — Analysis & Executive Summary

Synthesize the full pipeline output into a decision-ready document. Provides executive overview, validated chain of logic, deep offering description, and concrete next steps.

---

## Why This Phase Exists

Phases 1-4 produce rigorous, detailed artifacts — but no single artifact tells the whole story. Phase 5 exists to give a reader who has NOT seen the phase outputs everything they need to understand the problem, the offering, and the path forward — in one document.

Without this phase, you risk:
- Decision-makers reading Phase 4 without understanding Phase 1's root causes
- The logical chain from problem → executor → job → offering being implicit rather than explicit
- Validation gaps being hidden in phase-level detail
- No clear "what do we do next?" after the analysis is complete

---

## Input

- All phase outputs (Phases 1-4)
- Sub-agent outputs (Assumption Challenger, Cross-Reference Mapper, etc.)
- Data model completeness (12-cell grid status)

## Output

- Executive summary document (`executive-summary.md` in the run folder)
- Chain-of-logic narrative connecting all phases
- Deep offering description with evidence trail
- Prioritized next steps with validation experiments

---

## Process

### Step 1: Executive Overview

A 3-5 paragraph narrative that orients the reader. Covers: what problem was analyzed, what was found, and what's being proposed.

**Rules:**
- Lead with the problem, not the solution
- Write for someone who has zero context — no assumptions about prior knowledge
- State the core finding in one sentence before elaborating
- Use evidence from the phase outputs — don't introduce new claims

### Step 2: Chain of Logic

The backbone of Phase 5. Walk the reader through the logical chain that connects the problem to the offering, making every link explicit and evidence-backed.

**Structure:**

```
Problem Statement (Phase 1)
  ↓ validated by [3 cited sources]
Root Causes (Phase 1, 5 Whys terminal nodes)
  ↓ each cited with [structural evidence]
Stakeholder System (Phase 2)
  ↓ validated by [stakeholder completeness sources]
Job Executors Selected (Phase 2)
  ↓ grounded in [Phase 1 evidence for proximity/leverage]
Core Job (Phase 3)
  ↓ validated by [3 cited sources]
Job Map → Outcome Statements (Phase 3)
  ↓ validated by [3 sources per Relevant outcome]
  ↓ importance signals captured [Critical / Common / Minor]
Prioritized Unmet Outcomes (Phase 4)
  ↓ scored by [proxy or ODI methodology]
Performance Requirements → Selected Approaches (Phase 4)
  ↓ stress-tested against [rejected alternatives]
Capabilities → Offering (Phase 4)
  ↓ positioned against [competitive landscape]
```

**For each link, document:**

| Link | From | To | Evidence | Confidence |
|------|------|----|----------|------------|
| 1 | Problem statement | Root causes | [Phase 1 citations] | High / Medium / Low |
| 2 | Root causes | Executor selection | [Phase 2 evidence grounding] | High / Medium / Low |
| ... | ... | ... | ... | ... |

**Rules:**
- Every link must cite specific evidence from the phase outputs
- If a link has low confidence, say so — don't paper over weak connections
- Flag any link where the evidence is "analytical inference only" (no external citation)
- The chain should be readable as a standalone argument: "Because [A], therefore [B], therefore [C]..."

### Step 3: Deep Offering Description

Go beyond the Phase 4 offering definition to describe the offering in plain language, organized for a reader who needs to understand what it does and why it matters.

**Structure:**

| Section | Content |
|---------|---------|
| **What It Is** | Name + one-sentence description. No jargon. |
| **Who It's For** | Executor defined functionally (from Phase 2) with possible titles. Why this executor, not others. |
| **What It Does** | Capabilities organized by logical layers (not just listed). For each capability: what it enables the executor to do that they can't do today. |
| **How It's Different** | Competitive positioning: name the closest competitors, state what they do and don't do, explain the structural white space this offering occupies. |
| **What Must Be True** | The existential assumptions. If these are false, the offering fails or degrades. Include the degraded-mode design. |
| **Evidence Trail** | For each capability, trace backward: Capability ← Performance Requirements ← Unmet Outcomes ← Root Causes. Show the chain. |

**Rules:**
- Name competitors — don't speak generically about "existing solutions"
- For each claim about differentiation, cite the competitive coverage analysis from Phase 4
- Include the degraded-mode design — readers need to see both the full vision and the fallback

### Step 4: Validation & Next Steps

Translate the proof points from Phase 4 Step 8 into a prioritized action plan.

**4a. Validation Plan:**

| Priority | Experiment | Tests Which Assumption | Pass Criteria | Fail Criteria | Effort |
|----------|-----------|----------------------|---------------|---------------|--------|
| 1 | [From Phase 4 proof points] | [Which existential or high-risk assumption] | [Specific threshold] | [What disproves it] | Low / Medium / High |

**Prioritize by:**
1. Existential assumptions first (if false, offering fails)
2. High-severity assumptions next (if false, offering degrades significantly)
3. Feasibility-uncertain PRs next (from Phase 4 Step 2b flags)

**4b. Recommended Next Steps:**

A sequenced action plan — what to do first, second, third. Each step should be concrete enough that someone could act on it.

| # | Action | Purpose | Depends On | Timeline Signal |
|---|--------|---------|-----------|----------------|
| 1 | [Action] | [What this validates or enables] | [Prerequisites] | First / Soon / Later |

**Rules:**
- "Do more research" is not a next step. Name what research, on what question, using what method.
- Each action should have a clear purpose tied to a specific gap or assumption
- Sequence matters — don't present a flat list when some actions must precede others

### Step 5: Data Model Completeness

Verify and display the 12-cell grid:

| Tier | JTBD | Problem | Offering | Process |
|------|------|---------|----------|---------|
| Job | [What populates this cell] | [What populates this cell] | [What populates this cell] | [What populates this cell] |
| Step | [What populates this cell] | [What populates this cell] | [What populates this cell] | [What populates this cell] |
| Outcome | [What populates this cell] | [What populates this cell] | [What populates this cell] | [What populates this cell] |

**Check for:**
- Orphans (cells with no content or weak content)
- Cross-reference gaps (horizontal links missing between domains at the same tier)
- Vertical gaps (tier 3 items that don't trace up to tier 1)

### Step 6: Honest Limitations

Document what this analysis does NOT include, what remains unverified, and where the evidence is weakest.

| Category | What's Missing or Weak | Impact | Recommendation |
|----------|----------------------|--------|----------------|
| **Scope exclusions** | [What was intentionally excluded] | [How this limits conclusions] | [Whether to address later] |
| **Unvalidated assumptions** | [Assumptions that couldn't be cited] | [What breaks if they're wrong] | [How to validate] |
| **Evidence gaps** | [Where sources were thin or absent] | [Which conclusions are weakest] | [What research would strengthen them] |
| **Methodology limits** | [Where proxy scoring, analytical inference, or single-source claims were used] | [How confident we should be] | [What would improve confidence] |

### Step 7: Net Assessment

3-5 sentences answering three questions:
1. **Is this defensible?** — Does the evidence chain hold up? Where is it strongest and weakest?
2. **What's the core risk?** — The single biggest thing that could make this offering fail.
3. **What's the recommended next action?** — One concrete thing to do first.

**Rules:**
- Weak positions must be acknowledged, not hidden
- The net assessment is a judgment, not a summary — take a position
- If the honest answer is "this isn't strong enough to proceed," say so

---

## Decision Gate

Before declaring the analysis complete:

- [ ] Chain of logic is explicit and every link cites evidence
- [ ] Offering description is understandable without reading phase outputs
- [ ] Competitors are named (not generic)
- [ ] Existential assumptions are identified with falsifiable experiments
- [ ] Degraded-mode design is included
- [ ] Data model grid is complete (12 cells populated)
- [ ] Limitations are honestly documented
- [ ] Net assessment takes a position
- [ ] Next steps are sequenced and concrete
- [ ] Document is readable by someone with zero prior context

---

## Anti-Patterns

### The Summary Trap
Summarizing each phase sequentially instead of synthesizing across them. Phase 5 is not "Phase 1 said X, Phase 2 said Y." It's "Because X (Phase 1), we identified Y (Phase 2), which means Z (Phase 3), so we should build W (Phase 4)."

### The Confidence Inflation
Making the analysis sound more certain than it is. If proxy scores were used instead of ODI surveys, say so. If a root cause has one source instead of three, flag it.

### The Missing "So What?"
Describing the offering without explaining why anyone should care. Every capability should connect backward to a pain point the executor recognizes.

### The Flat Next Steps
Listing actions without sequencing or prioritization. "Validate assumption A" and "build prototype" are not equal — one must come first.

---

## Output

**File:** `executive-summary.md` in the run folder

**Target length:** 2-4 pages (roughly 1500-3000 words). Long enough to be complete, short enough to be read.

**Audience:** A decision-maker or stakeholder who needs to understand the analysis, evaluate its strength, and decide whether to invest in the next step. They have not read the phase outputs.
