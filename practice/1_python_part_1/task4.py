"""
Write function which receives list of integers. Calculate power of each integer and
subtract difference between original previous value and it's power. For first value subtract nothing.
Restriction:
Examples:
    # >>> calculate_power_with_difference([1, 2, 3])
    [1, 4, 7]  # because [1^2, 2^2 - (1^2 - 1), 3^2 - (2^2 - 2)]
"""
from typing import List


def calculate_power_with_difference(ints: List[int]) -> List[int]:
    new_ints = [ints[0] ** 2]
    for i in range(len(ints)):
        if i > 0:
            new_ints.append(ints[i]**2 - (ints[i-1]**2 - ints[i-1]))
        # print(f"i: {i}, ints[i]: {ints[i]}, ints[i-1]: {ints[i-1]}")
    return new_ints


if __name__ == '__main__':
    print(calculate_power_with_difference([1, 2, 3]))
