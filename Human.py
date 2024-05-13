from Player import Player
from Cell import Cell


class Human(Player):
    def __init__(self, name, color):
        super().__init__(name.capitalize(), color)

    def play_move(self, board):
        valid_moves = board.valid_moves(self)
        if len(valid_moves) == 0:
            print("No valid moves available. Passing the turn.")
            return None
        print("Enter your move: ")
        x = int(input("Enter row: "))
        y = int(input("Enter column: "))
        cell = Cell(x, y, self.color)
       
        while cell not in valid_moves:
            print("Please re-enter a valid move: ")
            x = int(input("Enter row: "))
            y = int(input("Enter column: "))
            cell = Cell(x, y, self.color)
        return cell
