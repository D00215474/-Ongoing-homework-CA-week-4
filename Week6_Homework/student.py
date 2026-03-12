from custom_exceptions import InvalidIDError, InvalidGradeError

class Student:  
    def __init__(self, student_id, name):
        self.student_id = student_id  
        self.name = name  
        self._grades = {}  # Dictionary to store course and grade pairs

    
    def student_id(self):
        return self._student_id
    
    # Setter for student_id with validation
    def student_id(self, value):
        self.validate_id(value)
        self._student_id = value

    
    def name(self):
        return self._name
    
    def name(self, value):
        if not value or not isinstance(value, str):
            raise ValueError("Name must be a non-empty string.")
        self._name = value

    def grades(self):
        """Returns a copy of the grades dictionary to preserve encapsulation."""
        return self._grades.copy()
    
    def validate_id(self, student_id):
        """
        Validates the student ID. 
        It must be a non-empty string and start with D00 
        """
        # Check if ID exists
        if not student_id or not isinstance(student_id, str):
            raise ValueError("Student ID must be a non-empty string.")
        
        # Check if ID starts with D00
        if not student_id.upper().startswith("D00"):
            raise InvalidIDError(f"Student ID '{student_id}' must start with 'D00'.")
        
    def validate_grade(self, grade):
        """
        Validates the grade.
        Check if the grade exists
        Check if it's a number
        Check if it's between 0 and 100
        """
        # Check if grade exists
        if grade is None:
            raise InvalidGradeError("Grade cannot be None.")
        
        # Check if grade is a number
        try:
            grade_value = float(grade)
        except (ValueError, TypeError):
            raise InvalidGradeError(f"Grade '{grade}' must be a number.")
        
        # Check if grade is between 0 and 100
        if grade_value < 0 or grade_value > 100:
            raise InvalidGradeError(f"Grade '{grade_value}' must be between 0 and 100.")
        
        return grade_value
    
    def add_grade(self, subject, grade):
        """
        Adds grades for subject name
        
        Args:
            subject: The name of the subject    
            grade: The grade value
        
        Returns:
            True if the grade was added, False if the subject already exists

        Raises:
            InvalidGradeError: If the grade is invalid.
        """
        # Validate the grade first
        valid_grade = self.validate_grade(grade)
        
        # Check if subject already exists
        if subject in self._grades:
            return False
        
        # Add the grade
        self._grades[subject] = valid_grade
        return True
    
    def __repr__(self):
        return f"Student('{self.student_id}', '{self.name}', {len(self._grades)} subjects)"
    
    def __str__(self):
        return f"Student ID: {self.student_id}, Name: {self.name}, Subjects: {len(self._grades)}"
    
    def __eq__(self, other):
        if not isinstance(other, Student):
            return False
        return self.student_id == other.student_id