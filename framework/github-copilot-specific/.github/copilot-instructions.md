# AI Epic Framework - GitHub Copilot Instructions

## Project Context
This project uses the AI Epic Framework, a systematic approach for AI assistants to help developers build complex applications through structured workflows, problem-solving methodologies, and architecture design processes.

## AI Context Header
**When To Use**: Load as primary navigation hub for accessing other framework documentation. Use for conditional loading decisions and optimizing context window usage. Keep loaded throughout session.

**Sample Queries**:
1. "Which documentation should I load for architecture design work?"
2. "How do I efficiently manage context window when working on epic workflows?"
3. "What's the decision matrix for loading problem-solving versus execution standards?"

## Framework Overview
The AI Epic Framework provides systematic approaches for AI assistants to help developers build complex applications through structured workflows, problem-solving methodologies, and architecture design processes.

## Core Principles
- **Context-Aware Loading**: Only load documentation when specifically needed for the current task
- **Progressive Disclosure**: Start with this system prompt, then conditionally load detailed documentation
- **Token Efficiency**: Avoid loading all files simultaneously to preserve context window
- **Task-Specific Guidance**: Match documentation to the specific workflow phase or problem type
- Use systematic problem-solving approaches for complex issues
- Implement hierarchical task breakdown (Initiative → Epic → Phase → Step)
- Apply research-first methodology for architecture decisions
- Maintain comprehensive documentation and context management
- Focus on AI framework application rather than generic engineering principles

## Decision Matrix: When to Load Which Documentation

### 1. Epic Workflow Instructions
**Load When:**
- User requests creation of new initiatives, epics, phases, or steps
- Questions about task hierarchy or folder structure
- Need to understand INDEX.md or REQUIREMENTS.md templates
- Creating or organizing workflow directory structure
- Delegation instructions or task execution flows are needed

**Key Indicators:**
- Keywords: "initiative", "epic", "phase", "step", "workflow", "task hierarchy"
- Directory paths: `/.epic-workflows/tasks/`
- File references: `INDEX.md`, `REQUIREMENTS.md`
- Task status tracking or progress management

### 2. Architecture Lifecycle Management
**Load When:**
- Working with architecture documentation in `docs/architecture/`
- Creating or updating architecture index files
- Questions about document categorization or folder structure
- Need to understand architecture document size limits (700 lines)
- Managing architecture document lifecycle (creation, update, deprecation)

**Key Indicators:**
- Keywords: "architecture", "documentation", "index.md", "categorization"
- Directory paths: `docs/architecture/`
- Document size concerns or breakdown requirements
- Architecture discovery or search commands needed

### 3. Architecture Design Process
**Load When:**
- Designing new system architecture or components
- Creating architecture proposals or technical designs
- Need guidance on research methodology for architecture decisions
- Questions about component design, integration patterns, or quality attributes
- Architecture review processes or validation requirements

**Key Indicators:**
- Keywords: "design", "architecture proposal", "component", "integration", "patterns"
- Technical design discussions or system planning
- Technology stack selection or evaluation
- Architecture validation or review processes

### 4. Problem Solving Framework
**Load When:**
- User explicitly requests systematic problem analysis
- Multiple failed solution attempts (3+ cycles)
- Complex multi-component system failures
- AI appears stuck in solution loops
- Need for comprehensive research and documentation approach

### 5. General Execution Standards
**Load When:**
- Questions about general development practices or standards
- File navigation and verification procedures
- Tool usage guidelines (Context7, Perplexity, Web search)
- Decision-making protocols or documentation requirements
- General quality assurance or execution methodology

## Epic Workflow Management

### MANDATORY SEQUENCE
Plan → Document → Execute → Track → Validate

### Task Hierarchy Structure
- **Initiative** → **Epic** → **Phase** → **Step** (smallest actionable unit)
- Sequential numbering required (1, 2, 3, etc.)
- Each level must reference its parent task in all documentation

### Directory Structure and Naming

#### Folder Naming Convention
```
/.epic-workflows/tasks/[TASK_TYPE]_[NUMBER]_[TASK_NAME]/
```

#### Hierarchical Structure
- **Initiative**  
  `/.epic-workflows/tasks/Initiative_[NUMBER]_[TASK_NAME]/`
- **Epic**  
  `/.epic-workflows/tasks/Initiative_[NUMBER]_[INITIATIVE_NAME]/Epic_[NUMBER]_[TASK_NAME]/`
- **Phase**  
  `/.epic-workflows/tasks/Initiative_[NUMBER]_[INITIATIVE_NAME]/Epic_[NUMBER]_[EPIC_NAME]/Phase_[NUMBER]_[TASK_NAME]/`
- **Step**  
  `/.epic-workflows/tasks/Initiative_[NUMBER]_[INITIATIVE_NAME]/Epic_[NUMBER]_[EPIC_NAME]/Phase_[NUMBER]_[PHASE_NAME]/Step_[NUMBER]_[TASK_NAME]/`

#### Naming Rules
- **[TASK_TYPE]**: Initiative, Epic, Phase, Step
- **[TASK_NAME]**: Short, descriptive (max 5 words)
- **[NUMBER]**: Sequential ordering (1, 2, 3 …)
- Parent names (`[INITIATIVE_NAME]`, `[EPIC_NAME]`, `[PHASE_NAME]`) are the short names of their respective parent tasks

#### Example Structure
```
.epic-workflows/
└── tasks/
    └── Initiative_1_user-auth-system/
        ├── INDEX.md
        ├── REQUIREMENTS.md
        ├── Epic_1_oauth-integration/
        │   ├── INDEX.md
        │   ├── REQUIREMENTS.md
        │   ├── Phase_1_google-oauth-setup/
        │   │   ├── INDEX.md
        │   │   ├── REQUIREMENTS.md
        │   │   ├── Step_1_install-passport-google/
        │   │   │   ├── INDEX.md
        │   │   │   └── REQUIREMENTS.md
        │   │   └── Step_2_configure-oauth-routes/
        │   │       ├── INDEX.md
        │   │       └── REQUIREMENTS.md
        │   └── Phase_2_token-validation/
        │       ├── INDEX.md
        │       └── REQUIREMENTS.md
        └── Epic_2_user-profile-management/
            ├── INDEX.md
            └── REQUIREMENTS.md
```

### Pre-Execution Requirements

#### Mandatory Task Creation Requirements
- Generate the entire folder hierarchy in `/.epic-workflows/tasks/` *before* work starts
- Every task directory **must** contain `INDEX.md` and `REQUIREMENTS.md`

#### Mandatory Goal Definition Requirements
**CRITICAL**: Every task at every level (Initiative, Epic, Phase, Step) **MUST** have clearly defined:

##### Business/Product Goal Requirements
- **Primary Business Objective**: Clear, measurable business value statement
- **Business Impact**: Quantifiable impact on business metrics (revenue, user engagement, efficiency, etc.)
- **User Value**: Direct benefit delivered to end users
- **Success Metrics**: Specific, measurable outcomes that define success
- **Parent Alignment**: Explicit explanation of how this goal supports parent task's business objective

##### Technical Goal Requirements  
- **Primary Technical Objective**: Clear, specific technical outcome statement
- **Technical Impact**: Measurable improvement to system (performance, security, maintainability, scalability)
- **Implementation Scope**: Clear boundaries of what will be built/modified
- **Quality Standards**: Specific performance, security, reliability requirements
- **Parent Alignment**: Explicit explanation of how this goal supports parent task's technical objective

### INDEX.md Template
```markdown
# [Task Name] - Index

## Overview
Brief description of the task and its objectives.

## Status
- [ ] Not Started
- [ ] In Progress
- [ ] Completed
- [ ] Blocked

## Dependencies
List any dependencies or prerequisites.

## Deliverables
List expected outputs and deliverables.

## Notes
Additional context and information.
```

### REQUIREMENTS.md Template
```markdown
# [Task Name] - Requirements

## Functional Requirements
- [Requirement 1]
- [Requirement 2]

## Technical Requirements
- [Technical requirement 1]
- [Technical requirement 2]

## Acceptance Criteria
- [Criterion 1]
- [Criterion 2]

## Constraints
- [Constraint 1]
- [Constraint 2]
```

## Problem Solving Framework

### When To Use
- User explicitly requests systematic problem analysis
- Multiple failed solution attempts (3+ cycles)
- Complex multi-component system failures
- AI appears stuck in solution loops
- Need for comprehensive research and documentation approach

### Systematic Analysis Process
1. **Problem Identification**: Clearly define the issue and scope
2. **Research Phase**: Gather comprehensive information and context
3. **Root Cause Analysis**: Identify underlying causes and dependencies
4. **Solution Development**: Create systematic solution approaches
5. **Implementation**: Execute solutions with validation
6. **Verification**: Confirm resolution and document learnings

### Research-First Methodology
- Always research before implementing solutions
- Use multiple information sources (documentation, examples, community)
- Document findings and decision rationale
- Validate assumptions through testing

### Problem Analysis Template
```
## Problem Analysis Report

### Problem Statement
[Clear, specific description of the issue]

### Investigation Scope
- **Components Affected**: [List]
- **User Impact**: [Description]
- **Business Impact**: [Description]

### Research Findings
- **Documentation Review**: [Findings]
- **Community Solutions**: [Findings]
- **Similar Issues**: [Findings]

### Root Cause Analysis
- **Primary Cause**: [Description]
- **Contributing Factors**: [List]
- **Dependencies**: [List]

### Solution Approach
- **Recommended Solution**: [Description]
- **Alternative Approaches**: [List]
- **Implementation Plan**: [Steps]

### Validation Strategy
- **Testing Approach**: [Description]
- **Success Criteria**: [List]
- **Rollback Plan**: [Description]
```

## Architecture Design Process

### When To Use
- Designing new system architecture or components
- Creating architecture proposals or technical designs
- Need guidance on research methodology for architecture decisions
- Questions about component design, integration patterns, or quality attributes
- Architecture review processes or validation requirements

### Research-First Architecture Methodology
1. **Research Phase**: Gather comprehensive information about requirements, constraints, and existing solutions
2. **Analysis Phase**: Evaluate options against quality attributes and business requirements
3. **Design Phase**: Create detailed architecture proposals with clear rationale
4. **Validation Phase**: Review and validate design decisions
5. **Documentation Phase**: Create comprehensive architecture documentation

### Component Design Template
```
## Component: [Name]
**Responsibility**: One-sentence summary
**Interfaces**: REST / gRPC / events
**Dependencies**: [List]
**Scaling**: Horizontal AutoScale / etc.
**Failure Modes**: [Describe]
```

### Quality Attributes Planning Matrix
| Attribute   | Strategy                                  |
|-------------|-------------------------------------------|
| Scalability | Stateless services + autoscaling groups   |
| Performance | In-memory cache, async I/O                |
| Security    | Zero-trust, least privilege, encryption   |
| Reliability | Circuit breakers, retries, health probes  |
| Observability | Structured logs, metrics, tracing      |

### Architecture Decision Record Template
```
## Architecture Decision Record

### Context
[Background and problem statement]

### Decision
[Clear statement of the decision made]

### Rationale
[Detailed explanation of why this decision was made]

### Alternatives Considered
[List of alternatives with pros/cons]

### Consequences
[Positive and negative consequences]

### Implementation Notes
[Specific implementation guidance]
```

## Architecture Lifecycle Management

### When To Use
- Working with architecture documentation in `docs/architecture/`
- Creating or updating architecture index files
- Questions about document categorization or folder structure
- Need to understand architecture document size limits (700 lines)
- Managing architecture document lifecycle (creation, update, deprecation)

### Document Organization Structure
```
docs/architecture/
├── index.md (mandatory)
├── [category]/
│   ├── index.md (mandatory)
│   ├── [component].md
│   └── [component].md
└── [category]/
    ├── index.md (mandatory)
    └── [component].md
```

### Mandatory Requirements
- **Index Files**: Every architecture folder must contain an `index.md`
- **Document Size**: Maximum 700 lines per document
- **Categorization**: Organize by system component or architectural concern
- **Cross-References**: Maintain links between related documents

### Document Lifecycle
1. **Creation**: New documents follow canonical structure
2. **Updates**: Track changes and maintain version history
3. **Deprecation**: Mark obsolete documents clearly
4. **Archival**: Move deprecated documents to archive folder

### Architecture Discovery Commands
```bash
# Find all architecture documents
find docs/architecture/ -name "*.md" -type f

# Check document sizes
find docs/architecture/ -name "*.md" -exec wc -l {} \;

# Find missing index files
find docs/architecture/ -type d -exec test ! -f {}/index.md \; -print

# Search architecture content
grep -r "architecture" docs/architecture/
```

## General Execution Standards

### When To Use
- Questions about general development practices or standards
- File navigation and verification procedures
- Tool usage guidelines (Context7, Perplexity, Web search)
- Decision-making protocols or documentation requirements
- General quality assurance or execution methodology

### Decision Making Protocol
1. **Research-First**: Always consult official documentation first
2. **Multi-Source Validation**: Cross-check from at least two authoritative sources
3. **Quality Over Speed**: Plan thoroughly, implement incrementally
4. **Comprehensive Documentation**: Capture every decision in task documentation
5. **Architecture Compliance**: Reference/update architecture docs for every significant change

### Tool Usage Guidelines
- **Context7**: Deep codebase pattern & dependency analysis
- **Perplexity**: External best-practice & doc retrieval
- **grep/rg**: Fast in-repo search for configs & patterns
- **wc -l**: Enforce <700-line doc rule
- **find**: Structure & file existence checks

### File Navigation and Verification
1. **Existence Check**: Verify files exist before referencing
2. **Content Validation**: Ensure content matches expectations
3. **Path Verification**: Confirm relative paths are correct
4. **Format Compliance**: Validate against IDE-specific requirements

### Quality Assurance Standards
- **Documentation**: Every significant decision must be documented
- **Testing**: All changes must include appropriate tests
- **Review**: Code and documentation changes require review
- **Validation**: Verify changes work as expected

## Context Management
- Optimize token usage through conditional documentation loading
- Use progressive disclosure for complex investigations
- Maintain context window efficiency
- Implement task-specific guidance systems

## When To Use This Framework
- Load when creating new initiatives, epics, phases, or steps
- Use for task hierarchy questions, folder structure organization, or workflow management
- Apply when facing stubborn technical issues or complex system failures
- Use when designing new system architecture or making technical decisions

## Success Metrics
- Problem fully resolved & validated
- Knowledge preserved in docs
- Process improvements captured
- Framework scales with project complexity 