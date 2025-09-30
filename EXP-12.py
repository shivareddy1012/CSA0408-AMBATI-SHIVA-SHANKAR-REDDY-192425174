import threading
import time

class Philosopher(threading.Thread):
    def __init__(self, name, left_fork, right_fork):
        threading.Thread.__init__(self)
        self.name = name
        self.left_fork = left_fork
        self.right_fork = right_fork

    def run(self):
        for _ in range(3):
            print(f"{self.name} is thinking.")
            time.sleep(1)
            self.dine()

    def dine(self):
        left_acquired = self.left_fork.acquire(timeout=2)
        if left_acquired:
            print(f"{self.name} picked up left fork.")
            right_acquired = self.right_fork.acquire(timeout=2)
            if right_acquired:
                print(f"{self.name} picked up right fork and starts eating.")
                time.sleep(2)
                self.right_fork.release()
                print(f"{self.name} released right fork.")
            self.left_fork.release()
            print(f"{self.name} released left fork.")

if __name__ == "__main__":
    forks = [threading.Lock() for _ in range(5)]
    philosophers = [Philosopher(f"Philosopher {i+1}", forks[i], forks[(i+1)%5]) for i in range(5)]

    for p in philosophers:
        p.start()

    for p in philosophers:
        p.join()

    print("Dining philosophers simulation completed.")
