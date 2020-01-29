"""
A* (A Star) Alghoritm visually represented in Python
by Luca Zani 28/01/2020
"""
import pygame
from Cell import *
from colors import *


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

    def run(self):
        """
        Game Loop
        :return: None
        """
        clock = pygame.time.Clock()

        self.createGrid()
        self.start = self.grid[0][0]
        self.end = self.grid[self.width // self.w - 1][self.height // self.w - 1]
        self.openSet.append(self.start)

        run = True
        while run:
            clock.tick(self.fps)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            if len(self.openSet) > 0:
                best = 0  # Index of the lowest F cell
                for i in range(len(self.openSet)):
                    if self.openSet[i].f < self.openSet[best].f:
                        best = i

                current = self.openSet[best]

                # Win Condition
                if self.openSet[best] == self.end:
                    self.done = True
                    print('Done!')

                self.openSet.remove(current)  # Potrebbe non andare
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

            else:
                print('No Solution')

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

        # DrawLoop
        for i in range(self.width // self.w):  # Cols
            for j in range(self.height // self.w):  # Rows
                self.grid[i][j].show(self.screen, self.w, white)

        for i in range(len(self.openSet)):
            self.openSet[i].show(self.screen, self.w, green)
        for i in range(len(self.closedSet)):
            self.closedSet[i].show(self.screen, self.w, red)

        pygame.display.flip()

    def heuristic(self, neighbor):
        pass


g = Game()
g.run()
