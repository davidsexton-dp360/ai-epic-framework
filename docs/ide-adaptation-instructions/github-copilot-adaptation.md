# GitHub Copilot Adaptation Instructions

## Overview
This document provides detailed instructions for adapting the AI Epic Framework to GitHub Copilot's repository custom instructions format. GitHub Copilot uses `.github/copilot-instructions.md` for project-specific guidance.

## GitHub Copilot Format Requirements
- **File Location**: `.github/copilot-instructions.md`
- **Content Style**: Clear, contextual instructions
- **Structure**: Project context, coding standards, and specific guidance
- **Integration**: Works with GitHub Copilot's code completion system

## Pre-Adaptation Setup

### Step 1: Clear Target Directory
```bash
# Remove existing content
rm -rf framework/github-copilot-specific/*
```

### Step 2: Create Directory Structure
```bash
# Create the .github directory structure
mkdir -p framework/github-copilot-specific/.github
```

## Content Adaptation Process

### Step 1: Create Main Framework Instructions File
Create `framework/github-copilot-specific/.github/copilot-instructions.md`:

```markdown
# AI Epic Framework - GitHub Copilot Instructions

## Project Context
This project uses the AI Epic Framework, a systematic approach for AI assistants to help developers build complex applications through structured workflows, problem-solving methodologies, and architecture design processes.

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

## Problem Solving Framework
- Apply systematic analysis for stubborn technical issues
- Use research-first approach before solution implementation
- Document investigation processes and findings
- Implement solution validation and verification

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

## Architecture Design Process
- Follow research methodology for architecture decisions
- Use component design templates and integration patterns
- Implement quality attribute analysis and trade-off evaluation
- Maintain architecture documentation lifecycle

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

## Execution Standards
- Follow file navigation and verification procedures
- Use appropriate tools (Context7, Perplexity, Web search)
- Implement decision-making protocols and documentation requirements
- Maintain quality assurance and execution methodology

## Tool Usage Guidelines
- **Context7**: Use for library documentation and API references
- **Perplexity**: Use for research and information gathering
- **Web Search**: Use for current information and examples
- **File Operations**: Use appropriate tools for file management

## Context Management
- Optimize token usage through conditional documentation loading
- Use progressive disclosure for complex investigations
- Maintain context window efficiency
- Implement task-specific guidance systems

## Conditional Loading Logic
- **Workflow Management**: Load epic workflow instructions
- **Problem Solving**: Load problem-solving framework
- **Architecture Design**: Load architecture design process
- **General Tasks**: Load execution standards

## Token Optimization
- Load documentation conditionally based on task requirements
- Use progressive disclosure for complex investigations
- Prioritize active task information
- Unload unnecessary context when possible

## When To Use Framework Components
- **Epic Workflow**: When creating new initiatives, epics, phases, or steps
- **Problem Solving**: When facing stubborn technical issues or complex system failures
- **Architecture Design**: When designing new system architecture or making technical decisions
- **Execution Standards**: For general development tasks and quality assurance

## Coding Standards
- Follow the framework's systematic approach to problem-solving
- Implement proper documentation and context management
- Use research-first methodology for complex decisions
- Maintain quality attributes in all implementations
- Focus on AI framework application rather than generic engineering principles

## File Organization
- Use the hierarchical task breakdown structure
- Create INDEX.md and REQUIREMENTS.md files for each task
- Maintain organized directory structures
- Document file relationships and dependencies

## Documentation Requirements
- Create clear and comprehensive documentation
- Use consistent formatting and structure
- Include examples and use cases
- Maintain up-to-date information
- Follow the framework's documentation standards

## Quality Assurance
- Implement comprehensive testing strategies
- Use code review and validation processes
- Maintain documentation standards
- Follow established coding conventions
- Apply the framework's quality attributes

## Integration Patterns
- **API-First Design**: Design interfaces before implementation
- **Event-Driven Architecture**: Use events for loose coupling
- **Microservices**: Decompose into focused, independent services
- **Data Consistency**: Implement appropriate consistency models

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
ls -la framework/github-copilot-specific/.github/
```

Expected files:
- `copilot-instructions.md`

### Step 2: Content Verification
- Verify all generic content is preserved
- Check that content follows GitHub Copilot's contextual style
- Ensure no external dependencies or references
- Validate that all framework concepts are included

### Step 3: Format Verification
- Confirm file uses proper Markdown formatting
- Verify content is organized logically
- Check that instructions are actionable and clear
- Ensure project context is well-defined

## GitHub Copilot Specific Features

### Repository Custom Instructions
- Instructions are specific to the repository
- Provides context for all code completion suggestions
- Integrates with GitHub Copilot's AI system
- Maintains consistency across the project

### Contextual Code Completion
- Framework guidance influences code suggestions
- Maintains systematic approach in generated code
- Ensures adherence to framework principles
- Provides relevant context for different file types

### Project-Specific Guidance
- Instructions are tailored to the specific project
- Maintains framework consistency across the codebase
- Provides clear guidance for different development scenarios
- Ensures quality and maintainability standards

## Success Criteria

The GitHub Copilot adaptation is successful when:
- The `copilot-instructions.md` file is created in `.github/` directory
- Content preserves 100% of generic framework functionality
- Format follows GitHub Copilot's contextual instruction approach
- Instructions are actionable, clear, and well-organized
- No external dependencies or references exist
- Framework functionality is identical to other IDE adaptations 