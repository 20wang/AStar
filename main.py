# uses an A* pathing algorithm to plot a course through a topographic map

import pygame
from grid import *
from pygame import *
import sys
import numpy as np

# draws a map
def drawMap(map):
    # map drawin' code courtesy of the amazing Christos Polzak
    arr_max = np.max(map.grid)
    arr_min = np.min(map.grid)
    color_arr = (255 * (map.grid - arr_min) / (arr_max - arr_min)).astype(int)
    gray = np.stack((color_arr, color_arr, color_arr), axis=-1)
    px = 1

    pygame.init()
    win = pygame.display.set_mode((len(gray[0]) * px, len(gray) * px))  # based on map size
    for r in range(len(gray)):
        for c in range(len(gray[r])):
            pygame.draw.rect(win, gray[r][c], (c * px, r * px, px, px))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
        # pygame.display.flip()

# main method for the class
if __name__ == '__main__':

    startX = 0
    startY = 0
    endX = 69
    endY = 100

    map = Map('Colorado_480x480.dat')
    drawMap(map)

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
                        xdist = float(endX - temp.x)
                        ydist = float(endY - temp.y)
                        xint = 0.00
                        yint = 0.00
                        if xdist == 0 and ydist == 0:
                            temp.setH(0)
                        else:
                            if xdist == 0:
                                yint = ydist / abs(ydist)
                            elif ydist == 0:
                                xint = xdist / abs(xdist)
                            else:
                                if abs(ydist) >= abs(xdist):
                                    xint = xdist / abs(ydist)
                                    yint = ydist / abs(ydist)
                                elif abs(xdist) > abs(ydist):
                                    yint = ydist / abs(xdist)
                                    xint = xdist / abs(xdist)

                            currentelev = temp.elev
                            change = 0
                            count = 1
                            while not (abs(xint * count) == abs(xdist) or abs(yint * count) == abs(ydist)):
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
    path = [node]
    print('(' + str(node.x) + ', ' + str(node.y) + ') ')
    pathing = True
    while pathing:
        node = node.parent
        path.append(node)
        print('(' + str(node.x) + ', ' + str(node.y) + ') ')
        if node.x == startX and node.y == startY:
            pathing = False
