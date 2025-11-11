# 🌐 Warframe API Endpoints

Documentazione degli endpoint utili da **https://api.warframestat.us/** per il progetto Warframe Build Assistant.

---

## 📊 Statistiche API

- **Base URL**: `https://api.warframestat.us/`
- **Totale Items**: ~16,080
- **Totale Weapons**: 623
- **Totale Mods**: 1,751
- **Warframes**: 114
- **Primary Weapons**: 187
- **Secondary Weapons**: 146
- **Melee Weapons**: 262
- **Arch-Gun**: 20
- **Arch-Melee**: 8
- **Mods**: 1,751
- **Pets**: 66
- **Sentinels**: 17

---

## 🔑 Endpoint Principali

### 1. **Tutti gli Items**
```
GET /items/
```
Restituisce tutti gli item del gioco (Warframe, armi, mod, companion, etc.)

**Risposta**: Array di ~16,080 oggetti

**Categorie disponibili**:
- `Warframes`
- `Mods`
- `Pets`
- `Sentinels`
- `Arcanes`, `Relics`, `Resources`
- `Gear`, `Glyphs`, `Skins`, `Sigils`
- `Archwing`, `Railjack`, `Quests`, `Node`

**Nota**: Le armi sono in `/weapons/` e le mod in `/mods/`

---

### 2. **Tutte le Mod**
```
GET /mods/
```
Restituisce tutte le mod del gioco

**Risposta**: Array di 1,751 oggetti

**Tutte le mod hanno** `category == "Mods"`

---

### 3. **Tutte le Armi**
```
GET /weapons/
```
Restituisce tutte le armi del gioco

**Risposta**: Array di 623 oggetti

**Categorie disponibili** (campo `category`):
- `Primary` (187 armi)
- `Secondary` (146 armi)
- `Melee` (262 armi)
- `Arch-Gun` (20 armi)
- `Arch-Melee` (8 armi)

---

### 4. **Ricerca Item per Nome**
```
GET /items/search/{query}/
```

**Esempio**:
```
GET /items/search/Excalibur/
```

**Risposta**: Array di oggetti che corrispondono alla query

**Uso**: Ricerca fuzzy per trovare item specifici

---

### 5. **Item Specifico per Nome Esatto**
```
GET /items/{itemName}/
```

**Esempio**:
```
GET /items/Excalibur/
GET /items/Boltor/
GET /items/Serration/
```

**Risposta**: Oggetto singolo con tutti i dettagli

**Nota**: Il nome deve essere esatto (case-sensitive)

---

## 📦 Struttura Dati per Categoria

### 🤖 Warframes

**Endpoint**: `GET /items/` (filtrare per `category == "Warframes"`)

**Campi disponibili** (44 campi):
```json
{
  "name": "Excalibur",
  "uniqueName": "/Lotus/Powersuits/Excalibur/ExcaliburBaseSuit",
  "description": "...",
  "health": 100,
  "shield": 100,
  "armor": 225,
  "power": 100,
  "sprint": 1.0,
  "sprintSpeed": 1.0,
  "stamina": 100,
  "aura": "madurai",
  "sex": "Male",
  "polarities": ["madurai", "vazarin"],
  "abilities": [
    {
      "uniqueName": "...",
      "name": "Slash Dash",
      "description": "...",
      "imageName": "..."
    }
  ],
  "passiveDescription": "...",
  "exalted": ["..."],
  "isPrime": false,
  "vaulted": false,
  "masteryReq": 0,
  "buildTime": 259200,
  "buildPrice": 25000,
  "bpCost": 35000,
  "marketCost": 75,
  "skipBuildTimePrice": 50,
  "components": [...],
  "imageName": "excalibur.png",
  "category": "Warframes",
  "tradable": false,
  "masterable": true,
  "productCategory": "Suits",
  "type": "Warframe",
  "introduced": {...},
  "releaseDate": "...",
  "patchlogs": [...],
  "drops": [...],
  "wikiaThumbnail": "...",
  "wikiaUrl": "...",
  "wikiAvailable": true
}
```

**Campi chiave per il progetto**:
- `name`, `uniqueName`, `description`
- `health`, `shield`, `armor`, `power`, `sprint`
- `aura`, `polarities`
- `abilities[]` (array di abilità)
- `passiveDescription`
- `isPrime`, `vaulted`, `masteryReq`
- `imageName`

---

### 🔫 Armi (Primary/Secondary/Melee/Arch-Gun/Arch-Melee)

**Endpoint**: `GET /weapons/` (filtrare per `category`)

**Campi disponibili** (~50 campi):
```json
{
  "name": "Boltor",
  "uniqueName": "/Lotus/Weapons/Tenno/Rifle/BoltoRifle",
  "description": "...",
  "category": "Primary",
  "type": "Primary",
  "productCategory": "LongGuns",
  "damage": 25,
  "damagePerShot": [25],
  "totalDamage": 25,
  "criticalChance": 0.1,
  "criticalMultiplier": 2.0,
  "procChance": 0.2,
  "fireRate": 8.75,
  "accuracy": 50,
  "magazineSize": 60,
  "reloadTime": 2.4,
  "multishot": 1,
  "noise": "Alarming",
  "trigger": "Auto",
  "attacks": [
    {
      "name": "Normal Attack",
      "damage": {...},
      "critChance": 0.1,
      "critMult": 2.0,
      "statusChance": 0.2,
      "speed": 8.75
    }
  ],
  "polarities": ["madurai"],
  "slot": 0,
  "masteryReq": 2,
  "disposition": 5,
  "omegaAttenuation": 1.0,
  "isPrime": false,
  "vaulted": false,
  "buildTime": 43200,
  "buildPrice": 15000,
  "marketCost": 150,
  "imageName": "boltor.png",
  "tradable": false,
  "masterable": true,
  "introduced": {...},
  "patchlogs": [...],
  "drops": [...]
}
```

**Campi chiave per il progetto**:
- `name`, `uniqueName`, `description`, `category`
- `damage`, `criticalChance`, `criticalMultiplier`, `procChance`
- `fireRate`, `accuracy`, `magazineSize`, `reloadTime`
- `attacks[]` (dettagli attacchi)
- `polarities[]`, `disposition`
- `masteryReq`, `isPrime`, `vaulted`
- `imageName`

---

### 🎴 Mods

**Endpoint**: `GET /mods/`

**Campi disponibili** (~30 campi):
```json
{
  "name": "Serration",
  "uniqueName": "/Lotus/Upgrades/Mods/Rifle/DualStat/RifleDamageMod",
  "description": "+165% Damage",
  "category": "Mods",
  "type": "Rifle Mod",
  "baseDrain": 14,
  "fusionLimit": 10,
  "rarity": "Rare",
  "polarity": "madurai",
  "compatName": "Rifle",
  "isAugment": false,
  "isExilus": false,
  "isUtility": false,
  "isPrime": false,
  "transmutable": true,
  "tradable": true,
  "levelStats": [
    {
      "stats": ["+15% Damage"]
    },
    {
      "stats": ["+30% Damage"]
    }
  ],
  "stats": ["+165% Damage"],
  "upgradeEntries": [...],
  "modSet": null,
  "modSetValues": null,
  "numUpgradesInSet": 0,
  "buffSet": null,
  "imageName": "serration.png",
  "introduced": {...},
  "patchlogs": [...],
  "drops": [...]
}
```

**Campi chiave per il progetto**:
- `name`, `uniqueName`, `description`
- `baseDrain`, `fusionLimit`, `rarity`, `polarity`
- `compatName` (tipo compatibilità)
- `isAugment`, `isExilus`
- `levelStats[]` (stats per livello)
- `stats[]` (stats massime)
- `tradable`, `transmutable`
- `imageName`

---

### 🐾 Companion (Pets/Sentinels)

**Endpoint**: `GET /items/` (filtrare per `category in ["Pets", "Sentinels"]`)

**Campi disponibili** (~40 campi):
```json
{
  "name": "Carrier",
  "uniqueName": "/Lotus/Weapons/Sentinels/CarrierSentinel/CarrierSentinel",
  "description": "...",
  "category": "Sentinels",
  "type": "Sentinel",
  "health": 200,
  "shield": 100,
  "armor": 50,
  "power": 100,
  "stamina": 100,
  "polarities": ["madurai"],
  "masteryReq": 0,
  "buildTime": 43200,
  "buildPrice": 15000,
  "isPrime": false,
  "vaulted": false,
  "imageName": "carrier.png",
  "tradable": false,
  "masterable": true,
  "productCategory": "Sentinels",
  "introduced": {...},
  "patchlogs": [...],
  "drops": [...]
}
```

**Campi chiave per il progetto**:
- `name`, `uniqueName`, `description`, `category`
- `health`, `shield`, `armor`, `power`
- `polarities[]`
- `masteryReq`, `isPrime`, `vaulted`
- `imageName`

---

## 🎯 Endpoint Utili per il Progetto

### Per Popolare il Database

1. **Caricare tutti i Warframe**:
   ```python
   GET /items/
   # Filtrare per category == "Warframes"
   ```

2. **Caricare tutte le Armi**:
   ```python
   GET /weapons/
   # Filtrare per category in ["Primary", "Secondary", "Melee", "Arch-Gun", "Arch-Melee"]
   ```

3. **Caricare tutte le Mod**:
   ```python
   GET /mods/
   # Tutte hanno category == "Mods"
   ```

4. **Caricare tutti i Companion**:
   ```python
   GET /items/
   # Filtrare per category in ["Pets", "Sentinels"]
   ```

---

## 💡 Strategia di Implementazione

### Script di Caricamento Dati

```python
# scripts/load_from_api.py

import requests
from typing import List, Dict

API_BASE_URL = "https://api.warframestat.us/"

def fetch_all_items() -> List[Dict]:
    """Recupera tutti gli item dall'API"""
    response = requests.get(f"{API_BASE_URL}items/")
    return response.json()

def fetch_all_weapons() -> List[Dict]:
    """Recupera tutte le armi dall'API"""
    response = requests.get(f"{API_BASE_URL}weapons/")
    return response.json()

def fetch_all_mods() -> List[Dict]:
    """Recupera tutte le mod dall'API"""
    response = requests.get(f"{API_BASE_URL}mods/")
    return response.json()

def filter_by_category(items: List[Dict], category: str) -> List[Dict]:
    """Filtra item per categoria"""
    return [item for item in items if item.get('category') == category]

def load_warframes():
    items = fetch_all_items()
    warframes = filter_by_category(items, "Warframes")
    # Processa e salva nel database
    
def load_weapons():
    weapons = fetch_all_weapons()
    primary = filter_by_category(weapons, "Primary")
    secondary = filter_by_category(weapons, "Secondary")
    melee = filter_by_category(weapons, "Melee")
    arch_gun = filter_by_category(weapons, "Arch-Gun")
    arch_melee = filter_by_category(weapons, "Arch-Melee")
    # Processa e salva nel database

def load_mods():
    mods = fetch_all_mods()
    # Processa e salva nel database

def load_companions():
    items = fetch_all_items()
    pets = filter_by_category(items, "Pets")
    sentinels = filter_by_category(items, "Sentinels")
    # Processa e salva nel database
```

---

## 🔄 Mapping API → Database

### Warframe
```
API Field              → DB Field
-----------------------------------------
name                   → name
uniqueName             → unique_name
description            → description
health                 → health
shield                 → shield
armor                  → armor
power                  → energy
sprint                 → sprint_speed
aura                   → aura_polarity
polarities             → polarities (JSON)
abilities              → Ability table (relazione)
passiveDescription     → passive_description
isPrime                → is_prime
masteryReq             → mastery_rank
```

### Weapons
```
API Field              → DB Field
-----------------------------------------
name                   → name
uniqueName             → unique_name
description            → description
category               → weapon_type
damage                 → base_damage
criticalChance         → critical_chance
criticalMultiplier     → critical_multiplier
procChance             → status_chance
fireRate               → fire_rate
accuracy               → accuracy
magazineSize           → magazine_size
reloadTime             → reload_time
polarities             → polarities (JSON)
disposition            → riven_disposition
masteryReq             → mastery_rank
```

### Mods
```
API Field              → DB Field
-----------------------------------------
name                   → name
uniqueName             → unique_name
description            → description
baseDrain              → drain_cost
fusionLimit            → max_rank
rarity                 → rarity
polarity               → polarity
compatName             → compatible_with
isAugment              → is_augment
stats                  → effect (JSON)
```

---

## ⚠️ Note Importanti

1. **Slash finale obbligatorio**: Tutti gli endpoint richiedono `/` alla fine
2. **Encoding UTF-8**: Usare `encoding='utf-8'` per leggere i dati
3. **Rate limiting**: Non documentato, usare con moderazione
4. **Dati statici**: L'API fornisce dati statici, non real-time game state
5. **Nomi case-sensitive**: I nomi degli item sono case-sensitive
6. **Immagini**: I campi `imageName` contengono solo il nome file, non l'URL completo

---

## 🔗 Risorse

- **API Base**: https://api.warframestat.us/
- **GitHub**: https://github.com/WFCD/warframe-items
- **Documentazione**: https://docs.warframestat.us/

---

**Ultimo aggiornamento**: 2024
