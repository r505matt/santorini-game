from . import display
from . import board

class Game:
    def __init__(self) -> None:
        self.board = board.Board()
        self.display = display.Display(self.board)

    def run_game(self):
        while True:
            self.display.render


if __name__ == "__main__":
    game = Game()
    game.run_game
