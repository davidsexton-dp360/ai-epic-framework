# Gemini CLI Setup Guide

Gemini CLI is Google's official command-line interface for Gemini AI, supporting the `GEMINI.md` format for system prompts and configuration. This guide explains how to configure the AI Epic Framework for Gemini CLI's Google ecosystem integration and terminal-based development workflows.

## 🎯 Overview

**Gemini CLI Features**:
- Official Google CLI tool for Gemini AI
- `GEMINI.md` system prompt format support
- Google ecosystem integration (Cloud, Workspace, etc.)
- Terminal-based AI assistance
- Google Cloud authentication and security

**Framework Benefits in Gemini CLI**:
- Google ecosystem-integrated systematic development
- Terminal-optimized framework guidance
- Cloud-native epic management and documentation
- Google security and privacy standards

## 📁 Framework Structure

Your Gemini CLI adaptation includes:

```
framework/gemini-cli-specific/
├── GEMINI.md                           # Main Gemini CLI system prompt
├── gemini-config.json                  # CLI configuration settings
├── google-cloud-integration.json       # Google Cloud service integration
├── framework-components/               # Component definitions for CLI
│   ├── epic-workflow-cli.md           # Terminal-optimized epic workflow
│   ├── problem-solving-cli.md         # CLI-friendly problem solving
│   ├── architecture-design-cli.md     # Terminal architecture design
│   └── execution-standards-cli.md     # CLI execution standards
├── google-workspace-integration/       # Google Workspace integration
│   ├── docs-templates/                # Google Docs epic templates
│   ├── sheets-tracking/               # Google Sheets progress tracking
│   └── drive-organization/            # Google Drive epic organization
├── cloud-deployment/                   # Google Cloud deployment configs
│   ├── cloud-functions-setup.json    # Serverless framework deployment
│   ├── app-engine-config.yaml        # App Engine epic hosting
│   └── firestore-epic-storage.json   # Epic data storage configuration
└── README.md                          # Setup instructions
```

## 🚀 Installation

### Step 1: Install Gemini CLI

**1. Install Google Cloud CLI (if not already installed)**:
```bash
# Install Google Cloud CLI
curl https://sdk.cloud.google.com | bash
exec -l $SHELL

# Initialize and authenticate
gcloud init
gcloud auth login
```

**2. Install Gemini CLI**:
```bash
# Install Gemini CLI (check Google's official documentation for latest method)
pip install google-generativeai
# or
npm install -g @google/generative-ai-cli
```

**3. Authenticate with Gemini**:
```bash
# Set up Gemini API credentials
gcloud auth application-default login
export GOOGLE_API_KEY="your-gemini-api-key"

# Verify installation
gemini --version
gemini --help
```

### Step 2: Copy Framework Configuration

**Copy Framework Files**:
```bash
# Copy all framework files to Gemini CLI directory
mkdir -p ~/.gemini-cli/framework
cp -r framework/gemini-cli-specific/* ~/.gemini-cli/framework/

# Or copy to project-specific location
cp framework/gemini-cli-specific/GEMINI.md /path/to/your/project/
cp framework/gemini-cli-specific/gemini-config.json /path/to/your/project/
```

### Step 3: Configure Gemini CLI

**1. Set Framework Configuration**:
```bash
# Initialize Gemini CLI with framework
gemini config set --system-prompt ~/.gemini-cli/framework/GEMINI.md
gemini config set --config-file ~/.gemini-cli/framework/gemini-config.json
```

**2. Configure Google Cloud Integration**:
```bash
# Set up Google Cloud project for framework
gcloud config set project your-project-id
gemini cloud-integration enable --config google-cloud-integration.json
```

**3. Verify Framework Setup**:
```bash
# Test framework functionality
gemini test-framework
gemini list-components
gemini test-google-integration
```

## 🎛️ Configuration

### Main System Prompt (GEMINI.md)

The `GEMINI.md` file configures Gemini CLI for framework usage:

```markdown
# AI Epic Framework for Gemini CLI

You are using the AI Epic Framework through Google's Gemini CLI to provide systematic, Google ecosystem-integrated AI assistance for complex application development.

## Framework Overview
The AI Epic Framework provides systematic approaches to complex application development through four core components:
1. Epic Workflow: Initiative → Epic → Phase → Step project hierarchy
2. Problem Solving: Systematic investigation for stubborn technical issues
3. Architecture Design: Requirements-driven architectural decision making
4. Execution Standards: Quality protocols and development guidelines

## Google Ecosystem Integration
- Leverage Google Cloud Platform for epic deployment and scaling
- Integrate with Google Workspace for documentation and collaboration
- Use Google security and privacy standards for framework operations
- Apply Google development best practices and tool ecosystem

## Component Activation Strategy

### Epic Workflow Component
**Activate when**: Developer mentions complex applications, large features, or project planning
**Google Integration**: 
- Create epic documentation in Google Docs
- Track progress in Google Sheets
- Store epic artifacts in Google Drive
- Deploy epic phases using Google Cloud Platform

**Application Strategy**:
1. Break down complex applications into Initiative → Epic → Phase → Step hierarchy
2. Create Google Workspace-compatible epic documentation
3. Integrate with Google Cloud for epic deployment and monitoring
4. Use Google collaboration tools for team epic coordination

### Problem Solving Component
**Activate when**: Developer has stubborn technical issues, multiple failed attempts, or complex debugging needs
**Google Integration**:
- Use Google Cloud debugging and monitoring tools
- Document investigations in Google Docs with collaborative editing
- Leverage Google's AI and ML tools for pattern analysis
- Apply Google Cloud security best practices

**Application Strategy**:
1. Apply systematic investigation methodology using Google Cloud tools
2. Document evidence and findings in Google Workspace
3. Use Google's AI/ML capabilities for advanced problem analysis
4. Integrate with Google Cloud monitoring and alerting

### Architecture Design Component  
**Activate when**: Developer needs architectural decisions, system design, or technology choices
**Google Integration**:
- Document architecture decisions in Google Docs
- Create architecture diagrams using Google Drawings/Slides
- Evaluate Google Cloud services and architecture patterns
- Apply Google Cloud Well-Architected Framework principles

**Application Strategy**:
1. Guide requirements-driven architectural decision making
2. Evaluate Google Cloud services for application needs
3. Document decisions using Google Workspace collaboration tools
4. Apply Google Cloud architecture best practices and patterns

### Execution Standards Component
**Activate when**: Developer needs code quality, review processes, or best practices guidance
**Google Integration**:
- Use Google Cloud Build for CI/CD and quality gates
- Apply Google's engineering best practices and style guides
- Integrate with Google Cloud monitoring for quality metrics
- Document standards in Google Sites or Docs

**Application Strategy**:
1. Apply Google engineering quality standards and practices
2. Use Google Cloud tools for code quality and security scanning
3. Implement Google-recommended CI/CD and deployment practices
4. Maintain quality documentation using Google Workspace

## Terminal Optimization
- Provide terminal-friendly command suggestions and workflows
- Structure output for optimal CLI reading and processing
- Support multi-session development with cloud state persistence
- Integrate with common terminal tools and Google Cloud CLI

## Google Cloud Native Patterns
- Recommend Google Cloud services appropriate for epic requirements
- Apply serverless-first and cloud-native architecture principles
- Integrate with Google's AI/ML services for enhanced capabilities
- Use Google Cloud security and compliance features

## Privacy and Security
- Follow Google Cloud security best practices
- Respect data privacy using Google's privacy controls
- Use Google Cloud IAM for access control and security
- Apply Google's responsible AI principles
```

### CLI Configuration File

The `gemini-config.json` configures Gemini CLI settings:

```json
{
  "framework": {
    "name": "AI Epic Framework",
    "version": "1.0",
    "google_integration": true,
    "cli_optimized": true
  },
  "gemini_settings": {
    "model": "gemini-pro",
    "temperature": 0.3,
    "max_tokens": 8192,
    "safety_settings": "google_recommended"
  },
  "google_cloud": {
    "project_id": "your-google-cloud-project",
    "region": "us-central1",
    "services": {
      "cloud_build": true,
      "cloud_run": true,
      "firestore": true,
      "cloud_storage": true,
      "cloud_functions": true
    }
  },
  "google_workspace": {
    "domain": "your-company.com",
    "integration_enabled": true,
    "services": {
      "docs": true,
      "sheets": true,
      "drive": true,
      "sites": true
    }
  },
  "framework_components": {
    "epic_workflow": {
      "cli_file": "framework-components/epic-workflow-cli.md",
      "google_docs_template": "google-workspace-integration/docs-templates/epic-template.docx",
      "sheets_tracking": "google-workspace-integration/sheets-tracking/epic-progress.xlsx"
    },
    "problem_solving": {
      "cli_file": "framework-components/problem-solving-cli.md",
      "cloud_debugging": true,
      "cloud_monitoring": true
    },
    "architecture_design": {
      "cli_file": "framework-components/architecture-design-cli.md",
      "cloud_architecture_center": true,
      "well_architected_framework": true
    },
    "execution_standards": {
      "cli_file": "framework-components/execution-standards-cli.md",
      "cloud_build_integration": true,
      "code_quality_gates": true
    }
  },
  "terminal_settings": {
    "output_format": "terminal_optimized",
    "color_output": true,
    "progress_indicators": true,
    "command_suggestions": true
  }
}
```

### Google Cloud Integration

The `google-cloud-integration.json` configures cloud services:

```json
{
  "epic_management": {
    "cloud_run": {
      "epic_dashboard_service": "epic-dashboard",
      "region": "us-central1",
      "min_instances": 0,
      "max_instances": 10
    },
    "firestore": {
      "database_id": "epic-framework",
      "collections": {
        "initiatives": "initiatives",
        "epics": "epics", 
        "phases": "phases",
        "steps": "steps"
      }
    },
    "cloud_storage": {
      "bucket_name": "epic-framework-artifacts",
      "epic_documentation": "epics/",
      "architecture_decisions": "architecture/",
      "investigation_reports": "investigations/"
    }
  },
  "development_tools": {
    "cloud_build": {
      "epic_deployment_triggers": true,
      "quality_gates": true,
      "security_scanning": true
    },
    "cloud_monitoring": {
      "epic_progress_dashboards": true,
      "application_performance": true,
      "error_tracking": true
    },
    "cloud_logging": {
      "framework_audit_logs": true,
      "application_logs": true,
      "investigation_logs": true
    }
  },
  "ai_ml_services": {
    "vertex_ai": {
      "code_analysis": true,
      "pattern_recognition": true,
      "performance_optimization": true
    },
    "cloud_translation": {
      "multi_language_documentation": true
    }
  }
}
```

## 🎯 Usage Patterns

### Google Ecosystem Framework Application

**1. Google Cloud Epic Development**:
```bash
# Start epic planning with Google integration
$ gemini epic plan --google-cloud

Developer: "Using Epic Workflow, plan a serverless customer service application"

Gemini CLI Response:
1. Activates Epic Workflow component with Google Cloud focus
2. Creates epic structure optimized for Google Cloud Platform
3. Generates Google Docs documentation with team collaboration
4. Sets up Google Sheets progress tracking
5. Configures Google Cloud deployment pipeline for epic phases
```

**2. Google Cloud Problem Investigation**:
```bash
# Start investigation with Google Cloud tools
$ gemini investigate --cloud-debugging

Developer: "Complex latency issue in our Cloud Run service that persists after optimization"

Gemini CLI Response:
1. Recognizes Problem Solving Framework trigger
2. Applies systematic investigation using Google Cloud monitoring
3. Leverages Cloud Trace and Cloud Profiler for evidence collection
4. Documents findings in collaborative Google Docs
5. Uses Vertex AI for pattern analysis and recommendations
```

**3. Google Cloud Architecture Design**:
```bash
# Architecture design with Google Cloud focus
$ gemini design --cloud-native

Developer: "Design architecture for a real-time analytics platform"

Gemini CLI Response:
1. Activates Architecture Design Process with Google Cloud emphasis
2. Evaluates Google Cloud services (BigQuery, Dataflow, Pub/Sub)
3. Applies Google Cloud Well-Architected Framework principles
4. Creates architecture documentation in Google Docs with diagrams
5. Provides Google Cloud deployment and scaling recommendations
```

### Google Workspace Integration Benefits

**1. Collaborative Documentation**:
- Epic documentation automatically created in Google Docs with team sharing
- Architecture decisions documented with collaborative editing
- Investigation reports shared across teams with real-time collaboration
- Framework standards maintained in Google Sites for organization-wide access

**2. Progress Tracking and Analytics**:
- Epic progress tracked in Google Sheets with automatic updates
- Team productivity metrics in Google Data Studio dashboards
- Problem resolution tracking with Google Analytics integration
- Framework usage analytics with Google Cloud monitoring

**3. Google Cloud Native Development**:
- Epic phases deployed as Google Cloud Run services
- Serverless architecture using Google Cloud Functions
- Data storage and management with Firestore and Cloud Storage
- CI/CD integration with Google Cloud Build

## 🔧 Customization for Google Ecosystem

### Google Cloud Project Configuration

**Cloud-Native Epic Setup**:
```json
{
  "google_cloud_epic_config": {
    "project_id": "my-app-epic-framework",
    "region": "us-central1",
    "epic_services": {
      "epic_dashboard": {
        "service": "cloud_run",
        "image": "gcr.io/my-app/epic-dashboard",
        "environment_variables": {
          "FIRESTORE_PROJECT": "my-app-epic-framework",
          "GOOGLE_WORKSPACE_DOMAIN": "mycompany.com"
        }
      },
      "epic_api": {
        "service": "cloud_functions",
        "runtime": "python39",
        "trigger": "https",
        "environment_variables": {
          "EPIC_STORAGE_BUCKET": "my-app-epic-artifacts"
        }
      }
    },
    "data_storage": {
      "firestore": {
        "mode": "native",
        "location": "us-central1",
        "collections": ["initiatives", "epics", "phases", "steps"]
      },
      "cloud_storage": {
        "bucket": "my-app-epic-artifacts",
        "lifecycle_rules": {
          "investigation_data_retention": "90_days",
          "epic_documentation_retention": "indefinite"
        }
      }
    }
  }
}
```

### Google Workspace Team Integration

**Workspace Collaboration Setup**:
```json
{
  "google_workspace_integration": {
    "domain": "mycompany.com",
    "framework_structure": {
      "epic_documentation": {
        "drive_folder": "AI Epic Framework",
        "docs_templates": {
          "epic_index": "Epic Index Template",
          "phase_planning": "Phase Planning Template",
          "architecture_decision": "ADR Template"
        },
        "sharing_permissions": {
          "development_team": "editor",
          "architecture_team": "editor", 
          "management": "viewer"
        }
      },
      "progress_tracking": {
        "sheets_workbook": "Epic Framework Progress Tracking",
        "dashboards": {
          "epic_completion": "Epic Completion Dashboard",
          "team_productivity": "Team Productivity Metrics",
          "problem_resolution": "Problem Resolution Tracking"
        }
      }
    }
  }
}
```

## 🎮 Practical Examples

### Example 1: Google Cloud Serverless Epic

**Scenario**: Building a serverless customer feedback platform

**Terminal Workflow**:
```bash
# Start Google Cloud serverless epic
$ gemini epic plan --serverless --google-cloud

Developer: "Plan a serverless customer feedback platform using Google Cloud"

Gemini CLI: "Creating serverless epic structure for Google Cloud:

Initiative: Customer Feedback Platform
├── Epic 1: Feedback Collection API (Cloud Functions + Firestore)
├── Epic 2: Real-time Analytics (BigQuery + Dataflow)
├── Epic 3: Dashboard Frontend (Cloud Run + React)
└── Epic 4: Notification System (Pub/Sub + Cloud Functions)

Google Cloud Integration:
- Epic documentation created in Google Docs
- Progress tracking set up in Google Sheets
- Cloud Build CI/CD pipeline configured
- Firestore database initialized for epic tracking
- Cloud Run services prepared for deployment

Commands to continue:
$ gcloud functions deploy feedback-api --source . --trigger-http
$ gcloud run deploy dashboard --image gcr.io/project/dashboard
$ gcloud pubsub topics create feedback-notifications"
```

### Example 2: Google Cloud Problem Investigation

**Scenario**: Performance issue in multi-service application

**Terminal Workflow**:
```bash
# Start Google Cloud problem investigation
$ gemini investigate --performance --cloud-monitoring

Developer: "Performance degradation across multiple Cloud Run services"

Gemini CLI: "Applying Problem Solving Framework with Google Cloud tools:

Investigation Setup:
1. Cloud Monitoring: Checking service latency and error rates
2. Cloud Trace: Analyzing request flow across services
3. Cloud Profiler: CPU and memory usage analysis
4. Cloud Logging: Error pattern analysis

Evidence Collection Commands:
$ gcloud logging read 'resource.type=cloud_run_revision' --limit=1000
$ gcloud alpha trace list-traces --filter='startTime>=2024-01-01'

Systematic Analysis:
- Service dependency mapping using Cloud Trace
- Performance baseline comparison using Cloud Monitoring
- Resource utilization analysis using Cloud Profiler
- Error correlation analysis using Cloud Logging

Investigation documented in Google Docs: [link]
Progress tracked in Google Sheets: [link]"
```

### Example 3: Google Cloud Architecture Design

**Scenario**: Designing scalable e-commerce platform

**Terminal Workflow**:
```bash
# Google Cloud architecture design
$ gemini design --ecommerce --scalable --google-cloud

Developer: "Design scalable e-commerce platform architecture using Google Cloud"

Gemini CLI: "Applying Architecture Design Process for Google Cloud e-commerce:

Requirements Analysis:
- High availability and global scale requirements
- Payment processing security and compliance
- Real-time inventory and order management
- Multi-channel customer experience

Google Cloud Service Evaluation:
1. Frontend: Cloud CDN + Cloud Run (global distribution)
2. API Gateway: Cloud Endpoints (rate limiting, authentication)
3. Microservices: Cloud Run (auto-scaling, containerized)
4. Database: Cloud Spanner (global consistency) + Firestore (real-time)
5. Search: Elasticsearch on Compute Engine
6. Analytics: BigQuery + Dataflow (real-time processing)
7. Storage: Cloud Storage (product images, documents)
8. Security: Cloud IAM + Cloud Security Command Center

Architecture Documentation:
- Decision rationale documented in Google Docs
- Architecture diagrams created in Google Drawings
- Service specifications stored in Google Drive
- Implementation plan tracked in Google Sheets

Deployment Commands:
$ gcloud run deploy api-gateway --image gcr.io/project/api-gateway
$ gcloud spanner databases create ecommerce --instance=prod-instance"
```

## 🔍 Troubleshooting

### Common Issues

**1. Google Cloud Authentication Issues**:
```bash
# Check authentication status
gcloud auth list
gemini auth-status

# Re-authenticate if needed
gcloud auth login
gcloud auth application-default login

# Verify project access
gcloud projects describe your-project-id
```

**2. Framework Component Loading Issues**:
```bash
# Check framework configuration
gemini config show

# Verify component files
ls -la ~/.gemini-cli/framework/framework-components/

# Test component loading
gemini test-component epic-workflow
gemini test-component problem-solving
```

**3. Google Workspace Integration Problems**:
```bash
# Check workspace permissions
gemini workspace-status

# Test Google Docs/Sheets integration
gemini test-workspace-integration

# Verify domain settings
gemini config show google-workspace
```

### Optimization Tips

**1. Google Cloud Performance**:
- Use regional Google Cloud services close to your development team
- Configure Cloud CDN for epic documentation and dashboard assets
- Set up Cloud Monitoring alerts for framework service performance
- Use Cloud Build caching for faster epic deployment cycles

**2. Terminal Workflow Optimization**:
- Set up shell aliases for common Gemini CLI framework commands
- Use Google Cloud Shell for consistent terminal environment
- Configure gcloud CLI for optimal framework integration
- Set up terminal multiplexing for persistent Google Cloud sessions

**3. Google Workspace Collaboration**:
- Set up automated epic documentation generation in Google Docs
- Configure Google Sheets for real-time epic progress tracking
- Use Google Sites for framework standards and team onboarding
- Set up Google Calendar integration for epic milestone tracking

## 📊 Success Metrics

### Framework Effectiveness in Google Ecosystem

**1. Google Cloud Integration**:
- Epic deployment automation using Google Cloud Build and Cloud Run
- Effective use of Google Cloud monitoring and debugging for problem solving
- Architecture decisions leveraging appropriate Google Cloud services
- Framework documentation and collaboration through Google Workspace

**2. Development Productivity**:
- Faster epic development cycles with Google Cloud native tools
- Improved problem resolution using Google Cloud observability
- Better architectural decisions with Google Cloud Well-Architected guidance
- Enhanced team collaboration through Google Workspace integration

**3. Google Ecosystem Benefits**:
- Seamless integration with existing Google Cloud infrastructure
- Effective use of Google AI/ML services for enhanced problem analysis
- Improved security and compliance using Google Cloud security features
- Cost optimization through Google Cloud resource management

## 📚 Additional Resources

### Google Documentation
- [Gemini API Documentation](https://developers.generativeai.google/docs) - Official Gemini API docs
- [Google Cloud CLI Reference](https://cloud.google.com/sdk/gcloud/reference) - gcloud command reference
- [Google Workspace API](https://developers.google.com/workspace) - Workspace integration APIs

### Framework Resources
- [Framework Overview](../framework-overview.md) - Complete framework understanding
- [Epic Workflow Guide](../epic-workflow-guide.md) - Detailed workflow implementation
- [Customization Guide](../customization-guide.md) - Adapting for your needs

### Google Cloud Development
- [Google Cloud Architecture Center](https://cloud.google.com/architecture) - Architecture patterns and best practices
- [Google Cloud Well-Architected Framework](https://cloud.google.com/architecture/framework) - Architecture design principles
- [Google Cloud DevOps](https://cloud.google.com/devops) - Development and deployment best practices

---

**Ready to enhance your development with Google ecosystem-integrated systematic AI assistance?** Install Gemini CLI, configure the framework with Google Cloud and Workspace integration, and experience systematic AI guidance that leverages Google's powerful cloud platform and collaboration tools. 