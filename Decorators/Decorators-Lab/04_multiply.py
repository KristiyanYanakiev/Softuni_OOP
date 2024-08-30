def multiply(time_to_multiply_by: int):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs) * time_to_multiply_by

        return wrapper
    return decorator



@multiply(5)
def add_ten(number):
    return number + 10

print(add_ten(6))