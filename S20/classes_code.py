import datetime
from weakref import WeakKeyDictionary
from math import pi
class Person:
    def __init__(self, first_name, last_name, birth_year, base_salary = 50000, bonus = 10):
        self._first_name = first_name
        self._last_name = last_name
        self.set_birth_year(birth_year)  # Validate during initialization
        self._base_salary = base_salary
        self.bonus = bonus  # Use the bonus property setter for validation
    
    def set_birth_year(self, year):
        current_year = datetime.datetime.now().year
        if not (1900 <= year <= current_year):
            raise ValueError("Invalid birth year. Year must be between 1900 and the current year.")
        self._birth_year = year

    full_name = property()

    @full_name.getter
    def full_name(self):
        return f"{self._first_name} {self._last_name}"

    @full_name.setter
    def full_name(self, full_name):
        first_name, last_name = full_name.split()
        self._first_name = first_name
        self._last_name = last_name
    
    @property
    def first_name(self):
        return self._first_name
    
    @property
    def last_name(self):
        return self._last_name

    @property
    def age(self):
        current_year = datetime.datetime.now().year
        return current_year - self._birth_year  # Calculate age dynamically

    @property
    def birth_year(self):
        return self._birth_year

    @property
    def base_salary(self):
        return self._base_salary
    
    @base_salary.setter
    def base_salary(self, value):
        if value < 0:
            raise ValueError("Base salary cannot be negative.")
        self._base_salary = value
    
    @property
    def bonus(self):
        return self._bonus

    @bonus.setter
    def bonus(self, value):
        if not 0 <= value <= 100:
            raise ValueError("Bonus percentage must be between 0 and 100.")
        self._bonus = value

    @property
    def salary(self):
        """Calculates the total salary including bonus."""
        return self.base_salary + (self.base_salary * self.bonus / 100)
    
class Circle:
    def __init__(self, radius):
        self._radius = radius
        self._area = None
        self._diameter = None

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value
        self._area = None  # Invalidate area cache
        self._diameter = None  # Invalidate diameter cache

    @property
    def diameter(self):
        if self._diameter is None:
            self._diameter = 2 * self.radius
        return self._diameter

    @property
    def area(self):
        if self._area is None:
            print("Calculating area...")
            self._area = pi * (self.radius ** 2)
        return self._area

    def set_radius(self, new_radius):  # Added set_radius method
        """Sets the radius and recalculates diameter and area."""
        self.radius = new_radius  # Utilize the radius setter for validation    

class DynamicClass:
    """
    A class that allows dynamic creation and access of attributes.
    """
    static_value = "Static Value"
    #validated_attr = ValidatedAttribute("validated_attr")  # Using the descriptor

    def __init__(self, **kwargs):
        """
        Initializes a new DynamicClass instance.

        Args:
            **kwargs: Keyword arguments representing initial dynamic attributes.
        """
        for name, value in kwargs.items():
            setattr(self, name, value)  # Dynamically set attributes

    def dynamic_attr(self, name, value):
        """
        Dynamically adds an attribute to the instance.

        Args:
            name (str): The name of the attribute to add.
            value: The value of the attribute.
        """
        setattr(self, name, value)  # Dynamically set attribute
        
 

class ValidatedAttribute:
    def __init__(self):
        self.data = WeakKeyDictionary()

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self.data.get(instance) # Use get to avoid KeyError

    def __set__(self, instance, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Attribute must be a positive integer.")
        self.data[instance] = value


