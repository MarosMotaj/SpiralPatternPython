#!/usr/bin/env python

from app import App


if __name__ == '__main__':
    app = App()
    matrix = [[11, 12, 13, 14],
              [22, 23, 24, 15],
              [21, 26, 25, 16],
              [20, 19, 18, 17]]

    print(app.solve_matrix(matrix))
