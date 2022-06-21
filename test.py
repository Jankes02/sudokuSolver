def determine_square(x, y):
    xTable, yTable = [0, 1, 2], [0, 1, 2]
    for i in range(3):
        xTable[i] += (x // 3) * 3
        yTable[i] += (y // 3) * 3

    return xTable, yTable


for i in range(9):
    for j in range(9):
        print(determine_square(i, j))
