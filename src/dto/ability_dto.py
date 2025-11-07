from pydantic import BaseModel, Field
from typing import Optional

class AbilityDTO(BaseModel):
    id: int
    warframe_id: int
    ability_index: int = Field(ge=1, le=4)
    name: str
    description: str
    energy_cost: Optional[float] = None
    can_helminth: bool
