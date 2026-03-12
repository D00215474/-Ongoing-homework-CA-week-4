from custom_exceptions import InvalidIDError, InvalidGradeError

class Student:  
    # Constructor to initialize student_id, name, and an empty dictionary for grades
        def __init__(self, student_id, name):
            self.student_id = student_id
            self.name = name
            self._grades = {} #Dictionary to store course and grade pairs

     # Method to add or update a grade for a course
        def validate_id(self, student_id):
            """
            Validates the student ID. 
            It must be a non-empty string of digits.
            check if it starts with D00 
            """
            # i need to check if ID exists in the system before adding it to the student
            if not student_id or not isinstance(student_id, str):
                raise ValueError("Student ID must be a non-empty string.")
            
            # check if ID starts with D00
            if not student_id.upper().startswith("D00"):
                raise InvalidIDError(f"Student ID '{student_id}' must start with 'D00'.")
            
        def validate_grade(self, grade):
            """
            Validates the grade.
            check if the grade is there
            checking if its a number
            check if its between 0 and 100
            """
            # check if grade is exists
            if grade is None:
                raise InvalidGradeError("Grade cannot be None.")
            
            # check if grade is a number
            try:
                grade_Value = float(grade)
            except (ValueError, TypeError):
                raise InvalidGradeError(f"Grade '{grade}' must be a number.")
            
            # Checking if grade is between 0 and 100
            if grade_Value < 0 or grade_Value > 100:
                raise InvalidGradeError(f"Grade '{grade_Value}' must be between 0 and 100.")
            
            return grade_Value

        # Method to add or update a grade for a course
        def grades(self):
            """Returns a copy of the grades dictionary to preserve encapsulation."""
            return self._grades.copy()
        
        def add_grade(self, subject, grade):
            """
                Adds grades for subject name
            Args:
                subject: The name of the subject    
                grade: The grade value
            
            Returns:
                True If the grade was added, False if the subject already exists

            Raises:
                InvalidGradeError: If the grade is invalid.

            """
            #Validate the grade first
            valid_grade = self.validate_grade(grade)
            if subject in self._grades:
                return False
            self._grades[subject] = valid_grade
            return True

        # Getter for student_id
        def student_id(self):
            return self._student_id
        
        # Setter for student_id with validation
        def student_id(self, value):
            self.validate_id(value)
            self._student_id = value

        # Getter for name
        def name(self):
            return self._name
        
        # Setter for name with validation
        def name(self, value):
            if not value or not isinstance(value, str):
                raise ValueError("Name must be a non-empty string.")
            self._name = value

       # Method to add or update a grade for a course
        def __repr__(self):
            return f"Student('{self.student_id}', '{self.name}', {len(self._grades)} subjects)"
        
        # Method to provide a string representation of the student
        def __str__(self):
            return f"Student ID: {self.student_id}, Name: {self.name}, Subjects: {len(self._grades)}"
        
        # Method to compare two student objects based on their IDs
        def __eq__(self, other):
            if not isinstance(other, Student):
                return False
            return self.student_id == other.student_id
        