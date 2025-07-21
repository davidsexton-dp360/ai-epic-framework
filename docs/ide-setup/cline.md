# Cline Setup Guide

Cline is a VS Code extension that uses `.clinerules` files and custom instructions for AI assistance. This guide explains how to install and configure the AI Epic Framework for Cline's MCP (Model Context Protocol) integration and VS Code workflow.

## 🎯 Overview

**Cline Features**:
- VS Code extension with MCP (Model Context Protocol) support
- `.clinerules` files for AI behavior configuration
- Custom instructions for detailed guidance
- Project-level AI assistance with file context awareness
- Integration with VS Code's development environment

**Framework Benefits in Cline**:
- Native VS Code integration with familiar workflows
- MCP-enhanced context understanding
- Project-scoped framework guidance
- Intelligent file and context management

## 📁 Framework Structure

Your Cline adaptation includes:

```
framework/cline-specific/
├── .clinerules                         # Main Cline rules file
├── custom-instructions.md              # Detailed framework guidance
├── framework-components/               # Individual component files
│   ├── epic-workflow-instructions.md   # Project workflow management
│   ├── problem-solving-framework.md    # Systematic troubleshooting
│   ├── architecture-design-process.md  # System design methodology
│   ├── architecture-lifecycle.md       # Documentation management
│   └── general-execution-standards.md  # Quality and execution protocols
└── README.md                          # Setup instructions
```

## 🚀 Installation

### Step 1: Install Cline Extension

**1. Install from VS Code Marketplace**:
- Open VS Code
- Go to Extensions (Ctrl+Shift+X)
- Search for "Cline"
- Install the extension
- Restart VS Code if needed

**2. Verify Installation**:
- Check that Cline appears in your extensions list
- Look for Cline commands in the Command Palette (Ctrl+Shift+P)
- Verify MCP functionality is available

### Step 2: Copy Framework Files

**Copy Framework to Project**:
```bash
# Copy main configuration files to project root
cp framework/cline-specific/.clinerules /path/to/your/project/
cp framework/cline-specific/custom-instructions.md /path/to/your/project/

# Copy component files for reference
cp -r framework/cline-specific/framework-components/ /path/to/your/project/
```

### Step 3: Configure Cline

**1. Set Up .clinerules**:
- Ensure `.clinerules` is in your project root
- Cline automatically detects and loads this file

**2. Configure Custom Instructions**:
- Open Command Palette (Ctrl+Shift+P)
- Run "Cline: Set Custom Instructions"
- Point to your `custom-instructions.md` file

**3. Verify MCP Integration**:
- Test Cline's context awareness with framework files
- Ensure MCP is properly processing framework components

## 🎛️ Configuration

### .clinerules File

The `.clinerules` file provides core framework configuration:

```markdown
# AI Epic Framework for Cline

## Framework Overview
This project uses the AI Epic Framework for systematic project management, 
problem-solving, and architecture design. Apply framework methodologies 
consistently for better AI-assisted development.

## Core Framework Components
- Epic Workflow: Initiative → Epic → Phase → Step hierarchy
- Problem Solving: Systematic troubleshooting for complex issues  
- Architecture Design: Structured system design methodology
- Architecture Lifecycle: Documentation management and organization
- General Execution: Quality protocols and decision-making standards

## Decision Matrix: Component Loading
Based on user queries, apply appropriate framework component:

### Epic/Project Work
Keywords: epic, initiative, project, feature, workflow, planning
Apply: Epic Workflow methodology with hierarchical breakdown
Reference: framework-components/epic-workflow-instructions.md

### Problem Solving  
Keywords: debug, problem, troubleshoot, investigate, complex, failed
Apply: Problem Solving Framework for systematic investigation
Reference: framework-components/problem-solving-framework.md

### Architecture Design
Keywords: architecture, design, component, system, structure, API
Apply: Architecture Design Process for systematic design
Reference: framework-components/architecture-design-process.md

### Documentation Management
Keywords: documentation, lifecycle, organize, maintain, knowledge
Apply: Architecture Lifecycle methodology
Reference: framework-components/architecture-lifecycle.md

### Quality/Review Work
Keywords: review, quality, standards, best practices, execution
Apply: General Execution Standards
Reference: framework-components/general-execution-standards.md

## Usage Instructions
1. Analyze user query for framework component keywords
2. Load appropriate methodology from identified component  
3. Apply structured approach using framework templates
4. Reference detailed component files for complete methodology
5. Maintain consistency with framework principles

## MCP Integration
- Use MCP to understand project file context
- Apply framework principles to current codebase
- Reference framework components based on project needs
- Maintain awareness of epic structure and requirements

## Project Context
Tech Stack: [Customize with your technologies]
Team Practices: [Customize with your methodologies]  
Quality Standards: [Customize with your requirements]
```

### Custom Instructions File

The `custom-instructions.md` provides detailed framework guidance:

```markdown
# AI Epic Framework - Detailed Instructions for Cline

## Framework Philosophy
The AI Epic Framework provides systematic approaches to project management, 
problem-solving, and architecture design. When working with this codebase, 
always consider which framework component applies to the current task.

## Detailed Component Guidance

### Epic Workflow Management
**When to Apply**: Feature development, project planning, task organization

**Methodology**:
1. **Task Hierarchy**: Break work into Initiative → Epic → Phase → Step
2. **Documentation**: Use INDEX.md and REQUIREMENTS.md templates
3. **Structure**: Follow sequential numbering and clear ownership
4. **Progress Tracking**: Maintain status and dependency information

**Key Principles**:
- Each level has clear scope and deliverables
- Parent-child relationships maintain context
- Documentation templates ensure consistency
- Sequential execution with dependency management

### Problem Solving Framework
**When to Apply**: Complex debugging, multi-component issues, 3+ failed attempts

**Methodology**:
1. **Problem Definition**: Clear problem statement with impact assessment
2. **Investigation Planning**: Systematic approach with hypothesis formation
3. **Evidence Collection**: Structured data gathering and documentation
4. **Root Cause Analysis**: Systematic analysis using proven techniques
5. **Solution Design**: Comprehensive solution with prevention measures

**Key Principles**:
- Systematic investigation over ad-hoc debugging
- Evidence-based decision making
- Documentation for knowledge sharing
- Prevention focus, not just immediate fixes

### Architecture Design Process  
**When to Apply**: System design, major refactoring, technology decisions

**Methodology**:
1. **Requirements Gathering**: Functional and non-functional requirements
2. **Technology Research**: Evidence-based evaluation and selection
3. **High-Level Design**: System architecture and component relationships
4. **Detailed Design**: Component interfaces and implementation details
5. **Quality Attributes**: Performance, security, reliability design

**Key Principles**:
- Requirements-driven design decisions
- Evidence-based technology selection
- Quality attributes considered from start
- Comprehensive documentation of decisions

### Architecture Lifecycle Management
**When to Apply**: Documentation organization, knowledge management

**Methodology**:
1. **Document Organization**: Categorization and structure
2. **Size Management**: Breaking down large documents
3. **Update Processes**: Maintaining current documentation
4. **Discovery**: Making information findable

**Key Principles**:
- Living documentation that stays current
- Logical organization for easy discovery
- Appropriate granularity for maintainability
- Clear ownership and update responsibilities

### General Execution Standards
**When to Apply**: Code review, quality assurance, research activities

**Methodology**:
1. **File Navigation**: Systematic file verification and management
2. **Research Protocols**: Evidence-based decision making
3. **Quality Standards**: Consistent code and documentation quality
4. **Tool Usage**: Effective use of development tools

**Key Principles**:
- Evidence-based decision making
- Consistent quality standards
- Systematic approaches to all work
- Proper documentation and communication

## MCP Integration Guidelines

### File Context Awareness
- Use MCP to understand current file context
- Apply framework principles to specific code areas
- Reference epic structure when reviewing code
- Maintain awareness of architectural decisions

### Project Structure Understanding  
- Recognize epic directory structures
- Understand framework documentation organization
- Apply appropriate component based on file location
- Maintain consistency across project structure

### Context-Aware Assistance
- Tailor framework application to current context
- Reference relevant framework components automatically
- Provide structured guidance based on project state
- Maintain epic and phase context in recommendations

## Integration with VS Code Workflows

### File-Based Framework Application
- Apply Epic Workflow when working in epic directories
- Use Problem Solving when investigating complex issues
- Apply Architecture Design for system-level changes
- Reference quality standards during code review

### Command Integration
- Use framework templates for file creation
- Apply structured approaches through VS Code commands
- Maintain framework consistency in VS Code workflows
- Leverage MCP for intelligent framework application

## Team Coordination
- Share framework approaches across team members
- Maintain consistent epic structure and documentation
- Apply framework standards in all team interactions
- Use framework vocabulary for clear communication
```

## 🎯 Usage Patterns

### Framework-Driven Development with Cline

**1. Epic Planning Workflow**:
```
Developer: "Using Epic Workflow, help me plan user authentication feature"

Cline Response:
1. Applies Epic Workflow methodology
2. Suggests Initiative → Epic → Phase → Step breakdown
3. Provides INDEX.md and REQUIREMENTS.md templates
4. Uses MCP to understand current project context
5. References framework-components/epic-workflow-instructions.md
```

**2. Problem Investigation Workflow**:
```
Developer: "I have a complex database issue that persists after multiple fixes"

Cline Response:
1. Recognizes Problem Solving Framework trigger (multiple attempts)
2. Applies systematic investigation methodology
3. Guides evidence collection and hypothesis formation
4. Uses MCP to analyze relevant database files
5. References framework-components/problem-solving-framework.md
```

**3. Architecture Design Workflow**:
```
Developer: "Help me design a new API service using our architecture process"

Cline Response:
1. Applies Architecture Design Process methodology
2. Guides requirements gathering and technology research
3. Considers quality attributes and integration patterns
4. Uses MCP to understand existing architecture
5. References framework-components/architecture-design-process.md
```

### MCP-Enhanced Framework Features

**1. Context-Aware Component Selection**:
- MCP analyzes current file and project context
- Automatically suggests relevant framework components
- Provides context-specific framework guidance
- Maintains awareness of epic and phase structure

**2. Intelligent File Management**:
- MCP understands framework directory structures
- Suggests appropriate file locations for epic work
- Maintains consistency with framework organization
- Tracks relationships between framework components

**3. Code-Framework Integration**:
- Links code changes to epic requirements
- Applies architecture decisions to implementation
- Maintains traceability between framework and code
- Suggests framework-compliant code organization

## 🔧 Customization for Cline

### Project-Specific Configuration

**Update .clinerules for Your Project**:
```markdown
## Project Context (Customize this section)
Tech Stack: React + TypeScript + Node.js + PostgreSQL
Architecture: Microservices with REST APIs
Team Practices: Agile with 2-week sprints
Quality Gates: ESLint + Jest + TypeScript strict mode

## Framework Application for Our Project
- All features follow Epic Workflow structure
- Complex issues use Problem Solving Framework
- API design follows Architecture Design Process  
- Code reviews apply General Execution Standards
```

**Custom Instructions Enhancement**:
```markdown
## Project-Specific Framework Guidelines

### Our Epic Structure
- Initiatives align with quarterly OKRs
- Epics represent user-facing features
- Phases are sprint-sized deliverables
- Steps are individual developer tasks

### Our Quality Standards
- TypeScript strict mode required
- 80% test coverage for all code
- Architecture decisions documented as ADRs
- All APIs follow OpenAPI specifications
```

### VS Code Integration Optimization

**Workspace Settings for Framework**:
```json
{
  "cline.customInstructions": "./custom-instructions.md",
  "cline.rules": "./.clinerules",
  "files.exclude": {
    "**/node_modules": true,
    "**/investigation": false,
    "**/.epic-workflows": false
  },
  "files.associations": {
    ".clinerules": "markdown",
    "*.epic": "markdown"
  }
}
```

**File Templates Integration**:
```json
{
  "cline.templates": {
    "epic-index": "framework-components/templates/INDEX.md",
    "epic-requirements": "framework-components/templates/REQUIREMENTS.md",
    "problem-investigation": "framework-components/templates/investigation.md"
  }
}
```

## 🎮 Practical Examples

### Example 1: Feature Development with MCP

**Scenario**: Implementing shopping cart functionality

**Workflow**:
1. Cline recognizes epic structure using MCP
2. Applies Epic Workflow methodology
3. Suggests breaking into phases: cart logic, UI components, persistence
4. Provides templates for epic documentation
5. Maintains context awareness throughout development

### Example 2: Complex Debugging with Context

**Scenario**: Performance issue affecting multiple services

**Workflow**:
1. MCP analyzes affected files and services
2. Applies Problem Solving Framework
3. Guides systematic investigation across services
4. Documents evidence using framework templates
5. Provides structured resolution approach

### Example 3: Architecture Decision with File Context

**Scenario**: Choosing state management approach

**Workflow**:
1. MCP understands current React component structure
2. Applies Architecture Design Process
3. Evaluates options based on existing codebase
4. Considers quality attributes and team constraints
5. Documents decision with proper rationale

## 🔍 Troubleshooting

### Common Issues

**1. .clinerules Not Loading**:
```
Problem: Cline not applying framework rules
Solution:
- Verify .clinerules is in project root
- Check file syntax and formatting
- Restart VS Code and Cline extension
- Ensure file is not in .gitignore
```

**2. MCP Context Issues**:
```
Problem: Cline not understanding project context
Solution:
- Verify MCP is properly configured
- Check file permissions and accessibility
- Ensure framework files are in project
- Test with explicit file references
```

**3. Custom Instructions Not Applied**:
```
Problem: Detailed framework guidance not working
Solution:
- Verify custom-instructions.md path is correct
- Check file content and formatting
- Use Cline command to reset instructions
- Ensure file is accessible to extension
```

### Optimization Tips

**1. MCP Performance**:
- Keep framework files organized and accessible
- Use clear file naming for better context understanding
- Maintain reasonable project size for MCP processing
- Regular cleanup of temporary investigation files

**2. Framework Integration**:
- Be explicit about framework component usage
- Reference specific components in queries
- Maintain consistent framework vocabulary
- Update framework files based on team needs

**3. VS Code Workflow**:
- Use VS Code workspace settings for consistency
- Leverage file associations for framework files
- Maintain organized project structure
- Use VS Code tasks for framework automation

## 📊 Success Metrics

### Framework Effectiveness in Cline

**1. MCP Integration Quality**:
- Context-aware framework application
- Accurate component selection based on queries
- Proper understanding of project structure

**2. Development Efficiency**:
- Faster feature development with epic structure
- More effective problem solving with systematic approach
- Better architecture decisions with structured process

**3. Code Quality**:
- Consistent application of quality standards
- Better documentation and decision tracking
- Improved code organization and structure

## 📚 Additional Resources

### Cline Documentation
- [Cline VS Code Extension](https://marketplace.visualstudio.com/items?itemName=cline.cline)
- [Cline Documentation](https://docs.cline.bot/)
- [MCP (Model Context Protocol)](https://docs.cline.bot/mcp)

### Framework Resources
- [Framework Overview](../framework-overview.md) - Complete framework understanding
- [Epic Workflow Guide](../epic-workflow-guide.md) - Detailed workflow implementation
- [Customization Guide](../customization-guide.md) - Adapting for your needs

### Component References
- `framework-components/epic-workflow-instructions.md` - Complete workflow methodology
- `framework-components/problem-solving-framework.md` - Systematic troubleshooting
- `framework-components/architecture-design-process.md` - Design methodology
- `framework-components/architecture-lifecycle.md` - Documentation management
- `framework-components/general-execution-standards.md` - Quality standards

---

**Ready to enhance your VS Code development with MCP-powered framework guidance?** Install the Cline extension, copy the framework files to your project, and configure the rules and instructions for your specific development needs. The MCP integration will provide intelligent, context-aware framework assistance throughout your development workflow. 