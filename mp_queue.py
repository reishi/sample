from multiprocessing import Process, Queue
import time
import queue
import sys

def worker(id, queue):
    while True:
        try:
            obj = queue.get(timeout=3)
            print(id, obj)
        except:
            break

if __name__ == '__main__':
    queue = Queue()

    workers = []
    for id in range(4):
        p = Process(target=worker, args=(id, queue))
        p.start()
        workers.append(p)

    for line in sys.stdin:
        queue.put(line.rstrip())

    for p in workers:
        p.join()
