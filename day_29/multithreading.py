import time
import threading


# prints square of each number, sleep is there to act like slow io
def calc_square(numbers):
    print("Calculate square numbers")
    for n in numbers:
        time.sleep(0.1)
        print("Square:", n * n)


# same thing but cubes
def calc_cube(numbers):
    print("Calculate cube numbers")
    for n in numbers:
        time.sleep(0.1)
        print("Cube:", n * n * n)


arr = [2, 3, 8, 9]

t1 = threading.Thread(target=calc_square, args=(arr,))
t2 = threading.Thread(target=calc_cube, args=(arr,))

t1.start()
t2.start()

t1.join()
t2.join()

print("Multithreading execution completed!")
