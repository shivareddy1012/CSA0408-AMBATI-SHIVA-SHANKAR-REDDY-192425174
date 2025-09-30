import threading
import time

def thread_function(name):
    for i in range(5):
        print(f"Thread {name} is running: {i}")
        time.sleep(1)

t1 = threading.Thread(target=thread_function, args=("A",))
t2 = threading.Thread(target=thread_function, args=("B",))

t1.start()
t2.start()

t1.join()
t2.join()

print("Multithreading execution completed.")
