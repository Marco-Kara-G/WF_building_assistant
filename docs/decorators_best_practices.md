# 🎨 Decorators - Best Practices e Implementazione

## 📊 Stato Attuale

I file `src/decorators/exception.py` e `src/decorators/logger.py` sono attualmente vuoti. Questo documento fornisce linee guida per implementarli seguendo le best practice.

---

## 🎯 Decoratori Consigliati per il Progetto

### 1. **Logger Decorator** (`src/decorators/logger.py`)

#### Scopo
Tracciare automaticamente l'esecuzione di funzioni/metodi con:
- Parametri di input
- Valore di ritorno
- Tempo di esecuzione
- Eventuali eccezioni

#### Best Practices da Implementare

**✅ Preservare i metadati della funzione originale**
- Usare `functools.wraps` per mantenere `__name__`, `__doc__`, `__annotations__`

**✅ Supportare funzioni sincrone e asincrone**
- Creare due versioni: `@log_execution` e `@log_execution_async`
- Oppure un unico decorator intelligente che rileva il tipo

**✅ Configurabilità**
- Livello di log (DEBUG, INFO, WARNING, ERROR)
- Possibilità di escludere parametri sensibili (password, token)
- Opzione per disabilitare il logging del valore di ritorno

**✅ Performance**
- Misurare il tempo di esecuzione con `time.perf_counter()`
- Evitare overhead eccessivo in produzione

**✅ Gestione eccezioni**
- Loggare l'eccezione ma ri-lanciarla (non swallow)
- Includere stack trace completo

#### Esempio di Firma Consigliata

```python
@log_execution(
    level="INFO",
    exclude_params=["password", "api_key"],
    log_return=True,
    log_execution_time=True
)
def my_function(param1, password):
    ...
```

---

### 2. **Exception Decorator** (`src/decorators/exception.py`)

#### Scopo
Gestire eccezioni in modo centralizzato e consistente:
- Catturare eccezioni specifiche
- Trasformare eccezioni tecniche in eccezioni di dominio
- Fornire fallback o retry logic
- Integrare con sistema di logging

#### Best Practices da Implementare

**✅ Specificità delle eccezioni**
- Permettere di specificare quali eccezioni catturare
- Non usare `except Exception` generico senza motivo

**✅ Trasformazione eccezioni**
- Convertire eccezioni SQLAlchemy in eccezioni custom del dominio
- Esempio: `DatabaseError`, `EntityNotFoundError`, `ValidationError`

**✅ Retry Logic (opzionale)**
- Per operazioni di rete o DB transitori
- Con backoff esponenziale
- Numero massimo di tentativi configurabile

**✅ Context preservation**
- Mantenere il traceback originale con `raise ... from e`
- Aggiungere contesto utile per il debugging

**✅ Integrazione con logging**
- Loggare automaticamente le eccezioni catturate
- Includere contesto della funzione e parametri

#### Esempio di Firma Consigliata

```python
@handle_exceptions(
    catch=(SQLAlchemyError, ConnectionError),
    raise_as=DatabaseError,
    retry=3,
    retry_delay=1.0,
    log_error=True
)
def database_operation():
    ...
```

---

## 🏗️ Architettura Consigliata

### Struttura File

```
src/decorators/
├── __init__.py          → Esporta tutti i decoratori
├── logger.py            → Decoratori per logging
├── exception.py         → Decoratori per gestione eccezioni
├── validation.py        → (Futuro) Validazione input/output
├── cache.py             → (Futuro) Caching risultati
└── timing.py            → (Futuro) Performance monitoring
```

### Dipendenze da Aggiungere

```toml
# pyproject.toml
dependencies = [
    # ... esistenti ...
    "python-json-logger>=2.0.7",  # Structured logging
]
```

---

## 🔧 Pattern di Implementazione

### 1. Decorator con Parametri

```python
from functools import wraps
from typing import Callable, Any

def my_decorator(param1: str, param2: bool = True):
    """Decorator factory che accetta parametri."""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            # Logica del decorator usando param1, param2
            result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator
```

### 2. Decorator per Async/Sync

```python
import asyncio
import inspect
from functools import wraps

def universal_decorator(func: Callable) -> Callable:
    """Funziona sia con funzioni sync che async."""
    if asyncio.iscoroutinefunction(func):
        @wraps(func)
        async def async_wrapper(*args, **kwargs):
            # Logica pre-esecuzione
            result = await func(*args, **kwargs)
            # Logica post-esecuzione
            return result
        return async_wrapper
    else:
        @wraps(func)
        def sync_wrapper(*args, **kwargs):
            # Logica pre-esecuzione
            result = func(*args, **kwargs)
            # Logica post-esecuzione
            return result
        return sync_wrapper
```

### 3. Decorator con Classi

```python
from functools import wraps
from typing import Callable

class LogExecution:
    """Decorator implementato come classe per stato complesso."""
    
    def __init__(self, level: str = "INFO"):
        self.level = level
    
    def __call__(self, func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Logica del decorator
            result = func(*args, **kwargs)
            return result
        return wrapper
```

---

## 🎯 Casi d'Uso Specifici per il Progetto

### Per API Endpoints (FastAPI)

```python
@log_execution(level="INFO")
@handle_exceptions(catch=(DatabaseError,), raise_as=HTTPException)
async def get_warframe(warframe_id: int):
    """Endpoint per recuperare un Warframe."""
    ...
```

### Per Database Operations

```python
@handle_exceptions(
    catch=(SQLAlchemyError,),
    raise_as=DatabaseError,
    retry=3
)
@log_execution(level="DEBUG", log_execution_time=True)
def create_warframe(session: Session, data: dict):
    """Crea un nuovo Warframe nel database."""
    ...
```

### Per Data Fetching (API esterne)

```python
@handle_exceptions(
    catch=(RequestException, Timeout),
    retry=3,
    retry_delay=2.0
)
@log_execution(level="INFO")
async def fetch_warframe_data(api_url: str):
    """Recupera dati da API esterna."""
    ...
```

---

## ⚠️ Anti-Pattern da Evitare

### ❌ Non Preservare Metadati

```python
# SBAGLIATO
def bad_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper  # Perde __name__, __doc__, ecc.
```

### ❌ Swallowing Exceptions

```python
# SBAGLIATO
def bad_exception_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception:
            return None  # Nasconde l'errore!
    return wrapper
```

### ❌ Overhead Eccessivo

```python
# SBAGLIATO - troppo logging in produzione
def verbose_logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        print(f"Args: {args}")
        print(f"Kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"Result: {result}")
        return result
    return wrapper
```

### ❌ Decorator Non Componibili

```python
# SBAGLIATO - non funziona con altri decoratori
def bad_decorator(func):
    # Non usa @wraps
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    wrapper.custom_attr = "value"  # Attributi custom problematici
    return wrapper
```

---

## 📚 Testing dei Decoratori

### Principi

1. **Testare il decorator in isolamento**
   - Verificare che preservi metadati
   - Verificare comportamento con/senza parametri

2. **Testare l'integrazione**
   - Applicare a funzioni reali
   - Verificare side effects (logging, eccezioni)

3. **Testare edge cases**
   - Funzioni che sollevano eccezioni
   - Funzioni async
   - Funzioni con parametri complessi

### Esempio Struttura Test

```python
# tests/test_decorators/test_logger.py
import pytest
from src.decorators.logger import log_execution

def test_log_execution_preserves_metadata():
    """Verifica che il decorator preservi i metadati."""
    @log_execution()
    def sample_func():
        """Sample docstring."""
        pass
    
    assert sample_func.__name__ == "sample_func"
    assert sample_func.__doc__ == "Sample docstring."

def test_log_execution_with_exception():
    """Verifica che le eccezioni vengano ri-lanciate."""
    @log_execution()
    def failing_func():
        raise ValueError("Test error")
    
    with pytest.raises(ValueError, match="Test error"):
        failing_func()
```

---

## 🚀 Roadmap Implementazione

### Fase 1: Base (Priorità Alta)
1. Implementare `@log_execution` base in `logger.py`
2. Implementare `@handle_exceptions` base in `exception.py`
3. Creare `__init__.py` per esportare i decoratori
4. Scrivere test unitari

### Fase 2: Miglioramenti (Priorità Media)
1. Aggiungere supporto async
2. Implementare retry logic
3. Aggiungere configurazione via parametri
4. Integrare con sistema di logging centralizzato

### Fase 3: Avanzato (Priorità Bassa)
1. Creare `validation.py` per validazione Pydantic
2. Creare `cache.py` per caching risultati
3. Creare `timing.py` per performance monitoring
4. Implementare decoratori specifici per FastAPI

---

## 📖 Riferimenti

- [PEP 318 - Decorators](https://peps.python.org/pep-0318/)
- [Python Decorator Library](https://wiki.python.org/moin/PythonDecoratorLibrary)
- [functools.wraps documentation](https://docs.python.org/3/library/functools.html#functools.wraps)
- [Real Python - Primer on Python Decorators](https://realpython.com/primer-on-python-decorators/)

---

## 💡 Note Finali

- **Inizia semplice**: Implementa prima le funzionalità base, poi aggiungi complessità
- **Testa sempre**: I decoratori sono codice critico che influenza tutto il sistema
- **Documenta**: Ogni decorator deve avere docstring chiara con esempi
- **Sii consistente**: Usa gli stessi pattern in tutto il progetto
- **Performance**: Misura l'overhead dei decoratori in produzione
