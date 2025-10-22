from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, Text, ForeignKey
from src.database.models.base_db_model import Base


class CompanionAbility(Base):
    __tablename__ = "companion_abilities"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    companion_id: Mapped[int] = mapped_column(Integer, ForeignKey("companions.id"), nullable=False)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
