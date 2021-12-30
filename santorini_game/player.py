import player_token
import utils

class Player:
    VALID_ROWS = utils.Constants.ROWS
    VALID_COLS = utils.Constants.COLS
    def __init__(self, num_players, player_symbol, board) -> None:
        self.board = board
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
            pos = self.choose_pos()
            if pos in board.get_token_positions():
                print("Space already taken")            
            else:
                current_token = self.tokens[self.place_tokens_index]
                current_token.set_pos(pos)
                self.place_tokens_index += 1
                return current_token

    def display_name(self):
        print("It is currently {}'s turn".format(self.player_symbols[0]))
        print("")

    def display_win_message(self):
        print("{} has won, the game is over!".format(self.player_symbols[0]))
        
    def choose_pos(self):
        while True:
            print("Choose a position:      ex.(A2)")
            pos = input()
            if self.is_valid_pos(pos):
                pos = self.pos_convert(pos.upper())
                return pos

    def is_valid_pos(self, preconvetered_pos):
        if len(preconvetered_pos) != 2:
            print("Invalid Input")
            return False
        pos = preconvetered_pos.upper()
        if pos[0] not in self.VALID_ROWS or pos[1] not in self.VALID_COLS:
            print("Out of bounds")
            return False
        return True
        

    def pos_convert(self, str):
        row = self.VALID_ROWS.index(str[0])
        col = self.VALID_COLS.index(str[1])
        return [row, col]

    def choose_token(self):
        choice = None
        while True:
            print("Choose which token to use: ")
            choice = input()
            if choice in self.player_symbols:
                break
            else:
                print("Invalid choice")
        for token in self.tokens:
            if token.get_symbol() == choice:
                return token
        print("something went horribly wrong") #TODO remove
    
    def move_choice(self, valid_moves):
        print("Possible moves include: ", end="")
        for move in valid_moves:
            row, col = move[0], move[1]
            row = self.VALID_ROWS[row]
            col = self.VALID_COLS[col]
            print("{}{}  ".format(row, col), end="")
        print("")
        while True:
            print("Choose a space to move the selected token to: ")
            pos = input()
            if self.is_valid_pos(pos):
                pos = self.pos_convert(pos.upper())
                if pos in valid_moves:
                    return pos
                else:
                    print("Invalid move position")

    def build_choice(self, valid_builds): 
        print("Possible builds include: ", end="")
        for build in valid_builds:
            row, col = build[0], build[1]
            row = self.VALID_ROWS[row]
            col = self.VALID_COLS[col]
            print("{}{}  ".format(row, col), end="")
        print("")
        while True:
            print("Choose a space to build in: ")
            pos = input()
            if self.is_valid_pos(pos):
                pos = self.pos_convert(pos.upper())
                if pos in valid_builds:
                    return pos
                else:
                    print("Invalid build position")
        
    def collect_adj(self, chosen_token, build = False):
        current_pos = chosen_token.get_pos()
        valid_moves = self.board.get_valid_moves(current_pos, build)
        return valid_moves