# Problem Solving Framework

## AI Context Header
**When To Use**: Load only after 3+ failed solution attempts, for multi-component system failures, or when explicitly requested. Provides systematic research-driven troubleshooting workflow with temporary file management.

**Sample Queries**:
1. "I've tried multiple solutions for this API integration issue and need systematic analysis"
2. "The authentication system is failing across multiple components - help me decompose this problem"
3. "Create a comprehensive research plan for debugging this performance issue"

## Framework Navigation
- **Main Navigation**: [user-rules-template.md](./user-rules-template.md) - Access other framework documentation
- **Epic Workflow**: [epic-workflow-instructions.md](./epic-workflow-instructions.md) - Complete workflow management system
- **Execution Standards**: [general-execution-standards.md](./general-execution-standards.md) - Research protocols and quality standards
- **Architecture Design**: [architecture-design-process.md](./architecture-design-process.md) - Component analysis methodology

## Overview
A systematic, research-driven workflow for tackling complex technical problems.

## Activation Triggers
Use **only if**:
- 3+ failed solution attempts
- Multi-component or systemic failure
- Explicit user request for deep analysis
- AI stuck in a loop

**Integration with Other Frameworks:**
- Apply [general-execution-standards.md](./general-execution-standards.md) research protocols during investigation
- Use [architecture-design-process.md](./architecture-design-process.md) for component analysis
- Follow [epic-workflow-instructions.md](./epic-workflow-instructions.md) if problem solving is part of epic work

## Mandatory Stages
1. **Research**  
2. **Decompose**  
3. **Execute**  
4. **Validate**  
5. **Cleanup**

---

## Temporary File Structure
```
/.epic-workflows/rules/tmp/
├── research-findings-[YYYYMMDD-HHMMSS].md
├── problem-breakdown-[YYYYMMDD-HHMMSS].md
├── solution-tracking-[YYYYMMDD-HHMMSS].md
├── validation-results-[YYYYMMDD-HHMMSS].md
└── final-summary-[YYYYMMDD-HHMMSS].md
```

## Stage 1 – Research
Create `research-findings-<timestamp>.md` containing:
- Codebase analysis (grep/ripgrep results, configs, tests)
- Documentation review (READMEs, ADRs, architecture docs)
- Dependency analysis (package.json, vulnerability scan)
- External research (error messages, StackOverflow, RFCs)
- Research gaps

## Stage 2 – Decompose
Create `problem-breakdown-<timestamp>.md`:
- Layered breakdown: symptoms → technical → architectural → environmental
- Priority list & dependency graph
- Primary/backup strategies + risk matrix

## Stage 3 – Execute
Create `solution-tracking-<timestamp>.md`:
- Log each attempt: research basis, steps, outcome
- Incremental commits & tests
- Pattern adaptations & rationale

## Stage 4 – Validate
Create `validation-results-<timestamp>.md`:
- Test matrix (unit, integration, e2e, perf, security)
- Root-cause confirmation
- Research alignment rating
- Lessons learned & recommendations

## Stage 5 – Cleanup
Create `final-summary-<timestamp>.md`:
- Root cause, solution, key changes
- Docs updated, artifacts produced
- Technical & process lessons
- Future improvements

## CLI Helpers
```bash
# Start a research file
ts=$(date +%Y%m%d-%H%M%S)
touch /.epic-workflows/rules/tmp/research-findings-$ts.md

# Purge tmp files older than 7 days
find /.epic-workflows/rules/tmp -name "*.md" -mtime +7 -delete
```

## Success Metrics
- Problem fully resolved & validated
- Knowledge preserved in docs
- Process improvements captured
