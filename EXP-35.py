class IndexedFile:
    def __init__(self, size):
        self.index_block = []
        self.size = size

disk = ['free'] * 100

def allocate_indexed(file):
    index_block = -1
    for i in range(len(disk)):
        if disk[i] == 'free':
            index_block = i
            break
    if index_block == -1:
        return False
    disk[index_block] = 'index_block'
    blocks_allocated = 0
    for i in range(len(disk)):
        if blocks_allocated == file.size:
            break
        if disk[i] == 'free' and i != index_block:
            disk[i] = 'data_block'
            file.index_block.append(i)
            blocks_allocated += 1
    return blocks_allocated == file.size

file = IndexedFile(5)
print(allocate_indexed(file))
print(f"Index block at {file.index_block}")
