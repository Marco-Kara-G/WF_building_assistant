from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, Text, Boolean
from src.database.models.base_db_model import Base


class Mod(Base):
    __tablename__ = "mods"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    unique_name: Mapped[str] = mapped_column(String(150), unique=True, nullable=False)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    mod_type: Mapped[str] = mapped_column(String(50), nullable=False)
    polarity: Mapped[str] = mapped_column(String(20), nullable=False)
    rarity: Mapped[str] = mapped_column(String(20), nullable=False)
    base_drain: Mapped[int] = mapped_column(Integer, nullable=False)
    max_rank: Mapped[int] = mapped_column(Integer, nullable=False)
    transmutable: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    tradable: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    fusion_limit: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
