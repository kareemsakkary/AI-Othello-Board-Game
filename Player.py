
class Player():
    def __init__(self, name, score):
        self.name = name
        self.color = score
    
    # write abstract play_move() method here
    @abstractmethod
    def play_move(self, valid_moves):
        pass

    def get_name(self):
        return self.name

    def get_score(self):
        return self.score

    def set_score(self, score):
        self.score = score

    def __str__(self):
        return self.name + " " + str(self.score)