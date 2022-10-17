import math
import time


def timer(func):
    def inner(*arg, **kargs):
        print("Time start")
        start = time.time()
        func(*arg, **kargs)
        end = time.time()
        print(f"Time end. Total time taken {end-start}")
    return inner


@timer
def get_factorial(n):
    result = math.factorial(n)
    print(f'factorial of {n} is {result}')


# timer(get_factorial)()

get_factorial(100)


