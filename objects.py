import random

import pygame
from colour import Color

from constants import *


class Grid:
    def __init__(self, width, n):
        self.grid = [[0 for _ in range(n)] for _ in range(n)]
        self.start = 0, 0
        self.end = None

        self.width = width
        self.n = n

        self.cell_size = width // n
        self.offset_x = (WIDTH - self.width) // 2
        self.offset_y = (HEIGHT - self.width) // 2

        print(self.offset_x, self.offset_y)

        self.path = []

    def draw(self, win):
        n = self.n
        c_size = self.cell_size

        for i in range(n):
            for j in range(n):
                color = BROWN if self.grid[i][j] == 1 else GREEN if self.grid[i][j] == 2 else GRAY
                if (i, j) == self.end:
                    color = PINK
                pygame.draw.rect(win, color,
                                 [j * c_size + self.offset_x, i * c_size + self.offset_y, c_size - 1, c_size - 1])
        self.show_path(win)

    def handle_left_click(self, x, y):
        i = (y - self.offset_y) // self.cell_size
        j = (x - self.offset_x) // self.cell_size
        if i < 0 or i >= self.n or j < 0 or j >= self.n:
            return
        self.grid[i][j] = 1

    def handle_right_click(self, x, y):
        i = (y - self.offset_y) // self.cell_size
        j = (x - self.offset_x) // self.cell_size
        if i < 0 or i >= self.n or j < 0 or j >= self.n:
            return
        self.grid[i][j] = 0

    def set_end(self, x, y):
        i = (y - self.offset_y) // self.cell_size
        j = (x - self.offset_x) // self.cell_size
        self.end = i, j

    def show_path(self, win):
        n = len(self.path)
        white = Color("black")
        colors = list(white.range_to(Color("pink"), n + 1))
        c_size = self.cell_size
        for x, (i, j) in enumerate(self.path):
            r, g, b = colors[x].rgb[0] * 255, colors[x].rgb[1] * 255, colors[x].rgb[2] * 255
            pygame.draw.rect(win, (r, g, b),
                             [j * c_size + self.offset_x + 0.25 * c_size, i * c_size + self.offset_y + 0.25 * c_size,
                              c_size * 0.5, c_size * 0.5])

    def reset(self):
        self.__init__(self.width, self.n)


def pathfind(grid, start, end):
    _, val, path = aux(grid, start, end, [], [])
    print(start, end, val, path)
    if val:
        return path


def aux(grid, pos, end, path, visited):
    path.append(pos)
    visited.append(pos)
    if pos == end:
        return visited, True, path
    i, j = pos
    n = len(grid)
    for next_pos in better_neighbours(i, j, n, end):
        vi, vj = next_pos
        if next_pos not in visited and grid[vi][vj] == 0:

            _, val, path = aux(grid, next_pos, end, path, visited)
            if val:
                return _, val, path
    return visited, False, path


def neighbours(i, j, n):
    v = []
    a = (1, 0), (-1, 0), (0, 1), (0, -1)
    for y, x in a:
        ni = i + y
        nj = j + x
        if 0 <= ni < n and 0 <= nj < n:
            v.append((ni, nj))
    random.shuffle(v)
    return v


def better_neighbours(i, j, n, end):
    ai, aj = end
    d = {"h": i - ai,
         "b": ai - i,
         "g": j - aj,
         "d": aj - j}
    k = list(d.keys())
    k.sort(key=lambda x: d[x], reverse=True)
    L = []
    for e in k:
        ii, jj = dic[e]
        if 0 <= i + ii < n and 0 <= j + jj < n:
            L.append((i + ii, j + jj))
    return L


dic = {"h": (-1, 0), "b": (1, 0), "g": (0, -1), "d": (0, 1)}
