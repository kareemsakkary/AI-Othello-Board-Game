import Player
import Cell


class Human(Player.Player):
    def __init__(self, name, color):
        super().__init__(name.capitalize(), color)

    def play_move(self, valid_moves):
        # to be edited to play moves only from valid moves list and not occupy invalid cells
        return Cell.Cell(int(input("Enter x: ")), int(input("Enter y: ")), self.color)
