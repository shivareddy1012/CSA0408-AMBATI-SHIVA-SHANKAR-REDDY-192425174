 
n = int(input("Enter number of processes: "))

processes = []
burst_time = []

 
for i in range(n):
    bt = int(input(f"Enter Burst Time for Process P{i+1}: "))
    processes.append(f"P{i+1}")
    burst_time.append(bt)

 
waiting_time = [0] * n
turnaround_time = [0] * n

 
for i in range(1, n):
    waiting_time[i] = waiting_time[i-1] + burst_time[i-1]

 
for i in range(n):
    turnaround_time[i] = burst_time[i] + waiting_time[i]

 
avg_wt = sum(waiting_time) / n
avg_tat = sum(turnaround_time) / n

 
print("\n--- First Come First Served (FCFS) Scheduling ---")
print("Process\tBurst Time\tWaiting Time\tTurnaround Time")
for i in range(n):
    print(f"{processes[i]}\t{burst_time[i]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")

print(f"\nAverage Waiting Time: {avg_wt:.2f}")
print(f"Average Turnaround Time: {avg_tat:.2f}")
