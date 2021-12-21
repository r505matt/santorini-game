class Player_Token:
    def __init__(self, player, player_symbol) -> None:
        self.player = player
        self.symbol = player_symbol
        self.pos = (-1, -1)
    
    def get_pos(self):
        return self.pos

    def set_pos(self, new_pos):
        self.pos = new_pos

    def get_symbol(self):
        return self.symbol