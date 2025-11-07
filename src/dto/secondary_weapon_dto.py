from pydantic import BaseModel
from typing import Optional

class SecondaryWeaponDTO(BaseModel):
    id: int
    unique_name: str
    name: str
    description: Optional[str] = None
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
    projectile: Optional[str] = None
    noise: str
    trigger: str
    riven_disposition: float
    polarities: Optional[dict] = None
    exilus_polarity: Optional[str] = None
