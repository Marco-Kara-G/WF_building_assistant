# Third Party Library
from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import sessionmaker, Session

# Local
from src.database.db_config.db_config import DBconfig,get_db_config


class DBconnection:
    _connection_string:str
    _config:DBconfig
    _engine: Engine

    def __init__(self):
        self._config = get_db_config()
        self._connection_string = f"{self._config.dialect}://{self._config.user}:{self._config.password}@{self._config.host}:{self._config.port}/{self._config.database}"
        self._engine = create_engine(self._connection_string, pool_size=20)
        self._session: sessionmaker[Session] = sessionmaker(bind=self._engine)

    def get_session(self) -> Session:
        return self._session()
