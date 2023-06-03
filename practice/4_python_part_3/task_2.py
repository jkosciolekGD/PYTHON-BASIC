"""
Write function which executes custom operation from math module
for given arguments.
Restriction: math function could take 1 or 2 arguments
If given operation does not exist, raise OperationNotFoundException
Examples:
     math_calculate('log', 1024, 2)
     10.0
     math_calculate('ceil', 10.7)
     11
"""
import math


class WrongNumberOfArgs(Exception):
    """Raised when the input has too little or too many arguments to do an operation"""
    pass


def math_calculate(function: str, *args):
    try:
        match function:
            # 1 argument - natural logarithm of arg
            # 2 arguments - logarithm of x to the 2nd arg base
            case 'log':
                if len(args) == 1:
                    return math.log(args[0])
                elif len(args) == 2:
                    return math.log(args[0], args[1])
                else:
                    raise WrongNumberOfArgs

            # 1 argument - smallest int greater than or equal to arg
            case 'ceil':
                if len(args) == 1:
                    return math.ceil(args[0])
                else:
                    raise WrongNumberOfArgs

            # 1 argument - the largest int less than or equal to arg
            case 'floor':
                if len(args) == 1:
                    return math.floor(args[0])
                else:
                    raise WrongNumberOfArgs

            # 1 argument - absolute value of x
            case 'abs':
                if len(args) == 1:
                    return math.fabs(args[0])
                else:
                    raise WrongNumberOfArgs

            # 2 arguments - accurate sum of arguments
            # another number of arguments is limited by the task requirements
            case 'sum':
                if len(args) == 2:
                    return math.fsum(args)
                else:
                    raise WrongNumberOfArgs

            # 2 arguments - return the remainder of 1st argument / 2nd argument
            case 'remainder':
                if len(args) == 2:
                    return math.fmod(args[0], args[1])
                else:
                    raise WrongNumberOfArgs

    except WrongNumberOfArgs:
        print("Wrong number of arguments of the function.")
        return None


# if __name__ == '__main__':
#     print(math_calculate('log'))
#     print(math_calculate('log', 2))
#     print(math_calculate('log', 1024, 2))
#     print(math_calculate('ceil', 10.7))
#     print(math_calculate('floor', 10.7))
#     print(math_calculate('abs', -4))
#     print(math_calculate('abs', 4))
#     print(math_calculate('sum', 1, 2))
#     print(math_calculate('sum', .1, .1))
#     print(math_calculate('remainder', 20, 3))


"""
Write tests for math_calculate function
"""


# assertion to None, because the only case, when the output could be None is when the custom exception has been raised
def test_log_without_arg():
    assert math_calculate('log') is None


def test_log_with_one_arg():
    assert math_calculate('log', 1) == 0


def test_log_with_two_arg():
    assert math_calculate('log', 1024, 2) == 10.0


def test_ceil_without_arg():
    assert math_calculate('ceil') is None


def test_ceil_with_one_arg():
    assert math_calculate('ceil', 10.7) == 11


def test_ceil_with_two_arg():
    assert math_calculate('ceil', 10.7, 12.3) is None


def test_floor_without_arg():
    assert math_calculate('floor') is None


def test_floor_with_one_arg():
    assert math_calculate('floor', 10.7) == 10


def test_floor_with_two_arg():
    assert math_calculate('floor', 10.7, 12.3) is None


def test_abs_without_arg():
    assert math_calculate('abs') is None


def test_abs_with_one_positive_arg():
    assert math_calculate('abs', 4) == 4


def test_abs_with_one_negative_arg():
    assert math_calculate('abs', -5) == 5


def test_abs_with_two_arg():
    assert math_calculate('abs', 10.7, 12.3) is None


def test_sum_without_arg():
    assert math_calculate('sum') is None


def test_sum_with_one_arg():
    assert math_calculate('sum', 10) is None


def test_sum_with_two_arg():
    assert math_calculate('sum', 10.7, 12.3) == 23


def test_remainder_without_arg():
    assert math_calculate('remainder') is None


def test_remainder_with_one_arg():
    assert math_calculate('remainder', 3) is None


def test_remainder_with_two_arg():
    assert math_calculate('remainder', 20, 3) == 2.0
