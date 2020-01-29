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

    def show(self, screen, w):
        """
        Draw a rectangle
        :param screen: pygame window
        :param w: int
        :return: None
        """
        x = self.i * w
        y = self.j * w
        rect = pygame.Rect(x, y, w, w)
        pygame.draw.rect(screen, white, rect)
