# Public Skill Model

**Status:** `active`  
**Repository:** RepoForge (Public Explanation Layer)  
**Last Updated:** 2026-04-01

---

## What Is Public About the Skill Model?

This document explains the **public-facing parts** of the skill-based governance model. It doesn't expose private skills, but it explains how the model works in public terms.

---

## Core Premise

Most AI-assisted creative work today relies on:
- **Ad-hoc prompting** — Every task gets a new explanation
- **Large document RAG** — Agents read dozens of pages to "figure it out"
- **Role-based instructions** — "You are a writer, you are a researcher"

This creates inconsistency:
- Different agents interpret the same instructions differently
- Judgment patterns don't compound—every new agent starts fresh
- Weak models struggle with open-ended interpretation

The **skill model** solves this by encoding judgment into **executable, self-contained units**.

---

## What Is a Skill?

A **skill** is a self-contained unit that encodes:

| Field | Purpose |
|-------|---------|
| **Purpose** | What problem does this skill solve? |
| **Best For** | What tasks is this skill good for? |
| **Not For** | What should this skill *not* be used for? (sets clear boundaries) |
| **Inputs** | What materials does the skill need to work? |
| **Source of Truth** | Which repositories/pages/docs should the skill trust? |
| **Operating Rules** | Judgment rules that must be followed. This is where "how Ewan thinks" gets encoded. |
| **Output Format** | What structure should the output follow? (consistency) |
| **Failure Modes** | What are the most common errors to avoid? |
| **Escalation** | When should the skill stop and ask for human judgment? |

## Why This Structure?

This structure is intentionally **strict** because:

1. **Weak models can execute it reliably** — Less open-ended interpretation needed
2. **Consistent output across agents** — Same input → similar output
3. **Clear boundaries** — Agents know when to escalate rather than guess
4. **Maintainable** — Rules can be updated when judgment changes
5. **Handoff-ready** — New agents can pick up where others left off

---

## Skill Classification by Layer

Skills live in different repositories depending on their purpose:

### 1. Source Skills (VIRTURA-SpacePort)

**Location:** `VIRTURA-SpacePort/stations/skill-forge/skills/`  
**Purpose:** Generalizable, research-derived skill templates that can be shared and reused.

**Example categories:**
- `repo-ops` — Repository maintenance, git operations, documentation
- `content-creation` — Writing, editing, summarizing
- `data-processing` — Cleaning, organizing, analyzing data
- `project-management` — Planning, tracking, checkpoints

**Privacy:** Public

### 2. Personal Skills (Forge)

**Location:** `Forge/skills/`  
**Purpose:** Encode personal judgment patterns. These skills simulate how the repository owner thinks, writes, and creates.

**Example categories:**
- `persona` — Simulate creative judgment (mapping works to practice lines, writing artist statements, structuring live visuals)
- `personal-ops` — Maintain personal knowledge system (portfolio navigation, project normalization, public/private boundary checking)

**Privacy:** Private — These encode personal patterns that don't need to be public

### 3. Work Skills (workforge)

**Location:** `workforge/skills/`  
**Purpose:** Execute professional work. These skills handle client-facing tasks, delivery, and business operations.

**Example categories:**
- `client-ops` — Client onboarding, proposals, follow-ups
- `delivery` — Project checkpoints, quality control, delivery packaging
- `business-ops` — Pricing, contracts, invoicing

**Privacy:** Private — Contains client data and business logic

### 4. Public Explanation (RepoForge)

**Location:** `RepoForge/docs/`  
**Purpose:** Explain the model publicly without exposing private skills.

**What's public:**
- The *structure* of the model
- The *why* behind skills-based governance
- *Sanitized examples* of how skills work
- Boundaries between layers

**Privacy:** Public

---

## How Skills Get Installed

The typical installation flow:

```
1. Research & develop skill template in SpacePort
   ↓
2. Install to Forge (personal) or workforge (work)
   ↓
3. Customize operating rules for personal use
   ↓
4. Add to skills/registry.md
   ↓
5. Agent can now execute the skill
```

---

## How Agents Execute Skills

When an agent needs to do a task:

**Old Way (Document-First)**
1. Read README → Read AGENT_ROLES → Read SYSTEM_GUIDE → Read dozens of docs
2. Try to synthesize understanding
3. Make judgment calls based on interpretation
4. Results vary based on agent strength and interpretation

**New Way (Skill-First)**
1. Read `skills/README.md`
2. Check `skills/registry.md` for relevant skill
3. Open the skill's `SKILL.md` and follow the structure
4. Execute following the explicit operating rules
5. Reference documents only as supporting materials
6. Output in the required format
7. Escalate if triggers are met

**Key Difference:** Judgment is *encoded* in the skill, not *interpreted* from documents.

---

## The Four-Layer Public Model

```
┌─────────────────────────────────────────────────────────┐
│  VIRTURA-SpacePort                                       │
│  (Source Layer - Public)                                 │
│  Research laboratory for skill templates                 │
└─────────────────────────────────────────────────────────┘
          │
          ▼ installs to
┌─────────────────────────────────────────────────────────┐
│  Forge                                                   │
│  (Personal Installed Layer - Private)                    │
│  Personal cognition + persona simulation                 │
└─────────────────────────────────────────────────────────┘
          │
          ▼ executes alongside
┌─────────────────────────────────────────────────────────┐
│  workforge                                               │
│  (Work Execution Layer - Private)                        │
│  Client work + delivery + business operations            │
└─────────────────────────────────────────────────────────┘
          │
          ▼ explained by
┌─────────────────────────────────────────────────────────┐
│  RepoForge                                               │
│  (Public Explanation Layer - Public)                      │
│  Shows the model without exposing private skills         │
└─────────────────────────────────────────────────────────┘
```

---

## Public vs. Private Boundaries

| What Goes Public | What Stays Private |
|------------------|--------------------|
| Model structure | Personal judgment patterns |
| Method explanation | Private memory and decisions |
| Generalized templates | Client and project data |
| Boundary definitions | Business logic (pricing, contracts) |
| Example structure | Unpublished works and research |

**Why this separation?**

1. **Transparency without exposure** — You can share the method without sharing everything
2. **Evolution independent** — Private skills can evolve without breaking public understanding
3. **Safety** — Confidentiality is maintained by design
4. **Reusability** — Others can adopt the model for their own use without copying your private content

---

## For People Who Want to Adopt This Model

If you find this model useful and want to adapt it for your own repositories:

### Start Small
1. **Pick one repetitive task** you do where you notice inconsistent results
2. **Write the skill** using the 9-field template (Purpose → Escalation)
3. **Test it** with different agents
4. **Refine the operating rules** based on failure modes you observe
5. Add it to your registry

### Don't Start With
- 50 skills at once
- Rewriting all your documentation
- Over-engineering for cases you haven't hit yet

### Remember
- Documents don't need to be deleted—they just get demoted to "supporting materials"
- Skills evolve as your judgment evolves—update them when your thinking changes
- The goal is *consistent execution*, not perfect documentation

---

## Frequently Asked Questions

### Q: Do I need to code to use this model?

**A:** No. Skills are just structured markdown files with explicit rules. Agents can execute them directly from markdown. You can add code later if you want automation, but it's not required.

### Q: Does this replace RAG?

**A:** No. It changes what you RAG. Instead of RAG-ing dozens of loose documents to find judgment patterns, you RAG the skill's `SKILL.md` (which has the encoded rules) and then RAG supporting documents *as needed* for content.

### Q: What about large language models that are good at open-ended interpretation?

**A:** Even strong models benefit from explicit judgment encoding. It reduces drift, keeps output consistent with your preferences, and makes handoff to weaker models possible when needed.

### Q: How is this different from just writing a good prompt?

**A:** A skill is a *persistent, versioned, categorized unit* that lives in your repository alongside the data it operates on. It's not a one-off prompt—it's part of your repository's structure.

---

## Further Reading

- [SKILLS_OVERVIEW.md](SKILLS_OVERVIEW.md) — High-level introduction to skills
- [FORGE_VS_WORKFORGE_VS_REPOFORGE.md](FORGE_VS_WORKFORGE_VS_REPOFORGE.md) — Layer boundaries explained
- [PROJECT_STORY.md](PROJECT_STORY.md) — How this project came to be

---

**Maintenance:** Update this document when the public model changes  
**Audience:** Public — Anyone interested in adopting this model
