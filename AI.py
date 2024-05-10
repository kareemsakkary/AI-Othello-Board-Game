import Player


class AI(Player.Player):
    def __init__(self, name, color):
        super().__init__(name, color)

    def play_move(self, valid_moves):
        return valid_moves[0]
