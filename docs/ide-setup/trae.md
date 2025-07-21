# Trae Setup Guide

Trae is an IDE-agnostic AI assistance tool that provides consistent AI support across multiple development environments. This guide explains how to configure the AI Epic Framework for Trae's flexible, multi-IDE approach.

## 🎯 Overview

**Trae Features**:
- IDE-agnostic AI assistance (works with any editor/IDE)
- Flexible configuration system
- Multi-project support with context switching
- Integration with various development tools
- Consistent AI behavior across different environments

**Framework Benefits in Trae**:
- Unified framework experience across all IDEs
- Consistent methodology regardless of development environment
- Flexible configuration for different project types
- Seamless context switching between projects and IDEs

## 📁 Framework Structure

Your Trae adaptation includes:

```
framework/trae-specific/
├── trae-config.yaml                     # Main Trae configuration
├── framework-context.md                 # Core framework guidance
├── ide-configs/                         # IDE-specific configurations
│   ├── vscode-config.json              # VS Code integration
│   ├── vim-config.vim                  # Vim integration
│   ├── emacs-config.el                 # Emacs integration
│   └── intellij-config.xml             # IntelliJ integration
├── project-templates/                   # Project-specific templates
│   ├── web-app-template.yaml           # Web application projects
│   ├── api-service-template.yaml       # API service projects
│   └── mobile-app-template.yaml        # Mobile application projects
└── README.md                           # Setup instructions
```

## 🚀 Installation

### Step 1: Install Trae

**1. Install Trae CLI**:
```bash
# Install Trae (check official documentation for latest method)
npm install -g trae-ai
# or
pip install trae-ai
# or
cargo install trae-ai
```

**2. Verify Installation**:
```bash
trae --version
trae --help
```

### Step 2: Copy Framework Configuration

**Copy Framework Files**:
```bash
# Copy configuration to Trae directory
mkdir -p ~/.trae/framework
cp -r framework/trae-specific/* ~/.trae/framework/

# Or use project-specific installation
cp -r framework/trae-specific /path/to/your/project/.trae/
```

### Step 3: Configure Trae

**1. Initialize Framework Configuration**:
```bash
# Initialize Trae with framework
trae init --framework ~/.trae/framework/trae-config.yaml
```

**2. Configure IDE Integration**:
```bash
# Set up IDE-specific configurations
trae ide-setup --auto-detect
# or manually specify IDE
trae ide-setup --ide vscode --config ~/.trae/framework/ide-configs/vscode-config.json
```

## 🎛️ Configuration

### Main Configuration File

The `trae-config.yaml` configures Trae for framework usage:

```yaml
framework:
  name: "AI Epic Framework"
  version: "1.0"
  description: "Systematic approach to complex application development"

components:
  epic-workflow:
    description: "Initiative → Epic → Phase → Step methodology"
    triggers:
      - "epic"
      - "project" 
      - "feature"
      - "workflow"
      - "planning"
    context_file: "components/epic-workflow.md"
    
  problem-solving:
    description: "Systematic investigation for stubborn issues"
    triggers:
      - "debug"
      - "problem"
      - "troubleshoot"
      - "investigate"
      - "complex"
    context_file: "components/problem-solving.md"
    
  architecture-design:
    description: "Structured system design methodology"
    triggers:
      - "architecture"
      - "design"
      - "component"
      - "system"
      - "structure"
    context_file: "components/architecture-design.md"
    
  execution-standards:
    description: "Quality protocols and execution guidelines"
    triggers:
      - "review"
      - "quality"
      - "standards"
      - "best practices"
    context_file: "components/execution-standards.md"

settings:
  auto_component_loading: true
  context_optimization: true
  ide_agnostic: true
  multi_project_support: true
  session_persistence: true

ide_integration:
  auto_detect: true
  supported_ides:
    - vscode
    - vim
    - neovim
    - emacs
    - intellij
    - sublime
    - atom
  
project_management:
  auto_project_detection: true
  context_switching: true
  project_specific_configs: true
```

### Framework Context File

The `framework-context.md` provides core guidance:

```markdown
# AI Epic Framework for Trae

## Framework Overview
You are using the AI Epic Framework through Trae to provide consistent, systematic AI assistance across multiple IDEs and development environments.

## Multi-IDE Consistency
Regardless of the IDE being used (VS Code, Vim, IntelliJ, etc.), apply the same framework methodology:
- Same decision matrix for component activation
- Consistent epic breakdown approaches
- Uniform problem-solving methodology
- Standardized architecture design process

## Component Activation Matrix

### Epic Workflow Component
**Activate when**: Developer mentions complex features, project planning, or large application development
**IDE Context**: Works across all IDEs with appropriate file creation and organization
**Purpose**: Break down complex applications systematically

### Problem Solving Component  
**Activate when**: Developer has stubborn technical issues or needs systematic investigation
**IDE Context**: Adapts to IDE-specific debugging tools and workflows
**Purpose**: Structured approach to complex technical problems

### Architecture Design Component
**Activate when**: Developer needs architectural decisions or system design guidance
**IDE Context**: Integrates with IDE-specific design and documentation tools
**Purpose**: Requirements-driven architectural decision making

### Execution Standards Component
**Activate when**: Developer needs code quality, review, or best practices guidance
**IDE Context**: Aligns with IDE-specific linting, formatting, and review tools
**Purpose**: Consistent quality standards across environments

## IDE-Agnostic Principles
- Framework guidance adapts to IDE capabilities
- File organization works across different file managers
- Methodology remains consistent regardless of environment
- Integration points align with each IDE's strengths
```

## 🎯 Usage Patterns

### Cross-IDE Framework Application

**1. VS Code Integration**:
```bash
# Start Trae with VS Code
trae start --ide vscode --project myapp

Developer: "Using Epic Workflow, help me plan a user dashboard feature"

Trae Response:
1. Activates Epic Workflow component
2. Creates VS Code-compatible epic directory structure
3. Generates INDEX.md and REQUIREMENTS.md with VS Code markdown preview
4. Provides VS Code-specific task integration
```

**2. Vim Integration**:
```bash
# Start Trae with Vim
trae start --ide vim --project myapp

Developer: "I have a complex performance issue that I can't solve"

Trae Response:
1. Recognizes Problem Solving Framework trigger
2. Applies systematic investigation methodology
3. Provides Vim-compatible file organization
4. Suggests Vim-specific debugging commands and workflows
```

**3. IntelliJ Integration**:
```bash
# Start Trae with IntelliJ
trae start --ide intellij --project myapp

Developer: "Help me design the architecture for this microservice"

Trae Response:
1. Activates Architecture Design Process
2. Guides requirements gathering and technology evaluation
3. Creates IntelliJ-compatible documentation structure
4. Integrates with IntelliJ project management features
```

### Multi-Project Support

**Project Context Switching**:
```bash
# Switch between projects with different configurations
trae switch-project --project webapp --framework-profile "web-development"
trae switch-project --project api-service --framework-profile "backend-service"
trae switch-project --project mobile-app --framework-profile "mobile-development"
```

**Project-Specific Templates**:
```yaml
# web-app-template.yaml
framework_profile: "web-development"
epic_structure:
  initiative_focus: "user experience"
  common_epics:
    - "user authentication"
    - "frontend components" 
    - "backend api"
    - "data management"
problem_solving:
  focus_areas:
    - "browser compatibility"
    - "performance optimization"
    - "user experience issues"
architecture:
  typical_decisions:
    - "frontend framework choice"
    - "state management approach"
    - "api design patterns"
```

## 🔧 Customization for Trae

### IDE-Specific Adaptations

**VS Code Configuration**:
```json
{
  "trae_integration": {
    "framework_activation": "workspace_folder",
    "epic_structure": {
      "create_tasks": true,
      "integrate_terminal": true,
      "markdown_preview": true
    },
    "problem_solving": {
      "debug_integration": true,
      "terminal_commands": true,
      "output_panel": true
    },
    "architecture": {
      "diagram_support": true,
      "documentation_preview": true,
      "project_structure": true
    }
  }
}
```

**Vim Configuration**:
```vim
" trae-framework integration for Vim
let g:trae_framework_enabled = 1
let g:trae_epic_structure = 1
let g:trae_auto_documentation = 1

" Framework-specific key mappings
nnoremap <leader>te :TraeEpicStart<CR>
nnoremap <leader>tp :TraeProblemSolve<CR>
nnoremap <leader>ta :TraeArchitectureDesign<CR>
nnoremap <leader>tr :TraeQualityReview<CR>

" Auto-commands for framework integration
autocmd BufNewFile,BufRead *.epic set filetype=markdown
autocmd BufNewFile,BufRead INDEX.md set syntax=epic_index
```

### Environment-Specific Workflows

**Terminal-Heavy Workflow**:
```bash
# Configure for terminal-centric development
trae config set workflow.terminal_focus true
trae config set display.cli_friendly true
trae config set integration.command_line_tools true

# Framework integration with terminal tools
trae config set epic.directory_structure "cli_friendly"
trae config set problem_solving.terminal_debugging true
trae config set architecture.text_based_diagrams true
```

**GUI-Heavy Workflow**:
```bash
# Configure for GUI-centric development
trae config set workflow.gui_focus true
trae config set display.rich_formatting true
trae config set integration.gui_tools true

# Framework integration with GUI tools
trae config set epic.visual_organization true
trae config set problem_solving.gui_debugging true
trae config set architecture.visual_diagrams true
```

## 🎮 Practical Examples

### Example 1: Cross-IDE Epic Development

**Scenario**: Web application development across VS Code and Vim

**VS Code Session**:
```bash
# Start epic planning in VS Code
$ trae start --ide vscode

Developer: "Using Epic Workflow, help me plan an e-commerce platform"

Trae: "Creating epic structure optimized for VS Code:
- Epic directories with VS Code workspace configuration
- Markdown files with preview support
- Task integration with VS Code task runner
- Git integration for epic progress tracking"
```

**Vim Session** (same project):
```bash
# Continue epic work in Vim
$ trae start --ide vim

Developer: "Continue working on Epic 2: Product Catalog"

Trae: "Switching to Vim-optimized interface:
- Text-based epic navigation
- Vim-friendly file organization
- Terminal-based task management
- Command-line tool integration"
```

### Example 2: Multi-Project Framework Application

**Project A** (Web App):
```bash
$ trae switch-project --project webapp

Developer: "Debug performance issue in user dashboard"

Trae: "Applying web-focused Problem Solving Framework:
- Browser performance profiling
- Frontend-specific investigation patterns
- User experience impact assessment
- Web-specific solution strategies"
```

**Project B** (API Service):
```bash
$ trae switch-project --project api-service

Developer: "Debug the same type of performance issue"

Trae: "Applying API-focused Problem Solving Framework:
- Server-side performance analysis
- Database query optimization
- API response time investigation
- Backend-specific solution strategies"
```

### Example 3: IDE Migration Support

**Migrating from VS Code to IntelliJ**:
```bash
# Export framework state from VS Code
$ trae export-state --ide vscode --project myapp --output myapp-state.json

# Switch to IntelliJ
$ trae start --ide intellij --project myapp

# Import framework state
$ trae import-state --input myapp-state.json

Trae: "Framework state migrated to IntelliJ:
- Epic structure converted to IntelliJ project format
- Problem investigations transferred with IntelliJ-compatible documentation
- Architecture decisions integrated with IntelliJ design tools"
```

## 🔍 Troubleshooting

### Common Issues

**1. IDE Detection Problems**:
```bash
# Check IDE detection
trae ide-detect --verbose

# Manually specify IDE if auto-detection fails
trae config set default_ide "vscode"

# Verify IDE configuration
trae config show ide_integration
```

**2. Framework Component Loading Issues**:
```bash
# Check component configuration
trae components list

# Test component loading
trae test-component epic-workflow

# Reset component configuration
trae components reset --reload-from-config
```

**3. Cross-IDE Consistency Problems**:
```bash
# Check framework consistency across IDEs
trae consistency-check --all-ides

# Synchronize framework state
trae sync-framework --all-projects

# Reset to default framework configuration
trae reset-framework --preserve-projects
```

### Optimization Tips

**1. Multi-IDE Workflow**:
- Use consistent project naming across IDEs
- Maintain synchronized framework configuration
- Set up IDE-specific optimizations while preserving framework consistency
- Regular framework state synchronization

**2. Project Management**:
- Use clear project profiles for different types of applications
- Maintain separate configurations for different development environments
- Regular cleanup of unused project configurations
- Backup framework configuration and project states

**3. Performance Optimization**:
- Configure framework loading based on project complexity
- Use IDE-specific optimizations when available
- Cache frequently used framework components
- Regular performance monitoring and optimization

## 📊 Success Metrics

### Framework Effectiveness in Trae

**1. Cross-IDE Consistency**:
- Same framework methodology regardless of IDE choice
- Consistent epic breakdown and project organization
- Uniform problem-solving approach across environments
- Standardized architecture design process

**2. Multi-Project Support**:
- Effective context switching between different project types
- Appropriate framework adaptation for different application domains
- Consistent quality standards across all projects
- Efficient project-specific configuration management

**3. Development Flexibility**:
- Freedom to use different IDEs while maintaining framework benefits
- Seamless migration between development environments
- Consistent AI assistance regardless of tool choice
- Enhanced productivity through IDE-agnostic systematic approaches

## 📚 Additional Resources

### Trae Documentation
- [Trae Official Website](https://trae.ai) - Main documentation and downloads
- [Trae IDE Integration](https://docs.trae.ai/ide-integration) - IDE-specific setup guides
- [Trae Configuration](https://docs.trae.ai/configuration) - Advanced configuration options

### Framework Resources
- [Framework Overview](../framework-overview.md) - Complete framework understanding
- [Epic Workflow Guide](../epic-workflow-guide.md) - Detailed workflow implementation
- [Customization Guide](../customization-guide.md) - Adapting for your needs

### Multi-IDE Development
- [Cross-IDE Workflows](../advanced/cross-ide-patterns.md) - Advanced multi-IDE patterns
- [Project Configuration Management](../advanced/project-configs.md) - Multi-project setup
- [IDE Migration Strategies](../advanced/ide-migration.md) - Switching between IDEs

---

**Ready to enjoy framework consistency across all your development environments?** Install Trae, configure the framework, and experience systematic AI assistance regardless of which IDE you choose to use. 