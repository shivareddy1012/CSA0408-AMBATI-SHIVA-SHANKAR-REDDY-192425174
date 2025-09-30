def is_safe(processes, available, max_demand, allocation):
    n = len(processes)
    m = len(available)
    need = [[max_demand[i][j] - allocation[i][j] for j in range(m)] for i in range(n)]
    finish = [False] * n
    safe_sequence = []
    work = available.copy()
    while len(safe_sequence) < n:
        found = False
        for i in range(n):
            if not finish[i] and all(need[i][j] <= work[j] for j in range(m)):
                for j in range(m):
                    work[j] += allocation[i][j]
                safe_sequence.append(processes[i])
                finish[i] = True
                found = True
        if not found:
            return False, []
    return True, safe_sequence

processes = [0, 1, 2, 3, 4]
available = [3, 3, 2]
max_demand = [
    [7, 5, 3],
    [3, 2, 2],
    [9, 0, 2],
    [2, 2, 2],
    [4, 3, 3]
]
allocation = [
    [0, 1, 0],
    [2, 0, 0],
    [3, 0, 2],
    [2, 1, 1],
    [0, 0, 2]
]

safe, sequence = is_safe(processes, available, max_demand, allocation)
if safe:
    print("The system is in a safe state.")
    print("Safe sequence:", sequence)
else:
    print("The system is NOT in a safe state. Deadlock possible.")
