import copy
GRID_SIZE = 9


def grid_to_list(grid):
    board = []
    for row in grid:
        row_values = []
        for entry in row:
            value = entry.get()
            if value == "":
                row_values.append(0)
            else:
                row_values.append(int(value))
        board.append(row_values)
        
    return board


def insert_list_into_grid(board, grid):
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            grid[i][j].insert(0, str(board[i][j]))
    
    return grid


def solve_trivial(board):
    solved = False
    while not solved:
        change = False
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                if board[i][j] == 0:
                    possible = []
                    for number in range(1, 10):
                        if is_possible(board, i, j, number):
                            possible.append(number)
                    if len(possible) == 1:
                        change = True
                        board[i][j] = possible[0]
                        if not there_is_zero(board):
                            solved = True
        if not change:
            return
        
        
def solve_r(board):
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            if board[y][x] == 0:
                for n in range(1, 10):
                    if is_possible(board, y, x, n):
                        board_copy = copy.deepcopy(board)
                        board_copy[y][x] = n
                        solve_trivial(board_copy)
                        result = solve_r(board_copy)
                        if result:
                            return result
                return False
    return copy.deepcopy(board)
        
        
def there_is_zero(board):
    for row in board:
        for number in row:
            if number == 0:
                return True
    return False


def is_possible(board, y, x, n):
    for i in range(GRID_SIZE):
        if board[y][i] == n:
            return False
    for i in range(GRID_SIZE):
        if board[i][x] == n:
            return False
    xTable, yTable = determine_square(x, y)
    for row in yTable:
        for column in xTable:
            if board[row][column] == n:
                return False
    return True


def determine_square(x, y):
    xTable, yTable = [0, 1, 2], [0, 1, 2]
    for i in range(3):
        xTable[i] += (x // 3) * 3
        yTable[i] += (y // 3) * 3

    return xTable, yTable
