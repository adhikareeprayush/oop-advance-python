# keeps giving the next fibonacci number, never ends on its own
def fibonacci_generator():
    a, b = 0, 1
    while True: 
        yield a # pauses the function and saves it's state (value of a and b) for the next call
        a, b = b, a + b # update a and b for the next fibonacci number


gen = fibonacci_generator()
print("First 8 Fibonacci numbers:")
for _ in range(8):
    print(next(gen), end=" ")
print()
