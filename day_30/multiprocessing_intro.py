import time
import multiprocessing


# prints square of each number, runs in its own process
def calc_square(numbers):
    for n in numbers:
        print("Square:", n * n)


# prints cube of each number, runs in its own process
def calc_cube(numbers):
    for n in numbers:
        print("Cube:", n * n * n)


if __name__ == "__main__":
    arr = [2, 3, 8]
    p1 = multiprocessing.Process(target=calc_square, args=(arr,))
    p2 = multiprocessing.Process(target=calc_cube, args=(arr,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Multiprocessing execution completed successfully!")
