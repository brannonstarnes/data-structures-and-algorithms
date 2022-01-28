from functools import wraps
import timeit


def func_duration(func):
    """Returns the time, in seconds, it takes to exectute a given function 1 times."""
    @wraps(func)
    def wrapper(*args, **kwargs, ):
        duration = timeit.timeit(stmt=f"{func(*args, **kwargs)}",
                                 setup ='pass',
                                 number = 1)
        return duration
    return wrapper



