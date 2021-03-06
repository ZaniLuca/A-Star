"""
A* (A Star) Alghoritm visually represented in Python
by Luca Zani 28/01/2020
"""
import pygame
from Cell import *
from Colors import *
import math
pygame.init()


class Game:

    def __init__(self):
        self.width = 400
        self.height = 400
        self.w = 50
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.fps = 30
        self.grid = [[None for i in range(self.width // self.w)] for j in
                     range(self.height // self.w)]  # Initalize 2D arr
        self.done = False  # is the end reached
        self.start = None  # StartPoint
        self.end = None  # EndPoint
        self.openSet = []
        self.closedSet = []
        self.path = []

    def run(self):
        """
        Game Loop
        :return: None
        """
        clock = pygame.time.Clock()

        self.createGrid()
        self.start = self.grid[0][0]
        # self.end = self.grid[self.width // self.w - 1][self.height // self.w - 1]
        self.end = self.grid[7][3]
        self.openSet.append(self.start)

        run = True
        while run:
            clock.tick(self.fps)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            if not self.done:
                if len(self.openSet) > 0:
                    best = 0  # Index of the lowest F cell
                    for i in range(len(self.openSet)):
                        if self.openSet[i].f < self.openSet[best].f:
                            best = i

                    current = self.openSet[best]

                    # Win Condition
                    if self.openSet[best] == self.end:
                        temp = current
                        self.path.append(temp)
                        while temp.previous:
                            self.path.append(temp.previous)
                            temp = temp.previous

                        self.done = True
                        print('Done!')

                    self.openSet.remove(current)
                    self.closedSet.append(current)

                    # Evaluating neighbors
                    for i in range(len(current.neighbors)):
                        neighbor = current.neighbors[i]

                        if neighbor not in self.closedSet:
                            temp_g = current.g + 1

                            # Check if i have evaluated the neighbor before
                            # if so we have a better G score
                            if neighbor in self.openSet:
                                if temp_g < neighbor.g:
                                    neighbor.g = temp_g
                            # otherwise just give the neighbor the temp_g
                            else:
                                neighbor.g = temp_g
                                self.openSet.append(neighbor)

                            neighbor.h = self.heuristic(neighbor)
                            neighbor.f = neighbor.g + neighbor.h
                            neighbor.previous = current

                else:
                    pass  # no solution

                self.update()

        pygame.quit()

    def createGrid(self):
        """
        create the cells
        add the neighbors
        :return: None
        """
        # Create cells
        for i in range(self.width // self.w):  # Cols
            for j in range(self.height // self.w):  # Rows
                self.grid[i][j] = Cell(i, j)

        # Adds Neighbors
        for i in range(self.width // self.w):
            for j in range(self.height // self.w):
                self.grid[i][j].addNeighbors(self.grid, self.width // self.w, self.height // self.w)

    def update(self):
        """
        Update the screen
        draw the cells
        :return: None
        """
        self.screen.fill(black)

        # Board
        for i in range(self.width // self.w):  # Cols
            for j in range(self.height // self.w):  # Rows
                self.grid[i][j].show(self.screen, self.w, white)

        # OpenSet
        for i in range(len(self.openSet)):
            self.openSet[i].show(self.screen, self.w, green)

        # ClosedSet
        for i in range(len(self.closedSet)):
            self.closedSet[i].show(self.screen, self.w, red)

        # Path
        for i in range(len(self.path)):
            self.path[i].show(self.screen, self.w, blue)

        self.end.show(self.screen, self.w, yellow)
        self.start.show(self.screen, self.w, yellow)

        pygame.display.flip()

    def heuristic(self, neighbor):
        """
        Calculate the h cost from the neighbor to the end
        h cost = distance from neighbir --> end
        :param neighbor: Cell
        :return: double
        """
        distance = math.sqrt((neighbor.i - self.end.i) ** 2 + (neighbor.j - self.end.j) ** 2)
        return distance


g = Game()
g.run()
