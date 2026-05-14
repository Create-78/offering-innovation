---
name: first-principles-decomposition
description: Use this skill when you need to break a problem down to its irreducible elements. Operationalizes first principles thinking into specific, repeatable decomposition moves.
---

# Skill: First Principles Decomposition

How to systematically strip a problem to its fundamental truths and rebuild understanding from the ground up.

---

## Core Principle

**A problem is a bundle of claims. Decompose the claims, challenge each one independently, and only keep what survives.**

First principles thinking isn't "think harder" — it's a specific set of moves that separate inherited assumptions from structural truths.

---

## When to Use

Use first principles decomposition when:
- A problem statement contains embedded assumptions you haven't verified
- You're working from a second-hand framing (someone told you the problem)
- Current solutions aren't working and you suspect the problem is mis-defined
- You need to find the *irreducible core* before applying any framework (like ODI)

Do NOT use when:
- The problem is well-defined and the question is about execution
- You're optimizing within a known solution space
- Time pressure requires action over analysis (use 5 Whys for faster root-cause)

---

## The Five Decomposition Moves

These are the operational steps. Apply them in sequence to any problem statement.

### Move 1: Parse the Claim

Break the problem statement into its atomic components.

**Method:** Identify every distinct claim, actor, action, object, and constraint in the statement.

**Example:**
> "Enterprise sales teams waste too much time on unqualified leads"

| Component | Type | Value |
|-----------|------|-------|
| Enterprise sales teams | Actor | Who experiences this |
| waste | Judgment | Assumes the time is non-productive |
| too much time | Measure + threshold | How much is "too much"? |
| unqualified leads | Object + judgment | What makes a lead "unqualified"? |

**Output:** A table of components, each tagged as fact, assumption, or judgment.

### Move 2: Challenge Each Component

For every assumption or judgment, ask: **"Is this necessarily true, or is this a convention?"**

| Component | Challenge | Result |
|-----------|-----------|--------|
| "waste" | Is the time truly non-productive, or does it produce learning/relationships? | Assumption — needs evidence |
| "too much" | Relative to what benchmark? Industry average? Competitor? Internal target? | Undefined threshold |
| "unqualified" | By whose criteria? At what point in time? Leads can become qualified. | Definition-dependent |

**Output:** Each component classified as **Structural truth** (can't be otherwise), **Testable claim** (could be verified), or **Assumption** (taken on faith).

### Move 3: Identify the Substrate

Strip away all assumptions and judgments. What remains?

**Method:** Restate the problem using only structural truths and testable claims.

**Example:**
> Original: "Enterprise sales teams waste too much time on unqualified leads"
> Substrate: "Sales teams allocate time to leads. Some leads do not convert. The ratio of time-to-conversion varies."

The substrate is boring. That's the point. It's the irreducible reality before anyone applied a narrative.

### Move 4: Reconstruct with Evidence

From the substrate, rebuild toward the problem — but only add claims you can support.

**Method:** For each element you want to add back, state what evidence would validate it.

| Claim to Add Back | Evidence Required | Available? |
|-------------------|-------------------|------------|
| "Too much time" → conversion ratio is below target | Benchmark data, historical conversion rates | Check |
| "Unqualified" → specific criteria exist and are applied consistently | Lead scoring model, win/loss analysis | Check |
| "Waste" → time on non-converting leads has no secondary value | Analysis of relationship/learning outcomes from lost deals | Check |

**Output:** A reconstructed problem statement where every element is evidence-backed or explicitly flagged as unvalidated.

### Move 5: State the Atomic Problem

Write the final decomposed problem in the form:

```
[Actor] experiences [specific friction] when [doing what]
because [structural cause — not assumption].
```

**Rules:**
- Every noun and verb must be concrete
- No embedded judgments (no "waste," "too much," "poor")
- The "because" clause points to a structural or systemic cause, not a symptom

---

## Techniques

### The Inversion Test
State the opposite of each assumption. If the opposite is also plausible, the assumption isn't a principle — it's a choice.

> "Leads are unqualified" → "Leads are qualified but we lack the information to recognize it"
> Both are plausible → "unqualified" is a framing choice, not a truth.

### The Time Travel Test
Would this problem exist 50 years ago? 50 years from now? If the problem is solution-dependent, you're looking at a symptom, not a fundamental.

### The Empty Room Test
If you put the actor in an empty room with only the raw inputs, what would they actually need? Remove all tools, processes, and norms. What's irreducible?

### The "Says Who?" Test
For every claim, ask who originally stated it and what their incentive was. Problems framed by vendors differ from problems framed by users.

---

## Anti-Patterns

### The Infinite Regress
Decomposing forever without reaching a useful stopping point.

**Fix:** Stop when you hit a *structural constraint* — something imposed by physics, economics, law, or human cognition that can't be designed away. "People have limited attention" is a principle. "People don't read emails" is a symptom.

### The Obvious Substrate
Stripping the problem to something so generic it's useless ("People do things. Sometimes things go wrong.").

**Fix:** The substrate should be *specific enough to act on*. If you can't derive next steps from it, you've gone too far.

### Assumption Laundering
Sneaking assumptions back in during the reconstruction step without evidence.

**Fix:** The evidence column must be filled for every claim added back. "Everyone knows" is not evidence.

### Solo Decomposition
Doing this alone and trusting your own judgment about what's "structural."

**Fix:** Have someone else challenge your Move 2 classifications. Your blind spots are invisible to you by definition.

---

## Example: Full Decomposition

**Input:** "Our onboarding process is too slow and new hires feel lost"

**Move 1 — Parse:**
| Component | Type |
|-----------|------|
| Our onboarding process | Object (specific to this org) |
| too slow | Judgment (relative to what?) |
| new hires | Actor |
| feel lost | Emotional state (self-reported? observed?) |

**Move 2 — Challenge:**
- "Too slow" → compared to what? Industry benchmark? New hire expectation? Productivity target?
- "Feel lost" → is this measured? Universal or specific roles? At what point in onboarding?
- "Our process" → is the process the cause, or is it the information, the people, or the tools?

**Move 3 — Substrate:**
> New hires enter the organization. They need information, relationships, and skills to perform their role. There is a time gap between joining and performing independently.

**Move 4 — Reconstruct:**
| Claim | Evidence |
|-------|----------|
| Time gap exceeds target | 90th-day productivity metric vs. benchmark |
| Information gap is primary cause | Survey data: "I didn't know where to find X" |
| Relationship gap contributes | Attrition data correlates with mentor assignment |

**Move 5 — Atomic Problem:**
> New hires at [org] take [X days] longer than target to reach independent performance because they lack structured access to role-specific information and relationships during their first 30 days.

---

## Quick Reference

### The Five Moves
1. **Parse** — Break statement into components (actor, action, object, constraint, judgment)
2. **Challenge** — Classify each as structural truth, testable claim, or assumption
3. **Substrate** — Strip to only structural truths
4. **Reconstruct** — Add back only what evidence supports
5. **Atomic Statement** — Restate as `[Actor] experiences [friction] when [doing what] because [structural cause]`

### Tests
- **Inversion:** Is the opposite also plausible? → It's an assumption, not a principle
- **Time Travel:** Would this exist in 50 years? → If not, it's solution-dependent
- **Empty Room:** What's irreducible? → That's your substrate
- **Says Who?** → Source shapes framing

### Stopping Rule
Stop decomposing when you hit something imposed by physics, economics, law, or cognition.
