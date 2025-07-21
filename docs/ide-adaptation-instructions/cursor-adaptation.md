# Cursor AI Adaptation Instructions

## Overview
This document provides step-by-step instructions for adapting the AI Epic Framework to Cursor AI's `.mdc` format with metadata headers and proper directory structure.

## Pre-Adaptation Setup

### 1. Clear Target Directory
```bash
# Remove all existing content from cursor-specific directory
rm -rf framework/cursor-specific/*
```

### 2. Create Directory Structure
```bash
# Create the .cursor/rules directory structure
mkdir -p framework/cursor-specific/.cursor/rules
```

## File Format Requirements

### Cursor AI MDC Format
- **File Extension**: `.mdc`
- **Metadata Headers**: Required at the top of each file
- **Content**: Markdown format with Cursor-specific features
- **Location**: `.cursor/rules/` directory

### Metadata Header Format
```markdown
---
description: "Brief description of the rule's purpose"
globs: ["*.ts", "*.tsx", "*.js", "*.jsx"]  # Optional: file patterns
alwaysApply: false  # Optional: default is false
---
```

## Adaptation Process

### Step 1: Create User Rules Template
**File**: `framework/cursor-specific/.cursor/rules/user-rules-template.mdc`

**Metadata**:
```markdown
---
description: "AI Epic Framework - Main user rules template for Cursor AI"
alwaysApply: true
---
```

**Content Transformation**:
1. Copy entire content from `framework/generic/user-rules-template.md`
2. Add metadata header at the very top
3. Update all internal references to use relative paths within the `.cursor/rules/` directory
4. Ensure all `@filename` references point to files within the same directory

### Step 2: Create Epic Workflow Instructions
**File**: `framework/cursor-specific/.cursor/rules/epic-workflow-instructions.mdc`

**Metadata**:
```markdown
---
description: "AI Epic Framework - Epic workflow management system"
globs: ["**/*.md", "**/INDEX.md", "**/REQUIREMENTS.md"]
alwaysApply: false
---
```

**Content Transformation**:
1. Copy entire content from `framework/generic/epic-workflow-instructions.md`
2. Add metadata header at the very top
3. Update all internal references to use relative paths
4. Ensure all navigation links work within the `.cursor/rules/` directory

### Step 3: Create Problem Solving Framework
**File**: `framework/cursor-specific/.cursor/rules/problem-solving-framework.mdc`

**Metadata**:
```markdown
---
description: "AI Epic Framework - Systematic problem-solving methodology"
globs: ["**/*.ts", "**/*.js", "**/*.py", "**/*.java"]
alwaysApply: false
---
```

**Content Transformation**:
1. Copy entire content from `framework/generic/problem-solving-framework.md`
2. Add metadata header at the very top
3. Update all internal references to use relative paths
4. Ensure all framework references work correctly

### Step 4: Create Architecture Design Process
**File**: `framework/cursor-specific/.cursor/rules/architecture-design-process.mdc`

**Metadata**:
```markdown
---
description: "AI Epic Framework - Architecture design methodology and templates"
globs: ["**/architecture/**/*.md", "**/docs/**/*.md"]
alwaysApply: false
---
```

**Content Transformation**:
1. Copy entire content from `framework/generic/architecture-design-process.md`
2. Add metadata header at the very top
3. Update all internal references to use relative paths
4. Ensure all template references work correctly

### Step 5: Create Architecture Lifecycle
**File**: `framework/cursor-specific/.cursor/rules/architecture-lifecycle.mdc`

**Metadata**:
```markdown
---
description: "AI Epic Framework - Architecture documentation lifecycle management"
globs: ["**/docs/architecture/**/*.md", "**/architecture/**/*.md"]
alwaysApply: false
---
```

**Content Transformation**:
1. Copy entire content from `framework/generic/architecture-lifecycle.md`
2. Add metadata header at the very top
3. Update all internal references to use relative paths
4. Ensure all documentation references work correctly

### Step 6: Create General Execution Standards
**File**: `framework/cursor-specific/.cursor/rules/general-execution-standards.mdc`

**Metadata**:
```markdown
---
description: "AI Epic Framework - Quality assurance and execution standards"
globs: ["**/*.ts", "**/*.js", "**/*.py", "**/*.java", "**/*.md"]
alwaysApply: true
---
```

**Content Transformation**:
1. Copy entire content from `framework/generic/general-execution-standards.md`
2. Add metadata header at the very top
3. Update all internal references to use relative paths
4. Ensure all standards references work correctly

## Content Preservation Rules

### Must Preserve Exactly
- All framework concepts and methodologies
- All decision matrices and workflows
- All examples and use cases
- All technical specifications
- All navigation logic (adapted for Cursor format)

### Must Adapt
- File extensions: `.md` → `.mdc`
- Add metadata headers to each file
- Update reference paths to be relative within `.cursor/rules/`
- Ensure `@filename` references work in Cursor context

### Must Not Change
- Core framework logic and processes
- Technical accuracy of any content
- Framework principles and philosophies
- Decision-making criteria and matrices

## Reference Path Updates

### Internal References
Update all internal references to use relative paths within the `.cursor/rules/` directory:

**Before**:
```markdown
- **Epic Workflow**: [epic-workflow-instructions.md](./epic-workflow-instructions.md)
```

**After**:
```markdown
- **Epic Workflow**: [epic-workflow-instructions.mdc](./epic-workflow-instructions.mdc)
```

### File References
Update all `@filename` references to point to files within the same directory:

**Before**:
```markdown
@service-template.ts
```

**After**:
```markdown
@service-template.ts
```
(Keep as-is if the referenced file exists in the same directory)

## Validation Steps

### 1. Content Verification
- [ ] All 6 generic files have been converted to `.mdc` format
- [ ] All content is 100% preserved from generic versions
- [ ] All metadata headers are properly formatted
- [ ] All internal references work correctly

### 2. Structure Verification
- [ ] Directory structure: `framework/cursor-specific/.cursor/rules/`
- [ ] All files have `.mdc` extension
- [ ] All files have proper metadata headers
- [ ] No external dependencies remain

### 3. Functionality Verification
- [ ] Cursor AI can load all rules
- [ ] Metadata headers are recognized
- [ ] File references work correctly
- [ ] Navigation between rules functions properly

## Final Directory Structure

```
framework/cursor-specific/
└── .cursor/
    └── rules/
        ├── user-rules-template.mdc
        ├── epic-workflow-instructions.mdc
        ├── problem-solving-framework.mdc
        ├── architecture-design-process.mdc
        ├── architecture-lifecycle.mdc
        └── general-execution-standards.mdc
```

## Error Prevention

1. **Never Skip Content**: Every section from generic files must be included
2. **Never Skip Metadata**: Every `.mdc` file must have proper metadata headers
3. **Never Use External Paths**: All references must be relative within `.cursor/rules/`
4. **Never Change Framework Logic**: The framework must function identically
5. **Never Skip Validation**: Always verify the adaptation works in Cursor

## Success Criteria

The Cursor AI adaptation is successful when:
- All 6 files are properly converted to `.mdc` format
- All content is 100% preserved from generic versions
- All metadata headers are correctly formatted
- All internal references work within the `.cursor/rules/` directory
- Cursor AI can load and use all rules correctly
- Framework functionality is identical to the generic version 