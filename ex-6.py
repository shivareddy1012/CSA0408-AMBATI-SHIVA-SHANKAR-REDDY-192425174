# Preemptive Priority Scheduling in Python

n = int(input("Enter number of processes: "))

processes = []
arrival_time = []
burst_time = []
priority = []

# Input process details
for i in range(n):
    at = int(input(f"Enter Arrival Time for Process P{i+1}: "))
    bt = int(input(f"Enter Burst Time for Process P{i+1}: "))
    pr = int(input(f"Enter Priority for Process P{i+1} (lower = higher priority): "))
    processes.append(f"P{i+1}")
    arrival_time.append(at)
    burst_time.append(bt)
    priority.append(pr)

# Make copies for later calculations
remaining_bt = burst_time.copy()
completion_time = [0] * n
waiting_time = [0] * n
turnaround_time = [0] * n

time = 0
completed = 0

print("\nGantt Chart (Execution Order):")

while completed != n:
    # Select process with highest priority among those that arrived
    idx = -1
    min_priority = float('inf')
    for i in range(n):
        if arrival_time[i] <= time and remaining_bt[i] > 0:
            if priority[i] < min_priority:
                min_priority = priority[i]
                idx = i

    if idx != -1:
        # Execute process for 1 unit of time
        print(f"| {processes[idx]} ", end="")
        remaining_bt[idx] -= 1
        time += 1

        # If process completes
        if remaining_bt[idx] == 0:
            completed += 1
            completion_time[idx] = time
    else:
        # No process is ready, idle time
        print("| Idle ", end="")
        time += 1

print("|")

# Calculate TAT and WT
for i in range(n):
    turnaround_time[i] = completion_time[i] - arrival_time[i]
    waiting_time[i] = turnaround_time[i] - burst_time[i]

# Averages
avg_wt = sum(waiting_time) / n
avg_tat = sum(turnaround_time) / n

# Print results
print("\n--- Preemptive Priority Scheduling ---")
print("Process\tAT\tBT\tPR\tCT\tTAT\tWT")
for i in range(n):
    print(f"{processes[i]}\t{arrival_time[i]}\t{burst_time[i]}\t{priority[i]}\t{completion_time[i]}\t{turnaround_time[i]}\t{waiting_time[i]}")

print(f"\nAverage Waiting Time: {avg_wt:.2f}")
print(f"Average Turnaround Time: {avg_tat:.2f}")
