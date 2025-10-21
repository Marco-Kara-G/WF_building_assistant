# Entity Relations Schema

## Entities

### Warframe

**Rappresenta:** il personaggio principale del giocatore.

**Contiene:**
- Nome
- Descrizione
- Polarità
- Statistiche base (salute, energia, armatura, scudo)

**Relazioni:**
- Può avere più Build associate
- Può essere influenzato da Mod (tramite una Build)

### Weapon

**Rappresenta:** qualsiasi arma (primaria, secondaria, corpo a corpo).

**Contiene:**
- Nome
- Tipo
- Danni base
- Velocità d'attacco

**Relazioni:**
- Può essere inclusa in una Build
- Può essere modificata da Mod

### Mod

**Rappresenta:** una carta che altera statistiche di Warframe o armi.

**Contiene:**
- Nome
- Tipo (Warframe/arma/companion)
- Effetto
- Valore
- Rarità
- Polarità

**Relazioni:**
- Può essere equipaggiata in una Build
- Può essere collegata a diversi tipi di entità (Warframe, Weapon, Companion)

### Companion

**Rappresenta:** un'unità di supporto che accompagna il giocatore.

**Contiene:**
- Nome
- Tipo (Sentinel, Kubrow, ecc.)
- Abilità

**Relazioni:**
- Può avere Mod proprie
- Può far parte di una Build

### Build

**Rappresenta:** una combinazione di Warframe, armi, companion e mod scelti per una configurazione.

**Contiene:**
- Nome
- Descrizione
- Autore
- Data creazione
- Lista dei componenti

**Relazioni:**
- 1 Warframe → N Build
- N Build → N Mod (relazione molti-a-molti)
- 1 Build → 1 Companion (opzionale)
- 1 Build → 3 Weapon (primaria, secondaria, melee)

## Database Relationships Schema

### Build Relationships

- **Build → Warframe** (1:1, mandatory)
  - Each build must have exactly one Warframe
  - Foreign key: build.warframe_id → warframe.id
  
- **Build → PrimaryWeapon** (1:0..1, optional)
  - Each build can have zero or one primary weapon
  - Foreign key: build.primary_weapon_id → primary_weapon.id
  
- **Build → SecondaryWeapon** (1:0..1, optional)
  - Each build can have zero or one secondary weapon
  - Foreign key: build.secondary_weapon_id → secondary_weapon.id
  
- **Build → MeleeWeapon** (1:0..1, optional)
  - Each build can have zero or one melee weapon
  - Foreign key: build.melee_weapon_id → melee_weapon.id
  
- **Build → Companion** (1:0..1, optional)
  - Each build can have zero or one companion
  - Foreign key: build.companion_id → companion.id
  
- **Build ↔ Mod** (N:N through BuildMod)
  - Each build can have multiple mods
  - Each mod can be used in multiple builds
  - Junction table: BuildMod with target_type and slot_index

### Warframe Relationships

- **Warframe → Ability** (1:4)
  - Each Warframe has exactly 4 abilities
  - Foreign key: ability.warframe_id → warframe.id
  
- **Warframe → PassiveAbility** (1:1)
  - Each Warframe has exactly 1 passive ability
  - Foreign key: passive_ability.warframe_id → warframe.id (UNIQUE)

### Companion Relationships

- **Companion → CompanionAbility** (1:N)
  - Each Companion can have multiple abilities
  - Foreign key: companion_ability.companion_id → companion.id
