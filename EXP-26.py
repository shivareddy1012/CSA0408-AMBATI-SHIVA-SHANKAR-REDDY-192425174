import os

filename = 'file.txt'
fd = os.open(filename, os.O_CREAT | os.O_RDWR)
os.write(fd, b'File management operations.')
os.lseek(fd, 0, os.SEEK_SET)
print(os.read(fd, 100).decode())
os.close(fd)
os.remove(filename)
print(f'{filename} deleted.')
