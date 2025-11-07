from pydantic import BaseModel
from typing import Optional


class WarframeDTO(BaseModel):
    id:int
    unique_name:str
    name:str
    description: Optional[str] = None
    health:float
    shield:float
    armor:float
    power:float
    sprint_speed:float
    mastery_rank:int
    polarities:Optional[dict] = None
    aura_polarity:str
    exilus_polarity:Optional[str] = None
    sex:Optional[str] = None
