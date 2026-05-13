---
name: five-whys
description: Use this skill for structured root-cause analysis. Operationalizes the 5 Whys technique with branching, evidence requirements, and stopping rules.
---

# Skill: 5 Whys Root-Cause Analysis

How to systematically trace a problem to its root cause through iterative causal questioning.

---

## Core Principle

**Every symptom has a cause. Follow the causal chain until you reach something you can't decompose further — that's your root cause.**

5 Whys isn't "ask why 5 times." It's a disciplined causal chain where each link must be supported by evidence or logic, and branches are followed independently.

---

## When to Use

Use 5 Whys when:
- You have a clear symptom or failure and need to find the root cause
- A problem keeps recurring despite fixes (you're treating symptoms)
- You need a fast root-cause method (faster than full first-principles decomposition)
- You want to map the causal structure of a problem for downstream analysis

Do NOT use when:
- The problem is poorly defined (use first-principles decomposition first to clarify)
- The cause is already known and the question is about solutions
- The problem is systemic with 10+ interacting causes (use systems mapping instead)

---

## The Process

### Step 1: State the Observable Problem

Write the problem as a specific, observable event or condition — not an interpretation.

**Good:** "Customer support tickets increased 40% in January"
**Bad:** "Customer support is overwhelmed" (interpretation)

**Rule:** Someone with no context should be able to verify whether this is happening.

### Step 2: Ask "Why?" — Level 1

Ask: **"Why does [observable problem] occur?"**

**Rules for each "why" answer:**
- Must be a **cause**, not a restatement of the problem
- Must be **verifiable** — you can point to evidence or logic
- Must be **specific** — not "because things are bad"

**If multiple causes exist:** Branch. Create parallel chains. Label them 1a, 1b, etc.

### Step 3: Continue Down Each Branch

For each answer, ask "Why does [that] happen?" Repeat.

**Document as a tree:**

```
Why 1: [Problem]
├── Why 2a: [Cause A]
│   ├── Why 3a: [Deeper cause]
│   │   └── Why 4a: [Root cause] ← STOP: structural constraint
│   └── Why 3b: [Deeper cause]
│       └── Why 4b: [Root cause] ← STOP: can't decompose
└── Why 2b: [Cause B]
    └── Why 3c: [Deeper cause]
        └── Why 4c: [Root cause] ← STOP: external constraint
```

### Step 4: Apply Stopping Rules

Stop a branch when you reach any of these:

| Stopping Condition | Example |
|-------------------|---------|
| **Structural constraint** | "Because human attention is limited" — can't change human cognition |
| **External constraint** | "Because the regulation requires it" — outside your control |
| **Organizational bedrock** | "Because leadership decided X" — a decision, not a cause |
| **Circular reference** | The answer points back to an earlier link — you've found a reinforcing loop |
| **No further decomposition** | You can't meaningfully ask "why" again — you've hit bottom |

**The "5" is a guideline, not a law.** Some chains resolve in 3. Some need 7. Follow the logic, not the count.

### Step 5: Classify Root Causes

For each terminal node (root cause), classify:

| Root Cause | Type | Actionability |
|-----------|------|---------------|
| [Cause] | Structural / Behavioral / Process / Knowledge / Resource | Within control / Influenceable / External |

**Types:**
- **Structural:** Built into the system architecture — requires redesign
- **Behavioral:** Human habits or incentives — requires motivation change
- **Process:** Missing or broken procedures — requires process change
- **Knowledge:** Information gaps — requires training or information access
- **Resource:** Insufficient capacity — requires investment

### Step 6: Select the Leverage Point

Not all root causes are equal. Identify which one, if addressed, would have the largest cascading effect on the problem.

**Criteria:**
- Appears in multiple branches (affects many symptoms)
- Is within your sphere of control
- Addressing it doesn't create new problems
- Has the highest ratio of impact-to-effort

---

## Techniques

### The Evidence Gate
At each level, demand: "How do we know this is true?" If the answer is "we assume" or "everyone says," flag it. Unverified links weaken the entire chain.

### Branch Prioritization
When you get 3+ branches at a level, quickly rank by:
1. **Frequency** — which cause occurs most often?
2. **Impact** — which cause has the biggest effect?
3. **Tractability** — which cause can we actually address?

Follow the highest-priority branch first.

### The Counterfactual Test
At each level, ask: "If [this cause] were removed, would the problem still exist?"
- If **yes**: this isn't the only cause — look for other branches
- If **no**: this is a necessary cause — keep following it

### Loop Detection
If a "why" answer resembles something earlier in the chain, you've found a **reinforcing loop**. Document it explicitly:

```
A causes B → B causes C → C reinforces A
```

Loops are important findings — they explain why problems persist despite interventions.

---

## Anti-Patterns

### The Blame Chain
Each "why" points to a person: "Because John didn't do X" → "Because John wasn't trained" → "Because John's manager didn't prioritize it."

**Fix:** Focus on systems, not individuals. Replace "John didn't" with "The process/system doesn't ensure that..."

### The Single Thread
Only following one branch when multiple causes exist.

**Fix:** Always check for multiple causes at each level. Ask "Is there another reason?" before moving deeper.

### The Premature Stop
Stopping at a convenient cause rather than a root cause. "Because we don't have enough budget" is often a premature stop — why isn't budget allocated?

**Fix:** Apply the stopping rules explicitly. If you can still ask "why" and get a meaningful answer, you haven't hit root.

### The Solution Masquerading as a Cause
"Because we don't have [specific tool/process]" — this is a solution, not a cause.

**Fix:** Reframe: "Because [the thing the tool would address] isn't happening." Stay in problem space.

### The Assumption Chain
Each "why" builds on the previous without evidence, creating a plausible but unverified story.

**Fix:** Apply the evidence gate at every level. Mark unverified links explicitly.

---

## Example: Full 5 Whys Analysis

**Observable Problem:** "Project deliverables are consistently 2-3 weeks late"

```
Why 1: Why are deliverables late?
├── 1a: Scope changes mid-project
│   ├── Why 2a: Requirements aren't locked before work begins
│   │   ├── Why 3a: Stakeholders aren't aligned on requirements
│   │   │   └── Why 4a: No structured requirement gathering process exists
│   │   │       └── ROOT: Process gap — no requirements framework
│   │   └── Why 3b: "Requirements" are really preferences, which shift as stakeholders see progress
│   │       └── ROOT: Structural — requirements emerge through iteration, not upfront
│   └── 1b: Client requests additions after seeing progress
│       └── Why 2b: No change control process
│           └── ROOT: Process gap — no scope management
└── 1c: Task estimates are consistently too low
    ├── Why 2c: Hidden dependencies aren't discovered until execution
    │   └── Why 3c: No dependency mapping in planning
    │       └── ROOT: Process gap — incomplete planning method
    └── Why 2d: Estimators don't account for integration/review time
        └── Why 3d: Estimates only include "build" time by convention
            └── ROOT: Knowledge gap — estimation mental model is incomplete
```

**Root Causes Classified:**

| Root Cause | Type | Actionability | Leverage |
|-----------|------|---------------|----------|
| No requirements framework | Process | Within control | High — affects 2 branches |
| Requirements emerge through iteration | Structural | Influenceable | Medium — can design for it |
| No scope management | Process | Within control | Medium — single branch |
| Incomplete planning method | Process | Within control | Medium — single branch |
| Estimation mental model incomplete | Knowledge | Within control | Low — single branch |

**Leverage Point:** "No requirements framework" — appears across multiple branches and is fully within control. But note the structural finding: if requirements *inherently* emerge through iteration, the framework must account for that rather than trying to eliminate it.

---

## Quick Reference

### Process
1. **State** — Observable, verifiable problem
2. **Ask Why** — Branch when multiple causes exist
3. **Continue** — Follow each branch to termination
4. **Stop** — Structural constraint / external constraint / circular / no further decomposition
5. **Classify** — Type (structural/behavioral/process/knowledge/resource) + actionability
6. **Leverage** — Which root cause has the highest cascading impact?

### Stopping Rules
- Structural constraint (physics, cognition, economics)
- External constraint (regulation, policy you can't change)
- Organizational bedrock (deliberate leadership decision)
- Circular reference (reinforcing loop — document it)
- No further decomposition possible

### Tests
- **Evidence Gate:** How do we know this is true?
- **Counterfactual:** If removed, would the problem still exist?
- **Loop Detection:** Does this point back to an earlier link?

### Output Format
```
[Observable Problem]
├── Why: [Cause] (evidence: [X])
│   └── Why: [Deeper cause] (evidence: [X])
│       └── ROOT: [Type] — [Description]
```
