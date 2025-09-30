import os
import multiprocessing

print("\n--- Parent Process ---")
print("Parent PID: ", os.getpid())

def child_process():
    print("\n--- Child Process ---")
    print("Child PID: ", os.getpid())
    print("Parent PID: ", os.getppid())

p = multiprocessing.Process(target=child_process)
p.start()

print("Child PID (from parent):", p.pid)
p.join()
