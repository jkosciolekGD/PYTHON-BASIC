"""
using datetime module find number of days from custom date to now
Custom date is a string with format "2021-12-24"
If entered string pattern does not match, raise a custom Exception
If entered date is from future, return negative value for number of days
    calculate_days('2021-10-07')  # for this example today is 6 october 2021
    -1
    calculate_days('2021-10-05')
    1
    calculate_days('10-07-2021')
    WrongFormatException
"""
from datetime import datetime
import pytest


# class InvalidDateFormat(Exception):
#     """Raised when the input value is not in a 'year-month-day' format"""
#     pass


def calculate_days(from_date: str) -> int:
    now = datetime.today().date()

    try:
        fr = datetime.strptime(from_date, '%Y-%m-%d').date()
        return (now - fr).days
    except ValueError:
        print("Invalid date format (excepted format: 'year-month-day')")
        return 0

    # print(now)
    # print(type(now))
    # print(fr)
    # print(type(fr))


# if __name__ == '__main__':
#     print(calculate_days("2023-06-05"))
#     print(calculate_days("2023-06-01"))
#     print(calculate_days("06-2023-01"))


"""
Write tests for calculate_days function
Note that all tests should pass regardless of the day test was run
Tip: for mocking datetime.now() use https://pypi.org/project/pytest-freezegun/
"""


@pytest.mark.freeze_time('2023-06-02')
def test_from_date_is_in_the_future(freezer):
    fr_date = '2023-06-05'

    assert calculate_days(fr_date) == -3


@pytest.mark.freeze_time('2023-06-02')
def test_from_date_is_in_the_past(freezer):
    fr_date = '2023-05-30'

    assert calculate_days(fr_date) == 3


def test_wrong_date_format_entered(capfd):
    fr_date = '06-2023-30'
    calculate_days(fr_date)
    out, err = capfd.readouterr()

    # check if console printed custom exception message
    assert out == "Invalid date format (excepted format: 'year-month-day')\n"
