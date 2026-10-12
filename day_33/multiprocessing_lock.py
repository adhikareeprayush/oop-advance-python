import time
import multiprocessing


# adds 1 to balance 100 times, lock stops the other process changing it at the same time
def deposit(balance, lock):
    for _ in range(100):
        time.sleep(0.001)
        lock.acquire()
        balance.value = balance.value + 1
        lock.release()


# takes 1 from balance 100 times using the same lock
def withdraw(balance, lock):
    for _ in range(100):
        time.sleep(0.001)
        lock.acquire()
        balance.value = balance.value - 1
        lock.release()


if __name__ == "__main__":
    balance = multiprocessing.Value('i', 200)
    lock = multiprocessing.Lock()

    p1 = multiprocessing.Process(target=deposit, args=(balance, lock))
    p2 = multiprocessing.Process(target=withdraw, args=(balance, lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Final Balance (Synchronized with Lock):", balance.value)
