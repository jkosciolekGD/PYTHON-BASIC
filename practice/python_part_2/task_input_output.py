"""
Write function which reads a number from input nth times.
If an entered value isn't a number, ignore it.
After all inputs are entered, calculate an average entered number.
Return string with following format:
If average exists, return: "Avg: X", where X is avg value which rounded to 2 places after the decimal
If it doesn't exists, return: "No numbers entered"
Examples:
    user enters: 1, 2, hello, 2, world
    # >>> read_numbers(5)
    Avg: 1.67
    ------------
    user enters: hello, world, foo, bar, baz
    # >>> read_numbers(5)
    No numbers entered

"""

import numpy as np


def read_numbers(n: int) -> str:
    numbers = []
    for i in range(n):
        inp = input("Insert something: ")
        try:
            val = int(inp)
            numbers.append(val)
        except ValueError:
            try:
                val = float(inp)
                numbers.append(val)
            except:
                pass

    if not numbers:
        return "No numbers entered."
    else:
        average = np.mean(numbers)
        return f"Avg: {average:.2f}"


if __name__ == '__main__':
    print(read_numbers(4))
