class Person:
    def __init__(self, name:str, age:int, job:str):
      self._name = name
      self._age = age
      self._job = job

    @property  # Use @property for name, age, and job
    def name(self):
        return self._name
    
    @property
    def age(self):
        return self._age

    @property
    def job(self):
        return self._job

    def get_details(self):
        # Corrected the f-string formatting to match the expected output
        return f"Name: {self.name}, Age: {self.age}, Job: {self.job}"   

class Student(Person):
    def __init__(self,name:str, age:int, job:str, grade:str):
        super().__init__(name, age, job)
        self._grade = grade

    @property
    def grade(self):
        return self._grade

    def get_details(self):
        # Corrected the f-string formatting to match the expected output
        person_details = super().get_details()
        return f"{person_details}, Grade: {self.grade}"

class Professor(Person):   
    def __init__(self, name:str, age:int, job:str, courses:list):
        super().__init__(name, age, job)
        self._courses = courses
    @property
    def courses(self):
       return self._courses 

    def get_details(self):
        # Corrected the f-string formatting to match the expected output
        person_details = super().get_details()
        return f"{person_details}, Courses: {self.courses}"   

class Employee(Person): 
    def __init__(self, name:str, age:int, job:str, department:str):
        super().__init__(name, age, job)
        self._department = department
    
    @property
    def department(self):
       return self._department 

    def get_details(self):
        # Corrected the f-string formatting to match the expected output
        person_details = super().get_details()
        return f"{person_details}, Department: {self.department}" 

class StudentProfessor(Student,Professor):
    def __init__(self, name: str, age: int, job: str, courses: list, grade: str):
        Person.__init__(self,name, age, job)  # Call Person.__init__ through Student
        self._grade = grade  # Initialize Student's grade
        self._courses = courses  # Initialize Professor's courses
    
    def get_details(self):
        student_details = super().get_details() # This calls Professor.get_details by default due to MRO
        # Extract the Professor's details from the end
        professor_part = student_details.split(', Courses:')[1]
        student_part = student_details.split(', Courses:')[0]
        # Combine details without redundancy
        print(f"{student_part}, Courses:{professor_part}")
        return f"{student_part}, Courses:{professor_part}"

class Location:
    __slots__ = '_name', '_longitude', '_latitude'
    def __init__(self, name, longitude, latitude):
        self._longitude = longitude
        self._latitude = latitude
        self._name = name
    @property
    def name(self):
        return self._name  

    @name.setter  # Added setter for name property
    def name(self, new_name):
        self._name = new_name
        
    @property
    def longitude(self):
        return self._longitude
    
    @property
    def latitude(self):
        return self._latitude

    def get_coordinates(self):
        return (self.longitude, self.latitude)