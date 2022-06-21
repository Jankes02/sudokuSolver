ALL_NUMBERS = [1, 2, 3, 4, 5, 6, 7, 8, 9]
WIDTH = 9
HEIGHT = 9


def intersection_of_sets(a, b, c):
    result = []
    for element in a:
        if element in b and element in c:
            result.append(element)
    return result


def determine_square(x, y):
    xTable, yTable = [0, 1, 2], [0, 1, 2]
    for i in range(3):
        xTable[i] += (x // 3) * 3
        yTable[i] += (y // 3) * 3

    return xTable, yTable


class Game:
    solved = False

    def __init__(self):
        self.board = []
        for i in range(HEIGHT):
            self.board.append([])
            for j in range(WIDTH):
                self.board.append(int(input()))

    def print(self):
        for row in self.board:
            for number in row:
                print(number, end=' ')
            print()

    def solve(self):
        while not self.solved:
            for i in range(HEIGHT):
                possible_in_row = self.check_row(i)
                for j in range(WIDTH):
                    if self.board[i][j] == 0:
                        possible_in_column = self.check_column(j)
                        possible_in_square = self.check_square(i, j)
                        possible = intersection_of_sets(possible_in_row, possible_in_column, possible_in_square)
                        if len(possible) == 1:
                            self.board[i][j] = possible[0]
                            possible_in_row.remove(possible[0])



    def check_row(self, row):
        result = ALL_NUMBERS[:]
        for number in self.board[row]:
            if number in result:
                result.remove(number)

        return result

    def check_column(self, column):
        result = ALL_NUMBERS[:]
        for row in self.board:
            if row[column] in result:
                result.remove(row[column])

        return result

    def check_square(self, row, column):
        result = ALL_NUMBERS[:]
        xTable, yTable = determine_square(row, column)
        for x in xTable:
            for y in yTable:
                if self.board[y][x] in result:
                    result.remove(self.board[y][x])
        return result
