# Void IDE Adaptation Instructions

## Overview
This document provides detailed instructions for adapting the AI Epic Framework to Void IDE's JSON configuration format. Void IDE uses JSON configuration files with a privacy-focused approach and enterprise features.

## Void IDE Format Requirements
- **File Format**: JSON configuration files
- **Content Style**: Structured JSON with rules and conditions
- **Privacy**: Local processing, no external dependencies
- **Structure**: Enterprise-focused configuration with comprehensive rules

## Pre-Adaptation Setup

### Step 1: Clear Target Directory
```bash
# Remove existing content
rm -rf framework/void-ide-specific/*
```

### Step 2: Create Directory Structure
```bash
# Create the void ide directory structure
mkdir -p framework/void-ide-specific
```

## Content Adaptation Process

### Step 1: Create Main Framework Configuration File
Create `framework/void-ide-specific/ai-epic-framework.json`:

```json
{
  "version": "1.0",
  "name": "AI Epic Framework",
  "description": "Systematic approaches for AI assistants to help developers build complex applications",
  "framework": {
    "overview": "The AI Epic Framework provides systematic approaches for AI assistants to help developers build complex applications through structured workflows, problem-solving methodologies, and architecture design processes",
    "core_principles": [
      "Use systematic problem-solving approaches for complex issues",
      "Implement hierarchical task breakdown (Initiative → Epic → Phase → Step)",
      "Apply research-first methodology for architecture decisions",
      "Maintain comprehensive documentation and context management",
      "Focus on AI framework application rather than generic engineering principles"
    ]
  },
  "rules": [
    {
      "name": "epic_workflow_management",
      "description": "Task hierarchy and workflow management",
      "priority": "high",
      "conditions": {
        "filePatterns": ["INDEX.md", "REQUIREMENTS.md"],
        "directories": ["Epic_*", "Phase_*", "Step_*"],
        "exclude": ["node_modules/", "dist/", "build/"]
      },
      "instructions": [
        "Break down complex projects into manageable epics",
        "Use INDEX.md and REQUIREMENTS.md templates for task organization",
        "Implement systematic delegation and execution flows",
        "Maintain progress tracking and status management",
        "Follow task hierarchy structure: Initiative/Epic_001_Task_Name/Phase_001_Phase_Name/Step_001_Step_Name/",
        "Create INDEX.md with Overview, Status, Dependencies, Deliverables, and Notes sections",
        "Create REQUIREMENTS.md with Functional Requirements, Technical Requirements, Acceptance Criteria, and Constraints sections"
      ],
      "templates": {
        "index_md": {
          "name": "INDEX.md Template",
          "content": "# [Task Name] - Index\n\n## Overview\nBrief description of the task and its objectives.\n\n## Status\n- [ ] Not Started\n- [ ] In Progress\n- [ ] Completed\n- [ ] Blocked\n\n## Dependencies\nList any dependencies or prerequisites.\n\n## Deliverables\nList expected outputs and deliverables.\n\n## Notes\nAdditional context and information."
        },
        "requirements_md": {
          "name": "REQUIREMENTS.md Template",
          "content": "# [Task Name] - Requirements\n\n## Functional Requirements\n- [Requirement 1]\n- [Requirement 2]\n\n## Technical Requirements\n- [Technical requirement 1]\n- [Technical requirement 2]\n\n## Acceptance Criteria\n- [Criterion 1]\n- [Criterion 2]\n\n## Constraints\n- [Constraint 1]\n- [Constraint 2]"
        }
      }
    },
    {
      "name": "problem_solving_framework",
      "description": "Systematic analysis for stubborn technical issues",
      "priority": "high",
      "conditions": {
        "filePatterns": ["*.log", "error*.md", "debug*.md", "investigation*.md"],
        "directories": ["investigation*", "debug*"],
        "exclude": ["node_modules/", "dist/", "build/"]
      },
      "instructions": [
        "Apply systematic analysis for stubborn technical issues",
        "Use research-first approach before solution implementation",
        "Document investigation processes and findings",
        "Implement solution validation and verification",
        "Follow systematic analysis process: Problem Identification → Research Phase → Root Cause Analysis → Solution Development → Implementation → Verification",
        "Always research before implementing solutions",
        "Use multiple information sources (documentation, examples, community)",
        "Document findings and decision rationale",
        "Validate assumptions through testing",
        "Record all research steps and findings",
        "Document failed attempts and lessons learned",
        "Test solutions in isolated environments",
        "Verify all requirements are met"
      ],
      "process": {
        "steps": [
          "Problem Identification: Clearly define the issue and scope",
          "Research Phase: Gather comprehensive information and context",
          "Root Cause Analysis: Identify underlying causes and dependencies",
          "Solution Development: Create systematic solution approaches",
          "Implementation: Execute solutions with validation",
          "Verification: Confirm resolution and document learnings"
        ]
      }
    },
    {
      "name": "architecture_design_process",
      "description": "Research methodology for architecture decisions",
      "priority": "high",
      "conditions": {
        "filePatterns": ["architecture*.md", "design*.md", "system*.md"],
        "directories": ["arch*", "design*", "system*"],
        "exclude": ["node_modules/", "dist/", "build/"]
      },
      "instructions": [
        "Follow research methodology for architecture decisions",
        "Use component design templates and integration patterns",
        "Implement quality attribute analysis and trade-off evaluation",
        "Maintain architecture documentation lifecycle",
        "Follow research methodology: Technology Evaluation → Requirement Analysis → Constraint Identification → Pattern Selection → Validation",
        "Define service components with interfaces, responsibilities, and dependencies",
        "Design data components with data models, storage, and access patterns",
        "Plan integration components with communication protocols and APIs",
        "Implement security components with authentication, authorization, and data protection",
        "Consider quality attributes: Performance, Scalability, Reliability, Security, Maintainability",
        "Use integration patterns: API-First Design, Event-Driven Architecture, Microservices, Data Consistency"
      ],
      "components": {
        "service": "Define interfaces, responsibilities, and dependencies",
        "data": "Design data models, storage, and access patterns",
        "integration": "Plan communication protocols and APIs",
        "security": "Implement authentication, authorization, and data protection"
      },
      "quality_attributes": [
        "Performance: Response time, throughput, and resource utilization",
        "Scalability: Horizontal and vertical scaling capabilities",
        "Reliability: Fault tolerance and error handling",
        "Security: Data protection and access control",
        "Maintainability: Code organization and documentation"
      ]
    },
    {
      "name": "execution_standards",
      "description": "File navigation and verification procedures",
      "priority": "medium",
      "conditions": {
        "filePatterns": ["*.py", "*.js", "*.ts", "*.java", "*.go", "*.rs"],
        "directories": ["src/", "components/", "services/"],
        "exclude": ["node_modules/", "dist/", "build/"]
      },
      "instructions": [
        "Follow file navigation and verification procedures",
        "Use appropriate tools (Context7, Perplexity, Web search)",
        "Implement decision-making protocols and documentation requirements",
        "Maintain quality assurance and execution methodology",
        "Always verify file existence before operations",
        "Use appropriate tools for file discovery and search",
        "Maintain organized directory structures",
        "Document file relationships and dependencies",
        "Use Context7 for library documentation and API references",
        "Use Perplexity for research and information gathering",
        "Use Web Search for current information and examples",
        "Document decision rationale and alternatives considered",
        "Use systematic evaluation criteria",
        "Consider long-term implications and maintenance",
        "Validate decisions through testing and feedback",
        "Implement comprehensive testing strategies",
        "Use code review and validation processes",
        "Maintain documentation standards",
        "Follow established coding conventions"
      ],
      "tools": {
        "context7": "Library documentation and API references",
        "perplexity": "Research and information gathering",
        "web_search": "Current information and examples",
        "file_operations": "File discovery and management"
      }
    },
    {
      "name": "context_management",
      "description": "Token optimization and context window management",
      "priority": "medium",
      "conditions": {
        "filePatterns": ["*.md", "*.txt"],
        "directories": ["docs*", "documentation*"],
        "exclude": ["node_modules/", "dist/", "build/"]
      },
      "instructions": [
        "Optimize token usage through conditional documentation loading",
        "Use progressive disclosure for complex investigations",
        "Maintain context window efficiency",
        "Implement task-specific guidance systems",
        "Load documentation conditionally based on task requirements",
        "Use progressive disclosure for complex investigations",
        "Prioritize active task information",
        "Unload unnecessary context when possible",
        "Load epic workflow instructions for workflow management",
        "Load problem-solving framework for problem solving",
        "Load architecture design process for architecture design",
        "Load execution standards for general tasks",
        "Monitor token usage and context window capacity",
        "Prioritize essential information for current task",
        "Use efficient information retrieval strategies",
        "Maintain context continuity across sessions",
        "Structure information hierarchically",
        "Use clear categorization and tagging",
        "Implement efficient search and retrieval",
        "Maintain information currency and accuracy"
      ],
      "conditional_loading": {
        "workflow_management": "Load epic workflow instructions",
        "problem_solving": "Load problem-solving framework",
        "architecture_design": "Load architecture design process",
        "general_tasks": "Load execution standards"
      }
    },
    {
      "name": "quality_attributes",
      "description": "Performance, scalability, reliability, security, and maintainability",
      "priority": "medium",
      "conditions": {
        "filePatterns": ["*.config.*", "*.conf", "dockerfile*", "*.yml", "*.yaml"],
        "directories": ["config/", "deploy/", "infrastructure/"],
        "exclude": ["node_modules/", "dist/", "build/"]
      },
      "instructions": [
        "Consider performance: Response time, throughput, and resource utilization",
        "Consider scalability: Horizontal and vertical scaling capabilities",
        "Consider reliability: Fault tolerance and error handling",
        "Consider security: Data protection and access control",
        "Consider maintainability: Code organization and documentation",
        "Implement appropriate performance optimizations",
        "Design for horizontal and vertical scaling",
        "Implement fault tolerance and error handling",
        "Ensure data protection and access control",
        "Maintain code organization and documentation"
      ],
      "attributes": {
        "performance": "Response time, throughput, and resource utilization",
        "scalability": "Horizontal and vertical scaling capabilities",
        "reliability": "Fault tolerance and error handling",
        "security": "Data protection and access control",
        "maintainability": "Code organization and documentation"
      }
    },
    {
      "name": "documentation_standards",
      "description": "Clear and comprehensive documentation requirements",
      "priority": "medium",
      "conditions": {
        "filePatterns": ["README*.md", "*.md", "docs/*.md"],
        "directories": ["docs/", "documentation/"],
        "exclude": ["node_modules/", "dist/", "build/"]
      },
      "instructions": [
        "Create clear and comprehensive documentation",
        "Use consistent formatting and structure",
        "Include examples and use cases",
        "Maintain up-to-date information",
        "Follow the framework's documentation standards",
        "Use consistent markdown formatting",
        "Include practical examples and use cases",
        "Keep documentation current and accurate",
        "Follow established documentation patterns",
        "Include troubleshooting and FAQ sections"
      ]
    },
    {
      "name": "integration_patterns",
      "description": "API-first design, event-driven architecture, microservices, and data consistency",
      "priority": "medium",
      "conditions": {
        "filePatterns": ["api*.md", "service*.md", "*.proto", "*.json"],
        "directories": ["api/", "services/", "microservices/"],
        "exclude": ["node_modules/", "dist/", "build/"]
      },
      "instructions": [
        "Use API-First Design: Design interfaces before implementation",
        "Use Event-Driven Architecture: Use events for loose coupling",
        "Use Microservices: Decompose into focused, independent services",
        "Use Data Consistency: Implement appropriate consistency models",
        "Design APIs before implementing functionality",
        "Use events for loose coupling between components",
        "Decompose systems into focused, independent services",
        "Implement appropriate data consistency models",
        "Define clear service boundaries and interfaces",
        "Use appropriate communication protocols"
      ],
      "patterns": {
        "api_first": "Design interfaces before implementation",
        "event_driven": "Use events for loose coupling",
        "microservices": "Decompose into focused, independent services",
        "data_consistency": "Implement appropriate consistency models"
      }
    },
    {
      "name": "coding_standards",
      "description": "Framework-based coding standards and practices",
      "priority": "high",
      "conditions": {
        "filePatterns": ["*.py", "*.js", "*.ts", "*.java", "*.go", "*.rs"],
        "directories": ["src/", "components/", "services/"],
        "exclude": ["node_modules/", "dist/", "build/"]
      },
      "instructions": [
        "Follow the framework's systematic approach to problem-solving",
        "Implement proper documentation and context management",
        "Use research-first methodology for complex decisions",
        "Maintain quality attributes in all implementations",
        "Focus on AI framework application rather than generic engineering principles",
        "Use TypeScript for all new code when applicable",
        "Write unit tests for business logic",
        "Follow component naming conventions",
        "Use established error handling patterns",
        "Apply the AI Epic Framework systematically",
        "Maintain code quality and readability",
        "Follow language-specific best practices",
        "Implement proper error handling and logging",
        "Use appropriate design patterns",
        "Maintain consistent coding style"
      ],
      "standards": {
        "typescript": "Use TypeScript for all new code when applicable",
        "testing": "Write unit tests for business logic",
        "naming": "Follow component naming conventions",
        "error_handling": "Use established error handling patterns",
        "quality": "Maintain code quality and readability"
      }
    }
  ],
  "settings": {
    "privacy": {
      "local_processing": true,
      "no_external_dependencies": true,
      "data_protection": true
    },
    "enterprise": {
      "team_collaboration": true,
      "version_control": true,
      "audit_trail": true
    }
  }
}
```

## Validation Steps

### Step 1: File Structure Verification
```bash
# Verify file structure
ls -la framework/void-ide-specific/
```

Expected files:
- `ai-epic-framework.json`

### Step 2: Content Verification
- Verify all generic content is preserved
- Check that content follows Void IDE's JSON format
- Ensure no external dependencies or references
- Validate that all framework concepts are included

### Step 3: Format Verification
- Confirm file uses proper JSON syntax
- Verify content is organized logically
- Check that rules are actionable and clear
- Ensure JSON structure is valid

## Void IDE Specific Features

### JSON Configuration
- Rules are defined in structured JSON format
- Supports comprehensive rule definitions with conditions and instructions
- Enables precise targeting of specific file types and directories
- Provides clear rule organization and hierarchy

### Privacy-Focused Processing
- All rules are processed locally
- No external API calls or dependencies
- Maintains user privacy and data security
- Works offline without internet connectivity

### Enterprise Features
- Team collaboration support
- Version control integration
- Audit trail capabilities
- Comprehensive rule management

## Success Criteria

The Void IDE adaptation is successful when:
- The `ai-epic-framework.json` file is created with all framework content
- Content preserves 100% of generic framework functionality
- Format follows Void IDE's JSON configuration approach
- Rules are actionable, clear, and well-organized
- JSON syntax is valid and properly structured
- Privacy-focused approach is maintained
- No external dependencies or references exist
- Framework functionality is identical to other IDE adaptations 

## Overview
This document provides detailed instructions for adapting the AI Epic Framework to Void IDE's JSON configuration format. Void IDE uses JSON configuration files with a privacy-focused approach and enterprise features.

## Void IDE Format Requirements
- **File Format**: JSON configuration files
- **Content Style**: Structured JSON with rules and conditions
- **Privacy**: Local processing, no external dependencies
- **Structure**: Enterprise-focused configuration with comprehensive rules

## Pre-Adaptation Setup

### Step 1: Clear Target Directory
```bash
# Remove existing content
rm -rf framework/void-ide-specific/*
```

### Step 2: Create Directory Structure
```bash
# Create the void ide directory structure
mkdir -p framework/void-ide-specific
```

## Content Adaptation Process

### Step 1: Create Main Framework Configuration File
Create `framework/void-ide-specific/ai-epic-framework.json`:

```json
{
  "version": "1.0",
  "name": "AI Epic Framework",
  "description": "Systematic approaches for AI assistants to help developers build complex applications",
  "framework": {
    "overview": "The AI Epic Framework provides systematic approaches for AI assistants to help developers build complex applications through structured workflows, problem-solving methodologies, and architecture design processes",
    "core_principles": [
      "Use systematic problem-solving approaches for complex issues",
      "Implement hierarchical task breakdown (Initiative → Epic → Phase → Step)",
      "Apply research-first methodology for architecture decisions",
      "Maintain comprehensive documentation and context management",
      "Focus on AI framework application rather than generic engineering principles"
    ]
  },
  "rules": [
    {
      "name": "epic_workflow_management",
      "description": "Task hierarchy and workflow management",
      "priority": "high",
      "conditions": {
        "filePatterns": ["INDEX.md", "REQUIREMENTS.md"],
        "directories": ["Epic_*", "Phase_*", "Step_*"],
        "exclude": ["node_modules/", "dist/", "build/"]
      },
      "instructions": [
        "Break down complex projects into manageable epics",
        "Use INDEX.md and REQUIREMENTS.md templates for task organization",
        "Implement systematic delegation and execution flows",
        "Maintain progress tracking and status management",
        "Follow task hierarchy structure: Initiative/Epic_001_Task_Name/Phase_001_Phase_Name/Step_001_Step_Name/",
        "Create INDEX.md with Overview, Status, Dependencies, Deliverables, and Notes sections",
        "Create REQUIREMENTS.md with Functional Requirements, Technical Requirements, Acceptance Criteria, and Constraints sections"
      ],
      "templates": {
        "index_md": {
          "name": "INDEX.md Template",
          "content": "# [Task Name] - Index\n\n## Overview\nBrief description of the task and its objectives.\n\n## Status\n- [ ] Not Started\n- [ ] In Progress\n- [ ] Completed\n- [ ] Blocked\n\n## Dependencies\nList any dependencies or prerequisites.\n\n## Deliverables\nList expected outputs and deliverables.\n\n## Notes\nAdditional context and information."
        },
        "requirements_md": {
          "name": "REQUIREMENTS.md Template",
          "content": "# [Task Name] - Requirements\n\n## Functional Requirements\n- [Requirement 1]\n- [Requirement 2]\n\n## Technical Requirements\n- [Technical requirement 1]\n- [Technical requirement 2]\n\n## Acceptance Criteria\n- [Criterion 1]\n- [Criterion 2]\n\n## Constraints\n- [Constraint 1]\n- [Constraint 2]"
        }
      }
    },
    {
      "name": "problem_solving_framework",
      "description": "Systematic analysis for stubborn technical issues",
      "priority": "high",
      "conditions": {
        "filePatterns": ["*.log", "error*.md", "debug*.md", "investigation*.md"],
        "directories": ["investigation*", "debug*"],
        "exclude": ["node_modules/", "dist/", "build/"]
      },
      "instructions": [
        "Apply systematic analysis for stubborn technical issues",
        "Use research-first approach before solution implementation",
        "Document investigation processes and findings",
        "Implement solution validation and verification",
        "Follow systematic analysis process: Problem Identification → Research Phase → Root Cause Analysis → Solution Development → Implementation → Verification",
        "Always research before implementing solutions",
        "Use multiple information sources (documentation, examples, community)",
        "Document findings and decision rationale",
        "Validate assumptions through testing",
        "Record all research steps and findings",
        "Document failed attempts and lessons learned",
        "Test solutions in isolated environments",
        "Verify all requirements are met"
      ],
      "process": {
        "steps": [
          "Problem Identification: Clearly define the issue and scope",
          "Research Phase: Gather comprehensive information and context",
          "Root Cause Analysis: Identify underlying causes and dependencies",
          "Solution Development: Create systematic solution approaches",
          "Implementation: Execute solutions with validation",
          "Verification: Confirm resolution and document learnings"
        ]
      }
    },
    {
      "name": "architecture_design_process",
      "description": "Research methodology for architecture decisions",
      "priority": "high",
      "conditions": {
        "filePatterns": ["architecture*.md", "design*.md", "system*.md"],
        "directories": ["arch*", "design*", "system*"],
        "exclude": ["node_modules/", "dist/", "build/"]
      },
      "instructions": [
        "Follow research methodology for architecture decisions",
        "Use component design templates and integration patterns",
        "Implement quality attribute analysis and trade-off evaluation",
        "Maintain architecture documentation lifecycle",
        "Follow research methodology: Technology Evaluation → Requirement Analysis → Constraint Identification → Pattern Selection → Validation",
        "Define service components with interfaces, responsibilities, and dependencies",
        "Design data components with data models, storage, and access patterns",
        "Plan integration components with communication protocols and APIs",
        "Implement security components with authentication, authorization, and data protection",
        "Consider quality attributes: Performance, Scalability, Reliability, Security, Maintainability",
        "Use integration patterns: API-First Design, Event-Driven Architecture, Microservices, Data Consistency"
      ],
      "components": {
        "service": "Define interfaces, responsibilities, and dependencies",
        "data": "Design data models, storage, and access patterns",
        "integration": "Plan communication protocols and APIs",
        "security": "Implement authentication, authorization, and data protection"
      },
      "quality_attributes": [
        "Performance: Response time, throughput, and resource utilization",
        "Scalability: Horizontal and vertical scaling capabilities",
        "Reliability: Fault tolerance and error handling",
        "Security: Data protection and access control",
        "Maintainability: Code organization and documentation"
      ]
    },
    {
      "name": "execution_standards",
      "description": "File navigation and verification procedures",
      "priority": "medium",
      "conditions": {
        "filePatterns": ["*.py", "*.js", "*.ts", "*.java", "*.go", "*.rs"],
        "directories": ["src/", "components/", "services/"],
        "exclude": ["node_modules/", "dist/", "build/"]
      },
      "instructions": [
        "Follow file navigation and verification procedures",
        "Use appropriate tools (Context7, Perplexity, Web search)",
        "Implement decision-making protocols and documentation requirements",
        "Maintain quality assurance and execution methodology",
        "Always verify file existence before operations",
        "Use appropriate tools for file discovery and search",
        "Maintain organized directory structures",
        "Document file relationships and dependencies",
        "Use Context7 for library documentation and API references",
        "Use Perplexity for research and information gathering",
        "Use Web Search for current information and examples",
        "Document decision rationale and alternatives considered",
        "Use systematic evaluation criteria",
        "Consider long-term implications and maintenance",
        "Validate decisions through testing and feedback",
        "Implement comprehensive testing strategies",
        "Use code review and validation processes",
        "Maintain documentation standards",
        "Follow established coding conventions"
      ],
      "tools": {
        "context7": "Library documentation and API references",
        "perplexity": "Research and information gathering",
        "web_search": "Current information and examples",
        "file_operations": "File discovery and management"
      }
    },
    {
      "name": "context_management",
      "description": "Token optimization and context window management",
      "priority": "medium",
      "conditions": {
        "filePatterns": ["*.md", "*.txt"],
        "directories": ["docs*", "documentation*"],
        "exclude": ["node_modules/", "dist/", "build/"]
      },
      "instructions": [
        "Optimize token usage through conditional documentation loading",
        "Use progressive disclosure for complex investigations",
        "Maintain context window efficiency",
        "Implement task-specific guidance systems",
        "Load documentation conditionally based on task requirements",
        "Use progressive disclosure for complex investigations",
        "Prioritize active task information",
        "Unload unnecessary context when possible",
        "Load epic workflow instructions for workflow management",
        "Load problem-solving framework for problem solving",
        "Load architecture design process for architecture design",
        "Load execution standards for general tasks",
        "Monitor token usage and context window capacity",
        "Prioritize essential information for current task",
        "Use efficient information retrieval strategies",
        "Maintain context continuity across sessions",
        "Structure information hierarchically",
        "Use clear categorization and tagging",
        "Implement efficient search and retrieval",
        "Maintain information currency and accuracy"
      ],
      "conditional_loading": {
        "workflow_management": "Load epic workflow instructions",
        "problem_solving": "Load problem-solving framework",
        "architecture_design": "Load architecture design process",
        "general_tasks": "Load execution standards"
      }
    },
    {
      "name": "quality_attributes",
      "description": "Performance, scalability, reliability, security, and maintainability",
      "priority": "medium",
      "conditions": {
        "filePatterns": ["*.config.*", "*.conf", "dockerfile*", "*.yml", "*.yaml"],
        "directories": ["config/", "deploy/", "infrastructure/"],
        "exclude": ["node_modules/", "dist/", "build/"]
      },
      "instructions": [
        "Consider performance: Response time, throughput, and resource utilization",
        "Consider scalability: Horizontal and vertical scaling capabilities",
        "Consider reliability: Fault tolerance and error handling",
        "Consider security: Data protection and access control",
        "Consider maintainability: Code organization and documentation",
        "Implement appropriate performance optimizations",
        "Design for horizontal and vertical scaling",
        "Implement fault tolerance and error handling",
        "Ensure data protection and access control",
        "Maintain code organization and documentation"
      ],
      "attributes": {
        "performance": "Response time, throughput, and resource utilization",
        "scalability": "Horizontal and vertical scaling capabilities",
        "reliability": "Fault tolerance and error handling",
        "security": "Data protection and access control",
        "maintainability": "Code organization and documentation"
      }
    },
    {
      "name": "documentation_standards",
      "description": "Clear and comprehensive documentation requirements",
      "priority": "medium",
      "conditions": {
        "filePatterns": ["README*.md", "*.md", "docs/*.md"],
        "directories": ["docs/", "documentation/"],
        "exclude": ["node_modules/", "dist/", "build/"]
      },
      "instructions": [
        "Create clear and comprehensive documentation",
        "Use consistent formatting and structure",
        "Include examples and use cases",
        "Maintain up-to-date information",
        "Follow the framework's documentation standards",
        "Use consistent markdown formatting",
        "Include practical examples and use cases",
        "Keep documentation current and accurate",
        "Follow established documentation patterns",
        "Include troubleshooting and FAQ sections"
      ]
    },
    {
      "name": "integration_patterns",
      "description": "API-first design, event-driven architecture, microservices, and data consistency",
      "priority": "medium",
      "conditions": {
        "filePatterns": ["api*.md", "service*.md", "*.proto", "*.json"],
        "directories": ["api/", "services/", "microservices/"],
        "exclude": ["node_modules/", "dist/", "build/"]
      },
      "instructions": [
        "Use API-First Design: Design interfaces before implementation",
        "Use Event-Driven Architecture: Use events for loose coupling",
        "Use Microservices: Decompose into focused, independent services",
        "Use Data Consistency: Implement appropriate consistency models",
        "Design APIs before implementing functionality",
        "Use events for loose coupling between components",
        "Decompose systems into focused, independent services",
        "Implement appropriate data consistency models",
        "Define clear service boundaries and interfaces",
        "Use appropriate communication protocols"
      ],
      "patterns": {
        "api_first": "Design interfaces before implementation",
        "event_driven": "Use events for loose coupling",
        "microservices": "Decompose into focused, independent services",
        "data_consistency": "Implement appropriate consistency models"
      }
    },
    {
      "name": "coding_standards",
      "description": "Framework-based coding standards and practices",
      "priority": "high",
      "conditions": {
        "filePatterns": ["*.py", "*.js", "*.ts", "*.java", "*.go", "*.rs"],
        "directories": ["src/", "components/", "services/"],
        "exclude": ["node_modules/", "dist/", "build/"]
      },
      "instructions": [
        "Follow the framework's systematic approach to problem-solving",
        "Implement proper documentation and context management",
        "Use research-first methodology for complex decisions",
        "Maintain quality attributes in all implementations",
        "Focus on AI framework application rather than generic engineering principles",
        "Use TypeScript for all new code when applicable",
        "Write unit tests for business logic",
        "Follow component naming conventions",
        "Use established error handling patterns",
        "Apply the AI Epic Framework systematically",
        "Maintain code quality and readability",
        "Follow language-specific best practices",
        "Implement proper error handling and logging",
        "Use appropriate design patterns",
        "Maintain consistent coding style"
      ],
      "standards": {
        "typescript": "Use TypeScript for all new code when applicable",
        "testing": "Write unit tests for business logic",
        "naming": "Follow component naming conventions",
        "error_handling": "Use established error handling patterns",
        "quality": "Maintain code quality and readability"
      }
    }
  ],
  "settings": {
    "privacy": {
      "local_processing": true,
      "no_external_dependencies": true,
      "data_protection": true
    },
    "enterprise": {
      "team_collaboration": true,
      "version_control": true,
      "audit_trail": true
    }
  }
}
```

## Validation Steps

### Step 1: File Structure Verification
```bash
# Verify file structure
ls -la framework/void-ide-specific/
```

Expected files:
- `ai-epic-framework.json`

### Step 2: Content Verification
- Verify all generic content is preserved
- Check that content follows Void IDE's JSON format
- Ensure no external dependencies or references
- Validate that all framework concepts are included

### Step 3: Format Verification
- Confirm file uses proper JSON syntax
- Verify content is organized logically
- Check that rules are actionable and clear
- Ensure JSON structure is valid

## Void IDE Specific Features

### JSON Configuration
- Rules are defined in structured JSON format
- Supports comprehensive rule definitions with conditions and instructions
- Enables precise targeting of specific file types and directories
- Provides clear rule organization and hierarchy

### Privacy-Focused Processing
- All rules are processed locally
- No external API calls or dependencies
- Maintains user privacy and data security
- Works offline without internet connectivity

### Enterprise Features
- Team collaboration support
- Version control integration
- Audit trail capabilities
- Comprehensive rule management

## Success Criteria

The Void IDE adaptation is successful when:
- The `ai-epic-framework.json` file is created with all framework content
- Content preserves 100% of generic framework functionality
- Format follows Void IDE's JSON configuration approach
- Rules are actionable, clear, and well-organized
- JSON syntax is valid and properly structured
- Privacy-focused approach is maintained
- No external dependencies or references exist
- Framework functionality is identical to other IDE adaptations 