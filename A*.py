"""
A* (A Star) Alghoritm visually represented in Python
by Luca Zani 28/01/2020
"""
import pygame


class Game:

    def __init__(self):
        self.width = 400
        self.height = 400
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.fps = 30
        self.grid = []  # Grid containig every square
        self.done = False  # is the end reached
        self.start = None  # StartPoint
        self.end = None  # EndPoint
        self.openSet = []
        self.closedSet = []

    def run(self):
        clock = pygame.time.Clock()

        run = True
        while run:
            clock.tick(self.fps)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

        pygame.quit()


g = Game()
g.run()
