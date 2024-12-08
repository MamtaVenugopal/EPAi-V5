class AdvancedNumber:
    def __init__(self, value):
      if isinstance(value, (int, float)):
        self._value = value

    @property
    def value(self):
        return self._value

    def __repr__(self):
        print('__repr__ called')
        return f"AdvancedNumber({self.value})"

    def __str__(self):
        print('__str__ called')
        return f"Value: {self.value}"

    def __add__(self, other):
        if isinstance(other,AdvancedNumber):
          return AdvancedNumber(self.value + other.value)
        elif isinstance(other, (int, float)):
            return AdvancedNumber(self.value + other)
        else:
            raise TypeError("Unsupported operand type for +")

    def __sub__(self,other):
        if isinstance(other,AdvancedNumber) :
          return AdvancedNumber(self.value - other.value)
        elif isinstance(other, (int, float)):
            return AdvancedNumber(self.value - other)
        else:
            raise TypeError("Unsupported operand type for -")

    def __mul__(self,other):
        if isinstance(other,AdvancedNumber) :
          return AdvancedNumber(self.value * other.value)
        elif isinstance(other, (int, float)):
            return AdvancedNumber(self.value * other)
        else:
            raise TypeError("Unsupported operand type for -")

    def __truediv__(self, other):
        if isinstance(other, AdvancedNumber):
            if other.value == 0:  # Check for division by zero
                raise ZeroDivisionError("Division by zero")
            return AdvancedNumber(self.value / other.value)
        elif isinstance(other, (int, float)):
            if other == 0:  # Check for division by zero
                raise ZeroDivisionError("Division by zero")
            return AdvancedNumber(self.value / other)
        else:
            raise TypeError("Unsupported operand type for /")

    def __mod__(self, other):
        if isinstance(other, AdvancedNumber):
            if other.value == 0:  # Check for division by zero
                raise ZeroDivisionError("Modulo by zero")
            return AdvancedNumber(self.value % other.value)
        elif isinstance(other, (int, float)):
            if other == 0:  # Check for division by zero
                raise ZeroDivisionError("Modulo by zero")
            return AdvancedNumber(self.value % other)
        else:
            raise TypeError("Unsupported operand type for %")

    def __lt__(self, other):
        if isinstance(other, AdvancedNumber):
            return self.value < other.value
        elif isinstance(other, (int, float)):
            return self.value < other
        return TypeError("Unsupported operand type for <")

    def __le__(self, other):
        if isinstance(other, AdvancedNumber):
            return self.value <= other.value
        elif isinstance(other, (int, float)):
            return self.value <= other
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, AdvancedNumber):
            return self.value > other.value
        elif isinstance(other, (int, float)):
            return self.value > other
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, AdvancedNumber):
            return self.value >= other.value
        elif isinstance(other, (int, float)):
            return self.value >= other
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, AdvancedNumber):
            return self.value == other.value
        elif isinstance(other, (int, float)):
            return self.value == other
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, AdvancedNumber):
            return self.value != other.value
        elif isinstance(other, (int, float)):
            return self.value != other
        return NotImplemented

    def __hash__(self):  # Removed 'other' argument
        return hash(self.value)  # Only hash the value
    

    def __bool__(self):
        return bool(self.value)

    def __call__(self):
        return self.value ** 2

    def __format__(self, format_spec):
        if format_spec == ".2f":
            return f"{self.value:.2f}"
        elif format_spec == "#x":
            return f"0x{self.value:x}"
    
    def __del__(self):
      print(f'AdvancedNumber with value {self.value} is being destroyed')