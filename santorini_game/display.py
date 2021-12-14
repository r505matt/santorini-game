import os
import utils
import board
from termcolor import cprint

class Display:
    COLORS = utils.Constants.COLORS
    ROW_BREAK = "---------------------"
    LEGEND_SPACING = "          "
    def __init__(self, board) -> None:
        self.board = board

    def print_board(self):
        print(self.ROW_BREAK)
        for row in range(4, -1, -1):
            print("|", end = "")
            for col in range(5):
                current = [row, col]
                if self.board.isempty(current):
                    grid_space = "   "
                else:
                    token = self.board.board_get_token(current)
                    grid_space = " {sym} ".format(token.get_symbol)
                level = self.board.board_level([row, col])
                cprint(grid_space, "grey", self.COLORS[level], end="")
                print("|", end="")
            self.print_legend(row)
            print(self.ROW_BREAK)

    def clear(self):
        os.system('clear')

    def print_legend(self, row_num):
        print(self.LEGEND_SPACING, end="")
        cprint("level {}".format(row_num), "grey", self.COLORS[row_num])

    def render(self):
        self.clear()        
        self.print_board()
        print(" ")
        print("Directions?")
        x = input()
