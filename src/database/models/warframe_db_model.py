from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, JSON, DECIMAL, Text
from src.database.models.base_db_model import Base


class Warframe(Base):
    __tablename__ = "warframes"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    unique_name: Mapped[str] = mapped_column(String(150), unique=True, nullable=False)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    health: Mapped[float] = mapped_column(DECIMAL(10, 2), nullable=False)
    shield: Mapped[float] = mapped_column(DECIMAL(10, 2), nullable=False)
    armor: Mapped[float] = mapped_column(DECIMAL(10, 2), nullable=False)
    power: Mapped[float] = mapped_column(DECIMAL(10, 2), nullable=False)
    sprint_speed: Mapped[float] = mapped_column(DECIMAL(5, 2), nullable=False)
    mastery_rank: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    polarities: Mapped[dict] = mapped_column(JSON, nullable=True)
    aura_polarity: Mapped[str] = mapped_column(String(20), nullable=False)
    exilus_polarity: Mapped[str] = mapped_column(String(20), nullable=True)
    sex: Mapped[str] = mapped_column(String(10), nullable=True)
