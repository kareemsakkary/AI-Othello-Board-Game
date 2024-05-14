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
                self.board[i].append(Cell(i, j, "E"))
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
                        while self.valid(nx, ny) and self.board[nx][ny].color != player.color:
                            if self.board[nx][ny].color == "E":
                                if not added.get(self.board[nx][ny]) and found_opponent:
                                    valid_moves.append(self.board[nx][ny])
                                    added[self.board[nx][ny]] = True
                                break
                            else:
                                found_opponent = True
                            nx = nx + dx[k]
                            ny = ny + dy[k]
        return valid_moves
    
    def make_move(self, player, cell):
        x = cell.x
        y = cell.y
        if self.board[x][y].color != "E":
            return False
        valid_move = False
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            while self.valid(nx, ny) and self.board[nx][ny].color != 'E':
                if self.board[nx][ny].color == player.color:
                    sx = x
                    sy = y
                    valid_move = True
                    while sx != nx or sy != ny:
                        if(sx != x or sy != y):
                            if player.color == "B":
                                self.countBlack += 1
                                self.countWhite -= 1
                            else:
                                self.countWhite += 1
                                self.countBlack -= 1
                        self.board[sx][sy].color = player.color
                        sx = sx + dx[k]
                        sy = sy + dy[k]
                    break
                nx = nx + dx[k]
                ny = ny + dy[k]
        if not valid_move:
            return False
        self.board[x][y].color = player.color
        if player.color == "B":
            self.countBlack += 1
        else:
            self.countWhite += 1
        return True
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

    def game_over(self):
        valid_black = self.valid_moves(Human("dummy", "B"))
        valid_white = self.valid_moves(Human("dummy", "W"))
        if (len(valid_black) == 0 and len(valid_white) == 0) or self.countBlack == 32 or self.countWhite == 32:
            return True
        return False
    
    def reset(self):
        self.board = []
        for i in range(8):
            self.board.append([])
            for j in range(8):
                self.board[i].append(Cell(i, j, "E"))
        self.board[3][3].color = "W"
        self.board[3][4].color = "B"
        self.board[4][3].color = "B"
        self.board[4][4].color = "W"
        self.countBlack = 2
        self.countWhite = 2

    def is_corner(self, x, y):
        # check if the given cell is a corner
        return (x, y) in [(0, 0), (0, 7), (7, 0), (7, 7)]

    def is_border(self, x, y):
        # check if the given cell is on the border of the board
        return (x == 0 or x == 7 or y == 0 or y == 7) and not self.is_corner(x, y)

    def count_can_outflank(self, player):
        valid_moves = []
        added = {}
        counted = {}
        c = 0
        for x in range(8):
            for y in range(8):
                if self.board[x][y].color == player.color:
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        found_opponent = False
                        temp = 0
                        while self.valid(nx, ny) and self.board[nx][ny].color != player.color:
                            if self.board[nx][ny].color == "E":
                                if not added.get(self.board[nx][ny]) and found_opponent:
                                    valid_moves.append(self.board[nx][ny])
                                    added[self.board[nx][ny]] = True
                                    c += temp
                                break
                            else:
                                if(not counted.get(self.board[nx][ny])):
                                    temp += 1
                                    counted[self.board[nx][ny]] = True
                                found_opponent = True
                            nx = nx + dx[k]
                            ny = ny + dy[k]
        return c

    
    
