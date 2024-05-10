from Player import Player
import copy
class AI(Player):
    def __init__(self, name, color, difficulty):
        super().__init__(name, color )
        self.name = name
        self.difficulty = difficulty

    def evaluate(self, tempBoard):
        if(self.color == "B"):
            return [tempBoard.countBlack - tempBoard.countWhite, None]
        else:
            return [tempBoard.countWhite - tempBoard.countBlack, None]
    
    def alphabeta(self,tempBoard, depth, alpha, beta, is_maximizing):
        if tempBoard.game_over():
            return self.evaluate(tempBoard)

        if depth == 0:
            return self.evaluate(tempBoard)

        if is_maximizing:
            best_score = float('-inf')
            best_move = None
            for move in tempBoard.valid_moves(Player("dummy",self.color)):
                temp = copy.deepcopy(tempBoard)
                tempBoard.make_move(Player("dummy",self.color), move) # update max player with this move
                score = self.alphabeta(tempBoard, depth - 1, alpha, beta, False)[0]
                tempBoard = temp # undo move
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
            for move in tempBoard.valid_moves(Player("dummy", 'W' if self.color == 'B' else 'B')):
              
                temp = copy.deepcopy(tempBoard)
                tempBoard.make_move(Player("dummy", 'W' if self.color == 'B' else 'B'),move)  # update min player with this move
                score = self.alphabeta(tempBoard, depth - 1, alpha, beta, True)[0] #undo move
                tempBoard = temp
                if score < best_score:
                    best_score = score
                    best_move = move
                beta = min(beta, score)
                if beta <= alpha:
                    break
            return [best_score, best_move]
    
   
    def play_move(self , board):
        print("AI is thinking...")
        depth = 1
        if(self.difficulty == "normal"):
            depth = 3
        elif(self.difficulty == "hard"):
            depth = 5
        best_move = self.alphabeta(board, depth, float('-inf'), float('inf'), True)[1]
        return best_move
