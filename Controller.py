import Board
import Player

class Controller():
    def __init__(self):
        self.board = Board.Board()
        self.player1 = None
        self.player2 = None
    
    @abstractmethod
    def play_game(self):
        pass