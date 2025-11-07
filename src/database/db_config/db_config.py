# Standard lybrary
import os
# Third Party Library
from dotenv import load_dotenv
from pydantic import BaseModel


load_dotenv()

class DBconfig(BaseModel):
    host: str
    port: str
    user: str
    password: str
    database: str
    dialect:str

def get_db_config() -> DBconfig:
    return DBconfig(
        host= os.getenv("DB_HOST"),
        port= os.getenv("DB_PORT"),
        user= os.getenv("DB_USER"),
        password= os.getenv("DB_PASSWORD"),
        database= os.getenv("DB_NAME"),
        dialect= os.getenv("DB_DIALECT")
    )

