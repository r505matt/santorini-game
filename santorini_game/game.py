from . import display

class Game:
    def __init__(self) -> None:
        self.display = display.Display()

    def run_game(self):
        while True:
            self.display.render


if __name__ == "__main__":
    game = Game()
    game.run_game
