import Cell

class Board():
    def __init__(self):
        self.boards = []
        for i in range(8):
            self.boards.append([])
            for j in range(8):
                self.boards[i].append(Cell.cell(i, j, "E"))