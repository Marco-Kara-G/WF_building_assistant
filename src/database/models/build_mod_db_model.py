from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, ForeignKey, UniqueConstraint
from src.database.models.base_db_model import Base


class BuildMod(Base):
    __tablename__ = "build_mods"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    build_id: Mapped[int] = mapped_column(Integer, ForeignKey("builds.id"), nullable=False)
    mod_id: Mapped[int] = mapped_column(Integer, ForeignKey("mods.id"), nullable=False)
    target_type: Mapped[str] = mapped_column(String(20), nullable=False)
    slot_index: Mapped[int] = mapped_column(Integer, nullable=False)
    mod_rank: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    
    __table_args__ = (
        UniqueConstraint('build_id', 'target_type', 'slot_index', name='uq_build_target_slot'),
    )
