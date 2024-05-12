from Player import Player
import copy
from Human import Human


class AI(Player):
    def __init__(self, name, color, difficulty):
        super().__init__(name, color)
        self.difficulty = difficulty

    def evaluate(self, temp_board):
        # 5 points player's color cells greater than the opponent color cells else -5
        # 10 points if number of valid moves greater than opponent else -10
        # 10 points if a cell with my color at the edge/border of the board else -10
        # 15 points if a cell with my color at the corner of the board else -15
        # 20 points cells can't be outflanked by the opponent greater than cells can't be outflanked by the player else -20

        valid_moves = temp_board.valid_moves(self)
        opponent_valid_moves = temp_board.valid_moves(Human("dummy", 'W' if self.color == 'B' else 'B'))

        val = 0
        # add 1 for each cell player's color and minus the opponent color cells
        if temp_board.countBlack > temp_board.countWhite:
            val += 5 * (1 if self.color == 'B' else (-1))
        else:
            val -= 5 * (1 if self.color == 'B' else (-1))

        if len(valid_moves) > len(opponent_valid_moves):
            val += 10 
        else:
            val -= 10

        cntPlayerBorder = 0
        cntOppoBorder = 0
        cntPlayerCorner = 0
        cntOppoCorner = 0
        for i in range(8):
            for j in range(8):
                if(temp_board.is_border(i, j)):
                    cntPlayerBorder += (temp_board.board[i][j].color == self.color)
                    cntOppoBorder += (temp_board.board[i][j].color == ("W" if self.color == "B" else "B"))
                if(temp_board.is_corner(i, j)):
                    cntPlayerCorner += (temp_board.board[i][j].color == self.color)
                    cntOppoCorner += (temp_board.board[i][j].color == ("W" if self.color == "B" else "B" )   )    
        if(cntPlayerBorder > cntOppoBorder):
            val += 10
        else:
            val -= 10

        if(cntPlayerCorner > cntOppoCorner):
            val += 20
        else:
            val -= 20

        cntPlayerOutflank = temp_board.count_can_outflank(self)
        cntOppoOutflank = temp_board.count_can_outflank(Human("dummy", 'W' if self.color == 'B' else 'B'))
        if(cntPlayerOutflank > cntOppoOutflank):
            val += 10
        else:
            val -= 10

        return [val, None]

    def alphabeta(self, temp_board, depth, alpha, beta, is_maximizing):
        if temp_board.game_over():
            return self.evaluate(temp_board)

        if depth == 0:
            return self.evaluate(temp_board)

        if is_maximizing:
            best_score = float('-inf')
            best_move = None
            if(len(temp_board.valid_moves(Human("dummy", self.color))) == 0):
                return self.alphabeta(temp_board, depth, alpha, beta, False)

            for move in temp_board.valid_moves(Human("dummy", self.color)):
                temp = copy.deepcopy(temp_board)
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
            if(len(temp_board.valid_moves(Human("dummy", 'W' if self.color == 'B' else 'B'))) == 0):
                return self.alphabeta(temp_board, depth, alpha, beta, True)
            for move in temp_board.valid_moves(Human("dummy", 'W' if self.color == 'B' else 'B')):
                temp = copy.deepcopy(temp_board)
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
