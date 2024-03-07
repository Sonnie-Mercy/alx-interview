#!/usr/bin/python3
""" a function def pascal_triangle(n)"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing
    the Pascal’s triangle of n
    """
    triangle = []
    for i in range(n):
        row = [1]  # First element of each row is always 1
        if i > 0:
            # Calculate elements for the current row based on the previous row
            prev_row = triangle[-1]
            for j in range(1, i):
                row.append(prev_row[j - 1] + prev_row[j])
            row.append(1)  # Last element of each row is always 1
        triangle.append(row)

    return triangle
