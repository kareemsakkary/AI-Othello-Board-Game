import Player
import Cell

class Human(Player.Player):
    def __init__(self, name, color):
        Player.__init__( name, color)
        self.name = name
        self.color = color

    def play_move(self, valid_moves):
        print("Enter your next move: ")
        x = int(input("Enter row: "))
        y = int(input("Enter column: "))
        cell = Cell(x, y, self.color)
        while(cell not in valid_moves):
            print("Please re-enter a valid move: ", end="")
            x = int(input("Enter row: "))
            y = int(input("Enter column: "))
            cell = Cell(x, y, self.color)
        return cell
        

player1 = Human("Nour", 'W')