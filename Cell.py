import pygame
from colors import *


class Cell:

    def __init__(self, i, j):
        """
        Cell Class representing every cell in the grid
        :param i: index
        :param j: index
        """
        self.i = i
        self.j = j
        self.f = 0
        self.h = 0
        self.g = 0
        self.neighbors = []
        self.previous = None

    def show(self, screen, w, color):
        """
        Draw a rectangle
        :param screen: pygame window
        :param w: int
        :param color: color
        :return: None
        """
        x = self.i * w - 1  # -1 is for centering correcting the cells
        y = self.j * w
        rect = pygame.Rect(x, y, w, w)
        pygame.draw.rect(screen, color, rect)
        pygame.draw.rect(screen, black, rect, 1)  # Border

    def addNeighbors(self, grid, cols, rows):

        if self.i < cols - 1:
            self.neighbors.append(grid[self.i + 1][self.j])  # Top
        if self.j < rows - 1:
            self.neighbors.append(grid[self.i][self.j + 1])  # Right
        if self.i > 0:
            self.neighbors.append(grid[self.i - 1][self.j])  # Bottom
        if self.j > 0:
            self.neighbors.append(grid[self.i][self.j - 1])  # Left
