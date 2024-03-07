#!/usr/bin/python3
""" a function def pascal_triangle(n)"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing
    the Pascal’s triangle of n
    """
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        row = [1]
        if []:
            for j in range(1, len(triangle[-1])):
                row.append(triangle[-1][j - 1] + triangle[-1][j])
            row.append(1)
        triangle.append(row)

    return triangle
