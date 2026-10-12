import multiprocessing


# puts the square of each number in the queue for the main process
def calc_square(numbers, q):
    for n in numbers:
        q.put(n * n)


if __name__ == "__main__":
    numbers = [2, 3, 5]
    q = multiprocessing.Queue()

    p = multiprocessing.Process(target=calc_square, args=(numbers, q))
    p.start()
    p.join()

    print("Items retrieved from Multiprocessing Queue:")
    while not q.empty():
        print(q.get())
