import os
import random

BOARD_SIZE = 8
MINES = 10
LAST_INDEX = BOARD_SIZE - 1

class board:
    
    def __init__(self):
        self.grid = [["*" for i in range(BOARD_SIZE)] for j in range(BOARD_SIZE)]

    def draw(self):
        columns = "    ".join([str(i) for i in range(BOARD_SIZE)])
        print("\n     ", columns)
        y = 0
        for row in self.grid:
            print(" ", y, row)
            y += 1
        print("\n", MINES, "mines remaining")

#   def reveal(self, x, y):
#      if self.grid[y][x] ==  

class mines:

    def __init__(self):
        self.grid = [[0 for i in range(BOARD_SIZE)] for j in range(BOARD_SIZE)]

    def mines(self):
        _n = 0
        while _n < MINES:
            x = random.randint(0, LAST_INDEX)
            y = random.randint(0, LAST_INDEX)
            if self.grid[y][x] == 0:
                self.grid[y][x] = 'X'
            elif self.grid[y][x] == 'X':
                continue
            _n += 1

    def draw(self):
        for row in self.grid:
            print(row)
        print("\n", MINES, "mines remaining")

    def numbers(self):
        _n = 0
        for y in range(BOARD_SIZE):
            for x in range(BOARD_SIZE):
                if self.grid[y][x] == 0:
                    _n = self._check_row(y, x)
                    _n += self._check_col(y, x)
                    _n += self._check_slash(y, x)
                    _n += self._check_backslash(y, x)
                    self.grid[y][x] = str(_n)
                    
    def _check_row(self, y, x):
        n = 0
        if x == 0:
            if self.grid[y][x + 1] == 'X':
                n += 1
        if x == LAST_INDEX:
            if self.grid[y][x - 1] == 'X':
                n += 1
        if 1 <= x and x < LAST_INDEX:
            for i in range(x - 1, x + 2, 2):
                if self.grid[y][i] == 'X':
                    n += 1
        return n

    def _check_col(self, y, x):
        n = 0
        if y == 0:
            if self.grid[y + 1][x] == 'X':
                n += 1
        if y == LAST_INDEX:
            if self.grid[y - 1][x] == 'X':
                n += 1
        if 1 <= y and y < LAST_INDEX:
            for i in range(y - 1, y + 2, 2):
                if self.grid[i][x] == 'X':
                    n += 1
        return n

    def _check_slash(self, y, x):
        n = 0
        if 1 <= y and 1 <= x and y < LAST_INDEX and x < LAST_INDEX:
            y += 1
            for i in range(x - 1, x + 2, 2):
                if self.grid[y][i] == 'X':
                    n += 1
                y -= 2
        # boundary conditions
        elif (x == 0 and y != 0) or (y == LAST_INDEX and x != LAST_INDEX):
            if self.grid[y - 1][x + 1] == 'X':
                n += 1
        elif (x == LAST_INDEX and y != LAST_INDEX) or (y == 0 and x != 0):
            if self.grid[y + 1][x - 1] == 'X':
                n+= 1
        return n

    def _check_backslash(self, y, x):
        n = 0
        if 1 <= y and 1 <= x and y < LAST_INDEX and x < LAST_INDEX:
            y -= 1
            for i in range(x - 1, x + 2, 2):
                if self.grid[y][i] == 'X':
                    n += 1
                y += 2
        # boundary conditions
        elif (x == 0 and y != LAST_INDEX) or (y == 0 and x != LAST_INDEX):
            if self.grid[y + 1][x + 1] == 'X':
                n += 1
        elif (x == LAST_INDEX and y != 0) or (y == LAST_INDEX and x != 0):
            if self.grid[y - 1][x - 1] == 'X':
                n+= 1
        return n

game = board()
bomb = mines()

def play_minesweeper():
    bomb.mines()
    bomb.numbers()
    while True:
        os.system("clear")
        bomb.draw()
        row = int(input("\nrow: "))
        column = int(input("column: "))

if __name__ == '__main__':
    play_minesweeper()