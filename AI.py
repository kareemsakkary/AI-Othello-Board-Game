from Player import Player


class AI(Player):
    def __init__(self, name, color):
        super().__init__(name, color)
        self.name = name

    def play_move(self, valid_moves):
        pass
