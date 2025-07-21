# Kilo Code Adaptation Instructions

## Overview
This document provides detailed instructions for adapting the AI Epic Framework to Kilo Code's custom rules format. Kilo Code uses a directory-based approach with `.kilocode/rules/` for project-specific rules and supports JSON configuration.

## Kilo Code Format Requirements
- **Directory Structure**: `.kilocode/rules/` for project rules
- **File Format**: Markdown files with descriptive names
- **Content Style**: Concise, focused rules
- **Privacy**: Local processing, no external dependencies

## Pre-Adaptation Setup

### Step 1: Clear Target Directory
```bash
# Remove existing content
rm -rf framework/kilo-code-specific/*
```

### Step 2: Create Directory Structure
```bash
# Create the .kilocode directory structure
mkdir -p framework/kilo-code-specific/.kilocode/rules
```

## Content Adaptation Process

### Step 1: Create Main Framework Rules File
Create `framework/kilo-code-specific/.kilocode/rules/ai-epic-framework.md`:

```markdown
# AI Epic Framework - Kilo Code Rules

## Framework Overview
The AI Epic Framework provides systematic approaches for AI assistants to help developers build complex applications through structured workflows, problem-solving methodologies, and architecture design processes.

## Core Principles
- Use systematic problem-solving approaches for complex issues
- Implement hierarchical task breakdown (Initiative → Epic → Phase → Step)
- Apply research-first methodology for architecture decisions
- Maintain comprehensive documentation and context management
- Focus on AI framework application rather than generic engineering principles

## Epic Workflow Management
- Break down complex projects into manageable epics
- Use INDEX.md and REQUIREMENTS.md templates for task organization
- Implement systematic delegation and execution flows
- Maintain progress tracking and status management

## Problem Solving Framework
- Apply systematic analysis for stubborn technical issues
- Use research-first approach before solution implementation
- Document investigation processes and findings
- Implement solution validation and verification

## Architecture Design Process
- Follow research methodology for architecture decisions
- Use component design templates and integration patterns
- Implement quality attribute analysis and trade-off evaluation
- Maintain architecture documentation lifecycle

## Execution Standards
- Follow file navigation and verification procedures
- Use appropriate tools (Context7, Perplexity, Web search)
- Implement decision-making protocols and documentation requirements
- Maintain quality assurance and execution methodology

## Context Management
- Optimize token usage through conditional documentation loading
- Use progressive disclosure for complex investigations
- Maintain context window efficiency
- Implement task-specific guidance systems
```

### Step 2: Create Workflow Instructions
Create `framework/kilo-code-specific/.kilocode/rules/epic-workflow.md`:

```markdown
# Epic Workflow Instructions

## When To Use
Load when creating new initiatives, epics, phases, or steps. Use for task hierarchy questions, folder structure organization, or workflow management.

## Task Hierarchy Structure
```
Initiative/
├── Epic_001_Task_Name/
│   ├── Phase_001_Phase_Name/
│   │   ├── Step_001_Step_Name/
│   │   │   ├── INDEX.md
│   │   │   ├── REQUIREMENTS.md
│   │   │   └── [implementation files]
│   │   └── Step_002_Step_Name/
│   └── Phase_002_Phase_Name/
└── Epic_002_Task_Name/
```

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

## Workflow Execution
1. Create task hierarchy following naming conventions
2. Generate INDEX.md and REQUIREMENTS.md files
3. Implement systematic delegation and progress tracking
4. Maintain documentation and context throughout execution
```

### Step 3: Create Problem Solving Rules
Create `framework/kilo-code-specific/.kilocode/rules/problem-solving.md`:

```markdown
# Problem Solving Framework

## When To Use
Apply when facing stubborn technical issues, multiple failed solution attempts, or complex multi-component system failures.

## Systematic Analysis Process
1. **Problem Identification**: Clearly define the issue and scope
2. **Research Phase**: Gather comprehensive information and context
3. **Root Cause Analysis**: Identify underlying causes and dependencies
4. **Solution Development**: Create systematic solution approaches
5. **Implementation**: Execute solutions with validation
6. **Verification**: Confirm resolution and document learnings

## Research-First Methodology
- Always research before implementing solutions
- Use multiple information sources (documentation, examples, community)
- Document findings and decision rationale
- Validate assumptions through testing

## Investigation Documentation
- Record all research steps and findings
- Document failed attempts and lessons learned
- Maintain context for future reference
- Create reusable knowledge base entries

## Solution Validation
- Test solutions in isolated environments
- Verify all requirements are met
- Document implementation steps
- Create rollback procedures
```

### Step 4: Create Architecture Design Rules
Create `framework/kilo-code-specific/.kilocode/rules/architecture-design.md`:

```markdown
# Architecture Design Process

## When To Use
Use when designing new system architecture, creating technical proposals, or making architecture decisions.

## Research Methodology
1. **Technology Evaluation**: Research relevant technologies and patterns
2. **Requirement Analysis**: Understand functional and non-functional requirements
3. **Constraint Identification**: Identify technical and business constraints
4. **Pattern Selection**: Choose appropriate architectural patterns
5. **Validation**: Verify design decisions through prototyping

## Component Design Templates
- **Service Components**: Define interfaces, responsibilities, and dependencies
- **Data Components**: Design data models, storage, and access patterns
- **Integration Components**: Plan communication protocols and APIs
- **Security Components**: Implement authentication, authorization, and data protection

## Quality Attributes
- **Performance**: Response time, throughput, and resource utilization
- **Scalability**: Horizontal and vertical scaling capabilities
- **Reliability**: Fault tolerance and error handling
- **Security**: Data protection and access control
- **Maintainability**: Code organization and documentation

## Integration Patterns
- **API-First Design**: Design interfaces before implementation
- **Event-Driven Architecture**: Use events for loose coupling
- **Microservices**: Decompose into focused, independent services
- **Data Consistency**: Implement appropriate consistency models
```

### Step 5: Create Execution Standards
Create `framework/kilo-code-specific/.kilocode/rules/execution-standards.md`:

```markdown
# Execution Standards

## File Navigation
- Always verify file existence before operations
- Use appropriate tools for file discovery and search
- Maintain organized directory structures
- Document file relationships and dependencies

## Tool Usage Guidelines
- **Context7**: Use for library documentation and API references
- **Perplexity**: Use for research and information gathering
- **Web Search**: Use for current information and examples
- **File Operations**: Use appropriate tools for file management

## Decision-Making Protocols
- Document decision rationale and alternatives considered
- Use systematic evaluation criteria
- Consider long-term implications and maintenance
- Validate decisions through testing and feedback

## Quality Assurance
- Implement comprehensive testing strategies
- Use code review and validation processes
- Maintain documentation standards
- Follow established coding conventions

## Documentation Requirements
- Create clear and comprehensive documentation
- Use consistent formatting and structure
- Include examples and use cases
- Maintain up-to-date information
```

### Step 6: Create Context Management Rules
Create `framework/kilo-code-specific/.kilocode/rules/context-management.md`:

```markdown
# Context Management

## Token Optimization
- Load documentation conditionally based on task requirements
- Use progressive disclosure for complex investigations
- Prioritize active task information
- Unload unnecessary context when possible

## Conditional Loading Logic
- **Workflow Management**: Load epic workflow instructions
- **Problem Solving**: Load problem-solving framework
- **Architecture Design**: Load architecture design process
- **General Tasks**: Load execution standards

## Context Window Management
- Monitor token usage and context window capacity
- Prioritize essential information for current task
- Use efficient information retrieval strategies
- Maintain context continuity across sessions

## Information Organization
- Structure information hierarchically
- Use clear categorization and tagging
- Implement efficient search and retrieval
- Maintain information currency and accuracy
```

## Validation Steps

### Step 1: Directory Structure Verification
```bash
# Verify directory structure
ls -la framework/kilo-code-specific/.kilocode/rules/
```

Expected files:
- `ai-epic-framework.md`
- `epic-workflow.md`
- `problem-solving.md`
- `architecture-design.md`
- `execution-standards.md`
- `context-management.md`

### Step 2: Content Verification
- Verify all generic content is preserved
- Check that content follows Kilo Code's concise style
- Ensure no external dependencies or references
- Validate that all framework concepts are included

### Step 3: Format Verification
- Confirm files use proper Markdown formatting
- Verify content is organized logically
- Check that rules are actionable and clear
- Ensure privacy-focused approach is maintained

## Kilo Code Specific Features

### Privacy-Focused Processing
- All rules are processed locally
- No external API calls or dependencies
- Maintains user privacy and data security
- Works offline without internet connectivity

### Directory-Based Organization
- Rules are organized in `.kilocode/rules/` directory
- Each rule file has a specific focus and purpose
- Easy to maintain and update individual rules
- Clear separation of concerns

### Concise Rule Format
- Rules are written in clear, actionable language
- Focus on practical guidance and examples
- Avoid unnecessary verbosity
- Maintain readability and usability

## Success Criteria

The Kilo Code adaptation is successful when:
- All 6 rule files are created in `.kilocode/rules/` directory
- Content preserves 100% of generic framework functionality
- Format follows Kilo Code's privacy-focused approach
- Rules are concise, actionable, and well-organized
- No external dependencies or references exist
- Framework functionality is identical to other IDE adaptations 