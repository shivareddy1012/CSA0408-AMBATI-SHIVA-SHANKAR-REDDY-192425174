def optimal_paging(pages, capacity):
    memory = []
    page_faults = 0
    for i in range(len(pages)):
        page = pages[i]
        if page not in memory:
            if len(memory) < capacity:
                memory.append(page)
            else:
                future_uses = []
                for mem_page in memory:
                    if mem_page in pages[i+1:]:
                        future_uses.append(pages[i+1:].index(mem_page))
                    else:
                        future_uses.append(float('inf'))
                index_to_replace = future_uses.index(max(future_uses))
                memory[index_to_replace] = page
            page_faults += 1
        print(f"Memory: {memory}")
    print(f"Total Page Faults: {page_faults}")

pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3]
capacity = 4
optimal_paging(pages, capacity)
