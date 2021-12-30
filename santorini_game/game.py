import display
import board
import player
import sys

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
        self.current_player = self.players[self.current_player_index]
        self.starting_positions()

    def setup_player_count(self):  # TODO make the game capable of 2-4 players
        self.player_count = 2  

    def setup_player(self):
        player_symbol = self.choose_symbol()
        new_player = player.Player(self.player_count, player_symbol, self.board)
        self.players.append(new_player)

    def choose_symbol(self):
        player_symbol = ""
        while not player_symbol.isalpha() or len(player_symbol) != 1: #TODO error checking, should only be 1 alphanum, seems off
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
            self.current_player.display_name()
            player_token = self.current_player.place_starting_tokens(self.board)
            placed_tokens.append(player_token)
            self.board.add_token(player_token)
            self.next_player()

    def run_game(self):
        while len(self.players) > 1:
            if self.take_turn():
                self.next_player()
            else:
                self.eliminate_player()
        self.game_over()
    
    def take_turn(self):
        self.display.render()
        self.current_player.display_name()
        chosen_token = self.current_player.choose_token()
        
        valid_moves = self.board.collect_adj(chosen_token)
        if len(valid_moves) < 1:
            return False            
        self.move_action(chosen_token, valid_moves)
        self.check_win(chosen_token)
        
        self.display.render()
        self.current_player.display_name()

        valid_builds = self.board.collect_adj(chosen_token, build = True)
        if len(valid_builds) < 1:
            return False
        self.build_action(valid_builds)
        return True

    def move_action(self, chosen_token, valid_moves):
        move_pos = self.current_player.move_choice(valid_moves)
        self.board.move_player_token(chosen_token, move_pos)
        self.board.update_token_positions()

    def build_action(self, valid_builds):
        build_pos = self.current_player.build_choice(valid_builds)
        self.board.board_build(build_pos)
        self.board.update_token_positions()

    def check_win(self, chosen_token):
        check_pos = chosen_token.get_pos()
        if self.board.board_level(check_pos) == 3:
            self.game_over()

    def eliminate_player(self):
        self.players.pop(self.current_player_index)
        if self.current_player_index == len(self.players):
            self.current_player_index -= 1
        self.current_player = self.players[self.current_player_index]

    def game_over(self):
        self.display.render()
        self.current_player.display_win_message()
        sys.exit()

    def next_player(self):
        self.current_player_index = (self.player_count + self.current_player_index + 1) % self.player_count
        self.current_player = self.players[self.current_player_index]

if __name__ == "__main__":
    game = Game()
    game.run_game()