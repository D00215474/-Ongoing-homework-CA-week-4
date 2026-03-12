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
                