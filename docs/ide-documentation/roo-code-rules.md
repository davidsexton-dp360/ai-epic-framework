# Roo Code Custom Instructions Documentation

## Overview
Custom Instructions allow you to personalize how Roo behaves, providing specific guidance that shapes responses, coding style, and decision-making processes.

## Instruction File Locations
You can provide custom instructions using global rules (applied across all projects), workspace rules (project-specific), or through the Prompts tab interface.

### Global Rules Directory
Apply to all projects automatically.
- **Linux/macOS:** `~/.roo/rules/` and `~/.roo/rules-{modeSlug}/`
- **Windows:** `%USERPROFILE%\.roo\rules\` and `%USERPROFILE%\.roo\rules-{modeSlug}\`

### Workspace Rules
Apply only to the current project, can override global rules.

#### Preferred Method: Directory (`.roo/rules/`)
```
.
├── .roo/
│   └── rules/          # Workspace-wide rules
│       ├── 01-general.md
│       └── 02-coding-style.txt
└── ... (other project files)
```

#### Fallback Method: Single File (`.roorules`)
```
.
├── .roorules           # Workspace-wide rules (single file)
└── ... (other project files)
```

### Mode-Specific Instructions
Apply only to a specific mode (e.g., `code`).

#### Preferred Method: Directory (`.roo/rules-{modeSlug}/`)
```
.
├── .roo/
│   └── rules-code/     # Rules for "code" mode
│       ├── 01-js-style.md
│       └── 02-ts-style.md
└── ... (other project files)
```

#### Fallback Method: Single File (`.roorules-{modeSlug}`)
```
.
├── .roorules-code      # Rules for "code" mode (single file)
└── ... (other project files)
```

Rules are loaded in order: Global rules first, then workspace rules (which can override global rules).

## What Are Custom Instructions?
Custom Instructions define specific behaviors, preferences, and constraints beyond Roo's basic role definition. Examples include coding style, documentation standards, testing requirements, and workflow guidelines.

## Setting Custom Instructions

### Global Custom Instructions
These instructions apply across all workspaces and maintain your preferences regardless of which project you're working on.

**How to set them:**
1. **Open Prompts Tab:** Click the icon in the Roo Code top menu bar
2. **Find Section:** Find the "Custom Instructions for All Modes" section
3. **Enter Instructions:** Enter your instructions in the text area
4. **Save Changes:** Click "Done" to save your changes

### Global Rules Directory
The Global Rules Directory feature provides reusable rules and custom instructions that automatically apply across all your projects. This system supports both global configurations and project-specific overrides.

#### Key Benefits
**Without Global Rules:** You had to maintain separate rule files in each project:
- Copy the same rules to every new project
- Update rules manually across multiple projects
- No consistency between projects

**With Global Rules:** Create rules once and use them everywhere:
- Set up your preferred coding standards globally
- Override specific rules per project when needed
- Maintain consistency across all your work
- Easy to update rules for all projects at once

#### Directory Structure
The global rules directory location is fixed and cannot be customized:

**Linux/macOS:**
```
~/.roo/                           # Your global Roo configuration
├── rules/                        # General rules applied to all projects
│   ├── coding-standards.md
│   ├── formatting-rules.md
│   └── security-guidelines.md
├── rules-code/                   # Rules specific to Code mode
│   ├── typescript-rules.md
│   └── testing-requirements.md
├── rules-docs-extractor/         # Rules for documentation extraction
│   └── documentation-style.md
└── rules-{mode}/                 # Rules for other specific modes
    └── mode-specific-rules.md
```

**Windows:**
```
%USERPROFILE%\.roo\               # Your global Roo configuration
├── rules\                        # General rules applied to all projects
│   ├── coding-standards.md
│   ├── formatting-rules.md
│   └── security-guidelines.md
├── rules-code\                   # Rules specific to Code mode
│   ├── typescript-rules.md
│   └── testing-requirements.md
└── rules-{mode}\                 # Rules for other specific modes
    └── mode-specific-rules.md
```

#### Setting Up Global Rules

1. **Create Global Rules Directory:**
   ```bash
   # Linux/macOS
   mkdir -p ~/.roo/rules
   # Windows
   mkdir %USERPROFILE%\.roo\rules
   ```

2. **Add General Rules (~/.roo/rules/coding-standards.md):**
   ```markdown
   # Global Coding Standards
   1. Always use TypeScript for new projects
   2. Write unit tests for all new functions
   3. Use descriptive variable names
   4. Add JSDoc comments for public APIs
   ```

3. **Add Mode-Specific Rules (~/.roo/rules-code/typescript-rules.md):**
   ```markdown
   # TypeScript Code Mode Rules
   1. Use strict mode in tsconfig.json
   2. Prefer interfaces over type aliases for object shapes
   3. Always specify return types for functions
   ```

#### Available Rule Directories
| Directory | Purpose |
|-----------|---------|
| `rules/` | General rules applied to all modes |
| `rules-code/` | Rules specific to Code mode |
| `rules-docs-extractor/` | Rules for documentation extraction |
| `rules-architect/` | Rules for system architecture tasks |
| `rules-debug/` | Rules for debugging workflows |
| `rules-{mode}/` | Rules for any custom mode |

#### Rule Loading Order
Rules are loaded in this order:
1. Global Rules (from `~/.roo/`)
2. Project Rules (from `project/.roo/`) - can override global rules
3. Legacy Files (`.roorules`, `.clinerules` - for backward compatibility)

Within each level, mode-specific rules are loaded before general rules.

### Workspace-Level Instructions
These instructions only apply within your current workspace, allowing you to customize Roo Code's behavior for specific projects.

#### Workspace-Wide Instructions via Files/Directories
Workspace-wide instructions apply to all modes within the current project and can be defined using files:

**Preferred Method: Directory-Based (`.roo/rules/`)**
- Create a directory named `.roo/rules/` in your workspace root.
- Place instruction files (e.g., `.md`, `.txt`) inside. Roo Code reads files recursively, appending their content to the system prompt in alphabetical order based on filename.
