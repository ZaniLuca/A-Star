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
        run = True
        while run:
            clock.tick(self.fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            if not self.done:
                pass
            self.update()

        pygame.quit()

    def createGrid(self):
        """
        create the cells
        :return: None
        """
        for i in range(self.width // self.w):  # Cols
            for j in range(self.height // self.w):  # Rows
                self.grid[i][j] = Cell(i, j)

    def update(self):
        """
        Update the screen
        draw the cells
        :return: None
        """
        self.screen.fill(white)
        for i in range(self.width // self.w):  # Cols
            for j in range(self.height // self.w):  # Rows
                self.grid[i][j].show(self.screen, self.w)
        pygame.display.flip()


g = Game()
g.run()
