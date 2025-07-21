# Trae AI Rules Documentation

## Overview
Trae AI provides a comprehensive rules system that allows you to customize how the AI behaves in your development environment. Rules can be applied at different levels and help ensure consistent behavior across your projects.

## Rule Types and Locations

### Global Rules
Global rules apply across all projects and are stored in your user configuration directory. These rules define your personal preferences and coding standards that apply regardless of the project you're working on.

**Location**: `~/.trae/rules/` (Linux/macOS) or `%USERPROFILE%\.trae\rules\` (Windows)

### Project Rules
Project rules are specific to individual projects and are stored within the project directory. These rules can override global rules and provide project-specific guidance.

**Location**: `.trae/rules/` within your project directory

### Workspace Rules
Workspace rules apply to specific workspaces or development contexts. These are useful for team environments or when working with different frameworks.

**Location**: `.trae/workspace-rules/` within your project directory

## Rule File Format
Rules are written in YAML format for easy reading and modification. Each rule file can contain multiple rules organized by categories.

### Basic Rule Structure
```yaml
# Example rule file: coding-standards.yaml
rules:
  - name: "TypeScript Standards"
    description: "Enforce TypeScript best practices"
    conditions:
      - file_pattern: "*.ts"
      - file_pattern: "*.tsx"
    instructions:
      - "Use strict TypeScript mode"
      - "Prefer interfaces over type aliases for object shapes"
      - "Always specify return types for functions"
      - "Use descriptive variable names"

  - name: "React Components"
    description: "React component development standards"
    conditions:
      - file_pattern: "*.tsx"
      - directory: "components/"
    instructions:
      - "Use functional components with hooks"
      - "Implement proper prop validation"
      - "Follow component naming conventions (PascalCase)"
      - "Use TypeScript for all components"
```

### Advanced Rule Configuration
```yaml
# Example: advanced-rules.yaml
rules:
  - name: "API Development"
    description: "Backend API development standards"
    priority: "high"
    conditions:
      - file_pattern: "*.js"
      - directory: "api/"
      - not_directory: "tests/"
    instructions:
      - "Use async/await for all database operations"
      - "Implement proper error handling with try/catch"
      - "Return consistent JSON response format"
      - "Use environment variables for configuration"
    examples:
      - "Always wrap database calls in try/catch blocks"
      - "Use HTTP status codes appropriately (200, 400, 500, etc.)"
```

## Rule Loading Order
Trae AI loads rules in the following priority order:

1. **Workspace Rules** (highest priority)
2. **Project Rules**
3. **Global Rules** (lowest priority)

When multiple rules apply to the same context, the higher priority rules take precedence. However, all applicable rules are considered to provide comprehensive guidance.

## Creating and Managing Rules

### Creating a New Rule
1. Navigate to the appropriate rules directory
2. Create a new YAML file with a descriptive name
3. Define your rules using the YAML format
4. Save the file - rules are automatically loaded

### Example: Creating Project-Specific Rules
```bash
# Create project rules directory
mkdir -p .trae/rules

# Create a new rule file
touch .trae/rules/frontend-standards.yaml
```

### Rule File Content
```yaml
# .trae/rules/frontend-standards.yaml
rules:
  - name: "Frontend Architecture"
    description: "Frontend development standards for this project"
    conditions:
      - directory: "src/"
    instructions:
      - "Use React 18 with hooks"
      - "Implement proper state management with Context API"
      - "Use CSS modules for styling"
      - "Follow atomic design principles"
      - "Write unit tests for all components"
```

## Rule Categories and Organization

### Coding Standards
Rules that define code quality and style:
```yaml
rules:
  - name: "Code Quality"
    description: "General code quality standards"
    instructions:
      - "Use meaningful variable and function names"
      - "Keep functions small and focused"
      - "Add comments for complex logic"
      - "Follow DRY principles"
```

### Framework-Specific Rules
Rules tailored to specific frameworks or libraries:
```yaml
rules:
  - name: "Next.js Standards"
    description: "Next.js specific development standards"
    conditions:
      - file_pattern: "*.tsx"
      - directory: "pages/"
    instructions:
      - "Use Next.js App Router for new pages"
      - "Implement proper SEO with meta tags"
      - "Use Next.js Image component for images"
      - "Follow Next.js file-based routing conventions"
```

### Testing Standards
Rules for testing practices:
```yaml
rules:
  - name: "Testing Standards"
    description: "Testing requirements and standards"
    conditions:
      - file_pattern: "*.test.*"
      - file_pattern: "*.spec.*"
    instructions:
      - "Write unit tests for all business logic"
      - "Use descriptive test names"
      - "Follow AAA pattern (Arrange, Act, Assert)"
      - "Mock external dependencies"
```

## Best Practices for Writing Rules

### Be Specific and Actionable
```yaml
# Good: Specific and actionable
instructions:
  - "Use TypeScript strict mode in tsconfig.json"
  - "Implement error boundaries for React components"
  - "Use environment variables for API endpoints"

# Avoid: Vague instructions
instructions:
  - "Write good code"
  - "Follow best practices"
  - "Be consistent"
```

### Use Appropriate Conditions
```yaml
# Target specific file types and directories
conditions:
  - file_pattern: "*.ts"
  - directory: "src/components/"
  - not_directory: "node_modules/"
```

### Provide Examples
```yaml
# Include examples for clarity
instructions:
  - "Use async/await instead of .then() chains"
examples:
  - "Prefer: const data = await fetchData() over fetchData().then(data => ...)"
```

## Rule Management and Maintenance

### Updating Rules
Rules can be updated at any time by editing the YAML files. Changes are automatically applied to new conversations.

### Version Control
Project rules should be included in version control to ensure team consistency:
```bash
# Add rules to git
git add .trae/rules/
git commit -m "Add project-specific AI rules"
```

### Rule Validation
Trae AI validates rule files when they're loaded. Common validation errors include:
- Invalid YAML syntax
- Missing required fields
- Invalid file patterns

## Integration with Development Workflow

### IDE Integration
Rules are automatically applied when using Trae AI in supported IDEs:
- VS Code
- IntelliJ IDEA
- Sublime Text
- Vim/Neovim

### Command Line Usage
Rules are also applied when using Trae AI from the command line:
```bash
trae generate component Button
trae refactor src/utils/helpers.ts
```

## Troubleshooting

### Rules Not Being Applied
1. **Check File Location**: Ensure rules are in the correct directory
2. **Verify YAML Syntax**: Check for syntax errors in rule files
3. **Check Conditions**: Ensure rule conditions match your current context
4. **Restart Trae AI**: Restart the application to reload rules

### Conflicting Rules
If rules seem to conflict:
1. **Check Priority**: Higher priority rules override lower ones
2. **Review Conditions**: Ensure conditions are specific enough
3. **Consolidate Rules**: Combine related rules into single files
4. **Test Rules**: Verify rules work as expected

## Advanced Features

### Conditional Rules
Rules can be made conditional based on various factors:
```yaml
rules:
  - name: "Development vs Production"
    description: "Different rules for different environments"
    conditions:
      - environment: "development"
    instructions:
      - "Enable debug logging"
      - "Use development API endpoints"
```

### Rule Inheritance
Rules can inherit from other rules:
```yaml
rules:
  - name: "Base Standards"
    description: "Base coding standards"
    instructions:
      - "Use TypeScript"
      - "Follow ESLint rules"

  - name: "Extended Standards"
    description: "Extended standards inheriting from base"
    inherits: "Base Standards"
    instructions:
      - "Use React hooks"
      - "Implement proper error handling"
```

### Custom Rule Templates
Create reusable rule templates for common scenarios:
```yaml
# templates/react-project.yaml
template:
  name: "React Project Template"
  description: "Standard rules for React projects"
  rules:
    - name: "React Standards"
      instructions:
        - "Use functional components"
        - "Implement proper prop validation"
        - "Use TypeScript"
```

## Security and Privacy
- Rules are stored locally on your machine
- No rule content is transmitted to external servers
- You have full control over what rules are applied
- Sensitive information in rules should be avoided

