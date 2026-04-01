# Skills Overview

**Status:** `active`  
**Repository:** RepoForge (Public Explanation Layer)  
**Last Updated:** 2026-04-01

---

## What This Document Explains

This is the **public explanation** of the skill-based governance system used across Ewan's repositories.

It explains:
- What skills are and why they matter
- How skills replace traditional "role-based" agent systems
- The four-layer architecture (SpacePort → Forge → workforge → RepoForge)
- Why this approach scales better than document-heavy systems

---

## The Problem with Traditional Agent Systems

Most AI assistant systems organize around:
- **Roles** ("you are a researcher", "you are a writer")
- **Documents** ("read these 50 pages to understand how to work")
- **Ad-hoc instructions** ("here's what I need for this task")

This creates three problems:

### 1. Roles Don't Capture Judgment Patterns

Saying "act as a research assistant" doesn't tell the agent:
- How Ewan decides which works belong to which practice line
- How Ewan writes about perceptual migration vs. technical documentation
- When Ewan chooses to collaborate deeply vs. contribute partially
- What Ewan considers publish-safe vs. private

**Roles describe function. Skills encode judgment.**

### 2. Documents Don't Scale

As repositories grow:
- New agents must read dozens of files to understand operations
- Contradictions emerge between old and new documents
- Agents "figure things out from context" inconsistently
- Knowledge lives in heads, not in executable form

**Documents require interpretation. Skills execute directly.**

### 3. Ad-hoc Instructions Create Inconsistency

Without encoded skills:
- Similar tasks get handled differently each time
- Quality depends on how well the human briefs each time
- Learning doesn't compound—every agent starts fresh
- Handoff requires extensive explanation

**Ad-hoc work resets every time. Skills accumulate intelligence.**

---

## What Is a Skill?

A **skill** is a self-contained, executable unit that encodes:
- **Purpose**: What problem it solves
- **Judgment rules**: How to make decisions the way Ewan would
- **Input requirements**: What materials it needs
- **Output format**: What it produces, consistently
- **Failure modes**: Common errors to avoid
- **Escalation triggers**: When to ask for human judgment

### Example: `artist-practice-cartographer`

Instead of telling an agent:
> "Look at my works and figure out how they relate to my practice lines..."

The skill encodes:
```
Purpose: Map works to practice lines (time structures / spatial generation / perceptual migration)
Source of Truth: portfolio/README.md + selected works + research notes
Operating Rules:
  - Check if work engages with temporal sequencing → time structures
  - Check if work creates environmental interfaces → spatial generation
  - Check if work translates states across mediums → perceptual migration
  - A work can belong to multiple lines; note primary and secondary
Output: practice note with work placement reasoning
```

**The skill doesn't just do the task—it does it the way Ewan judges.**

---

## The Four-Layer Architecture

```
┌─────────────────────────────────────────────────────────┐
│  SpacePort (Source Layer)                               │
│  Research Laboratory → Skill Mother Templates           │
│  Public, reusable, generalizable skills                 │
└─────────────────────────────────────────────────────────┘
                          ↓ installs to
┌─────────────────────────────────────────────────────────┐
│  Forge (Personal Installed Layer)                       │
│  Ewan's Cognition + Persona Skills                      │
│  Simulates how Ewan thinks, writes, judges, creates     │
└─────────────────────────────────────────────────────────┘
                          ↓ executes in
┌─────────────────────────────────────────────────────────┐
│  workforge (Work Execution Layer)                       │
│  Client Ops, Delivery, Business Workflows               │
│  Professional skills for client-facing work             │
└─────────────────────────────────────────────────────────┘
                          ↓ explained by
┌─────────────────────────────────────────────────────────┐
│  RepoForge (Public Explanation Layer)                   │
│  Shows skill-based governance publicly                  │
│  Demonstrates repo management + skills relationship     │
└─────────────────────────────────────────────────────────┘
```

### Layer Responsibilities

| Layer | Purpose | Skills Type | Privacy |
|-------|---------|-------------|---------|
| **SpacePort** | Source of truth for skill templates | Research-derived, generalizable | Public |
| **Forge** | Personal cognition simulation | Persona + personal ops | Private |
| **workforge** | Professional execution | Client + delivery + business | Private |
| **RepoForge** | Public explanation | Governance model only | Public |

---

## Skills vs. Documents: The Key Shift

### Old Model (Document-First)
```
Agent enters repository
  → Reads README.md
  → Reads docs/AGENT_ROLES.md
  → Reads docs/SYSTEM_GUIDE.md
  → Reads memory/, projects/, clients/
  → Tries to synthesize understanding
  → Makes judgment calls based on interpretation
```

**Problems:**
- Every agent interprets differently
- Contradictions between documents create confusion
- Learning doesn't compound
- Handoff requires re-explanation

### New Model (Skill-First)
```
Agent enters repository
  → Reads skills/README.md
  → Checks skills/registry.md for relevant skills
  → Executes skill with defined judgment rules
  → References docs/ as supporting materials only
```

**Benefits:**
- Consistent execution across agents
- Judgment encoded, not interpreted
- Learning compounds in skills
- Handoff is automatic (skills are the handoff)

---

## Why This Matters for Creative Practice

Creative work involves **judgment**, not just **tasks**:

| Task-Based | Judgment-Based |
|------------|----------------|
| "Write an artist statement" | "Write an artist statement the way Ewan writes—perceptual, spatial, avoiding art-speak" |
| "Organize my projects" | "Organize projects according to Ewan's practice lines, noting overlaps and evolutions" |
| "Prepare a proposal" | "Prepare a proposal that reflects Ewan's positioning—collaborative but bounded, experimental but deliverable" |

**Skills capture the difference between "do this" and "do this the way Ewan would."**

---

## Public vs. Private Skills

Not all skills are public. The system respects boundaries:

### Public (SpacePort, RepoForge)
- Generalizable methods
- Research-derived patterns
- Governance explanations
- Reusable templates

### Private (Forge, workforge)
- Personal judgment patterns
- Client-specific workflows
- Pricing and business logic
- Collaboration positioning

**RepoForge shows the model without exposing private skills.**

---

## For Developers Reading This

If you're considering implementing a similar system:

### Start Small
1. Identify **one repetitive judgment** you make
2. Write it as a skill with clear rules
3. Test it across different agents/tasks
4. Refine based on failures

### Don't Over-Engineer
- Skills don't need to be code (they can be structured markdown)
- Start with 3-5 core skills, not 50
- Let skills evolve from actual work, not abstract design

### Keep Documents, Just Demote Them
- Documents become **supporting materials** for skills
- They're still valuable, just not the primary abstraction
- Think: "docs support skills" not "skills support docs"

---

## Further Reading

- [FORGE_VS_WORKFORGE_VS_REPOFORGE.md](FORGE_VS_WORKFORGE_VS_REPOFORGE.md) — Detailed layer boundaries
- [PUBLIC_SKILL_MODEL.md](PUBLIC_SKILL_MODEL.md) — What's safe to show publicly
- VIRTURA-Forge/skills/registry.md — Example personal skill registry (private, referenced here for structure)

---

**Maintenance:** Update this document when the skill model evolves  
**Audience:** Public (collaborators, peers, potential contributors)
