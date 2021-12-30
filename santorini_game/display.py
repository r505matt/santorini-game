import os
import utils
from termcolor import cprint

class Display:
    COLORS = utils.Constants.COLORS
    ROW_BREAK = "   ---------------------"
    LEGEND_SPACING = "          "
    ROWS = utils.Constants.ROWS
    def __init__(self, board) -> None:
        self.board = board

    def print_board(self):
        print(self.ROW_BREAK)
        for row in range(4, -1, -1):
            self.print_row_legend(row)
            print("|", end = "")
            for col in range(5):
                current = [row, col]
                if self.board.isempty(current):
                    grid_space = "   "
                else:
                    player_token = self.board.board_get_token(current)
                    grid_space = " {0} ".format(player_token.get_symbol())
                level = self.board.board_level([row, col])
                cprint(grid_space, "grey", self.COLORS[level], end="")
                print("|", end="")
            self.print_color_legend(row)
            print(self.ROW_BREAK)
        self.print_col_legend()
        print("")

    def clear(self):
        os.system('clear')

    def print_color_legend(self, row_num):
        print(self.LEGEND_SPACING, end="")
        cprint("level {0}".format(row_num), "grey", self.COLORS[row_num])

    def print_row_legend(self, row_num):
        print(" {0} ".format(self.ROWS[row_num]), end="")

    def print_col_legend(self):
        print("     ", end="")
        for num in range(1,6):
            print("{0}   ".format(num), end="")
        print("       Color Legend")

    def render(self):
        self.clear()        
        self.print_board()
