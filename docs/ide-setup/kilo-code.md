# Kilo Code Setup Guide

Kilo Code is an open source VS Code extension that provides AI assistance with customizable rules and instructions. This guide explains how to configure the AI Epic Framework for Kilo Code's open source approach and VS Code integration.

## 🎯 Overview

**Kilo Code Features**:
- Open source VS Code extension
- Customizable AI behavior through rules and instructions
- Local and cloud AI model support
- Privacy-focused development assistance
- Community-driven development and extensions

**Framework Benefits in Kilo Code**:
- Open source framework integration
- Privacy-focused systematic development
- Customizable AI assistance for complex applications
- VS Code native integration with framework structure

## 📁 Framework Structure

Your Kilo Code adaptation includes:

```
framework/kilo-code-specific/
├── kilo-rules.json                      # Main Kilo Code rules configuration
├── custom-instructions.md               # Detailed framework guidance
├── framework-components/                # Individual component files
│   ├── epic-workflow-instructions.md   # Project workflow management
│   ├── problem-solving-framework.md    # Systematic troubleshooting
│   ├── architecture-design-process.md  # System design methodology
│   ├── architecture-lifecycle.md       # Documentation management
│   └── general-execution-standards.md  # Quality and execution protocols
├── vscode-settings.json                 # VS Code workspace integration
└── README.md                           # Setup instructions
```

## 🚀 Installation

### Step 1: Install Kilo Code Extension

**1. Install from VS Code Marketplace**:
- Open VS Code
- Go to Extensions (Ctrl+Shift+X)
- Search for "Kilo Code"
- Install the extension
- Restart VS Code if needed

**2. Verify Installation**:
- Check that Kilo Code appears in your extensions list
- Look for Kilo Code commands in the Command Palette (Ctrl+Shift+P)
- Verify extension is active and ready

### Step 2: Copy Framework Files

**Copy Framework to Project**:
```bash
# Copy all framework files to your project root
cp framework/kilo-code-specific/kilo-rules.json /path/to/your/project/
cp framework/kilo-code-specific/custom-instructions.md /path/to/your/project/

# Copy component files for reference
cp -r framework/kilo-code-specific/framework-components/ /path/to/your/project/

# Copy VS Code settings
cp framework/kilo-code-specific/vscode-settings.json /path/to/your/project/.vscode/settings.json
```

### Step 3: Configure Kilo Code

**1. Set Rules Configuration**:
- Open Command Palette (Ctrl+Shift+P)
- Run "Kilo Code: Load Rules File"
- Select your `kilo-rules.json` file

**2. Set Custom Instructions**:
- Open Command Palette (Ctrl+Shift+P)
- Run "Kilo Code: Set Custom Instructions"
- Point to your `custom-instructions.md` file

**3. Verify Framework Loading**:
- Test Kilo Code with framework-specific queries
- Ensure framework components are accessible
- Check VS Code workspace integration

## 🎛️ Configuration

### Main Rules File

The `kilo-rules.json` configures Kilo Code for framework usage:

```json
{
  "framework": {
    "name": "AI Epic Framework",
    "version": "1.0",
    "description": "Open source systematic approach to complex application development"
  },
  "rules": {
    "activation_patterns": {
      "epic_workflow": {
        "keywords": ["epic", "initiative", "project", "feature", "workflow", "planning"],
        "description": "Activate for complex project breakdown",
        "component_file": "framework-components/epic-workflow-instructions.md"
      },
      "problem_solving": {
        "keywords": ["debug", "problem", "troubleshoot", "investigate", "complex", "failed"],
        "description": "Activate for systematic problem investigation", 
        "component_file": "framework-components/problem-solving-framework.md"
      },
      "architecture_design": {
        "keywords": ["architecture", "design", "component", "system", "structure", "technology"],
        "description": "Activate for architectural decision making",
        "component_file": "framework-components/architecture-design-process.md"
      },
      "execution_standards": {
        "keywords": ["review", "quality", "standards", "best", "practices", "execution"],
        "description": "Activate for quality and standards guidance",
        "component_file": "framework-components/general-execution-standards.md"
      }
    },
    "behavior": {
      "auto_component_loading": true,
      "context_optimization": true,
      "privacy_mode": true,
      "open_source_preferred": true
    },
    "vscode_integration": {
      "workspace_awareness": true,
      "file_context": true,
      "terminal_integration": true,
      "task_integration": true
    }
  },
  "customization": {
    "project_specific": true,
    "team_shareable": true,
    "version_controlled": true,
    "extensible": true
  }
}
```

### Custom Instructions File

The `custom-instructions.md` provides detailed framework guidance:

```markdown
# AI Epic Framework for Kilo Code

## Framework Philosophy
You are using the open source AI Epic Framework to provide systematic, privacy-focused AI assistance for complex application development. Apply framework components based on developer needs while respecting open source principles.

## Component Loading Strategy

### Epic Workflow Management
**When to Activate**: Developer mentions large features, complex projects, or application planning
**VS Code Integration**: Create epic directory structure, workspace files, task definitions
**Open Source Focus**: Use open source project management patterns and tools

**Application Strategy**:
1. Break down complex applications into Initiative → Epic → Phase → Step hierarchy
2. Create VS Code workspace-compatible epic structure
3. Integrate with VS Code tasks and terminal for epic management
4. Provide open source project templates and patterns

### Problem Solving Framework
**When to Activate**: Developer has stubborn technical issues, multiple failed attempts, or complex debugging needs
**VS Code Integration**: Use VS Code debugging tools, terminal integration, extension ecosystem
**Open Source Focus**: Leverage open source debugging tools and community solutions

**Application Strategy**:
1. Apply systematic investigation methodology
2. Use VS Code debugging capabilities and extensions
3. Leverage open source troubleshooting tools and resources
4. Document findings in VS Code-compatible formats

### Architecture Design Process
**When to Activate**: Developer needs system design, technology choices, or architectural decisions
**VS Code Integration**: Create architecture documentation, diagrams, decision records
**Open Source Focus**: Recommend open source technologies and architectural patterns

**Application Strategy**:
1. Guide requirements-driven architectural decision making
2. Evaluate open source technology options systematically
3. Create VS Code-compatible architecture documentation
4. Support open source architectural patterns and best practices

### General Execution Standards
**When to Activate**: Developer needs code quality, review processes, or best practices guidance
**VS Code Integration**: Integrate with VS Code linting, formatting, and review tools
**Open Source Focus**: Apply open source quality standards and community practices

**Application Strategy**:
1. Apply systematic quality protocols
2. Use VS Code quality extensions and tools
3. Follow open source community standards and practices
4. Support open source development workflows

## Privacy and Open Source Principles
- Respect developer privacy and data ownership
- Prefer open source solutions and technologies
- Support community-driven development practices
- Maintain transparency in AI assistance approaches
- Enable local development and offline capabilities where possible

## VS Code Integration Guidelines
- Leverage VS Code's native capabilities for epic management
- Use workspace settings for framework configuration
- Integrate with VS Code task system for epic phases
- Support VS Code extension ecosystem for enhanced functionality
- Maintain compatibility with VS Code's file management and navigation
```

### VS Code Workspace Integration

The `vscode-settings.json` enhances VS Code integration:

```json
{
  "kiloCode.framework.enabled": true,
  "kiloCode.framework.rulesFile": "./kilo-rules.json",
  "kiloCode.framework.instructionsFile": "./custom-instructions.md",
  
  "files.associations": {
    "kilo-rules.json": "jsonc",
    "*.epic": "markdown",
    "INDEX.md": "markdown",
    "REQUIREMENTS.md": "markdown"
  },
  
  "tasks": {
    "version": "2.0.0",
    "tasks": [
      {
        "label": "Create Epic Structure",
        "type": "shell",
        "command": "mkdir",
        "args": ["-p", ".epic-workflows/tasks/${input:initiative}/${input:epic}"],
        "group": "build",
        "presentation": {
          "echo": true,
          "reveal": "always",
          "focus": false,
          "panel": "shared"
        }
      },
      {
        "label": "Start Problem Investigation",
        "type": "shell", 
        "command": "mkdir",
        "args": ["-p", "investigation/${input:problemName}"],
        "group": "build"
      }
    ]
  },
  
  "inputs": [
    {
      "id": "initiative",
      "description": "Initiative name",
      "default": "INITIATIVE_01",
      "type": "promptString"
    },
    {
      "id": "epic",
      "description": "Epic name", 
      "default": "EPIC_01_FEATURE_NAME",
      "type": "promptString"
    },
    {
      "id": "problemName",
      "description": "Problem investigation name",
      "default": "performance_issue",
      "type": "promptString"
    }
  ],
  
  "kiloCode.privacy": {
    "localProcessing": true,
    "dataMinimization": true,
    "noTelemetry": true
  }
}
```

## 🎯 Usage Patterns

### Framework-Driven Development with Kilo Code

**1. Epic Planning Workflow**:
```
Developer: "Using Epic Workflow, help me plan a social media application"

Kilo Code Response:
1. Activates Epic Workflow component from framework rules
2. Creates VS Code workspace-compatible epic structure
3. Sets up VS Code tasks for epic management
4. Provides open source technology recommendations
5. References framework-components/epic-workflow-instructions.md
```

**2. Problem Investigation Workflow**:
```
Developer: "I have a complex authentication bug that persists after multiple fixes"

Kilo Code Response:
1. Recognizes Problem Solving Framework trigger
2. Applies systematic investigation methodology
3. Uses VS Code debugging and terminal integration
4. Suggests open source debugging tools and techniques
5. References framework-components/problem-solving-framework.md
```

**3. Architecture Design Workflow**:
```
Developer: "Help me choose between different state management approaches"

Kilo Code Response:
1. Activates Architecture Design Process
2. Guides requirements-driven technology evaluation
3. Focuses on open source state management solutions
4. Creates VS Code-compatible architecture documentation
5. References framework-components/architecture-design-process.md
```

### Open Source Development Benefits

**1. Privacy-Focused Framework Usage**:
- Local processing capabilities respect developer privacy
- Framework guidance doesn't require external data transmission
- Open source principles applied to technology recommendations
- Community-driven best practices integrated into framework

**2. VS Code Native Integration**:
- Framework leverages VS Code's built-in capabilities
- Epic structure integrates with VS Code workspace management
- Problem-solving uses VS Code debugging and extension ecosystem
- Architecture decisions documented using VS Code-native formats

**3. Community Extensibility**:
- Framework rules can be customized and shared
- Open source extensions enhance framework capabilities
- Community contributions improve framework effectiveness
- Version-controlled framework evolution

## 🔧 Customization for Kilo Code

### Project-Specific Configuration

**Update Rules for Your Project**:
```json
{
  "project_context": {
    "name": "My Web Application",
    "tech_stack": "React + Node.js + PostgreSQL",
    "architecture": "Single Page Application with REST API",
    "team_size": 4,
    "development_approach": "Agile with open source tools"
  },
  "customizations": {
    "epic_structure": {
      "initiative_naming": "PROJECT_${quarter}_${goal}",
      "epic_templates": "web_application_epics",
      "phase_size": "sprint_sized"
    },
    "problem_solving": {
      "debugging_tools": ["VS Code debugger", "Chrome DevTools", "Node Inspector"],
      "investigation_format": "github_issue_template"
    },
    "architecture": {
      "preferred_patterns": ["component_architecture", "REST_APIs", "responsive_design"],
      "technology_focus": "open_source_first"
    }
  }
}
```

**Open Source Technology Preferences**:
```json
{
  "technology_preferences": {
    "frontend": {
      "frameworks": ["React", "Vue.js", "Svelte"],
      "build_tools": ["Vite", "Webpack", "Parcel"],
      "testing": ["Jest", "Vitest", "Cypress"]
    },
    "backend": {
      "runtime": ["Node.js", "Deno", "Python"],
      "databases": ["PostgreSQL", "MongoDB", "SQLite"],
      "web_servers": ["Express", "Fastify", "Koa"]
    },
    "devops": {
      "containers": ["Docker", "Podman"],
      "ci_cd": ["GitHub Actions", "GitLab CI", "Jenkins"],
      "monitoring": ["Prometheus", "Grafana", "ELK Stack"]
    }
  }
}
```

### VS Code Workspace Enhancement

**Enhanced Tasks Configuration**:
```json
{
  "tasks": {
    "version": "2.0.0",
    "tasks": [
      {
        "label": "Framework: Start Epic",
        "type": "shell",
        "command": "echo",
        "args": ["Starting Epic: ${input:epicName}"],
        "dependsOn": ["Create Epic Structure", "Initialize Epic Documentation"],
        "group": {
          "kind": "build",
          "isDefault": true
        }
      },
      {
        "label": "Framework: Investigation Mode",
        "type": "shell",
        "command": "code",
        "args": ["investigation/${input:problemName}/problem-definition.md"],
        "dependsOn": "Start Problem Investigation"
      },
      {
        "label": "Framework: Architecture Review",
        "type": "shell",
        "command": "code", 
        "args": ["docs/architecture/decisions/"]
      }
    ]
  }
}
```

## 🎮 Practical Examples

### Example 1: Open Source Epic Development

**Scenario**: Building an open source task management application

**VS Code Workflow**:
```
# Epic planning using VS Code tasks
Ctrl+Shift+P > Tasks: Run Task > Framework: Start Epic

Developer: "Using Epic Workflow, plan an open source task manager"

Kilo Code: "Creating epic structure for open source development:

Initiative: Open Source Task Manager
├── Epic 1: Core Task Management (using open source patterns)
├── Epic 2: User Authentication (OAuth with passport.js)
├── Epic 3: Real-time Updates (Socket.io integration)
└── Epic 4: Data Persistence (PostgreSQL with Sequelize)

VS Code workspace configured with:
- Epic directories in .epic-workflows/
- Open source technology focus
- Community contribution guidelines
- Privacy-respecting development practices"
```

### Example 2: Privacy-Focused Problem Solving

**Scenario**: Performance issue investigation with privacy considerations

**VS Code Workflow**:
```
# Start investigation using framework
Ctrl+Shift+P > Tasks: Run Task > Framework: Investigation Mode

Developer: "Complex performance issue in React app, tried multiple optimizations"

Kilo Code: "Applying Problem Solving Framework with privacy focus:

Investigation Strategy:
1. Local performance profiling (no data sent externally)
2. VS Code debugging with React Developer Tools
3. Local network analysis and monitoring
4. Component profiling using open source tools

Evidence Collection:
- Browser performance timeline (locally stored)
- React component render analysis
- Bundle analysis with webpack-bundle-analyzer
- Memory profiling with VS Code debugger

This keeps all investigation data local while applying systematic methodology."
```

### Example 3: Open Source Architecture Design

**Scenario**: Choosing between open source state management solutions

**VS Code Workflow**:
```
# Architecture review using framework
Ctrl+Shift+P > Tasks: Run Task > Framework: Architecture Review

Developer: "Help me choose between Redux, Zustand, and Valtio for state management"

Kilo Code: "Applying Architecture Design Process with open source focus:

Requirements Analysis:
- Application complexity and state needs
- Team expertise and learning curve
- Bundle size and performance requirements
- Community support and maintenance

Open Source Evaluation:
1. Redux: Mature ecosystem, extensive tooling, larger bundle
2. Zustand: Lightweight, TypeScript-first, growing community  
3. Valtio: Proxy-based, minimal boilerplate, newer approach

Technology Decision Matrix:
[Evaluates based on your specific requirements]

Recommendation: [Based on systematic analysis]
Implementation Plan: [VS Code-compatible setup steps]"
```

## 🔍 Troubleshooting

### Common Issues

**1. Rules File Not Loading**:
```
Problem: Kilo Code not applying framework rules
Solution:
- Verify kilo-rules.json is in project root
- Check JSON syntax and formatting
- Use Command Palette to reload rules file
- Restart VS Code and Kilo Code extension
```

**2. VS Code Integration Issues**:
```
Problem: Framework not integrating with VS Code features
Solution:
- Check vscode-settings.json is in .vscode/ directory
- Verify task definitions are properly configured
- Test VS Code tasks independently
- Check file associations and workspace settings
```

**3. Component Loading Problems**:
```
Problem: Framework components not accessible
Solution:
- Verify framework-components/ directory exists
- Check component file paths in rules configuration
- Test component loading with explicit references
- Ensure component files are valid markdown
```

### Optimization Tips

**1. Open Source Workflow**:
- Use open source VS Code extensions that complement the framework
- Configure framework to prefer open source technology recommendations
- Integrate with open source project management and documentation tools
- Maintain framework configuration in version control for team sharing

**2. Privacy Optimization**:
- Enable local processing mode in Kilo Code settings
- Configure framework to minimize external dependencies
- Use local debugging and analysis tools when possible
- Keep investigation data and documentation local

**3. VS Code Integration**:
- Set up custom keybindings for framework tasks
- Use VS Code snippets for common framework templates
- Configure workspace settings for optimal framework experience
- Integrate framework with VS Code's built-in Git support

## 📊 Success Metrics

### Framework Effectiveness in Kilo Code

**1. Open Source Integration**:
- Framework consistently recommends appropriate open source solutions
- Technology choices align with open source principles and community standards
- Development patterns support open source collaboration and contribution
- Privacy-focused approach maintains developer data ownership

**2. VS Code Native Experience**:
- Framework integrates seamlessly with VS Code workflows
- Epic structure works naturally with VS Code project management
- Problem solving leverages VS Code debugging and extension capabilities
- Architecture decisions are documented using VS Code-compatible formats

**3. Development Quality**:
- Systematic approach improves complex application development
- Framework guidance enhances VS Code development productivity
- Open source technology choices provide long-term sustainability
- Community-driven best practices improve code quality

## 📚 Additional Resources

### Kilo Code Documentation
- [Kilo Code Extension](https://marketplace.visualstudio.com/items?itemName=kilocode.kilocode) - VS Code marketplace
- [Kilo Code GitHub](https://github.com/kilocode/vscode-extension) - Open source repository
- [Kilo Code Configuration](https://github.com/kilocode/docs) - Configuration documentation

### Framework Resources
- [Framework Overview](../framework-overview.md) - Complete framework understanding
- [Epic Workflow Guide](../epic-workflow-guide.md) - Detailed workflow implementation
- [Customization Guide](../customization-guide.md) - Adapting for your needs

### Open Source Development
- [Open Source Epic Patterns](../advanced/open-source-epics.md) - Open source project management
- [Privacy-Focused Development](../advanced/privacy-development.md) - Privacy-respecting development practices
- [Community Collaboration](../advanced/community-patterns.md) - Open source collaboration patterns

---

**Ready to enhance your VS Code development with open source systematic AI assistance?** Install Kilo Code, configure the framework rules, and experience privacy-focused framework guidance that respects open source principles and community standards. 