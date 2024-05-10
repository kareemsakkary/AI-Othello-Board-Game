from Cell import Cell
from Human import Human
dx = [1, -1 , 0 , 0]
dy = [0,  0,  1, -1]


class Board:
    def __init__(self):
        self.board = []
        for i in range(8):
            self.board.append([])
            for j in range(8):
                self.board[i].append(Cell.Cell(i, j, "E"))
        self.board[3][3].color = "W"
        self.board[3][4].color = "B"
        self.board[4][3].color = "B"
        self.board[4][4].color = "W"
        self.countBlack = 2
        self.countWhite = 2

    def valid(self, x, y):
        return 0 <= x < 8 and 0 <= y < 8
    
    def valid_moves(self, player):
        valid_moves = []
        added = {}
        for x in range(8):
            for y in range(8):
                if self.board[x][y].color == player.color:
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        found_opponent = False
                        while self.valid(nx,ny) and self.board[nx][ny].color != player.color:
                            if self.board[nx][ny].color == "E" and found_opponent:
                                if not added.get(self.board[nx][ny]):
                                    valid_moves.append(self.board[nx][ny])
                                    added[self.board[nx][ny]] = True
                                break
                            elif self.board[nx][ny].color != "E":
                                found_opponent = True
                            nx = nx + dx[k]
                            ny = ny + dy[k]   
        return valid_moves

    def make_move(self, player, cell):
        x = cell.x
        y = cell.y
        self.board[x][y].color = player.color
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            while self.valid(nx, ny) and self.board[nx][ny].color != 'E':
                if self.board[nx][ny].color == player.color:
                    sx = x
                    sy = y
                    while sx != nx or sy != ny:
                        if player.color == "B":
                            self.countBlack += 1
                            self.countWhite -= 1
                        else:
                            self.countWhite += 1
                            self.countBlack -= 1
                        self.board[sx][sy].color = player.color
                        sx = sx + dx[k]
                        sy = sy + dy[k]
                    if player.color == "B":
                        self.countWhite += 1
                    else:
                        self.countBlack += 1
                    break
                nx = nx + dx[k]
                ny = ny + dy[k]
        return self.board
    
    def print_board(self, valid_moves=None):
        if valid_moves is None:
            valid_moves = []
        print(" ", end=" ")
        for i in range(8):
            print(i, end=" ")
        print()
        for i in range(8):
            print(i, end=" ")
            for j in range(8):
                if self.board[i][j] in valid_moves:
                    print("*", end=" ")
                elif self.board[i][j].color == "E":
                    print("-", end=" ")
                else:
                    print(self.board[i][j].color, end=" ")
            print()
        print()

    def reset(self):
        self.board = []
        for i in range(8):
            self.board.append([])
            for j in range(8):
                self.board[i].append(Cell.Cell(i, j, "E"))
        self.board[3][3].color = "W"
        self.board[3][4].color = "B"
        self.board[4][3].color = "B"
        self.board[4][4].color = "W"
        self.countBlack = 2
        self.countWhite = 2
    
    def game_over(self):
        validBlack = self.valid_moves(Human("dummy", "B"))
        validWhite = self.valid_moves(Human("dummy", "W"))
        if len(validBlack) == 0 and len(validWhite) == 0:
            if self.countBlack > self.countWhite:
                return "B"
            elif self.countBlack < self.countWhite:
                return "W"
            else:
                return "D"
        return False

# board = Board()
# Player = Human.Human("kareem",'B')
# li = board.valid_moves(Player)
# board.print_board()
# board.print_board(li)
#
# make = board.make_move(Player,li[1])
# li = board.valid_moves(Player)
# board.print_board(li)
# print(board.countBlack)
# print(board.countWhite)
