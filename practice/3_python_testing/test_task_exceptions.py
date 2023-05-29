"""
Write tests for division() function in python_part_2/task_exceptions.py
In case (1,1) it should check if exception were raised
In case (1,0) it should check if return value is None and "Division by 0" printed
If other cases it should check if division is correct

TIP: to test output of print() function use capfd fixture
https://stackoverflow.com/a/20507769
"""

from practice.python_part_2.task_exceptions import *


def test_division_ok(capfd):
    division1 = division(9, 3)

    out, err = capfd.readouterr()
    assert out == "Division finished\n"
    assert division1 == 3


def test_division_by_zero(capfd):
    division1 = division(2, 0)

    out, err = capfd.readouterr()
    assert out == 'Division finished\nDivision by zero.\nDivision finished\n'


def test_division_by_one(capfd):
    division1 = division(2, 1)

    out, err = capfd.readouterr()
    assert out == 'Deletion on 1 get the same result\nDivision finished\n'
