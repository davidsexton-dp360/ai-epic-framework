# AI Epic Framework

A systematic approach to complex application development through AI assistance. This framework provides structured methodologies for epic workflow management, problem solving, architecture design, and execution standards.

## 📄 License

This framework is licensed under the MIT License - see the [LICENSE](../LICENSE) file for details.

**MIT License Summary:**
- ✅ **Commercial use allowed** - Use in any project, including commercial applications
- ✅ **Modification permitted** - Adapt the framework to your specific needs
- ✅ **Distribution allowed** - Share modified versions with your team or community
- ✅ **Attribution required** - Include license and copyright notice in distributions

## 🏗️ Framework Structure

```
framework/
├── generic/                    # Source templates
├── [ide]-specific/            # Adapted versions
│   ├── user-rules-template.*  # Main rule (always applied)
│   ├── epic-workflow-*        # Context: workflow management
│   ├── problem-solving-*      # Context: systematic debugging
│   ├── architecture-*         # Context: design & lifecycle
│   └── general-execution-*    # Context: standards & tools
```

## 📱 IDE Support

### Multi-File IDEs (Supports Context Loading)
- **Cursor AI**: `.mdc` files, separate context files
- **Claude Code**: `CLAUDE.md` + context files  
- **Zed**: `.rules` + context files
- **Void IDE**: `.cursorrules` + context files

### Single-File IDEs (Combined/Optimized)
- **Windsurf**: `.windsurfrules` (6K limit) + reference docs
- **GitHub Copilot**: `.github/copilot-instructions.md` + reference

### Generic Support
- **Others**: Main rule + context files with compatibility formats

## 🚀 Usage

### For Multi-File IDEs:
1. Copy main rule file to project root
2. Copy context files to docs/ or keep in root
3. Main rule contains decision matrix for loading context

### For Single-File IDEs:
1. Copy main rule file to specified location
2. Reference context files as separate documentation
3. Load context manually when needed

## 🔧 Customization

Edit `framework/generic/` files and regenerate:
```bash
python3 create_ide_adaptations.py
```

## 💡 Benefits

- **Smart Loading**: Only load context when needed
- **Token Efficient**: Preserves context window space  
- **Scalable**: Works from simple to complex projects
- **Consistent**: Same patterns across all IDEs
