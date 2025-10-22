import os
from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context

from dotenv import load_dotenv

from src.database.models.base_db_model import Base
from src.database.models.warframe_db_model import Warframe
from src.database.models.mod_db_model import Mod
from src.database.models.companion_db_model import Companion
from src.database.models.companion_ability_db_model import CompanionAbility
from src.database.models.build_db_model import Build
from src.database.models.build_mod_db_model import BuildMod
from src.database.models.melee_weapon_db_model import  MeleeWeapon
from src.database.models.primary_weapon_db_model import PrimaryWeapon
from src.database.models.secondary_weapon_db_model import SecondaryWeapon
from src.database.models.ability_db_model import Ability
from src.database.models.passive_ability_db_model import PassiveAbility


load_dotenv()

config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)


target_metadata = Base.metadata

DB_NAME:str= os.getenv("DB_NAME")
DB_USER:str= os.getenv("DB_USER")
DB_PASSWORD:str= os.getenv("DB_PASSWORD")
DB_HOST:str= os.getenv("DB_HOST")
DB_PORT:str= os.getenv("DB_PORT")
DB_DIALECT:str= os.getenv("DB_DIALECT")

print("##########")
print(f"DB_NAME: {DB_NAME}")
print(f"DB_USER: {DB_USER}")
print(f"DB_HOST: {DB_HOST}")
print(f"DB_PORT: {DB_PORT}")
print(f"DB_DIALECT: {DB_DIALECT}")
print("##########")

if DB_USER and DB_PASSWORD and DB_HOST and DB_PORT and DB_DIALECT and DB_NAME:
    config.set_main_option("sqlalchemy.url", f"{DB_DIALECT}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
else:
    raise ValueError("Missing environment variables")


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
