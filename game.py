import pygame.sprite
from constants import *
from objects import Grid


class Game:
    def __init__(self, win):
        self.game_is_on = True
        self.win = win

        # obj
        self.grid = Grid(700, 25)

    def run(self):
        clock = pygame.time.Clock()

        while self.game_is_on:
            dt = clock.tick(FPS)
            self.win.fill(BLACK)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_is_on = False
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.grid.handle_click(*event.pos)
            if pygame.mouse.get_pressed(3)[2]:
                self.grid.handle_click(*pygame.mouse.get_pos())

            self.draw(self.win)
            pygame.display.flip()

    def draw(self, win):
        self.grid.draw(win)
