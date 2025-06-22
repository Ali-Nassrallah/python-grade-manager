students = {
    "Ali": [85, 92, 78],
    "Dana": [72, 89, 94],
    "Clara": [88, 76, 91],
    "Hadi": [64, 78, 82]
}

def calculate_average(grades):
    return sum(grades) / len(grades)

def get_grade_status(average):
    if average >= 90:
        return "Excellent"
    elif average >= 80:
        return "V.Good"
    elif average >= 70:
        return "Good"
    else:
        return "Needs Improvement"

def display_student_grades():
    print("\nStudent Grade Report:")
    print("=" * 40)
    
    student_records = [
        (name, grades, calculate_average(grades), get_grade_status(calculate_average(grades)))
        for name, grades in students.items()
    ]

    for name, grades, avg, status in student_records:
        print(f"{name}:")
        print(f"  Grades: {', '.join(map(str, grades))}")
        print(f"  Average: {avg:.1f}")
        print(f"  Status: {status}\n")

def add_student():
    """Add a new student to the system"""
    name = input("Enter student name: ")
    grades_input = input("Enter grades (comma separated): ")
    grades = [int(grade.strip()) for grade in grades_input.split(",")]
    students[name] = grades
    print(f"\n{name} added successfully!")

while True:
    print("\nStudent Grade Manager")
    print("1. View all student grades")
    print("2. Add new student")
    print("3. Exit")
    
    choice = input("Enter your choice (1-3): ")
    
    if choice == "1":
        display_student_grades()
    elif choice == "2":
        add_student()
    elif choice == "3":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")