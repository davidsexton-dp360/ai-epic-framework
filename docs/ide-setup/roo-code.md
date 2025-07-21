# Roo Code Setup Guide

Roo Code is a VS Code extension that uses custom instructions and `.rooignore` files for AI assistance. This guide explains how to install and configure the AI Epic Framework for Roo Code's specific capabilities.

## 🎯 Overview

**Roo Code Features**:
- VS Code extension with 15.4k+ installs
- Custom instructions for AI behavior configuration
- `.rooignore` files for selective file inclusion/exclusion
- Project-level AI assistance
- Integration with VS Code's existing workflows

**Framework Benefits in Roo Code**:
- Seamless VS Code integration
- Project-scoped framework guidance
- Intelligent file handling with .rooignore
- Custom instruction-driven AI assistance

## 📁 Framework Structure

Your Roo Code adaptation includes:

```
framework/roo-code-specific/
├── custom-instructions.md               # Main framework guidance
├── .rooignore                          # File filtering configuration
├── framework-components/               # Individual component files
│   ├── epic-workflow-instructions.md   # Project workflow management
│   ├── problem-solving-framework.md    # Systematic troubleshooting
│   ├── architecture-design-process.md  # System design methodology
│   ├── architecture-lifecycle.md       # Documentation management
│   └── general-execution-standards.md  # Quality and execution protocols
└── README.md                          # Setup instructions
```

## 🚀 Installation

### Step 1: Install Roo Code Extension

**1. Install from VS Code Marketplace**:
- Open VS Code
- Go to Extensions (Ctrl+Shift+X)
- Search for "Roo Code"
- Install the extension
- Restart VS Code if needed

**2. Verify Installation**:
- Check that Roo Code appears in your extensions list
- Look for Roo Code commands in the Command Palette (Ctrl+Shift+P)

### Step 2: Copy Framework Files

**Copy Framework to Project**:
```bash
# Copy all framework files to your project root
cp framework/roo-code-specific/custom-instructions.md /path/to/your/project/
cp framework/roo-code-specific/.rooignore /path/to/your/project/

# Copy component files for reference
cp -r framework/roo-code-specific/framework-components/ /path/to/your/project/
```

### Step 3: Configure Roo Code

**1. Set Custom Instructions**:
- Open Command Palette (Ctrl+Shift+P)
- Run "Roo Code: Set Custom Instructions"
- Point to your `custom-instructions.md` file

**2. Verify .rooignore**:
- Ensure `.rooignore` is in your project root
- Roo Code will automatically use this file for context filtering

## 🎛️ Configuration

### Custom Instructions File

The `custom-instructions.md` serves as your main framework configuration:

```markdown
# AI Epic Framework for Roo Code

## Framework Overview
This project uses the AI Epic Framework for systematic project management, 
problem-solving, and architecture design. The framework provides intelligent 
context loading and structured workflows for consistent AI-assisted development.

## Core Framework Components

### Navigation Hub
This custom instructions file serves as the navigation hub, providing decision 
logic for loading appropriate framework components based on your queries.

### Available Components
- **Epic Workflow**: Project hierarchy and task management (Initiative → Epic → Phase → Step)
- **Problem Solving**: Systematic troubleshooting methodology for complex issues
- **Architecture Design**: Structured approach to system design and technology decisions
- **Architecture Lifecycle**: Documentation management and organization standards
- **General Execution**: Quality protocols and decision-making guidelines

## Decision Matrix: Component Loading Logic

### Epic Workflow Management
**Load When**:
- User mentions: "epic", "initiative", "project", "feature", "workflow"
- Planning new features or organizing project structure
- Creating task hierarchies or managing project phases
- Need for systematic project breakdown

**Reference**: framework-components/epic-workflow-instructions.md
**Apply**: Initiative → Epic → Phase → Step methodology with INDEX.md and REQUIREMENTS.md templates

### Problem Solving Framework  
**Load When**:
- User mentions: "debug", "problem", "troubleshoot", "investigate"
- 3+ failed solution attempts mentioned
- Multi-component system failures
- Complex technical issues requiring systematic analysis

**Reference**: framework-components/problem-solving-framework.md
**Apply**: Systematic investigation workflow with evidence collection and root cause analysis

### Architecture Design Process
**Load When**:
- User mentions: "architecture", "design", "component", "system"
- Planning new systems or major refactoring
- Technology evaluation or selection needed
- API design or service boundaries

**Reference**: framework-components/architecture-design-process.md
**Apply**: Requirements gathering, technology research, and quality attribute design

### Architecture Lifecycle Management
**Load When**:
- User mentions: "documentation", "lifecycle", "maintain", "organize"
- Managing architecture documentation
- Document categorization or organization
- Architecture knowledge management

**Reference**: framework-components/architecture-lifecycle.md
**Apply**: Document categorization, size management, and update processes

### General Execution Standards
**Load When**:
- User mentions: "review", "quality", "standards", "best practices"
- Code review activities
- Quality assurance requirements
- Research and validation protocols

**Reference**: framework-components/general-execution-standards.md
**Apply**: Quality protocols, research methodologies, and decision-making guidelines

## Usage Instructions

### Component Selection
Based on your query, I will:
1. Analyze keywords and context to identify relevant framework components
2. Load appropriate methodology from the identified component
3. Apply structured approach to your specific request
4. Reference detailed component files when needed

### Explicit Component Usage
For optimal results, specify which component you want to use:
- "Using Epic Workflow, help me break down this feature..."
- "Following our Problem Solving Framework, help me debug..."
- "According to our Architecture Design process, how should I..."

### Framework Application
- Always apply systematic approaches from the framework
- Use structured templates and methodologies
- Document decisions and rationale
- Maintain consistency with framework principles

## Project Context
[Customize this section for your specific project]

### Technology Stack
- Languages: [Your programming languages]
- Frameworks: [Your frameworks and libraries]
- Database: [Your database systems]
- Infrastructure: [Your deployment and infrastructure]

### Team Practices
- Methodology: [Agile/Scrum/Kanban/etc.]
- Sprint Length: [Your sprint duration]
- Review Process: [Your code review practices]
- Quality Gates: [Your quality requirements]

### Quality Standards
- Code Style: [Your coding standards]
- Testing: [Your testing requirements]
- Documentation: [Your documentation standards]
- Performance: [Your performance criteria]

## Integration with Roo Code
- Use .rooignore to control which files are included in AI context
- Reference framework-components/ files for detailed methodologies
- Apply decision matrix logic for consistent component selection
- Leverage VS Code integration for seamless workflow management
```

### .rooignore Configuration

The `.rooignore` file controls which files Roo Code includes in AI context:

```gitignore
# AI Epic Framework - Roo Code Context Filter

# Include framework components
!framework-components/
!custom-instructions.md

# Exclude large or irrelevant files
node_modules/
.git/
*.log
*.tmp
dist/
build/
coverage/

# Exclude sensitive files
.env
.env.*
secrets/
*.key
*.pem

# Include important project files
!README.md
!package.json
!tsconfig.json
!*.config.js

# Include source code
!src/
!lib/
!components/
!pages/
!api/

# Include tests
!test/
!tests/
!__tests__/
!*.test.*
!*.spec.*

# Include documentation
!docs/
!*.md

# Exclude temporary framework files
investigation/
temp-analysis/
debug-files/

# Custom project exclusions
# Add your project-specific exclusions here
```

## 🎯 Usage Patterns

### Framework-Driven Development

**1. Feature Development Workflow**:
```
Developer: "Using Epic Workflow, I need to implement user authentication"

Roo Code Response:
1. Applies Epic Workflow methodology
2. Suggests Initiative → Epic → Phase → Step breakdown
3. Provides INDEX.md and REQUIREMENTS.md templates
4. References framework-components/epic-workflow-instructions.md
```

**2. Problem Solving Workflow**:
```
Developer: "I have a performance issue I can't solve after multiple attempts"

Roo Code Response:  
1. Recognizes 3+ failed attempts trigger
2. Applies Problem Solving Framework
3. Guides systematic investigation process
4. References framework-components/problem-solving-framework.md
```

**3. Architecture Design Workflow**:
```
Developer: "I need to design a new microservice for notifications"

Roo Code Response:
1. Applies Architecture Design Process
2. Guides requirements gathering and technology evaluation
3. Considers quality attributes and integration patterns
4. References framework-components/architecture-design-process.md
```

### VS Code Integration Benefits

**1. File Context Management**:
- `.rooignore` automatically filters relevant files
- Framework components available when referenced
- Project-specific context maintained

**2. Command Integration**:
- Use VS Code commands to trigger framework guidance
- Integrated with existing VS Code workflows
- Custom instructions apply to all Roo Code interactions

**3. Project Scope**:
- Framework applies to entire VS Code workspace
- Consistent guidance across all files and features
- Team-wide consistency when shared

## 🔧 Customization for Roo Code

### Project-Specific Adaptations

**Technology Stack Customization**:
```markdown
## Project Context (Update in custom-instructions.md)

### Our Tech Stack
- **Frontend**: React 18 + TypeScript + Tailwind CSS
- **Backend**: Node.js + Express + PostgreSQL
- **Testing**: Jest + React Testing Library
- **Deployment**: Docker + AWS ECS

### Our Standards
- **Code Style**: ESLint + Prettier configuration
- **Testing**: 80% code coverage requirement
- **Performance**: <100ms API response times
- **Security**: OWASP Top 10 compliance
```

**Team Workflow Integration**:
```markdown
## Team Development Process (Update in custom-instructions.md)

### Sprint Process
1. Features planned using Epic Workflow methodology
2. Complex issues require Problem Solving Framework documentation
3. Architecture changes need Architecture Design Process approval
4. All code must pass General Execution Standards review

### Review Process
- All PRs require framework compliance check
- Architecture decisions documented with rationale
- Problem investigations documented for knowledge sharing
```

### .rooignore Optimization

**Performance Optimization**:
```gitignore
# Optimize for faster AI processing
# Exclude large generated files
*.min.js
*.map
dist/
build/

# Exclude documentation that's not code-relevant
docs/images/
docs/videos/
*.pdf

# Include only relevant test files
!**/*.test.ts
!**/*.spec.ts
test-data/
fixtures/
```

**Security Considerations**:
```gitignore
# Ensure sensitive information is excluded
.env*
secrets/
keys/
certificates/
*.key
*.pem
*.p12

# Exclude local development files
.vscode/settings.json
.idea/
*.local
```

## 🎮 Practical Examples

### Example 1: Epic Planning with VS Code

**Scenario**: Planning a new e-commerce feature

**Steps**:
1. Open VS Code with Roo Code extension
2. Ask: "Using Epic Workflow, help me plan a shopping cart feature"
3. Roo Code applies framework methodology
4. Creates structured breakdown with templates
5. VS Code integration allows direct file creation

### Example 2: Debugging with Context

**Scenario**: Complex authentication issue

**Steps**:
1. `.rooignore` includes relevant auth files automatically
2. Ask: "Following Problem Solving Framework, this auth issue persists after multiple fixes"
3. Roo Code applies systematic investigation
4. Uses included files for better context understanding
5. Provides structured debugging approach

### Example 3: Architecture Review

**Scenario**: Reviewing API design

**Steps**:
1. Relevant architecture files included via `.rooignore`
2. Ask: "Using Architecture Design process, review this API structure"
3. Roo Code applies systematic review methodology
4. References existing architecture documentation
5. Provides structured feedback and recommendations

## 🔍 Troubleshooting

### Common Issues

**1. Custom Instructions Not Loading**:
```
Problem: Roo Code not applying framework guidance
Solution:
- Verify custom-instructions.md is properly set
- Check file path is correct
- Restart VS Code and Roo Code extension
- Ensure file is in proper markdown format
```

**2. .rooignore Not Working**:
```
Problem: Wrong files being included in context
Solution:
- Verify .rooignore is in project root
- Check .rooignore syntax (follows .gitignore format)
- Test with simple patterns first
- Restart Roo Code if needed
```

**3. Framework Components Not Referenced**:
```
Problem: Detailed methodology not being applied
Solution:
- Ensure framework-components/ directory exists
- Check component files are properly referenced
- Use explicit component mentions in queries
- Verify file paths in custom instructions
```

### Optimization Tips

**1. Context Management**:
- Regularly review and update .rooignore
- Include only relevant files for current work
- Use explicit framework component references
- Keep custom instructions current

**2. VS Code Integration**:
- Use Roo Code commands effectively
- Leverage VS Code workspace features
- Maintain consistent file organization
- Use VS Code settings for team consistency

**3. Team Coordination**:
- Share custom-instructions.md across team
- Maintain consistent .rooignore patterns
- Document any project-specific customizations
- Regular review of framework effectiveness

## 📊 Success Metrics

### Framework Effectiveness in Roo Code

**1. VS Code Integration**:
- Seamless workflow integration
- Effective file context management
- Consistent framework application

**2. Development Quality**:
- Structured approach to features and problems
- Improved code organization and documentation
- Better architectural decisions

**3. Team Benefits**:
- Shared framework understanding
- Consistent development patterns
- Improved knowledge transfer

## 📚 Additional Resources

### Roo Code Documentation
- [Roo Code VS Code Extension](https://marketplace.visualstudio.com/items?itemName=RooCode.roo-code)
- [Roo Code Documentation](https://docs.roocode.com/)
- [VS Code Extension Development](https://code.visualstudio.com/api)

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

**Ready to enhance your VS Code development with structured AI assistance?** Install the Roo Code extension, copy the framework files to your project, and configure the custom instructions for your specific needs. The framework will provide consistent guidance through VS Code's familiar interface. 