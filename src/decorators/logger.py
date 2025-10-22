from typing import Callable,Any
from functools import wraps
import logging

logger = logging.getLogger(__name__)

def handle_logger(func:Callable)->Callable:
    @wraps(func)
    def wrapper(*args:Any, **kwargs:Any)-> Any:
        logger.info(f"Starting {func.__name__}")
        response= func(*args, **kwargs)
        logger.info(f"Finished {func.__name__}")
        return response
    return wrapper
