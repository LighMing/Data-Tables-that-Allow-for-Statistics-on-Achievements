def display_all_info(students):
    if students:  # The list is not empty
        for i, student in enumerate(students, start=1):
            print(f"student{i} - Name: {student['name']}, Grade: {student['grade']}")
    else:
        print("There is no student information to display yet.")




def calculate_average():
    if not students:  # If the list is empty
        print("No student information was available to calculate grade point averages.")
        return

    total_grade = 0
    for student in students:
        total_grade += student['grade']

    average_grade = total_grade / len(students)
    print(f"The average score of the students is: {average_grade}")




students = []
def submit_new_student():
    student_name = input("Please enter the student's name: ")
    student_grade = float(input("Please enter student grades: "))

    student = {
        "name": student_name,
        "grade": student_grade
    }

    students.append(student)
    print(f"student {student_name} added successfully.")
    return students




def update_a_grade(student_name, new_grade):
    for student in students:
        if student['name'] == student_name:
            student['grade'] = new_grade
            print(f"{student_name}'s grade has been updated to {new_grade}.")
            return

    print(f"Sorry, no student named {student_name} was found.")

def update_all_grades(new_grade):
    for student in students:
        student['grade'] = new_grade

    print(f"All students' grades have been updated to {new_grade}.")




def delete_a_student(student_name):
    for student in students:
        if student['name'] == student_name:
            students.remove(student)
            print(f"The grade for {student_name} has been deleted.")
            return

    print(f"Sorry, no student named {student_name} was found.")





def sort_students_by_grade():
    print("Sorting students by grade...")
    sorted_students = sorted(students, key=lambda student: student['grade'])
    for student in sorted_students:
        print(f"Name: {student['name']}, Grade: {student['grade']}")