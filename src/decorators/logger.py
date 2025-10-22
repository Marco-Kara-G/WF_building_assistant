
def handle_logger(func):
    def wrapper(*args, **kwargs):
        print(f"Starting {func.__name__}")
        response= func(*args, **kwargs)
        print(f"Finished {func.__name__}")
        return response
    return wrapper()
