from functools import wraps
import logging
from typing import Callable, Any

logger = logging.getLogger(__name__)
def handle_exception(exceptions=(Exception,)):
    def decorator(func:Callable)-> Callable:
        @wraps(func)
        def wrapper(*args:Any, **kwargs:Any)->Any:
            try:
                return func(*args, **kwargs)
            except exceptions as e:
                logger.error(f"Error in {func.__name__}: {e}", exc_info=True)
                raise
        return wrapper
    return decorator