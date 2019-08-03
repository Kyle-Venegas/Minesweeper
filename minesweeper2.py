import os
import random

BOARD_SIZE = 10
MINES = 15
LAST_INDEX = BOARD_SIZE - 1

class board:
    mines = MINES
    
    def __init__(self):
        self.grid = [["*" for i in range(BOARD_SIZE)] for j in range(BOARD_SIZE)]

    def draw(self):
        columns = " ".join([str(i) for i in range(BOARD_SIZE)])
        print("\n     ", columns, "\n")
        y = 0
        for row in self.grid:
            print(" ", y, ' ', ' '.join(row))
            y += 1
        print("\n", self.mines, "mines remaining")

    def reveal(self, y, x, flag):
        mines = MINES
        if flag == 'y':
            if self.grid[y][x] == '*':
                self.grid[y][x] = 'f'
                self.mines -= 1
            elif self.grid[y][x] == 'f':
                self.grid[y][x] = '*'
                self.mines += 1
        else:
            if bomb.grid[y][x] == 0:
                self.grid[y][x] = str(bomb.numbers(y, x))
                # for free space
                if bomb.numbers(y, x) == ' ':
                    self.free_space(y, x)
            if bomb.grid[y][x]:
                for y in range(BOARD_SIZE):
                    for x in range(BOARD_SIZE):
                        if bomb.grid[y][x]:
                            self.grid[y][x] = 'X'
                return True

    def free_space(self, y, x):
        self._check_row(y, x)
        self._check_col(y, x)
        self._check_slash(y, x)
        self._check_backslash(y, x)
        if x == 0:
            if self.grid[y][x + 2] == '*' and self.grid[y][x + 1] == ' ':
                self.free_space(y, x + 1)
        if x == LAST_INDEX:
            if self.grid[y][x - 2] == '*' and self.grid[y][x - 1] == ' ':
                self.free_space(y, x - 1)
        if y == 0:
            if self.grid[y + 2][x] == '*' and self.grid[y + 1][x] == ' ':
                self.free_space(y + 1, x)
        if y == LAST_INDEX:
            if self.grid[y - 2][x] == '*' and self.grid[y - 1][x] == ' ':
                self.free_space(y - 1, x)
        if 1 <= x and x < LAST_INDEX:
            try:
                if self.grid[y][x - 2] == '*' and self.grid[y][x - 1] == ' ':
                    self.free_space(y, x - 1)
            except:
                if self.grid[y][x - 1] == '*' and self.grid[y][x] == ' ':
                    self.free_space(y, x - 1)
            try:
                if self.grid[y][x + 2] == '*' and self.grid[y][x + 1] == ' ':
                    self.free_space(y, x + 1)
            except:
                if self.grid[y][x + 1] == '*' and self.grid[y][x] == ' ':
                    self.free_space(y, x + 1)
        if 1 <= y and y < LAST_INDEX:
            try:
                if self.grid[y - 2][x] == '*' and self.grid[y - 1][x] ==' ':
                    self.free_space(y - 1, x)
            except:
                if self.grid[y - 1][x] == '*' and self.grid[y][x] ==' ':
                    self.free_space(y - 1, x)
            try:
                if self.grid[y + 2][x] == '*' and self.grid[y + 1][x] ==' ':
                    self.free_space(y + 1, x)
            except:
                if self.grid[y + 1][x] == '*' and self.grid[y][x] ==' ':
                    self.free_space(y + 1, x)


    def _check_row(self, y, x):
        n = 0
        if x == 0:
            if bomb.grid[y][x + 1] == 0:
                self.grid[y][x + 1] = str(bomb.numbers(y, x + 1))
        if x == LAST_INDEX:
            if bomb.grid[y][x - 1] == 0:
                self.grid[y][x - 1] = str(bomb.numbers(y, x - 1))
        if 1 <= x and x < LAST_INDEX:
            for i in range(x - 1, x + 2, 2):
                if bomb.grid[y][i] == 0:
                    self.grid[y][i] = str(bomb.numbers(y, i))

    def _check_col(self, y, x):
        n = 0
        if y == 0:
            if bomb.grid[y + 1][x] == 0:
                self.grid[y + 1][x] = str(bomb.numbers(y + 1, x))
        if y == LAST_INDEX:
            if bomb.grid[y - 1][x] == 0:
                self.grid[y - 1][x] = str(bomb.numbers(y - 1, x))
        if 1 <= y and y < LAST_INDEX:
            for i in range(y - 1, y + 2, 2):
                if bomb.grid[i][x] == 0:
                    self.grid[i][x] = str(bomb.numbers(i, x))

    def _check_slash(self, y, x):
        n = 0
        if 1 <= y and 1 <= x and y < LAST_INDEX and x < LAST_INDEX:
            y += 1
            for i in range(x - 1, x + 2, 2):
                if bomb.grid[y][i] == 0:
                    self.grid[y][i] = str(bomb.numbers(y, i))
                y -= 2
        # boundary conditions
        elif (x == 0 and y != 0) or (y == LAST_INDEX and x != LAST_INDEX):
            if bomb.grid[y - 1][x + 1] == 0:
                self.grid[y - 1][x + 1] = str(bomb.numbers(y - 1, x + 1))
        elif (x == LAST_INDEX and y != LAST_INDEX) or (y == 0 and x != 0):
            if bomb.grid[y + 1][x - 1] == 0:
                self.grid[y + 1][x - 1] = str(bomb.numbers(y + 1, x - 1))

    def _check_backslash(self, y, x):
        n = 0
        if 1 <= y and 1 <= x and y < LAST_INDEX and x < LAST_INDEX:
            y -= 1
            for i in range(x - 1, x + 2, 2):
                if bomb.grid[y][i] == 0:
                    self.grid[y][i] = str(bomb.numbers(y, i))
                y += 2
        # boundary conditions
        elif (x == 0 and y != LAST_INDEX) or (y == 0 and x != LAST_INDEX):
            if bomb.grid[y + 1][x + 1] == 0:
                self.grid[y + 1][x + 1] = str(bomb.numbers(y + 1, x + 1))
        elif (x == LAST_INDEX and y != 0) or (y == LAST_INDEX and x != 0):
            if bomb.grid[y - 1][x - 1] == 0:
                self.grid[y - 1][x - 1] = str(bomb.numbers(y - 1, x - 1))
            
class mines:

    def __init__(self):
        self.grid = [[0 for i in range(BOARD_SIZE)] for j in range(BOARD_SIZE)]

    def mines(self):
        _n = 0
        while _n < MINES:
            x = random.randint(0, LAST_INDEX)
            y = random.randint(0, LAST_INDEX)
            if self.grid[y][x] == 0:
                self.grid[y][x] = 1
            elif self.grid[y][x] == 1:
                continue
            _n += 1

    def draw(self):
        columns = "  ".join([str(i) for i in range(BOARD_SIZE)])
        print("\n    ", columns)
        y = 0
        for row in self.grid:
            print(' ', y, row)
            y += 1

    def numbers(self, y, x):
        if self.grid[y][x] == 0:
            n = self._check_row(y, x)
            n += self._check_col(y, x)
            n += self._check_slash(y, x)
            n += self._check_backslash(y, x)
        if n == 0:
            return ' '
        return n

    def _check_row(self, y, x):
        n = 0
        if x == 0:
            if self.grid[y][x + 1] == 1:
                n += 1
        if x == LAST_INDEX:
            if self.grid[y][x - 1] == 1:
                n += 1
        if 1 <= x and x < LAST_INDEX:
            for i in range(x - 1, x + 2, 2):
                if self.grid[y][i] == 1:
                    n += 1
        return n

    def _check_col(self, y, x):
        n = 0
        if y == 0:
            if self.grid[y + 1][x] == 1:
                n += 1
        if y == LAST_INDEX:
            if self.grid[y - 1][x] == 1:
                n += 1
        if 1 <= y and y < LAST_INDEX:
            for i in range(y - 1, y + 2, 2):
                if self.grid[i][x] == 1:
                    n += 1
        return n

    def _check_slash(self, y, x):
        n = 0
        if 1 <= y and 1 <= x and y < LAST_INDEX and x < LAST_INDEX:
            y += 1
            for i in range(x - 1, x + 2, 2):
                if self.grid[y][i] == 1:
                    n += 1
                y -= 2
        # boundary conditions
        elif (x == 0 and y != 0) or (y == LAST_INDEX and x != LAST_INDEX):
            if self.grid[y - 1][x + 1] == 1:
                n += 1
        elif (x == LAST_INDEX and y != LAST_INDEX) or (y == 0 and x != 0):
            if self.grid[y + 1][x - 1] == 1:
                n+= 1
        return n

    def _check_backslash(self, y, x):
        n = 0
        if 1 <= y and 1 <= x and y < LAST_INDEX and x < LAST_INDEX:
            y -= 1
            for i in range(x - 1, x + 2, 2):
                if self.grid[y][i] == 1:
                    n += 1
                y += 2
        # boundary conditions
        elif (x == 0 and y != LAST_INDEX) or (y == 0 and x != LAST_INDEX):
            if self.grid[y + 1][x + 1] == 1:
                n += 1
        elif (x == LAST_INDEX and y != 0) or (y == LAST_INDEX and x != 0):
            if self.grid[y - 1][x - 1] == 1:
                n+= 1
        return n

game = board()
bomb = mines()

def play_minesweeper():
    bomb.mines()
    while True:
        os.system("clear")
        game.draw()
        bomb.draw() #temporary to see if reveal function works
        x = int(input("\ncolumn: "))
        y = int(input("row: "))
        flag = input('flag? (y/n)')
        end = game.reveal(y, x, flag)
        if end:
            game.draw()
            print(" you lost")
            break

if __name__ == '__main__':
    play_minesweeper()
