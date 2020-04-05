from space import *

class Map:
    grid = []

    def __init__(self, fileName):

        # code shamelessly stolen from Julian Cochran
        file = open(fileName)
        for line in file:
            line = line.strip()
            line = line.split('   ')
            self.grid.append(line)
        for r in range(len(self.grid)):
            for c in range(len(self.grid[r])):
                self.grid[r][c] = int(self.grid[r][c])
        file.close()

        self.all_spaces = []
        for x in range(len(self.grid)):
            for y in range(len(self.grid[0])):
                self.all_spaces.append(Space(x, y, None, 0, 0, self.grid[x][y]))

    def getSpace(self, x, y):
        for s in self.all_spaces:
            if s.x == x and s.y == y:
                return s
