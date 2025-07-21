# Reference: architecture-lifecycle.md

# Architecture Lifecycle Management

## AI Context Header
**When To Use**: Load when working with docs/architecture/ folder structure, managing architecture documentation, creating index files, or enforcing document size limits (700 lines). Essential for architecture documentation organization.

**Sample Queries**:
1. "How should I organize the new microservices architecture documentation?"
2. "This architecture document is over 700 lines - how do I split it properly?"
3. "Where should I place the new authentication architecture docs and update the index?"

## Framework Navigation
- **Main Navigation**: [user-rules-template.md](./user-rules-template.md) - Access other framework documentation
- **Epic Workflow**: [epic-workflow-instructions.md](./epic-workflow-instructions.md) - Architecture integration in workflows
- **Architecture Design**: [architecture-design-process.md](./architecture-design-process.md) - Design methodology and component templates
- **Execution Standards**: [general-execution-standards.md](./general-execution-standards.md) - Documentation quality standards

## 1. Architecture Folder Structure and Categorization

The `docs/architecture/` directory, located at the project root, is the **single source of truth** for all architecture‐related documentation. Use the following rules to guarantee clarity, extensibility, and discoverability.

### 1.1 Categorization
All architecture documents **must** be placed in logical sub-folders grouped by domain, category, or the tooling they describe.

**Existing example categories**
- `/docs/architecture/core/` – Foundational principles & cross-cutting concerns
- `/docs/architecture/database/` – Database design, schema, and data-access patterns
- `/docs/architecture/decisions/` – Architectural Decision Records (ADRs) & major design choices

**Creating new categories**
If a new architectural domain or key technology is introduced, create a new sub-folder, e.g.:
- `/docs/architecture/authentication/`
- `/docs/architecture/microservices/`

### 1.2 Naming Conventions
- **Folder names** – lowercase, kebab-case (e.g. `event-driven`, `user-management`)
- **Markdown files** – lowercase, kebab-case, clearly describing the content (`event-driven-architecture.md`)

### 1.3 AI / Human Discoverability
A logical folder structure and naming convention enables:
1. Rapid human navigation
2. Accurate AI semantic search & indexing

### 1.4 Mandatory `index.md` in Every Folder
Each directory **must** include an `index.md` that indexes all documents & child folders in a table with three columns:
| Domain | Description | Location |
|--------|-------------|----------|

**Purpose of `index.md`**
- Instant lookup for engineers
- Machine-readable overview for AI agents
- Clear guidance on where to place new docs

## 2. Architecture Document Content Guidelines
Every `.md` inside `/docs/architecture/` must follow this canonical structure:

```
# [Component / Topic Name]

**Status**: Existing | Planned | Deprecated  
**Last Updated**: YYYY-MM-DD  
**Stakeholders**: [Teams / Roles]  
**Related Docs**: [Links]

## Purpose
Explain the intent and scope.

## Key Principles
Enumerate governing principles.

## Components & Interactions
Describe main components and how they interact.

## Diagrams / Visuals
Reference or describe diagrams that aid understanding.

## Trade-offs & Justifications
Document the reasoning behind major decisions.

## Technical Details
- **Technology Stack**
- **Configuration & Env Vars**
- **Dependencies & Versions**
- **Testing Strategy**
- **Deployment Considerations**

## Quality Attributes
Discuss performance, scalability, security, reliability, maintainability.
```

## 3. Integration with Epic Workflow
- **Pre-Implementation** – Before any new Initiative/Epic/Phase/Step starts, consult this file and relevant `index.md`s.
- **During Implementation** – Align all code & config with documented architecture.
- **Post-Completion** – Generate or update docs for any architectural change.

## 4. Document Size Management – 700 Line Hard Limit
- Monitor size via `wc -l file.md`.
- If >700 lines, split into focused sub-docs and update parent `index.md`.

## 5. Helpful CLI Snippets
```bash
# Find architecture docs on a topic
find docs/architecture/ -name "*.md" | grep -i oauth

# List all index files
find docs/architecture/ -name index.md

# Detect large files (>600 lines)
find docs/architecture/ -name "*.md" -exec wc -l {} + | awk '$1>600{print $2" → "$1" lines"}'
```

## 6. Validation Checklist
- Alignment with principles
- Correct folder & filename
- Listed in parent `index.md`
- <700 lines
- Status field populated
- Trade-offs recorded

---


