import os
import random


'''how to do 2 arrays one for '*' and the actual board'''

class board:

    BOARD_SIZE = 8
    MINES = 10
    BOMB = 'X'
    
    def __init__(self):
        self.grid = [[" " for i in range(self.BOARD_SIZE)] for j in range(self.BOARD_SIZE)]

    def draw(self):
        columns = "    ".join([str(i) for i in range(self.BOARD_SIZE)])
        print("\n     ", columns)
        y = 0
        for row in self.grid:
            print(" ", y, row)
            y += 1
        print("\n", self.MINES, "mines remaining")
    
    def mines(self):
        _n = 0
        while _n <= self.MINES:
            x = random.randint(0, self.BOARD_SIZE - 1)
            y = random.randint(0, self.BOARD_SIZE - 1)
            if self.grid[y][x] == ' ':
                self.grid[x][y] = 'X'
            _n += 1

    def numbers(self):
        _n = 0
        for y in range(self.BOARD_SIZE):
            for x in range(self.BOARD_SIZE):
                if self.grid[y][x] == ' ':
                    _n = self._check_row(y, x)
                    _n += self._check_col(y, x)
                    if _n != 0:
                        self.grid[y][x] = str(_n)

    def _check_row(self, y, x):
        _n = 0
        try:
            for i in range(x - 1, x + 2, 2):
                if self.grid[y][i] == 'X':
                    _n += 1
        except:
            pass
        return _n

    def _check_col(self, y, x):
        _n = 0
        try:
            for i in range(y - 1, y + 2, 2):
                if self.grid[i][x] == 'X':
                    _n += 1
        except:
            pass
        return _n
            
def play_minesweeper():
    game = board()
    game.mines()
    game.numbers()
    while True:
        os.system("clear")
        game.draw()
        row = int(input("\nrow: "))
        column = int(input("column: "))
        

if __name__ == '__main__':
    play_minesweeper()
