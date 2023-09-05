import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time} seconds to execute")
        return result
    return wrapper

@measure_time
def long_running_function():
    time.sleep(2)

long_running_function()
# Output: long_running_function took 2.0 seconds to execute
