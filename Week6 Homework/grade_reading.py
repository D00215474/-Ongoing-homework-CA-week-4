import os
from student import Student
from custom_exceptions import InvalidIDError, InvalidGradeError

def load_student_from_file(filename):
    """
    Read the grades file and create/update student objects

    Args:
        filename: Path to the grades.txt file

    Returns:
        Dictionary of student_id to Student objects
    """

    Students = {}
    line_number = 0

    try:
        with open(filename, 'r') as file:
            for line in file:
                line_number +=1
                line = line.strip()

                #skip empty lines
                if not line:
                    continue

                try:
                    # Parse the line
                    parts = line.split(',')

                    #check if we have enough parts
                    if len(parts) < 3:
                        print(f"Line {line_number}: Not enough data")
                        continue
                    
                    # Extract student_id and name
                    student_id = parts[0].strip()
                    name = parts[1].strip()

                    # check if we have a grade 
                    if len(parts) >= 4:
                        grade = parts[2].strip()
                        grade = parts
                    else:
                        # if no grade provided, set it to None
                        print(f"Line {line_number}: No grade provided for student {student_id}")
                        continue
                    if student_id in Students:
                        Student = Students[student_id]
                    else:
                        #creating new student
                        try:
                            Student = Student(student_id, name)
                            Students[student_id] = Student
                        except (ValueError, InvalidIDError) as e:
                            print(f"Line {line_number}: Error creating student: {e}")
                            continue
                    try:
                        if Student.add_grade(subject, grade):
                            print(f"Line {line_number}: Added grade for student {student_id}") 
                        else:
                            print(f"Line {line_number}: Failed to add grade for student {student_id}")
                    except InvalidGradeError as e:
                        print(f"Line {line_number}: Invalid grade: {e}")
                except Exception as e:
                    print(f"Line {line_number}: Unexpected error: {e}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        print("Please make sure grades.txt is in the same directory as this script.")


                