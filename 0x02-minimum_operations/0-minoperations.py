#!/usr/bin/python3
"""
Defines a function to calculate the minimum number of operations
to reach a certain number of characters.
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to result
    in exactly n H characters in the file.

    Args:
        n (int): The desired number of characters.

    Returns:
        int: The minimum number of operations needed, or 0 if impossible.
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2
    while n > 1:
        if n % divisor == 0:
            n //= divisor
            operations += divisor
        else:
            divisor += 1

    return operations
