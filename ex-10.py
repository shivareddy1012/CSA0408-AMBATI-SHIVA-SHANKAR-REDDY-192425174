from multiprocessing import Process, Value, Event
import time

def writer(shared_val, write_event, read_event):
    for i in range(5):
        shared_val.value = i           # write to shared memory
        print(f"Writer: wrote {i}")
        write_event.set()              # signal reader that value is written
        read_event.wait()              # wait until reader reads
        read_event.clear()
        time.sleep(0.5)                # optional delay

def reader(shared_val, write_event, read_event):
    for _ in range(5):
        write_event.wait()             # wait for writer to write
        print(f"Reader: read {shared_val.value}")
        write_event.clear()
        read_event.set()               # signal writer that value is read

if __name__ == "__main__":
    # Shared memory integer
    shared_value = Value('i', 0)  # 'i' = integer type

    # Events for synchronization
    write_event = Event()
    read_event = Event()

    # Create writer and reader processes
    p1 = Process(target=writer, args=(shared_value, write_event, read_event))
    p2 = Process(target=reader, args=(shared_value, write_event, read_event))

    # Start processes
    p1.start()
    p2.start()

    # Wait for processes to finish
    p1.join()
    p2.join()
