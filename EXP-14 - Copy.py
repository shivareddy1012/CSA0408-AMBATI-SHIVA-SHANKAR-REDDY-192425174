class SingleLevelDirectory:
    def __init__(self):
        self.directory = {}

    def create_file(self, filename, content=""):
        if filename in self.directory:
            print(f"File '{filename}' already exists.")
        else:
            self.directory[filename] = content
            print(f"File '{filename}' created.")

    def delete_file(self, filename):
        if filename in self.directory:
            del self.directory[filename]
            print(f"File '{filename}' deleted.")
        else:
            print(f"File '{filename}' not found.")

    def display_files(self):
        if self.directory:
            print("Files in directory:")
            for filename in self.directory:
                print(f"- {filename}")
        else:
            print("Directory is empty.")

if __name__ == "__main__":
    sld = SingleLevelDirectory()
    while True:
        print("\n1. Create File\n2. Delete File\n3. Display Files\n4. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            fname = input("Enter file name to create: ")
            sld.create_file(fname)
        elif choice == "2":
            fname = input("Enter file name to delete: ")
            sld.delete_file(fname)
        elif choice == "3":
            sld.display_files()
        elif choice == "4":
            break
        else:
            print("Invalid choice.")
