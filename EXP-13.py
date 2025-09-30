def first_fit(block_size, process_size):
    allocation = [-1] * len(process_size)
    blocks = block_size.copy()
    for i, ps in enumerate(process_size):
        for j, bs in enumerate(blocks):
            if bs >= ps:
                allocation[i] = j
                blocks[j] -= ps
                break
    return allocation

def best_fit(block_size, process_size):
    allocation = [-1] * len(process_size)
    blocks = block_size.copy()
    for i, ps in enumerate(process_size):
        best_idx = -1
        for j, bs in enumerate(blocks):
            if bs >= ps:
                if best_idx == -1 or bs < blocks[best_idx]:
                    best_idx = j
        if best_idx != -1:
            allocation[i] = best_idx
            blocks[best_idx] -= ps
    return allocation

def worst_fit(block_size, process_size):
    allocation = [-1] * len(process_size)
    blocks = block_size.copy()
    for i, ps in enumerate(process_size):
        worst_idx = -1
        for j, bs in enumerate(blocks):
            if bs >= ps:
                if worst_idx == -1 or bs > blocks[worst_idx]:
                    worst_idx = j
        if worst_idx != -1:
            allocation[i] = worst_idx
            blocks[worst_idx] -= ps
    return allocation

if __name__ == "__main__":
    block_size = list(map(int, input("Enter memory block sizes (space-separated): ").split()))
    process_size = list(map(int, input("Enter process sizes (space-separated): ").split()))

    ff_alloc = first_fit(block_size, process_size)
    bf_alloc = best_fit(block_size, process_size)
    wf_alloc = worst_fit(block_size, process_size)

    print("\nFirst-Fit Allocation:")
    for i, alloc in enumerate(ff_alloc):
        print(f"Process {i+1} -> Block {alloc if alloc != -1 else 'Not Allocated'}")

    print("\nBest-Fit Allocation:")
    for i, alloc in enumerate(bf_alloc):
        print(f"Process {i+1} -> Block {alloc if alloc != -1 else 'Not Allocated'}")

    print("\nWorst-Fit Allocation:")
    for i, alloc in enumerate(wf_alloc):
        print(f"Process {i+1} -> Block {alloc if alloc != -1 else 'Not Allocated'}")

