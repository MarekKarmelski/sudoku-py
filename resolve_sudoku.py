#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""ResolveSudoku application."""

from src.sudoku_resolver import SudokuResolver
from pprint import pprint


class ResolveSudoku:

    def run(self):
        """Run application"""
        sr = SudokuResolver()
        sr.load_board('boards/board3.csv')
        sr.resolve_board()
        pprint(sr.get_board())
        pass

app = ResolveSudoku()
app.run()
