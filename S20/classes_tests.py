import pytest

from classes_code import Person, Circle
def test_person():
    person = Person('John', 'Doe', 1990)
    assert person.age == 34  # Assuming the current year is 2024
    person.set_birth_year(1985)
    assert person.age == 39
    person.full_name = "Jane Smith"
    assert person.first_name == "Jane"
    assert person.last_name == "Smith"
    assert person.salary == 55000  # base_salary = 50000, bonus = 10%
    person.base_salary = 60000
    assert person.salary == 66000  # Updated salary

def test_circle():
    circle = Circle(10)
    assert circle.radius == 10
    assert circle.diameter == 20
    assert circle.area == pytest.approx(314.159, 0.001)
    circle.radius = 5
    assert circle.diameter == 10
    assert circle.area == pytest.approx(78.539, 0.001)
    with pytest.raises(ValueError):
        circle.radius = -1  # Should raise an error for negative radius

test_person()
test_circle()