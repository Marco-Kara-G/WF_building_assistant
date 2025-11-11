# Standard Library
from typing import List
# Local
from src.database.db_loader.fetch_entity_data.fetch_entity_data import fetch_entity_data
from src.decorators.exception import handle_exception
from src.decorators.logger import handle_logger
import src.dto


@handle_logger
@handle_exception
def load_data(entity):
    entity_types = set()
    for dto_name in src.dto.__all__:
        entity_type = dto_name.replace("DTO", "").lower()
        if entity_type.endswith("weapon"):
            entity_type = "weapon"
        entity_types.add(entity_type + "s")

    entity_type_list = sorted(entity_types)
    print(entity_type_list)


load_data("Warframes")