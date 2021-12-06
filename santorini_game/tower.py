class Tower:
    def __init__(self):
        self.level = 0

    def get_level(self):
        return self.level

    def build(self):
        if self.level <= 3:
            self.level += 1
            return True
        else:
            return False

    def is_winning_tower(self):
        return self.level == 3
        
    def is_capped_tower(self):
        return self.level == 4