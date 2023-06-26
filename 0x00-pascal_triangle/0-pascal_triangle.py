#!/usr/bin/python3
"""
Pascal's Triangle
"""


def pascal_triangle(n):
    """
    A function def pascal_triangle(n):
    that return a list of integers representing the Pascal's triangle of n
    """
    # Return an empty list if n is less than or equal to 0
    if n <= 0:
        return []
    # Initialize the triangle with the first row
    triangle = [[1]]

    # Loop through the remaining elements in the row
    for i in range(1, n):
        # Initialize a new row with the first element
        row = [1]

        # Loop through the remaining elements in the row
        for j in range(1, i):
            # Compute the value of current element using the values
            # from previous row
            value = triangle[i - 1][j - 1] + triangle[i - 1][j]
            row.append(value)

        # Add the last element of the row as 1
        row.append(1)

        # Append the new row to the triangle
        triangle.append(row)

    # Return the complete triangle
    return triangle
