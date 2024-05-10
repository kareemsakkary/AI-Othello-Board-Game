from Player import Player
import copy
from Human import Human


class AI(Player):
    def __init__(self, name, color, difficulty):
        super().__init__(name, color)
        self.difficulty = difficulty

    def evaluate(self, temp_board):
        # num_black_valid_moves = len(temp_board.valid_moves(Human("dummy", 'B')))
        # num_white_valid_moves = len(temp_board.valid_moves(Human("dummy", 'W')))
        # if self.color == "B":
        #     return [num_black_valid_moves, None]
        # else:
        #     return [num_white_valid_moves, None]

        if self.color == "B":
            return [temp_board.countBlack - temp_board.countWhite, None]
        else:
            return [temp_board.countWhite - temp_board.countBlack, None]
    
    def alphabeta(self, temp_board, depth, alpha, beta, is_maximizing):
        # if temp_board.game_over:
        #     return self.evaluate(temp_board)

        if depth == 0:
            return self.evaluate(temp_board)

        if is_maximizing:
            best_score = float('-inf')
            best_move = None
            for move in temp_board.valid_moves(Human("dummy", self.color)):
                temp = copy.deepcopy(temp_board)
                temp_board.make_move(Human("dummy", self.color), move)  # update max player with this move
                score = self.alphabeta(temp_board, depth - 1, alpha, beta, False)[0]
                temp_board = temp  # undo move
                if score > best_score:
                    best_score = score
                    best_move = move
                alpha = max(alpha, score)
                if beta <= alpha:
                    break
            return [best_score, best_move]

        else:
            best_score = float('inf')
            best_move = None
            for move in temp_board.valid_moves(Human("dummy", 'W' if self.color == 'B' else 'B')):
                temp = copy.deepcopy(temp_board)
                temp_board.make_move(Human("dummy", 'W' if self.color == 'B' else 'B'), move)  # update min player with this move
                score = self.alphabeta(temp_board, depth - 1, alpha, beta, True)[0]  # undo move
                temp_board = temp
                if score < best_score:
                    best_score = score
                    best_move = move
                beta = min(beta, score)
                if beta <= alpha:
                    break
            return [best_score, best_move]

    def play_move(self, board):
        print("AI is thinking...")
        best_move = self.alphabeta(board, self.difficulty, float('-inf'), float('inf'), True)[1]
        print(f"AI has made a move at cell: ({best_move.x}, {best_move.y})")
        return best_move
