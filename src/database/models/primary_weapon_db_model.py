from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, DECIMAL, Text, JSON
from src.database.models.base_db_model import Base


class PrimaryWeapon(Base):
    __tablename__ = "primary_weapons"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    unique_name: Mapped[str] = mapped_column(String(150), unique=True, nullable=False)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    weapon_type: Mapped[str] = mapped_column(String(50), nullable=False)
    mastery_rank: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    impact_damage: Mapped[float] = mapped_column(DECIMAL(10, 2), nullable=False, default=0)
    puncture_damage: Mapped[float] = mapped_column(DECIMAL(10, 2), nullable=False, default=0)
    slash_damage: Mapped[float] = mapped_column(DECIMAL(10, 2), nullable=False, default=0)
    fire_rate: Mapped[float] = mapped_column(DECIMAL(5, 2), nullable=False)
    critical_chance: Mapped[float] = mapped_column(DECIMAL(5, 4), nullable=False)
    critical_multiplier: Mapped[float] = mapped_column(DECIMAL(5, 2), nullable=False)
    status_chance: Mapped[float] = mapped_column(DECIMAL(5, 4), nullable=False)
    accuracy: Mapped[float] = mapped_column(DECIMAL(5, 2), nullable=False)
    magazine_size: Mapped[int] = mapped_column(Integer, nullable=False)
    max_ammo: Mapped[int] = mapped_column(Integer, nullable=False)
    reload_time: Mapped[float] = mapped_column(DECIMAL(5, 2), nullable=False)
    projectile: Mapped[str] = mapped_column(String(50), nullable=True)
    noise: Mapped[str] = mapped_column(String(20), nullable=False)
    trigger: Mapped[str] = mapped_column(String(50), nullable=False)
    riven_disposition: Mapped[float] = mapped_column(DECIMAL(3, 2), nullable=False)
    polarities: Mapped[dict] = mapped_column(JSON, nullable=True)
    exilus_polarity: Mapped[str] = mapped_column(String(20), nullable=True)
