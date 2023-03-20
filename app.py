#!/usr/bin/env python


class App:

    @staticmethod
    def solve_matrix(matrix):
        result_arr = []
        top_row = 0
        bottom_row = len(matrix) - 1
        left_col = 0
        right_col = len(matrix[0]) - 1

        while top_row <= bottom_row and left_col <= right_col:
            # Traverse right on top row
            for col in range(left_col, right_col + 1):
                result_arr.append(matrix[top_row][col])
            top_row += 1

            # Traverse down on right column
            for row in range(top_row, bottom_row + 1):
                result_arr.append(matrix[row][right_col])
            right_col -= 1

            # Traverse left on bottom row
            if top_row <= bottom_row:
                for col in range(right_col, left_col - 1, -1):
                    result_arr.append(matrix[bottom_row][col])
                bottom_row -= 1

            # Traverse up on left column
            if left_col <= right_col:
                for row in range(bottom_row, top_row - 1, -1):
                    result_arr.append(matrix[row][left_col])
                left_col += 1

        return result_arr
