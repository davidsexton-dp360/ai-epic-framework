# Cline Adaptation Instructions

## Overview
This document provides step-by-step instructions for adapting the AI Epic Framework to Cline's folder-based rules system with `.clinerules/` directory and organized markdown files.

## Pre-Adaptation Setup

### 1. Clear Target Directory
```bash
# Remove all existing content from cline-specific directory
rm -rf framework/cline-specific/*
```

### 2. Create Directory Structure
```bash
# Create the .clinerules directory structure
mkdir -p framework/cline-specific/.clinerules
```

## File Format Requirements

### Cline Format
- **File Extension**: `.md`
- **Location**: `.clinerules/` directory
- **Content**: Markdown format
- **Loading**: All markdown files are processed and combined
- **Organization**: Use numbered prefixes for loading order

### Directory Structure
- **`.clinerules/`**: Folder containing all active rules
- **Numbered Files**: Use prefixes like `01-`, `02-` for loading order
- **Descriptive Names**: Clear, descriptive filenames

## Adaptation Process

### Step 1: Create Framework Overview
**File**: `framework/cline-specific/.clinerules/01-framework-overview.md`

**Content Transformation**:
1. Copy entire content from `framework/generic/user-rules-template.md`
2. Add comprehensive framework overview at the top
3. Include all framework components and navigation
4. Update all internal references to use relative paths within the `.clinerules/` directory
5. Ensure all framework concepts are clearly explained

### Step 2: Create Epic Workflow Instructions
**File**: `framework/cline-specific/.clinerules/02-epic-workflow.md`

**Content Transformation**:
1. Copy entire content from `framework/generic/epic-workflow-instructions.md`
2. Focus on epic workflow management system
3. Include all task hierarchy and workflow processes
4. Update all internal references to use relative paths
5. Ensure all workflow concepts are clearly defined

### Step 3: Create Problem Solving Framework
**File**: `framework/cline-specific/.clinerules/03-problem-solving.md`

**Content Transformation**:
1. Copy entire content from `framework/generic/problem-solving-framework.md`
2. Focus on systematic problem-solving methodology
3. Include all troubleshooting approaches and decision matrices
4. Update all internal references to use relative paths
5. Ensure all problem-solving concepts are clearly explained

### Step 4: Create Architecture Design Process
**File**: `framework/cline-specific/.clinerules/04-architecture-design.md`

**Content Transformation**:
1. Copy entire content from `framework/generic/architecture-design-process.md`
2. Focus on architecture design methodology and templates
3. Include all design processes and decision frameworks
4. Update all internal references to use relative paths
5. Ensure all architecture concepts are clearly defined

### Step 5: Create Execution Standards
**File**: `framework/cline-specific/.clinerules/05-execution-standards.md`

**Content Transformation**:
1. Copy entire content from `framework/generic/general-execution-standards.md`
2. Focus on quality assurance and execution standards
3. Include all development practices and quality measures
4. Update all internal references to use relative paths
5. Ensure all execution standards are clearly defined

## Content Preservation Rules

### Must Preserve Exactly
- All framework concepts and methodologies
- All decision matrices and workflows
- All examples and use cases
- All technical specifications
- All navigation logic (adapted for Cline format)

### Must Adapt
- Organize content into numbered files for proper loading order
- Update reference paths to be relative within `.clinerules/` directory
- Ensure content works with Cline's file processing system
- Adapt for Cline's folder-based rule organization

### Must Not Change
- Core framework logic and processes
- Technical accuracy of any content
- Framework principles and philosophies
- Decision-making criteria and matrices

## Reference Path Updates

### Internal References
Update all internal references to use relative paths within the `.clinerules/` directory:

**Before**:
```markdown
- **Epic Workflow**: [epic-workflow-instructions.md](./epic-workflow-instructions.md)
```

**After**:
```markdown
- **Epic Workflow**: See 02-epic-workflow.md for detailed instructions
```

### File References
Update all file references to work within Cline's context:

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

### File Loading Order
1. **01-framework-overview.md**: Complete framework overview and navigation
2. **02-epic-workflow.md**: Epic workflow management system
3. **03-problem-solving.md**: Problem-solving methodology
4. **04-architecture-design.md**: Architecture design process
5. **05-execution-standards.md**: Quality assurance and standards

### Content Distribution
- **01-framework-overview.md**: Main framework concepts, navigation, decision matrices
- **02-epic-workflow.md**: Task hierarchy, workflow processes, delegation
- **03-problem-solving.md**: Troubleshooting approaches, decision frameworks
- **04-architecture-design.md**: Design methodologies, templates, processes
- **05-execution-standards.md**: Quality standards, development practices

## Validation Steps

### 1. Content Verification
- [ ] All 6 generic files' content is preserved across the 5 Cline files
- [ ] All framework concepts are clearly explained
- [ ] All decision matrices and workflows are included
- [ ] All internal references work correctly

### 2. Structure Verification
- [ ] Directory structure: `framework/cline-specific/.clinerules/`
- [ ] All files have numbered prefixes (01-, 02-, etc.)
- [ ] All files have descriptive names
- [ ] No external dependencies remain

### 3. Functionality Verification
- [ ] Cline can load all rules
- [ ] Rules are processed in correct order
- [ ] All markdown files are combined properly
- [ ] Framework functionality is preserved

## Final Directory Structure

```
framework/cline-specific/
└── .clinerules/
    ├── 01-framework-overview.md
    ├── 02-epic-workflow.md
    ├── 03-problem-solving.md
    ├── 04-architecture-design.md
    └── 05-execution-standards.md
```

## Error Prevention

1. **Never Skip Content**: Every section from generic files must be included
2. **Never Skip Numbering**: Must use numbered prefixes for proper loading order
3. **Never Use External Paths**: All references must be relative within `.clinerules/` directory
4. **Never Change Framework Logic**: The framework must function identically
5. **Never Skip Validation**: Always verify the adaptation works in Cline

## Success Criteria

The Cline adaptation is successful when:
- All framework content is preserved across the 5 numbered files
- Rules are properly organized in `.clinerules/` directory
- Files are numbered correctly for proper loading order
- All internal references work within the `.clinerules/` directory structure
- Cline can load and combine all rules correctly
- Framework functionality is identical to the generic version
- All markdown files are processed and combined as expected 

## Overview
This document provides step-by-step instructions for adapting the AI Epic Framework to Cline's folder-based rules system with `.clinerules/` directory and organized markdown files.

## Pre-Adaptation Setup

### 1. Clear Target Directory
```bash
# Remove all existing content from cline-specific directory
rm -rf framework/cline-specific/*
```

### 2. Create Directory Structure
```bash
# Create the .clinerules directory structure
mkdir -p framework/cline-specific/.clinerules
```

## File Format Requirements

### Cline Format
- **File Extension**: `.md`
- **Location**: `.clinerules/` directory
- **Content**: Markdown format
- **Loading**: All markdown files are processed and combined
- **Organization**: Use numbered prefixes for loading order

### Directory Structure
- **`.clinerules/`**: Folder containing all active rules
- **Numbered Files**: Use prefixes like `01-`, `02-` for loading order
- **Descriptive Names**: Clear, descriptive filenames

## Adaptation Process

### Step 1: Create Framework Overview
**File**: `framework/cline-specific/.clinerules/01-framework-overview.md`

**Content Transformation**:
1. Copy entire content from `framework/generic/user-rules-template.md`
2. Add comprehensive framework overview at the top
3. Include all framework components and navigation
4. Update all internal references to use relative paths within the `.clinerules/` directory
5. Ensure all framework concepts are clearly explained

### Step 2: Create Epic Workflow Instructions
**File**: `framework/cline-specific/.clinerules/02-epic-workflow.md`

**Content Transformation**:
1. Copy entire content from `framework/generic/epic-workflow-instructions.md`
2. Focus on epic workflow management system
3. Include all task hierarchy and workflow processes
4. Update all internal references to use relative paths
5. Ensure all workflow concepts are clearly defined

### Step 3: Create Problem Solving Framework
**File**: `framework/cline-specific/.clinerules/03-problem-solving.md`

**Content Transformation**:
1. Copy entire content from `framework/generic/problem-solving-framework.md`
2. Focus on systematic problem-solving methodology
3. Include all troubleshooting approaches and decision matrices
4. Update all internal references to use relative paths
5. Ensure all problem-solving concepts are clearly explained

### Step 4: Create Architecture Design Process
**File**: `framework/cline-specific/.clinerules/04-architecture-design.md`

**Content Transformation**:
1. Copy entire content from `framework/generic/architecture-design-process.md`
2. Focus on architecture design methodology and templates
3. Include all design processes and decision frameworks
4. Update all internal references to use relative paths
5. Ensure all architecture concepts are clearly defined

### Step 5: Create Execution Standards
**File**: `framework/cline-specific/.clinerules/05-execution-standards.md`

**Content Transformation**:
1. Copy entire content from `framework/generic/general-execution-standards.md`
2. Focus on quality assurance and execution standards
3. Include all development practices and quality measures
4. Update all internal references to use relative paths
5. Ensure all execution standards are clearly defined

## Content Preservation Rules

### Must Preserve Exactly
- All framework concepts and methodologies
- All decision matrices and workflows
- All examples and use cases
- All technical specifications
- All navigation logic (adapted for Cline format)

### Must Adapt
- Organize content into numbered files for proper loading order
- Update reference paths to be relative within `.clinerules/` directory
- Ensure content works with Cline's file processing system
- Adapt for Cline's folder-based rule organization

### Must Not Change
- Core framework logic and processes
- Technical accuracy of any content
- Framework principles and philosophies
- Decision-making criteria and matrices

## Reference Path Updates

### Internal References
Update all internal references to use relative paths within the `.clinerules/` directory:

**Before**:
```markdown
- **Epic Workflow**: [epic-workflow-instructions.md](./epic-workflow-instructions.md)
```

**After**:
```markdown
- **Epic Workflow**: See 02-epic-workflow.md for detailed instructions
```

### File References
Update all file references to work within Cline's context:

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

### File Loading Order
1. **01-framework-overview.md**: Complete framework overview and navigation
2. **02-epic-workflow.md**: Epic workflow management system
3. **03-problem-solving.md**: Problem-solving methodology
4. **04-architecture-design.md**: Architecture design process
5. **05-execution-standards.md**: Quality assurance and standards

### Content Distribution
- **01-framework-overview.md**: Main framework concepts, navigation, decision matrices
- **02-epic-workflow.md**: Task hierarchy, workflow processes, delegation
- **03-problem-solving.md**: Troubleshooting approaches, decision frameworks
- **04-architecture-design.md**: Design methodologies, templates, processes
- **05-execution-standards.md**: Quality standards, development practices

## Validation Steps

### 1. Content Verification
- [ ] All 6 generic files' content is preserved across the 5 Cline files
- [ ] All framework concepts are clearly explained
- [ ] All decision matrices and workflows are included
- [ ] All internal references work correctly

### 2. Structure Verification
- [ ] Directory structure: `framework/cline-specific/.clinerules/`
- [ ] All files have numbered prefixes (01-, 02-, etc.)
- [ ] All files have descriptive names
- [ ] No external dependencies remain

### 3. Functionality Verification
- [ ] Cline can load all rules
- [ ] Rules are processed in correct order
- [ ] All markdown files are combined properly
- [ ] Framework functionality is preserved

## Final Directory Structure

```
framework/cline-specific/
└── .clinerules/
    ├── 01-framework-overview.md
    ├── 02-epic-workflow.md
    ├── 03-problem-solving.md
    ├── 04-architecture-design.md
    └── 05-execution-standards.md
```

## Error Prevention

1. **Never Skip Content**: Every section from generic files must be included
2. **Never Skip Numbering**: Must use numbered prefixes for proper loading order
3. **Never Use External Paths**: All references must be relative within `.clinerules/` directory
4. **Never Change Framework Logic**: The framework must function identically
5. **Never Skip Validation**: Always verify the adaptation works in Cline

## Success Criteria

The Cline adaptation is successful when:
- All framework content is preserved across the 5 numbered files
- Rules are properly organized in `.clinerules/` directory
- Files are numbered correctly for proper loading order
- All internal references work within the `.clinerules/` directory structure
- Cline can load and combine all rules correctly
- Framework functionality is identical to the generic version
- All markdown files are processed and combined as expected 