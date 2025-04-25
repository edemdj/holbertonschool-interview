#!/usr/bin/python3
"""
Calculates the fewest number of operations needed
to achieve exactly n H characters using Copy All and Paste.
"""


def minOperations(n):
    """
    Determines the minimum number

    Parameters:
    n (int): The target number

    Returns:
    int: The minimum number of operations needed,
    """
    if n < 2:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
