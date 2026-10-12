import time


# decorator that prints how long the function took to run
def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {(end - start)*1000:.2f} ms")
        return result
    return wrapper


# square of every number
@time_it
def calc_square(numbers):
    result = []
    for num in numbers:
        result.append(num * num)
    return result


# cube of every number
@time_it
def calc_cube(numbers):
    result = []
    for num in numbers:
        result.append(num * num * num)
    return result


array = range(1, 100000)
out_square = calc_square(array)
out_cube = calc_cube(array)
