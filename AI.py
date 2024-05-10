import Player


class AI(Player.Player):
    def __init__(self, name, color, difficulty):
        super().__init__(name, color)
        self.difficulty = difficulty

    def play_move(self, valid_moves):
        return valid_moves[0]
