#!/usr/bin/python3

"This module contains function given an n x n 2D matrix"


def rotate_2d_matrix(matrix):
    "This function rotates matrix 2D 90 degree clockwise"

    m = 0
    n = len(matrix) - 1
    while m < n:
        for i in range(m, n):
            aux = matrix[i][n]
            matrix[i][n] = matrix[m][i]
            aux2 = matrix[n][n + m - i]
            matrix[n][n + m - i] = aux
            aux = matrix[n + m - i][m]
            matrix[n + m - i][m] = aux2
            matrix[m][i] = aux
        m += 1
        n -= 1
