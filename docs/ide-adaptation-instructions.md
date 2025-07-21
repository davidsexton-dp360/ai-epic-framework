# AI Epic Framework - IDE Adaptation Instructions

## Overview
This document provides comprehensive instructions for AI agents to adapt the AI Epic Framework from the generic format to IDE-specific formats. The goal is to maintain 100% content fidelity while following each IDE's specific requirements and best practices.

## Critical Requirements
- **Content Preservation**: All content from `framework/generic/` must be preserved exactly
- **Format Compliance**: Each IDE adaptation must follow the exact format specified in `docs/ide-documentation/`
- **Directory Structure**: Follow the precise directory structure for each IDE
- **Self-Contained**: Each IDE-specific folder must contain everything needed without external dependencies

## Pre-Adaptation Setup
Before starting any IDE adaptation:

1. **Clear Target Directory**: Remove all existing content from the target `framework/[ide]-specific/` directory
2. **Verify Source**: Ensure `framework/generic/` contains all required files:
   - `user-rules-template.md`
   - `epic-workflow-instructions.md`
   - `problem-solving-framework.md`
   - `architecture-design-process.md`
   - `architecture-lifecycle.md`
   - `general-execution-standards.md`
3. **Read IDE Documentation**: Review the corresponding file in `docs/ide-documentation/` for the target IDE

## IDE Adaptation Process

### Step 1: Select Target IDE
Choose one of the following IDEs to adapt:
- **Cursor AI** → Use instructions in `docs/ide-adaptation-instructions/cursor-adaptation.md`
- **Windsurf** → Use instructions in `docs/ide-adaptation-instructions/windsurf-adaptation.md`
- **GitHub Copilot** → Use instructions in `docs/ide-adaptation-instructions/github-copilot-adaptation.md`
- **Roo Code** → Use instructions in `docs/ide-adaptation-instructions/roo-code-adaptation.md`
- **Cline** → Use instructions in `docs/ide-adaptation-instructions/cline-adaptation.md`
- **Claude Code** → Use instructions in `docs/ide-adaptation-instructions/claude-code-adaptation.md`
- **Trae** → Use instructions in `docs/ide-adaptation-instructions/trae-adaptation.md`
- **Kilo Code** → Use instructions in `docs/ide-adaptation-instructions/kilo-code-adaptation.md`
- **Void IDE** → Use instructions in `docs/ide-adaptation-instructions/void-ide-adaptation.md`
- **Zencoder** → Use instructions in `docs/ide-adaptation-instructions/zencoder-adaptation.md`
- **Gemini CLI** → Use instructions in `docs/ide-adaptation-instructions/gemini-cli-adaptation.md`

### Step 2: Execute IDE-Specific Instructions
Follow the detailed instructions in the corresponding adaptation file. Each file contains:
- Exact directory structure requirements
- File format specifications
- Content transformation rules
- Validation steps

### Step 3: Verify Adaptation
After completing the adaptation:
1. **Content Check**: Verify all generic content is present
2. **Format Check**: Ensure files follow IDE-specific format
3. **Structure Check**: Confirm directory structure matches requirements
4. **Functionality Check**: Test that the adaptation works as expected

## Content Preservation Rules

### Must Preserve
- All framework concepts and methodologies
- All decision matrices and workflows
- All examples and use cases
- All technical specifications
- All navigation and cross-references (adapted for IDE format)

### May Adapt
- File extensions and naming conventions
- Directory structure and organization
- Metadata and frontmatter
- Reference paths (must be relative within the IDE-specific folder)
- Format-specific syntax (while preserving meaning)

### Must Not Change
- Core framework logic and processes
- Technical accuracy of any content
- Framework principles and philosophies
- Decision-making criteria and matrices

## Quality Assurance Checklist

After completing any IDE adaptation, verify:

- [ ] All 6 generic files have been adapted
- [ ] Content is 100% preserved from generic versions
- [ ] Directory structure matches IDE requirements
- [ ] File formats follow IDE specifications
- [ ] All internal references work correctly
- [ ] No external dependencies remain
- [ ] Self-contained functionality maintained
- [ ] IDE-specific features properly implemented

## Error Prevention Guidelines

1. **Never Skip Content**: Every section from generic files must be included
2. **Never Assume Format**: Always check the IDE documentation for exact requirements
3. **Never Use External Paths**: All references must be relative within the IDE-specific folder
4. **Never Deviate from Framework**: The framework logic must remain identical across all IDEs
5. **Never Skip Validation**: Always verify the adaptation works as expected

## Batch Adaptation Process

To adapt for all IDEs simultaneously:

1. **Clear All Directories**: Remove content from all `framework/*-specific/` directories
2. **Process Sequentially**: Apply each IDE's adaptation instructions one by one
3. **Verify Each**: Complete the quality assurance checklist for each IDE
4. **Final Review**: Ensure all 11 IDE adaptations are complete and functional

## Support and Troubleshooting

If encountering issues during adaptation:

1. **Check IDE Documentation**: Review `docs/ide-documentation/[ide]-rules.md`
2. **Verify Generic Content**: Ensure source files in `framework/generic/` are complete
3. **Follow Instructions Exactly**: Do not skip or modify adaptation steps
4. **Validate Output**: Test the adaptation with the target IDE

## Success Criteria

An IDE adaptation is successful when:
- All generic content is preserved exactly
- Format follows IDE-specific requirements precisely
- Directory structure matches IDE documentation
- Self-contained functionality is maintained
- No external dependencies exist
- Framework functionality is identical across all IDEs

---

**Remember**: The goal is to make the AI Epic Framework work identically across all IDEs while respecting each IDE's unique format and structure requirements. Content fidelity is paramount - the framework must function the same way regardless of which IDE is being used. 