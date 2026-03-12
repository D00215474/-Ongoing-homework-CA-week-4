class student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self._grades = {} #Dictionary to store course and grade pairs

        def student_id(self):
            return self._student_id
        
        def student_id(self, value):
            self._student_id = value

        def name(self):
            return self._name
        
        def name(self, value):
            if not value or not isinstance(value, str):
                raise ValueError("Name must be a non-empty string.")
            self._name = value

        