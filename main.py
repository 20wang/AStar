from grid import *
from space import *
from math import sqrt

if __name__ == '__main__':
    startX = 0
    startY = 0
    endX = 69
    endY = 100

    map = Map('Colorado_480x480.dat')

    open = []
    closed = []
    open.append(map.getSpace(startX, startY))

    checking = open[0]

    while checking.x != endX or checking.y != endY:

        closed.append(checking)
        open.remove(checking)

        for x in range(-1, 2):
            for y in range(-1, 2):
                if 0 <= checking.x + x < len(map.grid[0]) and 0 <= checking.y + y < len(map.grid) and (x != 0 or y != 0):
                    temp = map.getSpace(checking.x + x, checking.y + y)

                    newG = checking.g + abs(temp.elev - checking.elev)
                    if temp.g == 0 or temp.g > newG:
                        temp.setG(newG)
                        temp.setNewParent(checking)
                        if temp in closed:
                            closed.remove(temp)
                        if temp not in open:
                            open.append(temp)

                    if temp.h == 0:
                        xdist = float(endY - temp.x)
                        ydist = float(endY - temp.y)
                        xint = 0.00
                        yint = 0.00

                        if abs(ydist) >= abs(xdist):
                            xint = xdist / abs(ydist)
                            yint = ydist / abs(ydist)
                        elif abs(xdist) > abs(ydist):
                            yint = ydist / abs(xdist)
                            xint = xdist / abs(xdist)

                        currentelev = temp.elev
                        change = 0
                        count = 1
                        while not (abs(xint * count + temp.x) == abs(xdist) or abs(yint * count + temp.y) == abs(ydist)):
                            theo = map.getSpace(int(round(xint * count)) + temp.x, int(round(yint * count)) + temp.y)
                            change += abs(currentelev - theo.elev)
                            currentelev = theo.elev
                            count += 1
                        temp.setH(change)

        minF = open[0]
        for space in open:
            if minF.g + minF.h > space.g + space.h:
                minF = space
        checking = minF

        print('checking: ' + '(' + str(checking.x) + ', ' + str(checking.y) + ') ' + str(checking.elev))
        print('h: ' + str(checking.h))

    node = map.getSpace(endX, endY)
    print('(' + str(node.x) + ', ' + str(node.y) + ') ')
    pathing = True
    while pathing:
        node = node.parent
        print('(' + str(node.x) + ', ' + str(node.y) + ') ')
        if node.x == startX and node.y == startY:
            pathing = False
