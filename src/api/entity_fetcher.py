# Standard library
import os
from typing import List

# Third party
import requests
from dotenv import load_dotenv

# Local
from src.decorators.exception import handle_exception
from src.decorators.logger import handle_logger

load_dotenv()

api_base_url: str = os.getenv("API_BASE_URL")
if not api_base_url:
    raise ValueError("API_BASE_URL non configurato nel file .env")


@handle_logger
@handle_exception
def fetch_entity_names(entity_file: str) -> List[str]:
    """
    Recupera i nomi delle entità da un file JSON dell'API WFCD.
    
    Args:
        entity_file: Nome del file JSON (es. "Primary.json", "Warframes.json")
        
    Returns:
        Lista dei nomi delle entità
    """
    url = f"{api_base_url.rstrip('/')}/{entity_file.lstrip('/')}"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return [item["name"] for item in response.json() if "name" in item]


print(fetch_entity_names("Warframes.json"))