# 🧠 Warframe Build Assistant

Backend modulare per la creazione e gestione di build personalizzate per Warframe.

**Version**: 0.3.0  
**Status**: In Development  
**Python**: 3.13+

---

## 📋 Quick Links

- **[📚 Full Documentation](docs/README.md)** - Complete documentation library
- **[🏗️ Architecture](docs/01_ARCHITECTURE.md)** - System design and flows
- **[💾 Database](docs/01_database/)** - Database schema and design
- **[🔧 Technology Stack](docs/02_TECHNOLOGY_STACK.md)** - Technologies used

---

## 🎯 Project Purpose

Sistema backend completo per:
- Gestione dati di gioco (Warframe, Armi, Mod, Companion)
- Operazioni CRUD complete
- API REST per integrazione frontend
- Sistema di gestione build personalizzate

---

## 🛠️ Technology Stack

- **Python 3.13+** - Core language
- **FastAPI** - REST API framework
- **SQLAlchemy 2.0** - ORM
- **Pydantic 2.0** - Data validation
- **MySQL 8.0** - Database
- **Alembic** - Migrations
- **uv** - Package manager

---

## 🚀 Quick Start

### Prerequisites
- Python 3.13+
- MySQL 8.0
- uv package manager

### Installation

```bash
# Clone repository
git clone https://github.com/Marco-Kara-G/WF_building_assistant.git
cd WF_building_assistant

# Create virtual environment
uv venv

# Activate environment
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/Mac

# Install dependencies
uv pip install -e .
```

### Database Setup

```bash
# Configure .env file
cp .env.example .env
# Edit .env with your MySQL credentials

# Run migrations
alembic upgrade head
```

### Load Initial Data

```bash
# Load warframes data
python scripts/load_warframes.py
```

---

## 📁 Project Structure

```
Warframe_Build_Assistant/
├── docs/                       # 📚 Documentation library
│   ├── 00_PROJECT_OVERVIEW.md
│   ├── 01_ARCHITECTURE.md
│   ├── 02_TECHNOLOGY_STACK.md
│   ├── 01_database/
│   └── 02_modules/
├── migrations/                 # Database migrations
├── scripts/                    # Utility scripts
├── src/                        # Source code
│   ├── api/                    # REST API endpoints
│   ├── database/               # Database layer
│   │   ├── models/             # SQLAlchemy models
│   │   ├── dao/                # Data Access Objects
│   │   ├── db_config/          # DB configuration
│   │   └── db_connection/      # Connection management
│   ├── dto/                    # Data Transfer Objects
│   ├── services/               # Business logic
│   ├── decorators/             # Utility decorators
│   └── utils/                  # Utility functions
├── tests/                      # Test suite
├── .env                        # Environment variables
├── pyproject.toml              # Project configuration
└── README.md                   # This file
```

---

## 📊 Current Status

### ✅ Completed
- Database models (12 entities)
- Database migrations (Alembic)
- DTOs (8 entities)
- Decorators (logging, exceptions)
- DB configuration
- DB connection management

### 🔄 In Progress
- DAO layer
- Service layer
- Data loading scripts

### 📋 Planned
- REST API endpoints
- Build management system
- Testing suite
- Docker deployment

---

## 🏗️ Architecture Overview

```
External API → DTO → Service → DAO → Database
                                      ↓
                              REST API ← Client
```

**Layered Architecture** with clear separation:
- **Application Layer**: Scripts, REST API
- **Business Logic**: Services
- **Data Access**: DTOs, DAOs
- **Database**: SQLAlchemy Models, MySQL

**[Full Architecture Documentation](docs/01_ARCHITECTURE.md)**

---

## 💾 Database Entities

- **Warframe** - 14 fields
- **Primary/Secondary/Melee Weapons** - 24-30 fields
- **Mod** - 12 fields
- **Companion** - 9 fields
- **Ability** - 7 fields (linked to Warframe)
- **Build** - 11 fields (links all entities)

**[Database Design](docs/01_database/design_database.md)**

---

## 🔧 Development

### Run Migrations

```bash
# Create new migration
alembic revision --autogenerate -m "description"

# Apply migrations
alembic upgrade head

# Rollback
alembic downgrade -1
```

### Load Data

```bash
# Load specific entity
python scripts/load_warframes.py

# Load all data (future)
python scripts/load_all.py
```

### Run API Server (Future)

```bash
uvicorn src.api.main:app --reload
```

---

## 📚 Documentation

Complete documentation available in [`docs/`](docs/):

- **[Project Overview](docs/00_PROJECT_OVERVIEW.md)** - Purpose, status, roadmap
- **[Architecture](docs/01_ARCHITECTURE.md)** - System design, flows, patterns
- **[Technology Stack](docs/02_TECHNOLOGY_STACK.md)** - Technologies and tools
- **[Database](docs/01_database/)** - Schema, models, relationships
- **[Modules](docs/02_modules/)** - Module-specific documentation

---

## 🤝 Contributing

1. Read [Architecture Documentation](docs/01_ARCHITECTURE.md)
2. Follow existing patterns (Layered Architecture)
3. Use decorators for logging/error handling
4. Validate input with Pydantic
5. Write tests for new features
6. Update documentation

---

## 📝 License

TBD

---

## 🔗 Links

- **Documentation**: [`docs/`](docs/)
- **Issues**: [GitHub Issues]
- **Repository**: [GitHub]

---

**For detailed information, see the [complete documentation](docs/README.md).**
