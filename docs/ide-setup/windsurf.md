# Windsurf IDE Setup Guide

Windsurf by Codeium uses `.windsurfrules` files with a 6,000 character limit for AI assistance rules. This setup guide explains how to install and optimize the AI Epic Framework for Windsurf's specific requirements.

## 🎯 Overview

**Windsurf Features**:
- `.windsurfrules` files for AI assistance configuration
- 6,000 character limit per rules file
- Integrated with Codeium's AI platform
- Project-level rule application
- Built-in context optimization

**Framework Benefits in Windsurf**:
- Optimized content fitting within character limits
- Essential framework guidance in compact format
- Project-scoped intelligent assistance
- Efficient token usage through condensed rules

## 📁 Framework Structure

Your Windsurf adaptation includes:

```
framework/windsurf-specific/
├── .windsurfrules                       # Main framework rules (6K chars)
├── global_rules.md                      # Extended documentation (optional)
├── framework-components/                # Individual component files
│   ├── epic-workflow-summary.md        # Condensed workflow guide
│   ├── problem-solving-summary.md      # Condensed troubleshooting
│   ├── architecture-summary.md         # Condensed design guidance
│   └── execution-standards-summary.md  # Condensed quality standards
└── README.md                           # Setup instructions
```

## 🚀 Installation

### Step 1: Copy Framework Rules

**Primary Installation**:
```bash
# Copy the main rules file to your project root
cp framework/windsurf-specific/.windsurfrules /path/to/your/project/

# Or if you're in your project directory
cp /path/to/ai-epic-framework/framework/windsurf-specific/.windsurfrules .
```

**Extended Documentation (Optional)**:
```bash
# Copy additional reference materials if needed
cp framework/windsurf-specific/global_rules.md /path/to/your/project/
cp -r framework/windsurf-specific/framework-components/ /path/to/your/project/
```

### Step 2: Verify Windsurf Recognition

**1. Open Windsurf IDE**:
- Open your project in Windsurf
- Windsurf automatically detects `.windsurfrules` files

**2. Check Rules Loading**:
- Look for confirmation that rules are loaded
- Test AI assistance to verify framework guidance is active

**3. Validate Character Limit**:
- Ensure `.windsurfrules` file is under 6,000 characters
- Windsurf will warn if the limit is exceeded

## 🎛️ Configuration

### Main Rules File (.windsurfrules)

The `.windsurfrules` file contains condensed framework guidance:

```markdown
# AI Epic Framework for Windsurf

## Framework Overview
This project uses the AI Epic Framework for systematic project management, 
problem-solving, and architecture design. Apply these guidelines for 
consistent AI-assisted development.

## Core Components
- Epic Workflow: Initiative → Epic → Phase → Step hierarchy
- Problem Solving: Systematic troubleshooting after 3+ failed attempts
- Architecture Design: Structured system design methodology
- Quality Standards: Consistent execution and documentation

## Component Loading Logic
Based on your query, reference the appropriate approach:

### Epic/Project Work
When planning features or managing projects:
- Break work into Initiative → Epic → Phase → Step
- Use INDEX.md and REQUIREMENTS.md templates
- Apply sequential numbering and clear ownership
- Reference: epic-workflow-summary.md for details

### Problem Solving
When debugging complex issues (3+ failures, multi-component):
- Define problem clearly with impact assessment
- Plan systematic investigation approach
- Document evidence and test hypotheses
- Reference: problem-solving-summary.md for methodology

### Architecture Design
When designing systems or major changes:
- Gather functional and non-functional requirements
- Research and evaluate technology options
- Design for quality attributes (performance, security, reliability)
- Reference: architecture-summary.md for process

### Code Review/Quality
When reviewing code or ensuring standards:
- Apply systematic quality criteria
- Use evidence-based decision making
- Follow consistent documentation standards
- Reference: execution-standards-summary.md for guidelines

## Usage Patterns
- Specify which component you're using: "Using Epic Workflow, help me..."
- Reference component summaries for detailed methodology
- Apply framework principles consistently across team
- Document decisions and rationale for future reference

## Project Context
[Customize this section with your project-specific information]
- Tech Stack: [Your technologies]
- Team Practices: [Your methodologies]
- Quality Standards: [Your specific requirements]
```

### Character Limit Optimization

**Content Strategies**:
- **Essential Only**: Include only critical framework guidance
- **Condensed Language**: Use bullet points and short sentences
- **Reference System**: Point to detailed component files for full methodology
- **Project-Specific**: Customize content for your specific project needs

**Character Management**:
```bash
# Check character count of your .windsurfrules file
wc -c .windsurfrules

# Should be under 6,000 characters
# If over limit, trim non-essential content
```

## 🎯 Usage Patterns

### Component Reference System

Since Windsurf has character limits, the framework uses a reference-based approach:

**Main Rules**: Core framework guidance (within 6K limit)
**Component Files**: Detailed methodology (unlimited size)

### Practical Usage

**1. Epic Planning**:
```
Developer: "Using the Epic Workflow approach, help me break down 
user authentication into phases and steps."

Windsurf: [References epic-workflow guidance from .windsurfrules and 
applies Initiative → Epic → Phase → Step methodology]
```

**2. Problem Investigation**:
```
Developer: "I have a complex database performance issue. Using our 
Problem Solving Framework, help me investigate systematically."

Windsurf: [References problem-solving guidance and applies systematic 
investigation methodology]
```

**3. Architecture Planning**:
```
Developer: "I need to design a new microservice. Following our 
Architecture Design process, what should I consider?"

Windsurf: [References architecture guidance and applies systematic 
design methodology]
```

## 🔧 Customization for Windsurf

### Project-Specific Adaptations

**Technology Stack Integration**:
```markdown
## Project Context (Add to .windsurfrules)
**Tech Stack**: React + Node.js + PostgreSQL + Docker
**Architecture**: Microservices with REST APIs
**Team Practices**: Agile with 2-week sprints
**Quality Gates**: ESLint, Jest, TypeScript, Docker Compose

## Framework Application
When providing assistance:
- Consider our microservices architecture
- Reference our tech stack capabilities
- Apply our quality standards
- Follow our sprint-based delivery approach
```

**Team Workflow Integration**:
```markdown
## Team Development Process (Add to .windsurfrules)
1. All features follow Epic Workflow (Initiative → Epic → Phase → Step)
2. Complex issues use Problem Solving Framework
3. Architecture changes require Design Process documentation
4. All code must meet our Execution Standards
```

### Optimizing for Character Limits

**Content Prioritization** (in order of importance):
1. **Framework Overview** (100-200 chars): What the framework is
2. **Component Loading Logic** (2000-3000 chars): When to use each component
3. **Usage Patterns** (1000-1500 chars): How to apply components
4. **Project Context** (1000-2000 chars): Project-specific adaptations

**Condensing Techniques**:
```markdown
# Instead of:
"The Epic Workflow Management system provides a comprehensive approach 
to breaking down large projects into manageable hierarchical structures..."

# Use:
"Epic Workflow: Break projects into Initiative → Epic → Phase → Step hierarchy"

# Instead of:
"The Problem Solving Framework should be activated when you have attempted 
multiple solutions without success..."

# Use:
"Problem Solving: Use after 3+ failed attempts, multi-component issues"
```

## 🎮 Practical Examples

### Example 1: New Feature Development

**User Query**: "I need to implement user authentication for our web app"

**Windsurf Response**:
1. **Framework Recognition**: Identifies this as epic/project work
2. **Epic Workflow Application**: Suggests Initiative → Epic → Phase → Step breakdown
3. **Structured Approach**: Provides systematic feature development guidance
4. **Reference**: Points to epic-workflow-summary.md for detailed methodology

### Example 2: Performance Issue Investigation

**User Query**: "The API is slow and I've tried several optimizations without success"

**Windsurf Response**:
1. **Framework Recognition**: Identifies this as complex problem (multiple attempts)
2. **Problem Solving Application**: Applies systematic investigation methodology
3. **Evidence Collection**: Guides systematic evidence gathering and hypothesis testing
4. **Reference**: Points to problem-solving-summary.md for detailed process

### Example 3: System Architecture Design

**User Query**: "I need to design a notification system for our microservices"

**Windsurf Response**:
1. **Framework Recognition**: Identifies this as architecture design work
2. **Design Process Application**: Applies systematic design methodology
3. **Quality Attributes**: Considers performance, reliability, scalability
4. **Reference**: Points to architecture-summary.md for detailed process

## 🔍 Troubleshooting

### Common Issues

**1. Rules Not Loading**:
```
Problem: Windsurf not applying framework rules
Solution:
- Verify .windsurfrules exists in project root
- Check file is under 6,000 character limit
- Restart Windsurf if needed
- Ensure file has correct markdown formatting
```

**2. Character Limit Exceeded**:
```
Problem: .windsurfrules file too large
Solution:
- Trim non-essential content
- Use more condensed language
- Move detailed content to component files
- Reference external files for full methodology
```

**3. Inconsistent Framework Application**:
```
Problem: AI not consistently applying framework
Solution:
- Be explicit: "Using Epic Workflow, help me..."
- Reference specific components in queries
- Ensure .windsurfrules content is clear and specific
- Test with framework-specific keywords
```

### Optimization Tips

**1. Content Efficiency**:
- Use bullet points instead of paragraphs
- Eliminate redundant words
- Use abbreviations for common terms
- Focus on actionable guidance

**2. Reference Strategy**:
- Keep essential logic in .windsurfrules
- Store detailed methodology in component files
- Use clear references to external files
- Maintain navigation between files

**3. Team Coordination**:
- Share same .windsurfrules across team
- Maintain consistent component file versions
- Document any project-specific customizations
- Regular review of character usage

## 📊 Success Metrics

### Framework Effectiveness in Windsurf

**1. Character Efficiency**:
- Essential framework guidance within 6K limit
- Clear component loading logic
- Actionable guidance without excessive detail

**2. Usage Quality**:
- Consistent framework application
- Clear component selection
- Effective problem-solving guidance

**3. Team Benefits**:
- Shared framework understanding
- Consistent development approaches
- Improved project structure and quality

## 📚 Additional Resources

### Windsurf Documentation
- [Windsurf IDE Documentation](https://docs.codeium.com/windsurf)
- [Windsurf Rules System](https://docs.codeium.com/windsurf/rules)
- [Codeium AI Features](https://docs.codeium.com/features)

### Framework Resources
- [Framework Overview](../framework-overview.md) - Complete framework understanding
- [Epic Workflow Guide](../epic-workflow-guide.md) - Detailed workflow implementation
- [Customization Guide](../customization-guide.md) - Adapting for your needs

### Component Summaries (Reference Files)
- `epic-workflow-summary.md` - Condensed workflow methodology
- `problem-solving-summary.md` - Condensed troubleshooting approach
- `architecture-summary.md` - Condensed design process
- `execution-standards-summary.md` - Condensed quality guidelines

---

**Ready to optimize your AI assistance within character limits?** Copy the `.windsurfrules` file to your project root and customize the project context section for your specific needs. The framework will provide structured guidance while respecting Windsurf's 6K character limit. 