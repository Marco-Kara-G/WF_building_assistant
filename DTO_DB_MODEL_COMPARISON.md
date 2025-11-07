# 🔍 Confronto DTO vs DB Models

**Data**: Gennaio 2025  
**Scopo**: Verificare corrispondenza tra DTOs e Database Models

---

## 1. WarframeDTO vs Warframe Model

### DB Model (warframe_db_model.py)
```python
id: Mapped[int]
unique_name: Mapped[str]
name: Mapped[str]
description: Mapped[str]          # nullable=True
health: Mapped[float]
shield: Mapped[float]
armor: Mapped[float]
power: Mapped[float]
sprint_speed: Mapped[float]
mastery_rank: Mapped[int]
polarities: Mapped[dict]          # nullable=True
aura_polarity: Mapped[str]
exilus_polarity: Mapped[str]      # nullable=True
sex: Mapped[str]                  # nullable=True
```

### DTO (warframe_dto.py)
```python
id: int
unique_name: str
name: str
description: str                  # ❌ MANCA Optional
health: float
shield: float
armor: float
power: float
sprint_speed: float
mastery_rank: int
polarities: dict                  # ❌ MANCA Optional
aura_polarity: str
exilus_polarity: str              # ❌ MANCA Optional
sex: str                          # ❌ MANCA Optional
```

### ⚠️ Problemi
- ❌ `description` - DB nullable, DTO non Optional
- ❌ `polarities` - DB nullable, DTO non Optional
- ❌ `exilus_polarity` - DB nullable, DTO non Optional
- ❌ `sex` - DB nullable, DTO non Optional

---

## 2. PrimaryWeaponDTO vs PrimaryWeapon Model

### DB Model
```python
id: Mapped[int]
unique_name: Mapped[str]
name: Mapped[str]
description: Mapped[str]          # nullable=True
weapon_type: Mapped[str]
mastery_rank: Mapped[int]
impact_damage: Mapped[float]
puncture_damage: Mapped[float]
slash_damage: Mapped[float]
fire_rate: Mapped[float]
critical_chance: Mapped[float]
critical_multiplier: Mapped[float]
status_chance: Mapped[float]
accuracy: Mapped[float]
magazine_size: Mapped[int]
max_ammo: Mapped[int]
reload_time: Mapped[float]
projectile: Mapped[str]           # nullable=True
noise: Mapped[str]
trigger: Mapped[str]
riven_disposition: Mapped[float]
polarities: Mapped[dict]          # nullable=True
exilus_polarity: Mapped[str]      # nullable=True
```

### DTO
```python
id: int
unique_name: str
name: str
description: Optional[str] = None         # ✅ OK
weapon_type: str
mastery_rank: int
impact_damage: float
puncture_damage: float
slash_damage: float
fire_rate: float
critical_chance: float
critical_multiplier: float
status_chance: float
accuracy: float
magazine_size: int
max_ammo: int
reload_time: float
projectile: Optional[str] = None          # ✅ OK
noise: str
trigger: str
riven_disposition: float
polarities: Optional[dict] = None         # ✅ OK
exilus_polarity: Optional[str] = None     # ✅ OK
```

### ✅ Status
- ✅ Tutti i campi corrispondono
- ✅ Optional correttamente applicato

---

## 3. SecondaryWeaponDTO vs SecondaryWeapon Model

### Confronto
**Identico a PrimaryWeapon** - stessi campi

### ✅ Status
- ✅ Tutti i campi corrispondono
- ✅ Optional correttamente applicato

---

## 4. MeleeWeaponDTO vs MeleeWeapon Model

### DB Model
```python
id: Mapped[int]
unique_name: Mapped[str]
name: Mapped[str]
description: Mapped[str]          # nullable=True
weapon_type: Mapped[str]
mastery_rank: Mapped[int]
impact_damage: Mapped[float]
puncture_damage: Mapped[float]
slash_damage: Mapped[float]
attack_speed: Mapped[float]
critical_chance: Mapped[float]
critical_multiplier: Mapped[float]
status_chance: Mapped[float]
range: Mapped[float]
slam_attack: Mapped[float]
slam_radial_damage: Mapped[float]
slam_radius: Mapped[float]
slide_attack: Mapped[float]
heavy_attack_damage: Mapped[float]
heavy_slam_attack: Mapped[float]
heavy_slam_radial_damage: Mapped[float]
heavy_slam_radius: Mapped[float]
wind_up: Mapped[float]
follow_through: Mapped[float]
combo_duration: Mapped[float]
riven_disposition: Mapped[float]
polarities: Mapped[dict]          # nullable=True
stance_polarity: Mapped[str]
```

### DTO
```python
id: int
unique_name: str
name: str
description: Optional[str] = None         # ✅ OK
weapon_type: str
mastery_rank: int
impact_damage: float
puncture_damage: float
slash_damage: float
attack_speed: float
critical_chance: float
critical_multiplier: float
status_chance: float
range: float
slam_attack: float
slam_radial_damage: float
slam_radius: float
slide_attack: float
heavy_attack_damage: float
heavy_slam_attack: float
heavy_slam_radial_damage: float
heavy_slam_radius: float
wind_up: float
follow_through: float
combo_duration: float
riven_disposition: float
polarities: Optional[dict] = None         # ✅ OK
stance_polarity: str
```

### ✅ Status
- ✅ Tutti i campi corrispondono
- ✅ Optional correttamente applicato

---

## 5. ModDTO vs Mod Model

### DB Model
```python
id: Mapped[int]
unique_name: Mapped[str]
name: Mapped[str]
description: Mapped[str]          # nullable=True
mod_type: Mapped[str]
polarity: Mapped[str]
rarity: Mapped[str]
base_drain: Mapped[int]
max_rank: Mapped[int]
transmutable: Mapped[bool]
tradable: Mapped[bool]
fusion_limit: Mapped[int]
```

### DTO
```python
id: int
unique_name: str
name: str
description: Optional[str] = None         # ✅ OK
mod_type: str
polarity: str
rarity: str
base_drain: int
max_rank: int
transmutable: bool
tradable: bool
fusion_limit: int
```

### ✅ Status
- ✅ Tutti i campi corrispondono
- ✅ Optional correttamente applicato

---

## 6. CompanionDTO vs Companion Model

### DB Model
```python
id: Mapped[int]
unique_name: Mapped[str]
name: Mapped[str]
description: Mapped[str]          # nullable=True
companion_type: Mapped[str]
health: Mapped[float]
shield: Mapped[float]
armor: Mapped[float]
mastery_rank: Mapped[int]
polarities: Mapped[dict]          # nullable=True
```

### DTO
```python
id: int
unique_name: str
name: str
description: Optional[str] = None         # ✅ OK
companion_type: str
health: float
shield: float
armor: float
mastery_rank: int
polarities: Optional[dict] = None         # ✅ OK
```

### ✅ Status
- ✅ Tutti i campi corrispondono
- ✅ Optional correttamente applicato

---

## 7. AbilityDTO vs Ability Model

### DB Model
```python
id: Mapped[int]
warframe_id: Mapped[int]          # ForeignKey
ability_index: Mapped[int]        # CheckConstraint 1-4
name: Mapped[str]
description: Mapped[str]
energy_cost: Mapped[float]        # nullable=True
can_helminth: Mapped[bool]
```

### DTO
```python
id: int
warframe_id: int
ability_index: int = Field(ge=1, le=4)    # ✅ OK - Validazione Pydantic
name: str
description: str
energy_cost: Optional[float] = None       # ✅ OK
can_helminth: bool
```

### ✅ Status
- ✅ Tutti i campi corrispondono
- ✅ Optional correttamente applicato
- ✅ Constraint validato con Pydantic Field

---

## 8. BuildDTO vs Build Model

### DB Model
```python
id: Mapped[int]
name: Mapped[str]
description: Mapped[str]          # nullable=True
author: Mapped[str]               # nullable=True
created_at: Mapped[datetime]
updated_at: Mapped[datetime]
warframe_id: Mapped[int]          # ForeignKey
primary_weapon_id: Mapped[int]    # ForeignKey, nullable=True
secondary_weapon_id: Mapped[int]  # ForeignKey, nullable=True
melee_weapon_id: Mapped[int]      # ForeignKey, nullable=True
companion_id: Mapped[int]         # ForeignKey, nullable=True
```

### DTO
```python
id: int
name: str
description: Optional[str] = None         # ✅ OK
author: Optional[str] = None              # ✅ OK
created_at: datetime
updated_at: datetime
warframe_id: int
primary_weapon_id: Optional[int] = None   # ✅ OK
secondary_weapon_id: Optional[int] = None # ✅ OK
melee_weapon_id: Optional[int] = None     # ✅ OK
companion_id: Optional[int] = None        # ✅ OK
```

### ✅ Status
- ✅ Tutti i campi corrispondono
- ✅ Optional correttamente applicato

---

## 📊 Riepilogo Problemi

### ❌ WarframeDTO - 4 Problemi
1. `description` - Manca `Optional[str]`
2. `polarities` - Manca `Optional[dict]`
3. `exilus_polarity` - Manca `Optional[str]`
4. `sex` - Manca `Optional[str]`

### ✅ Altri DTOs - Tutti OK
- ✅ PrimaryWeaponDTO
- ✅ SecondaryWeaponDTO
- ✅ MeleeWeaponDTO
- ✅ ModDTO
- ✅ CompanionDTO
- ✅ AbilityDTO
- ✅ BuildDTO

---

## 🛠️ Fix Necessario

### warframe_dto.py
```python
from pydantic import BaseModel
from typing import Optional

class WarframeDTO(BaseModel):
    id: int
    unique_name: str
    name: str
    description: Optional[str] = None      # ✅ FIX
    health: float
    shield: float
    armor: float
    power: float
    sprint_speed: float
    mastery_rank: int
    polarities: Optional[dict] = None      # ✅ FIX
    aura_polarity: str
    exilus_polarity: Optional[str] = None  # ✅ FIX
    sex: Optional[str] = None              # ✅ FIX
```

---

## ✅ Conclusioni

**Status Generale**: 7/8 DTOs corretti (87.5%)

**Azione Richiesta**: Correggere `WarframeDTO` con 4 campi Optional

**Dopo Fix**: 8/8 DTOs corretti (100%)
