import threading
import time

mutex = threading.Lock()
shared_resource = 0

def synchronized_task(name):
    global shared_resource
    for _ in range(5):
        mutex.acquire()
        temp = shared_resource
        temp += 1
        time.sleep(0.1)
        shared_resource = temp
        print(f"{name} updated shared_resource to {shared_resource}")
        mutex.release()
        time.sleep(0.1)

t1 = threading.Thread(target=synchronized_task, args=("Thread-1",))
t2 = threading.Thread(target=synchronized_task, args=("Thread-2",))

t1.start()
t2.start()

t1.join()
t2.join()

print(f"Final value of shared_resource: {shared_resource}")
