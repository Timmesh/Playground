def log_args(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with arguments {args} and keyword arguments {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@log_args
def add(a, b):
    return a + b

print(add(10, 5))

# Output: Calling add with arguments (10, 5) and keyword arguments {}
#         Result: 15
