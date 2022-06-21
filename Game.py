import copy
import time

ALL_NUMBERS = [1, 2, 3, 4, 5, 6, 7, 8, 9]
WIDTH = 9
HEIGHT = 9
input_file = "C:\\Users\\janke\\Desktop\\template5.txt"


def determine_square(x, y):
    xTable, yTable = [0, 1, 2], [0, 1, 2]
    for i in range(3):
        xTable[i] += (x // 3) * 3
        yTable[i] += (y // 3) * 3

    return xTable, yTable


class Game:
    solved = False
    board = []

    def __init__(self):
        file = open(input_file, 'r')
        read_input = file.read()
        read_input = iter(read_input.split())
        file.close()

        for i in range(HEIGHT):
            self.board.append([])
            for j in range(WIDTH):
                self.board[i].append(int(next(read_input)))
        self.start = time.time()

    def print(self):
        for row in self.board:
            for number in row:
                print(number, end=' ')
            print()

    def solve_trivial(self):
        while not self.solved:
            change = False
            for i in range(HEIGHT):
                for j in range(WIDTH):
                    if self.board[i][j] == 0:
                        possible = []
                        for number in ALL_NUMBERS:
                            if self.possible(i, j, number):
                                possible.append(number)
                        if len(possible) == 1:
                            change = True
                            self.board[i][j] = possible[0]
                            if not self.there_is_zero():
                                self.solved = True
            if not change:
                return

    def solve_r(self):
        for y in range(HEIGHT):
            for x in range(WIDTH):
                if self.board[y][x] == 0:
                    for n in ALL_NUMBERS:
                        if self.possible(y, x, n):
                            board_copy = copy.deepcopy(self.board)
                            self.board[y][x] = n
                            self.solve_trivial()
                            self.solve_r()
                            self.board = board_copy
                    return
        self.print()
        end = time.time()
        print(end - self.start, end=' ')
        print("seconds elapsed")
        exit()

    def there_is_zero(self):
        for row in self.board:
            for number in row:
                if number == 0:
                    return True
        return False

    def possible(self, y, x, n):
        for i in range(WIDTH):
            if self.board[y][i] == n:
                return False
        for i in range(HEIGHT):
            if self.board[i][x] == n:
                return False
        xTable, yTable = determine_square(x, y)
        for row in yTable:
            for column in xTable:
                if self.board[row][column] == n:
                    return False
        return True
