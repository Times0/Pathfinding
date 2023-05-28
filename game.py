import pygame.sprite
from PygameUIKit import Group
from PygameUIKit.button import ButtonText

from objects import *

COLOR_BUTTON = (82, 148, 201)
COLOR_TEXT_BUTTON = DARK_WHITE

FONT_BTN = pygame.font.SysFont('None', 40)


class Game:
    def __init__(self, win):
        self.game_is_on = True
        self.win = win

        # obj
        self.grid = Grid(700, 20)
        self.find_path_btn = ButtonText(COLOR_BUTTON, self.grid.solve, "FIND PATH", border_radius=2,
                                        font_color=COLOR_TEXT_BUTTON, font=FONT_BTN)
        self.clear_btn = ButtonText(RED, self.grid.reset, "CLEAR", border_radius=2, font=FONT_BTN)
        # ui

        self.btns = Group(self.find_path_btn, self.clear_btn)
        self.labels = pygame.sprite.Group()

    def run(self):
        clock = pygame.time.Clock()
        while self.game_is_on:
            clock.tick(FPS)
            self.win.fill(LIGHT_BLACK)
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
        self.btns.handle_events(eves)

    def go(self):
        self.grid.solve()

    def draw(self, win):
        W, H = win.get_size()
        self.grid.draw(win)
        self.labels.draw(win)
        self.find_path_btn.draw(win, 100, H // 2 - self.find_path_btn.rect.height // 2 - 50)
        self.clear_btn.draw(win, 100, H // 2 + self.find_path_btn.rect.height // 2 + 20)
