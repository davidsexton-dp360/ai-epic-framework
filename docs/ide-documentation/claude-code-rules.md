# Claude Code Memory Documentation

## Overview
Claude Code uses a memory system to maintain context across conversations and help you work more efficiently. Memory allows Claude to remember important information about your codebase, preferences, and previous interactions.

## How Memory Works
Memory in Claude Code is designed to be helpful but not intrusive. Claude will automatically remember and reference relevant information when it's useful, but won't bring up irrelevant details from past conversations.

### What Claude Remembers
- **Codebase Context**: Important details about your project structure, architecture, and key files
- **Preferences**: Your coding style, preferred frameworks, and development practices
- **Recent Work**: Information about what you've been working on recently
- **Project-Specific Details**: Domain knowledge, business logic, and technical decisions

### What Claude Doesn't Remember
- **Personal Information**: Private details that aren't relevant to coding
- **Irrelevant Conversations**: Chats that don't relate to your current work
- **Sensitive Data**: Credentials, API keys, or other confidential information

## Memory Management
Claude Code provides several ways to manage memory and ensure it's working effectively for your workflow.

### Viewing Memory
You can see what Claude remembers by asking questions like:
- "What do you remember about this project?"
- "What are my coding preferences?"
- "What have we been working on recently?"

### Updating Memory
Claude's memory updates automatically as you work, but you can also explicitly tell Claude to remember something:
- "Remember that I prefer functional components in React"
- "Remember that this project uses TypeScript strict mode"
- "Remember that we're following the repository pattern for data access"

### Clearing Memory
If you want to start fresh or remove specific information:
- "Forget what you know about my coding preferences"
- "Clear your memory of this project"
- "Start over with a clean slate"

## Memory in Different Contexts
Memory works differently depending on the context of your work:

### Project-Specific Memory
When working in a specific project, Claude will remember:
- Project structure and architecture
- Key files and their purposes
- Dependencies and frameworks used
- Recent changes and decisions

### Global Preferences
Across all projects, Claude remembers:
- Your preferred coding style
- Common frameworks and tools you use
- Development practices you follow
- Communication preferences

### Conversation Context
Within a single conversation, Claude maintains context about:
- What you're currently working on
- Files you've discussed or modified
- Decisions you've made
- Next steps or tasks

## Best Practices for Using Memory

### Be Explicit About Important Information
When you want Claude to remember something important, be explicit:
```
"Remember that this project uses:
- Next.js 14 with App Router
- TypeScript strict mode
- Tailwind CSS for styling
- Prisma for database access"
```

### Provide Context for Decisions
Help Claude understand the reasoning behind your choices:
```
"Remember that we chose to use React Query because:
- It provides excellent caching
- It handles loading and error states automatically
- It integrates well with our existing setup"
```

### Update Memory as Projects Evolve
Keep Claude's memory current as your project changes:
```
"Update your memory - we've switched from Redux to Zustand for state management"
```

## Memory and Collaboration
When working with teams, memory can help maintain consistency:

### Team Standards
Claude can remember team-wide standards:
```
"Remember our team's coding standards:
- Use TypeScript for all new code
- Write unit tests for business logic
- Follow our component naming conventions
- Use our established error handling patterns"
```

### Project History
Memory helps Claude understand the evolution of your project:
```
"Remember that we refactored the authentication system last week to use JWT tokens instead of sessions"
```

## Troubleshooting Memory Issues

### Memory Not Working as Expected
If Claude isn't remembering what you expect:
1. **Be More Explicit**: Clearly state what you want Claude to remember
2. **Provide Context**: Explain why the information is important
3. **Ask for Confirmation**: Check what Claude actually remembers
4. **Refresh Memory**: Explicitly remind Claude of important details

### Too Much Memory
If Claude is bringing up too much irrelevant information:
1. **Be Specific**: Focus on what's relevant to your current work
2. **Clear Irrelevant Memory**: Ask Claude to forget specific details
3. **Start Fresh**: Begin a new conversation for a different topic

### Memory Conflicts
If Claude's memory seems inconsistent:
1. **Clarify Context**: Make sure Claude understands the current situation
2. **Update Memory**: Explicitly update outdated information
3. **Provide Examples**: Show Claude what you mean with concrete examples

## Advanced Memory Features

### Memory Persistence
Claude's memory persists across:
- Multiple conversations in the same project
- Different sessions and restarts
- Various file contexts within a project

### Memory Scope
Memory can be:
- **Project-Specific**: Information about a particular codebase
- **Global**: Preferences that apply across all projects
- **Temporary**: Context for the current conversation only

### Memory Accuracy
Claude strives to remember information accurately, but:
- Memory is based on Claude's understanding of your conversations
- Complex or ambiguous information may be simplified
- Memory can be updated or corrected as needed

## Privacy and Security
Claude Code is designed with privacy in mind:
- Memory is local to your Claude Code instance
- Sensitive information is not stored or transmitted
- You have full control over what Claude remembers
- Memory can be cleared at any time

## Integration with Other Features
Memory works seamlessly with other Claude Code features:
- **File Context**: Memory enhances Claude's understanding of your codebase
- **Code Generation**: Memory helps Claude generate code that matches your preferences
- **Debugging**: Memory helps Claude understand your debugging approach
- **Refactoring**: Memory ensures refactoring follows your established patterns
