def best_fit(block_size, process_size):
    allocation = [-1] * len(process_size)
    for i in range(len(process_size)):
        best_idx = -1
        for j in range(len(block_size)):
            if block_size[j] >= process_size[i]:
                if best_idx == -1 or block_size[j] < block_size[best_idx]:
                    best_idx = j
        if best_idx != -1:
            allocation[i] = best_idx
            block_size[best_idx] -= process_size[i]
    for i in range(len(process_size)):
        print(f"Process {i + 1} of size {process_size[i]}", end=" -> ")
        if allocation[i] != -1:
            print(f"allocated to block {allocation[i] + 1}")
        else:
            print("not allocated")

block_size = [100, 500, 200, 300, 600]
process_size = [212, 417, 112, 426]

best_fit(block_size, process_size)
