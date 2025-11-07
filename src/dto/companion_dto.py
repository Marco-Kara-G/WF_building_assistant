from pydantic import BaseModel
from typing import Optional

class CompanionDTO(BaseModel):
    id: int
    unique_name: str
    name: str
    description: Optional[str] = None
    companion_type: str
    health: float
    shield: float
    armor: float
    mastery_rank: int
    polarities: Optional[dict] = None
