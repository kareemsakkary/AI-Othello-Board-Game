from abc import ABC, abstractmethod


class Player(ABC):
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.coins = 30
    
    @abstractmethod
    def play_move(self, board):
        pass
