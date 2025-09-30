# Round Robin Scheduling Algorithm

# Input number of processes
n = int(input("Enter number of processes: "))

processes = []
AT = []   # Arrival Time
BT = []   # Burst Time

for i in range(n):
    at = int(input(f"Enter Arrival Time for Process P{i+1}: "))
    bt = int(input(f"Enter Burst Time for Process P{i+1}: "))
    processes.append(f"P{i+1}")
    AT.append(at)
    BT.append(bt)

# Time Quantum
quantum = int(input("Enter Time Quantum: "))

# Initialize
remaining_BT = BT[:]   # Copy burst times
WT = [0] * n           # Waiting Time
TAT = [0] * n          # Turnaround Time
CT = [0] * n           # Completion Time
time = 0
queue = []             # Ready Queue
gantt = []             # Gantt Chart

# Process indices sorted by arrival time
process_indices = list(range(n))
process_indices.sort(key=lambda i: AT[i])

# Start with first process if it has arrived
while True:
    done = True
    for i in process_indices:
        if remaining_BT[i] > 0 and AT[i] <= time:
            done = False
            # Execute process for time quantum or remaining burst
            exec_time = min(quantum, remaining_BT[i])
            gantt.append((processes[i], time, time + exec_time))
            time += exec_time
            remaining_BT[i] -= exec_time
            if remaining_BT[i] == 0:
                CT[i] = time
                TAT[i] = CT[i] - AT[i]
                WT[i] = TAT[i] - BT[i]
    if done:
        break
    # If CPU idle (no process has arrived yet)
    if all(AT[i] > time or remaining_BT[i] == 0 for i in process_indices):
        gantt.append(("Idle", time, time + 1))
        time += 1

# Calculate averages
avg_wt = sum(WT) / n
avg_tat = sum(TAT) / n

# Print Gantt Chart
print("\nGantt Chart:")
for p, start, end in gantt:
    print(f"| {p} ({start}-{end}) ", end="")
print("|")

# Print process table
print("\n--- Round Robin Scheduling ---")
print("Process\tAT\tBT\tCT\tTAT\tWT")
for i in range(n):
    print(f"{processes[i]}\t{AT[i]}\t{BT[i]}\t{CT[i]}\t{TAT[i]}\t{WT[i]}")

print(f"\nAverage Waiting Time: {avg_wt:.2f}")
print(f"Average Turnaround Time: {avg_tat:.2f}")
