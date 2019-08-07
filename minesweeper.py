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
                self.free_space(y, x)
            if bomb.grid[y][x]:
                for y in range(BOARD_SIZE):
                    for x in range(BOARD_SIZE):
                        if bomb.grid[y][x]:
                            self.grid[y][x] = 'X'
                return True

    def convert_zero(self, y, x):
        if bomb.numbers(y, x) == 0:
            self.grid[y][x] = ' '

    def free_space(self, y, x):

        if bomb.grid[y][x]:
            return
        if self.grid[y][x] != '*':
            return

        self.grid[y][x] = str(bomb.numbers(y, x))
        self.convert_zero(y, x)

        if bomb.numbers(y, x) > 0:
            return

        if x == 0:
            if y == 0:
                for (j, i) in [(0, 1), (1, 0), (1, 1),]:
                    self.free_space(y + j, x + i)
            elif y == LAST_INDEX:
                for (j, i) in [(0, 1), (-1, 0), (-1, 1)]:
                    self.free_space(y + j, x + i)
            else:
                for (j, i) in [(0, 1), (1, 0), (-1, 0), (1, 1), (-1, 1)]:
                    self.free_space(y + j, x + i)
        elif x == LAST_INDEX:
            if y == 0:
                for (j, i) in [(0, -1), (1, 0), (1, -1),]:
                    self.free_space(y + j, x + i)
            elif y == LAST_INDEX:
                for (j, i) in [(0, -1), (-1, 0), (-1, -1)]:
                    self.free_space(y + j, x + i)
            else:
                for (j, i) in [(0, -1), (1, 0), (-1, 0), (1, -1), (-1, -1)]:
                    self.free_space(y + j, x + i)

        elif y == 0:
            for (j, i) in [(0, 1), (0, -1), (1, 0), (1, -1), (1, 1)]:
                self.free_space(y + j, x + i)
        elif y == LAST_INDEX:
            for (j, i) in [(0, 1), (0, -1), (-1, 0), (-1, -1), (-1, 1)]:
                self.free_space(y + j, x + i)

        else:
            for (j, i) in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
                self.free_space(y + j, x + i)

    def win(self):
        n = 0
        for y in range(BOARD_SIZE):
            for x in range(BOARD_SIZE):
                if self.grid[y][x] == '*':
                    break
                if self.grid[y][x] == 'f' and bomb.grid[y][x]:
                    n += 1
                    if n == MINES:
                        return True
        return False

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
        n = 0
        if x == 0:
            if y == 0:
                for (j, i) in [(0, 1), (1, 0), (1, 1),]:
                    if self.grid[y + j][x + i]:
                        n += 1
            elif y == LAST_INDEX:
                for (j, i) in [(0, 1), (-1, 0), (-1, 1)]:
                    if self.grid[y + j][x + i]:
                        n += 1
            else:
                for (j, i) in [(0, 1), (1, 0), (-1, 0), (1, 1), (-1, 1)]:
                    if self.grid[y + j][x + i]:
                        n += 1
        elif x == LAST_INDEX:
            if y == 0:
                for (j, i) in [(0, -1), (1, 0), (1, -1),]:
                    if self.grid[y + j][x + i]:
                        n += 1
            elif y == LAST_INDEX:
                for (j, i) in [(0, -1), (-1, 0), (-1, -1)]:
                    if self.grid[y + j][x + i]:
                        n += 1
            else:
                for (j, i) in [(0, -1), (1, 0), (-1, 0), (1, -1), (-1, -1)]:
                    if self.grid[y + j][x + i]:
                        n += 1

        elif y == 0:
            for (j, i) in [(0, 1), (0, -1), (1, 0), (1, -1), (1, 1)]:
                if self.grid[y + j][x + i]:
                    n += 1
        elif y == LAST_INDEX:
            for (j, i) in [(0, 1), (0, -1), (-1, 0), (-1, -1), (-1, 1)]:
                if self.grid[y + j][x + i]:
                    n += 1

        else:
            for (j, i) in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
                if self.grid[y + j][x + i]:
                    n += 1
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
        flag = input('flag? (type "y" for yes, else enter): ')
        end = game.reveal(y, x, flag)
        if end or game.win():
            if game.win():
                print(" you win")
                break
            game.draw()
            print(" you lost")
            break

if __name__ == '__main__':
    play_minesweeper()
