# Leetcode: https://leetcode.com/problems/set-matrix-zeroes/

from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        for i in enumerate(matrix):

            for j in enumerate(matrix[0]):

                if matrix[i][j] == 0:

                    matrix[0][j] = False
                    matrix[i][0] = False

        for i in enumerate(matrix):

            for j in enumerate(matrix[0]):

                if matrix[i][0] is False or matrix[0][j] is False:

                    print(i, j)
                    matrix[i][j] = 0
