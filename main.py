from grid import *
from space import *
from math import sqrt

if __name__ == '__main__':
    startX = 0
    startY = 0
    endX = 479
    endY = 479

    map = Map('Colorado_480x480.dat')

    open = [Space(startX, startY, 0, 0, sqrt(abs(startX - endX)**2 + abs(startY - endY)**2))]
    closed = []

    checking = open[0]

    while checking.x != endX and checking.y != endY:

        closed.append(checking)
        open.remove(checking)

        for x in range(-1, 2):
            for y in range(-1, 2):
                if checking.x + x > 0 and checking.y + y > 0 and checking.y + y < len(map.grid)\
                        and checking.x + x < len(map.grid[0]) and (x != 0 or y != 0):
                    temp = Space(x, y, checking,
                                      checking.g + abs(map.grid[checking.x][checking.y] - map.grid[x][y]),
                                      sqrt(abs(startX - endX) ** 2 + abs(startY - endY) ** 2))
                    if not temp in closed:
                        open.append(temp)
                        print(temp)

        minF = open[0]
        for space in open:
            if minF.g + minF.h > space.g + space.h:
                minF = space
        checking = minF

        print(map.grid[checking.x][checking.y])
