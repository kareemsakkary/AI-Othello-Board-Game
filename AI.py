from Player import Player
import copy
from Human import Human


class AI(Player):
    def __init__(self, name, color, difficulty):
        super().__init__(name, color)
        self.difficulty = difficulty

    def evaluate(self, temp_board):
        valid_moves = temp_board.valid_moves(self)
        # 1 point for player's current cell color
        # 5 points for a valid move
        # 10 points if a valid move is on the edge/border of the board
        # 15 points if a valid move is a corner
        # 20 points if a cell of my color can't be outflanked by the opponent

        val = 0
        # add 1 for each cell player's color and minus the opponent color cells
        if self.color == "B":
            val += temp_board.countBlack - temp_board.countWhite
        else:
            val += temp_board.countWhite - temp_board.countBlack

        # Add 5 points for the number of valid moves
        val += 5 * len(valid_moves)

        # loop on valid moves and check it is a corner or on edge and can be outflanked
        for move in valid_moves:
            val += 10 if temp_board.is_border(move.x, move.y) else -10
            val += 15 if temp_board.is_corner(move.x, move.y) else -15
            val += 20 if not temp_board.can_outflank(self, move) else -20

        return [val, None]

    def alphabeta(self, temp_board, depth, alpha, beta, is_maximizing):
        if temp_board.game_over():
            return self.evaluate(temp_board)

        if depth == 0:
            return self.evaluate(temp_board)

        if is_maximizing:
            best_score = float('-inf')
            best_move = None
            for move in temp_board.valid_moves(Human("dummy", self.color)):
                temp = temp_board
                temp_board.make_move(Human("dummy", self.color), move)  # update max player with this move
                score = self.alphabeta(temp_board, depth - 1, alpha, beta, False)[0]
                temp_board = temp  # undo move
                if score > best_score:
                    best_score = score
                    best_move = move
                alpha = max(alpha, best_score)
                if beta <= alpha:
                    break
            return [best_score, best_move]

        else:
            best_score = float('inf')
            best_move = None
            for move in temp_board.valid_moves(Human("dummy", 'W' if self.color == 'B' else 'B')):
                temp = temp_board
                temp_board.make_move(Human("dummy", 'W' if self.color == 'B' else 'B'), move)  # update min player with this move
                score = self.alphabeta(temp_board, depth - 1, alpha, beta, True)[0]  # undo move
                temp_board = temp  # undo move
                if score < best_score:
                    best_score = score
                    best_move = move
                beta = min(beta, best_score)
                if beta <= alpha:
                    break
            return [best_score, best_move]

    def play_move(self, board):
        print("AI is thinking...")
        temp_board = copy.deepcopy(board)
        best_move = self.alphabeta(temp_board, self.difficulty, float('-inf'), float('inf'), True)[1]
        if best_move:
            print(f"AI has made a move at cell: ({best_move.x}, {best_move.y})")
        else:
            print("No moves for Ai to do")
        return best_move
