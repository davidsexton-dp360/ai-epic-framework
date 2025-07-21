# Epic Workflow Rules

## MANDATORY SEQUENCE
Plan → Document → Execute → Track → Validate

## Task Hierarchy Structure
- **Initiative** → **Epic** → **Phase** → **Step** (smallest actionable unit)
- Sequential numbering required (1, 2, 3, etc.)
- Each level must reference its parent task in all documentation

## Directory Structure and Naming

### Folder Naming Convention
```
/.epic-workflows/tasks/[TASK_TYPE]_[NUMBER]_[TASK_NAME]/
```

### Hierarchical Structure
- **Initiative**  
  `/.epic-workflows/tasks/Initiative_[NUMBER]_[TASK_NAME]/`
- **Epic**  
  `/.epic-workflows/tasks/Initiative_[NUMBER]_[INITIATIVE_NAME]/Epic_[NUMBER]_[TASK_NAME]/`
- **Phase**  
  `/.epic-workflows/tasks/Initiative_[NUMBER]_[INITIATIVE_NAME]/Epic_[NUMBER]_[EPIC_NAME]/Phase_[NUMBER]_[TASK_NAME]/`
- **Step**  
  `/.epic-workflows/tasks/Initiative_[NUMBER]_[INITIATIVE_NAME]/Epic_[NUMBER]_[EPIC_NAME]/Phase_[NUMBER]_[PHASE_NAME]/Step_[NUMBER]_[TASK_NAME]/`

### Naming Rules
- **[TASK_TYPE]**: Initiative, Epic, Phase, Step
- **[TASK_NAME]**: Short, descriptive (max 5 words)
- **[NUMBER]**: Sequential ordering (1, 2, 3 …)
- Parent names (`[INITIATIVE_NAME]`, `[EPIC_NAME]`, `[PHASE_NAME]`) are the short names of their respective parent tasks

### Example Structure
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

## Pre-Execution Requirements

### Mandatory Task Creation Requirements
- Generate the entire folder hierarchy in `/.epic-workflows/tasks/` *before* work starts
- Every task directory **must** contain `INDEX.md` and `REQUIREMENTS.md`

### Mandatory Goal Definition Requirements
**CRITICAL**: Every task at every level (Initiative, Epic, Phase, Step) **MUST** have clearly defined:

#### Business/Product Goal Requirements
- **Primary Business Objective**: Clear, measurable business value statement
- **Business Impact**: Quantifiable impact on business metrics (revenue, user engagement, efficiency, etc.)
- **User Value**: Direct benefit delivered to end users
- **Success Metrics**: Specific, measurable outcomes that define success
- **Parent Alignment**: Explicit explanation of how this goal supports parent task's business objective

#### Technical Goal Requirements  
- **Primary Technical Objective**: Clear, specific technical outcome statement
- **Technical Impact**: Measurable improvement to system (performance, security, maintainability, scalability)
- **Implementation Scope**: Clear boundaries of what will be built/modified
- **Quality Standards**: Specific performance, security, reliability requirements
- **Parent Alignment**: Explicit explanation of how this goal supports parent task's technical objective

## INDEX.md Template
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

## REQUIREMENTS.md Template
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

## Task Breakdown
- Use epic workflow for task breakdown (Initiative → Epic → Phase → Step)
- Create task hierarchy in `/.epic-workflows/tasks/`
- Use INDEX.md and REQUIREMENTS.md for each task
- Follow Plan → Document → Execute → Track → Validate sequence

## File Management
- Maintain architecture docs in `docs/architecture/`
- Use INDEX.md and REQUIREMENTS.md for each task
- Create task hierarchies with clear naming conventions
- Track progress and completion status

## Workflow Integration
- Integrate with existing project management tools
- Maintain consistency across team members
- Update task status regularly
- Document decisions and trade-offs
