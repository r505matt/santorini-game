import display
import board
import player

class Game:
    def __init__(self) -> None:
        self.board = board.Board()
        self.display = display.Display(self.board)
        self.players = []
        self.chosen_symbols = []
        self.game_setup()

    def game_setup(self):
        player_count = 2 #TODO make the game capable of 2-4 players
        for num in player_count:
            self.setup_player(player_count)

    def setup_player(self, player_count):
        player_symbol = self.choose_symbol()
        new_player = player.Player(player_count, player_symbol)
        self.players.append(new_player)

    def choose_symbol(self):
        player_symbol = None
        while not player_symbol.isalnum() or player_symbol.length() > 2:
            print("Choose a player symbol: ")
            player_symbol = input()
        self.chosen_symbols.append(player_symbol)
        return player_symbol

    def run_game(self):
        self.display.render()

if __name__ == "__main__":
    game = Game()
    game.run_game()