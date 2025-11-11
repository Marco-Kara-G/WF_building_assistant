# Technology Stack - Detailed Specification

**Version**: 1.0  
**Last Updated**: January 2025

---

## Core Technologies

### Python 3.13+
**Role**: Primary programming language  
**Why**: Modern features, strong typing, excellent ecosystem

**Key Features Used**:
- Type hints (PEP 484)
- Dataclasses
- Async/await (future)
- Pattern matching (future)

---

### uv
**Role**: Package manager and virtual environment  
**Why**: Faster than pip, better dependency resolution

**Usage**:
```bash
uv venv                    # Create virtual environment
uv pip install -e .        # Install project in editable mode
uv pip install requests    # Install package
```

**Configuration**: `pyproject.toml`

---

## Web Framework

### FastAPI (Future)
**Role**: REST API framework  
**Why**: Fast, automatic documentation, type validation

**Features**:
- Automatic OpenAPI/Swagger docs
- Pydantic integration
- Async support
- Dependency injection

**Example**:
```python
@app.get("/warframes", response_model=List[WarframeDTO])
async def get_warframes():
    return service.get_all()
```

---

## Database Stack

### MySQL 8.0
**Role**: Relational database  
**Why**: Reliable, performant, widely supported

**Configuration**:
```env
DB_HOST=localhost
DB_PORT=3306
DB_NAME=wfa_database
DB_USER=wfa_user
DB_PASSWORD=wfa_password
```

**Features Used**:
- JSON column type
- DECIMAL for precision
- Foreign keys
- Indexes

---

### SQLAlchemy 2.0
**Role**: ORM (Object-Relational Mapping)  
**Why**: Pythonic, powerful, type-safe

**Key Features**:
- Mapped columns with type hints
- Relationship management
- Query builder
- Connection pooling

**Example**:
```python
class Warframe(Base):
    __tablename__ = "warframes"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
```

**Dependencies**:
```toml
sqlalchemy = ">=2.0.44"
pymysql = ">=1.1.2"  # MySQL driver
```

---

### Alembic
**Role**: Database migration tool  
**Why**: Version control for database schema

**Workflow**:
```bash
# Create migration
alembic revision --autogenerate -m "add warframes table"

# Apply migration
alembic upgrade head

# Rollback
alembic downgrade -1
```

**Configuration**: `alembic.ini`

---

## Data Validation

### Pydantic 2.0
**Role**: Data validation and serialization  
**Why**: Type-safe, automatic validation, JSON schema

**Features**:
- Automatic type coercion
- Custom validators
- JSON serialization
- Field constraints

**Example**:
```python
class WarframeDTO(BaseModel):
    name: str
    health: float = Field(gt=0)  # Must be > 0
    description: Optional[str] = None
```

**Validation**:
```python
# Automatic validation on instantiation
dto = WarframeDTO(**api_data)  # Raises ValidationError if invalid
```

---

## Environment Management

### python-dotenv
**Role**: Environment variable management  
**Why**: Secure configuration, environment separation

**Usage**:
```python
from dotenv import load_dotenv
import os

load_dotenv()
db_host = os.getenv("DB_HOST")
```

**File**: `.env` (gitignored)

---

## HTTP Client

### requests
**Role**: HTTP library for API calls  
**Why**: Simple, reliable, widely used

**Features Used**:
- GET requests
- Timeout handling
- Status code validation
- JSON parsing

**Example**:
```python
response = requests.get(url, timeout=10)
response.raise_for_status()
data = response.json()
```

---

## Development Tools

### pytest (Future)
**Role**: Testing framework  
**Why**: Simple, powerful, extensive plugin ecosystem

**Planned Usage**:
```python
def test_warframe_service():
    mock_dao = Mock(WarframeDAO)
    service = WarframeService(mock_dao)
    result = service.load_from_dto(test_dto)
    assert result.name == "Excalibur"
```

---

### Docker (Future)
**Role**: Containerization  
**Why**: Consistent environments, easy deployment

**Planned Services**:
- MySQL container
- Application container
- Redis container (caching)

**Configuration**: `docker-compose.yml`

---

## Project Configuration

### pyproject.toml
**Role**: Project metadata and dependencies  
**Format**: TOML

**Current Configuration**:
```toml
[project]
name = "warframe-build-assistant"
version = "0.3.0"
requires-python = ">=3.13"

dependencies = [
    "alembic>=1.17.0",
    "pydantic>=2.12.3",
    "pymysql>=1.1.2",
    "requests>=2.32.5",
    "sqlalchemy>=2.0.44",
    "python-dotenv>=1.0.0",
]
```

---

## Dependency Tree

```
warframe-build-assistant
├── alembic (migrations)
│   └── sqlalchemy
├── fastapi (future)
│   ├── pydantic
│   └── starlette
├── sqlalchemy (ORM)
│   └── pymysql (MySQL driver)
├── pydantic (validation)
├── requests (HTTP client)
└── python-dotenv (env vars)
```

---

## Version Requirements

| Package | Version | Reason |
|---------|---------|--------|
| Python | >=3.13 | Modern features, type hints |
| SQLAlchemy | >=2.0.44 | Mapped columns, type safety |
| Pydantic | >=2.12.3 | Performance, validation |
| Alembic | >=1.17.0 | Latest migration features |
| PyMySQL | >=1.1.2 | MySQL 8.0 compatibility |
| Requests | >=2.32.5 | Security updates |

---

## Database Driver Choice

### Why PyMySQL?
- ✅ Pure Python (no C dependencies)
- ✅ Easy installation
- ✅ MySQL 8.0 compatible
- ✅ Works with SQLAlchemy

**Alternative**: `mysqlclient` (faster but requires C compiler)

**Connection String**:
```python
f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
```

---

## External APIs

### api.warframestat.us
**Role**: Source of game data  
**Why**: Real-time, comprehensive, free

**Endpoints Used**:
- `/warframes/` - All warframes data
- `/weapons/` - Weapons data (future)
- `/mods/` - Mods data (future)

**Response Format**: JSON array

**Example Response**:
```json
[
  {
    "name": "Ash",
    "uniqueName": "/Lotus/Powersuits/Ninja/Ninja",
    "health": 455,
    "shield": 270,
    "armor": 105,
    "power": 100,
    "abilities": [...]
  }
]
```

---

## Logging Strategy

### Python logging module
**Role**: Application logging  
**Why**: Built-in, flexible, standard

**Configuration**:
```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
```

**Usage via Decorators**:
```python
@handle_logger  # Automatic logging
def my_function():
    pass
```

**Log Levels**:
- `INFO`: Function entry/exit
- `ERROR`: Exceptions and errors
- `DEBUG`: Detailed debugging (future)

---

## Future Technologies

### Redis (Planned)
**Role**: Caching layer  
**Why**: Fast, in-memory, pub/sub support

**Use Cases**:
- Cache API responses
- Session storage
- Real-time updates

---

### Celery (Planned)
**Role**: Background task queue  
**Why**: Async processing, scheduled tasks

**Use Cases**:
- Periodic data updates
- Heavy computations
- Email notifications

---

### Prometheus + Grafana (Planned)
**Role**: Monitoring and metrics  
**Why**: Industry standard, powerful

**Metrics to Track**:
- Request latency
- Error rates
- Database query time
- API call success rate

---

## Development Environment

### Required Tools
- Python 3.13+
- MySQL 8.0
- uv package manager
- Git

### Optional Tools
- Docker Desktop
- MySQL Workbench
- Postman (API testing)
- VS Code with Python extension

---

## Production Considerations

### Performance
- Connection pooling (SQLAlchemy)
- Query optimization
- Caching strategy (Redis)
- Async operations (FastAPI)

### Security
- Environment variables for secrets
- SQL injection prevention (ORM)
- Input validation (Pydantic)
- HTTPS only (production)

### Scalability
- Horizontal scaling (Docker)
- Load balancing (Nginx)
- Database replication
- CDN for static assets

---

## Technology Decision Log

### Why SQLAlchemy over raw SQL?
- Type safety
- Automatic migrations
- Relationship management
- Query builder

### Why Pydantic over dataclasses?
- Automatic validation
- JSON serialization
- API integration
- Schema generation

### Why FastAPI over Flask?
- Async support
- Automatic docs
- Type validation
- Modern features

### Why MySQL over PostgreSQL?
- Team familiarity
- Simpler setup
- Good enough for use case
- Wide hosting support
