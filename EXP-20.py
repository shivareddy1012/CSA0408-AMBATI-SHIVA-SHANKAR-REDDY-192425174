import threading
import time
import random

readcount = 0
readcount_mutex = threading.Semaphore(1)
resource_access = threading.Semaphore(1)

def reader(reader_id):
    global readcount
    while True:
        readcount_mutex.acquire()
        readcount += 1
        if readcount == 1:
            resource_access.acquire()
        readcount_mutex.release()
        print(f"Reader {reader_id} is reading")
        time.sleep(random.uniform(0.5, 1.5))
        readcount_mutex.acquire()
        readcount -= 1
        if readcount == 0:
            resource_access.release()
        readcount_mutex.release()
        time.sleep(random.uniform(0.5, 1.5))

def writer(writer_id):
    while True:
        resource_access.acquire()
        print(f"Writer {writer_id} is writing")
        time.sleep(random.uniform(1, 2))
        resource_access.release()
        time.sleep(random.uniform(1, 2))

readers = [threading.Thread(target=reader, args=(i,)) for i in range(3)]
writers = [threading.Thread(target=writer, args=(i,)) for i in range(2)]

for r in readers:
    r.start()
for w in writers:
    w.start()

for r in readers:
    r.join()
for w in writers:
    w.join()
