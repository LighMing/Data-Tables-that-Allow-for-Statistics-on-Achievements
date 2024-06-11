def write_file(students):
    if len(students) > 0:  # The list is not empty
        file_name = input('Enter the name of the file you want to save the students info to (without extension): ')
        with open(f'{file_name}.txt', 'w') as f:
            for i, student in enumerate(students, start=1):
                f.write(f"student{i} - Name: {student['name']}, Grade: {student['grade']}\n")

        print(f'Students info has been saved successfully to {file_name}.txt')
    else:
        print('There are no students to write their info into a file.')
