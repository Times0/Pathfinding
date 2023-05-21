import heapq
import math

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
                color = DARKWHITE if self.grid[i][j] == 1 else LIGHTERBLACK
                if (i, j) == self.end:
                    color = PURPLE
                elif (i, j) == self.start:
                    color = RED
                s = c_size - 1 if self.grid[i][j] else c_size - 4
                pygame.draw.rect(win, color,
                                 [j * c_size + self.offset_x, i * c_size + self.offset_y, s, s])
        self.show_path(win)

    def handle_left_click(self, x, y):
        i = (y - self.offset_y) // self.cell_size
        j = (x - self.offset_x) // self.cell_size
        if i < 0 or i >= self.n or j < 0 or j >= self.n:
            return
        self.grid[i][j] = 1
        self.solve()

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
        start = Color("red")
        colors = list(start.range_to(Color("purple"), n + 1))
        c_size = self.cell_size

        pi, pj = None, None
        for x, (i, j) in enumerate(self.path):
            r, g, b = colors[x].rgb[0] * 255, colors[x].rgb[1] * 255, colors[x].rgb[2] * 255

            if pi is not None and pj is not None:
                pygame.draw.line(win, (r, g, b),
                                 ((pj + 0.5) * c_size + self.offset_x, (pi + 0.5) * c_size + self.offset_y),
                                 ((j + 0.5) * c_size + self.offset_x, (i + 0.5) * c_size + self.offset_y),
                                 int(30 / math.log2(n) * 1))
            pi, pj = i, j

    def reset(self):
        self.__init__(self.width, self.n)

    def solve(self):
        if self.start and self.end:
            self.path = a_star(self.grid, self.start, self.end)


# define heuristic function to estimate distance to goal
def heuristic(a, b):
    return abs(b[0] - a[0]) + abs(b[1] - a[1])


def a_star(grid, start, end):
    n, m = len(grid), len(grid[0])
    # define possible movements (up, down, left, right, diagonal)
    neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    # create set of visited nodes and heap queue for exploring nodes
    visited = set()
    heap = [(0, start)]
    came_from = dict()
    cost_so_far = dict()
    came_from[start] = None
    cost_so_far[start] = 0

    c = 0
    # loop until heap queue is empty or goal is reached
    while heap:
        c += 1
        # get node with the lowest cost from heap queue
        current_cost, current_node = heapq.heappop(heap)

        # check if goal is reached
        if current_node == end:
            break

        # check neighbors of current node
        for i, j in neighbors:
            neighbor = current_node[0] + i, current_node[1] + j
            ni, nj = neighbor

            # skip neighbor if it is outside the grid
            if ni < 0 or ni >= n or nj < 0 or nj >= m:
                continue

            new_cost = cost_so_far[current_node] + grid[ni][nj]

            # skip neighbor if it is not traversable or has already been visited
            if neighbor in visited or grid[ni][nj] == 1:
                continue

            # update cost and add neighbor to heap queue
            cost_so_far[neighbor] = new_cost
            priority = new_cost + heuristic(end, neighbor)
            heapq.heappush(heap, (priority, neighbor))
            visited.add(neighbor)
            came_from[neighbor] = current_node

    # build path from start to end using came_from dictionary
    path = []
    current = end
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()
    return path
