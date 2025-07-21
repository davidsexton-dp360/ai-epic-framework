# GitHub Copilot Custom Instructions Documentation

## Overview
GitHub Copilot allows you to create custom instructions that apply to your entire repository. These instructions help Copilot understand your project's context, coding style, and specific requirements.

## Repository Custom Instructions
The instructions in the `.github/copilot-instructions.md` file are available for use by Copilot Chat as soon as you save the file. The complete set of instructions will be automatically added to requests that you submit to Copilot in the context of that repository. For example, they are added to the prompt you submit to Copilot Chat.

## Creating Custom Instructions

### Step 1: Create the Directory and File
In the root of your repository, create a file named `.github/copilot-instructions.md`.
Create the `.github` directory if it does not already exist.

### Step 2: Add Instructions
Add natural language instructions to the file, in Markdown format.
Whitespace between instructions is ignored, so the instructions can be written as a single paragraph, each on a new line, or separated by blank lines for legibility.

### Step 3: Verify Instructions
To see your instructions in action, go to https://github.com/copilot, attach the repository containing the instructions file, and start a conversation.

## Repository Custom Instructions in Use
In Copilot Chat's immersive view (github.com/copilot), you can start a conversation that uses repository custom instructions by adding, as an attachment, the repository that contains the instructions file.

Whenever repository custom instructions are used by Copilot Chat, the instructions file is added as a reference for the response that's generated. To find out whether repository custom instructions were used, expand the list of references at the top of a chat response in the Chat panel and check whether the `.github/copilot-instructions.md` file is listed.

You can click the reference to open the file.

**Note**: It is possible for multiple types of custom instructions to apply to a conversation. Personal instructions take the highest priority, followed by repository instructions, with organization instructions prioritized last. However, all sets of relevant instructions are still combined and provided to Copilot Chat.

Whenever possible, you should avoid providing conflicting sets of instructions. If you are concerned about response quality, you can also choose to temporarily disable repository instructions.

## Custom Instructions Visibility
Custom instructions are not visible in the Chat view or inline chat, but you can verify that they are being used by Copilot by looking at the References list of a response in the Chat view. If custom instructions were added to the prompt that was sent to the model, the `.github/copilot-instructions.md` file is listed as a reference. You can click the reference to open the file.

## Enabling or Disabling Repository Custom Instructions
You can choose whether or not you want Copilot to use repository-based custom instructions.

### Enabling or Disabling Custom Instructions for Copilot Chat
Custom instructions are enabled for Copilot Chat by default but you can disable, or re-enable, them at any time. This applies to your own use of Copilot Chat and does not affect other users.

**On GitHub.com, do one of the following:**
1. Go to a repository with a custom instructions file and open the assistive chat panel.
2. Go to the immersive view of Copilot Chat (github.com/copilot) and attach a repository that contains a custom instructions file.

Click the button at the top of the Chat panel, or the top right of the immersive page.

## Example Custom Instructions

### Basic Project Context
```markdown
# Project Context
This is a React TypeScript project using Next.js 14 with App Router.
We use Tailwind CSS for styling and follow a component-based architecture.
All API calls should use the built-in Next.js API routes.
```

### Coding Standards
```markdown
# Coding Standards
- Use TypeScript for all new code
- Follow ESLint and Prettier configurations
- Use functional components with hooks
- Implement proper error handling
- Write unit tests for business logic
- Use descriptive variable and function names
```

### Architecture Guidelines
```markdown
# Architecture Guidelines
- Use the repository pattern for data access
- Implement proper separation of concerns
- Follow RESTful API design principles
- Use environment variables for configuration
- Implement proper logging and monitoring
```

### Documentation Requirements
```markdown
# Documentation Requirements
- Update README.md when adding new features
- Include JSDoc comments for public APIs
- Maintain changelog entries for releases
- Document environment setup requirements
```

## Best Practices

### Writing Effective Instructions
- **Be Specific**: Provide clear, actionable guidance
- **Use Examples**: Include code examples when helpful
- **Keep Updated**: Regularly review and update instructions
- **Avoid Conflicts**: Ensure instructions don't contradict each other
- **Use Markdown**: Format instructions for better readability

### Organization
- **Group Related Instructions**: Use headers to organize content
- **Prioritize Important Rules**: Put critical instructions first
- **Keep Concise**: Avoid overly verbose instructions
- **Version Control**: Include instructions in your repository

### Team Collaboration
- **Review Instructions**: Have team members review custom instructions
- **Consistent Standards**: Ensure instructions align with team practices
- **Documentation**: Explain the reasoning behind important instructions
- **Regular Updates**: Update instructions as project evolves

## Troubleshooting

### Instructions Not Being Applied
1. **Check File Location**: Ensure `.github/copilot-instructions.md` is in the repository root
2. **Verify File Format**: Make sure the file uses proper Markdown syntax
3. **Check References**: Look for the file in the References list of Copilot responses
4. **Restart Copilot**: Try restarting Copilot Chat to reload instructions

### Conflicting Instructions
1. **Review All Sources**: Check personal, repository, and organization instructions
2. **Prioritize Clearly**: Ensure important instructions are not overridden
3. **Test Instructions**: Verify instructions work as expected
4. **Simplify**: Remove redundant or conflicting instructions

## Integration with Other Features
- **Copilot Chat**: Instructions are automatically included in chat conversations
- **Inline Suggestions**: Instructions influence code completion suggestions
- **Code Review**: Instructions help Copilot understand context during reviews
- **Documentation**: Instructions can guide documentation generation

## Advanced Usage

### Conditional Instructions
You can create instructions that apply to specific scenarios:
```markdown
# Frontend Development
When working on React components:
- Use functional components with hooks
- Implement proper prop validation
- Follow component naming conventions

# Backend Development
When working on API routes:
- Use proper HTTP status codes
- Implement input validation
- Add comprehensive error handling
```

### File-Specific Instructions
Reference specific files or patterns:
```markdown
# Database Schema
When modifying database schemas, refer to @prisma/schema.prisma for conventions.

# API Documentation
When updating API endpoints, ensure @docs/api.md is updated accordingly.
```

### Workflow Instructions
Guide Copilot through specific workflows:
```markdown
# Feature Development Workflow
When implementing new features:
1. Create feature branch from main
2. Implement core functionality
3. Add unit tests
4. Update documentation
5. Create pull request
```