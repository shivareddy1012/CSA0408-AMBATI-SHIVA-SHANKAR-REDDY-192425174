def cscan_disk_scheduling(requests, head, disk_size):
    seek_sequence = []
    seek_count = 0
    left = [r for r in requests if r < head]
    right = [r for r in requests if r >= head]
    left.sort()
    right.sort()
    current = head

    for r in right:
        seek_sequence.append(r)
        seek_count += abs(current - r)
        current = r
    seek_count += abs(current - (disk_size - 1))
    current = 0
    seek_count += disk_size - 1
    for r in left:
        seek_sequence.append(r)
        seek_count += abs(current - r)
        current = r

    print(f"Seek sequence: {seek_sequence}")
    print(f"Total seek operations: {seek_count}")

requests = [82, 170, 43, 140, 24, 16, 190]
head = 50
disk_size = 200
cscan_disk_scheduling(requests, head, disk_size)
