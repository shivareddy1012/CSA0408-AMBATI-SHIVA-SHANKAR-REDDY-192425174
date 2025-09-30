pattern = 'search_term'
filename = 'testfile.txt'  

try:
    with open(filename, 'r') as file:
        found = False
        for line in file:
            if pattern.lower() in line.lower():
                print(line, end='')
                found = True
        if not found:
            print("No matches found.")
except FileNotFoundError:
    print(f"File '{filename}' not found.")
