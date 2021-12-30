import tower
import utils
class Board:
    DIRECTIONS = utils.Constants.DIRECTIONS
    def __init__(self) -> None:
        self.grid = [[tower.Tower() for i in range(5)] for j in range(5)]
        self.tokens = []
        self.token_positions = []

    def get_token_positions(self):
        return self.token_positions
        
    def __getitem__(self, index: list):
        row, col = index[0], index[1]
        return self.grid[row][col]

    def is_valid_move(self, start, end, build = False):
        if end[0] < 0 or end[0] > 4 or end[1] < 0 or end[1] > 4:  # checks for out of bounds
            return False
        elif (self[start].get_level() - self[end].get_level() <= -2) and build == False: #cannot jump up 2 levels, can jump down
            return False        
        elif self[end].get_level() == 4: #cannot move onto domed territory
            return False
        elif not self.isempty(end): #if there's a token there already
            return False
        else: 
            return True
    
    def isempty(self, pos): 
        if pos in self.token_positions or self.board_level(pos) == 4:
            return False
        else:
            return True

    def board_get_token(self, pos):
        for player_token in self.tokens:
            if player_token.get_pos() == pos:
                return player_token

    def update_token_positions(self):
        self.token_positions = []
        for player_token in self.tokens:
            self.token_positions.append(player_token.get_pos())

    def get_valid_moves(self, pos, build = False) -> list:
        valid_moves = []
        current_row, current_col = pos[0], pos[1]
        for direction in self.DIRECTIONS:
            change_row_col_tuple = self.DIRECTIONS[direction]
            new_row = current_row + change_row_col_tuple[0]
            new_col = current_col + change_row_col_tuple[1]
            new_pos = [new_row, new_col]
            if self.is_valid_move(pos, new_pos, build):
                valid_moves.append(new_pos)
        return valid_moves

    def add_token(self, token):
        self.tokens.append(token)
        self.update_token_positions()

    def board_level(self, pos):
         return self[pos].get_level()

    def board_build(self, pos):
        self[pos].build()

    def move_player_token(self, token, end_pos):
        token.set_pos(end_pos)

    def collect_adj(self, token, build=False):
        current_pos = token.get_pos()
        valid_moves = self.get_valid_moves(current_pos, build)
        return valid_moves
