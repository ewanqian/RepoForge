# Forge vs. workforge vs. RepoForge

**Status:** `active`  
**Repository:** RepoForge (Public Explanation Layer)  
**Last Updated:** 2026-04-01

---

## Quick Summary

| Repository | Layer | Purpose | Privacy |
|------------|-------|---------|---------|
| **Forge** | Personal Installed | Ewan's cognition + persona skills | Private |
| **workforge** | Work Execution | Client ops, delivery, business workflows | Private |
| **RepoForge** | Public Explanation | Show skill-based governance model | Public |
| **SpacePort** | Source Layer | Research lab → skill mother templates | Public |

---

## Why Three Repositories?

The separation exists because **different layers serve different purposes** and have **different audiences**.

### The Confusion This Solves

Before this structure:
- Personal methods mixed with client work
- Public repos tried to explain private logic
- Agents confused about which repo to trust for what
- Hard to share methodology without exposing private data

After this structure:
- Each repo has a clear, singular purpose
- Boundaries are explicit
- Agents know where to look for what
- Can share methodology publicly without exposing private judgment patterns

---

## Forge: Personal Cognition Layer

### Purpose
Forge is where **Ewan's thinking patterns are encoded as skills**. It simulates how Ewan:
- Judges which works belong to which practice lines
- Writes about perception, space, time, collaboration
- Decides what's publish-safe vs. private
- Organizes personal knowledge and memory

### What Lives Here
- **Persona skills**: artist-practice-cartographer, perceptual-migration-writer, live-visual-dramaturge, etc.
- **Personal ops skills**: portfolio-route-builder, project-credit-normalizer, public-private-boundary-checker
- **Memory**: Long-term reflections, decisions, lessons learned
- **Docs**: Writing style, demand trajectory, system guides (marked legacy or active)

### What Doesn't Live Here
- Client-specific work (goes to workforge)
- Public explanations of methodology (goes to RepoForge)
- Raw research materials (stays in SpacePort until distilled)

### Agent Behavior in Forge
When an agent enters Forge:
1. It's in the **personal cognition layer**
2. Skills here simulate **Ewan's judgment**, not generic assistance
3. Always check `skills/registry.md` before operating
4. Legacy docs (e.g., `AGENT_ROLES.md`) are reference only, not primary

### Privacy Level
**Private** — Contains personal judgment patterns, unpublished works, internal decision-making logic

---

## workforge: Work Execution Layer

### Purpose
workforge is where **professional work gets executed**. It handles:
- Client relationships and communications
- Project delivery and quality control
- Business administration (pricing, invoices, contracts)
- Self-management as a working professional

### What Lives Here
- **Client ops skills**: onboarding, proposals, follow-ups, feedback collection
- **Delivery skills**: checkpoint management, QC, packaging, revision tracking
- **Self-management skills**: time tracking, invoicing, capacity planning, boundaries
- **Business ops skills**: contract review, pricing calculation, tax prep, networking
- **Projects**: Active and completed client work
- **Clients**: Client records, communication logs, agreements

### What Doesn't Live Here
- Personal artistic practice (stays in Forge)
- Personal cognition and memory (stays in Forge)
- Public methodology explanations (goes to RepoForge)

### Agent Behavior in workforge
When an agent enters workforge:
1. It's in the **work execution layer**
2. Skills here are **professional and client-facing**
3. Respect client confidentiality and business boundaries
4. Do not mix personal skills (Forge) with work skills (workforge)

### Privacy Level
**Private** — Contains client data, financial information, business operations

---

## RepoForge: Public Explanation Layer

### Purpose
RepoForge is where **the skill-based governance model is explained publicly**. It:
- Shows how skills organize repository operations
- Demonstrates the four-layer architecture
- Provides public examples without exposing private logic
- Serves as documentation for collaborators and peers

### What Lives Here
- **SKILLS_OVERVIEW.md**: Explains what skills are and why they matter
- **FORGE_VS_WORKFORGE_VS_REPOFORGE.md**: This file, layer boundaries
- **PUBLIC_SKILL_MODEL.md**: What's safe to show publicly
- **Example skill structures**: Sanitized examples of skill registries
- **Governance documentation**: How repos are maintained, updated, handed off

### What Doesn't Live Here
- Actual personal skills from Forge (too private)
- Actual work skills from workforge (client confidential)
- Real project data, client names, pricing
- Unpublished artistic works or research

### Agent Behavior in RepoForge
When an agent enters RepoForge:
1. It's in the **public explanation layer**
2. Everything here is safe for public consumption
3. Use this to explain the system to others
4. Reference Forge/workforge structure without exposing their contents

### Privacy Level
**Public** — Intentionally designed for external viewing

---

## SpacePort: Source Layer (Bonus)

### Purpose
VIRTURA-SpacePort is the **research laboratory** where skill mother templates are developed. It:
- Houses research-derived skill templates
- Provides source-of-truth for generalizable skills
- Serves as installation source for Forge and workforge
- Keeps research separate from personal/workspace-specific implementations

### Relationship to Other Layers
```
SpacePort (source)
    ↓ installs to
Forge (personal installed)
    ↓ executes in
workforge (work execution)
    ↓ explained by
RepoForge (public explanation)
```

### Privacy Level
**Public** — Research outputs, reusable templates, generalizable methods

---

## Data Flow Between Layers

### Installation Flow (SpacePort → Forge/workforge)
1. Skill template developed in SpacePort/stations/skill-forge
2. Reviewed and tested
3. Installed to Forge/skills/installed-from-spaceport/ (for persona skills)
4. Or installed to workforge/skills/ (for work skills)
5. Local customization applied as needed

### Execution Flow (Forge ↔ workforge)
- Forge skills may **reference** workforge projects (e.g., "this collaboration belongs to X project")
- workforge skills may **call on** Forge persona skills (e.g., "write this proposal using Ewan's voice")
- But they remain **separate skill registries** with separate purposes

### Explanation Flow (Forge/workforge → RepoForge)
- RepoForge **describes the model** without copying private content
- Uses sanitized examples: "a persona skill might do X" not "here's Ewan's actual skill"
- Shows structure, not substance

---

## Common Questions

### Q: Why not just one big repository?

**A:** Because different audiences need different things:
- **You** need personal cognition (Forge)
- **Your work** needs professional execution (workforge)
- **Others** need to understand the model without seeing your private data (RepoForge)

Mixing them creates:
- Accidental exposure of private data
- Confusion about what's authoritative
- Harder maintenance (everything touches everything)

### Q: Can skills move between repositories?

**A:** Yes, but with transformation:
- **SpacePort → Forge**: Install as-is or with personal customization
- **SpacePort → workforge**: Install as work-facing skill
- **Forge → RepoForge**: Only as sanitized example, not full skill
- **workforge → RepoForge**: Only as abstracted pattern, no client data

### Q: What if a skill needs data from multiple repos?

**A:** The skill specifies its **Source of Truth**:
- A Forge skill might say: "Source: portfolio/README.md + Forge/memory/"
- A workforge skill might say: "Source: workforge/projects/ + workforge/clients/"
- Cross-repo references are fine, but the skill lives in one registry

### Q: How do agents know which repo to enter?

**A:** By task type:
- **Personal artistic practice** → Forge
- **Client work** → workforge
- **Explaining the system** → RepoForge
- **Installing new skills** → SpacePort → Forge/workforge

---

## Migration Path

If you're moving from an undifferentiated structure to this three-repo model:

### Phase 1: Add Skills Layers
1. Create `skills/README.md` and `skills/registry.md` in Forge
2. Create `skills/README.md` and `skills/registry.md` in workforge
3. Create `docs/SKILLS_OVERVIEW.md` in RepoForge

### Phase 2: Mark Legacy Documents
1. Add status headers to old agent/role/system docs
2. Mark as `legacy` or `active-needs-update`
3. Don't delete—just clarify they're not primary entry points

### Phase 3: Update Entry Points
1. Update `AI_ONBOARDING.md` to reference skills first
2. Update `INDEX.md` to include skills layer
3. Update READMEs to clarify layer purposes

### Phase 4: Migrate Content (Optional)
1. Move personal cognition docs to Forge (if not already there)
2. Move work execution docs to workforge
3. Move public explanations to RepoForge

---

## Visual Summary

```
┌─────────────────────────────────────────────────────────────┐
│                    VIRTURA-SpacePort                        │
│                 (Source Layer - Public)                     │
│   Research Lab → Skill Mother Templates                     │
│   stations/skill-forge/                                     │
└─────────────────────────────────────────────────────────────┘
                            ↓ installs to
        ┌───────────────────┴───────────────────┐
        ↓                                       ↓
┌───────────────────┐                 ┌───────────────────┐
│      Forge        │                 │    workforge      │
│ (Personal Layer)  │                 │ (Work Layer)      │
│                   │                 │                   │
│ skills/           │                 │ skills/           │
│ ├── persona/      │                 │ ├── client-ops/   │
│ ├── personal-ops/ │                 │ ├── delivery/     │
│ └── installed/    │                 │ └── business-ops/ │
│                   │                 │                   │
│ memory/           │                 │ projects/         │
│ docs/             │                 │ clients/          │
│ projects/         │                 │ templates/        │
└───────────────────┘                 └───────────────────┘
        ↓                                       ↓
        └───────────────────┬───────────────────┘
                            ↓ explained by
                ┌───────────────────────┐
                │      RepoForge        │
                │ (Public Explanation)  │
                │                       │
                │ docs/                 │
                │ ├── SKILLS_OVERVIEW   │
                │ ├── FORGE_VS_WORK...  │
                │ └── PUBLIC_SKILL...   │
                └───────────────────────┘
```

---

**Maintenance:** Update this document when layer boundaries evolve  
**Audience:** Internal (you + your agents) + external collaborators who need to understand the structure
