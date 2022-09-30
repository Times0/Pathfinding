import pygame.sprite
from constants import *
from objects import *
from buttons import Button
from label import Label


class Game:
    def __init__(self, win):
        self.game_is_on = True
        self.win = win

        basicfont = pygame.font.SysFont('comicsans', 30)

        # obj
        self.grid = Grid(700, 30)
        self.path_btn = Button(10, 10, 50, "Go !", GRAY, WHITE, basicfont, False, self.go)

        # ui
        self.explanation_lbl = Label("Mousewheel button to set arrival point", 10, 100,
                                     pygame.font.SysFont('comicsans', 20), WHITE)

        self.btns = pygame.sprite.Group(self.path_btn)
        self.labels = pygame.sprite.Group(self.explanation_lbl)

    def run(self):
        clock = pygame.time.Clock()

        while self.game_is_on:
            dt = clock.tick(FPS)
            self.win.fill(BLACK)
            self.events()
            self.draw(self.win)
            pygame.display.flip()

    def events(self):
        eves = pygame.event.get()
        for event in eves:
            if event.type == pygame.QUIT:
                self.game_is_on = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 2:
                self.grid.set_end(*event.pos)
        pressed = pygame.mouse.get_pressed(3)
        if pressed[0]:
            self.grid.handle_left_click(*pygame.mouse.get_pos())
        elif pressed[2]:
            self.grid.handle_right_click(*pygame.mouse.get_pos())
        self.btns.update(eves)

    def go(self):
        L = pathfind(self.grid.grid, self.grid.start, self.grid.end)
        if L:
            self.grid.path = L

    def draw(self, win):
        self.grid.draw(win)
        self.btns.draw(win)
        self.labels.draw(win)
