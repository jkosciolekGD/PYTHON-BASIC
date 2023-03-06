"""
Write function which receives filename and reads file line by line and returns min and mix integer from file.
Restriction: filename always valid, each line of file contains valid integer value
Examples:
    # file contains following lines:
        10
        -2
        0
        34
    # >>> get_min_max('filename')
    (-2, 34)

Hint:
To read file line-by-line you can use this:
with open(filename) as opened_file:
    for line in opened_file:
        ...
"""
from typing import Tuple


def get_min_max(filename: str) -> Tuple[int, int]:
    min_v, max_v = 0, 0
    with open(filename) as opened_file:
        for line in opened_file:
            min_v = min(int(line), min_v)
            max_v = max(int(line), max_v)
    opened_file.close()
    return(f"({min_v}, {max_v})")


if __name__ == '__main__':
    # file = open("filename.txt", "x")
    # file.write("10\n-2\n0\n34")
    # file.close()
    print(get_min_max('filename.txt'))

