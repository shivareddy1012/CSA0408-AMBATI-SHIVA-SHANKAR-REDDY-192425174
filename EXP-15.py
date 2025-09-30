class TwoLevelDirectory:
    def __init__(self):
        self.directory = {}

    def create_user(self, username):
        if username in self.directory:
            print(f"User '{username}' already exists.")
        else:
            self.directory[username] = {}
            print(f"User '{username}' created.")

    def create_file(self, username, filename, content=""):
        if username not in self.directory:
            print(f"User '{username}' does not exist.")
            return
        if filename in self.directory[username]:
            print(f"File '{filename}' already exists for user '{username}'.")
        else:
            self.directory[username][filename] = content
            print(f"File '{filename}' created for user '{username}'.")

    def delete_file(self, username, filename):
        if username in self.directory and filename in self.directory[username]:
            del self.directory[username][filename]
            print(f"File '{filename}' deleted for user '{username}'.")
        else:
            print(f"File '{filename}' not found for user '{username}'.")

    def display_files(self, username):
        if username in self.directory:
            files = self.directory[username]
            if files:
                print(f"Files for user '{username}':")
                for filename in files:
                    print(f"- {filename}")
            else:
                print(f"No files for user '{username}'.")
        else:
            print(f"User '{username}' does not exist.")

if __name__ == "__main__":
    tld = TwoLevelDirectory()
    while True:
        print("\n1. Create User\n2. Create File\n3. Delete File\n4. Display Files\n5. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            user = input("Enter username to create: ")
            tld.create_user(user)
        elif choice == "2":
            user = input("Enter username: ")
            fname = input("Enter file name to create: ")
            tld.create_file(user, fname)
        elif choice == "3":
            user = input("Enter username: ")
            fname = input("Enter file name to delete: ")
            tld.delete_file(user, fname)
        elif choice == "4":
            user = input("Enter username to display files: ")
            tld.display_files(user)
        elif choice == "5":
            break
        else:
            print("Invalid choice.")
