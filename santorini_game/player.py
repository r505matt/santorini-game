import player_token
import utils

class Player:
    VALID_ROWS = utils.Constants.ROWS
    VALID_COLS = utils.Constants.COLS
    def __init__(self, num_players, player_symbol) -> None:
        self.tokens = []
        self.place_tokens_index = 0
        self.player_symbols = [player_symbol.upper(), player_symbol.lower()]
        if num_players == 4:
            self.player_symbols.pop(1)
        for sym in self.player_symbols:
            new_token = player_token.Player_Token(self, sym)
            self.tokens.append(new_token)
        

    def place_starting_tokens(self, board): 
        while True:
            print("Choose a starting position:    ex.(A2)")
            pos = input()
            if len(pos) == 3:                
                pos = list(map(int, pos.split()))
            else:
                print("Invalid Input")
                continue
            if pos[0] < 0 or pos[1] < 0 or pos[0] > 4 or pos[1] > 4: #TODO needs more error checking
                print("Out of Bounds")
                continue
            elif pos in board.get_token_positions():
                print("Space already taken")
                continue
            else:
                current_token = self.tokens[self.place_tokens_index]
                current_token.set_pos(pos)
                self.place_tokens_index += 1
                return current_token

    def choose_pos(self):
        while True:
            print("Choose a positiong:      ex.(A2)")
            pos = input()
            if len(pos) != 2:
                print("Invalid Input")
                continue
            if pos[0] not in self.VALID_ROWS or pos[1] not in self.VALID_COLS:
                print ("Out of bounds")
            
    def choose_token(self):
        choice = None
        while choice not in self.player_symbols:
            print("Choose which token to use: ")
            choice = input()
        
    
    def move_action(self):
        pass

    def build_action(self):
        pass