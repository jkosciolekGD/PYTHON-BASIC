"""
Write tests for a read_numbers function.
It should check successful and failed cases
for example:
Test if user inputs: 1, 2, 3, 4
Test if user inputs: 1, 2, Text

Tip: for passing custom values to the input() function
Use unittest.mock patch function
https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch

TIP: for testing builtin input() function create another function which return input() and mock returned value
"""
from mock import patch
from practice.python_part_2.task_input_output import *


def numbers_input_generator():
    numbers = [1, 2, 3, 4]
    for i in numbers:
        yield i


def test_read_numbers_without_text_input():
    with patch('builtins.input', side_effect=[1, 2, 3, 4]):
        result = read_numbers(4)
        assert result == 'Avg: 2.50'


def test_read_numbers_with_text_input():
    with patch('builtins.input', side_effect=[1, 2, 'Text']):
        result = read_numbers(3)
        assert result == 'Avg: 1.50'


def test_read_numbers_with_text_input_without_any_number():
    with patch('builtins.input', side_effect=['Text', 'a', 'b', 'c']):
        result = read_numbers(4)
        assert result == 'No numbers entered.'
