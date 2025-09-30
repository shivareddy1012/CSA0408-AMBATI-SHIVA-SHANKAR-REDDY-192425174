class LinkedFileBlock:
    def __init__(self, block_num):
        self.block_num = block_num
        self.next = None

disk = ['free'] * 100

def allocate_linked(size):
    head = None
    prev = None
    allocated = 0
    for i in range(len(disk)):
        if allocated == size:
            break
        if disk[i] == 'free':
            disk[i] = 'allocated'
            node = LinkedFileBlock(i)
            if not head:
                head = node
            if prev:
                prev.next = node
            prev = node
            allocated += 1
    return head

head_block = allocate_linked(5)
current = head_block
while current:
    print(f"Block {current.block_num}")
    current = current.next

