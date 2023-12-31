# logcall.py
from functools import wraps

def logged(func):
    print('Adding logging to', func.__name__)
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Calling', func.__name__)
        return func(*args, **kwargs)
    return wrapper

def logformat(message):
    def logged_msg(func):
        print('Adding logging to', func.__name__)
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(message.format(func=func))
            return func(*args, **kwargs)
        return wrapper
    return logged_msg

#logged = logformat('{func.__code__.co_filename}:{func.__name__}')