import tower
import utils
class Board:
    DIRECTIONS = utils.Constants.DIRECTIONS
    def __init__(self) -> None:
        self.grid = [[tower.Tower() for i in range(5)] for j in range(5)]

    def __getitem__(self, index: list):
        row, col = index[0], index[1]
        return self.grid[row][col]

    def is_valid_move(self, start, end):
        if self[start].get_level() - self[end].get_level() <= -2: #cannot jump up 2 levels, can jump down
            return False
        elif end[0] < 0 or end[0] > 4 or end[1] < 0 or end[1] > 4: #checks for out of bounds
            return False
        else:
            return True
    
    def get_valid_moves(self, pos) -> list:
        valid_moves = []
        current_row, current_col = pos[0], pos[1]
        for direction, change_row_col_tuple in self.DIRECTIONS:
            new_row = current_row + change_row_col_tuple[0]
            new_col = current_col + change_row_col_tuple[1]
            new_pos = [new_row, new_col]
            if self.is_valid_move(self, pos, new_pos):
                valid_moves.append(direction)
        return valid_moves

    def board_level(self, pos):
         return self[pos].get_level()

    def move_player_token(self, token, end_pos):
        pass