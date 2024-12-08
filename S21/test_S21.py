import pytest
from advanced_number import AdvancedNumber

def test_initialization():
    obj = AdvancedNumber(5)
    assert obj.value == 5

def test_str_repr():
    obj = AdvancedNumber(5)
    assert str(obj) == "Value: 5"
    assert repr(obj) == "AdvancedNumber(5)"

def test_arithmetic_operations():
    obj1 = AdvancedNumber(10)
    obj2 = AdvancedNumber(5)
    assert (obj1 + obj2).value == 15
    assert (obj1 - obj2).value == 5
    assert (obj1 * 2).value == 20
    assert (obj1 / obj2).value == 2.0
    assert (obj1 % obj2).value == 0

def test_comparison_operations():
    obj1 = AdvancedNumber(10)
    obj2 = AdvancedNumber(5)
    assert obj1 > obj2
    assert obj2 < obj1
    assert obj1 != obj2
    assert obj1 >= AdvancedNumber(10)
    assert obj2 <= AdvancedNumber(5)

def test_hashable():
    obj1 = AdvancedNumber(10)
    obj2 = AdvancedNumber(10)
    obj_set = {obj1, obj2}
    assert len(obj_set) == 1

def test_boolean_conversion():
    assert bool(AdvancedNumber(10)) is True
    assert bool(AdvancedNumber(0)) is False

def test_callable():
    obj = AdvancedNumber(4)
    assert obj() == 16

def test_custom_formatting():
    obj = AdvancedNumber(10)
    assert format(obj, ".2f") == "10.00"
    assert format(obj, "#x") == "0xa"

def test_destruction(capsys):
    obj = AdvancedNumber(5)
    del obj
    captured = capsys.readouterr()
    assert "AdvancedNumber with value 5 is being destroyed" in captured.out