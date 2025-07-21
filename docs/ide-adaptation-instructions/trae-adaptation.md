# Trae Adaptation Instructions

## Overview
This document provides detailed instructions for adapting the AI Epic Framework to Trae's YAML configuration format. Trae uses YAML files for rules configuration with global, project, and workspace rule types.

## Trae Format Requirements
- **File Format**: YAML configuration files
- **Rule Types**: Global, project, and workspace rules
- **Content Style**: Structured YAML with conditions and instructions
- **Loading Order**: Global → Project → Workspace (workspace overrides)

## Pre-Adaptation Setup

### Step 1: Clear Target Directory
```bash
# Remove existing content
rm -rf framework/trae-specific/*
```

### Step 2: Create Directory Structure
```bash
# Create the trae directory structure
mkdir -p framework/trae-specific
```

## Content Adaptation Process

### Step 1: Create Main Framework Rules File
Create `framework/trae-specific/ai-epic-framework.yaml`:

```yaml
# AI Epic Framework - Trae Rules Configuration

version: "1.0"
name: "AI Epic Framework"
description: "Systematic approaches for AI assistants to help developers build complex applications"

rules:
  - name: "Framework Overview"
    description: "Core framework principles and methodologies"
    conditions:
      - file_pattern: "*.md"
      - file_pattern: "*.txt"
    instructions:
      - "The AI Epic Framework provides systematic approaches for AI assistants to help developers build complex applications through structured workflows, problem-solving methodologies, and architecture design processes"
      - "Use systematic problem-solving approaches for complex issues"
      - "Implement hierarchical task breakdown (Initiative → Epic → Phase → Step)"
      - "Apply research-first methodology for architecture decisions"
      - "Maintain comprehensive documentation and context management"
      - "Focus on AI framework application rather than generic engineering principles"

  - name: "Epic Workflow Management"
    description: "Task hierarchy and workflow management"
    conditions:
      - file_pattern: "INDEX.md"
      - file_pattern: "REQUIREMENTS.md"
      - directory_pattern: "Epic_*"
      - directory_pattern: "Phase_*"
      - directory_pattern: "Step_*"
    instructions:
      - "Break down complex projects into manageable epics"
      - "Use INDEX.md and REQUIREMENTS.md templates for task organization"
      - "Implement systematic delegation and execution flows"
      - "Maintain progress tracking and status management"
      - "Follow task hierarchy structure: Initiative/Epic_001_Task_Name/Phase_001_Phase_Name/Step_001_Step_Name/"
      - "Create INDEX.md with Overview, Status, Dependencies, Deliverables, and Notes sections"
      - "Create REQUIREMENTS.md with Functional Requirements, Technical Requirements, Acceptance Criteria, and Constraints sections"

  - name: "Problem Solving Framework"
    description: "Systematic analysis for stubborn technical issues"
    conditions:
      - file_pattern: "*.log"
      - file_pattern: "error*.md"
      - file_pattern: "debug*.md"
      - directory_pattern: "investigation*"
    instructions:
      - "Apply systematic analysis for stubborn technical issues"
      - "Use research-first approach before solution implementation"
      - "Document investigation processes and findings"
      - "Implement solution validation and verification"
      - "Follow systematic analysis process: Problem Identification → Research Phase → Root Cause Analysis → Solution Development → Implementation → Verification"
      - "Always research before implementing solutions"
      - "Use multiple information sources (documentation, examples, community)"
      - "Document findings and decision rationale"
      - "Validate assumptions through testing"
      - "Record all research steps and findings"
      - "Document failed attempts and lessons learned"
      - "Test solutions in isolated environments"
      - "Verify all requirements are met"

  - name: "Architecture Design Process"
    description: "Research methodology for architecture decisions"
    conditions:
      - file_pattern: "architecture*.md"
      - file_pattern: "design*.md"
      - file_pattern: "system*.md"
      - directory_pattern: "arch*"
      - directory_pattern: "design*"
    instructions:
      - "Follow research methodology for architecture decisions"
      - "Use component design templates and integration patterns"
      - "Implement quality attribute analysis and trade-off evaluation"
      - "Maintain architecture documentation lifecycle"
      - "Follow research methodology: Technology Evaluation → Requirement Analysis → Constraint Identification → Pattern Selection → Validation"
      - "Define service components with interfaces, responsibilities, and dependencies"
      - "Design data components with data models, storage, and access patterns"
      - "Plan integration components with communication protocols and APIs"
      - "Implement security components with authentication, authorization, and data protection"
      - "Consider quality attributes: Performance, Scalability, Reliability, Security, Maintainability"
      - "Use integration patterns: API-First Design, Event-Driven Architecture, Microservices, Data Consistency"

  - name: "Execution Standards"
    description: "File navigation and verification procedures"
    conditions:
      - file_pattern: "*.py"
      - file_pattern: "*.js"
      - file_pattern: "*.ts"
      - file_pattern: "*.java"
      - file_pattern: "*.go"
      - file_pattern: "*.rs"
    instructions:
      - "Follow file navigation and verification procedures"
      - "Use appropriate tools (Context7, Perplexity, Web search)"
      - "Implement decision-making protocols and documentation requirements"
      - "Maintain quality assurance and execution methodology"
      - "Always verify file existence before operations"
      - "Use appropriate tools for file discovery and search"
      - "Maintain organized directory structures"
      - "Document file relationships and dependencies"
      - "Use Context7 for library documentation and API references"
      - "Use Perplexity for research and information gathering"
      - "Use Web Search for current information and examples"
      - "Document decision rationale and alternatives considered"
      - "Use systematic evaluation criteria"
      - "Consider long-term implications and maintenance"
      - "Validate decisions through testing and feedback"
      - "Implement comprehensive testing strategies"
      - "Use code review and validation processes"
      - "Maintain documentation standards"
      - "Follow established coding conventions"

  - name: "Context Management"
    description: "Token optimization and context window management"
    conditions:
      - file_pattern: "*.md"
      - file_pattern: "*.txt"
      - directory_pattern: "docs*"
    instructions:
      - "Optimize token usage through conditional documentation loading"
      - "Use progressive disclosure for complex investigations"
      - "Maintain context window efficiency"
      - "Implement task-specific guidance systems"
      - "Load documentation conditionally based on task requirements"
      - "Use progressive disclosure for complex investigations"
      - "Prioritize active task information"
      - "Unload unnecessary context when possible"
      - "Load epic workflow instructions for workflow management"
      - "Load problem-solving framework for problem solving"
      - "Load architecture design process for architecture design"
      - "Load execution standards for general tasks"
      - "Monitor token usage and context window capacity"
      - "Prioritize essential information for current task"
      - "Use efficient information retrieval strategies"
      - "Maintain context continuity across sessions"
      - "Structure information hierarchically"
      - "Use clear categorization and tagging"
      - "Implement efficient search and retrieval"
      - "Maintain information currency and accuracy"

  - name: "Quality Attributes"
    description: "Performance, scalability, reliability, security, and maintainability"
    conditions:
      - file_pattern: "*.config.*"
      - file_pattern: "*.conf"
      - file_pattern: "dockerfile*"
      - file_pattern: "*.yml"
      - file_pattern: "*.yaml"
    instructions:
      - "Consider performance: Response time, throughput, and resource utilization"
      - "Consider scalability: Horizontal and vertical scaling capabilities"
      - "Consider reliability: Fault tolerance and error handling"
      - "Consider security: Data protection and access control"
      - "Consider maintainability: Code organization and documentation"
      - "Implement appropriate performance optimizations"
      - "Design for horizontal and vertical scaling"
      - "Implement fault tolerance and error handling"
      - "Ensure data protection and access control"
      - "Maintain code organization and documentation"

  - name: "Documentation Standards"
    description: "Clear and comprehensive documentation requirements"
    conditions:
      - file_pattern: "README*.md"
      - file_pattern: "*.md"
      - file_pattern: "docs/*.md"
    instructions:
      - "Create clear and comprehensive documentation"
      - "Use consistent formatting and structure"
      - "Include examples and use cases"
      - "Maintain up-to-date information"
      - "Follow the framework's documentation standards"
      - "Use consistent markdown formatting"
      - "Include practical examples and use cases"
      - "Keep documentation current and accurate"
      - "Follow established documentation patterns"
      - "Include troubleshooting and FAQ sections"

  - name: "Integration Patterns"
    description: "API-first design, event-driven architecture, microservices, and data consistency"
    conditions:
      - file_pattern: "api*.md"
      - file_pattern: "service*.md"
      - file_pattern: "*.proto"
      - file_pattern: "*.json"
    instructions:
      - "Use API-First Design: Design interfaces before implementation"
      - "Use Event-Driven Architecture: Use events for loose coupling"
      - "Use Microservices: Decompose into focused, independent services"
      - "Use Data Consistency: Implement appropriate consistency models"
      - "Design APIs before implementing functionality"
      - "Use events for loose coupling between components"
      - "Decompose systems into focused, independent services"
      - "Implement appropriate data consistency models"
      - "Define clear service boundaries and interfaces"
      - "Use appropriate communication protocols"

  - name: "Investigation and Validation"
    description: "Research documentation and solution validation"
    conditions:
      - file_pattern: "investigation*.md"
      - file_pattern: "research*.md"
      - file_pattern: "validation*.md"
      - file_pattern: "test*.md"
    instructions:
      - "Record all research steps and findings"
      - "Document failed attempts and lessons learned"
      - "Maintain context for future reference"
      - "Create reusable knowledge base entries"
      - "Test solutions in isolated environments"
      - "Verify all requirements are met"
      - "Document implementation steps"
      - "Create rollback procedures"
      - "Maintain comprehensive investigation logs"
      - "Document decision rationale and alternatives"
      - "Create test plans and validation procedures"
      - "Implement proper error handling and recovery"

  - name: "Coding Standards"
    description: "Framework-based coding standards and practices"
    conditions:
      - file_pattern: "*.py"
      - file_pattern: "*.js"
      - file_pattern: "*.ts"
      - file_pattern: "*.java"
      - file_pattern: "*.go"
      - file_pattern: "*.rs"
    instructions:
      - "Follow the framework's systematic approach to problem-solving"
      - "Implement proper documentation and context management"
      - "Use research-first methodology for complex decisions"
      - "Maintain quality attributes in all implementations"
      - "Focus on AI framework application rather than generic engineering principles"
      - "Use TypeScript for all new code when applicable"
      - "Write unit tests for business logic"
      - "Follow component naming conventions"
      - "Use established error handling patterns"
      - "Apply the AI Epic Framework systematically"
      - "Maintain code quality and readability"
      - "Follow language-specific best practices"
      - "Implement proper error handling and logging"
      - "Use appropriate design patterns"
      - "Maintain consistent coding style"
```

## Validation Steps

### Step 1: File Structure Verification
```bash
# Verify file structure
ls -la framework/trae-specific/
```

Expected files:
- `ai-epic-framework.yaml`

### Step 2: Content Verification
- Verify all generic content is preserved
- Check that content follows Trae's YAML format
- Ensure no external dependencies or references
- Validate that all framework concepts are included

### Step 3: Format Verification
- Confirm file uses proper YAML syntax
- Verify content is organized logically
- Check that rules are actionable and clear
- Ensure YAML structure is valid

## Trae Specific Features

### YAML Configuration
- Rules are defined in structured YAML format
- Supports conditions and instructions for each rule
- Enables precise targeting of specific file types and directories
- Provides clear rule organization and hierarchy

### Rule Types and Loading Order
- **Global Rules**: Applied to all projects
- **Project Rules**: Applied to specific project
- **Workspace Rules**: Applied to current workspace (overrides others)
- Loading order: Global → Project → Workspace

### Conditional Application
- Rules can be applied based on file patterns
- Directory patterns enable context-specific guidance
- File extensions trigger appropriate rule sets
- Enables precise framework application

## Success Criteria

The Trae adaptation is successful when:
- The `ai-epic-framework.yaml` file is created with all framework content
- Content preserves 100% of generic framework functionality
- Format follows Trae's YAML configuration approach
- Rules are actionable, clear, and well-organized
- YAML syntax is valid and properly structured
- No external dependencies or references exist
- Framework functionality is identical to other IDE adaptations 

## Overview
This document provides detailed instructions for adapting the AI Epic Framework to Trae's YAML configuration format. Trae uses YAML files for rules configuration with global, project, and workspace rule types.

## Trae Format Requirements
- **File Format**: YAML configuration files
- **Rule Types**: Global, project, and workspace rules
- **Content Style**: Structured YAML with conditions and instructions
- **Loading Order**: Global → Project → Workspace (workspace overrides)

## Pre-Adaptation Setup

### Step 1: Clear Target Directory
```bash
# Remove existing content
rm -rf framework/trae-specific/*
```

### Step 2: Create Directory Structure
```bash
# Create the trae directory structure
mkdir -p framework/trae-specific
```

## Content Adaptation Process

### Step 1: Create Main Framework Rules File
Create `framework/trae-specific/ai-epic-framework.yaml`:

```yaml
# AI Epic Framework - Trae Rules Configuration

version: "1.0"
name: "AI Epic Framework"
description: "Systematic approaches for AI assistants to help developers build complex applications"

rules:
  - name: "Framework Overview"
    description: "Core framework principles and methodologies"
    conditions:
      - file_pattern: "*.md"
      - file_pattern: "*.txt"
    instructions:
      - "The AI Epic Framework provides systematic approaches for AI assistants to help developers build complex applications through structured workflows, problem-solving methodologies, and architecture design processes"
      - "Use systematic problem-solving approaches for complex issues"
      - "Implement hierarchical task breakdown (Initiative → Epic → Phase → Step)"
      - "Apply research-first methodology for architecture decisions"
      - "Maintain comprehensive documentation and context management"
      - "Focus on AI framework application rather than generic engineering principles"

  - name: "Epic Workflow Management"
    description: "Task hierarchy and workflow management"
    conditions:
      - file_pattern: "INDEX.md"
      - file_pattern: "REQUIREMENTS.md"
      - directory_pattern: "Epic_*"
      - directory_pattern: "Phase_*"
      - directory_pattern: "Step_*"
    instructions:
      - "Break down complex projects into manageable epics"
      - "Use INDEX.md and REQUIREMENTS.md templates for task organization"
      - "Implement systematic delegation and execution flows"
      - "Maintain progress tracking and status management"
      - "Follow task hierarchy structure: Initiative/Epic_001_Task_Name/Phase_001_Phase_Name/Step_001_Step_Name/"
      - "Create INDEX.md with Overview, Status, Dependencies, Deliverables, and Notes sections"
      - "Create REQUIREMENTS.md with Functional Requirements, Technical Requirements, Acceptance Criteria, and Constraints sections"

  - name: "Problem Solving Framework"
    description: "Systematic analysis for stubborn technical issues"
    conditions:
      - file_pattern: "*.log"
      - file_pattern: "error*.md"
      - file_pattern: "debug*.md"
      - directory_pattern: "investigation*"
    instructions:
      - "Apply systematic analysis for stubborn technical issues"
      - "Use research-first approach before solution implementation"
      - "Document investigation processes and findings"
      - "Implement solution validation and verification"
      - "Follow systematic analysis process: Problem Identification → Research Phase → Root Cause Analysis → Solution Development → Implementation → Verification"
      - "Always research before implementing solutions"
      - "Use multiple information sources (documentation, examples, community)"
      - "Document findings and decision rationale"
      - "Validate assumptions through testing"
      - "Record all research steps and findings"
      - "Document failed attempts and lessons learned"
      - "Test solutions in isolated environments"
      - "Verify all requirements are met"

  - name: "Architecture Design Process"
    description: "Research methodology for architecture decisions"
    conditions:
      - file_pattern: "architecture*.md"
      - file_pattern: "design*.md"
      - file_pattern: "system*.md"
      - directory_pattern: "arch*"
      - directory_pattern: "design*"
    instructions:
      - "Follow research methodology for architecture decisions"
      - "Use component design templates and integration patterns"
      - "Implement quality attribute analysis and trade-off evaluation"
      - "Maintain architecture documentation lifecycle"
      - "Follow research methodology: Technology Evaluation → Requirement Analysis → Constraint Identification → Pattern Selection → Validation"
      - "Define service components with interfaces, responsibilities, and dependencies"
      - "Design data components with data models, storage, and access patterns"
      - "Plan integration components with communication protocols and APIs"
      - "Implement security components with authentication, authorization, and data protection"
      - "Consider quality attributes: Performance, Scalability, Reliability, Security, Maintainability"
      - "Use integration patterns: API-First Design, Event-Driven Architecture, Microservices, Data Consistency"

  - name: "Execution Standards"
    description: "File navigation and verification procedures"
    conditions:
      - file_pattern: "*.py"
      - file_pattern: "*.js"
      - file_pattern: "*.ts"
      - file_pattern: "*.java"
      - file_pattern: "*.go"
      - file_pattern: "*.rs"
    instructions:
      - "Follow file navigation and verification procedures"
      - "Use appropriate tools (Context7, Perplexity, Web search)"
      - "Implement decision-making protocols and documentation requirements"
      - "Maintain quality assurance and execution methodology"
      - "Always verify file existence before operations"
      - "Use appropriate tools for file discovery and search"
      - "Maintain organized directory structures"
      - "Document file relationships and dependencies"
      - "Use Context7 for library documentation and API references"
      - "Use Perplexity for research and information gathering"
      - "Use Web Search for current information and examples"
      - "Document decision rationale and alternatives considered"
      - "Use systematic evaluation criteria"
      - "Consider long-term implications and maintenance"
      - "Validate decisions through testing and feedback"
      - "Implement comprehensive testing strategies"
      - "Use code review and validation processes"
      - "Maintain documentation standards"
      - "Follow established coding conventions"

  - name: "Context Management"
    description: "Token optimization and context window management"
    conditions:
      - file_pattern: "*.md"
      - file_pattern: "*.txt"
      - directory_pattern: "docs*"
    instructions:
      - "Optimize token usage through conditional documentation loading"
      - "Use progressive disclosure for complex investigations"
      - "Maintain context window efficiency"
      - "Implement task-specific guidance systems"
      - "Load documentation conditionally based on task requirements"
      - "Use progressive disclosure for complex investigations"
      - "Prioritize active task information"
      - "Unload unnecessary context when possible"
      - "Load epic workflow instructions for workflow management"
      - "Load problem-solving framework for problem solving"
      - "Load architecture design process for architecture design"
      - "Load execution standards for general tasks"
      - "Monitor token usage and context window capacity"
      - "Prioritize essential information for current task"
      - "Use efficient information retrieval strategies"
      - "Maintain context continuity across sessions"
      - "Structure information hierarchically"
      - "Use clear categorization and tagging"
      - "Implement efficient search and retrieval"
      - "Maintain information currency and accuracy"

  - name: "Quality Attributes"
    description: "Performance, scalability, reliability, security, and maintainability"
    conditions:
      - file_pattern: "*.config.*"
      - file_pattern: "*.conf"
      - file_pattern: "dockerfile*"
      - file_pattern: "*.yml"
      - file_pattern: "*.yaml"
    instructions:
      - "Consider performance: Response time, throughput, and resource utilization"
      - "Consider scalability: Horizontal and vertical scaling capabilities"
      - "Consider reliability: Fault tolerance and error handling"
      - "Consider security: Data protection and access control"
      - "Consider maintainability: Code organization and documentation"
      - "Implement appropriate performance optimizations"
      - "Design for horizontal and vertical scaling"
      - "Implement fault tolerance and error handling"
      - "Ensure data protection and access control"
      - "Maintain code organization and documentation"

  - name: "Documentation Standards"
    description: "Clear and comprehensive documentation requirements"
    conditions:
      - file_pattern: "README*.md"
      - file_pattern: "*.md"
      - file_pattern: "docs/*.md"
    instructions:
      - "Create clear and comprehensive documentation"
      - "Use consistent formatting and structure"
      - "Include examples and use cases"
      - "Maintain up-to-date information"
      - "Follow the framework's documentation standards"
      - "Use consistent markdown formatting"
      - "Include practical examples and use cases"
      - "Keep documentation current and accurate"
      - "Follow established documentation patterns"
      - "Include troubleshooting and FAQ sections"

  - name: "Integration Patterns"
    description: "API-first design, event-driven architecture, microservices, and data consistency"
    conditions:
      - file_pattern: "api*.md"
      - file_pattern: "service*.md"
      - file_pattern: "*.proto"
      - file_pattern: "*.json"
    instructions:
      - "Use API-First Design: Design interfaces before implementation"
      - "Use Event-Driven Architecture: Use events for loose coupling"
      - "Use Microservices: Decompose into focused, independent services"
      - "Use Data Consistency: Implement appropriate consistency models"
      - "Design APIs before implementing functionality"
      - "Use events for loose coupling between components"
      - "Decompose systems into focused, independent services"
      - "Implement appropriate data consistency models"
      - "Define clear service boundaries and interfaces"
      - "Use appropriate communication protocols"

  - name: "Investigation and Validation"
    description: "Research documentation and solution validation"
    conditions:
      - file_pattern: "investigation*.md"
      - file_pattern: "research*.md"
      - file_pattern: "validation*.md"
      - file_pattern: "test*.md"
    instructions:
      - "Record all research steps and findings"
      - "Document failed attempts and lessons learned"
      - "Maintain context for future reference"
      - "Create reusable knowledge base entries"
      - "Test solutions in isolated environments"
      - "Verify all requirements are met"
      - "Document implementation steps"
      - "Create rollback procedures"
      - "Maintain comprehensive investigation logs"
      - "Document decision rationale and alternatives"
      - "Create test plans and validation procedures"
      - "Implement proper error handling and recovery"

  - name: "Coding Standards"
    description: "Framework-based coding standards and practices"
    conditions:
      - file_pattern: "*.py"
      - file_pattern: "*.js"
      - file_pattern: "*.ts"
      - file_pattern: "*.java"
      - file_pattern: "*.go"
      - file_pattern: "*.rs"
    instructions:
      - "Follow the framework's systematic approach to problem-solving"
      - "Implement proper documentation and context management"
      - "Use research-first methodology for complex decisions"
      - "Maintain quality attributes in all implementations"
      - "Focus on AI framework application rather than generic engineering principles"
      - "Use TypeScript for all new code when applicable"
      - "Write unit tests for business logic"
      - "Follow component naming conventions"
      - "Use established error handling patterns"
      - "Apply the AI Epic Framework systematically"
      - "Maintain code quality and readability"
      - "Follow language-specific best practices"
      - "Implement proper error handling and logging"
      - "Use appropriate design patterns"
      - "Maintain consistent coding style"
```

## Validation Steps

### Step 1: File Structure Verification
```bash
# Verify file structure
ls -la framework/trae-specific/
```

Expected files:
- `ai-epic-framework.yaml`

### Step 2: Content Verification
- Verify all generic content is preserved
- Check that content follows Trae's YAML format
- Ensure no external dependencies or references
- Validate that all framework concepts are included

### Step 3: Format Verification
- Confirm file uses proper YAML syntax
- Verify content is organized logically
- Check that rules are actionable and clear
- Ensure YAML structure is valid

## Trae Specific Features

### YAML Configuration
- Rules are defined in structured YAML format
- Supports conditions and instructions for each rule
- Enables precise targeting of specific file types and directories
- Provides clear rule organization and hierarchy

### Rule Types and Loading Order
- **Global Rules**: Applied to all projects
- **Project Rules**: Applied to specific project
- **Workspace Rules**: Applied to current workspace (overrides others)
- Loading order: Global → Project → Workspace

### Conditional Application
- Rules can be applied based on file patterns
- Directory patterns enable context-specific guidance
- File extensions trigger appropriate rule sets
- Enables precise framework application

## Success Criteria

The Trae adaptation is successful when:
- The `ai-epic-framework.yaml` file is created with all framework content
- Content preserves 100% of generic framework functionality
- Format follows Trae's YAML configuration approach
- Rules are actionable, clear, and well-organized
- YAML syntax is valid and properly structured
- No external dependencies or references exist
- Framework functionality is identical to other IDE adaptations 