from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class BuildDTO(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    author: Optional[str] = None
    created_at: datetime
    updated_at: datetime
    warframe_id: int
    primary_weapon_id: Optional[int] = None
    secondary_weapon_id: Optional[int] = None
    melee_weapon_id: Optional[int] = None
    companion_id: Optional[int] = None
