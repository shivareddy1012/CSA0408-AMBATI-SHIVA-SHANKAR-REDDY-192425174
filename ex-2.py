import os

# Step 1: Create a source file (for testing)
with open("source.txt", "w") as f:
    f.write("Hello, this is the source file.\nCopied using system calls in Python!")

src_file = "source.txt"
dest_file = "destination.txt"

try:
    # Step 2: Open source file (read-only)
    src_fd = os.open(src_file, os.O_RDONLY)

    # Step 3: Open destination file (write-only, create if not exists, truncate if exists)
    dest_fd = os.open(dest_file, os.O_WRONLY | os.O_CREAT | os.O_TRUNC)

    # Step 4: Read from source and write to destination
    while True:
        data = os.read(src_fd, 1024)  # read 1024 bytes
        if not data:  # End of file
            break
        os.write(dest_fd, data)

    print("✅ File copied successfully using system calls!")

except FileNotFoundError:
    print("❌ Error: Source file does not exist!")

finally:
    # Step 5: Close both files safely
    try:
        os.close(src_fd)
        os.close(dest_fd)
    except:
        pass

