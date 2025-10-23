from functools import wraps
import logging
from typing import Callable, Any
import requests


logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)

def handle_exception(func:Callable)-> Callable:
    @wraps(func)
    def wrapper(*args:Any, **kwargs:Any)->Any:
        try:
            return func(*args, **kwargs)
        except (ValueError, KeyError, TypeError) as e :
            logger.error(f"::ERROR:: Busines error in {func.__name__}: {str(e)}")
            raise
        except (ConnectionError, TimeoutError, FileNotFoundError, requests.HTTPError) as e :
            logger.error(f"::ERROR:: Infrastructure error in {func.__name__}: {str(e)}")
            raise
        except (AttributeError,IndexError) as e :
            logger.error(f"::ERROR:: Unexpected error in {func.__name__}: {str(e)}")
            raise
        except Exception as e :
            logger.error(f"::ERROR:: Unkwown error in {func.__name__ }")
            raise
    return wrapper
