# AI Epic Framework - Cline Rules

## AI Context Header
**When To Use**: Load as primary navigation hub for accessing other framework documentation. Use for conditional loading decisions and optimizing context window usage. Keep loaded throughout session.

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
