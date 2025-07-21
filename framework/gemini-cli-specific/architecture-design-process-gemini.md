# Architecture Design Process

# Architecture Design Process

## AI Context Header
**When To Use**: Load when designing system architecture, creating technical proposals, selecting technology stacks, or defining component boundaries. Use for architectural research methodology and design validation.

**Sample Queries**:
1. "Design a scalable architecture for real-time data processing with quality attributes planning"
2. "Create an architecture proposal for migrating from monolith to microservices"
3. "What's the proper research flow for evaluating database technologies for this use case?"

## Framework Navigation
- **Main Navigation**: [user-rules-template.md](./user-rules-template.md) - Access other framework documentation
- **Architecture Lifecycle**: [architecture-lifecycle.md](./architecture-lifecycle.md) - Documentation structure and management
- **Epic Workflow**: [epic-workflow-instructions.md](./epic-workflow-instructions.md) - Design integration in workflows
- **Execution Standards**: [general-execution-standards.md](./general-execution-standards.md) - Research and validation protocols
- **Problem Solving**: [problem-solving-framework.md](./problem-solving-framework.md) - Component analysis methodology

## Design Philosophy
1. Start with **requirements, constraints, and quality attributes**.
2. Research and select **appropriate patterns & technologies**.
3. Design **components with clear boundaries & contracts**.
4. Embed **scalability, performance, and security** from day one.
5. Plan for **testability, observability, and deployability**.

## 1. Requirements Analysis Checklist
- Functional & non-functional requirements gathered
- Business & technical constraints documented
- Integration needs identified
- Success metrics defined

## 2. Pattern & Technology Research
```
# Recommended research flow
1. Scan official docs
2. Search industry white-papers & RFCs
3. Use Ask Perplexity / web search for best practices
4. Compare at least two patterns & stacks
5. Record pros/cons and decision rationale
```

## 3. Component Design Template
```
## Component: [Name]
**Responsibility**: One-sentence summary
**Interfaces**: REST / gRPC / events
**Dependencies**: [List]
**Scaling**: Horizontal AutoScale / etc.
**Failure Modes**: [Describe]
```

## 4. Quality Attributes Planning Matrix
| Attribute   | Strategy                                  |
|-------------|-------------------------------------------|
| Scalability | Stateless services + autoscaling groups   |
| Performance | In-memory cache, async I/O                |
| Security    | Zero-trust, least privilege, encryption   |
| Reliability | Circuit breakers, retries, health probes  |
| Observability | Structured logs, metrics, tracing      |

## 5. Integration Architecture Options
- REST + OpenAPI
- GraphQL federation
- Event-driven with Kafka / NATS / RabbitMQ / etc.
- Microservices with gRPC
- Service mesh (Istio, Linkerd, Consul, Envoy, etc.)

## 6. Data Architecture Decisions
- OLTP vs OLAP split
- Schema versioning & migrations
- Caching & eventual consistency patterns

## 7. Proposal Structure
```
# [Proposal Title]

## Overview
Context + problem statement.

## Principles
Key guiding principles.

## Architecture Diagram
Textual description if image unavailable.

## Components
Detail table per component (template above).

## Trade-offs & Alternatives
Why chosen, what was rejected.

## Implementation Plan
Phases, milestones, rollback strategy.

## Quality Attribute Coverage
Map strategies to attributes.

## Risks & Mitigations
Table of risks.

## Validation & KPIs
Performance tests, security audits, SLIs.
```

## 8. Document Quality Gates
- Follows template & ≤700 lines
- Status field set (Existing / Planned)
- Stakeholders & last-updated filled
- Linked from parent `index.md`
- Reviewed by architecture guild

---
*Version 2025-07-16*
