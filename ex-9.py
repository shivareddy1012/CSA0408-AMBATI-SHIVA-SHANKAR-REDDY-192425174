from multiprocessing import Process, Value
import time

def writer(shared_val):
    for i in range(5):
        shared_val.value = i  # write to shared memory
        print(f"Writer: wrote {i}")
        time.sleep(1)  # simulate some delay

def reader(shared_val):
    prev = -1
    for _ in range(5):
        while shared_val.value == prev:
            time.sleep(0.1)  # wait for new value
        prev = shared_val.value
        print(f"Reader: read {prev}")

if __name__ == "__main__":
    # Shared memory integer
    shared_value = Value('i', 0)  # 'i' = integer, initial value = 0

    # Create processes
    p1 = Process(target=writer, args=(shared_value,))
    p2 = Process(target=reader, args=(shared_value,))

    # Start processes
    p1.start()
    p2.start()

    # Wait for both to finish
    p1.join()
    p2.join()

