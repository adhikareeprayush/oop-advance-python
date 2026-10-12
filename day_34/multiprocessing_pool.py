import time
from multiprocessing import Pool


# some cpu heavy work so the pool has something to split up
def f(n):
    sum_val = 0
    for x in range(1000):
        sum_val += x * x
    return sum_val


if __name__ == "__main__":
    t1 = time.time()
    p = Pool()
    result = p.map(f, range(10000))
    p.close()
    p.join()
    print("Pool map processing time:", time.time() - t1, "seconds")
