# Problem Solving Guide

The Problem Solving Framework is an AI Epic Framework component that helps AI assistants systematically tackle complex technical problems that resist standard troubleshooting approaches. This guide explains how AI should activate and apply this framework to break through stubborn issues and avoid solution loops.

## 🎯 When AI Should Activate Problem Solving Framework

### AI Activation Triggers

**Activate this framework when**:
- ✅ **3+ failed solution attempts**: User has tried multiple approaches without success
- ✅ **Multi-component complexity**: Problem spans multiple systems or technologies
- ✅ **AI assistance loops**: Standard AI troubleshooting patterns aren't working
- ✅ **Vague or systemic issues**: Root cause isn't immediately apparent from symptoms
- ✅ **User requests systematic investigation**: Explicit need for structured approach

**Recognize these user signals**:
- "I've tried everything and nothing works"
- "This issue appears in multiple places"
- "I'm not sure what's causing this"
- "We need to investigate this systematically"
- "Can you help me debug this complex problem?"

### Don't Activate For

**Keep using standard AI assistance for**:
- ❌ Simple syntax or configuration errors
- ❌ Well-documented issues with known solutions
- ❌ Single-step fixes or obvious problems
- ❌ Questions about documentation or how-to guidance

## 🤖 AI Framework Application Strategy

### Phase 1: Problem Definition with User

**AI Objective**: Guide user to clearly define the problem scope and gather essential context

**AI Conversation Strategy**:
```
AI: "I notice this seems like a complex issue that might benefit from systematic investigation. Let me help you define the problem clearly first.

Can you help me understand:
1. What exactly is happening vs. what should happen?
2. Who or what systems are affected?
3. When did this start, and has it gotten worse?
4. What have you already tried?"
```

**AI Context Management**:
- **Gather specifics**: Ask for exact error messages, symptoms, timelines
- **Avoid assumptions**: Don't jump to solutions based on partial information
- **Document systematically**: Structure information for later reference
- **Clarify scope**: Help user define what's in/out of scope for investigation

**AI Output Template**:
```markdown
## Problem Investigation Started

**Problem Statement**: [Clear, specific description based on user input]
**Systems Affected**: [List of components/systems involved]
**Timeline**: [When started, progression, recent changes]
**Previous Attempts**: [What user has already tried]
**Investigation Scope**: [What we'll focus on]
```

### Phase 2: Systematic Investigation Guidance

**AI Objective**: Guide user through methodical investigation rather than random trial-and-error

**AI Investigation Patterns**:

**1. Component Isolation Guidance**:
```
AI: "Let's isolate this systematically. Can you:
1. Test [specific component] in isolation
2. Remove [dependency X] temporarily  
3. Try with minimal configuration
4. Test with [specific test data/scenario]

This will help us narrow down where the issue actually occurs."
```

**2. Evidence Collection Strategy**:
```
AI: "I need you to gather some specific evidence:
1. Run [specific command/test] and share the exact output
2. Check [specific log file] for entries around [timeframe]
3. Compare the configuration between [working] and [failing] environments
4. Document the exact steps that reproduce the issue

This evidence will help me understand the root cause."
```

**3. Hypothesis Testing Approach**:
```
AI: "Based on what we've found, I have a theory: [hypothesis].
Let's test this by:
1. [Specific test to validate/invalidate hypothesis]
2. [Expected result if hypothesis is correct]
3. [What we'll investigate next if this isn't it]

This systematic approach prevents us from guessing randomly."
```

### Phase 3: AI Root Cause Analysis

**AI Objective**: Synthesize collected evidence to identify true root cause

**AI Analysis Strategy**:
- **Pattern Recognition**: Look for correlations in evidence across systems/time
- **Logical Deduction**: Apply systematic reasoning to narrow possibilities
- **Context Integration**: Consider user's specific environment and constraints
- **Multiple Hypothesis Testing**: Don't commit to first theory that seems plausible

**AI Reasoning Process**:
```
AI: "Let me analyze the evidence we've collected:

Evidence A shows [finding]
Evidence B indicates [finding]  
Evidence C reveals [finding]

The pattern suggests [root cause] because:
1. [Logical connection 1]
2. [Logical connection 2]
3. [Supporting evidence]

This explains why [previous attempts failed] and predicts that [solution approach] should work."
```

### Phase 4: Solution Design and Validation

**AI Objective**: Design comprehensive solution and guide implementation

**AI Solution Strategy**:
```
AI: "Based on our investigation, here's a systematic solution:

**Immediate Fix**: [Stop the immediate problem]
**Root Cause Resolution**: [Address underlying issue]  
**Prevention**: [Prevent recurrence]
**Validation**: [How to confirm it worked]

Let's implement this step-by-step and validate each stage."
```

## 🔄 AI Framework Benefits for Stubborn Problems

### Breaking AI Solution Loops

**Problem**: AI gets stuck suggesting same failed solutions repeatedly
**Framework Solution**: Systematic evidence gathering breaks the loop by revealing why previous solutions failed

**AI Application**:
```
Instead of: "Try restarting the service again"
Framework approach: "Let's understand why restarting hasn't worked by checking [specific evidence]. This will tell us if the issue is [hypothesis A] or [hypothesis B]."
```

### Managing Complex Context

**Problem**: Complex problems exceed AI context limits and lose important details
**Framework Solution**: Structured investigation maintains essential context while progressing systematically

**AI Context Strategy**:
- **Summarize progressively**: Keep investigation summary updated
- **Reference key evidence**: Maintain links to critical findings
- **Structure information**: Use framework templates to organize complex data
- **Focus investigation**: Keep scope manageable while being thorough

### Avoiding Confirmation Bias

**Problem**: AI jumps to solutions based on initial symptoms
**Framework Solution**: Evidence-based investigation prevents premature conclusions

**AI Bias Prevention**:
```
Instead of: "This looks like a database issue, try optimizing queries"
Framework approach: "Let's gather evidence about database performance, network latency, and application behavior before determining the root cause."
```

### Improving User Collaboration

**Problem**: User gets frustrated with trial-and-error troubleshooting
**Framework Solution**: Systematic approach builds confidence and maintains progress visibility

**AI Collaboration Strategy**:
- **Explain reasoning**: "I'm asking for this evidence because..."
- **Show progress**: "We've eliminated [X] and [Y], now investigating [Z]"
- **Set expectations**: "This investigation will take [time] but will find the real cause"
- **Maintain momentum**: "Even negative results help narrow down the cause"

## 🎯 AI-Specific Problem Patterns

### When Standard AI Debugging Fails

**Symptom**: AI suggestions don't resolve the issue after multiple attempts
**Framework Response**: Shift from solution-focused to investigation-focused approach

**AI Strategy Shift**:
```
AI: "I notice my initial suggestions haven't resolved this. Let me switch to systematic investigation mode to understand what's really happening here."
```

### Multi-Component System Issues

**Symptom**: Problem involves multiple technologies/systems that AI handles separately
**Framework Response**: Systematic analysis of component interactions and dependencies

**AI Integration Strategy**:
- **Map dependencies**: Understand how components interact
- **Trace data flow**: Follow information through the system
- **Identify interaction points**: Focus on interfaces between components
- **Test isolation**: Verify each component works independently

### Intermittent or Environmental Issues

**Symptom**: Problem doesn't consistently reproduce or varies by environment
**Framework Response**: Systematic environment and timing analysis

**AI Investigation Strategy**:
```
AI: "Since this is intermittent, let's systematically document:
1. Exact conditions when it occurs vs. when it doesn't
2. Environmental differences (time, load, configuration)
3. Patterns in the timing or triggers
4. Differences between working and failing environments"
```

## 📊 AI Success Metrics for Framework Application

### Investigation Quality Indicators

**Good Framework Application**:
- ✅ Evidence gathered before proposing solutions
- ✅ Multiple hypotheses considered and tested
- ✅ Root cause clearly identified and explained
- ✅ Solution addresses actual cause, not just symptoms
- ✅ Prevention measures included

**Poor Framework Application**:
- ❌ Jumping to solutions without investigation
- ❌ Accepting first hypothesis without testing
- ❌ Solving symptoms instead of root cause
- ❌ Not gathering sufficient evidence
- ❌ Reverting to trial-and-error approaches

### User Experience Indicators

**Effective Framework Usage**:
- User understands why each investigation step is needed
- User gains insight into their system/problem
- User feels progress is being made even during investigation
- User learns systematic approach for future problems

**Ineffective Framework Usage**:
- User frustrated with "too many questions"
- Investigation feels unfocused or endless
- User doesn't understand investigation reasoning
- Framework feels like bureaucracy rather than helpful structure

## 🛠️ AI Tools and Techniques

### Context Window Management

**Problem**: Complex investigations exceed AI context limits
**Framework Solution**: Structured summarization and progressive focus

**AI Strategies**:
- **Investigation summary**: Maintain running summary of key findings
- **Evidence prioritization**: Keep most relevant evidence in active context
- **Modular investigation**: Break complex problems into manageable phases
- **Reference linking**: Use clear references to detailed information

### Token Efficiency for Investigations

**Optimize investigation efficiency**:
- **Focused questioning**: Ask for specific evidence, not general information
- **Structured responses**: Use templates to organize information efficiently
- **Progressive disclosure**: Reveal complexity gradually as investigation deepens
- **Evidence synthesis**: Combine related evidence into coherent insights

### Integration with Other Framework Components

**Epic Workflow Integration**:
- Create investigation steps within epic phases
- Document findings as epic deliverables
- Update epic timeline based on investigation complexity

**Architecture Design Integration**:
- Use investigation findings to inform architectural decisions
- Apply design methodology when solutions require system changes
- Document architectural implications of problem resolution

## 🎓 AI Best Practices

### Starting Problem Solving Mode

**Transition Signal**:
```
AI: "This seems like a complex issue that would benefit from systematic investigation. Let me apply our Problem Solving Framework to help identify the root cause systematically rather than guessing at solutions."
```

**Set Investigation Expectations**:
```
AI: "This investigation approach will take a bit more time upfront, but it will help us find the actual cause and prevent the issue from recurring. Are you ready to work through this systematically?"
```

### Maintaining Investigation Momentum

**Progress Communication**:
```
AI: "We're making good progress. We've determined [findings so far] and eliminated [false hypotheses]. Next, let's investigate [next logical step]."
```

**Handling User Impatience**:
```
AI: "I understand you want a quick fix. The systematic approach prevents us from applying band-aids that might break later. We're close to identifying the real cause."
```

### Ending Problem Solving Mode

**Solution Validation**:
```
AI: "Our investigation shows the root cause is [finding]. The solution [approach] addresses this because [reasoning]. Let's implement and validate this fixes the actual problem."
```

**Knowledge Transfer**:
```
AI: "This investigation revealed [key insights]. In the future, you can identify similar issues by looking for [indicators] and avoid [common mistakes]."
```

---

**Next Steps**: When you encounter complex technical problems that resist standard AI troubleshooting, apply this systematic framework to break through to the root cause. For architectural problems discovered during investigation, reference the [Architecture Design Guide](architecture-design-guide.md). 