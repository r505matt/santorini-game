from . import tower

class Board:
    def __init__(self) -> None:
        self.grid = [[tower.Tower for i in range(5)] for j in range(5)]

    def __getitem__(self, index: list):
        row, col = index[0], index[1]
        return self.grid[row][col]

    def is_valid_move(self, start, end):
        if self[start].get_level - self[end].get_level <= -2:
            return False
        else:
            return True
    
    def get_valid_moves(self, pos) -> list:
        pass