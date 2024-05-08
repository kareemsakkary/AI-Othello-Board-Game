import Player

class Human(Player.Player):
    def __init__(self, name):
        Player.__init__(self, name)
        self.name = name

    def play_move(self, valid_moves):
        pass