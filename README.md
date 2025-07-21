# AI Epic Framework 🚀

A comprehensive, research-based framework for creating consistent AI prompts and rules that transforms how you work with AI coding assistants. Build better software faster with systematic workflows, intelligent context management, and proven architectural patterns.

## 🌟 What is the AI Epic Framework?

The AI Epic Framework is a **smart context management system** that helps you:

- **Break down complex projects** into manageable Initiative → Epic → Phase → Step hierarchies
- **Optimize AI interactions** through conditional documentation loading (saving tokens and improving responses)
- **Apply systematic approaches** to problem-solving, architecture design, and code quality
- **Maintain consistency** across teams and projects with standardized workflows
- **Work across 11+ AI IDEs** with purpose-built adaptations for each platform

## 🎯 Key Benefits

### ✅ **Structured Project Management**
Transform overwhelming projects into clear, actionable hierarchies:
```
Initiative: "E-commerce Platform"
├── Epic 1: "User Authentication System" 
│   ├── Phase 1: "OAuth Integration"
│   │   ├── Step 1: "Google OAuth Setup"
│   │   └── Step 2: "Login UI Components"
│   └── Phase 2: "User Profile Management"
└── Epic 2: "Payment Processing"
```

### ✅ **AI Token Efficiency**
Smart documentation loading means better AI responses:
- Load only relevant context for current tasks
- Preserve context window space for actual problem-solving
- Get more accurate, focused AI assistance

### ✅ **Systematic Problem Solving**
Research-driven troubleshooting workflow:
- Activates after 3+ failed attempts
- Structured investigation methodology  
- Temporary file management for complex debugging

### ✅ **Architecture Excellence**
Proven design processes and lifecycle management:
- Component design methodology
- Quality attribute considerations
- Documentation standards and templates

### ✅ **Universal IDE Support**
Works across **11 researched AI coding IDEs**:
- Cursor AI, Windsurf, GitHub Copilot, Claude Code, Cline, Roo Code, Kilo Code, and more
- Each with purpose-built adaptations matching their specific rule systems

## 🏗️ Core Framework Components

### 📋 **1. Epic Workflow Management**
**Purpose**: Structure large projects into manageable hierarchies  
**When to use**: Starting new projects, organizing complex features, team coordination

**Capabilities**:
- Initiative → Epic → Phase → Step breakdown
- Sequential numbering and clear task hierarchy
- INDEX.md and REQUIREMENTS.md templates
- Directory structure and naming conventions
- Delegation instructions and progress tracking

### 🔍 **2. Problem Solving Framework**  
**Purpose**: Systematic troubleshooting for complex technical issues  
**When to use**: After 3+ failed attempts, multi-component failures, explicit debugging needs

**Capabilities**:
- Research-driven investigation workflow
- Component analysis methodology
- Temporary file management for debugging
- Integration with architecture design patterns

### ⚙️ **3. Architecture Design Process**
**Purpose**: Structured approach to system design and component architecture  
**When to use**: New systems, major refactors, architectural decisions

**Capabilities**:
- Research methodology for technical decisions
- Component design and integration patterns
- Quality attribute considerations (performance, security, scalability)
- Review and validation procedures

### 📚 **4. Architecture Lifecycle Management**
**Purpose**: Organize and maintain architecture documentation  
**When to use**: System design, documentation management, knowledge sharing

**Capabilities**:
- Document categorization and organization
- Size limits and breakdown strategies
- Update and deprecation processes
- Discovery and search patterns

### 🎛️ **5. General Execution Standards**
**Purpose**: Quality protocols and decision-making guidelines  
**When to use**: Code reviews, research activities, maintaining standards

**Capabilities**:
- File navigation and verification procedures
- Tool usage guidelines (Context7, web search, etc.)
- Research protocols and quality standards
- Documentation requirements

### 🧭 **6. User Rules Template** (Navigation Hub)
**Purpose**: Smart context loading and framework navigation  
**When to use**: Always loaded - serves as the main navigation and decision matrix

**Capabilities**:
- Conditional documentation loading based on task context
- Decision matrix for choosing relevant frameworks
- Token efficiency optimization
- Progressive disclosure strategies

## 🎮 Real-World Use Cases

### 🏢 **Large Enterprise Project**
**Scenario**: Building a customer portal with multiple teams
```
Initiative: "Customer Portal Modernization"
├── Epic 1: "Authentication & Authorization"  
├── Epic 2: "Data Migration from Legacy Systems"
├── Epic 3: "New Dashboard UI/UX"
└── Epic 4: "API Gateway Implementation"
```

**Framework Application**:
- **Epic Workflow**: Structure and track progress across teams
- **Architecture Design**: Plan API gateway and data flow
- **Problem Solving**: Debug complex legacy integration issues
- **Execution Standards**: Maintain code quality across teams

### 🚀 **Startup MVP Development**
**Scenario**: Solo developer building SaaS product
```
Initiative: "Project Management SaaS MVP"
├── Epic 1: "Core Task Management"
│   ├── Phase 1: "Basic CRUD Operations"
│   └── Phase 2: "Real-time Updates"
└── Epic 2: "User Onboarding Flow"
```

**Framework Application**:
- **Epic Workflow**: Break down MVP into manageable chunks
- **Architecture Lifecycle**: Document decisions as you build
- **Problem Solving**: Systematic debugging when stuck
- **User Rules Template**: Optimize AI context for faster development

### 🔧 **Legacy System Modernization**
**Scenario**: Migrating monolith to microservices
```
Initiative: "Monolith to Microservices Migration"
├── Epic 1: "Extract User Service"
├── Epic 2: "Extract Payment Service"  
└── Epic 3: "API Gateway Implementation"
```

**Framework Application**:
- **Architecture Design**: Plan service boundaries and data flow
- **Problem Solving**: Debug complex migration issues
- **Execution Standards**: Maintain quality during transition
- **Architecture Lifecycle**: Document architectural decisions

## 🛠️ Quick Start Guide

### Step 1: Choose Your IDE
Select your AI coding assistant from our supported platforms:

| IDE | Installation Link | Rule System |
|-----|------------------|-------------|
| **Cursor AI** | [Setup Guide](docs/ide-setup/cursor.md) | `.mdc` files with YAML frontmatter |
| **Windsurf** | [Setup Guide](docs/ide-setup/windsurf.md) | `.windsurfrules` (6K char limit) |
| **GitHub Copilot** | [Setup Guide](docs/ide-setup/github-copilot.md) | `.github/copilot-instructions.md` |
| **Roo Code** | [Setup Guide](docs/ide-setup/roo-code.md) | Custom Instructions + `.rooignore` |
| **Cline** | [Setup Guide](docs/ide-setup/cline.md) | `.clinerules` + Custom Instructions |
| **More...** | [All IDE Setups](docs/ide-setup/) | 11 total IDE adaptations |

### Step 2: Install Framework
```bash
# Clone or download the framework
git clone [your-repo-url]

# Generate adaptations for all IDEs
python3 create_ide_adaptations.py

# Or create for specific IDE
python3 create_ide_adaptations.py --ide cursor
```

### Step 3: Basic Usage
1. **Copy your IDE's adaptation** files to your project
2. **Start with user-rules-template** as your main AI system prompt
3. **Load additional components** based on the decision matrix:
   - Building features? → Epic Workflow
   - Debugging issues? → Problem Solving Framework
   - Designing architecture? → Architecture Design Process

### Step 4: First Epic
Try creating your first epic:
```
Initiative: "Learning the AI Epic Framework"
└── Epic 1: "Setup and First Project"
    ├── Phase 1: "Framework Installation" 
    ├── Phase 2: "Create Sample Epic"
    └── Phase 3: "Test Problem Solving"
```

## 📖 Documentation

### 📚 **Core Documentation**
- **[Framework Overview](docs/framework-overview.md)** - Detailed explanation of all components
- **[Epic Workflow Guide](docs/epic-workflow-guide.md)** - Complete workflow management tutorial
- **[Problem Solving Guide](docs/problem-solving-guide.md)** - Systematic troubleshooting methodology
- **[Architecture Design Guide](docs/architecture-design-guide.md)** - Design process and patterns
- **[Customization Guide](docs/customization-guide.md)** - Adapt framework for your needs

### 🔧 **IDE Setup Guides**
- **[Cursor AI Setup](docs/ide-setup/cursor.md)** - Your optimized structure preserved
- **[Windsurf Setup](docs/ide-setup/windsurf.md)** - `.windsurfrules` configuration
- **[GitHub Copilot Setup](docs/ide-setup/github-copilot.md)** - Repository instructions
- **[Roo Code Setup](docs/ide-setup/roo-code.md)** - VS Code extension configuration
- **[Cline Setup](docs/ide-setup/cline.md)** - `.clinerules` and custom instructions
- **[All IDE Setups](docs/ide-setup/)** - Complete setup guides for all 11 IDEs

### 🎯 **Advanced Topics**
- **[Token Optimization](docs/advanced/token-optimization.md)** - Maximize AI efficiency
- **[Team Workflows](docs/advanced/team-workflows.md)** - Multi-developer coordination
- **[Integration Patterns](docs/advanced/integration-patterns.md)** - Framework integration strategies

## 🎨 Customization

The framework is designed to be adapted to your specific needs:

### **Modify Core Templates**
```bash
# Edit source files
vim framework/generic/user-rules-template.md
vim framework/generic/epic-workflow-instructions.md

# Regenerate all IDE adaptations
python3 create_ide_adaptations.py
```

### **Create Custom Components**
Add new framework files and update the navigation in `user-rules-template.md`:
```markdown
## Framework Navigation
- **Epic Workflow**: [epic-workflow-instructions.md](./epic-workflow-instructions.md)
- **Your Custom Component**: [your-custom-component.md](./your-custom-component.md)
```

### **IDE-Specific Customization**
Each IDE adaptation can be customized independently:
- **Cursor**: Modify `.mdc` files and YAML frontmatter
- **Windsurf**: Adjust content to fit 6K character limit
- **VS Code Extensions**: Customize settings and rule files

## 🤝 Contributing

We welcome contributions to improve the framework:

1. **Research Requirements**: All new IDE support must include official documentation research
2. **Test with Real IDEs**: Verify adaptations work with actual IDE installations
3. **Follow Framework Patterns**: Maintain consistency with existing structure
4. **Document Changes**: Update relevant documentation

## 📊 Framework Statistics

| Metric | Value |
|--------|-------|
| **Supported IDEs** | 11 verified platforms |
| **Core Components** | 6 framework modules |
| **Documentation Files** | 25+ guides and references |
| **Research Depth** | Official documentation based |
| **Token Efficiency** | Conditional loading system |

## 🆘 Support & Community

- **📖 Documentation**: Comprehensive guides in `/docs/` folder
- **🐛 Issues**: Report bugs or request features via GitHub issues
- **💡 Ideas**: Share customization ideas and use cases
- **🤝 Contribute**: Help improve framework for everyone

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

**MIT License Summary:**
- ✅ **Free to use** for commercial and non-commercial projects
- ✅ **Modify and distribute** as needed
- ✅ **No warranty** provided (use at your own risk)
- ✅ **Attribution** required (include license and copyright notice)

**Full License Text:** [LICENSE](LICENSE)

---

**Ready to transform your AI-assisted development?** Start with our [Framework Overview](docs/framework-overview.md) or jump straight to your [IDE Setup Guide](docs/ide-setup/).

*Built with ❤️ for developers who want to build better software faster with AI assistance.* 