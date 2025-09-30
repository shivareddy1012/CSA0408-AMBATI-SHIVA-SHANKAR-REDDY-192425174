class File:
    def __init__(self, start_block, length):
        self.start_block = start_block
        self.length = length

disk = ['free'] * 100

def allocate(file):
    for i in range(len(disk) - file.length + 1):
        if all(disk[j] == 'free' for j in range(i, i + file.length)):
            for j in range(i, i + file.length):
                disk[j] = 'allocated'
            file.start_block = i
            return True
    return False

file1 = File(-1, 10)
print(allocate(file1))
print(f"File allocated at block {file1.start_block}")
