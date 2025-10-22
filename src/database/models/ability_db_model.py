from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, DECIMAL, Text, ForeignKey, Boolean, CheckConstraint, UniqueConstraint
from src.database.models.base_db_model import Base


class Ability(Base):
    __tablename__ = "abilities"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    warframe_id: Mapped[int] = mapped_column(Integer, ForeignKey("warframes.id"), nullable=False)
    ability_index: Mapped[int] = mapped_column(Integer, nullable=False)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    energy_cost: Mapped[float] = mapped_column(DECIMAL(5, 2), nullable=True)
    can_helminth: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    
    __table_args__ = (
        CheckConstraint('ability_index >= 1 AND ability_index <= 4', name='check_ability_index'),
        UniqueConstraint('warframe_id', 'ability_index', name='uq_warframe_ability'),
    )
