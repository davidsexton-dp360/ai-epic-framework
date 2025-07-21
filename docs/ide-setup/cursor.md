# Cursor AI Setup Guide

Cursor AI uses `.mdc` files with YAML frontmatter for advanced rule management. Your framework adaptation has been optimized specifically for Cursor's intelligent context system.

## 🎯 Overview

**Cursor AI Features**:
- `.mdc` files with YAML frontmatter metadata
- Intelligent context loading and management
- Advanced rule hierarchy and organization
- Built-in token optimization

**Framework Benefits in Cursor**:
- Smart conditional loading optimized for Cursor's context system
- Pre-configured decision matrices for efficient AI interactions
- Hierarchical rule organization matching Cursor's architecture
- Token-efficient navigation hub

## 📁 Framework Structure

Your Cursor-specific adaptation includes:

```
framework/cursor-specific/
├── user-rules-template.mdc              # Main system prompt (navigation hub)
├── epic-workflow-instructions.mdc       # Project workflow management
├── problem-solving-framework.mdc        # Systematic troubleshooting
├── architecture-design-process.mdc      # System design methodology
├── architecture-lifecycle.mdc           # Documentation management
├── general-execution-standards.mdc      # Quality and execution protocols
└── README.md                           # Setup instructions
```

## 🚀 Installation

### Step 1: Copy Framework Files

**Option A: Copy All Files (Recommended)**
```bash
# Copy entire Cursor framework to your project
cp -r framework/cursor-specific/* /path/to/your/project/

# Or if you're in your project directory
cp -r /path/to/ai-epic-framework/framework/cursor-specific/* .
```

**Option B: Selective Installation**
```bash
# Copy only the main navigation hub (minimal setup)
cp framework/cursor-specific/user-rules-template.mdc /path/to/your/project/

# Add additional components as needed
cp framework/cursor-specific/epic-workflow-instructions.mdc /path/to/your/project/
```

### Step 2: Configure Cursor AI

**1. Open Cursor Settings**:
- Press `Cmd+,` (macOS) or `Ctrl+,` (Windows/Linux)
- Navigate to "Rules" or "User Rules"

**2. Copy Framework Content to Cursor User Rules**:
- **Copy the content** from `user-rules-template.mdc` 
- **Paste it directly into Cursor's User Rules text area** in the settings
- This content serves as your navigation hub and will intelligently load other components

**3. Set Up Additional Components (Optional)**:
- Copy content from other `.mdc` files as needed for your project
- Or reference them as external files if you prefer file-based organization
- The navigation hub will guide Cursor to load appropriate components

**4. Verify Configuration**:
- Check that Cursor recognizes the framework content in your User Rules
- Test with a framework-specific query to ensure proper loading

## 🎛️ Configuration

### Main Navigation Hub (User Rules Content)

The content from `user-rules-template.mdc` becomes your central control point in Cursor's User Rules:

```yaml
---
name: "AI Epic Framework Navigation"
description: "Smart context management and workflow organization"
version: "1.0"
tags: ["workflow", "architecture", "problem-solving"]
priority: 1
---
```

**Key Features**:
- **Decision Matrix**: Automatically determines which components to load based on your queries
- **Token Optimization**: Prevents context window overload by loading only relevant content
- **Progressive Disclosure**: Scales complexity based on task needs
- **Framework Navigation**: Guides Cursor to apply appropriate systematic approaches

### Component Loading Logic

The framework uses intelligent triggers to load specific components:

| Trigger Keywords | Loaded Component | Purpose |
|-----------------|------------------|---------|
| "epic", "initiative", "project" | Epic Workflow Management | Project structure and task hierarchy |
| "debug", "problem", "troubleshoot" | Problem Solving Framework | Systematic issue investigation |
| "architecture", "design", "component" | Architecture Design Process | System design methodology |
| "document", "lifecycle", "maintain" | Architecture Lifecycle | Documentation management |
| "review", "quality", "standards" | General Execution Standards | Quality protocols and guidelines |

## 🎯 Usage Patterns

### Basic Workflow

**1. Start Every Session**:
```
Load the user-rules-template.mdc as your primary rule
This establishes the navigation hub and decision matrix
```

**2. Conditional Component Loading**:
```
When starting epic work → Framework loads Epic Workflow Management
When debugging issues → Framework loads Problem Solving Framework  
When designing systems → Framework loads Architecture Design Process
```

**3. Token-Efficient Operation**:
```
Only relevant components load for current task
Context window preserved for actual problem-solving
Multiple components can be loaded when needed
```

### Advanced Features

**1. Multi-Component Scenarios**:
```
Complex feature development:
→ Load Epic Workflow (structure) + Architecture Design (technical) + Execution Standards (quality)

Complex debugging:
→ Load Problem Solving (investigation) + Architecture Design (if changes needed) + Execution Standards (research)
```

**2. Custom Triggers**:
You can add custom triggers to the decision matrix:
```markdown
### Your Custom Trigger
**Load When:**
- User mentions "your-keyword"
- Specific project phases
- Custom workflow scenarios

**Related Documentation:**
- [your-component.mdc] - Your custom component
```

## 🔧 Customization for Cursor

### Cursor-Specific Optimizations

**1. YAML Frontmatter Usage**:
```yaml
---
name: "Component Name"
description: "Brief component description"
version: "1.0"
tags: ["tag1", "tag2", "tag3"]
priority: 1-10  # Cursor loading priority
context_limit: 5000  # Token suggestion for this component
---
```

**2. Cursor Context Hints**:
```markdown
## AI Context Header
**When To Use**: [Specific conditions for Cursor to load this component]
**Token Usage**: [Estimated token consumption]
**Priority Level**: [1-10 priority for Cursor's decision engine]
```

**3. Cursor-Optimized Navigation**:
```markdown
## Framework Navigation (Cursor-Optimized)
- **Component Name**: [file.mdc](./file.mdc) - [Purpose and loading conditions]
```

### Adding Custom Components

**1. Create New `.mdc` File**:
```bash
# Create your custom component
vim your-custom-component.mdc
```

**2. Add YAML Frontmatter**:
```yaml
---
name: "Your Custom Component"
description: "Purpose of your custom component"
version: "1.0"
tags: ["custom", "workflow"]
priority: 5
---
```

**3. Update Navigation Hub**:
Add to your Cursor User Rules content:
```markdown
## Framework Navigation
- **Your Custom Component**: [your-custom-component.mdc](./your-custom-component.mdc) - [Purpose]
```

**4. Add Decision Matrix Entry**:
```markdown
### Your Custom Component ([your-custom-component.mdc](./your-custom-component.mdc))
**Load When:**
- [Specific trigger conditions]
```

## 🎮 Practical Examples

### Example 1: Starting a New Feature

**User Query**: "I need to build a user authentication system for our web app"

**Framework Response**:
1. **Navigation Hub Active**: Decision matrix identifies this as epic/project work
2. **Auto-Load**: Epic Workflow Management + Architecture Design Process
3. **Structured Approach**: Break down into Initiative → Epic → Phase → Step
4. **Design Methodology**: Apply systematic architecture design process

### Example 2: Debugging Complex Issue

**User Query**: "The payment system is failing intermittently across multiple components"

**Framework Response**:
1. **Navigation Hub Active**: Decision matrix identifies this as complex problem
2. **Auto-Load**: Problem Solving Framework + General Execution Standards
3. **Systematic Investigation**: Research-driven troubleshooting workflow
4. **Quality Protocols**: Evidence-based decision making

### Example 3: Code Review and Quality

**User Query**: "I need to review this pull request for our architecture standards"

**Framework Response**:
1. **Navigation Hub Active**: Decision matrix identifies this as quality/review work
2. **Auto-Load**: General Execution Standards + Architecture Design Process
3. **Quality Focus**: Apply quality protocols and architecture guidelines
4. **Documentation**: Ensure proper documentation standards

## 🔍 Troubleshooting

### Common Issues

**1. Framework Not Loading**:
```
Problem: Cursor not recognizing .mdc files
Solution: 
- Check file extensions are exactly .mdc
- Verify YAML frontmatter syntax
- Restart Cursor if needed
```

**2. Decision Matrix Not Working**:
```
Problem: Components not auto-loading based on queries
Solution:
- Check that user-rules-template.mdc content is properly pasted into Cursor User Rules
- Verify decision matrix syntax in your User Rules content
- Test with explicit keyword triggers
```

**3. Token Limit Issues**:
```
Problem: Context window getting too full
Solution:
- Load fewer components simultaneously
- Use progressive loading (start minimal, add as needed)
- Check component token estimates in YAML frontmatter
```

### Optimization Tips

**1. Cursor Performance**:
- Keep primary navigation hub content in your User Rules always active
- Load additional components only when needed
- Use Cursor's User Rules system effectively for framework management

**2. Context Management**:
- Start with navigation hub only
- Add components based on task complexity
- Unload unused components when task changes

**3. Team Coordination**:
- Share same framework content across team members' User Rules
- Maintain consistent navigation hub configuration in User Rules
- Document any custom modifications to the framework content

## 📊 Success Metrics

### Framework Effectiveness in Cursor

**1. Context Efficiency**:
- Reduced token usage per session
- Faster AI response times
- More accurate and relevant suggestions

**2. Workflow Improvement**:
- Structured approach to complex projects
- Systematic problem-solving
- Consistent quality standards

**3. Team Benefits**:
- Shared framework understanding
- Consistent documentation practices
- Improved knowledge transfer

## 📚 Additional Resources

### Cursor AI Documentation
- [Cursor Rules Documentation](https://docs.cursor.com/rules)
- [MDC File Format](https://docs.cursor.com/mdc-format)
- [Context Management](https://docs.cursor.com/context)

### Framework Resources
- [Framework Overview](../framework-overview.md) - Complete framework understanding
- [Epic Workflow Guide](../epic-workflow-guide.md) - Detailed workflow implementation
- [Customization Guide](../customization-guide.md) - Adapting for your needs

---

**Ready to get started?** Copy the content from `user-rules-template.mdc` into your Cursor User Rules settings. The intelligent navigation system will guide you through using the right components for each task. 