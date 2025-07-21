# General Execution Standards Rules

## Decision Making Protocol
1. **Research-First**: Always consult official documentation first
2. **Multi-Source Validation**: Cross-check from at least two authoritative sources
3. **Quality Over Speed**: Plan thoroughly, implement incrementally
4. **Comprehensive Documentation**: Capture every decision in task documentation
5. **Architecture Compliance**: Reference/update architecture docs for every significant change

## Tool Usage Guidelines
- **Context7**: Deep codebase pattern & dependency analysis
- **Perplexity**: External best-practice & doc retrieval
- **grep/rg**: Fast in-repo search for configs & patterns
- **wc -l**: Enforce <700-line doc rule
- **find**: Structure & file existence checks

## File Navigation and Verification
1. **Existence Check**: Verify files exist before referencing
2. **Content Validation**: Ensure content matches expectations
3. **Path Verification**: Confirm relative paths are correct
4. **Format Compliance**: Validate against IDE-specific requirements

## Quality Assurance Standards
- **Documentation**: Every significant decision must be documented
- **Testing**: All changes must include appropriate tests
- **Review**: Code and documentation changes require review
- **Validation**: Verify changes work as expected

## Research-First Methodology
- Always research before implementing solutions
- Use multiple information sources (documentation, examples, community)
- Document findings and decision rationale
- Validate assumptions through testing

## Context Management
- Optimize token usage through conditional documentation loading
- Use progressive disclosure for complex investigations
- Maintain context window efficiency
- Implement task-specific guidance systems
