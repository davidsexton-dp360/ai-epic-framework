# Kilo Code Custom Rules Documentation

## Overview
Custom rules provide a powerful way to define project-specific and global behaviors and constraints for the Kilo Code AI agent. With custom rules, you can ensure consistent formatting, restrict access to sensitive files, enforce coding standards, and customize the AI's behavior for your specific project needs or across all projects.

## Rule Format
Custom rules can be written in plain text, but Markdown format is recommended for better structure and comprehension by the AI models. The structured nature of Markdown helps the models parse and understand your rules more effectively.

- Use Markdown headers (#, ##, etc.) to define rule categories
- Use lists (-, *) to enumerate specific items or constraints
- Use code blocks (```) to include code examples when needed

## Rule Types
Kilo Code supports two types of custom rules:
- **Project Rules**: Apply only to the current project workspace
- **Global Rules**: Apply across all projects and workspaces

**Note**: The built-in rules management UI is available for general rules only. Mode-specific rules must be managed through the file system.

## Rule Location

### Project Rules
Custom rules are primarily loaded from the `.kilocode/rules/` directory. This is the recommended approach for organizing your project-specific rules. Each rule is typically placed in its own Markdown file with a descriptive name:

```
project/
├── .kilocode/
│   ├── rules/
│   │   ├── formatting.md
│   │   ├── restricted_files.md
│   │   └── naming_conventions.md
├── src/
└── ...
```

### Global Rules
Global rules are stored in your home directory and apply to all projects:
```
~/.kilocode/
├── rules/
│   ├── coding_standards.md
│   ├── security_guidelines.md
│   └── documentation_style.md
```

## Managing Rules Through the UI
Kilo Code provides a built-in interface for managing your custom rules without manually editing files in the `.kilocode/rules/` directories. To access the UI, click on the icon in the bottom right corner of the Kilo Code window.

You can access the rules management UI to:
- View all active rules (both project and global)
- Toggle rules on/off without deleting them
- Create and edit rules directly in the interface
- Organize rules by category and priority

## Rule Loading Order

### General Rules (Any Mode)
Rules are loaded in the following priority order:
1. Global rules from `~/.kilocode/rules/` directory
2. Project rules from `.kilocode/rules/` directory
3. Legacy fallback files (for backward compatibility):
   - `.roorules`
   - `.clinerules`
   - `.kilocoderules` (deprecated)

When both global and project rules exist, they are combined with project rules taking precedence over global rules for conflicting directives.

**Note**: We strongly recommend keeping your rules in the `.kilocode/rules/` folder as it provides better organization and is the preferred approach for future versions. The folder-based structure allows for more granular rule organization and clearer separation of concerns. The legacy file-based approach is maintained for backward compatibility but may be subject to change in future releases.

### Mode-Specific Rules
Additionally, the system supports mode-specific rules, which are loaded separately and have their own priority order:
1. First, it checks for `.kilocode/rules-${mode}/` directory
2. If that doesn't exist or is empty, it falls back to `.kilocoderules-${mode}` file (deprecated)

Currently, mode-specific rules are only supported at the project level.
When both generic rules and mode-specific rules exist, the mode-specific rules are given priority in the final output.

## Creating Custom Rules

### Using the UI Interface
The easiest way to create and manage rules is through the built-in UI:
1. Access the rules management interface from the Kilo Code panel
2. Choose between creating project-specific or global rules
3. Use the interface to create, edit, or toggle rules
4. Rules are automatically saved and applied immediately

### Using the File System
To create rules manually:

**For Project Rules:**
1. Create the `.kilocode/rules/` directory if it doesn't already exist
2. Create a new Markdown file with a descriptive name in this directory
3. Write your rule using Markdown formatting
4. Save the file

**For Global Rules:**
1. Create the `~/.kilocode/rules/` directory if it doesn't already exist
2. Create a new Markdown file with a descriptive name in this directory
3. Write your rule using Markdown formatting
4. Save the file

Rules will be automatically applied to all future Kilo Code interactions. Any new changes will be applied immediately.

## Example Rules

### Example 1: Table Formatting
```markdown
# Tables
When printing tables, always add an exclamation mark to each column header
```
This simple rule instructs the AI to add exclamation marks to all table column headers when generating tables in your project.

### Example 2: Restricted File Access
```markdown
# Restricted files
Files in the list contain sensitive data, they MUST NOT be read
- supersecrets.txt
- credentials.json
- .env
```

### Example 3: Coding Standards
```markdown
# Coding Standards
- Always use TypeScript for new projects
- Write unit tests for all new functions
- Use descriptive variable names
- Add JSDoc comments for public APIs
```

### Example 4: Documentation Requirements
```markdown
# Documentation
- Update relevant documentation in /docs when modifying features
- Keep README.md in sync with new capabilities
- Maintain changelog entries in CHANGELOG.md
```

## Best Practices
- **Be Specific**: Write clear, actionable rules that leave no room for interpretation
- **Use Structure**: Organize rules with headers and bullet points for better readability
- **Keep Focused**: Each rule file should focus on a specific concern or category
- **Test Rules**: Verify that your rules work as expected by testing them with the AI
- **Regular Updates**: Review and update your rules as your project evolves
- **Version Control**: Include project rules in your version control system for team consistency
