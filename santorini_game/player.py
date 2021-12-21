import player_token

class Player:
    def __init__(self, num_players, player_symbol) -> None:
        self.tokens = []
        if num_players == 4:
            token_count = 1
        else:
            token_count = 2
        for i in range(token_count):
            new_token = player_token.Player_Token(self, player_symbol)
            self.tokens.append(new_token)
        self.place_tokens_index = 0

    def place_starting_tokens(self, board): 
        while True:
            print("Choose a starting position: ")
            pos = input()
            if len(pos) == 3:                
                pos = list(map(int, pos.split()))
            else:
                print("Invalid Input")
                continue
            if pos[0] < 0 or pos[1] < 0 or pos[0] > 4 or pos[1] > 4: #TODO needs more error checking
                print("Improper input")
                continue
            elif pos in board.get_token_positions():
                print("Space already taken")
                continue
            else:
                current_token = self.tokens[self.place_tokens_index]
                current_token.set_pos(pos)
                self.place_tokens_index += 1
                return current_token
    
    def choose_token(self):
        pass
    
    def move_action(self):
        pass

    def build_action(self):
        pass