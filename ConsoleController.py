from Controller import Controller
from AI import AI
from Human import Human


class ConsoleController(Controller):
    def __init__(self):
        super().__init__()
        self.mode = None

    def display_ui(self, player=None):
        # initial board state
        if player is None:
            print("Start Playing!")
            self.board.print_board()
            return
        # print current player points and name
        print()
        print("-" + player.name + "'s turn" + " (" + player.color + ")")
        if player.color == "W":
            print("Current points: " + str(self.board.countWhite))
        else:
            print("Current points: " + str(self.board.countBlack))
        print()
        if player.name == "AI":
            self.board.print_board()
        else:
            valid_moves = self.board.valid_moves(player)
            # display valid moves for current player
            self.board.print_board(valid_moves)

    def display_final_score(self):
        # print final board state
        self.board.print_board()
        # print game over message
        print("****** Game Over ******")
        print("Final Score")
        # print player name and its final score
        black_color_name = self.player1.name if self.player1.color == "B" else self.player2.name
        white_color_name = self.player2.name if self.player2.color == "W" else self.player1.name
        print("-" + black_color_name + "'s points: " + str(self.board.countBlack) +
              "\t" +
              "-" + white_color_name + "'s points: " + str(self.board.countWhite))
        print()

        # check who wins
        if self.board.countBlack > self.board.countWhite:
            print(black_color_name + " wins the game!")
        elif self.board.countBlack < self.board.countWhite:
            print(white_color_name + " wins the game!")
        else:
            print("It's a tie!")
        print("Thanks for playing :)")

    def check_moves_left(self):
        # check if there are any valid moves left for both players
        return self.board.game_over()

    def choose_mode(self):
        valid_input = False
        print("Please choose the game mode:")
        print("1. Human vs Human")
        print("2. Human vs AI")
        name = None
        while not valid_input:
            mode_choice = input(">> ")
            if mode_choice == "1":
                self.mode = 1
                print("Please enter the second player name:")
                valid_input = True
                name = input(">> ")
            elif mode_choice == "2":
                self.mode = 2
                name = "AI"
                valid_input = True
            else:
                print("Invalid mode choice. Please choose Human vs Human or Human vs AI only.")
        return name

    def choose_difficulty(self):
        valid_input = False
        print("Please choose the AI difficulty level:")
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")
        while not valid_input:
            difficulty_choice = input(">> ")
            if difficulty_choice == "1":
                return 1
            elif difficulty_choice == "2":
                return 3
            elif difficulty_choice == "3":
                return 5
            else:
                print("Invalid difficulty choice. Please choose Easy, Medium or Hard only.")

    def initialize_players(self):
        print("Please enter your name:")
        name = input(">> ")
        second_player_name = self.choose_mode()
        print(name.capitalize() + ", please choose your preferred color choice:")
        print("1. Black")
        print("2. White")
        valid_input = False
        while not valid_input:
            color_choice = input(">> ")
            # Player 1 is always black and moves first
            if color_choice == "1":
                self.player1 = Human(name, 'B')
                # choose player 2 based on the mode
                if self.mode == 1:
                    self.player2 = Human(second_player_name, 'W')
                else:
                    self.player2 = AI("AI", 'W', self.choose_difficulty())
                valid_input = True
            elif color_choice == "2":
                # choose player 1 based on the mode
                if self.mode == 1:
                    self.player1 = Human(second_player_name, 'B')
                else:
                    self.player1 = AI("AI", 'B', self.choose_difficulty())
                self.player2 = Human(name, 'W')
                valid_input = True
            else:
                print("Invalid color choice. Please choose Black or White only.")

    def play_game(self):
        # initialize players name and color
        self.initialize_players()
        # display initial board state
        self.display_ui()
        # loop until there are no valid moves left
        while self.check_moves_left():
            # player 1 turn
            self.display_ui(self.player1)
            move = self.player1.play_move(self.board)
            if move:
                self.board.make_move(self.player1, move)
                self.player1.coins -= 1
            # player 2 turn
            self.display_ui(self.player2)

            move = self.player2.play_move(self.board)
            if move:
                self.board.make_move(self.player2, move)
                self.player2.coins -= 1
        # display final score
        self.display_final_score()
