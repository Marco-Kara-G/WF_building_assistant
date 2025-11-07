from pydantic import BaseModel
from typing import Optional

class ModDTO(BaseModel):
    id: int
    unique_name: str
    name: str
    description: Optional[str] = None
    mod_type: str
    polarity: str
    rarity: str
    base_drain: int
    max_rank: int
    transmutable: bool
    tradable: bool
    fusion_limit: int
