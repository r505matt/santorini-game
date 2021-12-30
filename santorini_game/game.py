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
        self.setup_player_count()
        for num in range(self.player_count):
            self.setup_player()
        self.current_player_index = 0
        self.starting_positions()

    def setup_player_count(self):  # TODO make the game capable of 2-4 players
        self.player_count = 2  

    def setup_player(self):
        player_symbol = self.choose_symbol()
        new_player = player.Player(self.player_count, player_symbol)
        self.players.append(new_player)

    def choose_symbol(self):
        player_symbol = ""
        while not player_symbol.isalnum() or len(player_symbol) != 1: #TODO error checking, should only be 1 alphanum, seems off
            print("Choose a player symbol: ")
            player_symbol = input() 
            if player_symbol in self.chosen_symbols:
                print("Symbol already chosen")
                player_symbol = ""
        self.chosen_symbols.append(player_symbol)
        return player_symbol

    def starting_positions(self): # TODO make the game capable of 2-4 players
        placed_tokens = []
        while len(placed_tokens) != 4: # part of above TODO
            self.display.render()
            current_player = self.players[self.current_player_index]
            player_token = current_player.place_starting_tokens(self.board)
            placed_tokens.append(player_token)
            self.board.add_token(player_token)
            self.next_player()

    def run_game(self):
        self.display.render()
        x = input()

    def next_player(self):
        self.current_player_index = (self.player_count + self.current_player_index + 1) % self.player_count

if __name__ == "__main__":
    game = Game()
    game.run_game()