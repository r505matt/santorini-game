import token

class Player:
    def __init__(self, num_players, player_symbol) -> None:
        self.tokens = []
        if num_players == 4:
            token_count = 1
        else:
            token_count = 2
        for i in range(token_count):
            self.tokens.append(token.Token(self, player_symbol))
    
    def choose_token(self):
        pass
    
    def move_action(self):
        pass

    def build_action(self):
        pass