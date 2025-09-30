import threading
import time
import random

buffer = []
buffer_size = 5

empty = threading.Semaphore(buffer_size)
full = threading.Semaphore(0)
mutex = threading.Semaphore(1)

def producer():
    while True:
        item = random.randint(1, 100)
        empty.acquire()
        mutex.acquire()
        buffer.append(item)
        print(f"Produced: {item}")
        mutex.release()
        full.release()
        time.sleep(random.uniform(0.5, 1.5))

def consumer():
    while True:
        full.acquire()
        mutex.acquire()
        item = buffer.pop(0)
        print(f"Consumed: {item}")
        mutex.release()
        empty.release()
        time.sleep(random.uniform(0.5, 1.5))

producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

producer_thread.start()
consumer_thread.start()

producer_thread.join()
consumer_thread.join()
