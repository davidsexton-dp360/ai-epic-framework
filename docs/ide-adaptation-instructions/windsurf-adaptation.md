# Windsurf Adaptation Instructions

## Overview
This document provides detailed instructions for adapting the AI Epic Framework to Windsurf's memories and rules system. Windsurf uses `.windsurfrules` files with concise rules and supports activation modes.

## Windsurf Format Requirements
- **File Extension**: `.windsurfrules`
- **Content Style**: Concise, bullet-point rules
- **Activation**: Can be activated for specific contexts
- **Structure**: Simple markdown with clear instructions

## Pre-Adaptation Setup

### Step 1: Clear Target Directory
```bash
# Remove existing content
rm -rf framework/windsurf-specific/*
```

### Step 2: Create Directory Structure
```bash
# Create the windsurf directory structure
mkdir -p framework/windsurf-specific
```

## Content Adaptation Process

### Step 1: Create Main Framework Rules File
Create `framework/windsurf-specific/.windsurfrules`:

```markdown
# AI Epic Framework - Windsurf Rules

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

## When To Use
- Load when creating new initiatives, epics, phases, or steps
- Use for task hierarchy questions, folder structure organization, or workflow management
- Apply when facing stubborn technical issues or complex system failures
- Use when designing new system architecture or making technical decisions

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

## Tool Usage Guidelines
- **Context7**: Use for library documentation and API references
- **Perplexity**: Use for research and information gathering
- **Web Search**: Use for current information and examples
- **File Operations**: Use appropriate tools for file management

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
```

## Validation Steps

### Step 1: File Structure Verification
```bash
# Verify file structure
ls -la framework/windsurf-specific/
```

Expected files:
- `.windsurfrules`

### Step 2: Content Verification
- Verify all generic content is preserved
- Check that content follows Windsurf's concise style
- Ensure no external dependencies or references
- Validate that all framework concepts are included

### Step 3: Format Verification
- Confirm file uses proper Markdown formatting
- Verify content is organized logically
- Check that rules are actionable and clear
- Ensure concise rule format is maintained

## Windsurf Specific Features

### Concise Rule Format
- Rules are written in clear, actionable language
- Focus on practical guidance and examples
- Avoid unnecessary verbosity
- Maintain readability and usability

### Activation Modes
- Rules can be activated for specific contexts
- Supports conditional loading based on task requirements
- Maintains context efficiency
- Enables focused assistance

### Memory System
- Rules are stored in Windsurf's memory system
- Supports persistent context across sessions
- Enables learning and adaptation
- Maintains user preferences and patterns

## Success Criteria

The Windsurf adaptation is successful when:
- The `.windsurfrules` file is created with all framework content
- Content preserves 100% of generic framework functionality
- Format follows Windsurf's concise rule approach
- Rules are actionable, clear, and well-organized
- No external dependencies or references exist
- Framework functionality is identical to other IDE adaptations 