
class Player():
    def __init__(self, name, color):
        self.name = name
        self.color = color
    
    # write abstract play_move() method here
    def play_move(self, board, valid_moves):
        pass

    def get_name(self):
        return self.name

    def get_score(self):
        return self.score

    def set_score(self, score):
        self.score = score

    def __str__(self):
        return self.name + " " + str(self.score)