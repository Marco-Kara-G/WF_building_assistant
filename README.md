# 🧠 Warframe Build Assistant

Un assistente backend modulare per la creazione e gestione di build personalizzate per Warframe.

## 📋 Scopo del Progetto

Creare un backend modulare che permetta di:
- Consultare, salvare e combinare dati di gioco (Warframe, armi, mod, companion)
- Creare build personalizzate
- Integrare in futuro un'IA di supporto per suggerimenti di build ottimali basati su dati aggiornati

## 🎯 Obiettivi Iniziali

- Gestire dati statici del gioco (importati da API esterne o dataset locali)
- Implementare operazioni CRUD su:
  - Warframe
  - Armi
  - Mod
  - Build
- Implementare una base solida: autenticazione, DB coerente, API ben strutturate
- Preparare un'architettura scalabile per il futuro (microservizi, IA, aggiornamenti automatici)

## 🛠️ Stack Tecnologico

- **Python** - Linguaggio base
- **uv** - Package manager e ambiente virtuale
- **FastAPI** - API REST (in futuro)
- **SQLAlchemy + Pydantic** - Gestione dati e validazione
- **MySQL** - Database principale
- **Docker** - Orchestrazione e riproducibilità (più avanti)
- **pytest** - Test automatizzati

## 📁 Struttura del Progetto

```
Warframe_Build_Assistant/
├── docs/                    → Documentazione tecnica e decisioni progettuali
│   ├── learning/           → Materiale di studio e correzioni (gitignored)
│   │   ├── issues/         → Fix per problemi specifici
│   │   └── study/          → Tutorial e best practices
│   ├── design_database.md  → Design del database
│   └── entity_relations.*  → Relazioni tra entità
├── migrations/             → Versionamento schema DB (Alembic)
├── scripts/                → Script di supporto e manutenzione
├── src/                    → Codice sorgente
│   ├── api/                → Endpoint REST
│   ├── config/             → Configurazione ambiente e variabili
│   ├── database/           → Connessione e sessione DB + modelli
│   │   ├── models/         → Modelli SQLAlchemy (Warframe, Armi, Mod, ecc.)
│   │   └── docker/         → Configurazione Docker per MySQL
│   ├── decorators/         → Decoratori per logging ed exception handling ✅
│   ├── models/             → Schema Pydantic (futuro)
│   └── utils/              → Funzioni di utilità
├── tests/                  → Test unitari e d'integrazione
├── pyproject.toml          → Configurazione uv + dipendenze
└── uv.lock                 → Lock delle versioni
```

## 🗺️ Roadmap

### ✅ Completato
1. **Definizione dominio** → Entità e relazioni definite
2. **Progettazione modello dati** → Modelli SQLAlchemy creati per tutte le entità
3. **Setup database** → Alembic configurato, migrazioni create
4. **Decoratori base** → Sistema di logging ed exception handling funzionante

### 🔄 In Corso
5. **Connessione al DB MySQL** → Schema creato, connessione da testare
6. **Popolamento dati iniziali** → Script per importare dati base

### 📋 Prossimi Step
7. **API CRUD base** → Endpoint per Warframe, Armi, Mod
8. **Implementazione autenticazione** → JWT per API
9. **Testing + documentazione API**
10. **Frontend base** → Interfaccia per testare le API

### 🚀 Futuro
11. **Aggiornamento automatico dati** → Sync con API esterne
12. **Modulo AI** → Suggerimenti build ottimali

## 📊 Stato Attuale

**Versione**: 0.2.0 (Database Design + Decoratori)

### 🎯 Componenti Funzionanti
- ✅ **Database Models**: Tutti i modelli SQLAlchemy definiti
- ✅ **Migrazioni**: Sistema Alembic configurato
- ✅ **Decoratori**: Logging ed exception handling production-ready
- ✅ **Documentazione**: Design database e materiale di studio

### 🔧 Componenti in Sviluppo
- 🔄 **Connessione DB**: MySQL setup da testare
- 🔄 **Data Population**: Script di import dati

### 📋 Prossimi Obiettivi
- **API Layer**: Creare endpoint REST base
- **Testing**: Setup pytest e test automatizzati
- **Data Validation**: Schema Pydantic per input/output

---

## 💡 Filosofia di Sviluppo

Procedere per micro-step, senza saltare fasi:
- Ogni passaggio deve essere compreso e giustificato
- Niente copia-incolla cieco
- Ogni blocco del sistema deve avere una ragione d'esistere, documentata in `docs/`
- Materiale di studio separato dal codice di progetto (`docs/learning/`)

## 🚀 Setup

```bash
# Clona il repository
git clone https://github.com/Marco-Kara-G/WF_building_assistant.git
cd WF_building_assistant

# Crea ambiente virtuale con uv
uv venv

# Attiva l'ambiente virtuale
.venv\Scripts\activate  # Windows

# Installa le dipendenze
uv pip install -e .
```

## 🔧 Componenti Tecnici

### Database Models ✅
- **Warframe**: Statistiche base, polarità, abilità
- **Armi**: Primary, Secondary, Melee con statistiche specifiche
- **Mod**: Effetti, polarità, requisiti
- **Build**: Configurazioni personalizzate
- **Companion**: Pet e Sentinel con abilità

### Decoratori ✅
```python
# Exception handling con logging
@handle_exception(exceptions=(ValueError, TypeError))
def risky_function():
    pass

# Logging automatico
@handle_logger
def tracked_function():
    pass
```

### Database Setup ✅
```bash
# Creare migrazione
alembic revision --autogenerate -m "descrizione"

# Applicare migrazioni
alembic upgrade head
```

---

## 📚 Documentazione

- `docs/design_database.md` - Design e decisioni database
- `docs/entity_relations.md` - Relazioni tra entità
- `docs/learning/` - Materiale di studio (gitignored)
  - `study/decorators/` - Tutorial e best practices
  - `issues/decorators/` - Fix e correzioni

---

## 📝 Licenza

TBD 
