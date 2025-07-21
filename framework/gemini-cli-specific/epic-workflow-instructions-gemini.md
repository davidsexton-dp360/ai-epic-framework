# Epic Workflow Instructions

# Epic Workflow Management

## AI Context Header
**When To Use**: Load when creating task hierarchies (Initiative→Epic→Phase→Step), managing workflow structure, delegating tasks, or tracking epic progress. Essential for any workflow organization or task creation activities.

**Sample Queries**:
1. "Create a new epic for user authentication with OAuth integration phases"
2. "How should I structure the requirements for a multi-phase data migration initiative?"
3. "What's the proper way to delegate a step-level task with clear acceptance criteria?"

## Framework Navigation
- **User Rules**: [user-rules-template.md](./user-rules-template.md) - Main navigation and conditional loading guide
- **Problem Solving**: [problem-solving-framework.md](./problem-solving-framework.md) - Systematic troubleshooting approach
- **Execution Standards**: [general-execution-standards.md](./general-execution-standards.md) - Quality and decision-making protocols
- **Architecture Lifecycle**: [architecture-lifecycle.md](./architecture-lifecycle.md) - Architecture documentation management
- **Architecture Design**: [architecture-design-process.md](./architecture-design-process.md) - Design methodology and templates

## MANDATORY SEQUENCE
Plan → Document → Execute → Track → Validate

## 1. Task Hierarchy Structure
- **Initiative** → **Epic** → **Phase** → **Step** (smallest actionable unit)
- Sequential numbering required (1, 2, 3, etc.)
- Each level must reference its parent task in all documentation

## 2. Directory Structure and Naming

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

#### Naming Rules
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

## 3. Pre-Execution Requirements

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

### Goal Validation Protocol
**AI Agent MUST validate goals before task creation:**

1. **Goal Clarity Check**: If business or technical goals are unclear, vague, or missing:
   - **STOP task creation**
   - **ASK user for clarification** with specific questions:
     - "What specific business value should this [task type] deliver?"
     - "How will we measure success of this [task type]?"
     - "What technical improvement should this [task type] achieve?"
     - "How does this [task type] support the [parent task] objective?"

2. **Parent Alignment Check**: For child tasks (Epic → Phase → Step):
   - **VERIFY** child goals directly support parent goals
   - **IDENTIFY** any goal drift or feature creep
   - **REQUIRE** explicit alignment statement

3. **Goal Documentation**: Goals must be:
   - **Specific**: Not generic or vague
   - **Measurable**: Include success criteria
   - **Achievable**: Realistic within scope
   - **Relevant**: Aligned with parent objectives
   - **Time-bound**: Clear completion definition

### Feature Creep Prevention
- **Scope Drift Detection**: If proposed work doesn't align with stated goals, flag as potential feature creep
- **Goal Hierarchy Enforcement**: Child tasks cannot introduce goals that conflict with parent goals
- **Regular Goal Review**: Each task completion must validate goals were achieved as stated
- **Quality Standards**: Apply [general-execution-standards.md](./general-execution-standards.md) for decision validation

## 4. File Templates

### 4.1 INDEX.md
```
# [TASK_TYPE] [NUMBER]: [TASK_NAME]

**Status**: [Not Started | In Progress | Completed]  
**Created**: YYYY-MM-DD HH:MM  
**Updated**: YYYY-MM-DD HH:MM

## Business/Product Goal
**Primary Business Objective**: [Clear statement of business value this task delivers]
- **Business Impact**: [How this task contributes to business metrics, user experience, revenue, etc.]
- **User Value**: [Direct benefit to end users]
- **Success Metrics**: [Measurable outcomes that define success]
- **Alignment with Parent**: [How this goal supports the parent task's business objective]

## Technical Goal  
**Primary Technical Objective**: [Clear statement of technical outcome this task achieves]
- **Technical Impact**: [How this task improves system architecture, performance, security, maintainability]
- **Implementation Scope**: [Boundaries of what will be built/modified]
- **Quality Standards**: [Performance, security, reliability requirements]
- **Alignment with Parent**: [How this goal supports the parent task's technical objective]

## Hierarchy
- **Parent**: [PARENT_TASK_TYPE]_[NUMBER]_[PARENT_NAME]
- **Initiative**: Initiative_[NUMBER]_[INITIATIVE_NAME]
- **Epic**: Epic_[NUMBER]_[EPIC_NAME] (if applicable)
- **Phase**: Phase_[NUMBER]_[PHASE_NAME] (if applicable)

## Goal Alignment Validation
- [ ] **Business Goal Clarity**: Business objective is specific and measurable
- [ ] **Technical Goal Clarity**: Technical objective is specific and achievable  
- [ ] **Parent Business Alignment**: This task's business goal directly supports parent's business goal
- [ ] **Parent Technical Alignment**: This task's technical goal directly supports parent's technical goal
- [ ] **No Goal Drift**: This task stays within scope of stated objectives
- [ ] **Success Criteria Defined**: Clear metrics for determining completion

## Subtasks
| Type | Number | Name | Status | Business Goal Alignment | Technical Goal Alignment | Location |
|------|--------|------|--------|-------------------------|--------------------------|----------|
| phase | 1 | google-oauth-setup | In Progress | ✅ Supports user authentication goal | ✅ Supports OAuth architecture goal | Phase_1_google-oauth-setup |
| phase | 2 | token-validation | Not Started | ✅ Supports security goal | ✅ Supports token management goal | Phase_2_token-validation |

## Context
[Detailed explanation of the scope, purpose, and context of this task, including how it fits into the larger initiative]

## Deliverables
- **Business Deliverable 1**: [What business value will be delivered]
- **Technical Deliverable 1**: [What technical component will be built]  
- **Documentation Deliverable**: [What documentation will be created/updated]
- **Validation Deliverable**: [How success will be measured and validated]

## Architecture References
- **Primary Architecture**: `docs/architecture/[domain]/index.md` - [Brief description of relevance]
- **Design Patterns**: `docs/architecture/patterns/[pattern-doc].md` - [How this pattern applies]
- **Security Guidelines**: `docs/architecture/security/[security-doc].md` - [Security considerations]

## Risk Assessment
### Business Risks
- **Risk**: [Description of business risk]
  - **Mitigation**: [How to prevent or handle this risk]

### Technical Risks  
- **Risk**: [Description of technical risk]
  - **Mitigation**: [How to prevent or handle this risk]

## Success Validation
This task will be considered successful when:
- [ ] All stated business success metrics are achieved
- [ ] All stated technical objectives are measurably met
- [ ] All subtasks are completed and validated
- [ ] Architecture documentation is updated
- [ ] Goal alignment is maintained throughout execution
```

### 4.2 REQUIREMENTS.md
```
# Requirements: [TASK_NAME]

## Business/Product Goal
**Primary Business Objective**: [Clear statement of business value this task delivers]
- **Business Impact**: [How this task contributes to business metrics, user experience, revenue, etc.]
- **User Value**: [Direct benefit to end users]
- **Success Metrics**: [Measurable outcomes that define success]
- **Alignment with Parent**: [How this goal supports the parent task's business objective]

## Technical Goal
**Primary Technical Objective**: [Clear statement of technical outcome this task achieves]
- **Technical Impact**: [How this task improves system architecture, performance, security, maintainability]
- **Implementation Scope**: [Boundaries of what will be built/modified]
- **Quality Standards**: [Performance, security, reliability requirements]
- **Alignment with Parent**: [How this goal supports the parent task's technical objective]

## Functional Requirements

### Core Functionality
- **FR-001: [Requirement Name]**
  - **Description**: [Detailed description of what the system must do]
  - **User Story**: As a [user type], I want [functionality] so that [benefit]
  - **Acceptance Criteria**:
    • [Specific, testable condition 1]
    • [Specific, testable condition 2]
    • [Specific, testable condition 3]
  - **Business Rules**: [Any business logic constraints or rules]
  - **Edge Cases**: [Important edge cases to handle]
  - **Status**: [Not Started | In Progress | Completed]

- **FR-002: [Requirement Name]**
  - **Description**: [Detailed description]
  - **User Story**: As a [user type], I want [functionality] so that [benefit]
  - **Acceptance Criteria**:
    • [Specific condition 1]
    • [Specific condition 2]
  - **Dependencies**: [Links to other requirements this depends on]
  - **Status**: [Not Started | In Progress | Completed]

### User Experience Requirements
- **UX-001: [Requirement Name]**
  - **Description**: [UI/UX specific requirements]
  - **Design Requirements**:
    • [Visual design requirement 1]
    • [Interaction design requirement 2]
    • [Accessibility requirement 3]
  - **User Flow**: [Description of user journey]
  - **Error Handling**: [How errors are presented to users]
  - **Status**: [Not Started | In Progress | Completed]

## Technical Requirements

### Architecture & Design
- **TR-001: [Technical Component Name]**
  - **Description**: [Detailed technical implementation requirement]
  - **Architecture Reference**: [`docs/architecture/[domain]/[specific-doc].md`]
  - **Implementation Details**:
    • [Specific technical detail 1]
    • [Specific technical detail 2]
    • [Specific technical detail 3]
  - **Technology Stack**: [Specific technologies, libraries, frameworks to use]
  - **Design Patterns**: [Specific patterns to follow, reference architecture docs]
  - **Status**: [Not Started | In Progress | Completed]

- **TR-002: [Security Requirement]**
  - **Description**: [Security-specific technical requirement]
  - **Architecture Reference**: [`docs/architecture/security/[specific-security-doc].md`]
  - **Security Controls**:
    • [Authentication requirement]
    • [Authorization requirement]
    • [Data protection requirement]
  - **Compliance**: [Any regulatory or security standards to meet]
  - **Threat Mitigation**: [Specific threats this addresses]
  - **Status**: [Not Started | In Progress | Completed]

### Performance & Scalability
- **PR-001: [Performance Requirement]**
  - **Description**: [Performance-specific requirement]
  - **Performance Targets**:
    • Response time: [specific time requirement]
    • Throughput: [specific volume requirement]
    • Concurrent users: [specific capacity requirement]
  - **Monitoring**: [How performance will be measured]
  - **Architecture Reference**: [`docs/architecture/performance/[performance-doc].md`]
  - **Status**: [Not Started | In Progress | Completed]

### Data Requirements
- **DR-001: [Data Requirement]**
  - **Description**: [Data-specific requirement]
  - **Data Model**: [Description of data structures needed]
  - **Data Flow**: [How data moves through the system]
  - **Storage Requirements**: [Database, caching, file storage needs]
  - **Data Validation**: [Input validation and business rules]
  - **Architecture Reference**: [`docs/architecture/data/[data-doc].md`]
  - **Status**: [Not Started | In Progress | Completed]

### Integration Requirements
- **IR-001: [Integration Requirement]**
  - **Description**: [External system integration requirement]
  - **API Specifications**: [Details of APIs to integrate with]
  - **Data Exchange**: [Format and protocol for data exchange]
  - **Error Handling**: [How integration failures are handled]
  - **Architecture Reference**: [`docs/architecture/integrations/[integration-doc].md`]
  - **Status**: [Not Started | In Progress | Completed]

## Implementation Validation Checklist

### Pre-Implementation Validation
- [ ] **Business Goal Clarity**: Business objective is clearly defined and measurable
- [ ] **Technical Goal Clarity**: Technical objective is specific and achievable
- [ ] **Parent Alignment**: Goals align with and support parent task objectives
- [ ] **Architecture Review**: All referenced architecture documents have been reviewed
- [ ] **Dependency Check**: All blocking dependencies are identified and resolved
- [ ] **Resource Availability**: Required resources (APIs, services, data) are available

### Implementation Progress Validation
- [ ] **Functional Requirements**: All FR requirements marked as "Completed"
- [ ] **Technical Requirements**: All TR requirements marked as "Completed"
- [ ] **Architecture Compliance**: Implementation follows referenced architecture patterns
- [ ] **Code Quality**: Code meets established quality standards and patterns
- [ ] **Testing Coverage**: All acceptance criteria have corresponding tests
- [ ] **Documentation**: Implementation is properly documented

### Post-Implementation Validation
- [ ] **Business Goal Achievement**: Success metrics demonstrate business goal was met
- [ ] **Technical Goal Achievement**: Technical objectives have been measurably achieved
- [ ] **User Acceptance**: Functional requirements pass user acceptance testing
- [ ] **Performance Validation**: Performance requirements are met under expected load
- [ ] **Security Validation**: Security requirements pass security testing
- [ ] **Integration Validation**: All integrations work as specified
- [ ] **Error Handling**: Error scenarios are properly handled and tested
- [ ] **Documentation Complete**: All architecture docs updated to reflect changes

## Dependencies

### Task Dependencies
- **Blocks**: [List of tasks that cannot start until this task is completed]
  • [Task Type]_[Number]_[Task Name]: [Reason why it's blocked]
  • [Task Type]_[Number]_[Task Name]: [Reason why it's blocked]

- **Blocked By**: [List of tasks that must be completed before this task can start]
  • [Task Type]_[Number]_[Task Name]: [What is needed from this task]
  • [Task Type]_[Number]_[Task Name]: [What is needed from this task]

### External Dependencies
- **Third-Party Services**: [External services this task depends on]
  • [Service Name]: [What is needed and current status]
  • [Service Name]: [What is needed and current status]

- **Infrastructure**: [Infrastructure requirements]
  • [Infrastructure Component]: [What is needed and availability]
  • [Infrastructure Component]: [What is needed and availability]

- **Data Sources**: [External data sources required]
  • [Data Source]: [What data is needed and how to access it]
  • [Data Source]: [What data is needed and how to access it]

## Architecture Integration

### Referenced Architecture Documents
- **Primary Architecture**: [`docs/architecture/[domain]/index.md`] - [Brief description of relevance]
- **Design Patterns**: [`docs/architecture/patterns/[pattern-doc].md`] - [How this pattern applies]
- **Security Guidelines**: [`docs/architecture/security/[security-doc].md`] - [Security considerations]
- **Data Architecture**: [`docs/architecture/data/[data-doc].md`] - [Data design implications]
- **Integration Patterns**: [`docs/architecture/integrations/[integration-doc].md`] - [Integration approach]

### Architecture Updates Required
- [ ] **New Architecture Documents**: [List any new architecture docs that need to be created]
- [ ] **Architecture Updates**: [List existing architecture docs that need updates]
- [ ] **Pattern Documentation**: [New patterns discovered that should be documented]

## Risk Assessment

### Technical Risks
- **Risk**: [Description of technical risk]
  - **Probability**: [High | Medium | Low]
  - **Impact**: [High | Medium | Low]
  - **Mitigation**: [How to prevent or handle this risk]

### Business Risks
- **Risk**: [Description of business risk]
  - **Probability**: [High | Medium | Low]
  - **Impact**: [High | Medium | Low]
  - **Mitigation**: [How to prevent or handle this risk]

## Success Definition

### Completion Criteria
This task is considered complete when:
- [ ] All functional requirements are implemented and tested
- [ ] All technical requirements are implemented and meet quality standards
- [ ] Business goal success metrics are achieved
- [ ] Technical goal objectives are measurably met
- [ ] All validation checklists are completed
- [ ] Architecture documentation is updated
- [ ] Implementation is deployed and operational

### Handoff Requirements
For task handoff to be successful:
- [ ] Complete implementation documentation provided
- [ ] All tests passing and documented
- [ ] Performance benchmarks meet requirements
- [ ] Security validation completed
- [ ] Operational runbooks updated (if applicable)
- [ ] Knowledge transfer completed (if applicable)
```

## 5. Architecture Integration Protocol
1. **Before work**: Review relevant `docs/architecture/*/index.md` (see [architecture-lifecycle.md](./architecture-lifecycle.md))
2. **During work**: Align implementation with architectural principles (see [architecture-design-process.md](./architecture-design-process.md))
3. **After completion**: Create or update architecture docs reflecting changes (see [architecture-lifecycle.md](./architecture-lifecycle.md))

## 6. Task Execution Flow
- Status progresses: *Not Started* → *In Progress* → *Completed*
- Update `INDEX.md` prior to delegating a task
- Each subtask must have clear context and requirements
- Record outcomes in parent tasks on completion

## 7. Progress Tracking
- `INDEX.md` holds status and hierarchy
- `REQUIREMENTS.md` tracks requirement-level progress
- Parent tasks update automatically when children complete

## 8. File-Discovery Commands
```bash
# Find by type and number
find /.epic-workflows/tasks/ -name "*[TASK_TYPE]_[NUMBER]*" -type d

# Find in-progress tasks
grep -r "Status.*In Progress" /.epic-workflows/tasks/*/INDEX.md

# Locate architecture references
grep -r "Architecture References" /.epic-workflows/tasks/*/INDEX.md
```

## 9. AI Agent Task Creation Protocol

### Mandatory Pre-Creation Validation
Before creating any task (Initiative, Epic, Phase, Step), AI Agent **MUST**:

1. **Goal Validation Check**:
   - [ ] **Business Goal Clarity**: Is the business objective specific and measurable?
   - [ ] **Technical Goal Clarity**: Is the technical objective specific and achievable?
   - [ ] **Parent Alignment**: Do goals support parent task objectives (if parent exists)?
   - [ ] **Success Metrics**: Are completion criteria clearly defined?

2. **If ANY goal is unclear or missing**:
   - **STOP** task creation immediately
   - **ASK** user for clarification using these prompts:
     - "What specific business value should this [TASK_TYPE] deliver to users/business?"
     - "How will we measure the success of this [TASK_TYPE]?"
     - "What technical improvement/outcome should this [TASK_TYPE] achieve?"
     - "How does this [TASK_TYPE] support the [PARENT_TASK] goal of [PARENT_GOAL]?"
   - **APPLY** [general-execution-standards.md](./general-execution-standards.md) for research and validation protocols

3. **Feature Creep Detection**:
   - [ ] **Scope Check**: Does proposed work align with stated goals?
   - [ ] **Parent Consistency**: Do child goals support (not conflict with) parent goals?
   - [ ] **Goal Drift Warning**: Flag if scope appears to expand beyond original intent

### Task Creation Sequence
1. **Validate Goals** (using protocol above)
2. **Create Directory Structure** (`/.epic-workflows/tasks/[TASK_TYPE]_[NUMBER]_[TASK_NAME]/`)
3. **Generate INDEX.md** (with validated goals)
4. **Generate REQUIREMENTS.md** (with detailed implementation requirements)
5. **Validate Architecture References** (ensure docs exist or note what needs creation)

### Delegation Instructions Template
When delegating or creating tasks, provide:
- **Context**: Inherit from parent `INDEX.md` goals and context
- **Business Goal**: Specific, measurable business objective aligned with parent
- **Technical Goal**: Specific, achievable technical objective aligned with parent  
- **Scope**: Derived from parent `REQUIREMENTS.md` but focused on this task
- **Architecture**: Cite related docs under `docs/architecture/`
- **Location**: `/.epic-workflows/tasks/[TASK_TYPE]_[NUMBER]_[TASK_NAME]/`
- **Parent**: `[PARENT_TASK_TYPE]_[NUMBER]_[PARENT_NAME]`
- **Validation**: Clear success criteria and completion checklist

### Goal Enforcement Rules
1. **No Vague Goals**: Reject goals like "improve the system" or "make it better"
2. **Measurable Success**: Every goal must have quantifiable success criteria
3. **Parent Alignment**: Child tasks cannot contradict or ignore parent objectives
4. **Scope Boundaries**: Clearly define what IS and IS NOT included in the task
5. **Business Value**: Every task must deliver identifiable business value

### AI Agent Error Prevention
- **Don't assume goals**: If user doesn't provide clear goals, ask for them
- **Don't create without validation**: Never create tasks with incomplete goal definition
- **Don't allow scope creep**: Actively monitor for feature drift and flag it
- **Don't skip architecture**: Always reference relevant architecture docs
- **Don't forget validation**: Include comprehensive validation checklists

*Use `attempt_completion` tool with a thorough summary when closing a task, including validation that all goals were achieved.*

## Related Framework Documentation

### Quality and Standards
- **[general-execution-standards.md](./general-execution-standards.md)** - Research protocols, quality standards, and decision-making frameworks that apply to all epic work
- **[problem-solving-framework.md](./problem-solving-framework.md)** - Systematic troubleshooting approach for when epic execution encounters complex issues

### Architecture Integration
- **[architecture-lifecycle.md](./architecture-lifecycle.md)** - How to properly manage architecture documentation during epic execution
- **[architecture-design-process.md](./architecture-design-process.md)** - Design methodology for architectural components created during epics

### Navigation and Usage
- **[user-rules-template.md](./user-rules-template.md)** - Main navigation guide for accessing this and other framework documentation conditionally
