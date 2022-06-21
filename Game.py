class Game:
    solved = False

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = []
        for i in range(height):
            self.board.append([])
            for j in range(width):
                self.board.append(int(input()))
