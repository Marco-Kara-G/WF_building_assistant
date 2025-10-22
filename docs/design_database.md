 # Database Design

## Entities and Attributes

### Warframe

| Attribute | Type | Constraints | Description |
|-----------|------|-------------|-------------|
| id | INTEGER | PRIMARY KEY, AUTO_INCREMENT | Unique identifier |
| unique_name | VARCHAR(150) | NOT NULL, UNIQUE | API unique identifier |
| name | VARCHAR(100) | NOT NULL | Warframe display name |
| description | TEXT | NULL | Warframe description |
| health | DECIMAL(10,2) | NOT NULL | Base health at rank 0 |
| shield | DECIMAL(10,2) | NOT NULL | Base shield at rank 0 |
| armor | DECIMAL(10,2) | NOT NULL | Base armor at rank 0 |
| power | DECIMAL(10,2) | NOT NULL | Base energy at rank 0 |
| sprint_speed | DECIMAL(5,2) | NOT NULL | Sprint speed multiplier |
| mastery_rank | INTEGER | NOT NULL, DEFAULT 0 | Required mastery rank |
| polarities | JSON | NULL | Array of mod slot polarities |
| aura_polarity | VARCHAR(20) | NOT NULL | Aura slot polarity |
| exilus_polarity | VARCHAR(20) | NULL | Exilus slot polarity |
| sex | VARCHAR(10) | NULL | Male or Female |

**Notes:**
- `unique_name` matches API identifier (e.g., /Lotus/Warframes/...)
- Stats are base values at rank 0, scale with rank
- `polarities` is JSON array of polarity strings
- `power` is the energy stat in API terminology

### Ability

| Attribute | Type | Constraints | Description |
|-----------|------|-------------|-------------|
| id | INTEGER | PRIMARY KEY, AUTO_INCREMENT | Unique identifier |
| warframe_id | INTEGER | NOT NULL, FOREIGN KEY (Warframe.id) | Reference to Warframe |
| ability_index | INTEGER | NOT NULL, CHECK (1 <= value <= 4) | Ability slot (1-4) |
| name | VARCHAR(100) | NOT NULL | Ability name |
| description | TEXT | NOT NULL | Ability description |
| energy_cost | DECIMAL(5,2) | NULL | Energy required to cast |
| can_helminth | BOOLEAN | NOT NULL, DEFAULT FALSE | Can be used in Helminth system |

**Notes:**
- Each Warframe has exactly 4 abilities (ability_index 1-4)
- `energy_cost` can be NULL for passive or toggle abilities
- Foreign key constraint ensures referential integrity with Warframe table
- Unique constraint on (warframe_id, ability_index)

### PassiveAbility

| Attribute | Type | Constraints | Description |
|-----------|------|-------------|-------------|
| id | INTEGER | PRIMARY KEY, AUTO_INCREMENT | Unique identifier |
| warframe_id | INTEGER | NOT NULL, UNIQUE, FOREIGN KEY (Warframe.id) | Reference to Warframe |
| name | VARCHAR(100) | NULL | Passive ability name (if available) |
| description | TEXT | NOT NULL | Passive ability description |

**Notes:**
- Each Warframe has exactly 1 passive ability
- UNIQUE constraint on warframe_id ensures one-to-one relationship
- `name` is optional as API may not always provide it

### PrimaryWeapon

| Attribute | Type | Constraints | Description |
|-----------|------|-------------|-------------|
| id | INTEGER | PRIMARY KEY, AUTO_INCREMENT | Unique identifier |
| unique_name | VARCHAR(150) | NOT NULL, UNIQUE | API unique identifier |
| name | VARCHAR(100) | NOT NULL | Weapon display name |
| description | TEXT | NULL | Weapon description |
| weapon_type | VARCHAR(50) | NOT NULL | Type: Rifle, Shotgun, Bow, Sniper, Launcher |
| mastery_rank | INTEGER | NOT NULL, DEFAULT 0 | Required mastery rank |
| impact_damage | DECIMAL(10,2) | NOT NULL, DEFAULT 0 | Impact damage |
| puncture_damage | DECIMAL(10,2) | NOT NULL, DEFAULT 0 | Puncture damage |
| slash_damage | DECIMAL(10,2) | NOT NULL, DEFAULT 0 | Slash damage |
| fire_rate | DECIMAL(5,2) | NOT NULL | Rounds per second |
| critical_chance | DECIMAL(5,4) | NOT NULL | Critical chance (0-1 decimal) |
| critical_multiplier | DECIMAL(5,2) | NOT NULL | Critical damage multiplier |
| status_chance | DECIMAL(5,4) | NOT NULL | Status chance (0-1 decimal) |
| accuracy | DECIMAL(5,2) | NOT NULL | Weapon accuracy |
| magazine_size | INTEGER | NOT NULL | Magazine capacity |
| max_ammo | INTEGER | NOT NULL | Maximum ammo reserve |
| reload_time | DECIMAL(5,2) | NOT NULL | Reload time in seconds |
| projectile | VARCHAR(50) | NULL | Projectile type |
| noise | VARCHAR(20) | NOT NULL | Silent or Alarming |
| trigger | VARCHAR(50) | NOT NULL | Trigger type (Auto, Semi-Auto, Burst, etc.) |
| riven_disposition | DECIMAL(3,2) | NOT NULL | Riven disposition (0.5 to 1.55) |
| polarities | JSON | NULL | Array of mod slot polarities |
| exilus_polarity | VARCHAR(20) | NULL | Exilus slot polarity |

**Notes:**
- `unique_name` matches API identifier (e.g., /Lotus/Weapons/...)
- Damage split into separate columns for easier queries
- `critical_chance` and `status_chance` stored as decimals (0.25 = 25%)
- `polarities` is JSON array of polarity strings

### SecondaryWeapon

| Attribute | Type | Constraints | Description |
|-----------|------|-------------|-------------|
| id | INTEGER | PRIMARY KEY, AUTO_INCREMENT | Unique identifier |
| unique_name | VARCHAR(150) | NOT NULL, UNIQUE | API unique identifier |
| name | VARCHAR(100) | NOT NULL | Weapon display name |
| description | TEXT | NULL | Weapon description |
| weapon_type | VARCHAR(50) | NOT NULL | Type: Pistol, Dual Pistols, Thrown, Shotgun |
| mastery_rank | INTEGER | NOT NULL, DEFAULT 0 | Required mastery rank |
| impact_damage | DECIMAL(10,2) | NOT NULL, DEFAULT 0 | Impact damage |
| puncture_damage | DECIMAL(10,2) | NOT NULL, DEFAULT 0 | Puncture damage |
| slash_damage | DECIMAL(10,2) | NOT NULL, DEFAULT 0 | Slash damage |
| fire_rate | DECIMAL(5,2) | NOT NULL | Rounds per second |
| critical_chance | DECIMAL(5,4) | NOT NULL | Critical chance (0-1 decimal) |
| critical_multiplier | DECIMAL(5,2) | NOT NULL | Critical damage multiplier |
| status_chance | DECIMAL(5,4) | NOT NULL | Status chance (0-1 decimal) |
| accuracy | DECIMAL(5,2) | NOT NULL | Weapon accuracy |
| magazine_size | INTEGER | NOT NULL | Magazine capacity |
| max_ammo | INTEGER | NOT NULL | Maximum ammo reserve |
| reload_time | DECIMAL(5,2) | NOT NULL | Reload time in seconds |
| projectile | VARCHAR(50) | NULL | Projectile type |
| noise | VARCHAR(20) | NOT NULL | Silent or Alarming |
| trigger | VARCHAR(50) | NOT NULL | Trigger type (Auto, Semi-Auto, Burst, etc.) |
| riven_disposition | DECIMAL(3,2) | NOT NULL | Riven disposition (0.5 to 1.55) |
| polarities | JSON | NULL | Array of mod slot polarities |
| exilus_polarity | VARCHAR(20) | NULL | Exilus slot polarity |

**Notes:**
- `unique_name` matches API identifier
- Damage split into separate columns for easier queries
- `critical_chance` and `status_chance` stored as decimals (0.25 = 25%)
- `polarities` is JSON array of polarity strings

### MeleeWeapon

| Attribute | Type | Constraints | Description |
|-----------|------|-------------|-------------|
| id | INTEGER | PRIMARY KEY, AUTO_INCREMENT | Unique identifier |
| unique_name | VARCHAR(150) | NOT NULL, UNIQUE | API unique identifier |
| name | VARCHAR(100) | NOT NULL | Weapon display name |
| description | TEXT | NULL | Weapon description |
| weapon_type | VARCHAR(50) | NOT NULL | Type: Sword, Hammer, Staff, Polearm, Dagger, etc. |
| mastery_rank | INTEGER | NOT NULL, DEFAULT 0 | Required mastery rank |
| impact_damage | DECIMAL(10,2) | NOT NULL, DEFAULT 0 | Impact damage |
| puncture_damage | DECIMAL(10,2) | NOT NULL, DEFAULT 0 | Puncture damage |
| slash_damage | DECIMAL(10,2) | NOT NULL, DEFAULT 0 | Slash damage |
| attack_speed | DECIMAL(5,2) | NOT NULL | Attacks per second |
| critical_chance | DECIMAL(5,4) | NOT NULL | Critical chance (0-1 decimal) |
| critical_multiplier | DECIMAL(5,2) | NOT NULL | Critical damage multiplier |
| status_chance | DECIMAL(5,4) | NOT NULL | Status chance (0-1 decimal) |
| range | DECIMAL(5,2) | NOT NULL | Melee range in meters |
| slam_attack | DECIMAL(10,2) | NOT NULL | Slam attack damage |
| slam_radial_damage | DECIMAL(10,2) | NOT NULL | Slam radial damage |
| slam_radius | DECIMAL(5,2) | NOT NULL | Slam attack radius |
| slide_attack | DECIMAL(10,2) | NOT NULL | Slide attack damage |
| heavy_attack_damage | DECIMAL(10,2) | NOT NULL | Heavy attack damage |
| heavy_slam_attack | DECIMAL(10,2) | NOT NULL | Heavy slam attack damage |
| heavy_slam_radial_damage | DECIMAL(10,2) | NOT NULL | Heavy slam radial damage |
| heavy_slam_radius | DECIMAL(5,2) | NOT NULL | Heavy slam radius |
| wind_up | DECIMAL(5,2) | NOT NULL | Heavy attack wind-up time |
| follow_through | DECIMAL(5,2) | NOT NULL | Follow through value |
| combo_duration | DECIMAL(5,2) | NOT NULL | Combo counter duration |
| riven_disposition | DECIMAL(3,2) | NOT NULL | Riven disposition (0.5 to 1.55) |
| polarities | JSON | NULL | Array of mod slot polarities |
| stance_polarity | VARCHAR(20) | NOT NULL | Stance slot polarity |

**Notes:**
- `unique_name` matches API identifier
- Damage split into separate columns for easier queries
- `critical_chance` and `status_chance` stored as decimals (0.25 = 25%)
- `polarities` is JSON array of polarity strings
- Melee has `stance_polarity` instead of `exilus_polarity`

### Mod

| Attribute | Type | Constraints | Description |
|-----------|------|-------------|-------------|
| id | INTEGER | PRIMARY KEY, AUTO_INCREMENT | Unique identifier |
| unique_name | VARCHAR(150) | NOT NULL, UNIQUE | API unique identifier |
| name | VARCHAR(100) | NOT NULL | Mod display name |
| description | TEXT | NULL | Mod description |
| mod_type | VARCHAR(50) | NOT NULL | Type: Warframe, Primary, Secondary, Melee, Companion, Archwing, etc. |
| polarity | VARCHAR(20) | NOT NULL | Mod polarity (Madurai, Vazarin, Naramon, Zenurik, Unairu, Penjaga, Umbra) |
| rarity | VARCHAR(20) | NOT NULL | Common, Uncommon, Rare, Legendary, Primed, Amalgam, Riven |
| base_drain | INTEGER | NOT NULL | Base mod capacity cost |
| max_rank | INTEGER | NOT NULL | Maximum rank (0-10) |
| transmutable | BOOLEAN | NOT NULL, DEFAULT TRUE | Can be transmuted |
| tradable | BOOLEAN | NOT NULL, DEFAULT TRUE | Can be traded |
| fusion_limit | INTEGER | NOT NULL, DEFAULT 0 | Fusion limit for duplicates |

**Notes:**
- `unique_name` matches API identifier
- `base_drain` is the cost at rank 0, increases with rank
- `mod_type` determines which equipment can use this mod
- Riven mods have special handling with weapon-specific stats

### Companion

| Attribute | Type | Constraints | Description |
|-----------|------|-------------|-------------|
| id | INTEGER | PRIMARY KEY, AUTO_INCREMENT | Unique identifier |
| unique_name | VARCHAR(150) | NOT NULL, UNIQUE | API unique identifier |
| name | VARCHAR(100) | NOT NULL | Companion display name |
| description | TEXT | NULL | Companion description |
| companion_type | VARCHAR(50) | NOT NULL | Type: Sentinel, Kubrow, Kavat, MOA, Hound, etc. |
| health | DECIMAL(10,2) | NOT NULL | Base health |
| shield | DECIMAL(10,2) | NOT NULL | Base shield |
| armor | DECIMAL(10,2) | NOT NULL | Base armor |
| mastery_rank | INTEGER | NOT NULL, DEFAULT 0 | Required mastery rank |
| polarities | JSON | NULL | Array of mod slot polarities |

**Notes:**
- `unique_name` matches API identifier
- Stats are base values, scale with rank
- `polarities` is JSON array of polarity strings
- Companions have their own mod slots separate from Warframe

### CompanionAbility

| Attribute | Type | Constraints | Description |
|-----------|------|-------------|-------------|
| id | INTEGER | PRIMARY KEY, AUTO_INCREMENT | Unique identifier |
| companion_id | INTEGER | NOT NULL, FOREIGN KEY (Companion.id) | Reference to Companion |
| name | VARCHAR(100) | NOT NULL | Ability name |
| description | TEXT | NOT NULL | Ability description |

**Notes:**
- Each Companion can have multiple abilities
- Foreign key constraint ensures referential integrity with Companion table

### Build

| Attribute | Type | Constraints | Description |
|-----------|------|-------------|-------------|
| id | INTEGER | PRIMARY KEY, AUTO_INCREMENT | Unique identifier |
| name | VARCHAR(100) | NOT NULL | Build name |
| description | TEXT | NULL | Build description |
| author | VARCHAR(100) | NULL | Build creator |
| created_at | TIMESTAMP | NOT NULL, DEFAULT CURRENT_TIMESTAMP | Creation timestamp |
| updated_at | TIMESTAMP | NOT NULL, DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP | Last update timestamp |
| warframe_id | INTEGER | NOT NULL, FOREIGN KEY (Warframe.id) | Reference to Warframe |
| primary_weapon_id | INTEGER | NULL, FOREIGN KEY (PrimaryWeapon.id) | Reference to Primary Weapon |
| secondary_weapon_id | INTEGER | NULL, FOREIGN KEY (SecondaryWeapon.id) | Reference to Secondary Weapon |
| melee_weapon_id | INTEGER | NULL, FOREIGN KEY (MeleeWeapon.id) | Reference to Melee Weapon |
| companion_id | INTEGER | NULL, FOREIGN KEY (Companion.id) | Reference to Companion |

**Notes:**
- Each build must have exactly 1 Warframe (NOT NULL)
- Weapons are optional (can have 0-3 weapons)
- Companion is optional (0 or 1)
- Timestamps track creation and modification

### BuildMod

| Attribute | Type | Constraints | Description |
|-----------|------|-------------|-------------|
| id | INTEGER | PRIMARY KEY, AUTO_INCREMENT | Unique identifier |
| build_id | INTEGER | NOT NULL, FOREIGN KEY (Build.id) | Reference to Build |
| mod_id | INTEGER | NOT NULL, FOREIGN KEY (Mod.id) | Reference to Mod |
| target_type | VARCHAR(20) | NOT NULL | Target: Warframe, Primary, Secondary, Melee, Companion |
| slot_index | INTEGER | NOT NULL | Mod slot position (0-based) |
| mod_rank | INTEGER | NOT NULL, DEFAULT 0 | Current rank of the mod |

**Notes:**
- Junction table for N:N relationship between Build and Mod
- `target_type` specifies which equipment the mod is applied to
- `slot_index` indicates the position in the mod configuration
- `mod_rank` stores the rank at which the mod is used in this build
- Unique constraint on (build_id, target_type, slot_index)
