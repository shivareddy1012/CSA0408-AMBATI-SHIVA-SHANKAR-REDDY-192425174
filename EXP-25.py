import os

fd = os.open('testfile.txt', os.O_CREAT | os.O_RDWR)
os.write(fd, b'Testing I/O system calls.')
os.lseek(fd, 0, os.SEEK_SET)
content = os.read(fd, 100)
print(content.decode())

stat_info = os.stat('testfile.txt')
print(stat_info)

entries = os.listdir('.')  # safer for directory listing
for entry in entries:
    print(entry)

os.close(fd)
