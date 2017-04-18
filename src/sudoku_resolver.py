#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""SudokuResolver class."""

import pandas as pd
import numpy as np
import copy as cp


class SudokuResolver:

    sudoku_board = False

    allowed_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    help_board = False

    def __init__(self):
        """Constructor."""
        self.help_board = pd.DataFrame(np.zeros((9, 9))).astype(int)

    def load_board(self, board_name):
        """Load sudoku board to resolve."""
        self.sudoku_board = pd.read_csv(board_name)
        self.sudoku_board = self.sudoku_board.fillna(0.0).astype(int).replace(0, '-')

    def resolve_board(self):
        """Resolve sudoku board."""
        sq = []
        sq1 = self.get_subsquare(0, 3, 0, 3)
        self.fill_help_board(0, 3, 0, 3, 0)
        sq.append(self.allowed_in_square(sq1))
        sq2 = self.get_subsquare(0, 3, 3, 6)
        self.fill_help_board(0, 3, 3, 6, 1)
        sq.append(self.allowed_in_square(sq2))
        sq3 = self.get_subsquare(0, 3, 6, 9)
        self.fill_help_board(0, 3, 6, 9, 2)
        sq.append(self.allowed_in_square(sq3))
        sq4 = self.get_subsquare(3, 6, 0, 3)
        self.fill_help_board(3, 6, 0, 3, 3)
        sq.append(self.allowed_in_square(sq4))
        sq5 = self.get_subsquare(3, 6, 3, 6)
        self.fill_help_board(3, 6, 3, 6, 4)
        sq.append(self.allowed_in_square(sq5))
        sq6 = self.get_subsquare(3, 6, 6, 9)
        self.fill_help_board(3, 6, 6, 9, 5)
        sq.append(self.allowed_in_square(sq6))
        sq7 = self.get_subsquare(6, 9, 0, 3)
        self.fill_help_board(6, 9, 0, 3, 6)
        sq.append(self.allowed_in_square(sq7))
        sq8 = self.get_subsquare(6, 9, 3, 6)
        self.fill_help_board(6, 9, 3, 6, 7)
        sq.append(self.allowed_in_square(sq8))
        sq9 = self.get_subsquare(6, 9, 6, 9)
        self.fill_help_board(6, 9, 6, 9, 8)
        sq.append(self.allowed_in_square(sq9))
        rows = []
        for i in range(0, 9):
            rows.append(self.allowed_in_row(self.sudoku_board.iloc[i]))
        cols = []
        for i in range(0, 9):
            cols.append(self.allowed_in_col(self.sudoku_board[[i]]))
        for i in range(0, 9):
            for j in range(0, 9):
                if self.sudoku_board.loc[i][j] is '-':
                    self.sudoku_board.loc[i][j] = list(
                        set(rows[i]) & set(cols[j]) & set(sq[self.help_board.loc[i][j]])
                    )
        is_list = True
        while is_list:
            is_list = False
            for i in range(0, 9):
                for j in range(0, 9):
                    if type(self.sudoku_board.loc[i][j]) is list:
                        is_list = True
                        if len(self.sudoku_board.loc[i][j]) == 1:
                            sq_nr = self.help_board.loc[i][j]
                            one_el = self.sudoku_board.loc[i][j]
                            self.sudoku_board.loc[i][j] = one_el[0]
                            for k in range(0, 9):
                                for l in range(0, 9):
                                    if k == i or l == j or self.help_board.loc[k][l] == sq_nr:
                                        if type(self.sudoku_board.loc[k][l]) is list:
                                            values_list = self.sudoku_board.loc[k][l]
                                            if one_el[0] in values_list:
                                                values_list.remove(one_el[0])
                                                self.sudoku_board.loc[k][l] = values_list

    def get_subsquare(self, row_start=0, row_end=1, col_start=0, col_end=1):
        """Get subsquare from sudoku board."""
        return self.sudoku_board.iloc[row_start:row_end, col_start:col_end]

    def fill_help_board(self, row_start=0, row_end=1, col_start=0, col_end=1, value=0):
        """Fill help board."""
        self.help_board.iloc[row_start:row_end, col_start:col_end] = value

    def allowed_in_square(self, square):
        """Get list of allowed values in subsquare."""
        allowed = cp.copy(self.allowed_values)
        for i in range(0, 3):
            for j in range(0, 3):
                if square.iloc[i][j] in self.allowed_values:
                    allowed.remove(square.iloc[i][j])
        return allowed

    def allowed_in_row(self, row):
        """Get list of allowed values in row."""
        allowed = cp.copy(self.allowed_values)
        for i in range(0, 9):
            if row[i] in self.allowed_values:
                allowed.remove(row[i])
        return allowed

    def allowed_in_col(self, col):
        """Get list of allowed values in col."""
        allowed = cp.copy(self.allowed_values)
        for i in range(0, 9):
            if col.iloc[i][0] in self.allowed_values:
                allowed.remove(col.iloc[i][0])
        return allowed

    def get_board(self):
        """Get sudoku board."""
        return self.sudoku_board
