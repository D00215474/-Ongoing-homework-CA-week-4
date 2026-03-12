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

    students = {}
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
                        subject = parts[2].strip()
                        grade = parts[3].strip()
                    else:
                        # if no grade provided, set it to None
                        print(f"Line {line_number}: No grade provided")
                        continue

                    if student_id in students:
                        student = students[student_id]
                        #creating new student
                        try:
                            if student.add_grade(subject, grade):
                                print(f"Line{line_number}: Added grade {grade} for {subject} to {name}")
                            else:
                                print(f"Line{line_number}: Subject '{subject}' already exists for {name} - keeping original grade {student.grades[subject]}")
                        except InvalidGradeError as e:
                            print(f"Line{line_number}: Invalid grade - {e} - skipping")
                    else:
                        # Create new student
                        try:
                            student = student(student_id, name)
                            students[student_id] = student
                            # Add tge grade to new student
                            try:
                                if student.add_grade(subject, grade):
                                        print(f"Line {line_number}: Added grade {grade} for student {name}") 
                                else:
                                    print(f"Line {line_number}: Subject {subject} already exists for {name} - Keeping original grade {student.grades[subject]}")
                            except InvalidGradeError as e:
                                print(f"Line {line_number}: Invalid grade: {e}")
                        except (ValueError, InvalidIDError) as e:
                            print(f"Line {line_number}: Unexpected error: {e}")
                            continue
                except Exception as e:
                    print(f"Lile '{line_number}: Unexpected Error - {e}' not found.")
                            
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        print(f"Error: Permission denied when trying to read '{filename}'.")
        print("Please check the file permissions and try again.")
        return None
    except PermissionError:
        print(f"Error: Permission denied to read '{filename}' .")
    
    return students

def main():
    """Main function to load students and print their grades."""
    print("=" * 50)
    print("Loading students from grades.txt...")
    print("=" * 50)

    #Load students from file
    filename = 'grades.txt'
    students = load_student_from_file(filename)

    if students is None:
        #File error occured, exit the program
        print("Exiting program due to file error.")
        return

    #Print loaded students and their grades
    print(f"\nSuccessfully loaded {len(students)} student from {filename}:")
    print("=" * 50)

    #Display summary of loaded students
    for student_id, student in students.items():
        print(f" {student}")
    
    print("=" * 50)

if __name__ == "__main__":
    main()




                