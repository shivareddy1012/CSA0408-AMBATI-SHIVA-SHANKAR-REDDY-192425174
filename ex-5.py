# Priority Scheduling (Non-preemptive)

# Step 1: Input number of processes
n = int(input("Enter number of processes: "))

processes = []
burst_time = []
priority = []

# Step 2: Input burst time and priority for each process
for i in range(n):
    bt = int(input(f"Enter Burst Time for Process P{i+1}: "))
    pr = int(input(f"Enter Priority for Process P{i+1} (lower number = higher priority): "))
    processes.append(f"P{i+1}")
    burst_time.append(bt)
    priority.append(pr)

# Step 3: Sort by priority (ascending → highest priority first)
sorted_data = sorted(zip(processes, burst_time, priority), key=lambda x: x[2])
processes, burst_time, priority = zip(*sorted_data)

# Step 4: Initialize WT & TAT
waiting_time = [0] * n
turnaround_time = [0] * n

# Step 5: Compute Waiting Times
for i in range(1, n):
    waiting_time[i] = waiting_time[i-1] + burst_time[i-1]

# Step 6: Compute Turnaround Times
for i in range(n):
    turnaround_time[i] = burst_time[i] + waiting_time[i]

# Step 7: Compute averages
avg_wt = sum(waiting_time) / n
avg_tat = sum(turnaround_time) / n

# Step 8: Print Results
print("\n--- Priority Scheduling (Non-preemptive) ---")
print("Process\tBurst Time\tPriority\tWaiting Time\tTurnaround Time")
for i in range(n):
    print(f"{processes[i]}\t{burst_time[i]}\t\t{priority[i]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")

print(f"\nAverage Waiting Time: {avg_wt:.2f}")
print(f"Average Turnaround Time: {avg_tat:.2f}")
