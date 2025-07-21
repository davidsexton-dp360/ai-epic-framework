# Cline Rules Documentation

## Overview
Cline Rules allow you to provide Cline with system-level guidance. Think of them as a persistent way to include context and preferences for your projects or globally for every conversation.

## Creating a Rule
You can create a rule by clicking the `+` button in the Rules tab. This will open a new file in your IDE which you can use to write your rule.

Once you save the file:
- Your rule will be stored in the `.clinerules/` directory in your project (if it's a Workspace Rule)
- Or in the `Documents/Cline/Rules` directory (if it's a Global Rule).

You can also have Cline create a rule for you by using the `/newrule` slash command in the chat.

## Example Cline Rule Structure
```markdown
# Project Guidelines

## Documentation Requirements
- Update relevant documentation in /docs when modifying features
- Keep README.md in sync with new capabilities
- Maintain changelog entries in CHANGELOG.md

## Architecture Decision Records
Create ADRs in /docs/adr for:
- Major dependency changes
- Architectural pattern changes
- New integration patterns
- Database schema changes
  Follow template in /docs/adr/template.md

## Code Style & Patterns
- Generate API clients using OpenAPI Generator
- Use TypeScript axios template
- Place generated code in /src/generated
- Prefer composition over inheritance
- Use repository pattern for data access
- Follow error handling pattern in /src/utils/errors.ts

## Testing Standards
- Unit tests required for business logic
- Integration tests for API endpoints
- E2E tests for critical user flows
```

## Key Benefits
- **Version Controlled**: The `.clinerules` file becomes part of your project's source code
- **Team Consistency**: Ensures consistent behavior across all team members
- **Project-Specific**: Rules and standards tailored to each project's needs
- **Institutional Knowledge**: Maintains project standards and practices in code

Place the `.clinerules` file in your project's root directory:
```
your-project/
├── .clinerules
├── src/
├── docs/
└── ...
```

Cline's system prompt, on the other hand, is not user-editable. For a broader look at prompt engineering best practices, check out this resource.

## Tips for Writing Effective Cline Rules
- Be Clear and Concise: Use simple language and avoid ambiguity.
- Focus on Desired Outcomes: Describe the results you want, not the specific steps.
- Test and Iterate: Experiment to find what works best for your workflow.

## .clinerules/ Folder System
```
your-project/
├── .clinerules/              # Folder containing active rules
│   ├── 01-coding.md          # Core coding standards
│   ├── 02-documentation.md   # Documentation requirements
│   └── current-sprint.md     # Rules specific to current work
├── src/
└── ...
```

Cline automatically processes **all Markdown files** inside the `.clinerules/` directory, combining them into a unified set of rules. The numeric prefixes (optional) help organize files in a logical sequence.

### Using a Rules Bank
For projects with multiple contexts or teams, maintain a rules bank directory:
```
your-project/
├── .clinerules/              # Active rules - automatically applied
│   ├── 01-coding.md
│   └── client-a.md
│
├── clinerules-bank/          # Repository of available but inactive rules
│   ├── clients/              # Client-specific rule sets
│   │   ├── client-a.md
│   │   └── client-b.md
│   ├── frameworks/           # Framework-specific rules
│   │   ├── react.md
│   │   └── vue.md
│   └── project-types/        # Project type standards
│       ├── api-service.md
│       └── frontend-app.md
└── ...
```

### Benefits of the Folder Approach
- **Organization**: Keep related rules together in logical groups
- **Flexibility**: Easily enable/disable rule sets by moving files
- **Scalability**: Add new rules without cluttering a single file
- **Team Collaboration**: Different team members can maintain different rule sets

### Usage Examples
1. **Client-Specific Rules**: Copy `clinerules-bank/clients/client-a.md` to `.clinerules/client-a.md` when working on Client A's project
2. **Framework Rules**: Copy `clinerules-bank/frameworks/react.md` to `.clinerules/react.md` when working on React components
3. **Project Type Rules**: Copy `clinerules-bank/project-types/api-service.md` to `.clinerules/api-service.md` when building API services

### Implementation Tips
- Use descriptive filenames that indicate the rule's purpose
- Keep individual rule files focused on specific concerns
- Use numeric prefixes (01-, 02-, etc.) to control loading order
- Regularly review and update your rules bank as projects evolve

## Managing Rules with the Toggleable Popover
The toggleable popover provides an easy way to manage your rules without manually editing files. You can:
- View all active rules
- Toggle rules on/off
- Create new rules
- Edit existing rules
- Organize rules by category

This interface makes it simple to maintain your rules and ensures they're always up to date with your current project needs.

```
