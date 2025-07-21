# Zencoder Rules Documentation

## Overview
Zencoder provides a comprehensive rules system that allows you to customize AI behavior across different contexts and projects. The rules system supports multiple formats and provides flexible configuration options for enterprise environments.

## Rule Types and Formats

### Zen Rules (.zenrules)
Zen Rules are the primary format for Zencoder rules. These are JSON-based configuration files that provide structured rule definitions with advanced features.

**Location**: `.zenrules` in project root or `.zencoder/rules/` directory

### Multi-Format Support
Zencoder supports multiple rule formats for compatibility:
- **Zen Rules** (`.zenrules`) - Native Zencoder format
- **Cursor Rules** (`.cursorrules`) - Cursor AI compatibility
- **Claude Rules** (`.claude-rules`) - Claude AI compatibility
- **GitHub Copilot** (`.github/copilot-instructions.md`) - GitHub Copilot compatibility

## Zen Rules Format

### Basic Rule Structure
```json
{
  "version": "1.0",
  "name": "Project Rules",
  "description": "AI Epic Framework project rules",
  "rules": [
    {
      "name": "coding-standards",
      "description": "Enforce coding standards",
      "priority": "high",
      "conditions": {
        "filePatterns": ["*.ts", "*.tsx", "*.js", "*.jsx"],
        "directories": ["src/", "components/"],
        "exclude": ["node_modules/", "dist/"]
      },
      "instructions": [
        "Use TypeScript for all new code",
        "Follow ESLint and Prettier configurations",
        "Use functional components with hooks",
        "Implement proper error handling",
        "Write unit tests for business logic"
      ],
      "examples": {
        "good": [
          "const Component = ({ prop }: ComponentProps) => { ... }",
          "const [state, setState] = useState<StateType>(initialState)"
        ],
        "avoid": [
          "class Component extends React.Component { ... }",
          "const Component = (props) => { ... }"
        ]
      }
    }
  ]
}
```

### Advanced Rule Configuration
```json
{
  "version": "1.0",
  "name": "Enterprise Rules",
  "description": "Enterprise-grade development standards",
  "metadata": {
    "author": "Development Team",
    "version": "2.1.0",
    "lastUpdated": "2024-01-15"
  },
  "global": {
    "security": {
      "enabled": true,
      "scanSensitiveData": true,
      "blockPatterns": ["password", "api_key", "secret"]
    },
    "compliance": {
      "gdpr": true,
      "sox": false,
      "hipaa": false
    }
  },
  "rules": [
    {
      "name": "security-standards",
      "description": "Security and compliance requirements",
      "priority": "critical",
      "conditions": {
        "filePatterns": ["*.ts", "*.js", "*.py", "*.java"],
        "environments": ["production", "staging"]
      },
      "instructions": [
        "Never log sensitive information",
        "Use environment variables for configuration",
        "Implement proper input validation",
        "Use HTTPS for all external requests",
        "Follow OWASP security guidelines"
      ],
      "validations": [
        {
          "type": "regex",
          "pattern": "console\\.log.*password",
          "message": "Sensitive data logging detected"
        },
        {
          "type": "regex",
          "pattern": "api_key.*=.*['\"][^'\"]+['\"]",
          "message": "Hardcoded API key detected"
        }
      ]
    }
  ]
}
```

## Directory Structure

### Project-Level Rules
```
project/
├── .zenrules                    # Main project rules
├── .zencoder/
│   ├── rules/                   # Additional rule files
│   │   ├── frontend.zenrules
│   │   ├── backend.zenrules
│   │   └── testing.zenrules
│   ├── templates/               # Rule templates
│   │   ├── react.zenrules
│   │   └── nodejs.zenrules
│   └── config/
│       └── zencoder.json        # Zencoder configuration
└── ...
```

### Global Rules
```
~/.zencoder/
├── rules/                       # Global rules
│   ├── personal.zenrules
│   ├── company.zenrules
│   └── security.zenrules
├── templates/                   # Global templates
└── config/
    └── zencoder.json           # Global configuration
```

## Rule Categories

### Coding Standards
```json
{
  "name": "coding-standards",
  "description": "Code quality and style standards",
  "instructions": [
    "Use meaningful variable and function names",
    "Keep functions small and focused (max 20 lines)",
    "Add JSDoc comments for public APIs",
    "Follow DRY principles",
    "Use consistent indentation (2 spaces)",
    "Implement proper error handling"
  ]
}
```

### Framework-Specific Rules
```json
{
  "name": "react-standards",
  "description": "React development standards",
  "conditions": {
    "filePatterns": ["*.tsx", "*.jsx"],
    "directories": ["src/components/"]
  },
  "instructions": [
    "Use functional components with hooks",
    "Implement proper prop validation with TypeScript",
    "Follow component naming conventions (PascalCase)",
    "Use React.memo for performance optimization",
    "Implement proper error boundaries"
  ]
}
```

### Testing Standards
```json
{
  "name": "testing-standards",
  "description": "Testing requirements and standards",
  "conditions": {
    "filePatterns": ["*.test.*", "*.spec.*"]
  },
  "instructions": [
    "Write unit tests for all business logic",
    "Use descriptive test names",
    "Follow AAA pattern (Arrange, Act, Assert)",
    "Mock external dependencies",
    "Achieve minimum 80% code coverage",
    "Use testing-library for React components"
  ]
}
```

## Enterprise Features

### Team Coordination
```json
{
  "team": {
    "enabled": true,
    "syncRules": true,
    "approvalRequired": false,
    "notifications": {
      "ruleViolations": true,
      "ruleUpdates": true
    }
  }
}
```

### Security and Compliance
```json
{
  "security": {
    "enabled": true,
    "scanPatterns": [
      "password.*=.*['\"][^'\"]+['\"]",
      "api_key.*=.*['\"][^'\"]+['\"]",
      "secret.*=.*['\"][^'\"]+['\"]"
    ],
    "blockPatterns": [
      "console\\.log.*password",
      "console\\.log.*secret"
    ],
    "compliance": {
      "gdpr": true,
      "sox": true,
      "hipaa": false
    }
  }
}
```

### Analytics and Monitoring
```json
{
  "analytics": {
    "enabled": true,
    "trackRuleUsage": true,
    "trackViolations": true,
    "generateReports": true,
    "metrics": [
      "ruleEffectiveness",
      "complianceScore",
      "teamAdoption"
    ]
  }
}
```

## Rule Loading and Priority

### Loading Order
1. **Global Rules** (lowest priority)
2. **Project Rules** (medium priority)
3. **Workspace Rules** (highest priority)

### Priority Levels
- **critical**: Must be followed, blocks violations
- **high**: Strongly recommended, warnings for violations
- **medium**: Recommended, suggestions for violations
- **low**: Optional, informational only

## Creating and Managing Rules

### Creating a New Rule File
```bash
# Create project rules directory
mkdir -p .zencoder/rules

# Create a new rule file
touch .zencoder/rules/frontend.zenrules
```

### Rule Validation
Zencoder validates rule files for:
- JSON syntax correctness
- Required field presence
- Valid rule structure
- Pattern syntax validation

### Rule Testing
```bash
# Validate rule file
zencoder validate-rules .zenrules

# Test rules against codebase
zencoder test-rules --file src/components/Button.tsx

# Generate rule compliance report
zencoder report --rules .zenrules
```

## Integration with Development Tools

### IDE Integration
Zencoder integrates with popular IDEs:
- **VS Code**: Native extension support
- **IntelliJ IDEA**: Plugin available
- **Sublime Text**: Package support
- **Vim/Neovim**: Plugin support

### CI/CD Integration
```yaml
# GitHub Actions example
- name: Validate Zencoder Rules
  run: |
    zencoder validate-rules .zenrules
    zencoder test-compliance --strict

- name: Generate Compliance Report
  run: zencoder report --output compliance-report.html
```

### Git Hooks
```bash
#!/bin/sh
# pre-commit hook
zencoder validate-changes --staged
```

## Best Practices

### Writing Effective Rules
1. **Be Specific**: Use clear, actionable instructions
2. **Provide Examples**: Include good and bad examples
3. **Use Conditions**: Target specific file types and directories
4. **Set Priorities**: Use appropriate priority levels
5. **Keep Updated**: Regularly review and update rules

### Organization
1. **Group Related Rules**: Use categories and namespaces
2. **Version Control**: Include rules in version control
3. **Documentation**: Document rule reasoning and context
4. **Team Review**: Have team members review rules

### Performance
1. **Optimize Patterns**: Use efficient regex patterns
2. **Limit Scope**: Avoid overly broad conditions
3. **Cache Rules**: Enable rule caching for large projects
4. **Monitor Impact**: Track rule performance and effectiveness

## Troubleshooting

### Common Issues
1. **Rules Not Applied**: Check file location and syntax
2. **Performance Issues**: Optimize rule conditions and patterns
3. **Conflicts**: Resolve priority conflicts between rules
4. **Validation Errors**: Fix JSON syntax and structure issues

### Debugging
```bash
# Enable debug mode
zencoder --debug validate-rules .zenrules

# Check rule loading
zencoder --verbose test-rules

# Generate detailed report
zencoder report --verbose --output debug-report.html
```

## Advanced Features

### Rule Templates
```json
{
  "template": {
    "name": "React Project Template",
    "description": "Standard rules for React projects",
    "variables": {
      "framework": "react",
      "language": "typescript",
      "testing": "jest"
    },
    "rules": [
      {
        "name": "react-standards",
        "instructions": [
          "Use {{framework}} functional components",
          "Use {{language}} for type safety",
          "Use {{testing}} for unit tests"
        ]
      }
    ]
  }
}
```

### Conditional Rules
```json
{
  "name": "environment-specific",
  "conditions": {
    "environment": "production",
    "filePatterns": ["*.js", "*.ts"]
  },
  "instructions": [
    "Enable production optimizations",
    "Disable debug logging",
    "Use production API endpoints"
  ]
}
```

### Rule Inheritance
```json
{
  "name": "extended-standards",
  "inherits": ["base-standards", "security-standards"],
  "instructions": [
    "Additional project-specific rules"
  ]
}
```
