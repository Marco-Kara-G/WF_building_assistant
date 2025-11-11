# Warframe Build Assistant - Documentation Library

**Welcome to the project documentation!**

This directory contains comprehensive documentation organized hierarchically.

---

## 📚 Documentation Structure

```
docs/
├── README.md                    # This file - Navigation guide
├── 00_PROJECT_OVERVIEW.md       # Project overview and status
├── 01_ARCHITECTURE.md           # System architecture with diagrams
├── 02_TECHNOLOGY_STACK.md       # Technology details
├── 01_database/                 # Database module
│   ├── design_database.md       # Database design
│   ├── entity_relations.md      # Entity relationships
│   └── entity_relations.svg     # ER diagram
└── 02_modules/                  # Application modules
    ├── data_loading/            # Data loading documentation
    ├── api_rest/                # REST API documentation
    └── build_management/        # Build management documentation
```

---

## 🎯 Quick Navigation

### Level 0: Project Foundation
Start here for project overview:
- **[Project Overview](00_PROJECT_OVERVIEW.md)** - Purpose, status, structure
- **[Architecture](01_ARCHITECTURE.md)** - System design, flows, patterns
- **[Technology Stack](02_TECHNOLOGY_STACK.md)** - Technologies and tools

### Level 1: Core Modules
Deep dive into specific areas:
- **[Database](01_database/)** - Schema, models, migrations
- **[Modules](02_modules/)** - Application modules documentation

---

## 📖 Reading Guide

### For New Developers
1. Start with `00_PROJECT_OVERVIEW.md`
2. Read `01_ARCHITECTURE.md` for system understanding
3. Review `01_database/design_database.md` for data model
4. Explore specific modules in `02_modules/`

### For Contributors
1. Check `00_PROJECT_OVERVIEW.md` for current status
2. Review relevant module documentation in `02_modules/`
3. Follow architecture patterns in `01_ARCHITECTURE.md`

### For Architects
1. Review `01_ARCHITECTURE.md` for design decisions
2. Check `02_TECHNOLOGY_STACK.md` for technology choices
3. Examine `01_database/` for data architecture

---

## 📝 Documentation Standards

### File Naming
- Level 0: `NN_TITLE.md` (e.g., `00_PROJECT_OVERVIEW.md`)
- Modules: `module_name/` directories
- Lowercase with underscores for subdirectories

### Content Structure
Each document should include:
- Title and metadata (version, date)
- Clear sections with headers
- Code examples where relevant
- Diagrams (Mermaid preferred)
- Cross-references to related docs

### Mermaid Diagrams
Use Mermaid for:
- Architecture diagrams
- Sequence diagrams
- Flow charts
- ER diagrams

---

## 🔄 Documentation Workflow

### When to Update
- New feature implementation
- Architecture changes
- Technology updates
- Bug fixes affecting design

### How to Update
1. Identify affected documents
2. Update content
3. Update version/date
4. Cross-check related docs
5. Commit with descriptive message

---

## 📂 Module Documentation Template

When creating new module documentation:

```markdown
# Module Name

**Version**: 1.0
**Status**: [Planning/In Progress/Complete]
**Last Updated**: YYYY-MM-DD

## Purpose
Brief description of module purpose

## Architecture
Module-specific architecture details

## Components
List of components with descriptions

## Data Flow
Sequence diagrams or flow descriptions

## API Reference
Public interfaces and methods

## Examples
Usage examples

## Testing
Testing strategy and examples
```

---

## 🎨 Diagram Guidelines

### Architecture Diagrams
- Use consistent colors for layer types
- Show data flow direction
- Include all major components
- Keep it high-level

### Sequence Diagrams
- Show complete interaction flow
- Include error paths
- Label each step clearly
- Use consistent participant names

### ER Diagrams
- Show all relationships
- Include cardinality
- Mark primary/foreign keys
- Use standard notation

---

## 🔗 External Resources

### Project Links
- **Repository**: [GitHub URL]
- **Issue Tracker**: [GitHub Issues]
- **Wiki**: [GitHub Wiki]

### Technology Documentation
- [Python 3.13](https://docs.python.org/3.13/)
- [SQLAlchemy 2.0](https://docs.sqlalchemy.org/en/20/)
- [Pydantic 2.0](https://docs.pydantic.dev/2.0/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Alembic](https://alembic.sqlalchemy.org/)

---

## 📊 Documentation Status

| Document | Status | Last Updated |
|----------|--------|--------------|
| 00_PROJECT_OVERVIEW.md | ✅ Complete | 2025-01 |
| 01_ARCHITECTURE.md | ✅ Complete | 2025-01 |
| 02_TECHNOLOGY_STACK.md | ✅ Complete | 2025-01 |
| 01_database/ | ✅ Complete | 2024-12 |
| 02_modules/data_loading/ | 📋 Planned | - |
| 02_modules/api_rest/ | 📋 Planned | - |
| 02_modules/build_management/ | 📋 Planned | - |

---

## 🤝 Contributing to Documentation

### Guidelines
1. Keep documentation in sync with code
2. Use clear, concise language
3. Include examples
4. Update cross-references
5. Follow naming conventions

### Review Process
1. Self-review for clarity
2. Check all links work
3. Verify diagrams render correctly
4. Ensure consistency with existing docs

---

## 📞 Support

For questions about documentation:
- Open an issue on GitHub
- Contact project maintainers
- Check existing documentation first

---

**Last Updated**: January 2025  
**Maintained By**: Project Team
