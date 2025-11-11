# Standard library
from typing import List
# Third party
import requests
# Local
from src.decorators.exception import handle_exception
from src.decorators.logger import handle_logger
from src.database.db_loader.fetch_entity_names.fetch_entity_names import fetch_entity_names,api_base_url

@handle_logger
@handle_exception
def fetch_entity_data(entity_category:str):
    name_list: List[str] = fetch_entity_names(entity_category)
    for name in name_list:
        url = f"{api_base_url.rstrip('/')}/{entity_category.lstrip('/')}/{name.lstrip('/')}"
        response = requests.get(url, timeout=10)
        data = response.json()
        print(data)



