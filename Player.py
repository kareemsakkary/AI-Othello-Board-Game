from abc import ABC, abstractmethod


class Player(ABC):
    def __init__(self, name, color):
        self.name = name
        self.color = color

    @abstractmethod
    def play_move(self, valid_moves):
        pass
