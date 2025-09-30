import pickle
import os

filename = "employees.dat"

def add_employee(emp_id, name, salary):
    record = {"id": emp_id, "name": name, "salary": salary}
    with open(filename, "ab") as f:
        pickle.dump(record, f)
    print(f"Employee {name} added.")

def display_employees():
    if not os.path.exists(filename):
        print("No employee records found.")
        return
    print("\nEmployee Records:")
    with open(filename, "rb") as f:
        while True:
            try:
                record = pickle.load(f)
                print(f"ID: {record['id']}, Name: {record['name']}, Salary: {record['salary']}")
            except EOFError:
                break

def search_employee(emp_id):
    if not os.path.exists(filename):
        print("No employee records found.")
        return
    with open(filename, "rb") as f:
        found = False
        while True:
            try:
                record = pickle.load(f)
                if record['id'] == emp_id:
                    print(f"Found: ID: {record['id']}, Name: {record['name']}, Salary: {record['salary']}")
                    found = True
                    break
            except EOFError:
                break
        if not found:
            print(f"Employee with ID {emp_id} not found.")

if __name__ == "__main__":
    while True:
        print("\n1. Add Employee\n2. Display Employees\n3. Search Employee\n4. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            eid = int(input("Enter Employee ID: "))
            name = input("Enter Employee Name: ")
            salary = float(input("Enter Salary: "))
            add_employee(eid, name, salary)
        elif choice == "2":
            display_employees()
        elif choice == "3":
            eid = int(input("Enter Employee ID to search: "))
            search_employee(eid)
        elif choice == "4":
            break
        else:
            print("Invalid choice.")
