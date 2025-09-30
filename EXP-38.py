def scan_disk_scheduling(requests, head, disk_size, direction):
    seek_sequence = []
    seek_count = 0
    left = [r for r in requests if r < head]
    right = [r for r in requests if r >= head]
    left.sort()
    right.sort()
    current = head

    if direction == "left":
        for r in reversed(left):
            seek_sequence.append(r)
            seek_count += abs(current - r)
            current = r
        seek_count += current  # move to start (0)
        current = 0
        for r in right:
            seek_sequence.append(r)
            seek_count += abs(current - r)
            current = r
    else:
        for r in right:
            seek_sequence.append(r)
            seek_count += abs(current - r)
            current = r
        seek_count += (disk_size - 1 - current)
        current = disk_size - 1
        for r in reversed(left):
            seek_sequence.append(r)
            seek_count += abs(current - r)
            current = r

    print(f"Seek sequence: {seek_sequence}")
    print(f"Total seek operations: {seek_count}")

requests = [82, 170, 43, 140, 24, 16, 190]
head = 50
disk_size = 200
scan_disk_scheduling(requests, head, disk_size, "right")

