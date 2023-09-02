#!/usr/bin/python3
"""A matrix division function"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix"""
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    res = []
    dim = len(matrix[0])

    for i in range(len(matrix)):
        if dim != len(matrix(i)):
            raise TypeError("Each row of the matrix must have the same size")

        temp = []

        for j in range(len(matrix[i])):
            if not isinstance(matrix[i][j], (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats")

            temp.append(round(matrix[i][j] / div, 2))
        res.append(temp)

    return res
