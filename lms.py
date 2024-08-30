"""
Instructions: Implement Python programs to accomplish the following task

Task

You are tasked with developing a Python program to manage a student database. The user should be able to add new students
or stop the input process by entering "stop." Each student's name, along with a sequentially generated ID starting from 1, 
should be stored in a tuple, with these tuples kept in a list. The program must check for duplicate names before adding a 
new student and display a message if a duplicate is found. After the input process ends, the program should first display 
the complete list of student tuples and then display each student's ID and name individually. Additionally, the program 
should show the total number of students, calculate and display the total length of all student names combined, and 
identify the student with the longest and shortest name using appropriate operators. Implement these operations within a
function named manage_student_database() and ensure you call this function at the end of your code.
"""

def manage_student_database():
    # Create an empty list to store student tuples
    students_list = []
    student_id = 1

    # Loop until the user enters "stop"
    while True:
        # Get the student's name
        student_name = input("Enter student's name (or type 'stop' to finish): ").strip()
        
        # If the user enters "stop", break the loop
        if student_name.lower() == "stop":
            break
        
        # Check for duplicate names
        if any(student_name == student[1] for student in students_list):
            print(f"Duplicate name found: {student_name} already exists in the database.")
        else:
            # Add the student's tuple to the list
            students_list.append((student_id, student_name))    
            # Increment the student ID
            student_id += 1

    # Display the complete list of students    
    print("\nComplete list of students:")
    for student in students_list:
        print(student)
    
    # Display each student's ID and name individually
    print("\nIndividual student details:")
    for student in students_list:
        print(f"ID: {student[0]}, Name: {student[1]}")    
    
    # Display the total number of students
    total_students = len(students_list)
    print(f"\nTotal number of students: {total_students}")
    
    # Calculate and display the total length of all student names combined
    total_name_length = sum(len(student[1]) for student in students_list) 
    print(f"Total length of all student names combined: {total_name_length}")
    
    # Identify the student with the longest and shortest name
    if students_list:
        longest_stud_name = max(students_list, key=lambda student: len(student[1]))
        shortest_stud_name = min(students_list, key=lambda student: len(student[1]))
        print(f"\nStudent with the longest name: {longest_stud_name[1]} (ID: {longest_stud_name[0]}, Length: {len(longest_stud_name[1])})")
        print(f"Student with the shortest name: {shortest_stud_name[1]} (ID: {shortest_stud_name[0]}, Length: {len(shortest_stud_name[1])})")

# Call the function to run the program        
manage_student_database()
