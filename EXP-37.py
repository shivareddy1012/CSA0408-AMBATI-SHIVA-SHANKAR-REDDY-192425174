def fcfs_disk_scheduling(requests, head):
    seek_sequence = []
    seek_count = 0
    current = head
    for request in requests:
        seek_sequence.append(request)
        seek_count += abs(request - current)
        current = request
    print(f"Seek sequence: {seek_sequence}")
    print(f"Total seek operations: {seek_count}")

requests = [82, 170, 43, 140, 24, 16, 190]
head = 50
fcfs_disk_scheduling(requests, head)
