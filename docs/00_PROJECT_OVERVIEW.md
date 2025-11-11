# Warframe Build Assistant - Project Overview

**Version**: 0.3.0  
**Last Updated**: January 2025  
**Status**: In Development

---

## Project Purpose

Backend modulare per la creazione e gestione di build personalizzate per Warframe con:
- Gestione dati di gioco (Warframe, Armi, Mod, Companion)
- Sistema CRUD completo
- API REST per integrazione frontend
- Sistema di gestione build personalizzate

---

## Technology Stack

### Core
- **Python 3.13+** - Linguaggio principale
- **uv** - Package manager e gestione ambiente virtuale
- **FastAPI** - Framework API REST
- **SQLAlchemy 2.0** - ORM per database
- **Pydantic 2.0** - Validazione dati e schema
- **MySQL 8.0** - Database relazionale
- **Alembic** - Gestione migrazioni database

### Development
- **pytest** - Testing framework
- **Docker** - Containerizzazione (futuro)

---

## Project Structure

```
Warframe_Build_Assistant/
├── docs/                       # Documentazione progetto
│   ├── 00_PROJECT_OVERVIEW.md  # Questo file
│   ├── 01_ARCHITECTURE.md      # Architettura completa
│   ├── 02_TECHNOLOGY_STACK.md  # Dettagli stack tecnologico
│   ├── 01_database/            # Modulo Database
│   └── 02_modules/             # Moduli applicativi
│       ├── data_loading/
│       ├── api_rest/
│       └── build_management/
├── migrations/                 # Migrazioni Alembic
├── scripts/                    # Script utility
├── src/                        # Codice sorgente
│   ├── api/                    # Endpoint REST
│   ├── database/               # Layer database
│   │   ├── models/             # SQLAlchemy models
│   │   ├── dao/                # Data Access Objects
│   │   ├── db_config/          # Configurazione DB
│   │   └── db_connection/      # Gestione connessioni
│   ├── dto/                    # Data Transfer Objects
│   ├── services/               # Business logic
│   ├── decorators/             # Decoratori utility
│   └── utils/                  # Funzioni utility
└── tests/                      # Test suite
```

---

## Current Implementation Status

### ✅ Completed Components
- Database Models (12 entities)
- Database Migrations (Alembic)
- DTOs (8 entities)
- Decorators (logging, exception handling)
- DB Configuration
- DB Connection Management
- DAO Layer (partial)

### 🔄 In Progress
- Service Layer
- Data Loading Scripts
- API REST Endpoints

### 📋 Planned
- Build Management System
- Testing Suite
- Docker Configuration
- CI/CD Pipeline

---

## Core Modules

### 1. Database Layer
**Path**: `src/database/`  
**Documentation**: `docs/01_database/`

Gestione completa del layer database con:
- 12 modelli SQLAlchemy
- Sistema migrazioni Alembic
- DAO pattern per CRUD operations
- Connection pooling

### 2. Data Loading
**Path**: `src/services/`, `scripts/`  
**Documentation**: `docs/02_modules/data_loading/`

Sistema di caricamento dati da API esterne:
- Fetch da API Warframe
- Validazione con DTOs
- Trasformazione e persistenza
- Update automatico dati esistenti

### 3. API REST
**Path**: `src/api/`  
**Documentation**: `docs/02_modules/api_rest/`

Endpoint REST per operazioni CRUD:
- GET /warframes, /weapons, /mods
- POST /builds
- PUT /builds/{id}
- DELETE /builds/{id}

### 4. Build Management
**Path**: `src/services/build_service.py`  
**Documentation**: `docs/02_modules/build_management/`

Sistema gestione build personalizzate:
- Creazione build
- Validazione configurazioni
- Calcolo statistiche
- Esportazione/Importazione

---

## Data Flow Overview

```
External API → DTO → Service → DAO → Database
                                      ↓
                              API REST ← Client
```

---

## Development Workflow

### Setup Environment
```bash
uv venv
.venv\Scripts\activate
uv pip install -e .
```

### Database Migrations
```bash
alembic revision --autogenerate -m "description"
alembic upgrade head
```

### Run Data Loading
```bash
python scripts/load_warframes.py
```

### Run API Server
```bash
uvicorn src.api.main:app --reload
```

---

## Documentation Navigation

- **Architecture**: `01_ARCHITECTURE.md` - Diagrammi e flussi completi
- **Technology Stack**: `02_TECHNOLOGY_STACK.md` - Dettagli tecnologie
- **Database**: `01_database/` - Design e schema database
- **Modules**: `02_modules/` - Documentazione per modulo

---

## Contributing Guidelines

1. Seguire architettura layered esistente
2. Usare decoratori per logging/error handling
3. Validare input con Pydantic
4. Scrivere test per nuove feature
5. Documentare modifiche architetturali

---

## Roadmap

### Phase 1: Foundation (Current)
- ✅ Database setup
- ✅ DTOs implementation
- 🔄 DAO layer
- 🔄 Service layer

### Phase 2: Data Loading
- Data fetching from API
- Transformation pipeline
- Database population

### Phase 3: API REST
- CRUD endpoints
- Request validation
- Response formatting

### Phase 4: Build Management
- Build creation
- Statistics calculation
- Export/Import

### Phase 5: Production
- Docker deployment
- CI/CD pipeline
- Monitoring

---

## Contact & Support

**Repository**: [GitHub Link]  
**Documentation**: `docs/`  
**Issues**: [GitHub Issues]
