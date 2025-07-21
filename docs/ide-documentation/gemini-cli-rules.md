# Gemini CLI Documentation

## Overview
Gemini CLI is a command-line interface for Google's Gemini AI models, providing powerful AI assistance for development tasks, code generation, and project management. It integrates seamlessly with Google Cloud Platform and offers extensive customization options.

## Installation and Setup

### Prerequisites
- Python 3.8 or higher
- Google Cloud SDK (for advanced features)
- Valid Google Cloud project with Gemini API enabled

### Installation
```bash
# Install via pip
pip install google-gemini-cli

# Or install from source
git clone https://github.com/google-gemini/gemini-cli
cd gemini-cli
pip install -e .
```

### Configuration
```bash
# Set up authentication
gemini auth login

# Configure default project
gemini config set project YOUR_PROJECT_ID

# Set default model
gemini config set model gemini-pro
```

## Core Features

### Interactive Chat Mode
```bash
# Start interactive chat
gemini chat

# Chat with specific model
gemini chat --model gemini-pro-vision

# Load context from files
gemini chat --context src/main.py
```

### Code Generation
```bash
# Generate code from description
gemini generate "Create a React component for user profile"

# Generate with specific language
gemini generate --lang python "Function to parse JSON data"

# Generate with template
gemini generate --template react-component "UserCard component"
```

### File Operations
```bash
# Analyze code file
gemini analyze src/main.py

# Refactor code
gemini refactor src/utils.py --style functional

# Document code
gemini document src/api.py --format markdown
```

## Configuration and Customization

### Configuration Files
Gemini CLI uses configuration files for persistent settings:

**Global Configuration** (`~/.gemini/config.yaml`):
```yaml
# Global settings
project: my-project-id
model: gemini-pro
region: us-central1

# Default parameters
temperature: 0.7
max_tokens: 2048

# Output formatting
output_format: markdown
color_output: true

# Integration settings
google_cloud:
  enabled: true
  project: my-project-id
  region: us-central1
```

**Project Configuration** (`.gemini/config.yaml`):
```yaml
# Project-specific settings
name: my-project
description: AI-powered web application

# Project context
context:
  - src/
  - docs/
  - tests/

# Custom prompts
prompts:
  code_review: |
    Review this code for:
    - Security issues
    - Performance optimizations
    - Best practices
    - Documentation quality

  testing: |
    Generate tests for this code:
    - Unit tests
    - Integration tests
    - Edge cases
    - Error scenarios
```

### Environment Variables
```bash
# API configuration
export GEMINI_API_KEY=your_api_key
export GEMINI_PROJECT_ID=your_project_id

# Model settings
export GEMINI_MODEL=gemini-pro
export GEMINI_TEMPERATURE=0.7

# Output settings
export GEMINI_OUTPUT_FORMAT=json
export GEMINI_COLOR_OUTPUT=false
```

## Advanced Features

### Google Cloud Integration
```bash
# Deploy to Google Cloud Run
gemini deploy --service my-app --region us-central1

# Monitor with Cloud Monitoring
gemini monitor --service my-app --metrics requests,latency

# Use Cloud Build
gemini build --config cloudbuild.yaml
```

### Custom Models and Fine-tuning
```bash
# List available models
gemini models list

# Use custom model
gemini chat --model projects/my-project/models/custom-model

# Fine-tune model
gemini fine-tune --data training_data.jsonl --model gemini-pro
```

### Batch Processing
```bash
# Process multiple files
gemini batch --input "src/**/*.py" --command "analyze"

# Generate documentation for all files
gemini batch --input "src/**/*.py" --command "document --format markdown"

# Refactor entire codebase
gemini batch --input "src/**/*.py" --command "refactor --style functional"
```

## Integration with Development Workflow

### IDE Integration
Gemini CLI integrates with popular IDEs:

**VS Code Extension**:
```json
{
  "gemini.command": "gemini",
  "gemini.model": "gemini-pro",
  "gemini.project": "my-project"
}
```

**Git Hooks**:
```bash
#!/bin/sh
# pre-commit hook
gemini analyze --staged --format json > analysis.json
```

### CI/CD Integration
```yaml
# GitHub Actions
- name: Code Analysis
  run: |
    gemini analyze src/ --format json > analysis.json
    gemini document src/ --format markdown > docs/api.md

- name: Security Scan
  run: |
    gemini security-scan src/ --output security-report.json
```

## Custom Commands and Extensions

### Creating Custom Commands
```python
# custom_commands.py
from gemini_cli import Command

class CodeReviewCommand(Command):
    name = "review"
    description = "Review code for best practices"
    
    def execute(self, args):
        # Custom implementation
        pass
```

### Plugin System
```python
# plugins/code_generator.py
from gemini_cli import Plugin

class CodeGeneratorPlugin(Plugin):
    name = "code-generator"
    
    def register_commands(self):
        return [CodeReviewCommand()]
```

## Best Practices

### Security
```bash
# Use service accounts for production
gemini auth service-account --key-file service-account.json

# Enable audit logging
gemini config set audit_logging true

# Use secure API keys
gemini config set api_key_file ~/.gemini/api_key
```

### Performance
```bash
# Use caching for repeated requests
gemini config set cache_enabled true
gemini config set cache_ttl 3600

# Batch operations for efficiency
gemini batch --input "src/**/*.py" --parallel 4
```

### Error Handling
```bash
# Enable verbose logging
gemini --verbose chat

# Save error logs
gemini --log-file errors.log chat

# Retry failed requests
gemini --retry 3 --retry-delay 5 chat
```

## Troubleshooting

### Common Issues
1. **Authentication Errors**: Check API key and project configuration
2. **Rate Limiting**: Implement exponential backoff
3. **Model Availability**: Verify model is available in your region
4. **Network Issues**: Check firewall and proxy settings

### Debug Mode
```bash
# Enable debug logging
gemini --debug chat

# Check configuration
gemini config show

# Validate setup
gemini doctor
```

## API Reference

### Core Commands
```bash
# Chat commands
gemini chat [options] [prompt]
gemini chat --model MODEL [options] [prompt]
gemini chat --context FILE [options] [prompt]

# Generation commands
gemini generate [options] [description]
gemini generate --lang LANGUAGE [options] [description]
gemini generate --template TEMPLATE [options] [description]

# Analysis commands
gemini analyze [options] FILE
gemini analyze --format FORMAT [options] FILE
gemini analyze --output OUTPUT [options] FILE
```

### Configuration Commands
```bash
# Configuration management
gemini config set KEY VALUE
gemini config get KEY
gemini config show
gemini config reset

# Authentication
gemini auth login
gemini auth logout
gemini auth service-account --key-file FILE
```

### Utility Commands
```bash
# Model management
gemini models list
gemini models info MODEL

# Project management
gemini projects list
gemini projects create NAME
gemini projects delete NAME

# Batch operations
gemini batch --input PATTERN --command COMMAND
gemini batch --parallel N --input PATTERN --command COMMAND
```

## Examples

### Code Generation
```bash
# Generate React component
gemini generate --lang typescript --template react-component "User profile card with avatar and details"

# Generate API endpoint
gemini generate --lang python --template fastapi-endpoint "User authentication endpoint with JWT"

# Generate test file
gemini generate --lang python --template pytest "Unit tests for user service"
```

### Code Analysis
```bash
# Analyze security
gemini analyze src/ --security --output security-report.json

# Analyze performance
gemini analyze src/ --performance --output performance-report.json

# Analyze code quality
gemini analyze src/ --quality --output quality-report.json
```

### Documentation
```bash
# Generate API documentation
gemini document src/api/ --format openapi --output docs/api.yaml

# Generate README
gemini document src/ --format markdown --output README.md

# Generate inline documentation
gemini document src/ --format inline --output src/
```

## Integration Examples

### Google Workspace Integration
```bash
# Create Google Doc from code analysis
gemini analyze src/ --format doc --output "Code Analysis Report"

# Update Google Sheets with metrics
gemini metrics --format sheets --output "Project Metrics"

# Sync with Google Drive
gemini sync --drive-folder "Project Documentation"
```

### Google Cloud Platform Integration
```bash
# Deploy to Cloud Run
gemini deploy --service my-app --source src/ --region us-central1

# Monitor with Cloud Monitoring
gemini monitor --service my-app --metrics requests,latency,errors

# Use Cloud Build
gemini build --config cloudbuild.yaml --source src/
```

## Advanced Configuration

### Custom Templates
```yaml
# templates/custom.yaml
templates:
  react-component:
    description: "React functional component with TypeScript"
    template: |
      import React from 'react';
      
      interface {{ComponentName}}Props {
        // Props interface
      }
      
      export const {{ComponentName}}: React.FC<{{ComponentName}}Props> = ({}) => {
        return (
          <div>
            {{ComponentName}} component
          </div>
        );
      };
```

### Custom Prompts
```yaml
# prompts/custom.yaml
prompts:
  code_review:
    description: "Comprehensive code review"
    prompt: |
      Review this code for:
      - Security vulnerabilities
      - Performance issues
      - Code quality and maintainability
      - Documentation completeness
      - Test coverage
      
      Provide specific recommendations for improvement.
```

### Workflow Automation
```yaml
# workflows/development.yaml
workflows:
  new_feature:
    description: "Complete workflow for new feature development"
    steps:
      - name: "Generate code"
        command: "gemini generate --template feature"
      - name: "Generate tests"
        command: "gemini generate --template tests"
      - name: "Generate documentation"
        command: "gemini document --format markdown"
      - name: "Code review"
        command: "gemini analyze --security --quality"
```