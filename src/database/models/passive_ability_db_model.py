from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, Text, ForeignKey
from src.database.models.base_db_model import Base


class PassiveAbility(Base):
    __tablename__ = "passive_abilities"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    warframe_id: Mapped[int] = mapped_column(Integer, ForeignKey("warframes.id"), unique=True, nullable=False)
    name: Mapped[str] = mapped_column(String(100), nullable=True)
    description: Mapped[str] = mapped_column(Text, nullable=False)
