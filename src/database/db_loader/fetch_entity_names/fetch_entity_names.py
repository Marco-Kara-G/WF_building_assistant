# Standard library
import os
from typing import List, Set
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
def fetch_entity_names(entity_category: str) -> List[str]:
    """
    Recupera i nomi delle entità dall'API Warframe.

    Args:
        entity_category: Categoria dell'entità (es. "Warframes", "Primary", "Mods")

    Returns:
        Lista dei nomi delle entità
    """
    weapon_categories = {"Primary", "Secondary", "Melee", "Arch-Gun", "Arch-Melee"}
    
    if entity_category in weapon_categories:
        url = f"{api_base_url.rstrip('/')}/weapons/"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        return [item["name"] for item in data if item.get("category") == entity_category]
    elif entity_category == "Mods":
        url = f"{api_base_url.rstrip('/')}/mods/"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        return [item["name"] for item in data]
    else:
        url = f"{api_base_url.rstrip('/')}/items/"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        return [item["name"] for item in data if item.get("category") == entity_category]