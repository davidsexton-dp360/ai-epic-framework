# Roo Code Adaptation Instructions

## Overview
This document provides step-by-step instructions for adapting the AI Epic Framework to Roo Code's directory-based rules system with `.roo/rules/` and `.roo/rules-code/` structure.

## Pre-Adaptation Setup

### 1. Clear Target Directory
```bash
# Remove all existing content from roo-code-specific directory
rm -rf framework/roo-code-specific/*
```

### 2. Create Directory Structure
```bash
# Create the .roo directory structure
mkdir -p framework/roo-code-specific/.roo/rules
mkdir -p framework/roo-code-specific/.roo/rules-code
```

## File Format Requirements

### Roo Code Format
- **File Extension**: `.md`
- **Location**: `.roo/rules/` for general rules, `.roo/rules-code/` for code-specific rules
- **Content**: Markdown format
- **Loading**: Files are read in alphabetical order

### Directory Structure
- **`.roo/rules/`**: General rules applied to all modes
- **`.roo/rules-code/`**: Rules specific to Code mode
- **`.rooignore`**: File filtering (optional)

## Adaptation Process

### Step 1: Create Main Framework Rules
**File**: `framework/roo-code-specific/.roo/rules/ai-epic-framework.md`

**Content Transformation**:
1. Copy entire content from `framework/generic/user-rules-template.md`
2. Add comprehensive framework overview at the top
3. Include all framework components and navigation
4. Update all internal references to use relative paths within the `.roo/` directory structure
5. Ensure all framework concepts are clearly explained

### Step 2: Create Code-Specific Rules
**File**: `framework/roo-code-specific/.roo/rules-code/ai-epic-framework.md`

**Content Transformation**:
1. Copy entire content from `framework/generic/user-rules-template.md`
2. Focus on code-specific aspects of the framework
3. Include all development workflows and standards
4. Update all internal references to use relative paths
5. Ensure all coding practices and standards are clearly defined

### Step 3: Create .rooignore File
**File**: `framework/roo-code-specific/.rooignore`

**Content**:
```
# AI Epic Framework - Roo Code Configuration
# This file defines which files should be ignored by Roo Code

# Ignore temporary files
*.tmp
*.temp
*.log

# Ignore build artifacts
dist/
build/
node_modules/

# Ignore sensitive files
.env
.env.local
.env.production

# Ignore IDE files
.vscode/
.idea/
*.swp
*.swo

# Ignore OS files
.DS_Store
Thumbs.db
```

## Content Preservation Rules

### Must Preserve Exactly
- All framework concepts and methodologies
- All decision matrices and workflows
- All examples and use cases
- All technical specifications
- All navigation logic (adapted for Roo format)

### Must Adapt
- Organize content for Roo's directory-based system
- Update reference paths to be relative within `.roo/` directory structure
- Ensure content works with Roo's alphabetical loading order
- Adapt for Roo's mode-specific rule system

### Must Not Change
- Core framework logic and processes
- Technical accuracy of any content
- Framework principles and philosophies
- Decision-making criteria and matrices

## Reference Path Updates

### Internal References
Update all internal references to use relative paths within the `.roo/` directory structure:

**Before**:
```markdown
- **Epic Workflow**: [epic-workflow-instructions.md](./epic-workflow-instructions.md)
```

**After**:
```markdown
- **Epic Workflow**: See epic workflow section below
```

### File References
Update all file references to work within Roo's context:

**Before**:
```markdown
@service-template.ts
```

**After**:
```markdown
# Service Template Example
```typescript
// Example service template
export class ServiceTemplate {
  // Implementation details
}
```
```

## Content Organization

### Main Rules File (`.roo/rules/ai-epic-framework.md`)
Include:
- Complete framework overview
- All framework components
- Navigation and decision matrices
- General principles and methodologies
- Cross-mode applicability

### Code-Specific Rules File (`.roo/rules-code/ai-epic-framework.md`)
Include:
- Development-specific workflows
- Coding standards and practices
- Technical implementation guidelines
- Code generation and refactoring rules
- Testing and quality assurance

## Validation Steps

### 1. Content Verification
- [ ] All 6 generic files' content is preserved in the adaptation
- [ ] All framework concepts are clearly explained
- [ ] All decision matrices and workflows are included
- [ ] All internal references work correctly

### 2. Structure Verification
- [ ] Directory structure: `framework/roo-code-specific/.roo/`
- [ ] Rules directory: `.roo/rules/ai-epic-framework.md`
- [ ] Code rules directory: `.roo/rules-code/ai-epic-framework.md`
- [ ] .rooignore file is properly configured
- [ ] No external dependencies remain

### 3. Functionality Verification
- [ ] Roo Code can load all rules
- [ ] Rules are applied in correct order
- [ ] Mode-specific rules work correctly
- [ ] Framework functionality is preserved

## Final Directory Structure

```
framework/roo-code-specific/
├── .roo/
│   ├── rules/
│   │   └── ai-epic-framework.md
│   ├── rules-code/
│   │   └── ai-epic-framework.md
│   └── .rooignore
```

## Error Prevention

1. **Never Skip Content**: Every section from generic files must be included
2. **Never Skip Directory Structure**: Must follow Roo's exact directory requirements
3. **Never Use External Paths**: All references must be relative within `.roo/` directory
4. **Never Change Framework Logic**: The framework must function identically
5. **Never Skip Validation**: Always verify the adaptation works in Roo Code

## Success Criteria

The Roo Code adaptation is successful when:
- All framework content is preserved in the directory structure
- Rules are properly organized in `.roo/rules/` and `.roo/rules-code/`
- .rooignore file is properly configured
- All internal references work within the `.roo/` directory structure
- Roo Code can load and apply all rules correctly
- Framework functionality is identical to the generic version
- Mode-specific rules work as expected 