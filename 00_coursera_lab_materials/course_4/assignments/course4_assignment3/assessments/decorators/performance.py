import time
import functools

def performance(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        return result, elapsed_time
    return wrapper


@performance
def add(a, b):
    return a + b

sum_result, time_taken = add(1, 2)
print(sum_result)
print(time_taken)