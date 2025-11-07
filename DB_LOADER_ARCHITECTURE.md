# 🏗️ Architettura DB Loader - Design Document

**Obiettivo**: Caricare dati da API esterna nel database MySQL

---

## 🎯 Pattern Architetturale

### Opzione 1: Layered Architecture (Raccomandato per questo progetto)
```
API External → DTO → Service → DAO → Database
```

### Opzione 2: Clean Architecture (Overkill per questo caso)
```
API → Use Cases → Entities → Repositories → Database
```

**Scelta**: **Layered Architecture** - Più semplice, adatto per CRUD operations

---

## 📦 Componenti Necessari

### 1. DTO (Data Transfer Object)
**Scopo**: Rappresentare dati API in formato type-safe  
**Posizione**: `src/dto/`

```python
# src/dto/warframe_dto.py
from pydantic import BaseModel
from typing import List, Optional

class AbilityDTO(BaseModel):
    name: str
    description: str
    uniqueName: str
    imageName: Optional[str] = None

class WarframeDTO(BaseModel):
    name: str
    uniqueName: str
    health: int
    shield: int
    armor: int
    power: int
    abilities: List[AbilityDTO]
    polarities: List[str]
    # ... altri campi
```

**Pro**:
- ✅ Validazione automatica con Pydantic
- ✅ Type hints per IDE
- ✅ Separazione tra API e DB

**Contro**:
- ⚠️ Duplicazione con DB models (ma necessaria)

---

### 2. DAO (Data Access Object)
**Scopo**: Gestire operazioni CRUD sul database  
**Posizione**: `src/database/dao/`

```python
# src/database/dao/warframe_dao.py
from sqlalchemy.orm import Session
from src.database.models.warframe_db_model import Warframe
from typing import Optional, List

class WarframeDAO:
    def __init__(self, session: Session):
        self.session = session
    
    def create(self, warframe: Warframe) -> Warframe:
        self.session.add(warframe)
        self.session.commit()
        self.session.refresh(warframe)
        return warframe
    
    def get_by_name(self, name: str) -> Optional[Warframe]:
        return self.session.query(Warframe).filter(Warframe.name == name).first()
    
    def get_all(self) -> List[Warframe]:
        return self.session.query(Warframe).all()
    
    def exists(self, name: str) -> bool:
        return self.session.query(Warframe).filter(Warframe.name == name).count() > 0
```

**Pro**:
- ✅ Incapsula logica SQL
- ✅ Riutilizzabile
- ✅ Testabile

---

### 3. Service
**Scopo**: Business logic + orchestrazione  
**Posizione**: `src/services/`

```python
# src/services/warframe_service.py
from typing import List
from src.dto.warframe_dto import WarframeDTO
from src.database.dao.warframe_dao import WarframeDAO
from src.database.models.warframe_db_model import Warframe
from src.decorators.logger import handle_logger
from src.decorators.exception import handle_exception

class WarframeService:
    def __init__(self, dao: WarframeDAO):
        self.dao = dao
    
    @handle_logger
    @handle_exception
    def load_from_dto(self, dto: WarframeDTO) -> Warframe:
        """
        Carica un warframe da DTO a DB.
        Se esiste già, lo aggiorna.
        """
        # Check se esiste
        existing = self.dao.get_by_name(dto.name)
        if existing:
            # Update logic
            return self._update_warframe(existing, dto)
        
        # Create new
        warframe = self._dto_to_model(dto)
        return self.dao.create(warframe)
    
    def _dto_to_model(self, dto: WarframeDTO) -> Warframe:
        """Converte DTO in DB Model"""
        return Warframe(
            name=dto.name,
            unique_name=dto.uniqueName,
            health=dto.health,
            shield=dto.shield,
            armor=dto.armor,
            power=dto.power,
            # ... mapping campi
        )
    
    def _update_warframe(self, model: Warframe, dto: WarframeDTO) -> Warframe:
        """Aggiorna model esistente con dati DTO"""
        model.health = dto.health
        model.shield = dto.shield
        # ... update altri campi
        self.dao.session.commit()
        return model
```

**Pro**:
- ✅ Logica business centralizzata
- ✅ Gestisce update/create
- ✅ Usa decoratori per logging

---

### 4. Controller (Loader Script)
**Scopo**: Orchestrare il flusso completo  
**Posizione**: `scripts/`

```python
# scripts/load_warframes.py
from src.database.db_connection.db_connection import DBconnection
from src.database.dao.warframe_dao import WarframeDAO
from src.services.warframe_service import WarframeService
from src.database.db_fetcher.fetch_entity_data.fetch_entity_data import fetch_entity_data
from src.dto.warframe_dto import WarframeDTO

def load_warframes():
    # 1. Fetch da API
    raw_data = fetch_entity_data("warframes")
    
    # 2. Converti in DTO
    dtos = [WarframeDTO(**item) for item in raw_data]
    
    # 3. Setup DB
    db = DBconnection()
    session = db.get_session()
    
    try:
        # 4. Setup DAO e Service
        dao = WarframeDAO(session)
        service = WarframeService(dao)
        
        # 5. Load nel DB
        loaded = 0
        for dto in dtos:
            service.load_from_dto(dto)
            loaded += 1
            print(f"✅ Loaded: {dto.name} ({loaded}/{len(dtos)})")
        
        print(f"\n🎉 Caricati {loaded} warframes!")
        
    finally:
        session.close()

if __name__ == "__main__":
    load_warframes()
```

---

## 🤔 Serve Controller separato?

### NO - Controller non serve
**Motivo**: Il loader script È già il controller

**Struttura Semplificata**:
```
scripts/load_warframes.py  ← Controller (orchestrazione)
    ↓
src/services/warframe_service.py  ← Business logic
    ↓
src/database/dao/warframe_dao.py  ← Data access
    ↓
Database
```

---

## 📊 Struttura Directory Proposta

```
src/
├── dto/                        # ✅ NUOVO
│   ├── __init__.py
│   ├── warframe_dto.py
│   ├── weapon_dto.py
│   └── mod_dto.py
├── database/
│   ├── dao/                    # ✅ NUOVO
│   │   ├── __init__.py
│   │   ├── warframe_dao.py
│   │   ├── weapon_dao.py
│   │   └── mod_dao.py
│   ├── models/                 # ✅ Già esistente
│   ├── db_connection/          # ✅ Già esistente
│   └── db_config/              # ✅ Già esistente
├── services/                   # ✅ NUOVO
│   ├── __init__.py
│   ├── warframe_service.py
│   ├── weapon_service.py
│   └── mod_service.py
└── database/db_fetcher/        # ✅ Già esistente (rinominare in external_api?)

scripts/                        # ✅ NUOVO contenuto
├── load_warframes.py
├── load_weapons.py
└── load_all.py
```

---

## 🎯 Componenti Necessari - Riepilogo

| Componente | Necessario? | Motivo |
|------------|-------------|--------|
| **DTO** | ✅ SÌ | Validazione + type safety |
| **DAO** | ✅ SÌ | Incapsula SQL, riutilizzabile |
| **Service** | ✅ SÌ | Business logic (update/create) |
| **Controller** | ❌ NO | Script loader è già controller |

---

## 🔄 Flusso Dati Completo

```
1. API External
   ↓ (fetch_entity_data)
2. Raw JSON
   ↓ (WarframeDTO(**json))
3. DTO (validated)
   ↓ (service.load_from_dto)
4. Service (business logic)
   ↓ (dao.create/update)
5. DAO (SQL operations)
   ↓ (session.add/commit)
6. Database
```

---

## 💡 Vantaggi Architettura

### Separazione Responsabilità
- **DTO**: Validazione dati esterni
- **Service**: Logica business (update vs create)
- **DAO**: Operazioni database
- **Script**: Orchestrazione

### Testabilità
```python
# Test Service senza DB
mock_dao = Mock(WarframeDAO)
service = WarframeService(mock_dao)
service.load_from_dto(test_dto)
```

### Riutilizzabilità
```python
# Stesso DAO per API REST future
@app.get("/warframes")
def get_warframes():
    dao = WarframeDAO(session)
    return dao.get_all()
```

---

## 🚀 Piano Implementazione

### Step 1: DTO (1-2 ore)
- [ ] Creare `src/dto/warframe_dto.py`
- [ ] Mappare tutti i campi API
- [ ] Testare validazione Pydantic

### Step 2: DAO (1 ora)
- [ ] Creare `src/database/dao/warframe_dao.py`
- [ ] Implementare CRUD base
- [ ] Testare con DB

### Step 3: Service (1-2 ore)
- [ ] Creare `src/services/warframe_service.py`
- [ ] Implementare logica update/create
- [ ] Gestire relazioni (abilities)

### Step 4: Loader Script (30 min)
- [ ] Creare `scripts/load_warframes.py`
- [ ] Orchestrare flusso completo
- [ ] Testare caricamento

**Tempo Totale Stimato**: 4-5 ore

---

## 📝 Esempio Completo Minimale

### DTO
```python
class WarframeDTO(BaseModel):
    name: str
    health: int
    shield: int
```

### DAO
```python
class WarframeDAO:
    def create(self, warframe: Warframe) -> Warframe:
        self.session.add(warframe)
        self.session.commit()
        return warframe
```

### Service
```python
class WarframeService:
    def load_from_dto(self, dto: WarframeDTO) -> Warframe:
        warframe = Warframe(name=dto.name, health=dto.health, shield=dto.shield)
        return self.dao.create(warframe)
```

### Script
```python
def load_warframes():
    raw_data = fetch_entity_data("warframes")
    dtos = [WarframeDTO(**item) for item in raw_data]
    
    db = DBconnection()
    session = db.get_session()
    dao = WarframeDAO(session)
    service = WarframeService(dao)
    
    for dto in dtos:
        service.load_from_dto(dto)
```

---

## ✅ Conclusioni

**Componenti Necessari**:
1. ✅ **DTO** - Validazione dati API
2. ✅ **DAO** - Operazioni database
3. ✅ **Service** - Business logic
4. ❌ **Controller** - Script loader è sufficiente

**Architettura**: Layered (semplice ed efficace)

**Prossimo Step**: Implementare DTO per Warframe
