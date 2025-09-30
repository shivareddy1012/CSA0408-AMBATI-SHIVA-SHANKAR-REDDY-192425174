# Non-Preemptive Shortest Job First (SJF) Scheduling

n = int(input("Enter number of processes: "))

processes = []
arrival_time = []
burst_time = []

# Input process details
for i in range(n):
    at = int(input(f"Enter Arrival Time for Process P{i+1}: "))
    bt = int(input(f"Enter Burst Time for Process P{i+1}: "))
    processes.append(f"P{i+1}")
    arrival_time.append(at)
    burst_time.append(bt)

# Initialize values
completion_time = [0] * n
waiting_time = [0] * n
turnaround_time = [0] * n
is_completed = [False] * n

time = 0
completed = 0

print("\nGantt Chart (Execution Order):")

# Loop until all processes complete
while completed != n:
    idx = -1
    min_bt = float('inf')

    # Select the process with shortest burst time among arrived ones
    for i in range(n):
        if arrival_time[i] <= time and not is_completed[i]:
            if burst_time[i] < min_bt:
                min_bt = burst_time[i]
                idx = i

    if idx != -1:
        # Run the process
        print(f"| {processes[idx]} ", end="")
        time += burst_time[idx]
        completion_time[idx] = time
        turnaround_time[idx] = completion_time[idx] - arrival_time[idx]
        waiting_time[idx] = turnaround_time[idx] - burst_time[idx]
        is_completed[idx] = True
        completed += 1
    else:
        # If no process is ready, CPU idle
        print("| Idle ", end="")
        time += 1

print("|")

# Calculate averages
avg_wt = sum(waiting_time) / n
avg_tat = sum(turnaround_time) / n

# Print results
print("\n--- Non-Preemptive Shortest Job First (SJF) ---")
print("Process\tAT\tBT\tCT\tTAT\tWT")
for i in range(n):
    print(f"{processes[i]}\t{arrival_time[i]}\t{burst_time[i]}\t{completion_time[i]}\t{turnaround_time[i]}\t{waiting_time[i]}")

print(f"\nAverage Waiting Time: {avg_wt:.2f}")
print(f"Average Turnaround Time: {avg_tat:.2f}")
