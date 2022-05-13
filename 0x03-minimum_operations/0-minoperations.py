#!/usr/bin/python3
"""
This Method calculates the fewest number of operations in the task
"""


def minOperations(n):
    """This method returns the number of operations to copy paste the task"""
    if n <= 1:
        return 0
    operation = 0
    divisor = 2
    quotient = n
    while quotient > 1:
        if (quotient % divisor) == 0:
            quotient = quotient // divisor
            operation += divisor
        else:
            divisor += 1
    return operation
