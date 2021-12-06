import os
from . import board
from . import utils
from termcolor import colored, cprint

class Display:
    COLORS = utils.COLORS
    ROW_BREAK = "---------------------"
    LEGEND_SPACING = "          "
    def __init__(self, board) -> None:
        self.board = board.Board()
    
    def print_board(self):
        print(self.ROW_BREAK)
        for row in range(4, -1, -1):
            print("|", end = "")
            for col in range(5):
                level = self.board[row, col].get_level()
                cprint("  ", "white", Display.COLORS[level], end="")
                print("|", end="")
            self.print_legend(row)
            print(self.ROW_BREAK)

    def clear(self):
        os.system('clear')

    def print_legend(self, row_num):
        print(self.LEGEND_SPACING, end="")
        cprint("level {row_num}", Display.COLOR[row_num])

    def render(self):
        self.clear        
        self.print_board
        print(" ")
        print("Directions?")
