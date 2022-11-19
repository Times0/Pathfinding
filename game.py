import pygame.sprite
from constants import *
from objects import *
from buttons import Button, ButtonImg
from label import Label

r_image = pygame.image.load("restart.png")
r_image = pygame.transform.scale(r_image, (35, 35))


class Game:
    def __init__(self, win):
        self.game_is_on = True
        self.win = win

        basicfont = pygame.font.SysFont('comicsans', 50)

        # obj
        self.grid = Grid(700, 20)
        self.path_btn = Button(30, HEIGHT // 2 - 50, 50, "FIND PATH", (47, 47, 55), DARKWHITE, basicfont, False,
                               self.go)
        self.r_btn = ButtonImg(r_image, 10, HEIGHT - 100, self.grid.reset)
        # ui
        self.explanation_lbl = Label("Mousewheel button to set arrival point", 10, 100,
                                     pygame.font.SysFont('comicsans', 20), WHITE)

        self.btns = pygame.sprite.Group(self.path_btn, self.r_btn)
        self.labels = pygame.sprite.Group()

    def run(self):
        clock = pygame.time.Clock()

        while self.game_is_on:
            dt = clock.tick(FPS)
            self.win.fill(LIGHTBLACK)
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
        self.grid.solve()

    def draw(self, win):
        self.grid.draw(win)
        self.btns.draw(win)
        self.labels.draw(win)
