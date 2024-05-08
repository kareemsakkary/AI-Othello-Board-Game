import Player

class Human(Player.Player):
    def __init__(self, name, color):
        Player.__init__( name, color)
        self.name = name
        self.color = color

    def play_move(self, valid_moves):
        pass