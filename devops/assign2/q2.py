grades = {
    "Alice": "A",
    "Bob": "B",
    "Charlie": "C",
}

def add_student(name, grade):
    """Add a new student and their grade to the dictionary."""
    grades[name] = grade
    print(f"Added {name} with grade {grade}.")
        
def update_student(name, grade):
    """Update a student's grade in the dictionary."""
    if name in grades:
        grades[name] = grade
        print(f"Updated {name}'s grade to {grade}.")
    else:
        print(f"{name} not found.")
        
def print_grades():
    """Print all students and their grades."""
    for name, grade in grades.items():
        print(f"{name}: {grade}")
        
while True:
    command = input("Enter a command (add, update, print, exit): ").strip().lower()
    
    if command == "add":
        name = input("Enter student's name: ")
        grade = input("Enter student's grade: ")
        add_student(name, grade)
    elif command == "update":
        name = input("Enter student's name: ")
        grade = input("Enter new grade: ")
        update_student(name, grade)
    elif command == "print":
        print_grades()
    elif command == "exit":
        break
    else:
        print("Invalid command. Please try again.")