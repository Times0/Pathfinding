import pygame
from constants import *


class Grid:
    def __init__(self, width, n):
        self.grid = [[0 for _ in range(n)] for _ in range(n)]

        self.width = width
        self.n = n
        self.cell_size = width // n
        self.offset_x = (WIDTH - self.width) // 2
        self.offset_y = (HEIGHT - self.width) // 2

    def draw(self, win):
        n = self.n
        c_size = self.cell_size

        for i in range(n):
            for j in range(n):
                color = WHITE if self.grid[i][j] else GRAY
                pygame.draw.rect(win, color,
                                 [j * c_size + self.offset_x, i * c_size + self.offset_y, c_size - 1, c_size - 1])

    def handle_click(self, x, y):
        i = (y - self.offset_y) // self.cell_size
        j = (x - self.offset_x) // self.cell_size
        if i < 0 or i >= self.n or j < 0 or j >= self.n:
            return
        self.grid[i][j] = 1
