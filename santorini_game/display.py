from . import board
from . import utils
from termcolor import colored, cprint

class Display:
    COLORS = utils.COLORS
    ROW_BREAK = "---------------------"
    def __init__(self, board) -> None:
        self.board = board.Board()
    
    def print_board(self):
        print(self.ROW_BREAK)
        for row in range(4, -1, -1):
            print("|", end = "")
            for col in range(5):
                level = self.board[row, col].get_level()
                cprint("  ", "white", COLORS[level], end="")
                print("|", end="")
            print(self.ROW_BREAK)

                