import threading
import time

def thread_func(name):
    print(f"Thread {name} started")
    time.sleep(1)
    print(f"Thread {name} exiting")
    return  # thread exits here naturally

t1 = threading.Thread(target=thread_func, args=('A',))
t2 = threading.Thread(target=thread_func, args=('B',))

t1.start()
t2.start()

t1.join()
t2.join()

print(f"Threads t1 and t2 are {'equal' if t1 == t2 else 'not equal'}")
