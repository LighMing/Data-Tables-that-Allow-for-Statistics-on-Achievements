# Menu
# 1.Display all info
# 2.Calculate average
# 3.Submit a new student
# 4.Update a grade
# 5.Delete a student
# 6.Sort student by grade
# 7.Exit

from student_actions import display_all_info, submit_new_student, calculate_average
from student_actions import update_a_grade, update_all_grades, delete_a_student, sort_students_by_grade
from make_a_file import write_file
def main():
    students = []
    while True:
        print("\nWelcome to Grade Statistics program!")
        print("Please choose an option from the following list:")

        print("1. Submit new student.")
        print("2. Update a student's grade.")
        print("3. Delete a student.")
        print("4. Display all student info.")
        print("5. Calculate the average grade.")
        print("6. Update all grades.")
        print("7. Sort students by grade.")
        print("8. Write student info to file.")
        print("9. Exit Program.")


        choice = int(input("Enter your choice: "))

        if choice == 1:
            submit_new_student()
        elif choice == 2:
            student_name = input("Enter the name of the student whose grade you want to update: ")
            new_grade = float(input("Enter the new grade: "))
            students = update_a_grade(student_name, new_grade)
        elif choice == 3:
            student_name = input("Enter the name of the student you want to delete: ")
            delete_a_student(student_name)
        elif choice == 4:
            display_all_info(students)
        elif choice == 5:
            calculate_average()
        elif choice == 6:
            new_grade = float(input("Enter the new grade: "))
            update_all_grades(new_grade)
        elif choice == 7:
            sort_students_by_grade()
        elif choice == 8:
            write_file(students)
        elif choice == 9:
            print("Exiting the program...")
            break
        else:
            print("Invalid choice, please choose a valid option.")

if __name__ == "__main__":
    main()