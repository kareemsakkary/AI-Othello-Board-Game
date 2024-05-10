import Board
import Human
import AI
import copy
board = Board.Board()
player = AI.AI("Nour", 'B', "easy")

board.print_board()
tempBoard = copy.deepcopy(board)
cell = player.play_move(tempBoard)
move = board.make_move(player, cell)
board.print_board()

