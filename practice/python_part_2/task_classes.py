"""
Create 3 classes with interconnection between them (Student, Teacher,
Homework)
Use datetime module for working with date/time
1. Homework takes 2 attributes for __init__: tasks text and number of days to complete
Attributes:
    text - task text
    deadline - datetime.timedelta object with date until task should be completed
    created - datetime.datetime object when the task was created
Methods:
    is_active - check if task already closed
2. Student
Attributes:
    last_name
    first_name
Methods:
    do_homework - request Homework object and returns it,
    if Homework is expired, prints 'You are late' and returns None
3. Teacher
Attributes:
     last_name
     first_name
Methods:
    create_homework - request task text and number of days to complete, returns Homework object
    Note that this method doesn't need object itself
PEP8 comply strictly.
"""
import datetime


class Homework:
    def __init__(self, task, deadline):
        self.task = task
        self.deadline = datetime.datetime.now() + datetime.timedelta(days=deadline)
        self.created = datetime.datetime.now()
        self.status = False  # False if not ended, True if completed

    def is_active(self):
        return self.status


class Teacher:
    def __init__(self, first, last):
        self.first_name = first
        self.last_name = last

    def create_homework(self, task, days):
        if days >= 0:
            return Homework(task, days)
        else:
            return "Deadline should not be a negative number."



class Student:
    def __init__(self, first, last):
        self.last_name = last
        self.first_name = first

    def do_homework(self, homework: Homework):
        if homework.deadline > datetime.datetime.now():
            homework.status = True
            return homework
        else:
            print("You are late")
            return None


if __name__ == '__main__':
    teacher = Teacher('Dmitry', 'Orlyakov')
    student = Student('Vladislav', 'Popov')
    print(teacher.last_name)  # Daniil
    print(student.first_name)  # Petrov

    expired_homework = teacher.create_homework('Learn functions', 0)
    print(expired_homework.created)  # Example: 2019-05-26 16:44:30.688762
    print(expired_homework.deadline)  # 0:00:00
    print(expired_homework.task)  # 'Learn functions'

    # create function from method and use it
    oop_homework = teacher.create_homework('create 2 simple classes', 5)
    print(oop_homework.deadline)  # 5 days, 0:00:00

    student.do_homework(oop_homework)
    student.do_homework(expired_homework)  # You are late
