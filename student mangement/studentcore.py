import json

# STEP 1: Load data from JSON or return empty structure
def load_data():
    try:
        with open("student_data.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"name": [], "marks": {}}

# STEP 2: Save the data back to JSON
def update_data(student):
    with open("student_data.json", "w") as f:
        json.dump(student, f, indent=4)

# Add a student
def add_student(student):
    stuname = input("Enter student name: ").lower()
    if stuname not in student["name"]:
        student["name"].append(stuname)
        print(f"Student '{stuname}' added successfully.")
        update_data(student)
    else:
        print(f"Student '{stuname}' already exists.")

# Add marks for a student
def add_marks(student):
    name = input("Enter student name: ").lower()
    if name in student["name"]:
        mark = []
        for i in range(1, 4):
            mark.append(int(input(f"Enter marks for subject {i}: ")))
        student["marks"][name] = mark
        print(f"Marks for {name} added successfully.")
        update_data(student)
    else:
        print(f"Student '{name}' not found.")

# Update marks
def update_marks(student):
    name = input("Enter student name to update marks: ").lower()
    if name in student["name"]:
        mark = []
        for i in range(1, 4):
            mark.append(int(input(f"Update marks for subject {i}: ")))
        student["marks"][name] = mark
        print(f"Marks for '{name}' updated successfully.")
        update_data(student)
    else:
        print(f"Student '{name}' not found.")

# Delete a student
def delete_student(student):
    name = input("Enter student name to delete: ").lower()
    if name in student["name"]:
        student["name"].remove(name)
        if name in student["marks"]:
            del student["marks"][name]
        print(f"Student '{name}' deleted successfully.")
        update_data(student)
    else:
        print(f"Student '{name}' not found.")

# View students
def view_students(student):
    print("\n--- Student List ---")
    for name in student["name"]:
        print(f"- {name.title()}")
    print("\n--- Marks ---")
    for name, marks in student["marks"].items():
        print(f"{name.title()}: {marks}")

# MAIN DRIVER
student = load_data()

while True:
    print("\n===== Student Manager =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Add Marks")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if choice == 1:
        add_student(student)
    elif choice == 2:
        view_students(student)
    elif choice == 3:
        add_marks(student)
    elif choice == 4:
        update_marks(student)
    elif choice == 5:
        delete_student(student)
    elif choice == 6:
        update_data(student)
        print("Exiting Student Manager.")
        break
    else:
        print("Invalid choice. Please try again.")
