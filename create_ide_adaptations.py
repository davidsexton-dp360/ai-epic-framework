#!/usr/bin/env python3
"""
AI Epic Framework - IDE Adaptation Generator

This script generates IDE-specific adaptations of the generic framework files
for all supported AI coding IDEs. It converts the generic markdown files into
the appropriate format for each IDE's rule system.

Supported IDEs:
- Cursor AI (.mdc files)
- Windsurf (.windsurfrules files)
- GitHub Copilot (.github/copilot-instructions.md)
- Roo Code (.rooignore files)
- Cline (.clinerules files)
- Claude Code (configuration files)
- Trae (YAML configuration)
- Kilo Code (JSON rules)
- Void IDE (JSON configuration)
- Zencoder (multiple formats)
- Gemini CLI (GEMINI.md system prompt)
"""

import os
import shutil
import re
from pathlib import Path

class IDEAdaptationGenerator:
    def __init__(self):
        self.base_dir = Path(__file__).parent
        self.generic_dir = self.base_dir / "framework" / "generic"
        self.framework_dir = self.base_dir / "framework"
        
        # IDE-specific directories and file extensions (updated based on latest documentation)
        self.ide_configs = {
            "cursor-specific": {
                "ext": ".mdc",
                "files": [
                    "user-rules-template.mdc",
                    "epic-workflow-instructions.mdc",
                    "problem-solving-framework.mdc",
                    "architecture-design-process.mdc",
                    "architecture-lifecycle.mdc",
                    "general-execution-standards.mdc"
                ]
            },
            "windsurf-specific": {
                "ext": ".windsurfrules",
                "files": [
                    "user-rules-template.windsurfrules",
                    "epic-workflow-instructions.windsurfrules",
                    "problem-solving-framework.windsurfrules",
                    "architecture-design-process.windsurfrules",
                    "architecture-lifecycle.windsurfrules",
                    "general-execution-standards.windsurfrules"
                ]
            },
            "github-copilot-specific": {
                "ext": ".md",
                "files": [
                    "copilot-instructions.md"
                ]
            },
            "roo-code-specific": {
                "ext": ".md",
                "files": [
                    ".roo/rules/ai-epic-framework.md",
                    ".roo/rules-code/ai-epic-framework.md",
                    ".rooignore"
                ]
            },
            "cline-specific": {
                "ext": ".md",
                "files": [
                    ".clinerules/ai-epic-framework.md",
                    ".clinerules/01-framework-overview.md",
                    ".clinerules/02-epic-workflow.md",
                    ".clinerules/03-problem-solving.md",
                    ".clinerules/04-architecture-design.md",
                    ".clinerules/05-execution-standards.md"
                ]
            },
            "claude-code-specific": {
                "ext": ".md",
                "files": [
                    "framework-prompt.md",
                    "claude-config.json"
                ]
            },
            "trae-specific": {
                "ext": ".yaml",
                "files": [
                    "trae-config.yaml",
                    "framework-context.md"
                ]
            },
            "kilo-code-specific": {
                "ext": ".md",
                "files": [
                    ".kilocode/rules/ai-epic-framework.md",
                    ".kilocode/rules/01-framework-overview.md",
                    ".kilocode/rules/02-epic-workflow.md",
                    ".kilocode/rules/03-problem-solving.md",
                    ".kilocode/rules/04-architecture-design.md",
                    ".kilocode/rules/05-execution-standards.md"
                ]
            },
            "void-specific": {
                "ext": ".json",
                "files": [
                    "void-config.json",
                    "framework-system-prompt.md",
                    "privacy-rules.json"
                ]
            },
            "zencoder-specific": {
                "ext": ".rules",
                "files": [
                    "framework-rules.rules",
                    "enterprise-config.json",
                    "cursor-compatibility.cursorrules",
                    "cline-compatibility.clinerules",
                    "windsurf-compatibility.windsurfrules",
                    "copilot-compatibility.md"
                ]
            },
            "gemini-cli-specific": {
                "ext": ".md",
                "files": [
                    "GEMINI.md",
                    "gemini-config.json",
                    "google-cloud-integration.json"
                ]
            }
        }

    def create_ide_directories(self):
        """Create IDE-specific directories if they don't exist and clear them before use."""
        for ide_dir in self.ide_configs.keys():
            ide_path = self.framework_dir / ide_dir
            if ide_path.exists():
                # Remove all files in the directory
                for item in ide_path.iterdir():
                    if item.is_file() or item.is_symlink():
                        item.unlink()
                    elif item.is_dir():
                        shutil.rmtree(item)
            else:
                ide_path.mkdir(exist_ok=True)
            print(f"✅ Cleared and verified directory: {ide_dir}")

    def copy_generic_files(self):
        """Copy generic framework files to IDE-specific directories with appropriate extensions."""
        generic_files = [
            "user-rules-template.md",
            "epic-workflow-instructions.md",
            "problem-solving-framework.md",
            "architecture-design-process.md",
            "architecture-lifecycle.md",
            "general-execution-standards.md"
        ]

        for ide_name, config in self.ide_configs.items():
            ide_dir = self.framework_dir / ide_name
            
            # Handle special cases first
            if ide_name == "github-copilot-specific":
                self.create_copilot_instructions(ide_dir)
                continue
            elif ide_name == "roo-code-specific":
                self.create_roo_code_files(ide_dir)
                continue
            elif ide_name == "cline-specific":
                self.create_cline_files(ide_dir)
                continue
            elif ide_name == "windsurf-specific":
                self.create_windsurf_files(ide_dir)
                continue
            elif ide_name == "claude-code-specific":
                self.create_claude_code_files(ide_dir)
                continue
            elif ide_name == "trae-specific":
                self.create_trae_files(ide_dir)
                continue
            elif ide_name == "kilo-code-specific":
                self.create_kilo_code_files(ide_dir)
                continue
            elif ide_name == "void-specific":
                self.create_void_files(ide_dir)
                continue
            elif ide_name == "zencoder-specific":
                self.create_zencoder_files(ide_dir)
                continue
            elif ide_name == "gemini-cli-specific":
                self.create_gemini_files(ide_dir)
                continue

            # Standard file copying for Cursor AI
            if ide_name == "cursor-specific":
                for generic_file in generic_files:
                    source_file = self.generic_dir / generic_file
                    target_file = ide_dir / generic_file.replace(".md", ".mdc")
                    
                    if source_file.exists():
                        self.create_cursor_file_with_meta(source_file, target_file, generic_file)
                        print(f"✅ Copied {generic_file} → {target_file.name}")

    def create_cursor_file_with_meta(self, source_file, target_file, generic_file):
        """Create Cursor AI file with meta headers at the top."""
        # Define the "When To Use" descriptions for each file
        when_to_use_descriptions = {
            "user-rules-template.md": "Load as primary navigation hub for accessing other framework documentation. Use for conditional loading decisions and optimizing context window usage. Keep loaded throughout session.",
            "epic-workflow-instructions.md": "Load when creating task hierarchies (Initiative→Epic→Phase→Step), managing workflow structure, delegating tasks, or tracking epic progress. Essential for any workflow organization or task creation activities.",
            "problem-solving-framework.md": "Load only after 3+ failed solution attempts, for multi-component system failures, or when explicitly requested. Provides systematic research-driven troubleshooting workflow with temporary file management.",
            "architecture-design-process.md": "Load when designing system architecture, creating technical proposals, selecting technology stacks, or defining component boundaries. Use for architectural research methodology and design validation.",
            "architecture-lifecycle.md": "Load when working with docs/architecture/ folder structure, managing architecture documentation, creating index files, or enforcing document size limits (700 lines). Essential for architecture documentation organization.",
            "general-execution-standards.md": "Load for research protocols, decision-making standards, tool usage guidelines, and quality assurance. Reference for general development practices and cross-cutting concerns."
        }
        
        # Read the source file content
        with open(source_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Fix relative paths for Cursor AI context
        content = self.fix_relative_paths_for_ide(content, "cursor-specific")
        
        # Create the meta header
        description = when_to_use_descriptions.get(generic_file, "AI Epic Framework component")
        meta_header = f"""---
description: {description}
alwaysApply: false
---

"""
        
        # Combine meta header with content
        new_content = meta_header + content
        
        # Write to target file
        with open(target_file, 'w', encoding='utf-8') as f:
            f.write(new_content)

    def fix_relative_paths_for_ide(self, content, ide_name):
        """Fix relative paths in framework content for specific IDE context."""
        if ide_name == "cursor-specific":
            # Cursor AI: files are in same directory with .mdc extension
            content = content.replace('./epic-workflow-instructions.md', './epic-workflow-instructions.mdc')
            content = content.replace('./problem-solving-framework.md', './problem-solving-framework.mdc')
            content = content.replace('./architecture-design-process.md', './architecture-design-process.mdc')
            content = content.replace('./architecture-lifecycle.md', './architecture-lifecycle.mdc')
            content = content.replace('./general-execution-standards.md', './general-execution-standards.mdc')
        else:
            # All other IDEs: files are in same directory with .md extension (self-contained)
            content = content.replace('./epic-workflow-instructions.md', './epic-workflow-instructions.md')
            content = content.replace('./problem-solving-framework.md', './problem-solving-framework.md')
            content = content.replace('./architecture-design-process.md', './architecture-design-process.md')
            content = content.replace('./architecture-lifecycle.md', './architecture-lifecycle.md')
            content = content.replace('./general-execution-standards.md', './general-execution-standards.md')
        
        return content

    def create_roo_code_files(self, ide_dir):
        """Create Roo Code specific files using latest directory-based approach."""
        # Create .roo directory structure
        roo_dir = ide_dir / ".roo"
        roo_rules_dir = roo_dir / "rules"
        roo_rules_code_dir = roo_dir / "rules-code"
        
        roo_rules_dir.mkdir(parents=True, exist_ok=True)
        roo_rules_code_dir.mkdir(parents=True, exist_ok=True)
        
        # Read the full user-rules-template content for the custom instructions
        user_rules_file = self.generic_dir / "user-rules-template.md"
        with open(user_rules_file, 'r', encoding='utf-8') as f:
            user_rules_content = f.read()
        
        # Fix relative paths for Roo Code context
        user_rules_content = self.fix_relative_paths_for_ide(user_rules_content, "roo-code-specific")
        
        # Create main framework rules file (applies to all modes)
        framework_rules = f"""# AI Epic Framework - Roo Code Rules

## Framework Overview
This project uses the AI Epic Framework for systematic complex application development.

{user_rules_content}

## Roo Code Integration
- **Directory-Based Rules**: Framework rules stored in `.roo/rules/` directory
- **Mode-Specific Rules**: Code-specific rules in `.roo/rules-code/` directory
- **File Filtering**: Use `.rooignore` to control AI context inclusion
- **Intelligent Context**: Framework optimizes file inclusion for better AI assistance

## Framework Components
- **Epic Workflow**: Hierarchical task breakdown (Initiative → Epic → Phase → Step)
- **Problem Solving**: Systematic troubleshooting methodology
- **Architecture Design**: Guided architectural decision-making
- **Execution Standards**: Quality assurance and best practices

## Usage Guidelines
1. Use epic workflow for project breakdown and task organization
2. Apply problem-solving framework for complex technical issues
3. Use architecture design process for system planning and decisions
4. Follow execution standards for research and validation

## File Organization
- Framework files: `framework/` directory
- Documentation: `docs/` directory with comprehensive guides
- Task structure: `/.epic-workflows/tasks/` for hierarchical task management
- Architecture docs: `docs/architecture/` for system design documentation
"""
        
        # Create code-specific rules file
        code_rules = """# AI Epic Framework - Code Mode Rules

## Code Development Guidelines
When working in Code mode, follow these framework-specific guidelines:

## Epic Workflow Integration
- Create task hierarchies in `/.epic-workflows/tasks/`
- Use INDEX.md and REQUIREMENTS.md for each task
- Follow Plan → Document → Execute → Track → Validate sequence

## Problem Solving Framework
- Apply after 3+ failed solution attempts
- Use systematic research-driven approach
- Create temporary files for investigation
- Follow Research → Decompose → Execute → Validate → Cleanup

## Architecture Design Process
- Start with requirements and constraints
- Research patterns and technologies
- Design components with clear boundaries
- Plan for scalability, performance, security
- Document decisions and trade-offs

## Execution Standards
- Research-first approach
- Multi-source validation
- Quality over speed
- Comprehensive documentation
- Architecture compliance

## Code Quality Attributes
- Scalability: Stateless services, autoscaling
- Performance: Caching, async I/O
- Security: Zero-trust, encryption
- Reliability: Circuit breakers, health probes
- Observability: Structured logs, metrics
"""
        
        # .rooignore for file filtering
        rooignore_content = """# Roo Code File Filtering Configuration
# This file controls which files Roo Code includes in AI context

# Include framework documentation
docs/
framework/
*.md
*.mdx

# Include source code
src/
lib/
app/
components/
pages/
utils/
hooks/
services/

# Include configuration files
package.json
tsconfig.json
next.config.js
tailwind.config.js
.eslintrc.js
.prettierrc

# Include test files
__tests__/
*.test.js
*.test.ts
*.spec.js
*.spec.ts

# Exclude build artifacts
node_modules/
.next/
dist/
build/
coverage/
.env.local
.env.production

# Exclude temporary files
*.log
*.tmp
.DS_Store
Thumbs.db
"""
        
        # Write files to appropriate directories
        with open(roo_rules_dir / "ai-epic-framework.md", "w") as f:
            f.write(framework_rules)
        
        with open(roo_rules_code_dir / "ai-epic-framework.md", "w") as f:
            f.write(code_rules)
        
        with open(ide_dir / ".rooignore", "w") as f:
            f.write(rooignore_content)
        
        print(f"✅ Created Roo Code configuration files with directory-based structure")

    def create_cline_files(self, ide_dir):
        """Create Cline specific files using latest folder-based approach."""
        # Create .clinerules directory structure
        clinerules_dir = ide_dir / ".clinerules"
        clinerules_dir.mkdir(parents=True, exist_ok=True)
        
        # Read the full user-rules-template content for the custom instructions
        user_rules_file = self.generic_dir / "user-rules-template.md"
        with open(user_rules_file, 'r', encoding='utf-8') as f:
            user_rules_content = f.read()
        
        # Fix relative paths for Cline context
        user_rules_content = self.fix_relative_paths_for_ide(user_rules_content, "cline-specific")
        
        # Create main framework overview file
        framework_overview = f"""# AI Epic Framework - Cline Rules

## Framework Overview
This project uses the AI Epic Framework for systematic complex application development.

{user_rules_content}

## Cline Integration
- **Folder-Based Rules**: Framework rules stored in `.clinerules/` directory
- **MCP Integration**: Leverage Cline's MCP capabilities for enhanced AI assistance
- **VS Code Compatibility**: Seamless integration with VS Code ecosystem
- **Team Collaboration**: Maintain framework documentation for team coordination

## Framework Components
- **Epic Workflow**: Hierarchical task breakdown (Initiative → Epic → Phase → Step)
- **Problem Solving**: Systematic troubleshooting methodology
- **Architecture Design**: Guided architectural decision-making
- **Execution Standards**: Quality assurance and best practices

## Usage Guidelines
1. Use epic workflow for project breakdown and task organization
2. Apply problem-solving framework for complex technical issues
3. Use architecture design process for system planning and decisions
4. Follow execution standards for research and validation

## File Organization
- Framework files: `framework/` directory
- Documentation: `docs/` directory with comprehensive guides
- Task structure: `/.epic-workflows/tasks/` for hierarchical task management
- Architecture docs: `docs/architecture/` for system design documentation
"""
        
        # Create epic workflow rules
        epic_workflow = """# Epic Workflow Rules

## Task Breakdown
- Use epic workflow for task breakdown (Initiative → Epic → Phase → Step)
- Create task hierarchy in `/.epic-workflows/tasks/`
- Use INDEX.md and REQUIREMENTS.md for each task
- Follow Plan → Document → Execute → Track → Validate sequence

## File Management
- Maintain architecture docs in `docs/architecture/`
- Use INDEX.md and REQUIREMENTS.md for each task
- Create task hierarchies with clear naming conventions
- Track progress and completion status

## Workflow Integration
- Integrate with existing project management tools
- Maintain consistency across team members
- Update task status regularly
- Document decisions and trade-offs
"""
        
        # Create problem solving rules
        problem_solving = """# Problem Solving Framework Rules

## When to Apply
- Apply problem-solving framework after 3+ failed attempts
- Use for multi-component system failures
- Apply for complex technical issues
- Use when explicitly requested

## Research Protocol
- Consult official documentation first
- Use Context7 and Perplexity for research
- Cross-check from multiple sources
- Document decisions and trade-offs

## Systematic Approach
- Follow Research → Decompose → Execute → Validate → Cleanup
- Create temporary files for investigation
- Use systematic research-driven approach
- Validate solutions thoroughly

## Quality Standards
- Plan thoroughly, implement incrementally
- Validate after each milestone
- Update architecture docs for significant changes
- Maintain comprehensive documentation
"""
        
        # Create architecture design rules
        architecture_design = """# Architecture Design Process Rules

## Design Methodology
- Use architecture design process for system design
- Start with requirements and constraints
- Research patterns and technologies
- Design components with clear boundaries

## Quality Attributes
- Plan for scalability, performance, security
- Consider reliability and observability
- Document decisions and trade-offs
- Validate architectural decisions

## Integration Patterns
- Use REST + OpenAPI for API design
- Consider event-driven patterns with Kafka/NATS
- Implement microservices with gRPC
- Plan for service mesh (Istio, Linkerd)

## Documentation
- Maintain architecture docs in `docs/architecture/`
- Create architecture decision records (ADRs)
- Document component boundaries and interfaces
- Keep architecture docs up to date
"""
        
        # Create execution standards rules
        execution_standards = """# Execution Standards Rules

## Quality Assurance
- Follow execution standards for quality assurance
- Research-first approach for all decisions
- Multi-source validation for information
- Quality over speed in all implementations

## Development Process
- Plan thoroughly before implementation
- Implement incrementally with validation
- Update documentation for all changes
- Maintain comprehensive project documentation

## Team Coordination
- Ensure consistency across team members
- Use framework standards for all projects
- Maintain framework documentation
- Coordinate framework updates across team

## Best Practices
- Follow established coding standards
- Use version control effectively
- Implement proper testing strategies
- Maintain security best practices
"""
        
        # Write files to .clinerules directory
        with open(clinerules_dir / "01-framework-overview.md", "w") as f:
            f.write(framework_overview)
        
        with open(clinerules_dir / "02-epic-workflow.md", "w") as f:
            f.write(epic_workflow)
        
        with open(clinerules_dir / "03-problem-solving.md", "w") as f:
            f.write(problem_solving)
        
        with open(clinerules_dir / "04-architecture-design.md", "w") as f:
            f.write(architecture_design)
        
        with open(clinerules_dir / "05-execution-standards.md", "w") as f:
            f.write(execution_standards)
        
        print(f"✅ Created Cline configuration files with folder-based structure")

    def create_windsurf_files(self, ide_dir):
        """Create Windsurf specific files - .windsurfrules with character limits."""
        # Read the full user-rules-template content for the custom instructions
        user_rules_file = self.generic_dir / "user-rules-template.md"
        with open(user_rules_file, 'r', encoding='utf-8') as f:
            user_rules_content = f.read()
        
        # Fix relative paths for Windsurf context
        user_rules_content = self.fix_relative_paths_for_ide(user_rules_content, "windsurf-specific")
        
        # Windsurf has 6K character limit, so we need concise versions
        windsurf_rules = """# AI Epic Framework - Windsurf Rules

## Core Framework
Use AI Epic Framework for systematic complex application development.

## Epic Workflow
- Break down projects: Initiative → Epic → Phase → Step
- Create task hierarchy in /.epic-workflows/tasks/
- Use INDEX.md and REQUIREMENTS.md for each task
- Follow Plan → Document → Execute → Track → Validate sequence

## Problem Solving
- Apply after 3+ failed attempts
- Use systematic research-driven approach
- Create temporary files for investigation
- Follow Research → Decompose → Execute → Validate → Cleanup

## Architecture Design
- Start with requirements and constraints
- Research patterns and technologies
- Design components with clear boundaries
- Plan for scalability, performance, security
- Document decisions and trade-offs

## Execution Standards
- Research-first approach
- Multi-source validation
- Quality over speed
- Comprehensive documentation
- Architecture compliance

## File Organization
- Framework files in framework/
- Documentation in docs/
- Architecture docs in docs/architecture/
- Task files in /.epic-workflows/tasks/

## Quality Attributes
- Scalability: Stateless services, autoscaling
- Performance: Caching, async I/O
- Security: Zero-trust, encryption
- Reliability: Circuit breakers, health probes
- Observability: Structured logs, metrics

## Integration Patterns
- REST + OpenAPI
- Event-driven with Kafka/NATS
- Microservices with gRPC
- Service mesh (Istio, Linkerd)

## Success Metrics
- Problem fully resolved and validated
- Knowledge preserved in documentation
- Process improvements captured
- Architecture docs updated
- Task completion tracked
"""
        
        # Custom instructions for Windsurf with full framework content
        custom_instructions = f"""# AI Epic Framework - Windsurf Instructions

## Windsurf AI Integration
Windsurf AI provides intelligent coding assistance with the AI Epic Framework.

{user_rules_content}

## Windsurf Specific Features
- **Character Limit Optimization**: Framework rules optimized for 6K character limit
- **Essential Patterns**: Focus on core framework patterns and workflows
- **Reference Documentation**: Access detailed docs through relative paths
- **Efficient Context**: Optimized for Windsurf's context window

## Usage Guidelines
1. Use epic workflow for project breakdown
2. Apply problem-solving framework for debugging
3. Use architecture design process for system planning
4. Follow execution standards for quality

## Configuration
See `.windsurfrules` for framework rules configuration.
"""
        
        # Windsurf uses .windsurfrules for framework content (6K limit) and custom-instructions.md for details
        # No need to copy separate framework files - everything goes in the main files
        
        with open(ide_dir / ".windsurfrules", "w") as f:
            f.write(windsurf_rules)
        
        with open(ide_dir / "custom-instructions.md", "w") as f:
            f.write(custom_instructions)
        
        print(f"✅ Created Windsurf configuration files")

    def create_copilot_instructions(self, ide_dir):
        """Create GitHub Copilot instructions file with complete framework content."""
        # Read all generic framework files
        generic_files = [
            "user-rules-template.md",
            "epic-workflow-instructions.md",
            "problem-solving-framework.md",
            "architecture-design-process.md",
            "architecture-lifecycle.md",
            "general-execution-standards.md"
        ]
        
        # Combine all framework content
        combined_content = ""
        
        for generic_file in generic_files:
            source_file = self.generic_dir / generic_file
            if source_file.exists():
                with open(source_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Fix relative paths for GitHub Copilot context
                content = self.fix_relative_paths_for_ide(content, "github-copilot-specific")
                
                # Add section header for this file
                file_title = generic_file.replace('.md', '').replace('-', ' ').title()
                combined_content += f"\n\n# {file_title}\n\n{content}\n"
        
        # GitHub Copilot instructions with complete framework content
        copilot_content = f"""# AI Epic Framework - GitHub Copilot Instructions

## Repository Framework
This project uses the AI Epic Framework for systematic complex application development.

## Framework Overview
The AI Epic Framework provides comprehensive guidance for systematic complex application development, including epic workflow management, problem-solving methodologies, architecture design processes, and execution standards.

## Core Framework Components
- **Epic Workflow**: Hierarchical task breakdown (Initiative → Epic → Phase → Step)
- **Problem Solving**: Systematic troubleshooting methodology
- **Architecture Design**: Guided architectural decision-making
- **Execution Standards**: Quality assurance and best practices

## Framework Usage
1. **Task Management**: Use epic workflow for project breakdown and task organization
2. **Debugging**: Apply problem-solving framework for complex technical issues
3. **Design**: Use architecture design process for system planning and decisions
4. **Quality**: Follow execution standards for research and validation

## File Organization
- Framework files: `framework/generic/` and `framework/github-copilot-specific/`
- Documentation: `docs/` directory with comprehensive guides
- Task structure: `/.epic-workflows/tasks/` for hierarchical task management
- Architecture docs: `docs/architecture/` for system design documentation

## Development Workflow
1. **Planning**: Use epic workflow to break down complex features
2. **Implementation**: Follow execution standards for quality development
3. **Problem Solving**: Apply systematic approach for debugging
4. **Architecture**: Use design process for technical decisions
5. **Documentation**: Maintain comprehensive project documentation

## Framework Integration
- Copilot will reference these instructions for all development tasks
- Use framework decision matrix to determine appropriate methodologies
- Follow structured approaches for complex problem-solving
- Maintain consistency with framework principles

## Key Principles
- **Research-First**: Always consult official documentation
- **Multi-Source Validation**: Cross-check information from multiple sources
- **Quality Over Speed**: Plan thoroughly, implement incrementally
- **Comprehensive Documentation**: Document all decisions and trade-offs
- **Architecture Compliance**: Reference and update architecture docs

{combined_content}

For detailed setup and usage instructions, see: `docs/ide-setup/github-copilot.md`
"""
        
        with open(ide_dir / "copilot-instructions.md", "w") as f:
            f.write(copilot_content)
        print(f"✅ Created GitHub Copilot instructions with complete framework content")

    def create_claude_code_files(self, ide_dir):
        """Create Claude Code specific files."""
        # Read the full user-rules-template content for the framework prompt
        user_rules_file = self.generic_dir / "user-rules-template.md"
        with open(user_rules_file, 'r', encoding='utf-8') as f:
            user_rules_content = f.read()
        
        # Fix relative paths for Claude Code context
        user_rules_content = self.fix_relative_paths_for_ide(user_rules_content, "claude-code-specific")
        
        # Create comprehensive framework prompt for Claude Code
        framework_prompt = f"""# AI Epic Framework - Claude Code System Prompt

## Claude Code Configuration
You are an AI assistant configured with the AI Epic Framework for systematic complex application development. This system prompt provides comprehensive guidance for terminal-based development with structured methodologies.

{user_rules_content}

## Claude Code Specific Instructions
- Use terminal commands and file operations for development tasks
- Leverage Claude Code's agentic capabilities for autonomous development
- Apply framework methodologies through command-line interfaces
- Maintain framework documentation and task structure through file operations
- Use the decision matrix to determine which framework components to apply

## Terminal Integration
- Execute framework workflows through terminal commands
- Create and manage task hierarchies using file system operations
- Apply problem-solving framework through systematic investigation
- Use architecture design process for technical decision-making
- Follow execution standards for quality assurance

## Configuration
See `claude-config.json` for detailed configuration settings.
"""
        
        # Claude config
        claude_config = {
            "framework": {
                "name": "AI Epic Framework",
                "version": "1.0.0",
                "description": "Systematic complex application development framework",
                "components": [
                    "epic-workflow",
                    "problem-solving",
                    "architecture-design",
                    "architecture-lifecycle",
                    "execution-standards"
                ],
                "features": [
                    "hierarchical-task-management",
                    "systematic-troubleshooting",
                    "guided-architecture-design",
                    "quality-assurance-protocols",
                    "terminal-integration"
                ]
            },
            "claude_code": {
                "system_prompt_file": "framework-prompt.md",
                "auto_load_framework": True,
                "token_optimization": True,
                "terminal_capabilities": True,
                "agentic_development": True,
                "file_operations": True,
                "command_execution": True
            },
            "development_workflow": {
                "task_creation": "epic-workflow",
                "problem_resolution": "problem-solving-framework",
                "architecture_design": "architecture-design-process",
                "documentation": "architecture-lifecycle",
                "quality_assurance": "execution-standards"
            },
            "terminal_integration": {
                "file_management": True,
                "command_execution": True,
                "project_structure": True,
                "documentation_generation": True,
                "task_tracking": True
            }
        }
        
        # Claude Code uses framework-prompt.md for system prompt and claude-config.json for configuration
        # No need to copy separate framework files - everything goes in the main files
        
        with open(ide_dir / "framework-prompt.md", "w") as f:
            f.write(framework_prompt)
        
        import json
        with open(ide_dir / "claude-config.json", "w") as f:
            json.dump(claude_config, f, indent=2)
        
        print(f"✅ Created Claude Code configuration files")

    def create_trae_files(self, ide_dir):
        """Create Trae specific files."""
        # Read the full user-rules-template content for the framework context
        user_rules_file = self.generic_dir / "user-rules-template.md"
        with open(user_rules_file, 'r', encoding='utf-8') as f:
            user_rules_content = f.read()
        
        # Fix relative paths for Trae context
        user_rules_content = self.fix_relative_paths_for_ide(user_rules_content, "trae-specific")
        
        # Trae config
        trae_config = {
            "framework": {
                "name": "AI Epic Framework",
                "version": "1.0.0",
                "description": "Systematic complex application development framework"
            },
            "trae": {
                "ide_agnostic": True,
                "cross_platform": True,
                "framework_context_file": "framework-context.md",
                "multi_project_support": True
            },
            "components": {
                "epic_workflow": True,
                "problem_solving": True,
                "architecture_design": True,
                "architecture_lifecycle": True,
                "execution_standards": True
            },
            "cross_ide_features": {
                "consistent_behavior": True,
                "framework_persistence": True,
                "project_adaptation": True,
                "team_coordination": True
            }
        }
        
        # Framework context with full content
        framework_context = f"""# AI Epic Framework - Trae Context

## Cross-IDE Framework Integration
Trae enables consistent AI assistance across different development environments while maintaining the AI Epic Framework's structured approach.

{user_rules_content}

## Trae-Specific Integration
- **IDE Agnostic**: Framework works consistently across all supported IDEs
- **Cross Platform**: Maintains framework behavior across different operating systems
- **Multi Project**: Framework adapts to different project types and structures
- **Team Coordination**: Consistent framework usage across team members

## Usage Across IDEs
1. **Framework Persistence**: Framework rules and methodologies remain consistent
2. **Project Adaptation**: Framework adapts to different project structures and requirements
3. **Team Coordination**: All team members use the same framework approach
4. **IDE Switching**: Seamless framework experience when switching between IDEs

## Configuration
See `trae-config.yaml` for detailed configuration settings.
"""
        
        # Copy all framework files to Trae directory
        generic_files = [
            "epic-workflow-instructions.md",
            "problem-solving-framework.md",
            "architecture-design-process.md",
            "architecture-lifecycle.md",
            "general-execution-standards.md"
        ]
        
        for generic_file in generic_files:
            source_file = self.generic_dir / generic_file
            target_file = ide_dir / generic_file
            
            if source_file.exists():
                # Fix relative paths for Trae context
                with open(source_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                content = self.fix_relative_paths_for_ide(content, "trae-specific")
                
                with open(target_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"✅ Copied {generic_file} to Trae directory")
        
        import yaml
        with open(ide_dir / "trae-config.yaml", "w") as f:
            yaml.dump(trae_config, f, default_flow_style=False)
        
        with open(ide_dir / "framework-context.md", "w") as f:
            f.write(framework_context)
        
        print(f"✅ Created Trae configuration files")

    def create_kilo_code_files(self, ide_dir):
        """Create Kilo Code specific files using latest directory-based approach."""
        # Create .kilocode directory structure
        kilocode_dir = ide_dir / ".kilocode"
        kilocode_rules_dir = kilocode_dir / "rules"
        
        kilocode_rules_dir.mkdir(parents=True, exist_ok=True)
        
        # Read the full user-rules-template content for the custom instructions
        user_rules_file = self.generic_dir / "user-rules-template.md"
        with open(user_rules_file, 'r', encoding='utf-8') as f:
            user_rules_content = f.read()
        
        # Fix relative paths for Kilo Code context
        user_rules_content = self.fix_relative_paths_for_ide(user_rules_content, "kilo-code-specific")
        
        # Create main framework overview file
        framework_overview = f"""# AI Epic Framework - Kilo Code Rules

## Framework Overview
This project uses the AI Epic Framework for systematic complex application development.

{user_rules_content}

## Kilo Code Integration
- **Directory-Based Rules**: Framework rules stored in `.kilocode/rules/` directory
- **Privacy-Focused**: Framework operates with local AI models where possible
- **Open Source**: Complete transparency in framework implementation
- **VS Code Compatible**: Works seamlessly with VS Code extensions

## Framework Components
- **Epic Workflow**: Hierarchical task breakdown (Initiative → Epic → Phase → Step)
- **Problem Solving**: Systematic troubleshooting methodology
- **Architecture Design**: Guided architectural decision-making
- **Execution Standards**: Quality assurance and best practices

## Usage Guidelines
1. Use epic workflow for project breakdown and task organization
2. Apply problem-solving framework for complex technical issues
3. Use architecture design process for system planning and decisions
4. Follow execution standards for research and validation

## File Organization
- Framework files: `framework/` directory
- Documentation: `docs/` directory with comprehensive guides
- Task structure: `/.epic-workflows/tasks/` for hierarchical task management
- Architecture docs: `docs/architecture/` for system design documentation

## Privacy Features
- **Local Processing**: Framework operates with local AI models where possible
- **No Telemetry**: No data collection or tracking of framework usage
- **Open Source**: Complete transparency in framework implementation
- **Privacy First**: All framework operations prioritize user privacy
"""
        
        # Create epic workflow rules
        epic_workflow = """# Epic Workflow Rules

## Task Breakdown
- Use epic workflow for task breakdown (Initiative → Epic → Phase → Step)
- Create task hierarchy in `/.epic-workflows/tasks/`
- Use INDEX.md and REQUIREMENTS.md for each task
- Follow Plan → Document → Execute → Track → Validate sequence

## File Management
- Maintain architecture docs in `docs/architecture/`
- Use INDEX.md and REQUIREMENTS.md for each task
- Create task hierarchies with clear naming conventions
- Track progress and completion status

## Workflow Integration
- Integrate with existing project management tools
- Maintain consistency across team members
- Update task status regularly
- Document decisions and trade-offs
"""
        
        # Create problem solving rules
        problem_solving = """# Problem Solving Framework Rules

## When to Apply
- Apply problem-solving framework after 3+ failed attempts
- Use for multi-component system failures
- Apply for complex technical issues
- Use when explicitly requested

## Research Protocol
- Consult official documentation first
- Use Context7 and Perplexity for research
- Cross-check from multiple sources
- Document decisions and trade-offs

## Systematic Approach
- Follow Research → Decompose → Execute → Validate → Cleanup
- Create temporary files for investigation
- Use systematic research-driven approach
- Validate solutions thoroughly

## Quality Standards
- Plan thoroughly, implement incrementally
- Validate after each milestone
- Update architecture docs for significant changes
- Maintain comprehensive documentation
"""
        
        # Create architecture design rules
        architecture_design = """# Architecture Design Process Rules

## Design Methodology
- Use architecture design process for system design
- Start with requirements and constraints
- Research patterns and technologies
- Design components with clear boundaries

## Quality Attributes
- Plan for scalability, performance, security
- Consider reliability and observability
- Document decisions and trade-offs
- Validate architectural decisions

## Integration Patterns
- Use REST + OpenAPI for API design
- Consider event-driven patterns with Kafka/NATS
- Implement microservices with gRPC
- Plan for service mesh (Istio, Linkerd)

## Documentation
- Maintain architecture docs in `docs/architecture/`
- Create architecture decision records (ADRs)
- Document component boundaries and interfaces
- Keep architecture docs up to date
"""
        
        # Create execution standards rules
        execution_standards = """# Execution Standards Rules

## Quality Assurance
- Follow execution standards for quality assurance
- Research-first approach for all decisions
- Multi-source validation for information
- Quality over speed in all implementations

## Development Process
- Plan thoroughly before implementation
- Implement incrementally with validation
- Update documentation for all changes
- Maintain comprehensive project documentation

## Team Coordination
- Ensure consistency across team members
- Use framework standards for all projects
- Maintain framework documentation
- Coordinate framework updates across team

## Best Practices
- Follow established coding standards
- Use version control effectively
- Implement proper testing strategies
- Maintain security best practices
"""
        
        # Write files to .kilocode/rules directory
        with open(kilocode_rules_dir / "01-framework-overview.md", "w") as f:
            f.write(framework_overview)
        
        with open(kilocode_rules_dir / "02-epic-workflow.md", "w") as f:
            f.write(epic_workflow)
        
        with open(kilocode_rules_dir / "03-problem-solving.md", "w") as f:
            f.write(problem_solving)
        
        with open(kilocode_rules_dir / "04-architecture-design.md", "w") as f:
            f.write(architecture_design)
        
        with open(kilocode_rules_dir / "05-execution-standards.md", "w") as f:
            f.write(execution_standards)
        
        print(f"✅ Created Kilo Code configuration files with directory-based structure")

    def create_void_files(self, ide_dir):
        """Create Void IDE specific files."""
        # Read the full user-rules-template content for the system prompt
        user_rules_file = self.generic_dir / "user-rules-template.md"
        with open(user_rules_file, 'r', encoding='utf-8') as f:
            user_rules_content = f.read()
        
        # Fix relative paths for Void IDE context
        user_rules_content = self.fix_relative_paths_for_ide(user_rules_content, "void-specific")
        
        # Void config
        void_config = {
            "framework": {
                "name": "AI Epic Framework",
                "version": "1.0.0",
                "description": "Systematic complex application development framework"
            },
            "void_ide": {
                "privacy_conscious": True,
                "vscode_compatible": True,
                "local_ai_support": True,
                "offline_processing": True,
                "no_telemetry": True
            },
            "components": {
                "epic_workflow": True,
                "problem_solving": True,
                "architecture_design": True,
                "architecture_lifecycle": True,
                "execution_standards": True
            },
            "privacy_features": {
                "local_processing": True,
                "no_telemetry": True,
                "offline_capabilities": True,
                "data_minimization": True
            }
        }
        
        # Framework system prompt with full content
        system_prompt = f"""# AI Epic Framework - Void IDE System Prompt

## Privacy-Conscious AI Development
Void IDE provides privacy-focused AI assistance with local processing capabilities and the AI Epic Framework.

{user_rules_content}

## Void IDE Specific Features
- **Local AI Models**: Framework operates with local AI models for complete privacy
- **Offline Processing**: Framework works without internet connectivity
- **No Telemetry**: Zero data collection or tracking
- **VS Code Compatible**: Seamless integration with VS Code ecosystem

## Privacy-First Development
- **Local Processing**: All framework operations happen locally
- **Data Minimization**: Only essential data is processed
- **Offline Capabilities**: Framework functions without cloud dependencies
- **Privacy Controls**: Granular control over all data handling

## Configuration
See `void-config.json` and `privacy-rules.json` for detailed configuration settings.
"""
        
        # Privacy rules
        privacy_rules = {
            "privacy": {
                "local_processing": True,
                "no_telemetry": True,
                "data_minimization": True
            },
            "framework": {
                "epic_workflow": True,
                "problem_solving": True,
                "architecture_design": True,
                "execution_standards": True
            }
        }
        
        # Copy all framework files to Void IDE directory
        generic_files = [
            "epic-workflow-instructions.md",
            "problem-solving-framework.md",
            "architecture-design-process.md",
            "architecture-lifecycle.md",
            "general-execution-standards.md"
        ]
        
        for generic_file in generic_files:
            source_file = self.generic_dir / generic_file
            target_file = ide_dir / generic_file
            
            if source_file.exists():
                # Fix relative paths for Void IDE context
                with open(source_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                content = self.fix_relative_paths_for_ide(content, "void-specific")
                
                with open(target_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"✅ Copied {generic_file} to Void IDE directory")
        
        import json
        with open(ide_dir / "void-config.json", "w") as f:
            json.dump(void_config, f, indent=2)
        
        with open(ide_dir / "framework-system-prompt.md", "w") as f:
            f.write(system_prompt)
        
        with open(ide_dir / "privacy-rules.json", "w") as f:
            json.dump(privacy_rules, f, indent=2)
        
        print(f"✅ Created Void IDE configuration files")

    def create_zencoder_files(self, ide_dir):
        """Create Zencoder specific files."""
        # Read the full user-rules-template content for the framework rules
        user_rules_file = self.generic_dir / "user-rules-template.md"
        with open(user_rules_file, 'r', encoding='utf-8') as f:
            user_rules_content = f.read()
        
        # Fix relative paths for Zencoder context
        user_rules_content = self.fix_relative_paths_for_ide(user_rules_content, "zencoder-specific")
        
        # Framework rules with full content
        framework_rules = f"""# AI Epic Framework - Zencoder Rules

## Enterprise AI Development Framework
Zencoder provides enterprise-grade AI assistance with multi-format rule support and the AI Epic Framework.

{user_rules_content}

## Zencoder Enterprise Features
- **Multi-Format Support**: Framework rules in multiple formats (.rules, .cursorrules, .clinerules, etc.)
- **Team Coordination**: Enterprise-wide framework consistency
- **Security & Compliance**: Enterprise-grade security and compliance features
- **Analytics & Monitoring**: Framework usage analytics and performance monitoring
- **Scalability**: Framework scales across large enterprise teams

## Enterprise Integration
- **Multi-Team Support**: Framework coordination across multiple development teams
- **Centralized Management**: Centralized framework configuration and updates
- **Compliance Features**: Built-in compliance and governance features
- **Performance Monitoring**: Framework performance and usage analytics

## Configuration
See `enterprise-config.json` for detailed enterprise configuration settings.
"""
        
        # Enterprise config
        enterprise_config = {
            "framework": {
                "name": "AI Epic Framework",
                "version": "1.0.0"
            },
            "zencoder": {
                "enterprise": True,
                "multi_format": True,
                "team_coordination": True
            },
            "formats": {
                "rules": True,
                "cursorrules": True,
                "clinerules": True,
                "windsurfrules": True,
                "copilot": True
            }
        }
        
        # Compatibility files
        cursor_compatibility = """# Cursor AI Compatibility
Cursor AI compatible rules for the AI Epic Framework.
"""
        
        cline_compatibility = """# Cline Compatibility
Cline compatible rules for the AI Epic Framework.
"""
        
        windsurf_compatibility = """# Windsurf Compatibility
Windsurf compatible rules for the AI Epic Framework.
"""
        
        copilot_compatibility = """# GitHub Copilot Compatibility
GitHub Copilot compatible instructions for the AI Epic Framework.
"""
        
        # Copy all framework files to Zencoder directory
        generic_files = [
            "epic-workflow-instructions.md",
            "problem-solving-framework.md",
            "architecture-design-process.md",
            "architecture-lifecycle.md",
            "general-execution-standards.md"
        ]
        
        for generic_file in generic_files:
            source_file = self.generic_dir / generic_file
            target_file = ide_dir / generic_file
            
            if source_file.exists():
                # Fix relative paths for Zencoder context
                with open(source_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                content = self.fix_relative_paths_for_ide(content, "zencoder-specific")
                
                with open(target_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"✅ Copied {generic_file} to Zencoder directory")
        
        with open(ide_dir / "framework-rules.rules", "w") as f:
            f.write(framework_rules)
        
        import json
        with open(ide_dir / "enterprise-config.json", "w") as f:
            json.dump(enterprise_config, f, indent=2)
        
        with open(ide_dir / "cursor-compatibility.cursorrules", "w") as f:
            f.write(cursor_compatibility)
        
        with open(ide_dir / "cline-compatibility.clinerules", "w") as f:
            f.write(cline_compatibility)
        
        with open(ide_dir / "windsurf-compatibility.windsurfrules", "w") as f:
            f.write(windsurf_compatibility)
        
        with open(ide_dir / "copilot-compatibility.md", "w") as f:
            f.write(copilot_compatibility)
        
        print(f"✅ Created Zencoder configuration files")

    def create_gemini_files(self, ide_dir):
        """Create Gemini CLI specific files."""
        # Read the full user-rules-template content for the system prompt
        user_rules_file = self.generic_dir / "user-rules-template.md"
        with open(user_rules_file, 'r', encoding='utf-8') as f:
            user_rules_content = f.read()
        
        # Fix relative paths for Gemini CLI context
        user_rules_content = self.fix_relative_paths_for_ide(user_rules_content, "gemini-cli-specific")
        
        # GEMINI.md system prompt with full content
        gemini_prompt = f"""# AI Epic Framework - Gemini CLI System Prompt

## Google Ecosystem AI Development
Gemini CLI provides AI assistance with deep Google Cloud Platform and Google Workspace integration and the AI Epic Framework.

{user_rules_content}

## Gemini CLI Specific Features
- **Google Cloud Integration**: Framework optimized for Google Cloud Platform services
- **Google Workspace**: Integration with Google Docs, Sheets, and Drive
- **GCP-Native Design**: Framework patterns optimized for Google Cloud architecture
- **Google Cloud Build**: Automated framework deployment and CI/CD integration

## Google Ecosystem Integration
- **Google Cloud Platform**: Framework optimized for GCP services and patterns
- **Google Workspace**: Documentation and collaboration through Google Workspace
- **Google Cloud Build**: Automated framework deployment and testing
- **Google Cloud Monitoring**: Framework performance and usage monitoring

## GCP-Native Development
- **Cloud-Native Patterns**: Framework optimized for cloud-native development
- **GCP Services**: Integration with Compute Engine, Cloud Functions, Cloud Run, etc.
- **Google Cloud Security**: Framework security patterns aligned with GCP best practices
- **Scalability**: Framework designed for Google Cloud scalability patterns

## Configuration
See `gemini-config.json` and `google-cloud-integration.json` for detailed configuration settings.
"""
        
        # Gemini config
        gemini_config = {
            "framework": {
                "name": "AI Epic Framework",
                "version": "1.0.0"
            },
            "gemini_cli": {
                "google_ecosystem": True,
                "gcp_integration": True,
                "workspace_integration": True
            },
            "components": {
                "epic_workflow": True,
                "problem_solving": True,
                "architecture_design": True,
                "execution_standards": True
            }
        }
        
        # Google Cloud integration
        gcp_integration = {
            "google_cloud": {
                "services": [
                    "Compute Engine",
                    "Cloud Functions",
                    "Cloud Run",
                    "App Engine",
                    "Cloud Storage",
                    "Cloud SQL",
                    "Firestore",
                    "Pub/Sub"
                ],
                "monitoring": [
                    "Cloud Monitoring",
                    "Cloud Trace",
                    "Cloud Profiler"
                ],
                "workspace": [
                    "Google Docs",
                    "Google Sheets",
                    "Google Drive"
                ]
            }
        }
        
        # Copy all framework files to Gemini CLI directory
        generic_files = [
            "epic-workflow-instructions.md",
            "problem-solving-framework.md",
            "architecture-design-process.md",
            "architecture-lifecycle.md",
            "general-execution-standards.md"
        ]
        
        for generic_file in generic_files:
            source_file = self.generic_dir / generic_file
            target_file = ide_dir / generic_file
            
            if source_file.exists():
                # Fix relative paths for Gemini CLI context
                with open(source_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                content = self.fix_relative_paths_for_ide(content, "gemini-cli-specific")
                
                with open(target_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"✅ Copied {generic_file} to Gemini CLI directory")
        
        with open(ide_dir / "GEMINI.md", "w") as f:
            f.write(gemini_prompt)
        
        import json
        with open(ide_dir / "gemini-config.json", "w") as f:
            json.dump(gemini_config, f, indent=2)
        
        with open(ide_dir / "google-cloud-integration.json", "w") as f:
            json.dump(gcp_integration, f, indent=2)
        
        print(f"✅ Created Gemini CLI configuration files")

    def generate_all_adaptations(self):
        """Generate all IDE adaptations."""
        print("🚀 Generating AI Epic Framework IDE Adaptations...")
        print("=" * 60)
        
        # Create directories
        self.create_ide_directories()
        print()
        
        # Copy and adapt files
        self.copy_generic_files()
        print()
        
        print("✅ All IDE adaptations generated successfully!")
        print()
        print("📁 Generated adaptations:")
        for ide_name in self.ide_configs.keys():
            print(f"   - {ide_name}/")
        print()
        print("🎯 Next steps:")
        print("   1. Review the generated adaptations in framework/[ide]-specific/")
        print("   2. Customize any IDE-specific configurations as needed")
        print("   3. Test the adaptations with your target IDEs")
        print("   4. Update documentation if needed")

def main():
    """Main function to run the IDE adaptation generator."""
    generator = IDEAdaptationGenerator()
    generator.generate_all_adaptations()

if __name__ == "__main__":
    main() 