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
├── docs/           → Documentazione tecnica e decisioni progettuali
├── migrations/     → Versionamento schema DB
├── scripts/        → Script di supporto e manutenzione
├── src/            → Codice sorgente
│   ├── api/        → Endpoint REST
│   ├── config/     → Configurazione ambiente e variabili
│   ├── database/   → Connessione e sessione DB
│   ├── models/     → Modelli SQLAlchemy + schema Pydantic
│   └── utils/      → Funzioni di utilità
├── tests/          → Test unitari e d'integrazione
├── pyproject.toml  → Configurazione uv + dipendenze
└── uv.lock         → Lock delle versioni
```

## 🗺️ Roadmap

1. **Definizione dominio** → Comprendere entità, relazioni e scopo
2. **Progettazione modello dati** → Definire Warframe, Mod, Build ecc.
3. **Connessione al DB MySQL** → Creare e migrare lo schema base
4. **Implementazione autenticazione base** → JWT minimale per API locali
5. **Creazione API CRUD** → Per le entità principali
6. **Testing + documentazione API**
7. **(Futuro)** Aggiornamento automatico dei dati di gioco
8. **(Futuro)** Modulo AI per suggerimenti e ottimizzazioni

## 💡 Filosofia di Sviluppo

Procedere per micro-step, senza saltare fasi:
- Ogni passaggio deve essere compreso e giustificato
- Niente copia-incolla cieco
- Ogni blocco del sistema deve avere una ragione d'esistere, documentata in `docs/`

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

## 📝 Licenza

TBD 
