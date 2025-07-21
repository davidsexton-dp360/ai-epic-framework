# Architecture Design Process Rules

## Research-First Architecture Methodology
1. **Research Phase**: Gather comprehensive information about requirements, constraints, and existing solutions
2. **Analysis Phase**: Evaluate options against quality attributes and business requirements
3. **Design Phase**: Create detailed architecture proposals with clear rationale
4. **Validation Phase**: Review and validate design decisions
5. **Documentation Phase**: Create comprehensive architecture documentation

## Component Design Template
```
## Component: [Name]
**Responsibility**: One-sentence summary
**Interfaces**: REST / gRPC / events
**Dependencies**: [List]
**Scaling**: Horizontal AutoScale / etc.
**Failure Modes**: [Describe]
```

## Quality Attributes Planning Matrix
| Attribute   | Strategy                                  |
|-------------|-------------------------------------------|
| Scalability | Stateless services + autoscaling groups   |
| Performance | In-memory cache, async I/O                |
| Security    | Zero-trust, least privilege, encryption   |
| Reliability | Circuit breakers, retries, health probes  |
| Observability | Structured logs, metrics, tracing      |

## Architecture Decision Record Template
```
## Architecture Decision Record

### Context
[Background and problem statement]

### Decision
[Clear statement of the decision made]

### Rationale
[Detailed explanation of why this decision was made]

### Alternatives Considered
[List of alternatives with pros/cons]

### Consequences
[Positive and negative consequences]

### Implementation Notes
[Specific implementation guidance]
```

## Architecture Lifecycle Management

### Document Organization Structure
```
docs/architecture/
├── index.md (mandatory)
├── [category]/
│   ├── index.md (mandatory)
│   ├── [component].md
│   └── [component].md
└── [category]/
    ├── index.md (mandatory)
    └── [component].md
```

### Mandatory Requirements
- **Index Files**: Every architecture folder must contain an `index.md`
- **Document Size**: Maximum 700 lines per document
- **Categorization**: Organize by system component or architectural concern
- **Cross-References**: Maintain links between related documents

### Document Lifecycle
1. **Creation**: New documents follow canonical structure
2. **Updates**: Track changes and maintain version history
3. **Deprecation**: Mark obsolete documents clearly
4. **Archival**: Move deprecated documents to archive folder

### Architecture Discovery Commands
```bash
# Find all architecture documents
find docs/architecture/ -name "*.md" -type f

# Check document sizes
find docs/architecture/ -name "*.md" -exec wc -l {} \;

# Find missing index files
find docs/architecture/ -type d -exec test ! -f {}/index.md \; -print

# Search architecture content
grep -r "architecture" docs/architecture/
```
