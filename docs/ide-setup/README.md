# IDE Setup Guides Overview

The AI Epic Framework supports 11 different AI coding IDEs, each with purpose-built adaptations matching their specific rule systems and capabilities. This guide helps you choose the right IDE adaptation and provides quick links to detailed setup instructions.

## 📄 License

This framework is licensed under the MIT License - see the [LICENSE](../../LICENSE) file for details.

**MIT License Benefits:**
- ✅ **Free for commercial use** - Use in any project, including commercial applications
- ✅ **Modify freely** - Adapt the framework to your specific needs
- ✅ **Distribute** - Share modified versions with your team or community
- ✅ **Simple attribution** - Just include the license and copyright notice

## 🎯 Quick IDE Selection

### Choose Your IDE

| IDE | Best For | Rule System | Team Support | Setup Complexity |
|-----|----------|-------------|--------------|------------------|
| **[Cursor AI](cursor.md)** | Individual developers, token optimization | `.mdc` files with YAML | Individual | Medium |
| **[GitHub Copilot](github-copilot.md)** | Team-wide consistency, repository-scoped | `.github/copilot-instructions.md` | Excellent | Easy |
| **[Windsurf](windsurf.md)** | Codeium users, character-limited rules | `.windsurfrules` (6K char limit) | Good | Easy |
| **[Cline](cline.md)** | VS Code users, MCP integration | `.clinerules` + custom instructions | Good | Medium |
| **[Roo Code](roo-code.md)** | VS Code extension users | Custom instructions + `.rooignore` | Good | Easy |
| **[Claude Code](claude-code.md)** | Terminal-based development | Configuration files | Individual | Medium |
| **[Trae](trae.md)** | IDE-agnostic AI assistance | IDE configuration | Good | Easy |
| **[Kilo Code](kilo-code.md)** | Open source VS Code users | Custom rules + instructions | Good | Easy |
| **[Void IDE](void-ide.md)** | Privacy-focused development | VS Code-style config | Individual | Medium |
| **[Zencoder](zencoder.md)** | Enterprise users, multiple formats | Flexible rule formats | Excellent | Advanced |
| **[Gemini CLI](gemini-cli.md)** | Google ecosystem, CLI workflows | `GEMINI.md` format | Individual | Easy |

### Quick Recommendation Guide

**For Teams** → [GitHub Copilot](github-copilot.md)
- Repository-scoped instructions
- Automatic team-wide consistency
- Version-controlled framework evolution

**For Individual Power Users** → [Cursor AI](cursor.md)
- Advanced conditional loading
- Token optimization
- Sophisticated rule hierarchy

**For VS Code Users** → [Cline](cline.md) or [Roo Code](roo-code.md)
- Native VS Code integration
- Familiar extension-based setup
- Good community support

**For Enterprise** → [Zencoder](zencoder.md)
- Multiple rule format support
- Enterprise-grade features
- Advanced customization options

## 🏗️ Framework Structure Comparison

### Single-File IDEs
These IDEs use one primary rule file with embedded framework navigation:

- **GitHub Copilot**: `.github/copilot-instructions.md` (repository-wide)
- **Windsurf**: `.windsurfrules` (6K character limit)
- **Claude Code**: Configuration-based approach
- **Gemini CLI**: `GEMINI.md` system prompt

### Multi-File IDEs
These IDEs support conditional loading of multiple framework components:

- **Cursor AI**: `.mdc` files with intelligent loading
- **Cline**: `.clinerules` + component files
- **Roo Code**: Custom instructions + multiple components
- **Kilo Code**: Custom rules + custom instructions
- **Void IDE**: VS Code-style multi-file configuration
- **Zencoder**: Multiple format support (`.rules`, `.cursorrules`, etc.)
- **Trae**: IDE configuration + component files

## 🚀 Setup Process Overview

### Universal Setup Steps

**1. Generate Framework Adaptations**:
```bash
# Generate all IDE adaptations
python3 create_ide_adaptations.py

# Or generate specific IDE
python3 create_ide_adaptations.py --ide cursor
python3 create_ide_adaptations.py --ide github-copilot
```

**2. Choose Your IDE**:
- Review the comparison table above
- Consider your team setup and requirements
- Check IDE-specific capabilities

**3. Follow Specific Setup Guide**:
- Each IDE has detailed setup instructions
- Copy framework files to appropriate locations
- Configure IDE-specific settings

**4. Test Framework Operation**:
- Verify framework files are recognized
- Test conditional loading (multi-file IDEs)
- Confirm navigation hub functionality

### Framework Files Explanation

**Core Framework Components**:
- **user-rules-template**: Main navigation hub and decision matrix
- **epic-workflow-instructions**: Project hierarchy and task management
- **problem-solving-framework**: Systematic troubleshooting methodology
- **architecture-design-process**: System design and component architecture
- **architecture-lifecycle**: Documentation management and organization
- **general-execution-standards**: Quality protocols and execution guidelines

**IDE-Specific Adaptations**:
- File formats adapted to IDE requirements (.mdc, .md, .rules, etc.)
- Content structure optimized for IDE parsing
- Navigation systems matching IDE capabilities
- Integration patterns for IDE-specific features

## 🎯 Detailed Setup Guides

### Premium/Commercial IDEs

#### [Cursor AI Setup](cursor.md)
**Features**: Advanced `.mdc` files with YAML frontmatter, intelligent context loading  
**Best For**: Individual developers seeking maximum AI efficiency  
**Setup Time**: ~15 minutes  
**Key Benefits**: Token optimization, conditional loading, sophisticated rule hierarchy

#### [GitHub Copilot Setup](github-copilot.md)
**Features**: Repository-level instructions, team-wide consistency  
**Best For**: Teams wanting shared AI assistance patterns  
**Setup Time**: ~5 minutes  
**Key Benefits**: Automatic team deployment, version-controlled framework, repository scope

#### [Windsurf Setup](windsurf.md)
**Features**: `.windsurfrules` with character limits, Codeium integration  
**Best For**: Users of Codeium's AI platform  
**Setup Time**: ~10 minutes  
**Key Benefits**: Direct Codeium integration, streamlined rule management

#### [Zencoder Setup](zencoder.md)
**Features**: Multiple rule formats, enterprise features  
**Best For**: Enterprise teams with complex requirements  
**Setup Time**: ~20 minutes  
**Key Benefits**: Format flexibility, enterprise support, advanced customization

### VS Code Extensions

#### [Cline Setup](cline.md)
**Features**: `.clinerules` files with MCP integration  
**Best For**: VS Code users wanting advanced AI assistance  
**Setup Time**: ~10 minutes  
**Key Benefits**: MCP support, VS Code integration, comprehensive documentation

#### [Roo Code Setup](roo-code.md)
**Features**: Custom instructions with `.rooignore` support  
**Best For**: VS Code users seeking lightweight AI integration  
**Setup Time**: ~5 minutes  
**Key Benefits**: Simple setup, VS Code native, good community

#### [Kilo Code Setup](kilo-code.md)
**Features**: Open source VS Code extension with custom rules  
**Best For**: Open source advocates, customizable workflows  
**Setup Time**: ~10 minutes  
**Key Benefits**: Open source, VS Code integration, customizable

### CLI and Terminal Tools

#### [Claude Code Setup](claude-code.md)
**Features**: Anthropic's official agentic coding tool  
**Best For**: Terminal-based development workflows  
**Setup Time**: ~15 minutes  
**Key Benefits**: Official Anthropic support, terminal integration, agentic capabilities

#### [Gemini CLI Setup](gemini-cli.md)
**Features**: Google's official CLI tool with `GEMINI.md` format  
**Best For**: Google ecosystem users, CLI workflows  
**Setup Time**: ~10 minutes  
**Key Benefits**: Official Google support, CLI integration, ecosystem compatibility

### Independent IDEs

#### [Void IDE Setup](void-ide.md)
**Features**: Open source Cursor alternative with privacy focus  
**Best For**: Privacy-conscious developers, open source workflows  
**Setup Time**: ~15 minutes  
**Key Benefits**: Privacy-focused, open source, Cursor-like features

#### [Trae Setup](trae.md)
**Features**: IDE-agnostic AI assistance with configuration files  
**Best For**: Multi-IDE workflows, flexible development setups  
**Setup Time**: ~10 minutes  
**Key Benefits**: IDE flexibility, configuration-driven, broad compatibility

## 🔧 Common Setup Issues

### Universal Troubleshooting

**Framework Files Not Recognized**:
```
Solution Steps:
1. Verify file extensions match IDE requirements
2. Check file placement in correct directories
3. Restart IDE after copying files
4. Verify IDE-specific configuration settings
```

**Decision Matrix Not Working**:
```
Problem: Components not loading conditionally
Solution:
1. Check navigation hub file is set as primary rule
2. Verify decision matrix syntax in main file
3. Test with explicit component references
4. Check IDE supports conditional loading
```

**Token/Context Issues**:
```
Problem: Framework consuming too much context
Solution:
1. Use progressive loading (start minimal)
2. Check IDE token limits and optimization
3. Consider single-file IDE adaptation instead
4. Customize component content for brevity
```

### IDE-Specific Issues

**File Format Problems**:
- **Cursor**: Ensure `.mdc` files have proper YAML frontmatter
- **GitHub Copilot**: Verify `.github` directory is in repository root
- **Windsurf**: Check content fits within 6K character limit
- **VS Code Extensions**: Confirm extension recognizes custom rule files

## 📊 Feature Comparison Matrix

| Feature | Cursor | GitHub Copilot | Windsurf | Cline | Roo Code | Others |
|---------|--------|----------------|----------|-------|----------|---------|
| **Conditional Loading** | ✅ Advanced | ❌ Reference-based | ❌ Single file | ✅ Basic | ✅ Basic | Varies |
| **Team Sharing** | ❌ Individual | ✅ Automatic | ✅ Project-based | ✅ Project-based | ✅ Project-based | Varies |
| **Token Optimization** | ✅ Advanced | ✅ Built-in | ❌ Limited | ✅ Good | ✅ Good | Varies |
| **Custom Components** | ✅ Easy | ✅ Easy | ❌ Limited | ✅ Easy | ✅ Easy | Varies |
| **Version Control** | ✅ Yes | ✅ Automatic | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Yes |

## 🎓 Next Steps

### Getting Started
1. **Choose your IDE** from the comparison table
2. **Follow the specific setup guide** for detailed instructions
3. **Test the framework** with a simple query
4. **Customize as needed** using the [Customization Guide](../customization-guide.md)

### Advanced Usage
- **Multi-IDE Setup**: Use different adaptations for different projects
- **Team Coordination**: Establish shared IDE choices and configurations
- **Custom Components**: Add organization-specific framework extensions
- **Integration**: Connect with existing development workflows

### Support Resources
- **[Framework Overview](../framework-overview.md)**: Complete framework understanding
- **[Epic Workflow Guide](../epic-workflow-guide.md)**: Detailed workflow implementation
- **[Customization Guide](../customization-guide.md)**: Adapting for your needs
- **[Problem Solving Guide](../problem-solving-guide.md)**: Troubleshooting methodology

---

**Ready to transform your AI-assisted development?** Choose your IDE and follow the setup guide to get started with the AI Epic Framework. 