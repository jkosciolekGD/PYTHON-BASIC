"""
Write tests for classes in python_part_2/task_classes.py (Homework, Teacher, Student).
Check if all methods working correctly.
Also check corner-cases, for example if homework number of days is negative.
"""

# I had to rename this directory to python_part_2, because I could not import the path starting with a number
from practice.python_part_2.task_classes import *
import pytest


@pytest.fixture
def homework1():
    return Homework('abc', 5)


@pytest.fixture
def teacher1():
    return Teacher('aaa', 'bbb')


@pytest.fixture
def student1():
    return Student('aaa', 'bbb')


# setup: 2 homeworks with 5 days deadline
# it should say that  homework1 is not completed yet, but homework2 is completed
def test_homework_is_active(homework1):
    homework2 = Homework('cde', 5)

    homework2.status = True

    assert homework2.is_active()
    assert not homework1.is_active()


def test_teacher_create_homework(teacher1):

    homework1 = teacher1.create_homework('123', 5)

    assert not homework1.is_active()
    assert homework1.task == '123'


def test_if_student_did_his_homework(student1, homework1):
    student1.do_homework(homework1)

    assert homework1.is_active()


# If student is late with his homework, it should print 'You are late' in a console, so I am checking it with capfd
def test_if_homework_could_be_late(student1, capfd):
    homework2 = Homework('axc', 0)

    student1.do_homework(homework2)

    out, err = capfd.readouterr()
    assert out == "You are late\n"


def test_if_homework_deadline_days_are_negative(teacher1):
    hmwrk = teacher1.create_homework('asd', -2)

    assert hmwrk == "Deadline should not be a negative number."
