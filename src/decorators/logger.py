from typing import Callable,Any
from functools import wraps
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def handle_logger(func:Callable)->Callable:
    @wraps(func)
    def wrapper(*args:Any, **kwargs:Any)-> Any:
        logger.info(f" ::INFO:: Starting {func.__name__}")
        response= func(*args, **kwargs)
        logger.info(f" ::INFO:: Finished {func.__name__}")
        return response
    return wrapper
