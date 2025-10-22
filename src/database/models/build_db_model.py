from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, Text, ForeignKey, TIMESTAMP, func
from src.database.models.base_db_model import Base
from datetime import datetime


class Build(Base):
    __tablename__ = "builds"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    author: Mapped[str] = mapped_column(String(100), nullable=True)
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP, nullable=False, server_default=func.current_timestamp())
    updated_at: Mapped[datetime] = mapped_column(TIMESTAMP, nullable=False, server_default=func.current_timestamp(), onupdate=func.current_timestamp())
    warframe_id: Mapped[int] = mapped_column(Integer, ForeignKey("warframes.id"), nullable=False)
    primary_weapon_id: Mapped[int] = mapped_column(Integer, ForeignKey("primary_weapons.id"), nullable=True)
    secondary_weapon_id: Mapped[int] = mapped_column(Integer, ForeignKey("secondary_weapons.id"), nullable=True)
    melee_weapon_id: Mapped[int] = mapped_column(Integer, ForeignKey("melee_weapons.id"), nullable=True)
    companion_id: Mapped[int] = mapped_column(Integer, ForeignKey("companions.id"), nullable=True)
