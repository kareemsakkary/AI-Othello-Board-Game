import Player
import Cell


class Human(Player.Player):
    def __init__(self, name, color):
        super().__init__(name.capitalize(), color)

    def play_move(self, board):
        print("Enter your move: ")
        x = int(input("Enter row: "))
        y = int(input("Enter column: "))
        cell = Cell.Cell(x, y, self.color)
        valid_moves = board.valid_moves(self)
        while cell not in valid_moves:
            print("Please re-enter a valid move: ")
            x = int(input("Enter row: "))
            y = int(input("Enter column: "))
            cell = Cell.Cell(x, y, self.color)
        return cell
