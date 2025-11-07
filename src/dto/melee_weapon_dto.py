from pydantic import BaseModel
from typing import Optional

class MeleeWeaponDTO(BaseModel):
    id: int
    unique_name: str
    name: str
    description: Optional[str] = None
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
    polarities: Optional[dict] = None
    stance_polarity: str
