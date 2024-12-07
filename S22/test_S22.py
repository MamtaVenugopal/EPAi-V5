import pytest
from S22.my_classes import Person, Student, Professor, Employee, StudentProfessor, Location

def test_person_details():
    person = Person("Alice", 30, "Engineer")
    assert person.get_details() == "Name: Alice, Age: 30, Job: Engineer"

def test_student_details():
    student = Student("Bob", 20, "Student", "A")
    assert student.get_details() == "Name: Bob, Age: 20, Job: Student, Grade: A"

def test_professor_details():
    professor = Professor("Dr. Smith", 45, "Professor", ["Math", "Physics"])
    assert professor.get_details() == "Name: Dr. Smith, Age: 45, Job: Professor, Courses: ['Math', 'Physics']"

def test_employee_details():
    employee = Employee("John", 40, "Employee", "HR")
    assert employee.get_details() == "Name: John, Age: 40, Job: Employee, Department: HR"

def test_student_professor_details():
    student_professor = StudentProfessor("Dr. Brown", 50, "Professor", ["Computer Science"], "B")
    assert student_professor.get_details() == "Name: Dr. Brown, Age: 50, Job: Professor, Courses: ['Computer Science'], Grade: B"

def test_location_creation():
    location = Location("Paris", 48.8566, 2.3522)
    assert location.get_coordinates() == (48.8566, 2.3522)

def test_person_inheritance():
    student = Student("Charlie", 22, "Student", "B")
    assert isinstance(student, Person)

def test_professor_inheritance():
    professor = Professor("Dr. Lee", 38, "Professor", ["History"])
    assert isinstance(professor, Person)

def test_slots_usage():
    location = Location("Tokyo", 35.6762, 139.6503)
    location.name = "Kyoto"
    assert location.name == "Kyoto"
    with pytest.raises(AttributeError):
        location.country = "Japan"  # Slots prevent this attribute

def test_multiple_inheritance():
    student_professor = StudentProfessor("Dr. White", 60, "Professor", ["Engineering"], "A")
    assert isinstance(student_professor, Student)
    assert isinstance(student_professor, Professor)
    assert student_professor.get_details() == "Name: Dr. White, Age: 60, Job: Professor, Courses: ['Engineering'], Grade: A"
