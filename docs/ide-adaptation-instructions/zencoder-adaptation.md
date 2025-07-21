# Zencoder Adaptation Instructions

## Overview
This document provides detailed instructions for adapting the AI Epic Framework to Zencoder's Zen Rules format. Zencoder uses `.zenrules` files with multi-format support and enterprise features.

## Zencoder Format Requirements
- **File Extension**: `.zenrules`
- **Content Style**: Multi-format support (JSON, YAML, Markdown)
- **Structure**: Enterprise-focused with comprehensive rules
- **Features**: Multi-format rule support, enterprise features

## Pre-Adaptation Setup

### Step 1: Clear Target Directory
```bash
# Remove existing content
rm -rf framework/zencoder-specific/*
```

### Step 2: Create Directory Structure
```bash
# Create the zencoder directory structure
mkdir -p framework/zencoder-specific
```

## Content Adaptation Process

### Step 1: Create Main Framework Rules File
Create `framework/zencoder-specific/.zenrules`:

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
      "examples": {
        "good": [
          "Initiative/Epic_001_User_Authentication/Phase_001_Setup/Step_001_Database_Design/",
          "INDEX.md with clear status tracking",
          "REQUIREMENTS.md with detailed acceptance criteria"
        ],
        "avoid": [
          "Flat directory structures",
          "Missing documentation files",
          "Unclear task dependencies"
        ]
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
      "examples": {
        "good": [
          "Comprehensive investigation logs",
          "Multiple solution attempts documented",
          "Clear decision rationale",
          "Validation test results"
        ],
        "avoid": [
          "Jumping to solutions without research",
          "Incomplete documentation",
          "Missing validation steps"
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
      "examples": {
        "good": [
          "Comprehensive technology evaluation",
          "Clear component interfaces",
          "Quality attribute analysis",
          "Integration pattern documentation"
        ],
        "avoid": [
          "Rushed architecture decisions",
          "Missing quality attribute consideration",
          "Poorly defined interfaces"
        ]
      }
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
      "examples": {
        "good": [
          "Systematic file verification",
          "Comprehensive tool usage",
          "Clear decision documentation",
          "Thorough testing procedures"
        ],
        "avoid": [
          "Skipping verification steps",
          "Incomplete tool usage",
          "Missing decision rationale"
        ]
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
      "examples": {
        "good": [
          "Conditional documentation loading",
          "Progressive disclosure approach",
          "Efficient context management",
          "Structured information organization"
        ],
        "avoid": [
          "Loading unnecessary context",
          "Poor information organization",
          "Inefficient token usage"
        ]
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
      "examples": {
        "good": [
          "Performance optimization strategies",
          "Scalable architecture design",
          "Comprehensive error handling",
          "Security best practices"
        ],
        "avoid": [
          "Ignoring performance implications",
          "Poor scalability planning",
          "Weak error handling",
          "Security vulnerabilities"
        ]
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
      ],
      "examples": {
        "good": [
          "Clear and comprehensive documentation",
          "Consistent formatting and structure",
          "Practical examples and use cases",
          "Up-to-date information"
        ],
        "avoid": [
          "Incomplete documentation",
          "Inconsistent formatting",
          "Missing examples",
          "Outdated information"
        ]
      }
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
      "examples": {
        "good": [
          "API-first design approach",
          "Event-driven architecture",
          "Microservices decomposition",
          "Appropriate data consistency models"
        ],
        "avoid": [
          "Implementation before API design",
          "Tight coupling between components",
          "Monolithic architecture",
          "Inconsistent data models"
        ]
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
      "examples": {
        "good": [
          "const Component = ({ prop }: ComponentProps) => { ... }",
          "const [state, setState] = useState<StateType>(initialState)",
          "Systematic problem-solving approach",
          "Proper error handling and logging"
        ],
        "avoid": [
          "class Component extends React.Component { ... }",
          "const Component = (props) => { ... }",
          "Generic engineering approaches",
          "Poor error handling"
        ]
      }
    }
  ],
  "enterprise": {
    "team_collaboration": true,
    "version_control": true,
    "audit_trail": true,
    "multi_format_support": true
  }
}
```

## Validation Steps

### Step 1: File Structure Verification
```bash
# Verify file structure
ls -la framework/zencoder-specific/
```

Expected files:
- `.zenrules`

### Step 2: Content Verification
- Verify all generic content is preserved
- Check that content follows Zencoder's JSON format
- Ensure no external dependencies or references
- Validate that all framework concepts are included

### Step 3: Format Verification
- Confirm file uses proper JSON syntax
- Verify content is organized logically
- Check that rules are actionable and clear
- Ensure JSON structure is valid

## Zencoder Specific Features

### Zen Rules (.zenrules)
- Rules are defined in structured JSON format
- Supports comprehensive rule definitions with conditions and instructions
- Enables precise targeting of specific file types and directories
- Provides clear rule organization and hierarchy

### Multi-Format Support
- Supports JSON, YAML, and Markdown formats
- Enables flexible rule configuration
- Maintains consistency across different formats
- Provides enterprise-grade rule management

### Enterprise Features
- Team collaboration support
- Version control integration
- Audit trail capabilities
- Comprehensive rule management
- Multi-format rule support

## Success Criteria

The Zencoder adaptation is successful when:
- The `.zenrules` file is created with all framework content
- Content preserves 100% of generic framework functionality
- Format follows Zencoder's JSON configuration approach
- Rules are actionable, clear, and well-organized
- JSON syntax is valid and properly structured
- Enterprise features are properly configured
- No external dependencies or references exist
- Framework functionality is identical to other IDE adaptations 

## Overview
This document provides detailed instructions for adapting the AI Epic Framework to Zencoder's Zen Rules format. Zencoder uses `.zenrules` files with multi-format support and enterprise features.

## Zencoder Format Requirements
- **File Extension**: `.zenrules`
- **Content Style**: Multi-format support (JSON, YAML, Markdown)
- **Structure**: Enterprise-focused with comprehensive rules
- **Features**: Multi-format rule support, enterprise features

## Pre-Adaptation Setup

### Step 1: Clear Target Directory
```bash
# Remove existing content
rm -rf framework/zencoder-specific/*
```

### Step 2: Create Directory Structure
```bash
# Create the zencoder directory structure
mkdir -p framework/zencoder-specific
```

## Content Adaptation Process

### Step 1: Create Main Framework Rules File
Create `framework/zencoder-specific/.zenrules`:

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
      "examples": {
        "good": [
          "Initiative/Epic_001_User_Authentication/Phase_001_Setup/Step_001_Database_Design/",
          "INDEX.md with clear status tracking",
          "REQUIREMENTS.md with detailed acceptance criteria"
        ],
        "avoid": [
          "Flat directory structures",
          "Missing documentation files",
          "Unclear task dependencies"
        ]
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
      "examples": {
        "good": [
          "Comprehensive investigation logs",
          "Multiple solution attempts documented",
          "Clear decision rationale",
          "Validation test results"
        ],
        "avoid": [
          "Jumping to solutions without research",
          "Incomplete documentation",
          "Missing validation steps"
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
      "examples": {
        "good": [
          "Comprehensive technology evaluation",
          "Clear component interfaces",
          "Quality attribute analysis",
          "Integration pattern documentation"
        ],
        "avoid": [
          "Rushed architecture decisions",
          "Missing quality attribute consideration",
          "Poorly defined interfaces"
        ]
      }
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
      "examples": {
        "good": [
          "Systematic file verification",
          "Comprehensive tool usage",
          "Clear decision documentation",
          "Thorough testing procedures"
        ],
        "avoid": [
          "Skipping verification steps",
          "Incomplete tool usage",
          "Missing decision rationale"
        ]
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
      "examples": {
        "good": [
          "Conditional documentation loading",
          "Progressive disclosure approach",
          "Efficient context management",
          "Structured information organization"
        ],
        "avoid": [
          "Loading unnecessary context",
          "Poor information organization",
          "Inefficient token usage"
        ]
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
      "examples": {
        "good": [
          "Performance optimization strategies",
          "Scalable architecture design",
          "Comprehensive error handling",
          "Security best practices"
        ],
        "avoid": [
          "Ignoring performance implications",
          "Poor scalability planning",
          "Weak error handling",
          "Security vulnerabilities"
        ]
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
      ],
      "examples": {
        "good": [
          "Clear and comprehensive documentation",
          "Consistent formatting and structure",
          "Practical examples and use cases",
          "Up-to-date information"
        ],
        "avoid": [
          "Incomplete documentation",
          "Inconsistent formatting",
          "Missing examples",
          "Outdated information"
        ]
      }
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
      "examples": {
        "good": [
          "API-first design approach",
          "Event-driven architecture",
          "Microservices decomposition",
          "Appropriate data consistency models"
        ],
        "avoid": [
          "Implementation before API design",
          "Tight coupling between components",
          "Monolithic architecture",
          "Inconsistent data models"
        ]
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
      "examples": {
        "good": [
          "const Component = ({ prop }: ComponentProps) => { ... }",
          "const [state, setState] = useState<StateType>(initialState)",
          "Systematic problem-solving approach",
          "Proper error handling and logging"
        ],
        "avoid": [
          "class Component extends React.Component { ... }",
          "const Component = (props) => { ... }",
          "Generic engineering approaches",
          "Poor error handling"
        ]
      }
    }
  ],
  "enterprise": {
    "team_collaboration": true,
    "version_control": true,
    "audit_trail": true,
    "multi_format_support": true
  }
}
```

## Validation Steps

### Step 1: File Structure Verification
```bash
# Verify file structure
ls -la framework/zencoder-specific/
```

Expected files:
- `.zenrules`

### Step 2: Content Verification
- Verify all generic content is preserved
- Check that content follows Zencoder's JSON format
- Ensure no external dependencies or references
- Validate that all framework concepts are included

### Step 3: Format Verification
- Confirm file uses proper JSON syntax
- Verify content is organized logically
- Check that rules are actionable and clear
- Ensure JSON structure is valid

## Zencoder Specific Features

### Zen Rules (.zenrules)
- Rules are defined in structured JSON format
- Supports comprehensive rule definitions with conditions and instructions
- Enables precise targeting of specific file types and directories
- Provides clear rule organization and hierarchy

### Multi-Format Support
- Supports JSON, YAML, and Markdown formats
- Enables flexible rule configuration
- Maintains consistency across different formats
- Provides enterprise-grade rule management

### Enterprise Features
- Team collaboration support
- Version control integration
- Audit trail capabilities
- Comprehensive rule management
- Multi-format rule support

## Success Criteria

The Zencoder adaptation is successful when:
- The `.zenrules` file is created with all framework content
- Content preserves 100% of generic framework functionality
- Format follows Zencoder's JSON configuration approach
- Rules are actionable, clear, and well-organized
- JSON syntax is valid and properly structured
- Enterprise features are properly configured
- No external dependencies or references exist
- Framework functionality is identical to other IDE adaptations 