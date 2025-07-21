# General Execution Standards

# General Execution Standards

## AI Context Header
**When To Use**: Load for research protocols, decision-making standards, tool usage guidelines, and quality assurance. Reference for general development practices and cross-cutting concerns.

**Sample Queries**:
1. "What's the proper research methodology for evaluating this technology stack?"
2. "How should I validate and document this architectural decision?"
3. "What tools should I use for analyzing codebase patterns and dependencies?"

## Framework Navigation
- **Main Navigation**: [user-rules-template.md](./user-rules-template.md) - Access other framework documentation
- **Epic Workflow**: [epic-workflow-instructions.md](./epic-workflow-instructions.md) - Workflow execution standards
- **Problem Solving**: [problem-solving-framework.md](./problem-solving-framework.md) - Systematic troubleshooting approach
- **Architecture Lifecycle**: [architecture-lifecycle.md](./architecture-lifecycle.md) - Architecture documentation standards
- **Architecture Design**: [architecture-design-process.md](./architecture-design-process.md) - Research and validation methodology

## Decision Making Protocol

### 1. Research-First
- Always consult **official documentation** first.
- Use Context7 and Ask Perplexity for additional insight.
- Record every source.

### 2. Multi-Source Validation
- Cross-check information from at least **two authoritative sources**.
- Resolve conflicts before implementation.

### 3. Quality Over Speed
- Plan thoroughly; implement incrementally.
- Validate after each milestone.

### 4. Comprehensive Documentation
- Every decision must be captured in task `INDEX.md` or architecture docs.
- Trade-offs and alternatives always logged.

### 5. Architecture Compliance
- Reference / update architecture docs for **every significant change**.

---

## File Navigation Cheat-Sheet

### Verify Directories
```bash
# Root workflow dir
ls -la /.epic-workflows/

# Tasks dir
ls -la /.epic-workflows/tasks/

# Architecture root
ls -la docs/architecture/
```

### Verify Required Files
```bash
ls -la /.epic-workflows/tasks/Initiative_*/*/INDEX.md
ls -la docs/architecture/*/index.md
```

### Post-Implementation Validation
```bash
# Show newly created task files
find /.epic-workflows/tasks -mmin -30 -type f

# Check architecture doc size
wc -l docs/architecture/**/**/*.md | sort -n | tail -5
```

---

## Tool Usage Guidelines

| Tool          | Primary Purpose                               |
|---------------|-----------------------------------------------|
| **Context7**  | Deep codebase pattern & dependency analysis   |
| **Perplexity**| External best-practice & doc retrieval        |
| **grep/rg**   | Fast in-repo search for configs & patterns    |
| **wc -l**     | Enforce <700-line doc rule                    |
| **find**      | Structure & file existence checks             |

---

## Execution Workflow
1. Plan → 2. Document → 3. Execute (small commits) → 4. Validate → 5. Record → 6. Merge

### Validation Checklist
- [ ] Tests green (unit, integration, e2e)
- [ ] Lint & static analysis pass
- [ ] Architecture docs updated
- [ ] Task `INDEX.md` status = **Completed**

### Rollback Strategy
- Use Git branches; keep changes atomic.
- Ensure previous release tag is functional.

---

## Communication Principles
- **Clarity**: State assumptions, constraints, and context.
- **Traceability**: Link code changes to tasks & docs.
- **Transparency**: Document risks and mitigations.

---

© 2025 Engineering Excellence Council
