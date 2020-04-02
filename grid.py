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
