from abc import ABC, abstractmethod
import Board


class Controller(ABC):
    def __init__(self):
        self.board = Board.Board()
        self.player1 = None
        self.player2 = None

    @abstractmethod
    def display_ui(self, player=None):
        pass

    @abstractmethod
    def display_final_score(self):
        pass

    @abstractmethod
    def initialize_players(self):
        pass

    @abstractmethod
    def play_game(self):
        pass
