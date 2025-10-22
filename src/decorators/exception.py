
def handle_exception(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            print(f"ValueError occurred: {e}")
            return None
        except TypeError as e:
            print(f"TypeError occurred: {e}")
            return None
        except AttributeError as e:
            print(f"AttributeError occurred: {e}")
            return None
        except KeyError as e:
            print(f"KeyError occurred: {e}")
            return None
        except IndexError as e:
            print(f"IndexError occurred: {e}")
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
    return wrapper